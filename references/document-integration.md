# Infographics inside documents

Read for integrated proposals/reports, visual revisions of text-heavy documents, reference-led design, or connector-quality feedback. These instructions do not apply a visual-first layout to plain-text forms, ATS resumes, or syntax-only requests.

## 1. Interpret the direction as an acceptance condition

Translate the user's direction into visible outcomes before drafting. Examples:

| Direction | Required change | Insufficient response |
| --- | --- | --- |
| “Too much text” / “글 위주다” | Redistribute explanation into meaningful flows, comparisons, or grouped evidence; shorten duplicate prose | Add small decorative cards after unchanged paragraphs |
| “Use this infographic skill actively” | Use the selected rendered infographic in the requested artifact where it carries explanatory work | Deliver only a separate HTML demo or replace it with unrelated hand-drawn shapes |
| “The line is broken” | Verify every intended source-to-target connection and its direction in the final export | Thicken a short line without fixing its endpoint, or check only that it rendered |
| “Like last year's example” | Inspect the available reference, identify transferable information structure, and label what kind of source it is | Claim a press-release diagram establishes the layout of an unavailable submission |

When the current conversation contains an approved visual preference, use it for comparable artifacts without waiting for the user to name the skill again. Keep the preference scoped: approval of one visual proposal does not prescribe that layout for all documents.

## 2. Map required content before placing paragraphs

For each relevant official section, identify the reader's question, the claim to communicate, the supporting evidence/status, the suitable visual, and the residual prose. A short working table is sufficient; do not create a new deliverable solely for this planning step.

- Sequence or dependency: show inputs, transformations, outputs, failure paths, and responsible actors where relevant.
- Parallel requirements or checks: use comparable cards or a compact table; do not imply chronology with arrows.
- A real contrast: use a comparison with the same criteria on both sides. Do not fabricate competitor deficiencies.
- Quantities: chart only measured or sourced values. Do not invent performance numbers to fill a graphic.
- A short single fact: retain prose when a visual would add no information.

For a visual-first proposal, choose the main explanatory visual before filling the page with paragraphs. A useful arrangement is a conclusion-led title, a readable visual, short interpretation, and a compact evidence/limitation note. Adapt this to the official form; it is not a mandatory layout or fixed ratio.

Preserve required headings, order, limits, and claims. Formal compliance does not itself require a text-heavy page. Conversely, a locked official form or explicit text-only rule overrides this layout preference: fit permitted visuals within the form or keep the requested form text-only. Do not add an unrequested presentation or redesign the official form to make space.

Avoid repeating all diagram labels in body text. Use prose for reasoning, caveats, and evidence that the diagram cannot carry clearly. Consolidate repeated caveats without hiding material uncertainty.

## 3. Inspect the reference and keep its status explicit

Distinguish an original submission, official summary, press-release illustration, screenshot, and user-reported recollection. Record which was actually available. Inspect the relevant visual before claiming stylistic similarity.

Transfer communication principles such as data → processing → user outcome, grouping, or responsibility boundaries. Do not copy another team's unverified claims, diagrams, logos, or private material. When the submission original is unavailable, state that its prose-to-visual balance and exact formatting are unknown. A recollection that a sample was used is a search clue, not evidence of its contents.

## 4. Render, integrate, and check the export path

Use the selected AntV DSL or Graphviz DOT as the editable visual source. Follow the renderer reference, export, and embed that same design in the requested document. Explicit AntV requests stay on AntV. Avoid maintaining an attractive sidecar while the actual PDF uses a separate low-information approximation.

- Wait for fonts and actual icon rendering; a valid icon string can still resolve to an empty or misleading asset. Inspect each principal icon. Use a verified icon or a small consistent vector replacement if resolution fails.
- Prefer vector embedding where the target renderer supports the exported SVG. AntV exports can contain `foreignObject`, symbol references, gradients, and filters: a converter may silently omit text/icons. Test the real export path. If needed, render to a sufficiently high-resolution image at the intended print size (typically around 300 ppi) and retain the editable source.
- Check the diagram on the final page, not only enlarged in a browser. For A4 proposals, aim for roughly 9–11 pt principal labels; essential content that falls below about 8 pt usually needs a simpler layout or more space. Official typography rules take priority. Footnote size is not a justification for shrinking the main explanation.
- If a template creates awkward Korean word splits, shorten labels, increase usable width, or change layout. Do not solve density by shrinking all text.
- Keep proposed, previously reported, and verified components distinguishable. A polished structure diagram is not proof of an implemented system. Do not replace unavailable real product evidence with a fabricated dashboard.

## 5. Connector and icon acceptance

For genuine process connections, not decorative list separators:

1. Count the expected transitions and verify the corresponding edges. A simple six-node chain has five transitions; branched graphs require their own edge list.
2. Derive endpoints from actual source and target bounds in the same transformed coordinate system. A line ending near the center of an inter-node gap is incomplete. Small consistent boundary padding is acceptable only when the connected pair remains unambiguous; explicit edge-to-edge feedback requires boundary-to-boundary connections.
3. Verify arrowhead direction and start/end attachments, especially after a row wraps or a branch changes direction. Keep connectors out of text and icons.
4. Check contrast against the final page background. A template's gradient or translucent arrow may fade into an apparent break even when geometry exists. For a clear-connection request, use a continuous, sufficiently contrasted line with a distinct arrowhead.
5. If post-processing is needed, preserve semantics and source editing. Compute geometry from current bounds or assert the exact template/layout preconditions; never reuse hard-coded coordinates on a changed layout. Re-render after changes.

## 6. Completion evidence

Inspect every changed page in the final exported artifact and recheck any affected neighboring pages. Confirm:

- Required sections remain present and their substantive content was not lost during compression.
- The main point and relationships can be understood without reading every paragraph.
- Principal labels, icon meaning, all intended transitions, and status/limitation notes remain readable.
- There are no blank icons, disconnected intended edges, wrong-direction arrows, clipping, or unexpected text loss from SVG conversion.
- The deliverable itself contains the diagrams; the preview, embedded images, and editable/exported companions represent the same final design if those companions are delivered.

Report what changed and what was actually checked. Structural/syntax validation alone must not be described as visual validation. Do not claim that passing these checks guarantees the user's preferred design on the first attempt.

## Scoped regression examples

- A visual competition proposal: map required sections to meaningful visuals, embed them in the PDF, preserve implementation uncertainty, and inspect the export.
- A plain-text application form: preserve its format and character limits; no forced infographic or new artifact.
- A request for DSL only: return one valid code block, without unnecessary browser work or PDF generation.
- A cropped screenshot with one broken connector: inspect the target diagram and fix the edge within the requested scope; do not redesign unrelated pages unless asked.
- An unavailable past submission with only an official diagram: use the diagram's observed structure while explicitly leaving the original submission's format unknown.
