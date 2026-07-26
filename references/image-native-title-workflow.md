# Image-native title workflow

Use this reference when a Chinese film title must feel born inside the image rather than added as ordinary display type.

The workflow adapts transferable title-production rules from the public
[`oriental-editorial-poster`](https://github.com/dacnay816y62-hub/fantasy-dongfang-jianyuehaibao)
skill, inspected at commit `6948d6b8c6c64c7de794597871d9c1cbb61d8898`. Preserve the current skill's film-title fidelity and verified-credit requirements.

## Contents

1. Production routes
2. A/B/C title treatments
3. Native-title concept gate
4. Title prompt contract
5. Character and font logic
6. Verification and regeneration
7. Exact-copy finishing
8. Layout schema

## Production routes

Choose one route before writing the image prompt.

| Route | Use when | Main title | Factual copy |
|---|---|---|---|
| Native expressive | 1–4 Chinese characters, teaser or festival art, maximum image-title fusion | generated inside the image pass | add verified credits deterministically |
| Native controlled | short or medium title, finished poster, calmer hierarchy | generated inside the image pass with a clear title field | add verified credits deterministically |
| Deterministic exact | long title, many formats, legal production, accessibility, or repeated title failure | typeset with `compose_poster.py` | typeset deterministically |

Default to **Native controlled** for a 1–4 character Chinese film title when the user asks for expressive, material, fantasy, editorial, or image-integrated typography. Use **Native expressive** when the user explicitly prioritizes experimental title form. Use **Deterministic exact** when factual precision or repeatable adaptation is more important.

Do not generate cast, crew, dates, legal lines, ratings, awards, or logos inside the image model. The image-native route applies to the main title and, optionally, one short non-factual subtitle or English tag only.

## A/B/C title treatments

Use these treatments to force structural variation. They are title roles, not fixed layouts.

| Treatment | Evidence behavior | Title behavior |
|---|---|---|
| A — Evidence intervention | film-grounded map, projection, object trace, garment, weather record, document, print, or historical fragment enters the page | title behaves as inscription, specimen, crop, label, or one evidenced interruption |
| B — Single evidence | one object, material, gesture, costume, weather trace, or location fragment is the visual boss | title stays controlled and gains meaning through alignment, pressure, reflection, edge, or one material action |
| C — Title structure | the title carries more of the composition | title becomes a readable frame, mask, crop-window, relief, section, threshold, or structural rail without turning the entire world into a literal glyph |

For three poster concepts, normally make one concept from each treatment. Change the evidence role, title role, dominant axis, crop logic, and reading path between them. Select the strongest treatment after the semantic mechanism gate; do not automatically prefer C merely because it looks more typographic.

For a single final poster, record the selected treatment as `A`, `B`, or `C` in working notes and in `image_native_title.title_treatment`.

## Native-title concept gate

Before selecting the poster direction, develop six genuinely different title mechanisms privately. Each candidate must state:

1. material fact;
2. semantic pivot;
3. title mechanism;
4. why the mechanism cannot move unchanged to an unrelated film;
5. title role: frame, mask, specimen, threshold, interruption, trace, or label;
6. text reserve and its exact job;
7. beauty engine.

Score each candidate from 1–5 for:

- story inevitability;
- material inevitability;
- semantic surprise;
- formal beauty;
- visual economy;
- exact-title legibility;
- distance from the last five outputs in title mechanism, ground material, production process, dominant hue, and accent family.

Select only a mechanism averaging at least 4, with story inevitability, formal beauty, and legibility each at least 4. Carry the strongest three mechanisms into the three poster concepts.

Reject a candidate when:

- the title is merely large;
- a generic font effect could be reused after replacing the film name;
- the title becomes a literal object-shaped rebus;
- the image becomes visually empty when the title is hidden;
- multiple effects compete;
- an arbitrary brush font, seal, ink splash, or grunge layer is doing the cultural work.

## Title prompt contract

For Native expressive or Native controlled routes, place this information near the beginning of the image prompt:

```text
Create one finished vertical theatrical poster with integrated Chinese typography.
Render the exact main Chinese film title clearly: "准确片名".
The title must contain exactly these characters, in this order, with no substitutions,
extra characters, question marks, pseudo-Chinese marks, or repeated title.
```

Then specify visible construction:

- title role in the composition;
- image role and the exact boundary shared with the title;
- how the title changes crop, balance, passage, or reading path;
- how the image changes title contour, material, spacing, baseline, or visibility;
- horizontal, vertical, diagonal, radial, or edge-pressure axis;
- normalized title field or safe envelope and its crop pressure;
- collision rule: what the title may cross, touch, frame, mask, or never cover;
- solid, outline, sampled glyph, Song/Ming, Heiti, or sourced calligraphic skeleton;
- at least two controlled variables beyond font choice, such as character scale, baseline rhythm, tracking, stroke crop, outline/solid contrast, selected-stroke material, or semantic line break;
- one material-specific title action;
- one evidence-title relationship;
- maximum of two title/copy zones;
- required quiet-space percentage;
- palette and material proof.

Finish with:

```text
Typography must be integrated into the image, not pasted over a finished illustration.
Use one visual boss, one title action, and at most one precise interruptor.
Do not invent microtext, dates, institutions, credits, seals, QR codes, logos, or metadata.
```

Do not ask for “beautiful calligraphy,” “Chinese-style font,” or an artist's style. Describe the glyph skeleton, weight, spacing, crop, material, and semantic action as visible pixels.

## Character and font logic

- Preserve the exact official film title. Do not shorten it to improve generation unless the user approves an alternate campaign title.
- Prefer 1–4 Chinese characters for native generation. For longer titles, use a calmer native field or the deterministic route.
- If a real calligraphy source is used, record the source page, script, attribution when available, and selected character. Preserve its skeleton; do not ask the model to invent a named calligrapher's hand.
- Without reliable samples, specify Song/Ming or Heiti skeletons. Do not use synthetic brush lettering as a fallback.
- Design intent must appear through at least two controlled variables: scale contrast, stroke crop, baseline shift, vertical/horizontal tension, selected-stroke material, repeated micro-title, or deliberate title reserve.
- A selected-stroke material window counts as the one title action. Do not combine it with reflection, shadow, fracture, and outline merely because they are available.
- Keep English titles and subtitles secondary. They may support rhythm but cannot compete with the Chinese H1.

## Verification and regeneration

Inspect the native title at full size and thumbnail size.

Verify:

- every character;
- character order;
- simplified or traditional variant;
- punctuation and spacing;
- no question mark, false radical, duplicated stroke group, pseudo-character, or accidental second title;
- title-motif relationship;
- visible two-way dependence between title and image;
- the declared shared boundary and collision rule;
- at least two controlled variables beyond font choice;
- title legibility at thumbnail size.

If the H1 is wrong:

1. do not cover it with a conventional title;
2. simplify the prompt around the exact H1;
3. remove optional generated copy;
4. reduce the number of title effects;
5. regenerate once with the title isolated in a clearer field;
6. regenerate a second time or switch to Deterministic exact if the error persists.

Use a deterministic correction only after switching routes explicitly. Do not leave a wrong native title beneath an exact overlay.

## Exact-copy finishing

For Native expressive and Native controlled:

1. keep the generated title-bearing poster plate;
2. add verified credits, dates, and factual copy with `compose_poster.py`;
3. do not add a second title block;
4. keep exact factual typography calm;
5. deliver the generated title plate and the final credit-composed poster.

For Deterministic exact:

1. generate text-free key art;
2. construct the exact title through one story-grounded structural operation;
3. add verified credits;
4. deliver both key art and final poster.

## Layout schema

When the main title already exists and has been checked in the generated poster plate, omit the `title` text block and record:

```json
{
  "image_native_title": {
    "text": "准确片名",
    "validated": true,
    "validation_method": "full-size visual inspection",
    "production_mode": "native-controlled",
    "title_treatment": "B",
    "generation_attempts": 1,
    "shared_boundary_verified": true,
    "mutual_change_verified": true
  },
  "credit_sources": [
    "https://example.com/verified-film-source"
  ],
  "text_blocks": [
    {
      "text": "导演：姓名　主演：姓名 / 姓名",
      "role": "verified_credits",
      "x": 0.5,
      "y": 0.92,
      "font_size": 0.012
    }
  ]
}
```

`compose_poster.py --final` accepts either:

- an exact `title` text block; or
- a validated `image_native_title` record.

It always requires `verified_credits` and a non-empty `credit_sources` array.
