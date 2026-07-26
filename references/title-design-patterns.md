# Title design patterns

Use this reference when the film title must act as image, structure, or metaphor rather than ordinary display type.

## Contents

1. Research synthesis
2. Film-title fidelity
3. Title composition card
4. Title-image contract
5. Semantic mechanism gate
6. Glyph sourcing and controlled variables
7. Text reserve
8. Structural operations
9. Script controls
10. Native-title prompt controls
11. Quality checks

## Research synthesis

Combine two durable bodies of practice:

- Story-first authored film posters treat the title as a place where the story happens, not as a label added afterward.
- Contemporary text-material editorial posters require one observable material fact, one title action, and an active quiet field.

Use the combined principles below:

- derive the title mechanism from the film's dramatic core;
- let figures, gaps, landscape, or time occupy its strokes;
- split a phrase by meaning when different words represent different worlds;
- change character scale to express power, historical pressure, distance, or isolation;
- make solid and empty strokes carry doubles, absence, concealment, or memory;
- derive texture from the film's rain, paper, earth, cloth, architecture, work, or violence;
- use one hero evidence field, one title action, and at most one interruptor;
- make empty space hold readable copy, distance, silence, pressure, or scale;
- preserve a sensory attraction in material, light, crop, or color before the title is decoded;
- keep the exact title readable after transformation.

These principles are supported by Huang Hai's discussion of turning `乱` into a stage curtain and splitting `草木人间` into natural and human realms, as well as analysis of figures embedded in the strokes of `影` and `黄金时代`:

- https://www.jff.jpf.go.jp/article/huanghai/
- https://pdf.hanspub.org/arl20230400000_88571438.pdf

The one-evidence, one-title-action, text-reserve, and beauty-engine rules were adapted from the public `oriental-editorial-poster` skill:

- https://github.com/dacnay816y62-hub/fantasy-dongfang-jianyuehaibao

Do not copy those compositions. Change the film, spatial logic, material, motif relationship, and title behavior.

## Film-title fidelity

Do not shorten, paraphrase, or rewrite an official film title merely to make the design easier. A film poster must contain the exact approved title.

- Refine hierarchy through line breaks, scale, grouping, or semantic zones.
- Use an abbreviated campaign title only when the user supplies or approves it.
- If an approved shorthand is used, keep the full official title elsewhere in the final poster.
- Keep credits and factual copy deterministic. Do not ask the image model to generate final billing.

Choose the H1 production route using `image-native-title-workflow.md`. An accepted native title must be generated inside the poster plate, checked character by character, and left unobscured. A deterministic title must remain editable. Never hide a wrong generated title under a correct overlay.

## Title composition card

Before choosing an effect, record:

| Field | Requirement |
|---|---|
| Film core | One dramatic proposition or emotional conflict |
| Title strategy | Edge monument, quiet catalogue, split inscription, type specimen, object label, text field, or another film-specific structure |
| Primary evidence | One object, material, trace, gesture, space, or weather event |
| Material fact | One observable trait: fold, fracture, fiber, reflection, weight, stain, weave, edge, shadow, or residue |
| Semantic pivot | How that trait changes the meaning of the title |
| Title role | Frame, mask, threshold, specimen, trace, interruption, label, architecture, or counterweight |
| Image role | Evidence, field, crop, trace, object, atmosphere, or passage |
| Shared boundary | The exact edge, axis, opening, horizon, contour, light band, or material transition used by both title and image |
| Mutual change | State separately how the title changes the image and how the image changes the title |
| Glyph skeleton | Licensed display face, sourced calligraphic sample, Song/Ming, or Heiti |
| Controlled variables | At least two visible variables beyond font choice |
| Title action | One verb: contain, interrupt, reflect, press, split, suspend, erode, bind, measure, or reveal |
| Dominant axis | Vertical, horizontal, diagonal, radial, or edge pressure |
| Title field | A planned normalized rectangle or structural path established before key-art generation |
| Collision rule | What the title may cross, touch, mask, frame, or never cover |
| Text reserve | Low, medium, or high; name the exact content it holds |
| Interruptor | Optional single line, edge, thread, waterline, crack, or color event |
| Palette | Source-led neutrals plus at most one decisive accent |
| Beauty engine | Material, light, crop pressure, rhythm, or color tension that works before the title is read |
| Post-view reward | The relationship that becomes clearer after watching the film |
| Removal test | What balance, direction, passage, or meaning collapses when the title is hidden |
| Swap test | Why another film title cannot occupy the same structure unchanged |
| Legibility test | How exact characters remain readable at thumbnail and full size |

## Title-image contract

Design the title and key art in the same planning pass. Do not generate a complete illustration and later search for unused space.

Require a two-way relationship:

