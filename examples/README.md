# Original Graphviz starters

`assets/graphviz/`의 편집 가능한 DOT를 Graphviz 15.1.1 Windows portable로 렌더링한 예시입니다. GitHub 다크·라이트 모드에서 모두 읽히도록 이 미리보기 SVG에만 흰 배경을 적용했습니다. 모두 구조 설명용 가상 데이터이며 회사·제품·성능에 관한 실제 주장이 아닙니다.

| 상황 | DOT | 렌더 결과 | 엔진 |
| --- | --- | --- | --- |
| 호출 비용과 병목 | [call-profile.dot](../assets/graphviz/call-profile.dot) | [SVG](rendered/call-profile.svg) | `dot` |
| 인과 피드백 가설 | [causal-feedback.dot](../assets/graphviz/causal-feedback.dot) | [SVG](rendered/causal-feedback.svg) | `neato` |
| 책임 경계와 전달 | [clustered-workflow.dot](../assets/graphviz/clustered-workflow.dot) | [SVG](rendered/clustered-workflow.svg) | `dot` |
| 분기·병합 의존성 | [dependency-dag.dot](../assets/graphviz/dependency-dag.dot) | [SVG](rendered/dependency-dag.svg) | `dot` |
| 버전·제품 계보 | [hierarchy-lineage.dot](../assets/graphviz/hierarchy-lineage.dot) | [SVG](rendered/hierarchy-lineage.svg) | `dot` |
| 네트워크 토폴로지 | [network-topology.dot](../assets/graphviz/network-topology.dot) | [SVG](rendered/network-topology.svg) | `twopi` |
| 중심 개념과 가지 | [radial-map.dot](../assets/graphviz/radial-map.dot) | [SVG](rendered/radial-map.svg) | `twopi` |
| 필드 단위 연결 | [record-ports.dot](../assets/graphviz/record-ports.dot) | [SVG](rendered/record-ports.svg) | `dot` |
| 공유 자원 경합 | [resource-contention.dot](../assets/graphviz/resource-contention.dot) | [SVG](rendered/resource-contention.svg) | `neato` |
| 상태·보완·재검토 | [state-review.dot](../assets/graphviz/state-review.dot) | [SVG](rendered/state-review.svg) | `dot` |

## 수정 순서

1. 예제의 가상 엔터티와 관계를 실제 확인된 내용으로 전부 교체합니다.
2. 화살표가 순서, 의존성, 데이터 이동, 영향 중 무엇을 뜻하는지 정합니다.
3. 클러스터·색·도형에는 한 가지 일관된 의미만 부여합니다.
4. `python scripts/validate-starters.py`로 구조를 확인합니다.
5. 최종 사용 크기에서 한글 넘침, 선 겹침, 화살표 방향과 대비를 직접 봅니다.

렌더 성공과 의미가 맞다는 판단은 다릅니다. 실제 콘텐츠로 바꾼 뒤에는 원래 예제의 예상 노드·연결선 수가 더 이상 수락 기준이 아니므로, 의도한 관계 목록과 새 결과를 다시 대조해야 합니다.
