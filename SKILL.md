---
name: cinematic-portrait-poster
description: Create original vertical movie-poster concepts, image-generation prompts, generated key art, integrated film-title designs, verified cast-and-crew credit layouts, and precise final typography from a film title, synopsis, screenplay, character brief, stills, campaign requirements, or admired poster references. Use for Chinese-language or international film posters, teaser posters, official key art, character posters, festival posters, and 2:3, 3:4, or 9:16 adaptations that need symbolic storytelling, Eastern poetic restraint, strong visual metaphors, reference-style translation, or a production-ready poster workflow.
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
- Read [references/authored-reference-translation.md](references/authored-reference-translation.md) whenever the user names an artist, studio, campaign, poster, or visual reference.
- Read [references/typography.md](references/typography.md) before adding real titles, credits, dates, or bilingual copy.
- Read [references/title-design-patterns.md](references/title-design-patterns.md) when designing any expressive title, dominant title structure, material-filled glyph, custom character construction, or typography-led series.
- Read [references/quality-gate.md](references/quality-gate.md) before final delivery.

## Workflow

### 1. Normalize the brief

Extract supplied facts without inventing names, awards, release dates, logos, or billing. Record:

- title and optional English title;
- exact title language variant and punctuation;
- director, screenwriter, principal cast, and any supplied approved credit line;
- logline or synopsis;
- genre, period, region, audience, and campaign stage;
- protagonist, desire, opposition, irreversible turn, and emotional aftertaste;
- recurring objects, spaces, actions, natural imagery, and visual restrictions;
- exact required copy and supplied reference assets.

For Standard and Series modes, the exact film title and verified credits are required. Use user-supplied approved copy or verify at minimum the director and principal cast from reliable sources; include the screenwriter when reliably available. Record the source. If these facts cannot be verified, stop before final typesetting and request them. A clearly labeled placeholder is acceptable only in a concept preview, never in a final poster.

For optional fields, omit them or visibly mark them as placeholders in the layout plan. Ask only when a missing fact blocks the requested deliverable.

### 2. Build the narrative DNA

Follow `references/narrative-analysis.md`. Reduce the film to:

1. one dramatic proposition;
2. one dominant emotion;
3. one primary motif and no more than two supporting motifs;
4. one concealed meaning that becomes clearer after viewing the film.

Do not summarize the entire plot in the poster.

### 3. Translate authored references

When the brief names an admired artist or work, follow `references/authored-reference-translation.md`:

1. summarize the reference's high-level design principles;
2. separate durable principles from recognizable signatures;
3. compile a neutral reference recipe without the artist's name;
4. define an originality delta that changes subject, spatial logic, material logic, and motif relationship.

Do not treat ink wash, calligraphy, vintage grain, or any palette as a style shortcut. Every visible choice must follow from the film.

### 4. Propose three concepts

Make the concepts structurally different. For each provide:

- concept name;
- one-sentence visual hook;
- primary motif and metaphor operation;
- composition family, material, palette, typography mode, title-integration behavior, and credit-block zone;
- title material fact, semantic pivot, one title action, text-reserve level, and beauty engine;
- why the title mechanism cannot be moved unchanged to an unrelated film;
- why it belongs to this film;
- spoiler risk: low, medium, or high.

Reject concepts that would fit many unrelated films after swapping only the title. In Standard mode, select the strongest direction using story relevance, silhouette clarity, emotional force, originality, campaign usefulness, and low spoiler risk.

Before selecting, run a spectacle test: if the concept depends mainly on a dramatic pose, explosion, glow, or star likeness, rebuild it around a film-specific symbol.

Run a title test: if the title could be moved anywhere without changing the composition, redesign its scale, axis, interruption, containment, alignment, or material echo. The title must participate in the visual system without asking the image model to draw the final letters.

Run the semantic mechanism gate in `references/title-design-patterns.md`. Reject a title direction when its story inevitability, formal beauty, or legibility scores below 4/5. Use one primary evidence field, one title action, and at most one interruptor. Mentally hide the title for one second; if the remaining image has no sensory or emotional pull, rebuild the image language.

### 5. Compile the visual recipe

Choose one value from each axis:

```text
format / composition family / metaphor operation / primary motif /
scale relation / material process / palette / title behavior /
title action / text reserve / interruptor / beauty engine /
credit behavior / emotional temperature
```

Use a single primary visual mechanism. Favor a legible silhouette and a strong near/far reading over a dense collage.

