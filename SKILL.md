---
name: infographic-creator
description: Create or improve explanatory infographics, flows, comparisons, and system diagrams using AntV or Graphviz, as standalone visuals or inside reports, PDFs, and slides. Use for information design and reference-led visual revisions, not routine prose edits, ordinary statistical charts, or image-only illustration.
---

# Infographic Creator

Create visuals whose structure explains the content before decoration is added. A template that renders correctly is only a starting point. Preserve the user's requested language, deliverable, renderer, facts, and evidence boundaries.

## Choose the deliverable and renderer

- **Syntax only:** return one requested-language code block (`infographic` or `dot`), without extra explanation. An unspecified infographic DSL means AntV; do not silently return DOT instead.
- **Standalone visual:** deliver the inspected visual with editable source. For HTML, provide a working SVG download and usable dimensions; do not deliver a code fragment as the finished visual.
- **Integrated document:** place the actual rendered visual in the requested report, PDF, or slides. Read [document-integration.md](references/document-integration.md) and use an available format skill for export and page inspection. An HTML companion does not replace the requested document.

Select by the information problem, not whichever renderer is installed:

| Information to explain | Starting choice | Why / limit |
| --- | --- | --- |
| Small parallel list, comparison, timeline, simple sequence | AntV | Concise editorial templates; preserve equal comparison criteria |
| Multi-role handoff with aligned time steps | AntV interaction | Real lane/time semantics; do not invent chronology |
| Dependencies, nested boundaries, shared resources, conditional loops, field-level links | Graphviz `dot` | Explicit topology, clusters, ranks, ports, and edge labels |
| Root-centered concept map | AntV mindmap or Graphviz `twopi` | Radial distance must not imply measured importance |
| Undirected relationship exploration | Graphviz `neato` / `fdp`; `sfdp` for large networks | Overview plus selected detail; a hairball is not an explanation |
| Quantitative trend or distribution | Appropriate chart tool | Do not force a node graph or unmeasured node sizes |
| Branded explanation around a complex graph | Graphviz SVG inside an editorial HTML/document layout | Keep one consistent final visual and editable graph source |

Keep explicit AntV/Graphviz requests on that renderer. If it cannot express a required relationship, explain the limitation and use an in-scope alternative only when permitted. Do not add Graphviz simply to make a short list look technical.

## Design before syntax

For a substantial visual, establish a compact internal brief: **reader's question; supported takeaway; entities and relationships; evidence/status; target size; visual grammar**. Infer sensible defaults from the task; ask only for missing information that materially affects correctness. Do not ask the user to pick a template when the structure is clear.

1. **Choose the semantic shape.** Distinguish a list, sequence, branching decision, hierarchy, network, and comparison. A list of three nouns does not justify arrows. Name directed relations with verbs or conditions where ambiguity matters.
2. **Compose the reading path.** Give the main explanation the largest area. Group by real responsibility, stage, or category. Put exceptions beside the main flow and route returns visibly. Avoid equal-sized cards for information with unequal roles.
3. **Apply a visual grammar.** Use consistent type roles, spacing, node styles, and semantic colors. Main path, secondary context, and exceptions should be distinguishable without color alone. Icons are optional unless the chosen template needs them; they must earn their space.
4. **Render early.** For a major redesign or an uncertain fit, compare two plausible structures at final size and choose the clearer one. Routine edits do not need multiple variants. Do not equate more nodes, colors, gradients, or 3D effects with higher quality.
5. **Inspect and revise.** Fix topology first, then density and typography, then finish. Shorten, regroup, or split an unreadable graph rather than shrinking every label.

Read [visual-design.md](references/visual-design.md) for substantial new visuals, bland/template-like feedback, or complex layouts. It defines concrete composition and critique criteria.

For reference-led work, inspect both the actual image and relevant source when available. Read [graphviz-patterns.md](references/graphviz-patterns.md) for reusable structural recipes and their limits. For a Graphviz task whose structure is not already obvious, search the complete reviewed gallery catalog with `python scripts/select-graphviz-pattern.py "<the user's situation>"`; then read only the shortlisted rows in [graphviz-gallery-catalog.md](references/graphviz-gallery-catalog.md) and their official pages. Transfer the principle; do not inherit another example's claims, arbitrary palette, or licensing assumptions.

## Author and render

### AntV

Read [antv-syntax.md](references/antv-syntax.md) when writing DSL and [antv-rendering.md](references/antv-rendering.md) for HTML/export. Retain the pinned `@antv/infographic@0.2.20` runtime unless deliberately updated and tested. The template catalog is not a guarantee that every named template works in the pin. Verify unfamiliar selections.

### Graphviz

Read [graphviz-rendering.md](references/graphviz-rendering.md) before writing DOT or rendering. It covers engines, Korean labels, ports, layout traps, local execution, and the reusable renderer. The catalog contains all 47 official gallery entries indexed on 2026-09-06, grouped by practical situation with use/avoid decisions; it is a selection reference, not a bundle of redistributable templates. Original adaptable sources are in [assets/graphviz](assets/graphviz); select by semantics, not filename alone. These are hypothetical teaching examples, not candidate/company evidence.

## Acceptance conditions

- **Meaning:** the reader can identify the main point, grouping, and direction without reading every paragraph. No fabricated numbers, dependencies, implementation claims, or comparison disadvantages.
- **Topology:** every intended node and edge survives export. Check all branches, return paths, attachments, and arrowheads against the intended relationship list. Layout-only edges are invisible and never imply business relationships.
- **Legibility:** inspect the actual final size, Korean line breaks, glyphs, label collisions, connector clearance, and contrast. Fit the layout to the canvas; do not stretch SVG non-uniformly.
- **Finish:** restrained and consistent hierarchy, spacing, alignment, edge weight, and meaningful accent use. No blank icons, decorative arrow clutter, unexplained shape changes, or fake dashboards.
- **Delivery:** export opens, SVG download works when offered, source is retained, and the requested document includes the same visual. An offline claim requires no external runtime/font/icon dependency.

Structural validation, render success, visual inspection, and final document inspection are separate facts. State only the checks actually performed; mark any unresolved limitation. Do not describe an uninspected export as complete.

For upstream provenance or an intentional update, read [upstream.md](references/upstream.md). Preserve local design extensions when refreshing upstream material.
