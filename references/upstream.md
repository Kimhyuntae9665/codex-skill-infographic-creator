# Upstream provenance

- Repository: https://github.com/antvis/Infographic
- Installed skill path: `skills/infographic-creator`
- Pinned commit: `2ea1894255e4002c7735586778be86d13ec30346`
- Installed on: 2026-09-01 (Asia/Seoul)
- License: MIT, as declared by the upstream repository
- Pinned browser runtime: `@antv/infographic@0.2.20`
- Product site: https://infographic.antv.vision/
- Original short link: https://t.co/lVtiwZUY9T

The original AntV content was downloaded from the pinned commit above. Treat upstream
changes as unreviewed until the new revision is inspected and the local skill
passes validation again.

To refresh intentionally, use the Codex `skill-installer` workflow with the
same repository path and a reviewed commit. Preserve this provenance file or
replace its commit and install date with the newly verified values.

Local extension, 2026-09-06: renderer routing, editorial design guidance,
Graphviz pattern research, original DOT examples, and a local Viz.js render
helper were added at the user's request. AntV syntax was moved to
antv-syntax.md; its runtime pin was preserved. These local extensions are not
part of the upstream commit. Preserve them when updating. Graphviz sources and
their reuse boundaries are listed in graphviz-patterns.md. The optional Viz.js
helper was tested with @viz-js/viz 3.30.0; dependencies are not vendored here.

Full-gallery extension, 2026-09-06: all 47 examples linked from the official
Graphviz gallery index were retrieved with their available DOT sources and
catalogued into 13 practical situations. The generated metadata lives in
graphviz-gallery-index.json, the readable decisions in
graphviz-gallery-catalog.md, and the focused selector in
scripts/select-graphviz-pattern.py. Gallery source code and images are not
vendored because licenses vary; only links, metadata, and original guidance
are retained.
