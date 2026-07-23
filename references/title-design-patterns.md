# Title design patterns

Use this reference when the film title must act as image, structure, or metaphor rather than ordinary display type.

## Research translation

The durable lesson from authored Chinese poster work is not a calligraphic surface. It is a change in the title's job:

- treat the title as a place where the story happens;
- let figures, gaps, landscape, or time occupy its strokes;
- split a phrase by meaning when different words represent different worlds;
- change character scale to express power, historical pressure, distance, or isolation;
- make solid and empty strokes carry doubles, absence, concealment, or memory;
- derive texture from the film's rain, paper, earth, cloth, architecture, work, or violence;
- keep the exact title readable after transformation.

These principles are supported by Huang Hai's discussion of turning `乱` into a stage curtain and splitting `草木人间` into natural and human realms, as well as analysis of figures embedded in the strokes of `影` and `黄金时代`:

- https://www.jff.jpf.go.jp/article/huanghai/
- https://pdf.hanspub.org/arl20230400000_88571438.pdf

Do not copy those compositions. Change the film, spatial logic, material, motif relationship, and title behavior.

## Choose one structural operation

| Operation | Story use | Construction |
|---|---|---|
| Title monument | history, fate, epic scale | make the title the dominant mass; reduce figures to witnesses |
| Stroke architecture | complex relationships, social pressure | separate broad stroke bands into passages, ledges, or barriers |
| Negative window | secrecy, absence, hidden identity | remove one or two purposeful openings from the title |
| Semantic split | nature/human, past/present, home/world | assign different zones or materials to meaningful word groups |
| Scale rhythm | unequal power, growth, ensemble tension | vary individual character scale and baseline |
| Outline echo | memory, doubles, afterimage | pair a solid title with displaced outlines |
| Mirror fade | water, reflection, death, alternate reality | reflect the title across a story-grounded boundary |
| Material title | sport, rain, ash, thread, paper, repair | alter edges and gaps using a material evidenced by the film |

Use one structural operation and, at most, one compatible material treatment. Do not stack effects merely to look designed.

## Script controls

`compose_poster.py` supports:

- `split_chalk`: fractured bands and athletic chalk erosion;
- `rain_canopy`: rain channels, canopy separation, and leaf voids;
- `stroke_architecture`: broad displaced stroke bands;
- `negative_window`: large openings cut through filled glyphs;
- `outline_echo`: displaced outline afterimages; use `effect_color`;
- `mirror_fade`: a fading reflected title;
- `character_layout`: per-character scale, offset, rotation, color, and optional stroke.

Example:

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
    {"scale": 0.78, "dy": 0.045},
    {"scale": 1.05, "rotation": -3},
    {"scale": 0.9, "dx": -0.01, "dy": 0.025}
  ]
}
```

`dx` and `dy` are fractions of poster width. `stroke_width` is also a width fraction. Repeat the last `character_layout` object when the title contains more characters than the array.

## Quality checks

- At thumbnail size, the title must contribute one clear mass or axis.
- At full size, the transformation must reveal one story relationship.
- Removing the title must weaken the composition.
- Replacing the title with another film name must break the concept.
- Distortion must not create a wrong character or uncertain title reading.
- Credits must remain typographically calm; expressive treatment belongs mainly to the title.
