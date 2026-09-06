#!/usr/bin/env python3
"""Rank the reviewed Graphviz gallery catalog for a concrete information-design query."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

INDEX = Path(__file__).resolve().parents[1] / "references" / "graphviz-gallery-index.json"

INTENTS = {
    "boundary": {"팀", "책임", "부서", "단계", "환경", "영역", "경계", "handoff", "cluster", "swimlane"},
    "state": {"상태", "승인", "거절", "조건", "재시도", "반복", "완료", "lifecycle", "fsm", "transition"},
    "dependency": {"의존성", "빌드", "패키지", "모듈", "영향", "dag", "dependency", "import", "pipeline", "레이어"},
    "schema": {"스키마", "필드", "속성", "엔터티", "데이터", "클래스", "인터페이스", "구획", "schema", "uml", "er"},
    "hierarchy": {"계층", "트리", "조직", "계보", "버전", "부모", "자식", "파싱", "tree", "hierarchy", "lineage"},
    "causal": {"인과", "피드백", "변수", "영향", "시스템", "causal", "feedback", "dynamics"},
    "contention": {"경합", "교착", "공유", "자원", "동시성", "deadlock", "contention", "resource"},
    "network": {"네트워크", "경로", "호스트", "토폴로지", "통신", "스위치", "route", "network", "topology"},
    "large": {"대규모", "수백", "수천", "커뮤니티", "군집", "large", "community", "sfdp", "gvmap"},
    "mindmap": {"마인드맵", "중심", "개념", "주제", "분류", "mindmap", "radial", "concept"},
    "profile": {"성능", "병목", "호출", "cpu", "시간", "profile", "callgraph", "pprof", "gprof"},
    "layout": {"격자", "고정", "배치", "테스트", "렌더", "grid", "layout", "shape", "smoke"},
    "style": {"색상", "그라데이션", "투명도", "팔레트", "스타일", "color", "gradient", "palette", "transparency"},
}

SITUATION_INTENT = {
    "경계가 있는 흐름": "boundary", "상태·업무 흐름": "state", "시스템·의존성": "dependency",
    "성능·호출 관계": "profile", "데이터 모델·구획": "schema", "계층·계보": "hierarchy",
    "인과·시스템 모델": "causal", "자원 경합·동시성": "contention", "네트워크·경로": "network",
    "네트워크·대규모 관계": "large", "개념·마인드맵": "mindmap", "레이아웃·진단": "layout",
    "스타일·색상 참고": "style",
}

def tokens(text: str) -> set[str]:
    return {x for x in re.findall(r"[0-9A-Za-z가-힣]+", text.lower()) if len(x) > 1}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Information-design situation in Korean or English")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(INDEX.read_text(encoding="utf-8"))
    query_tokens = tokens(args.query)
    normalized_query = args.query.lower()
    active_intents = {
        name for name, words in INTENTS.items()
        if query_tokens & words or any(word in normalized_query for word in words if len(word) >= 2)
    }
    style_query = bool(active_intents & {"style", "layout"})
    ranked = []
    for row in catalog["rows"]:
        searchable = " ".join([row["title"], row["situation"], row["fit_when"], " ".join(row["keywords"]), " ".join(row["features"])]).lower()
        row_tokens = tokens(searchable)
        overlap = query_tokens & row_tokens
        score = len(overlap) * 4
        row_intent = SITUATION_INTENT[row["situation"]]
        if row_intent in active_intents:
            score += 12
        if score > 0:
            if row["role"] == "primary":
                score += 3
            elif row["role"] == "reference" and not style_query:
                score -= 7
        if row["title"].lower() in args.query.lower():
            score += 20
        if score > 0:
            ranked.append((score, row))
    ranked.sort(key=lambda x: (-x[0], x[1]["title"]))
    selected = [{"score": score, **row} for score, row in ranked[:max(1, args.limit)]]
    if not selected and not args.json:
        print("No strong catalog match. Identify direction, boundaries, conditions, and scale before choosing a layout.")
        return
    if args.json:
        print(json.dumps({"query": args.query, "active_intents": sorted(active_intents), "results": selected}, ensure_ascii=False, indent=2))
        return
    print(f"Query: {args.query}")
    print(f"Detected: {', '.join(sorted(active_intents)) or 'general relationship'}")
    for i, row in enumerate(selected, 1):
        print(f"{i}. {row['title']} [{row['role']}; {row['engine']}] score={row['score']}")
        print(f"   Use: {row['fit_when']}")
        print(f"   Avoid: {row['avoid_when']}")
        print(f"   Source: {row['url']}")

if __name__ == "__main__":
    main()