Default format is a vertical 2:3 poster. Use 3:4 for social feeds and 9:16 for full-screen mobile only when requested or clearly appropriate. Keep all critical elements within a 7% safe margin.

### 6. Compile the image prompt

Write five compact paragraphs in this order:

1. canvas, aspect ratio, surface, and intended poster function;
2. attention geometry, subject size, location, and negative-space behavior;
3. exact visual metaphor, motif relationship, and scale contrast;
4. medium, texture, palette, light, and emotional temperature;
5. hard avoids.

Describe only visible pixels. Use concrete nouns, spatial relationships, proportions, materials, and colors. Do not include analysis, field labels, a designer's name, or long prose.

Scrub the prompt before generation:

- remove artist, studio, and copyrighted campaign names;
- replace vague style labels with visible construction;
- remove decorative elements that lack a story source;
- ensure the primary metaphor can be stated in one sentence;
- ensure at least four originality axes differ from any cited reference.

Generate **text-free key art by default**, but compose it around an intentional title zone and a readable credit zone. Permit only abstract glyph-like marks when they are part of the image. Reserve exact Chinese titles, credits, dates, and billing for deterministic typesetting.

State whether the text reserve is low (12–22%), medium (25–38%), or high (40–55%) and name the exact content it supports. The open field must carry reading, silence, distance, pressure, or scale; it cannot be unexplained emptiness.

Hard avoids:

- celebrity head grids or floating-head montage unless explicitly requested;
- generic Chinese motifs unrelated to the film;
- decorative dragons, clouds, seals, ink, or calligraphy added only to signal “Chinese”;
- multiple competing metaphors;
- fake awards, festival laurels, logos, dates, credits, or ratings;
- glossy mockups, product-ad layouts, UI panels, watermarks, neon cyberpunk defaults, generic blockbuster glow, and game-key-art clutter;
- exact imitation of a named living artist or a recognizable existing poster composition.

### 7. Generate and inspect key art

Use the built-in image-generation capability unless in Concept or Prompt-only mode. Use supplied images only according to the user's stated role: identity reference, costume reference, location reference, or source material.

Inspect the generated key art at full size and thumbnail size. Regenerate with one targeted correction when the main metaphor is missing, the silhouette collapses, text artifacts dominate, spectacle overwhelms meaning, culturally irrelevant decoration appears, or the result closely echoes a known poster.

### 8. Typeset exact copy

Follow `references/typography.md`. Keep a text-free key-art file. Create a layout JSON from [assets/layout-example.json](assets/layout-example.json), then run:

```powershell
python scripts/compose_poster.py --background <key-art.png> --layout <layout.json> --output <poster.png> --final
```

For every Standard or Series poster:

1. typeset the exact film title as a dominant designed element;
2. make its axis, scale, spacing, color, and position complete the selected metaphor;
3. preserve the exact approved film title; do not shorten or paraphrase it for design convenience;
4. choose one title structure from `references/title-design-patterns.md`; do not rely on font choice alone;
5. use per-character construction, one selected material image, or one story-grounded effect when the title needs custom form;
6. use a precise single window or single interruption instead of arbitrary repeated cutouts when the story calls for containment or fracture;
7. typeset a verified credit block containing at minimum the director and principal cast, plus the screenwriter when reliably available;
8. keep credits subordinate but readable at full size;
9. inspect title-motif interaction and credit legibility at both full size and thumbnail size.

Prefer an explicitly supplied licensed font. The script can use common system fallbacks, but verify Chinese glyph coverage visually. Never fabricate names, roles, billing order, production companies, or a production billing block.

Always use `--final` for the delivered poster. It rejects layouts missing `title` or `verified_credits` roles, common placeholder tokens, or a non-empty `credit_sources` list.

### 9. Validate and deliver

Apply `references/quality-gate.md`. Return:

1. narrative DNA;
2. three concepts and, outside Concept mode, the selected direction;
3. visual recipe;
4. outside Concept mode, the final image prompt and hard avoids;
5. in Standard or Series mode, text-free key art;
6. in Standard or Series mode, a typeset poster containing the integrated film title and verified cast-and-crew credits;
7. a short design interpretation;
8. any placeholders, factual uncertainties, font substitutions, or spoiler concerns.

Also state the provenance used to verify title spelling and credits.

In Concept mode, stop after three unselected directions, their visual recipes, and optional compact prompt outlines. Do not pick a winner or generate images unless the user explicitly asks.

When an authored reference was requested, also return:

9. the high-level principles extracted from it;
10. the originality delta used to avoid copying its recognizable expression.

For a series, also return a consistency rule and a variation rule for each member.
