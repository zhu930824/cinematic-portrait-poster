# Typography

## Separate key art from copy

Generate text-free key art first. Add exact copy deterministically. Keep both files.

Every Standard or Series poster must contain the exact film title and a verified cast-and-crew block. A text-free key-art file is an intermediate asset, not the final poster.

Never ask the image model to render:

- long Chinese titles;
- cast and crew lists;
- release dates that must be accurate;
- billing blocks, legal lines, ratings, awards, laurels, or logos.

## Hierarchy

Use no more than five functional levels:

1. Chinese title;
2. optional English title;
3. tagline;
4. date or campaign message;
5. verified credits.

The title must dominate or co-dominate with the primary motif. Credits remain subordinate but readable. Do not let title, face, tagline, date, and credits compete equally.

## Integrate the title

Plan the title while designing the image, not after generating it. Reserve its space in the key-art prompt and make it participate through one or more of:

- sharing the scene's main axis;
- completing or interrupting the motif's contour;
- acting as a threshold, field line, wall, trail, or horizon;
- echoing a story-grounded material;
- creating deliberate compression, balance, or tension with the subject;
- becoming architecture only when the letterform structure belongs to the film.

Keep exact letters deterministic. Do not ask the image model to render the title. Reject a layout when the title can move to an arbitrary corner without weakening the composition.

When font selection alone cannot express the film, read `title-design-patterns.md`. Reconstruct the title through scale, position, negative space, outline, reflection, or material logic. Preserve legibility; expressive typography is a narrative structure, not arbitrary distortion.

## Title behaviors

- quiet suspension in active negative space;
- vertical title aligned to a scene axis;
- title pressed against or interrupted by the motif;
- monumental title used as architecture;
- compact seal-like block, without fabricating a traditional seal;
- restrained bottom lockup only when its baseline completes the image geometry.

Use title-as-architecture only when the letterform meaning or structure belongs to the film.

## Credits

- Require verified names and roles before final export.
- Include at minimum the director and principal cast; include the screenwriter when reliably available.
- Preserve supplied billing order. Do not infer contractual prominence.
- Use role labels when a compact legal billing block is not supplied, for example `导演：…  编剧：…` and `主演：…`.
- Do not invent producers, companies, presenters, release dates, legal lines, or union marks.
- Keep credits inside the safe area with sufficient contrast at full resolution.
- Use `max_width` in the layout JSON so long lines shrink to fit rather than run off-canvas.
- Change the approved credit block's role to `verified_credits`; keep `verified_credits_placeholder` only in drafts.
- Record URLs or `user-supplied approved copy` in the layout's top-level `credit_sources` array.

## Font and copy rules

- Prefer user-supplied, licensed fonts.
- Record any system-font substitution.
- Verify simplified/traditional Chinese choice, punctuation, capitalization, names, and dates.
- Preserve safe margins of at least 7%; use 10% for uncertain crops.
- Do not stretch fonts. Adjust size, tracking, or line breaks.
- Keep taglines short. Treat unverified promotional copy as a placeholder.
- Use a real production billing block only when exact approved copy is supplied. Otherwise use a factual compact credit block with explicit role labels.

## Compose script

Copy `assets/layout-example.json` and edit normalized positions. Coordinates are fractions of image width and height. Each text block supports:

```json
{
  "text": "电影片名",
  "role": "title",
  "x": 0.82,
  "y": 0.12,
  "font_size": 0.055,
  "color": "#161412",
  "align": "center",
  "orientation": "vertical",
  "tracking": 0.012,
  "font": null
}
```

`font_size`, `tracking`, and optional `max_width` are fractions of poster width. `line_spacing` is a multiplier of font size. A `font` path may be absolute or relative to the layout file. Inspect the result visually; automated placement cannot judge collisions with key art.

Use `"effect": "split_chalk"` only when fractured, athletic, handmade title lettering belongs to the story. Optional `effect_strength` controls band displacement and `effect_seed` keeps the erosion deterministic. Treat the effect as custom lettering, not a universal preset.

Use `"effect": "rain_canopy"` when rain, shelter, growth, or forest protection is central to the story. It divides a bold title into canopy and trunk zones, cuts narrow rain channels through the strokes, and introduces small leaf-like voids near the lower edge. Use it with restrained displacement so the exact title remains legible.

Additional structural effects are documented in `title-design-patterns.md`: `stroke_architecture`, `negative_window`, `outline_echo`, and `mirror_fade`. Use `character_layout` for per-character scale, offset, rotation, color, and stroke. Combine no more than one structural effect with one story-grounded material treatment.

Export delivered posters with `compose_poster.py --final`. The final-copy check requires `title` and `verified_credits` roles, a non-empty `credit_sources` array, and no common placeholder tokens.
