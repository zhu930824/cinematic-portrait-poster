# Typography

## Separate key art from copy

Generate text-free key art first. Add exact copy deterministically. Keep both files.

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

One level must dominate. Do not let title, face, tagline, and date compete equally.

## Title behaviors

- quiet suspension in negative space;
- vertical title aligned to a scene axis;
- title pressed against or interrupted by the motif;
- monumental title used as architecture;
- compact seal-like block, without fabricating a traditional seal;
- restrained bottom lockup for image-led work.

Use title-as-architecture only when the letterform meaning or structure belongs to the film.

## Font and copy rules

- Prefer user-supplied, licensed fonts.
- Record any system-font substitution.
- Verify simplified/traditional Chinese choice, punctuation, capitalization, names, and dates.
- Preserve safe margins of at least 7%; use 10% for uncertain crops.
- Do not stretch fonts. Adjust size, tracking, or line breaks.
- Keep taglines short. Treat unverified promotional copy as a placeholder.
- Use a real billing block only when exact approved copy is supplied.

## Compose script

Copy `assets/layout-example.json` and edit normalized positions. Coordinates are fractions of image width and height. Each text block supports:

```json
{
  "text": "片名",
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

`font_size` and `tracking` are fractions of poster width. A `font` path may be absolute or relative to the layout file. Inspect the result visually; automated placement cannot judge collisions with key art.
