# Graphviz gallery: transferable patterns

Research date: 2026-09-06. This file explains the core reusable patterns. The complete review now covers all 47 entries linked from the official gallery index; use [graphviz-gallery-catalog.md](graphviz-gallery-catalog.md) or `scripts/select-graphviz-pattern.py` to shortlist them by situation. Every page and available DOT source was retrieved. The rendered Clusters, UML, and Happiness SVGs were inspected in Chrome as representative images; the remaining entries were source/page reviews. Observations and adaptations are design judgments, not promises made by Graphviz.

| Official example | Transferable lesson | Apply when | Do not inherit |
| --- | --- | --- | --- |
| [Clusters](https://graphviz.org/Gallery/directed/cluster.html) | Named regions make process membership visible while preserving cross-boundary edges | Responsibilities, environments, sub-processes | Its grey/blue palette, thin margins, or arbitrary node names |
| [Basic Git Concepts and Operations](https://graphviz.org/Gallery/directed/git.html) | Distinct entities and labeled operations explain state changes; ports identify different interactions with one entity | Product workflows and data movement | Git commands, source-specific semantics, or dense detail without need |
| [UML Class diagram demo](https://graphviz.org/Gallery/directed/UML_Class_diagram.html) | Compartmented nodes separate an entity from its fields; field ports make links precise | Schemas, contracts, shared-resource diagrams | Specialized UML arrow meanings unless actually intended; visible label crowding is a defect to fix |
| [Finite Automaton](https://graphviz.org/Gallery/directed/fsm.html) | State transitions and loops preserve conditions that a linear timeline loses | Validation, retries, lifecycle state | Unexplained symbols or assuming that every flow is an automaton |
| [Entity-Relation Data Model](https://graphviz.org/Gallery/neato/ER.html) | Different node roles distinguish entities, attributes, and relations | Conceptual data modeling | Causal arrows for mere associations, or invented cardinality |
| [Mind map of Happiness](https://graphviz.org/Gallery/twopi/happiness.html) | A root-centered radial layout and typographic levels communicate conceptual depth | Compact topic maps | Decorative handwriting, large canvas, pale edges, or quantitative meaning for radial distance |

The gallery demonstrates graph capabilities, not a uniform benchmark for contemporary infographic aesthetics. Clustering, typed edges, ports, and rank control expand explanatory structure. Editorial typography, spacing, restrained color, and final-size revision provide the finish.

## Structural recipes

- **Responsibility + flow:** one cluster per real boundary, nodes assigned to the correct cluster, labeled transfers, distinct supported return paths. Start with [clustered-workflow.dot](../assets/graphviz/clustered-workflow.dot). Do not manufacture feedback to make a simple process look sophisticated.
- **Conditional lifecycle:** states as nodes, transitions labeled with conditions, retry and terminal outcomes distinguished when the source supports it. Start with [state-review.dot](../assets/graphviz/state-review.dot).
- **Structured entity + field connection:** HTML-like table label with a header and short fields, stable ports, and field-specific links. Start with [record-ports.dot](../assets/graphviz/record-ports.dot). Do not claim UML/ER conformance without the actual notation.
- **Root + concept branches:** explicitly selected root, modest branch count, subordinate secondary labels. Start with [radial-map.dot](../assets/graphviz/radial-map.dot). Switch to a tree/detail panels if Korean labels crowd the perimeter.

## Original starter library

These sources are original, hypothetical, and safe to adapt. They cover the recurring structural families from the complete gallery catalog; styling demos remain catalog references rather than production starters.

| Situation | Starter | Engine | Replace and verify |
| --- | --- | --- | --- |
| Responsibility boundaries and handoffs | [clustered-workflow.dot](../assets/graphviz/clustered-workflow.dot) | `dot` | Boundaries, actions, transfers, return condition |
| Conditional state lifecycle | [state-review.dot](../assets/graphviz/state-review.dot) | `dot` | States, transition conditions, terminal states |
| Fields and precise links | [record-ports.dot](../assets/graphviz/record-ports.dot) | `dot` | Field definitions and target rules |
| Root-centered concept map | [radial-map.dot](../assets/graphviz/radial-map.dot) | `twopi` | Root, equal-level branches, non-quantitative note |
| Directed dependencies and fork/merge | [dependency-dag.dot](../assets/graphviz/dependency-dag.dot) | `dot` | Every dependency and exception |
| Product/version lineage | [hierarchy-lineage.dot](../assets/graphviz/hierarchy-lineage.dot) | `dot` | Parent-child derivation; support/compatibility are separate facts |
| Causal feedback hypothesis | [causal-feedback.dot](../assets/graphviz/causal-feedback.dot) | `neato` | Evidence for every direction and polarity |
| Shared-resource contention | [resource-contention.dot](../assets/graphviz/resource-contention.dot) | `neato` | Actors, resources, link meaning, concurrency evidence |
| Network topology | [network-topology.dot](../assets/graphviz/network-topology.dot) | `twopi` | Actual links; access/security claims require separate evidence |
| Runtime call profile | [call-profile.dot](../assets/graphviz/call-profile.dot) | `dot` | Measured calls, costs, sample window; encode size/color only from values |

Large relationship overviews remain catalog-driven rather than bundled as a starter. `sfdp` behavior varied materially across the tested runtimes; follow the compatibility gate in graphviz-rendering.md and use the official large-graph example as a structural reference.

## Technical sources and reuse boundary

- [Layout engines](https://graphviz.org/docs/layouts/): algorithm choice.
- [Node shapes and HTML-like labels](https://graphviz.org/doc/info/shapes.html): label grammar and field ports.
- [splines](https://graphviz.org/docs/attrs/splines/): routing and orthogonal limitations.
- [constraint](https://graphviz.org/docs/attrs/constraint/): exclude an edge from rank assignment without removing its meaning.
- [compound](https://graphviz.org/docs/attrs/compound/): cluster-boundary clipping with lhead/ltail.

Gallery pages carry different copyright/license notices; do not assume all examples share the AntV MIT license. Bundled DOT examples are newly authored hypothetical examples using documented features, not reproductions of gallery graphs. Verify permissions before redistributing a source image or substantial example code.
