# Visual design: from diagram to explanation

Read for substantial infographic work or requests to make a visual less generic. These are adaptable editorial defaults, not Graphviz requirements or a universal house style.

## Composition and hierarchy

- Start with a supported takeaway title, not merely a topic name. Use a neutral question if evidence does not support a conclusion.
- Establish three levels: main claim; structure/section labels; details and evidence notes. Use whitespace and weight as well as font size. Avoid making every card equally prominent.
- Let the important path occupy a stable direction, usually left-to-right or top-to-bottom. Place branches by condition and keep feedback on an outside lane. A short flow should not zigzag solely to fill space.
- Enclose related entities only when the boundary means something: team, environment, subsystem, phase. Label the boundary. Proximity alone should not suggest ownership that is not known.
- Align entities that share a stage or comparable role, not unrelated items that happen to fit. Separate the diagram title and explanatory notes from layout constraints when an HTML/document wrapper handles them better.
- Choose aspect ratio from the destination. A wide six-stage diagram may need two coordinated panels on portrait paper. Do not resize a landscape graph into microscopic text.

## Typography and spacing

- Use one readable Korean-capable family, with restrained weights. Verify actual font availability and rendered glyphs. A declared font is not proof it was used.
- Keep labels short enough to scan; move evidence details to a note or structured secondary line. Break Korean at phrase boundaries. Keep units with their values.
- At intended display size, start near 16–20 px for principal web labels; document sizes follow document-integration.md. These are reading-size heuristics, not source SVG font-size mandates.
- Reuse spacing intervals, for example 8/16/24/32 px in an editorial wrapper. Allow more separation between groups than within groups. Graphviz spacing uses its own units; do not transfer pixel values blindly.
- For data-rich entities, use a title plus one or two compartments. Use ports if a line refers to a specific field or resource. Do not turn each node into a miniature paragraph.

## Color, shape, and connectors

Start with neutral background/text, one primary accent, and an exception accent when needed. Add categorical colors only when they encode real categories. Example adjustable tokens:

| Role | Light editorial | Technical dark |
| --- | --- | --- |
| Background / text | `#F6F8FB` / `#17243B` | `#111827` / `#F3F4F6` |
| Primary path | `#2855C7` | `#93C5FD` |
| Secondary boundary | `#CBD5E1` | `#64748B` |
| Exception | `#9A4D0B` | `#FDBA74` |

Check actual contrast on the final background. Pair state colors with words or line styles. A gradient can decorate a surface, but should not make an essential connector fade into invisibility.

- Use shape changes for roles: action, decision, stored data, terminal state. Explain unfamiliar conventions. UML diamonds and triangles have specific meanings; do not use them as decoration in ordinary business diagrams.
- Pick a small edge vocabulary: solid directed flow; dashed labeled exception/return; undirected association where there is no causal direction. These meanings are local conventions and must be stated when not obvious.
- Emphasize a main path only when supported. Equal stroke width is safer than invented edge volume. Avoid merged edges when they hide source/target identity.
- A good icon aids recognition. Omit repetitive rockets, shields, and lightbulbs when labels already do the work. Never substitute an icon for a required state or condition label.

## Critique and repair

| Visible problem | Repair to try first |
| --- | --- |
| Identical boxes look like a generic template | Re-establish main vs secondary content; encode genuine groups and roles |
| Rainbow palette with no legend | Reduce accents or map each color to a meaningful category |
| Many crossings | Change rank direction, ordering, group boundaries, or split overview/detail |
| Dense radial map | Reduce label depth; separate branches into detail panels |
| Long text inside small cards | Keep entity/action label and short qualifier; move explanation outside |
| Attractive boxes but unclear purpose | Rewrite the takeaway and label ambiguous relationships |
| Huge graph shrunk to fit | Select the relevant subgraph and disclose scope; retain full graph separately if useful |
| Arrow overlaps a node label | Re-layout with actual text bounds; change ports or route style |

Judge the result at normal size, not only zoomed in: What is the first thing read? What relationship is learned? Is any element visually important without being substantively important? Fix the weakest answer before adding decoration. Do not assign an invented objective quality score or guarantee a subjective preference.
