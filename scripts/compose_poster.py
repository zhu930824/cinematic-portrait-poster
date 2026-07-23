#!/usr/bin/env python3
"""Overlay exact poster copy on text-free key art using a JSON layout."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageColor, ImageDraw, ImageFont


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


def draw_horizontal(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: int,
    align: str,
) -> None:
    lines = text.splitlines() or [""]
    line_height = round(font.size * 1.28)
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


def main() -> None:
    args = parse_args()
    layout = json.loads(args.layout.read_text(encoding="utf-8"))
    image = Image.open(args.background).convert("RGBA")
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for block in iter_blocks(layout):
        font_size = max(8, round(float(block["font_size"]) * width))
        tracking = round(float(block.get("tracking", 0)) * width)
        font = resolve_font(block, args.layout, font_size)
        xy = (round(float(block["x"]) * width), round(float(block["y"]) * height))
        color = block.get("color", "#111111")
        align = block.get("align", "left")
        if align not in {"left", "center", "right"}:
            raise ValueError(f"Unsupported align: {align}")
        if block.get("orientation", "horizontal") == "vertical":
            draw_vertical(draw, xy, str(block["text"]), font, color, tracking, align)
        else:
            draw_horizontal(draw, xy, str(block["text"]), font, color, tracking, align)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() in {".jpg", ".jpeg"}:
        image.convert("RGB").save(args.output, quality=95)
    else:
        image.save(args.output)
    print(f"Saved poster: {args.output} ({width}x{height})")


if __name__ == "__main__":
    main()

