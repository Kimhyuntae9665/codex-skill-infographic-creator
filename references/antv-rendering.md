# AntV rendering and export

Use with antv-syntax.md. Runtime pin: `https://unpkg.com/@antv/infographic@0.2.20/dist/infographic.min.js`.

Create a complete UTF-8 HTML document with source-language `lang`, a meaningful title, a container with real width/height (not a percentage of an undefined parent), and a visible export button. Initialize `new AntVInfographic.Infographic({container:'#container', width:'100%', height:'100%'})` and call `render(syntax)`.

- Await fonts and re-render as needed; then check completion and glyph/icon visibility. Method return does not establish that asynchronous icons are ready.
- Export with `await infographic.toDataURL({type:'svg'})`; attach to a download link and verify the same visual opens. Display loading/error states instead of allowing an empty export.
- Serialize DSL safely, including escaping closing script tags; use textContent for labels outside the renderer. Do not insert raw user content into executable JavaScript/HTML.
- Verify unfamiliar templates against the pin. Unsupported templates/fields must be fixed or changed explicitly; do not silently drop content.
- Check selected icons. Use a verified ID or consistent vector replacement if resolution fails. Do not force an icon into every technical node.
- Use a stable artboard with responsive containment. At narrow widths, allow explicit zoom/scroll or use a simpler layout rather than unreadably shrinking the graph. Avoid accidental page overflow.
- CDN HTML requires network access. For offline delivery, bundle runtime/fonts/icons or deliver self-contained static SVG/HTML with source and download. Do not label a CDN-dependent file offline.
- SVG may contain foreignObject, filters, or symbols; test the actual document converter. Keep editable DSL if raster fallback is needed.

For integrated artifacts, follow document-integration.md. HTML-preview success does not validate the exported PDF.
