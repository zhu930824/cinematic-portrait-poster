# Typography

## Choose title production before composing

Read `image-native-title-workflow.md` when the title must feel generated inside the image rather than added afterward.

Every Standard or Series poster must contain the exact film title and a verified cast-and-crew block. A text-free key-art file is an intermediate asset, not the final poster.

Choose one route:

- **Native expressive**: generate a 1–4 character Chinese H1 as part of the image for maximum title-image fusion.
- **Native controlled**: generate the H1 inside a calmer finished poster plate, then add factual copy deterministically.
- **Deterministic exact**: generate text-free key art and build the title with `compose_poster.py`.

Default to Native controlled when the user asks for expressive Chinese typography, fantasy text treatment, image-native titles, or consistency with `oriental-editorial-poster`. Default to Deterministic exact for long titles, legal production, repeated adaptations, or after two failed native-title attempts.

Never ask the image model to render cast and crew lists, release dates, billing blocks, legal lines, ratings, awards, laurels, or logos.

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

Keep the exact official title in every route. In a native route, state the exact H1 near the start of the prompt and reject any wrong character rather than covering it with a conventional title. In a deterministic route, typeset exact letters after image generation. Reject a layout when the title can move to an arbitrary corner without weakening the composition.

When font selection alone cannot express the film, read `title-design-patterns.md`. Reconstruct the title through scale, position, negative space, outline, reflection, or material logic. Preserve legibility; expressive typography is a narrative structure, not arbitrary distortion.

Do not import editorial-cover title shortening into theatrical film titles. Keep the exact approved film title. Refine it through line breaks, scale groups, semantic zones, or secondary campaign copy instead of deleting official words.

Choose one primary evidence field, one title action, and at most one interruptor. Reserve low (12–22%), medium (25–38%), or high (40–55%) calm space and state what exact title, credit, copy, or emotional pause occupies it.

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

### Credit architecture

Treat credits as the poster's factual secondary composition, not export residue. When the image has sufficient reserve, build up to three groups:

1. **creator line** — director, writer, or “a film by” equivalent near an existing architectural edge, quiet field, or title axis;
2. **principal-cast rail** — principal cast or voice performers as a deliberate horizontal or vertical name rhythm;
3. **compact verified credits** — role-labeled director, writer, music, and principal cast in the final information zone.

All groups must come from `credit_sources`. Use roles such as `creator_credit`, `verified_cast`, and `verified_credits`; `verified_credits` remains mandatory for `--final`.

- Plan these zones in the image prompt even when factual text is added later.
- Share a baseline, centerline, edge, window rail, horizon, or title axis with the visual system.
- Use scale contrast: creator line or cast rail may be more visible than the compact credit block, but neither may compete with the H1.
- Do not place every name in one tiny two-line block merely to pass validation.
- Do not fabricate contractual billing order. When no approved legal billing is supplied, label roles and preserve source order.
- Avoid decorative pseudo-billing, condensed all-caps imitations, logos, union marks, and production-company lines unless exact approved copy is supplied.
- At full size, every factual group must be readable. At thumbnail size, it may resolve as a calm rail or block that completes the poster geometry.

## Font and copy rules

- Prefer user-supplied, licensed fonts.
- Record any system-font substitution.
- When using sourced calligraphy, record the source, script, attribution when available, and selected character. Preserve the source skeleton.
- Without reliable calligraphy samples, use Song/Ming or Heiti. Do not request generic synthetic brush lettering.
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

Additional structural effects are documented in `title-design-patterns.md`: `stroke_architecture`, `negative_window`, `interrupt_cut`, `relief_press`, `outline_echo`, and `mirror_fade`. Use `effect_windows` for one precise negative-space opening. Use `character_layout` for per-character scale, offset, rotation, color, opacity, stroke, or a traceable `fill_image`. Combine no more than one structural effect with one story-grounded material treatment.

Export delivered posters with `compose_poster.py --final`. The final-copy check requires either a `title` block or a validated `image_native_title` record, plus `verified_credits`, a non-empty `credit_sources` array, and no common placeholder tokens.
