# Cast-and-crew typography

Use this reference for every Standard or Series poster. Treat verified cast-and-crew copy as a designed secondary visual system, not a tiny export footer.

## Contents

1. Credit architecture
2. Participation mechanisms
3. Readability floor
4. Layout contract
5. Copy discipline
6. Inspection

## Credit architecture

Build three factual groups:

1. **Creator signature** (`creator_credit`) — director and, when appropriate, writer or “a film by” equivalent. Make it an authored entry point, quiet counterweight, or signature near the title, motif, or an intentional field. Do not bury it inside the compact block.
2. **Principal-cast rail** (`verified_cast`) — principal cast as a prominent, readable name rhythm. Extend an axis, horizon, edge, or sequence already present in the image. Do not treat it as legal microcopy.
3. **Factual base** (`verified_credits`) — role-labelled director, writer, and principal cast. Use it as a compact factual threshold, evidence label, or structural base rather than the only place where important names appear.

All three roles are required for `--final`. Do not repeat unsourced producers, companies, presenters, legal copy, or billing order merely to make the block look theatrical.

Reserve 12–22% of the poster for the complete credit system. The reserve may be split across the page; it does not have to be one bottom strip. Declare its total share and relationship in `credit_design`.

Keep the hierarchy unmistakable:

```text
film title > principal cast ≈ creator signature > factual base
```

An auteur-led campaign may make the creator signature equal to or slightly stronger than the cast rail. In every case, both the director and principal cast must be more immediately readable than the factual base.

## Assign each role a compositional job

Write a different job for each group before typesetting:

- `creator_function`: where the director acts as authorial entry point or counterweight;
- `cast_function`: which path, edge, horizon, sequence, or rhythm the principal names extend;
- `credits_function`: which threshold, evidence structure, or base the compact facts establish.

Then run a removal test. Temporarily hide the creator signature and cast rail separately. Record in `removal_test` what balance, direction, rhythm, or authorship cue becomes weaker. If nothing changes, reposition or regroup the names before rendering.

Do not use vague declarations such as “integrated with the design.” Name the visible relationship, for example: “director signature balances the title in the upper-left quiet field” or “cast names continue the train-track baseline.”

## Participation mechanisms

Choose one primary mechanism and one secondary mechanism:

| Mechanism | Construction |
|---|---|
| Shared axis | align creator, cast, and compact block to the title, horizon, rail, wall, or gaze |
| Counterweight | place a larger creator or cast group in a quiet field balancing the title or motif |
| Spatial rail | make names continue a road, train line, architectural edge, waterline, or movement path |
| Threshold | let credits form a gate, border, ledge, or lower/upper boundary without enclosing the whole poster |
| Scale echo | repeat the title's scale rhythm at a much quieter level |
| Material echo | borrow one title color, rule, indentation, or surface behavior without applying expressive distortion |
| Evidence label | attach factual groups to a real document, specimen, map, or archival structure |
| Constellation | distribute a small number of principal names around corresponding story positions without implying false character mapping |

Participation means removing a credit group would weaken the composition's balance, direction, or rhythm. It does not mean distorting names, hiding them inside imagery, or making them compete with the title.

Do not default to centered names plus a tiny centered block. Change alignment, grouping, baseline, direction, or placement because of the selected poster geometry.

Prefer one of these campaign hierarchies:

| Campaign emphasis | Creator signature | Principal-cast rail | Factual base |
|---|---|---|---|
| Auteur-led | signature near title or decisive quiet field | calmer supporting rail | compact structural threshold |
| Star-led | clear authorial counterweight | widest or most rhythmic secondary text | compact base |
| Ensemble | small authored entry point | names grouped as measured sequence, not one dense sentence | multi-line factual base |
| Festival / concept | restrained signature tied to motif | sparse names on one evidence axis | archival label or border |

Do not imply contractual star billing, character-name mapping, or relative importance unless the approved campaign copy supports it.

## Readability floor

Font sizes are normalized against poster width:

| Role | Recommended | Hard minimum for `--final` |
|---|---:|---:|
| `creator_credit` | 1.6–2.6% | 1.4% |
| `verified_cast` | 1.7–2.8% | 1.5% |
| `verified_credits` | 1.35–1.8% | 1.25% |

At 1024 px width, the hard minima are approximately 14 px, 15 px, and 13 px. Prefer larger sizes for mobile or social delivery.

The declared `creator_credit` and `verified_cast` sizes must each be larger than the declared `verified_credits` size. Size alone is insufficient: also distinguish at least one of position, grouping, tracking, weight, color, or axis.

Set `min_font_size` on every credit block. `compose_poster.py` may reduce text to fit `max_width`, but it must stop at this floor and fail instead of silently producing unreadable copy.

When a line does not fit:

1. add a meaningful line break;
2. widen or reposition the reserve;
3. reduce tracking;
4. shorten only optional, approved copy;
5. never remove verified names or shrink below the floor.

Use sufficient contrast. Fine warm gray on textured paper may look elegant at full resolution but disappear on a phone. Check both the glyph stems and the spaces between names.

## Layout contract

Add this top-level record:

```json
{
  "credit_design": {
    "primary_axis": "bottom rail continuing the image horizon",
    "reserved_area": 0.16,
    "participation": "cast rail extends the track; creator signature counterbalances the vertical title",
    "creator_function": "director signature opens the upper-left quiet field and balances the title",
    "cast_function": "principal names continue the track baseline as a three-beat rhythm",
    "credits_function": "compact role-labelled facts establish the lower threshold",
    "removal_test": "without the director the upper-left loses authorship and balance; without the cast rail the track stops before crossing the page"
  }
}
```

All seven `credit_design` fields are mandatory for `--final`. `reserved_area` must be between `0.12` and `0.30`.

Example blocks:

```json
[
  {
    "text": "导演　姓名",
    "role": "creator_credit",
    "font_size": 0.018,
    "min_font_size": 0.014
  },
  {
    "text": "主演甲　主演乙　主演丙",
    "role": "verified_cast",
    "font_size": 0.020,
    "min_font_size": 0.015
  },
  {
    "text": "导演　姓名　　编剧　姓名甲 / 姓名乙\n主演　主演甲 / 主演乙 / 主演丙",
    "role": "verified_credits",
    "font_size": 0.014,
    "min_font_size": 0.0125
  }
]
```

Positions, alignment, color, tracking, and orientation must follow the poster geometry. These values illustrate hierarchy, not a reusable bottom-center template.

## Copy discipline

- Verify every name and role and record sources.
- Preserve supplied billing order. When contractual order is unavailable, use explicit role labels and preserve source order.
- Keep Chinese name spacing consistent. Use ideographic spaces, rules, or line breaks deliberately.
- Keep English transliterations secondary unless they are approved campaign copy.
- Do not condense, stretch, rotate, outline, or texture a person's name until it becomes hard to identify.
- Do not generate credit text inside the image model.

## Inspection

Check at three sizes:

- **Thumbnail**: the credit system reads as a deliberate rail, counterweight, or boundary.
- **Phone width**: creator and principal-cast names are readable without zooming.
- **Full size**: every role, name, separator, and source-approved ordering is exact.

Reject the final poster when:

- the credit block exists only to satisfy validation;
- the director appears only inside `verified_credits`;
- the principal cast reads like legal microcopy rather than a visible name rhythm;
- any required group is visually detached from the main geometry;
- names disappear into texture or low contrast;
- fitting reduces a group below its hard minimum;
- the creator or cast size is not larger than the compact factual base;
- the title and credits use unrelated axes, spacing logic, and color behavior;
- the principal cast is technically present but functionally unreadable.