1. **Title changes image** — the title must alter at least one of crop, negative space, focal balance, scale, passage, horizon, silhouette, or reading path.
2. **Image changes title** — the motif must alter at least one of contour, stroke visibility, material, spacing, baseline, color, fill, or character scale.

Define a `shared_boundary` before generation. It may be a doorway edge, rain line, orbit, wall seam, garment fold, field marking, reflection plane, shadow edge, or another film-evidenced structure. Both the title and image must respond to it.

Define a `title_field` before generation:

```json
{
  "x": 0.08,
  "y": 0.12,
  "width": 0.52,
  "height": 0.34
}
```

The field is a compositional footprint, not a generic blank rectangle. Key art must create the pressure, opening, edge, light, or counterweight that makes this location necessary. For a path-based or edge-cropped title, use the rectangle as its safe envelope and describe the actual path in `shared_boundary`.

Reject the design when:

- the same title block can move to another corner without changing the poster;
- the title overlaps the image but neither changes the other;
- the image is already compositionally complete without the declared title field;
- the title depends only on a decorative font or texture preset;
- the shared boundary has no film evidence.

## Semantic mechanism gate

Develop three structurally different title mechanisms alongside the three poster concepts. For each, state:

1. the material fact;
2. the semantic pivot;
3. the title action;
4. why the mechanism cannot be swapped unchanged onto an unrelated film;
5. the text reserve and its job;
6. the beauty engine.

Score each mechanism from 1–5:

| Criterion | Passing signal |
|---|---|
| Story inevitability | The action follows from this film rather than a typography trend |
| Semantic surprise | The title gains a second reading without becoming a rebus |
| Formal beauty | The image remains desirable before the title is decoded |
| Visual economy | One title action is enough |
| Legibility | The approved title remains exact at full size and thumbnail size |
| Originality | It does not repeat the last two title structures or a known poster trick |

Reject a mechanism when `Story inevitability`, `Formal beauty`, or `Legibility` scores below 4. Reject it when the same treatment works unchanged after replacing the title with a random noun.

Hide the title mentally for one second. If the remaining visual has no material, light, rhythm, or emotional pull, the concept is a diagram rather than a poster. Keep the semantic pivot but rebuild the image language.

## Glyph sourcing and controlled variables

Choose the glyph skeleton in this order:

1. an explicitly supplied licensed title treatment or font;
2. a traceable, rights-compatible calligraphic character sample used as an anchor;
3. a licensed Song/Ming or Heiti skeleton;
4. a system fallback with verified Chinese coverage.

When using sampled calligraphy, record the source page, script, attribution when available, and selected character. Preserve the recognizable skeleton and natural stroke logic. Do not ask an image model to invent a named calligrapher's hand.

Make design intent visible through at least two controlled variables:

- scale contrast between characters or semantic word groups;
- baseline or vertical-position shift;
- deliberate tracking compression or expansion;
- stroke crop or edge pressure;
- solid/outline contrast;
- selected-stroke material fill;
- color or opacity hierarchy;
- orientation or axis tension;
- one evidence-led interruption;
- one meaningful line break or semantic split.

Font family alone does not count. Applying the same texture to every character counts as one variable, not several. Do not stretch glyphs; change size, tracking, layout, or construct individual characters instead.

## Text reserve

Reserve calm space deliberately:

| Level | Area | Use |
|---|---:|---|
| Low | 12–22% | Short title tightly fused with the motif; minimal copy |
| Medium | 25–38% | Default theatrical poster; title plus compact verified credits |
| High | 40–55% | Long title, bilingual copy, festival information, or restrained catalogue treatment |

The reserve is not empty background. State which title, credit, tagline, or visual pause it supports. Do not choose high reserve merely to make a short title appear tasteful.

## Choose one structural operation

| Operation | Story use | Construction |
|---|---|---|
| Title monument | history, fate, epic scale | make the title the dominant mass; reduce figures to witnesses |
| Stroke architecture | complex relationships, social pressure | separate broad stroke bands into passages, ledges, or barriers |
| Negative window | secrecy, absence, hidden identity | remove one or two purposeful openings from the title |
| Material crop-window | craft, place, evidence, inheritance | fill one selected character or stroke with one traceable material image |
| Single interruption | fracture, bond, censorship, threshold | let one fold, thread, crack, rule, or waterline cut the title once |
| Relief press | memory, document, institutional pressure | press the title shallowly into a story-grounded paper, wall, metal, or cloth field |
| Semantic split | nature/human, past/present, home/world | assign different zones or materials to meaningful word groups |
| Scale rhythm | unequal power, growth, ensemble tension | vary individual character scale and baseline |
| Outline echo | memory, doubles, afterimage | pair a solid title with displaced outlines |
| Mirror fade | water, reflection, death, alternate reality | reflect the title across a story-grounded boundary |
| Material title | sport, rain, ash, thread, paper, repair | alter edges and gaps using a material evidenced by the film |
| Quiet catalogue | intimate drama, craft, evidence-led story | keep the title calm while one object or material remains dominant |
| Split inscription | archives, writing, investigation | divide the title into columns, strips, notes, or evidence labels |

