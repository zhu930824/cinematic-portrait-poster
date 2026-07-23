#!/usr/bin/env python3
"""Overlay exact poster copy on text-free key art using a JSON layout."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageChops, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps


WINDOWS_FONT_CANDIDATES = (
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\simsun.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\arial.ttf"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--layout", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--final",
        action="store_true",
        help="Require an exact title and verified, non-placeholder cast-and-crew credits.",
    )
    return parser.parse_args()


def resolve_font(block: dict, layout_path: Path, size_px: int) -> ImageFont.FreeTypeFont:
    configured = block.get("font")
    candidates: list[Path] = []
    if configured:
        candidate = Path(configured)
        if not candidate.is_absolute():
            candidate = layout_path.parent / candidate
        candidates.append(candidate)
    candidates.extend(WINDOWS_FONT_CANDIDATES)
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size_px)
    raise FileNotFoundError(
        "No usable font found. Set each block's 'font' to a licensed TTF/OTF/TTC file."
    )


def tracked_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, tracking: int) -> int:
    widths = [draw.textlength(char, font=font) for char in text]
    return round(sum(widths) + max(0, len(text) - 1) * tracking)


def fit_font_to_width(
    block: dict,
    layout_path: Path,
    draw: ImageDraw.ImageDraw,
    size_px: int,
    tracking: int,
    image_width: int,
) -> ImageFont.FreeTypeFont:
    max_width = block.get("max_width")
    font = resolve_font(block, layout_path, size_px)
    if max_width is None:
        return font

    max_width_px = round(float(max_width) * image_width)
    lines = str(block["text"]).splitlines() or [""]
    while font.size > 8 and any(
        tracked_width(draw, line, font, tracking) > max_width_px for line in lines
    ):
        font = resolve_font(block, layout_path, font.size - 1)
    return font


def draw_horizontal(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: int,
    align: str,
    line_spacing: float,
) -> None:
    lines = text.splitlines() or [""]
    line_height = round(font.size * line_spacing)
    for line_index, line in enumerate(lines):
        line_width = tracked_width(draw, line, font, tracking)
        start_x = xy[0]
        if align == "center":
            start_x -= line_width // 2
        elif align == "right":
            start_x -= line_width
        cursor_x = start_x
        for char in line:
            draw.text((cursor_x, xy[1] + line_index * line_height), char, font=font, fill=fill)
            cursor_x += round(draw.textlength(char, font=font)) + tracking


def draw_vertical(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: int,
    align: str,
) -> None:
    chars = [char for char in text if char not in "\r\n"]
    step = font.size + tracking
    total_height = max(0, len(chars) * step - tracking)
    start_y = xy[1]
    if align == "center":
        start_y -= total_height // 2
    elif align == "right":
        start_y -= total_height
    for index, char in enumerate(chars):
        bbox = draw.textbbox((0, 0), char, font=font)
        char_width = bbox[2] - bbox[0]
        draw.text((xy[0] - char_width // 2, start_y + index * step), char, font=font, fill=fill)


def draw_character_layout(
    layer: Image.Image,
    block: dict,
    layout_path: Path,
    xy: tuple[int, int],
    fill: str,
    tracking: int,
    align: str,
    base_size: int,
) -> None:
    """Draw a single-line title with per-character scale, offset, rotation, and color."""
    chars = [char for char in str(block["text"]) if char not in "\r\n"]
    specs = block.get("character_layout")
    if not isinstance(specs, list) or not specs:
        raise ValueError("character_layout must be a non-empty array")

    normalized_specs = [
        specs[min(index, len(specs) - 1)] if isinstance(specs[min(index, len(specs) - 1)], dict) else {}
        for index in range(len(chars))
    ]
    fonts = [
        resolve_font(
            block,
            layout_path,
            max(8, round(base_size * float(spec.get("scale", 1.0)))),
        )
        for spec in normalized_specs
    ]
    measure = ImageDraw.Draw(layer)
    advances = [round(measure.textlength(char, font=font)) for char, font in zip(chars, fonts)]
    total_width = sum(advances) + max(0, len(chars) - 1) * tracking
    cursor_x = xy[0]
    if align == "center":
        cursor_x -= total_width // 2
    elif align == "right":
        cursor_x -= total_width

    for char, spec, font, advance in zip(chars, normalized_specs, fonts, advances):
        bbox = measure.textbbox((0, 0), char, font=font)
        pad = max(8, round(font.size * 0.18))
        glyph_size = (
            max(1, bbox[2] - bbox[0] + pad * 2),
            max(1, bbox[3] - bbox[1] + pad * 2),
        )
        glyph = Image.new("RGBA", glyph_size, (0, 0, 0, 0))
        glyph_draw = ImageDraw.Draw(glyph)
        glyph_draw.text(
            (pad - bbox[0], pad - bbox[1]),
            char,
            font=font,
            fill=spec.get("color", fill),
            stroke_width=max(0, round(float(spec.get("stroke_width", 0)) * layer.width)),
            stroke_fill=spec.get("stroke_color", spec.get("color", fill)),
        )
        rotation = float(spec.get("rotation", 0))
        if rotation:
            glyph = glyph.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True)
        offset_x = round(float(spec.get("dx", 0)) * layer.width)
        offset_y = round(float(spec.get("dy", 0)) * layer.width)
        layer.alpha_composite(glyph, (cursor_x + offset_x - pad, xy[1] + offset_y - pad))
        cursor_x += advance + tracking


def colorize_mask(mask: Image.Image, color: str) -> Image.Image:
    rgb = ImageColor.getrgb(color)
    colored = Image.new("RGBA", mask.size, (*rgb, 255))
    colored.putalpha(mask)
    return colored


def shifted_layer(layer: Image.Image, dx: int, dy: int) -> Image.Image:
    shifted = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    shifted.paste(layer, (dx, dy), layer)
    return shifted


def apply_split_chalk_effect(
    layer: Image.Image,
    strength: float,
    seed: int,
) -> Image.Image:
    bbox = layer.getbbox()
    if bbox is None:
        return layer

    x0, y0, x1, y1 = bbox
    text_width = x1 - x0
    text_height = y1 - y0
    shift = max(2, round(layer.width * strength))
    band_count = 5
    band_height = max(1, (text_height + band_count - 1) // band_count)
    shifted = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    offsets = (0, shift, -shift, shift // 2, -shift // 2)

    for band_index in range(band_count):
        band_y0 = y0 + band_index * band_height
        band_y1 = min(y1, band_y0 + band_height)
        if band_y0 >= band_y1:
            continue
        crop = layer.crop((x0, band_y0, x1, band_y1))
        shifted.alpha_composite(
            crop,
            (x0 + offsets[band_index % len(offsets)], band_y0),
        )

    mask = shifted.getchannel("A")
    mask_draw = ImageDraw.Draw(mask)
    cut_width = max(2, round(text_height * 0.018))
    for fraction in (0.28, 0.61):
        cut_x = round(x0 + text_width * fraction)
        mask_draw.line(
            (
                cut_x - round(text_height * 0.18),
                y1,
                cut_x + round(text_height * 0.28),
                y0,
            ),
            fill=0,
            width=cut_width,
        )

    rng = random.Random(seed)
    hole_count = max(24, round(text_width * text_height / 900))
    for _ in range(hole_count):
        hx = rng.randint(x0, max(x0, x1 - 1))
        hy = rng.randint(y0, max(y0, y1 - 1))
        radius_x = rng.randint(1, max(2, round(text_height * 0.018)))
        radius_y = rng.randint(1, max(2, round(text_height * 0.012)))
        mask_draw.ellipse(
            (hx - radius_x, hy - radius_y, hx + radius_x, hy + radius_y),
            fill=0,
        )

    shifted.putalpha(mask)
    return shifted


def apply_rain_canopy_effect(
    layer: Image.Image,
    strength: float,
    seed: int,
) -> Image.Image:
    """Turn a bold title skeleton into rain-cut, canopy-like custom lettering."""
    bbox = layer.getbbox()
    if bbox is None:
        return layer

    x0, y0, x1, y1 = bbox
    text_width = x1 - x0
    text_height = y1 - y0
    shift = max(2, round(layer.width * strength))

    shaped = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    crown_y = y0 + round(text_height * 0.34)
    shaped.alpha_composite(layer.crop((x0, y0, x1, crown_y)), (x0 - shift, y0))
    shaped.alpha_composite(
        layer.crop((x0, crown_y, x1, y1)),
        (x0 + shift // 2, crown_y),
    )

    mask = shaped.getchannel("A")
    mask_draw = ImageDraw.Draw(mask)
    rng = random.Random(seed)

    # Narrow vertical interruptions echo the rain field without destroying glyph recognition.
    channel_count = max(7, round(text_width / max(24, text_height * 0.16)))
    for index in range(channel_count):
        channel_x = round(x0 + (index + 0.55) * text_width / channel_count)
        channel_x += rng.randint(-max(1, shift), max(1, shift))
        channel_top = rng.randint(y0, max(y0, crown_y - 1))
        channel_bottom = rng.randint(crown_y, max(crown_y, y1 - 1))
        channel_width = rng.randint(1, max(2, round(text_height * 0.012)))
        mask_draw.line(
            (channel_x, channel_top, channel_x, channel_bottom),
            fill=0,
            width=channel_width,
        )

    # Small paired leaf-shaped voids make the lower edge feel like germinating rain.
    leaf_count = max(4, round(text_width / max(70, text_height * 0.42)))
    for index in range(leaf_count):
        leaf_x = round(x0 + (index + 0.5) * text_width / leaf_count)
        leaf_y = rng.randint(round(y0 + text_height * 0.58), max(round(y0 + text_height * 0.58), y1 - 2))
        leaf_w = max(2, round(text_height * 0.035))
        leaf_h = max(2, round(text_height * 0.018))
        mask_draw.ellipse(
            (leaf_x - leaf_w, leaf_y - leaf_h, leaf_x, leaf_y + leaf_h),
            fill=0,
        )
        mask_draw.ellipse(
            (leaf_x, leaf_y - leaf_h, leaf_x + leaf_w, leaf_y + leaf_h),
            fill=0,
        )

    shaped.putalpha(mask)
    return shaped


def apply_outline_echo_effect(
    layer: Image.Image,
    strength: float,
    echo_color: str,
) -> Image.Image:
    bbox = layer.getbbox()
    if bbox is None:
        return layer
    width = max(3, round(layer.width * strength))
    filter_size = width * 2 + 1
    if filter_size % 2 == 0:
        filter_size += 1
    expanded = layer.getchannel("A").filter(ImageFilter.MaxFilter(filter_size))
    outline = ImageChops.subtract(expanded, layer.getchannel("A"))
    echo = colorize_mask(outline, echo_color)
    result = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    result.alpha_composite(shifted_layer(echo, -width * 2, width * 2))
    result.alpha_composite(layer)
    return result


def apply_stroke_architecture_effect(
    layer: Image.Image,
    strength: float,
) -> Image.Image:
    bbox = layer.getbbox()
    if bbox is None:
        return layer
    x0, y0, x1, y1 = bbox
    text_height = y1 - y0
    shift = max(3, round(layer.width * strength))
    band_count = 4
    band_height = max(1, (text_height + band_count - 1) // band_count)
    offsets = (-shift, shift, -shift, shift)
    result = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    for index in range(band_count):
        band_y0 = y0 + index * band_height
        band_y1 = min(y1, band_y0 + band_height)
        if band_y0 >= band_y1:
            continue
        result.alpha_composite(
            layer.crop((x0, band_y0, x1, band_y1)),
            (x0 + offsets[index], band_y0),
        )
    return result


def apply_negative_window_effect(
    layer: Image.Image,
    strength: float,
    seed: int,
) -> Image.Image:
    bbox = layer.getbbox()
    if bbox is None:
        return layer
    x0, y0, x1, y1 = bbox
    text_width = x1 - x0
    text_height = y1 - y0
    mask = layer.getchannel("A")
    mask_draw = ImageDraw.Draw(mask)
    rng = random.Random(seed)
    window_count = max(1, min(4, round(text_width / max(1, text_height))))
    window_width = max(3, round(text_height * max(0.08, strength * 10)))
    for index in range(window_count):
        center_x = round(x0 + (index + 0.5) * text_width / window_count)
        center_y = round(y0 + text_height * rng.uniform(0.38, 0.62))
        if index % 2:
            mask_draw.rectangle(
                (
                    center_x - window_width // 2,
                    y0 + round(text_height * 0.16),
                    center_x + window_width // 2,
                    y1 - round(text_height * 0.12),
                ),
                fill=0,
            )
        else:
            radius_y = round(text_height * 0.24)
            mask_draw.ellipse(
                (
                    center_x - window_width,
                    center_y - radius_y,
                    center_x + window_width,
                    center_y + radius_y,
                ),
                fill=0,
            )
    result = layer.copy()
    result.putalpha(mask)
    return result


def apply_mirror_fade_effect(
    layer: Image.Image,
    strength: float,
) -> Image.Image:
    bbox = layer.getbbox()
    if bbox is None:
        return layer
    x0, y0, x1, y1 = bbox
    crop = layer.crop((x0, y0, x1, y1))
    mirrored = ImageOps.flip(crop)
    fade_height = mirrored.height
    fade = Image.new("L", mirrored.size, 0)
    fade_draw = ImageDraw.Draw(fade)
    opacity = max(24, min(180, round(255 * max(0.15, strength * 20))))
    for row in range(fade_height):
        alpha = round(opacity * (1 - row / max(1, fade_height - 1)))
        fade_draw.line((0, row, mirrored.width, row), fill=alpha)
    mirrored.putalpha(ImageChops.multiply(mirrored.getchannel("A"), fade))
    result = layer.copy()
    gap = max(2, round(layer.width * strength))
    result.alpha_composite(mirrored, (x0, y1 + gap))
    return result


def apply_title_effect(layer: Image.Image, block: dict) -> Image.Image:
    effect = block.get("effect")
    strength = float(block.get("effect_strength", 0.008))
    seed = int(block.get("effect_seed", 0))
    if effect == "split_chalk":
        return apply_split_chalk_effect(layer, strength, seed)
    if effect == "rain_canopy":
        return apply_rain_canopy_effect(layer, strength, seed)
    if effect == "outline_echo":
        return apply_outline_echo_effect(
            layer,
            strength,
            str(block.get("effect_color", "#8C8174")),
        )
    if effect == "stroke_architecture":
        return apply_stroke_architecture_effect(layer, strength)
    if effect == "negative_window":
        return apply_negative_window_effect(layer, strength, seed)
    if effect == "mirror_fade":
        return apply_mirror_fade_effect(layer, strength)
    if effect:
        raise ValueError(f"Unsupported effect: {effect}")
    return layer


def validate_block(block: dict, index: int) -> None:
    required = ("text", "x", "y", "font_size")
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Text block {index} is missing: {', '.join(missing)}")
    for key in ("x", "y", "font_size"):
        value = float(block[key])
        if key in ("x", "y") and not 0 <= value <= 1:
            raise ValueError(f"Text block {index} has {key} outside 0..1")
        if key == "font_size" and value <= 0:
            raise ValueError(f"Text block {index} has non-positive font_size")
    if "max_width" in block and not 0 < float(block["max_width"]) <= 1:
        raise ValueError(f"Text block {index} has max_width outside 0..1")
    if "line_spacing" in block and float(block["line_spacing"]) <= 0:
        raise ValueError(f"Text block {index} has non-positive line_spacing")
    ImageColor.getrgb(block.get("color", "#111111"))


def iter_blocks(layout: dict) -> Iterable[dict]:
    blocks = layout.get("text_blocks")
    if not isinstance(blocks, list):
        raise ValueError("Layout must contain a 'text_blocks' array")
    for index, block in enumerate(blocks):
        if not isinstance(block, dict):
            raise ValueError(f"Text block {index} must be an object")
        validate_block(block, index)
        yield block


def validate_final_copy(layout: dict) -> None:
    blocks = list(iter_blocks(layout))
    by_role = {str(block.get("role", "")): block for block in blocks}
    missing = [role for role in ("title", "verified_credits") if role not in by_role]
    if missing:
        raise ValueError(
            "Final poster layout is missing required role(s): " + ", ".join(missing)
        )

    forbidden = ("姓名", "片名", "PLACEHOLDER", "TBD", "20XX")
    for role in ("title", "verified_credits"):
        text = str(by_role[role]["text"]).strip()
        if not text:
            raise ValueError(f"Final poster {role} text is empty")
        if any(token.casefold() in text.casefold() for token in forbidden):
            raise ValueError(f"Final poster {role} still contains placeholder copy")

    sources = layout.get("credit_sources")
    if not isinstance(sources, list) or not any(
        isinstance(source, str) and source.strip() for source in sources
    ):
        raise ValueError(
            "Final poster layout requires a non-empty credit_sources list"
        )


def main() -> None:
    args = parse_args()
    layout = json.loads(args.layout.read_text(encoding="utf-8"))
    if args.final:
        validate_final_copy(layout)
    image = Image.open(args.background).convert("RGBA")
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for block in iter_blocks(layout):
        font_size = max(8, round(float(block["font_size"]) * width))
        tracking = round(float(block.get("tracking", 0)) * width)
        font = fit_font_to_width(block, args.layout, draw, font_size, tracking, width)
        xy = (round(float(block["x"]) * width), round(float(block["y"]) * height))
        color = block.get("color", "#111111")
        align = block.get("align", "left")
        if align not in {"left", "center", "right"}:
            raise ValueError(f"Unsupported align: {align}")
        orientation = block.get("orientation", "horizontal")
        effect = block.get("effect")
        character_layout = block.get("character_layout")
        if effect or character_layout:
            text_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
            layer_draw = ImageDraw.Draw(text_layer)
            if character_layout:
                draw_character_layout(
                    text_layer,
                    block,
                    args.layout,
                    xy,
                    color,
                    tracking,
                    align,
                    font_size,
                )
            elif orientation == "vertical":
                draw_vertical(
                    layer_draw,
                    xy,
                    str(block["text"]),
                    font,
                    color,
                    tracking,
                    align,
                )
            else:
                draw_horizontal(
                    layer_draw,
                    xy,
                    str(block["text"]),
                    font,
                    color,
                    tracking,
                    align,
                    float(block.get("line_spacing", 1.28)),
                )
            text_layer = apply_title_effect(text_layer, block)
            image.alpha_composite(text_layer)
        elif orientation == "vertical":
            draw_vertical(draw, xy, str(block["text"]), font, color, tracking, align)
        else:
            draw_horizontal(
                draw,
                xy,
                str(block["text"]),
                font,
                color,
                tracking,
                align,
                float(block.get("line_spacing", 1.28)),
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() in {".jpg", ".jpeg"}:
        image.convert("RGB").save(args.output, quality=95)
    else:
        image.save(args.output)
    print(f"Saved poster: {args.output} ({width}x{height})")


if __name__ == "__main__":
    main()

