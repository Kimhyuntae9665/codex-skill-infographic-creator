# Graphviz authoring and local rendering

## Match engine to semantics

Use `dot` for directed flow/dependency, hierarchy, clusters, and field links; `twopi` for a selected root and radial levels; `neato`/`fdp` for undirected relationships; `sfdp` for large exploratory overviews. Circular arrangement does not establish that a process cycles. Do not force `dot` rank controls into other engines.

## DOT mechanics that affect quality

- Use stable ASCII IDs and separate UTF-8 labels. Declare graph/node/edge fonts; Korean examples use `Malgun Gothic` on Windows. Check the target font and glyphs; Viz.js metrics and browser fonts can differ.
- Set graph `rankdir=LR` or `TB` to fit the destination, then tune `nodesep`, `ranksep`, and margins. Use `{rank=same; ...}` for real peers/stages. In `dot`, `constraint=false` keeps a feedback edge from changing ranks; it does not remove the edge or reverse its direction.
- Name cluster subgraphs `cluster_*` and label what the boundary means. An ordinary subgraph is not automatically a visible cluster. For deliberate boundary-to-boundary clipping, use `compound=true` and `lhead`/`ltail` on an edge between actual nodes inside those clusters.
- Start with `splines=spline` or `polyline` for labeled edges and ports. Official docs state that `ortho` does not handle ports or, in dot, edge labels. Do not use it as a universal quality fix. Inspect any workaround.
- For compartments, use `shape=plain` and HTML-like TABLE labels with TD `PORT` attributes. This is Graphviz's restricted label grammar, not browser HTML/CSS. Escape literal `&`, `<`, `>`, and quotes; do not mix HTML labels with record syntax. Use `node:port:compass` for precise attachment where appropriate.
- Keep main labels concise and add explicit phrase breaks (`\n` in quoted labels; `<BR/>` in HTML labels). Avoid `fixedsize=true` when text changes; it can overflow. Do not resize SVG text independently of its node without re-layout.
- Use `->` in a directed graph and `--` for undirected associations. Preserve unique relations; `concentrate=true` may obscure individual connections. Invisible edges are layout aids and must not become visible domain edges.
- Test warnings and the actual SVG. Successful parsing does not rule out collisions, wrong ports, font fallback, or poor aspect ratio.

Observed in the tested Viz.js build: Korean fonts and non-ASCII glyphs use fallback layout metrics. Browser text can therefore exceed estimated table widths even when rendering succeeds. Use generous content-sized nodes or minimum TD widths, then inspect the actual browser/export; do not silence the warning or declare typography correct from parsing. For dense or long Korean labels, prefer native Graphviz with a verified text-layout/font stack. The bundled field-port example uses minimum column widths for this reason. Changing its labels requires another size check.

## Runtime choices

Prefer an already available Graphviz CLI, checked with `dot -V`. Render UTF-8 DOT via an argument-safe command such as `dot -Kdot -Tsvg input.dot -o output.svg`. Do not construct shell commands from unescaped labels.

If native Graphviz is absent, use the provided Node helper with **local** `@viz-js/viz`. Tested package pin: `3.30.0`. No system-wide Graphviz installation is required. Install that exact package into a task-local runtime using the available package manager, preserving its lockfile; the helper itself never installs or downloads dependencies.

```text
node scripts/render-graphviz.mjs input.dot output.svg --engine dot --viz-module /absolute/path/to/node_modules/@viz-js/viz/dist/viz.js
```

For a normal package installation visible from the helper, omit `--viz-module`. With a task-local installation, pass the module path explicitly. Discover local Node/Python paths; do not copy another session's runtime paths into a portable workflow. The helper prints runtime, warnings, source/output hashes, and geometry counts, and writes a render report. Those counts are observations, not a comparison with the user's intended graph.

Ten original examples in `assets/graphviz/` cover the recurring structural families in the gallery catalog. Read the engine column in graphviz-patterns.md; do not assume every starter uses `dot`. Copy and adapt sources for real tasks, replacing every hypothetical entity and relationship. Example claims remain hypothetical. Large-graph `sfdp` remains catalog-driven because the tested runtimes did not provide a clean common execution path.

When native Graphviz is available, run `python scripts/validate-starters.py` to render all ten starters with their intended engines and verify SVG geometry plus node, edge, and cluster counts. This is structural validation; it does not replace final-size visual inspection.

### Large-graph compatibility gate

Do not infer usable `sfdp` support merely because the engine name is listed. On 2026-09-06, a 60-node/88-edge probe behaved differently across three Windows paths: Viz.js 3.25.0 (Graphviz 14.1.3) produced SVG with all graph elements but reported a triangulation-library error; Viz.js 3.30.0 (Graphviz 16.0.0) and the official portable Graphviz 15.1.1 Windows build terminated during the same layout. These results are specific probes, not a claim about every platform or input.

For a real large graph, test the selected runtime with a representative non-sensitive subset and reject crashes or error-level messages before the full render. Use a compatible maintained runtime or reduce the view to an explicitly disclosed subgraph. Do not silently replace `sfdp` with a layout that changes the analytical meaning or claim that an overview supports label-level reading.

## Export and QA

1. Keep DOT, render SVG, review warnings, and compare node/edge identities to the intended graph. Read the report as structural evidence only.
2. Inspect the SVG at the real reading size. Verify Korean text stays inside nodes, all conditions are legible, loops have correct targets, and field edges attach to the intended row.
3. For an HTML wrapper, keep the SVG aspect ratio and include a title, concise interpretation, legend when needed, and source/status note. Embed static SVG and DOT download data for a self-contained artifact; avoid remote dependencies if claiming offline support.
4. If rendering multiple SVGs inline, prefix IDs and any local ID references per graph, or isolate the SVGs as images. Duplicate `graph0`/`node1` IDs cause ambiguous DOM targeting.
5. Test the actual download and final document path. Check downstream font substitution/rasterization. Retain editable source and disclose any uninspected delivery format.

Sources: [Graphviz layout engines](https://graphviz.org/docs/layouts/), [splines](https://graphviz.org/docs/attrs/splines/), [HTML-like labels](https://graphviz.org/doc/info/shapes.html), [Viz.js API](https://viz-js.com/api/). Verified 2026-09-06; changing runtime versions requires fresh rendering checks.
