---
name: cinematic-portrait-poster
description: Create original vertical movie-poster concepts, image-generation prompts, generated key art, and precise typography layouts from a film title, synopsis, screenplay, character brief, stills, or campaign requirements. Use for Chinese-language or international film posters, teaser posters, official key art, character posters, festival posters, and 2:3, 3:4, or 9:16 adaptations that need symbolic storytelling, Eastern poetic restraint, strong visual metaphors, or a production-ready poster workflow.
---

# Cinematic Portrait Poster

Create an original narrative poster from the film's dramatic core. Treat admired poster work as design research, never as a surface style to copy. Do not put a living artist's name in an image prompt or claim that the output is in that artist's exact style. Translate references into high-level properties such as symbolic compression, negative space, scale contrast, material texture, and culturally grounded imagery.

## Select a mode

- **Concept**: return three distinct concept directions without generating images.
- **Standard**: default; develop concepts, select one, generate key art, typeset it, and return the finished poster.
- **Series**: create a coherent teaser, main poster, character set, or aspect-ratio family. Reuse a visual system, not one unchanged layout.
- **Prompt-only**: stop after the final image prompt only when explicitly requested.

## Load references

Read only what the task needs:

- Always read [references/narrative-analysis.md](references/narrative-analysis.md) and [references/metaphor-grammar.md](references/metaphor-grammar.md).
- Read [references/composition-recipes.md](references/composition-recipes.md) to choose layout, material, palette, and genre treatment.
- Read [references/typography.md](references/typography.md) before adding real titles, credits, dates, or bilingual copy.
- Read [references/quality-gate.md](references/quality-gate.md) before final delivery.

## Workflow

### 1. Normalize the brief

Extract supplied facts without inventing names, awards, release dates, logos, or billing. Record:

- title and optional English title
- logline or synopsis
- genre, period, region, audience, and campaign stage
- protagonist, desire, opposition, irreversible turn, and emotional aftertaste
- recurring objects, spaces, actions, natural imagery, and visual restrictions
- exact required copy and supplied reference assets

If a factual field is missing, omit it or visibly mark it as a placeholder in the layout plan. Ask only when the missing fact blocks the requested deliverable.

### 2. Build the narrative DNA

Follow `references/narrative-analysis.md`. Reduce the film to:

1. one dramatic proposition;
2. one dominant emotion;
3. one primary motif and no more than two supporting motifs;
4. one concealed meaning that becomes clearer after viewing the film.

Do not summarize the entire plot in the poster.

### 3. Propose three concepts

Make the concepts structurally different. For each provide:

- concept name;
- one-sentence visual hook;
- primary motif and metaphor operation;
- composition family, material, palette, and typography mode;
- why it belongs to this film;
- spoiler risk: low, medium, or high.

Reject concepts that would fit many unrelated films after swapping only the title. In Standard mode, select the strongest direction using story relevance, silhouette clarity, emotional force, originality, campaign usefulness, and low spoiler risk.

### 4. Compile the visual recipe

Choose one value from each axis:

```text
format / composition family / metaphor operation / primary motif /
scale relation / material process / palette / title behavior / emotional temperature
```

Use a single primary visual mechanism. Favor a legible silhouette and a strong near/far reading over a dense collage.

Default format is a vertical 2:3 poster. Use 3:4 for social feeds and 9:16 for full-screen mobile only when requested or clearly appropriate. Keep all critical elements within a 7% safe margin.

### 5. Compile the image prompt

Write five compact paragraphs in this order:

1. canvas, aspect ratio, surface, and intended poster function;
2. attention geometry, subject size, location, and negative-space behavior;
3. exact visual metaphor, motif relationship, and scale contrast;
4. medium, texture, palette, light, and emotional temperature;
5. hard avoids.

Describe only visible pixels. Use concrete nouns, spatial relationships, proportions, materials, and colors. Do not include analysis, field labels, a designer's name, or long prose.

Generate **text-free key art by default**. Permit only abstract glyph-like marks when they are part of the image. Reserve exact Chinese titles, credits, dates, and billing for deterministic typesetting.

Hard avoids:

- celebrity head grids or floating-head montage unless explicitly requested;
- generic Chinese motifs unrelated to the film;
- decorative dragons, clouds, seals, ink, or calligraphy added only to signal “Chinese”;
- multiple competing metaphors;
- fake awards, festival laurels, logos, dates, credits, or ratings;
- glossy mockups, product-ad layouts, UI panels, watermarks, neon cyberpunk defaults, and game-key-art clutter;
- exact imitation of a named living artist or a recognizable existing poster composition.

### 6. Generate and inspect key art

Use the built-in image-generation capability unless in Concept or Prompt-only mode. Use supplied images only according to the user's stated role: identity reference, costume reference, location reference, or source material.

Inspect the generated key art at full size and thumbnail size. Regenerate once when the main metaphor is missing, the silhouette collapses, text artifacts dominate, culturally irrelevant decoration appears, or the result closely echoes a known poster.

### 7. Typeset exact copy

Follow `references/typography.md`. Keep a text-free key-art file. Create a layout JSON from [assets/layout-example.json](assets/layout-example.json), then run:

```powershell
python scripts/compose_poster.py --background <key-art.png> --layout <layout.json> --output <poster.png>
```

Prefer an explicitly supplied licensed font. The script can use common system fallbacks, but verify Chinese glyph coverage visually. Never fabricate a production billing block.

### 8. Validate and deliver

Apply `references/quality-gate.md`. Return:

1. narrative DNA;
2. three concepts and the selected direction;
3. visual recipe;
4. final image prompt and hard avoids;
5. text-free key art;
6. typeset poster when exact copy is available;
7. a short design interpretation;
8. any placeholders, factual uncertainties, font substitutions, or spoiler concerns.

For a series, also return a consistency rule and a variation rule for each member.

