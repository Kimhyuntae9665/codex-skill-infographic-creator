#!/usr/bin/env python3
"""Validate the reviewed gallery index and local starter/reference integrity."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "graphviz-gallery-index.json"
CATALOG = ROOT / "references" / "graphviz-gallery-catalog.md"

def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    rows = data["rows"]
    assert data["entry_count"] == 47 == len(rows)
    assert len({row["title"] for row in rows}) == 47
    assert len({row["url"] for row in rows}) == 47
    assert all(row["reviewed"]["page"] for row in rows)
    assert all(row["source_url"] and row["reviewed"]["dot_source"] for row in rows)
    assert all(row["situation"] and row["fit_when"] and row["avoid_when"] and row["keywords"] for row in rows)
    markdown = CATALOG.read_text(encoding="utf-8")
    assert all(f'[{row["title"]}]({row["url"]})' in markdown for row in rows)
    checked = [ROOT / "SKILL.md", *ROOT.glob("references/*.md")]
    for file in checked:
        for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            local = file.parent / target.split("#", 1)[0]
            assert local.exists(), f"Broken local link in {file}: {target}"
    starters = sorted((ROOT / "assets" / "graphviz").glob("*.dot"))
    assert len(starters) == 10, len(starters)
    print("PASS: 47 unique reviewed gallery entries, complete readable catalog, local links, and 10 original starters.")

if __name__ == "__main__":
    main()
