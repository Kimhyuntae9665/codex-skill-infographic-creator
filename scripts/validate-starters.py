#!/usr/bin/env python3
"""Render and structurally validate the ten original Graphviz starter files."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "graphviz"
EXPECTED = {
    "call-profile": ("dot", 5, 4, 0),
    "causal-feedback": ("neato", 4, 4, 0),
    "clustered-workflow": ("dot", 5, 5, 2),
    "dependency-dag": ("dot", 6, 6, 0),
    "hierarchy-lineage": ("dot", 6, 5, 0),
    "network-topology": ("twopi", 8, 7, 0),
    "radial-map": ("twopi", 5, 4, 0),
    "record-ports": ("dot", 2, 3, 0),
    "resource-contention": ("neato", 5, 4, 0),
    "state-review": ("dot", 4, 4, 0),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dot", help="Path to Graphviz dot executable; defaults to PATH")
    args = parser.parse_args()
    executable = args.dot or shutil.which("dot")
    if not executable:
        raise SystemExit("Graphviz dot executable was not found. Install Graphviz or pass --dot.")

    with tempfile.TemporaryDirectory(prefix="infographic-starters-") as tmp:
        output_dir = Path(tmp)
        for stem, (engine, nodes, edges, clusters) in EXPECTED.items():
            source = ASSETS / f"{stem}.dot"
            output = output_dir / f"{stem}.svg"
            run = subprocess.run(
                [executable, f"-K{engine}", "-Tsvg", str(source), "-o", str(output)],
                text=True,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            )
            if run.returncode != 0 or "error:" in run.stderr.lower():
                raise SystemExit(f"{stem}: render failed\n{run.stderr.strip()}")
            root = ET.parse(output).getroot()
            groups = list(root.iter("{http://www.w3.org/2000/svg}g"))
            actual = tuple(
                sum(group.attrib.get("class") == kind for group in groups)
                for kind in ("node", "edge", "cluster")
            )
            expected = (nodes, edges, clusters)
            if actual != expected:
                raise SystemExit(f"{stem}: expected node/edge/cluster {expected}, got {actual}")
            view_box = root.attrib.get("viewBox", "").split()
            if len(view_box) != 4 or float(view_box[2]) <= 0 or float(view_box[3]) <= 0:
                raise SystemExit(f"{stem}: invalid SVG viewBox {view_box}")
            if not any("가" <= char <= "힣" for char in "".join(root.itertext())):
                raise SystemExit(f"{stem}: expected Korean teaching labels were not retained")

    print("PASS: 10 starters rendered with exact node/edge/cluster counts and valid SVG geometry.")


if __name__ == "__main__":
    main()
