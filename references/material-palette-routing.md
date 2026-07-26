# Material and palette routing

Use this reference for every poster concept. Choose the visual ground from the film, not from a generic idea of tasteful poster design.

## Evidence-first surface

Record one observable story source before selecting a surface or production process:

```text
story evidence / ground / image-making process / palette roles /
quiet-field substance / recent-output delta
```

Paper, parchment, archive stock, printed ephemera, fibers, fading, stains, scratches, ink misregistration, halftone, and distressed edges require direct evidence from the film's period, place, profession, prop, institution, or dramatic action. “Historical,” “poetic,” “Chinese,” “festival,” and “artistic” are not evidence.

Do not combine aged paper, warm bone white, charcoal, vermilion, screen print, paper tooth, and ink misregistration as a default prestige bundle. Use no more than one unevidenced surface cue; preferably use none.

## Ground and process lanes

Choose the lane the story requires. Paper is one option, not the neutral default.

| Lane | Ground | Process and light | Useful evidence |
|---|---|---|---|
| Clean graphic | solid or sharply divided color field | crisp flat paint, clean offset, vector-like edge | institutions, games, social systems, comedy |
| Luminous atmosphere | sky, haze, darkness, fog, projected light | translucent glazing, bloom with controlled blacks | memory, dreams, childhood, distance |
| Wet environment | rain, puddle, river, wet asphalt, condensation | reflection, refraction, liquid edge | weather, travel, grief, encounter |
| Photographic intervention | photographed space, face, garment, architecture | restrained photography plus one graphic action | performance, intimacy, contemporary realism |
| Saturated painting | chromatic field or location color | gouache, oil, airbrush, digital paint without visible paper tooth | animation, fantasy, desire, heightened emotion |
| Material object | metal, glass, lacquer, cloth, wood, earth, skin | surface-specific highlight, wear, fracture, weave, polish | craft, labor, body, technology, place |
| Architectural field | wall, stage, corridor, facade, void | hard light, shadow, projection, measured geometry | power, confinement, ritual, public life |
| Evidenced print | film-specific document, newspaper, ticket, archive, handmade print | paper, ink, rubbing, screen print, letterpress | archives, printing, bureaucracy, historical evidence |

If the film supports several lanes, prefer the one least similar to the last two completed posters while preserving story relevance.

## Quiet field is spatial, not material

Define what the quiet field physically is:

- open sky, darkness, fog, water, wall, snow, stage light, color field, distant landscape, or genuine paper evidence;
- name how it carries distance, silence, pressure, shelter, scale, or readable copy;
- never write only “blank paper,” “warm neutral background,” or “calm textured field.”

## Palette routing

Assign roles before color names:

```text
ground = time and environment
structure = visual skeleton
emotion = psychological temperature
fate accent = decisive event
```

Do not default to bone white + charcoal + vermilion. Vary at least two of ground hue, value structure, saturation range, accent family, and color temperature from the last two outputs. Animation and fantasy should normally test one chromatically richer direction. Family drama should derive temperature from season, weather, home, costume, or emotional change rather than default to worn warm neutrals.

## Recent-output rotation

Inspect up to five recent completed posters when available. Record:

```text
ground material / dominant hue / production process /
texture age / title mechanism / accent color
```

Reject the selected direction when it repeats four or more fields from either of the last two posters without film-specific necessity. After two consecutive paper-based or distressed-print posters, the next poster must use a non-paper, non-distressed lane unless the film contains direct paper evidence.

## Layout contract

Record the final decision:

```json
{
  "surface_design": {
    "ground": "rain-dark foliage, mist and reflective puddle",
    "story_evidence": "the encounter occurs during a summer rainstorm",
    "production_process": "luminous layered gouache with wet reflections and no visible paper tooth",
    "palette_logic": "rain blue-green ground, near-black structure, coral umbrella accent",
    "quiet_field": "mist and pale rain carry shelter, scale and creator copy",
    "recent_output_delta": "replaces the previous aged print ground with wet chromatic atmosphere",
    "paper_based": false,
    "paper_evidence": null,
    "distressed": false,
    "distress_evidence": null
  }
}
```

For `paper_based: true`, provide non-empty `paper_evidence`. For `distressed: true`, provide non-empty `distress_evidence`. A final poster must fail validation when these declarations are missing or inconsistent.

## Inspection

- Hide the title: does the ground still feel specific to the film?
- Convert mentally to beige paper: if the concept loses nothing, the surface decision is generic.
- Check the dominant color clusters: does one warm paper family occupy the image without narrative need?
- Remove grain, stains, fading, and misregistration: if meaning survives, omit them.
- Compare with the last two outputs at thumbnail size: reject a repeated material skin.