Use one structural operation and, at most, one compatible material treatment. Do not stack effects merely to look designed.

Rotate structures in a series. Do not use a giant title, image-inside-type, shadow, or negative window in more than two consecutive posters.

## Script controls

`compose_poster.py` supports:

- `split_chalk`: fractured bands and athletic chalk erosion;
- `rain_canopy`: rain channels, canopy separation, and leaf voids;
- `stroke_architecture`: broad displaced stroke bands;
- `negative_window`: automatic openings or precise `effect_windows`;
- `interrupt_cut`: one controlled line crossing the title; use `effect_position` and `effect_angle`;
- `relief_press`: shallow highlight-and-shadow pressure; use only with a plausible surface;
- `outline_echo`: displaced outline afterimages; use `effect_color`;
- `mirror_fade`: a fading reflected title;
- `character_layout`: per-character scale, offset, rotation, color, opacity, optional stroke, and optional `fill_image`.

Per-character material example:

```json
{
  "text": "电影片名",
  "role": "title",
  "x": 0.5,
  "y": 0.42,
  "font_size": 0.12,
  "color": "#171411",
  "align": "center",
  "tracking": -0.012,
  "effect": "outline_echo",
  "effect_strength": 0.006,
  "effect_color": "#B64032",
  "character_layout": [
    {"scale": 1.25, "dy": -0.02},
    {
      "scale": 0.78,
      "dy": 0.045,
      "fill_image": "material-detail.png",
      "fill_crop": [0.1, 0.0, 0.9, 1.0],
      "fill_position": [0.45, 0.5],
      "stroke_width": 0.002,
      "stroke_color": "#171411"
    },
    {"scale": 1.05, "rotation": -3},
    {"scale": 0.9, "dx": -0.01, "dy": 0.025}
  ]
}
```

Precise single-window example:

```json
{
  "effect": "negative_window",
  "effect_windows": [
    {"shape": "rectangle", "x": 0.62, "y": 0.48, "width": 0.12, "height": 0.58}
  ]
}
```

Single-interruption example:

```json
{
  "effect": "interrupt_cut",
  "effect_strength": 0.006,
  "effect_position": [0.5, 0.56],
  "effect_angle": -8
}
```

`dx`, `dy`, and `stroke_width` are fractions of poster width. `fill_crop` is a normalized box inside the source image. Repeat the last `character_layout` object when the title contains more characters than the array.

## Native-title prompt controls

For Native expressive or Native controlled, specify all of the following in the image prompt:

- exact Chinese title in quotation marks near the beginning;
- exact character count and order;
- glyph skeleton: sourced calligraphic sample, Song/Ming, or Heiti;
- title role: frame, mask, threshold, specimen, trace, interruption, or label;
- dominant axis and approximate title field;
- per-character scale or baseline rhythm when meaningful;
- one material-specific title action;
- one evidence-title relationship;
- the shared boundary and both directions of mutual change;
- the planned title field and collision rule;
- at least two controlled variables beyond font choice;
- at most two text zones;
- no pseudo-Chinese, question marks, substitutions, duplicated title, or invented microtype.

Do not use “creative Chinese font” as an instruction. Describe visible stroke weight, spacing, contour, crop, texture, material, and interaction.

If the generated H1 is wrong, regenerate with fewer text zones and a clearer title field. After two failures, switch to Deterministic exact and remove the incorrect generated title from the source plate.

## Quality checks

- At thumbnail size, the title must contribute one clear mass or axis.
- At full size, the transformation must reveal one story relationship.
- The title uses one action, not a stack of unrelated effects.
- The primary evidence shows one observable material fact.
- The text reserve has a named job.
- The poster remains visually desirable when the title is mentally hidden.
- Removing the title must weaken the composition.
- The title changes the image and the image changes the title in separately describable ways.
- A film-evidenced shared boundary is visible.
- The key art anticipates the declared title field rather than leaving a generic empty corner.
- At least two controlled variables are visible beyond font choice.
- Replacing the title with another film name must break the concept.
- Distortion must not create a wrong character or uncertain title reading.
- A native title has been checked character by character and contains no question mark, false radical, repeated title, or pseudo-character.
- A wrong native title was regenerated rather than covered by post-added text.
- The official film title has not been shortened without approval.
- A series does not repeat the same title mechanism automatically.
- Credits must remain typographically calm; expressive treatment belongs mainly to the title.
