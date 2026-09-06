#!/usr/bin/env node
// Local DOT -> SVG. Does not install packages or claim visual QA.
import {readFile, writeFile, mkdir} from 'node:fs/promises';
import {resolve, dirname} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';

const usage = 'Usage: node render-graphviz.mjs input.dot output.svg [--engine dot|twopi|neato|fdp|sfdp|circo|osage|patchwork] [--viz-module /absolute/path/dist/viz.js]';
const hash = text => createHash('sha256').update(text).digest('hex');

async function main() {
  const args = process.argv.slice(2);
  if (args.includes('--help')) { console.log(usage); return; }
  if (args.length < 2) throw new Error(usage);
  const [input, output, ...options] = args;
  let engine = 'dot', modulePath;
  for (let i=0; i<options.length; i+=2) {
    if (!options[i+1]) throw new Error(usage);
    if (options[i] === '--engine') engine = options[i+1];
    else if (options[i] === '--viz-module') modulePath = options[i+1];
    else throw new Error(`Unknown option: ${options[i]}`);
  }
  if (!output.toLowerCase().endsWith('.svg')) throw new Error('Output must end in .svg');
  if (resolve(input) === resolve(output)) throw new Error('Source and output must differ');
  const {instance} = await import(modulePath ? pathToFileURL(resolve(modulePath)).href : '@viz-js/viz');
  const viz = await instance();
  if (!viz.engines.includes(engine)) throw new Error(`Unsupported engine: ${engine}`);
  const source = (await readFile(input,'utf8')).replace(/^\uFEFF/,'');
  const result = viz.render(source, {format:'svg',engine});
  const report = {
    source:resolve(input), output:resolve(output), engine,
    graphvizVersion:viz.graphvizVersion, sourceSha256:hash(source),
    renderStatus:result.status, messages:result.errors,
    visualInspection:'not_performed', semanticComparison:'not_performed'
  };
  if (result.status !== 'success') {
    console.error(JSON.stringify(report,null,2));
    throw new Error('Graphviz rendering failed; no new output written');
  }
  const svg = result.output;
  if (!svg.includes('<svg')) throw new Error('Renderer did not return SVG');
  report.outputSha256 = hash(svg);
  report.messageLevel = result.errors.some(e => e.level === 'error') ? 'error' : result.errors.length ? 'warning' : 'none';
  report.renderedNodes = (svg.match(/class="node"/g)||[]).length;
  report.renderedEdges = (svg.match(/class="edge"/g)||[]).length;
  report.renderedClusters = (svg.match(/class="cluster"/g)||[]).length;
  await mkdir(dirname(resolve(output)),{recursive:true});
  await writeFile(output,svg,'utf8');
  await writeFile(output+'.render.json',JSON.stringify(report,null,2)+'\n','utf8');
  console.log(JSON.stringify(report,null,2));
}
main().catch(error => {console.error(error.message); process.exitCode=1;});
