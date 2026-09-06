# Graphviz gallery decision catalog

Reviewed 2026-09-06. This catalog covers all 47 examples linked from the official Graphviz Gallery index on that date. Every page and available DOT source was retrieved; only Clusters, UML Class diagram demo, and Mind map of Happiness received direct representative browser-image inspection. `primary` means a strong structural starting point, `adapt` means useful after simplification, and `reference` means a technique/demo rather than an infographic template.

Use this catalog only after identifying the information structure. Run `scripts/select-graphviz-pattern.py` for a focused shortlist; then read the shortlisted official page/source. Do not load or imitate all 47 at once. Gallery examples have varied licenses and visual age; link for attribution and author an original diagram.

## Fast routing

| User situation | First candidates |
| --- | --- |
| Team/phase boundaries and handoffs | Clusters; Basic Git Concepts |
| Approval, retry, lifecycle, conditions | Finite Automaton; Traffic Lights |
| Build/code/model dependency DAG | Bazel; Ninja; Go Imports; Neural Network |
| Schema, fields, precise attachments | Data Structures; UML; Entity-Relation |
| Product/version/parse hierarchy | UNIX Tree; Math Parse Tree; Family Tree |
| Causal feedback model | World Dynamics |
| Shared-resource contention | Philosophers dilemma; Process |
| Network topology and routes | Switch Network; Intranet; Pandora FMS |
| Hundreds/thousands of relationships | sfdp Large Graph; gvmap clusters |
| Root-centered concept map | Mind map of Happiness |
| Renderer/layout/style experiment | Hello World; Grid; polygon/color/gradient references |

## 경계가 있는 흐름

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Clusters](https://graphviz.org/Gallery/directed/cluster.html) | `primary` | 팀·환경·단계별 경계 안팎으로 이동하는 업무나 데이터 | 실제 경계가 없는 단순 목록 | `dot`; clusters |

## 상태·업무 흐름

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Basic Git Concepts and Operations](https://graphviz.org/Gallery/directed/git.html) | `adapt` | 상태 저장소 사이를 명령이나 행동이 이동시키는 흐름 | 짧은 3단계 업무 흐름에 명령 설명까지 모두 넣기 | `dot`; html-labels, ports, rank-control, edge-labels, transparency |
| [Finite Automaton](https://graphviz.org/Gallery/directed/fsm.html) | `primary` | 조건·반복·종료 상태가 중요한 검증 또는 수명주기 | 조건이 없는 단순 순서 | `dot`; rank-control, edge-labels, custom-shapes |
| [Parsing tree](https://graphviz.org/Gallery/directed/psg.html) | `adapt` | 문법 상태·룩어헤드·전이처럼 노드 내부 정보가 많은 상태 그래프 | 일반 독자에게 파서 세부를 그대로 노출 | `dot`; html-labels, ports, rank-control, edge-labels |
| [Traffic Lights](https://graphviz.org/Gallery/neato/traffic_lights.html) | `primary` | 동시 사건과 제약을 가진 Petri net형 제어 흐름 | 단순 신호등 그림이나 일반 타임라인 | `neato`; custom-shapes |

## 시스템·의존성

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Bazel Build System](https://graphviz.org/Gallery/directed/bazel.html) | `adapt` | 빌드 대상과 산출물의 큰 방향성 의존성 | 비기술 독자용 한 장 요약 또는 순차 프로세스 | `dot`; basic layout |
| [Go Package Imports](https://graphviz.org/Gallery/directed/go-package.html) | `adapt` | 패키지 import와 전이 의존성을 링크 가능한 맵으로 표시 | 버전·방향을 확인하지 않은 코드 관계 | `dot`; urls |
| [Linux Kernel Diagram](https://graphviz.org/Gallery/directed/Linux_kernel_diagram.html) | `adapt` | 여러 계층과 교차 연결을 가진 대형 시스템 아키텍처 | 작은 지면에 전체 구조를 축소하거나 확인하지 않은 계층을 추가 | `dot`; rank-control, edge-labels, transparency, urls, custom-shapes |
| [Neural Network (Keras)](https://graphviz.org/Gallery/directed/neural-network.html) | `primary` | 분기와 병합이 있는 모델·파이프라인 아키텍처 | 학습 성능이나 텐서 크기를 확인하지 않고 표시 | `dot`; record-nodes, rank-control |
| [Ninja Build System](https://graphviz.org/Gallery/directed/ninja.html) | `adapt` | 파일·작업·산출물의 빌드 DAG | 업무 담당자 흐름을 파일 의존성처럼 표시 | `dot`; rank-control, edge-labels, custom-shapes |
| [Module Dependencies](https://graphviz.org/Gallery/neato/softmaint.html) | `primary` | 변경 영향과 독립적으로 시험할 모듈 묶음 탐색 | 자동 배치만으로 테스트 독립성을 단정 | `neato`; custom-shapes |

## 성능·호출 관계

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [pprof CPU Profile](https://graphviz.org/Gallery/directed/pprof.html) | `primary` | 측정된 호출 관계와 비용을 함께 보여주는 프로파일 | 측정값 없이 선 굵기·색으로 성능을 암시 | `dot`; clusters, edge-labels |
| [Program Profile](https://graphviz.org/Gallery/directed/profile.html) | `adapt` | 함수 호출과 측정된 실행 비용의 전체 흐름 | 정적 아키텍처와 런타임 프로파일을 혼동 | `dot`; basic layout |

## 데이터 모델·구획

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Data Structures](https://graphviz.org/Gallery/directed/datastruct.html) | `primary` | 포인터·필드·하위 항목이 있는 복합 데이터 구조 | 텍스트 문단을 억지로 작은 칸에 나누기 | `dot`; rank-control |
| [UML Class diagram demo](https://graphviz.org/Gallery/directed/UML_Class_diagram.html) | `primary` | 클래스·인터페이스·구성 요소의 구획과 필드별 연결 | UML 의미를 모른 채 삼각형·다이아몬드 화살표를 장식으로 사용 | `dot`; html-labels, record-nodes, ports, edge-labels, custom-shapes |
| [Entity-Relation Data Model](https://graphviz.org/Gallery/neato/ER.html) | `primary` | 엔터티·속성·관계와 확인된 카디널리티 | 원인·절차 화살표 또는 추정 카디널리티 | `neato`; edge-labels, custom-shapes |

## 계층·계보

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Family Tree](https://graphviz.org/Gallery/directed/kennedyanc.html) | `adapt` | 사진을 포함한 조상·후손 중심 계보 | 동의 없는 개인정보나 살아 있는 가족 정보 공개 | `dot`; images, custom-shapes |
| [Math Parse Tree](https://graphviz.org/Gallery/directed/Genetic_Programming.html) | `primary` | 수식·표현식·규칙의 트리형 분해 | 순환·다중 부모 관계 | `dot`; basic layout |
| [Racehorse Pedigree](https://graphviz.org/Gallery/directed/lion_share.html) | `adapt` | 부모 쌍과 자손 관계가 필요한 pedigree | 일반 조직도를 혼인·교배 표기로 표현 | `dot`; custom-shapes |
| [Siblings](https://graphviz.org/Gallery/directed/siblings.html) | `adapt` | 세대·연결 링크가 있는 비공식 계보 또는 멘토 계열 | 공식 조직의 보고 관계로 오해시킬 배치 | `dot`; urls |
| [UNIX Family 'Tree'](https://graphviz.org/Gallery/directed/unix.html) | `primary` | 제품·기술·버전의 장기 계보와 분기 | 현재 지원 상태나 호환성을 계보만으로 판단 | `dot`; basic layout |

## 인과·시스템 모델

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [World Dynamics](https://graphviz.org/Gallery/directed/world.html) | `primary` | 상호 영향을 주는 변수와 피드백의 개념 모델 | 상관관계를 검증 없이 인과 화살표로 승격 | `dot`; rank-control |

## 자원 경합·동시성

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Philosophers dilemma. Neato layout.](https://graphviz.org/Gallery/neato/philo.html) | `primary` | 여러 행위자가 공유 자원을 경쟁하는 교착 구조 | 일반 협업 문제를 교착으로 과장 | `neato`; custom-shapes |
| [Process](https://graphviz.org/Gallery/neato/process.html) | `adapt` | 프로세스·자원·연결처럼 대칭적인 시스템 관계 | 방향·순서가 핵심인 절차 | `neato`; basic layout |

## 네트워크·경로

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Switch Network](https://graphviz.org/Gallery/directed/switch.html) | `primary` | 분할기·선택기와 병렬 경로가 있는 스위칭 구조 | 동시에 존재하지 않는 경로를 병렬로 표현 | `dot`; rank-control, custom-shapes |
| [Synchronous Digital Hierarchy](https://graphviz.org/Gallery/directed/sdh.html) | `adapt` | 한 그래프에 여러 종류의 의미 관계가 공존하는 통신 구조 | 선 종류의 범례 없이 복잡한 관계를 표시 | `dot`; rank-control, custom-shapes |
| [Intranet Layout](https://graphviz.org/Gallery/undirected/save/inet.html) | `adapt` | 내부망 토폴로지와 완전 연결 하위 집합 | 보안 경계·접근 권한을 연결선만으로 추정 | `auto`; basic layout |
| [A Network Map](https://graphviz.org/Gallery/twopi/twopi2.html) | `adapt` | 한 중심 또는 권역을 기준으로 장애 추적용 대형 네트워크 맵 | 정확한 지리 거리·대역폭을 방사 거리로 해석 | `twopi`; edge-labels, urls |
| [Network Map by Pandora FMS](https://graphviz.org/Gallery/twopi/networkmap_twopi.html) | `adapt` | 네트워크 탐색 결과와 호스트 경로의 계층적 지도 | 실제 접근 가능성·보안 상태를 자동으로 추정 | `twopi`; html-labels, urls |

## 네트워크·대규모 관계

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Cluster relations in a graph highlighted using gvmap](https://graphviz.org/Gallery/undirected/gd_1994_2007.html) | `primary` | 큰 관계망에서 커뮤니티 영역을 찾아 배경으로 구분 | 군집 알고리즘 결과를 공식 조직·원인으로 단정 | `auto`; transparency, fixed-position |
| [Undirected Graph Clusters](https://graphviz.org/Gallery/undirected/fdpclust.html) | `primary` | 노드-그룹·그룹-그룹 관계가 있는 비방향 클러스터 | 방향이 필요한 승인·데이터 흐름 | `fdp`; basic layout |
| [Undirected Large Graph Layout Using sfdp](https://graphviz.org/Gallery/undirected/root.html) | `primary` | 수백~수천 노드 관계망의 전체 구조 탐색 | 작은 문서에 전체를 축소하거나 세부 판독을 약속 | `sfdp`; edge-labels, urls |

## 개념·마인드맵

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Mind map of Happiness](https://graphviz.org/Gallery/twopi/happiness.html) | `primary` | 중심 개념과 같은 수준의 주제 가지 | 중요도·성과를 반지름이나 면적으로 암시 | `twopi`; edge-labels, transparency, urls, custom-shapes |

## 레이아웃·진단

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Hello World](https://graphviz.org/Gallery/directed/hello.html) | `reference` | Graphviz 설치·렌더 파이프라인의 최소 동작 확인 | 실제 인포그래픽 설계의 출발 템플릿 | `dot`; basic layout |
| [Polygons](https://graphviz.org/Gallery/directed/crazy.html) | `reference` | 도형·색상 렌더러 스트레스 테스트와 shape 참고 | 업무 의미 없이 특이한 도형을 장식으로 채택 | `dot`; custom-shapes |
| [Grid](https://graphviz.org/Gallery/undirected/grid.html) | `reference` | 노드를 엄격한 격자에 고정해야 하는 보드·경로 배치 | 보이지 않는 선을 실제 관계처럼 해석하거나 자유 네트워크에 강제 | `dot`; rank-control, custom-shapes |

## 스타일·색상 참고

| Example | Role | Use when | Avoid when | Engine / techniques |
| --- | --- | --- | --- | --- |
| [Color wheel, 33 colors. Neato layout](https://graphviz.org/Gallery/neato/color_wheel.html) | `reference` | 범주 팔레트와 색상 구분 가능성을 시험 | 33색을 실제 인포그래픽에 그대로 사용 | `neato`; edge-labels, transparency, custom-shapes |
| [Partially Transparent Colors](https://graphviz.org/Gallery/neato/transparency.html) | `reference` | 겹침·강조를 위한 투명도 동작 확인 | 낮은 대비의 핵심 선·텍스트 | `neato`; transparency, custom-shapes |
| [Twelve colors, neato layout](https://graphviz.org/Gallery/neato/colors.html) | `reference` | 작은 범주 팔레트와 투명도 조합 시험 | 색으로만 범주나 상태를 구별 | `neato`; transparency, custom-shapes |
| [Cluster Gradients](https://graphviz.org/Gallery/gradient/cluster.html) | `reference` | 그룹 배경에 절제된 방향성 색 변화를 시험 | 그라데이션으로 그룹 의미를 대신 | `auto`; clusters, gradients, transparency |
| [Gradient Linear Angles](https://graphviz.org/Gallery/gradient/linear_angle.html) | `reference` | 선형 그라데이션 방향과 각도 비교 | 데이터 방향을 근거 없이 색 방향으로 암시 | `auto`; html-labels, gradients |
| [Gradient Radial Angles](https://graphviz.org/Gallery/gradient/radial_angle.html) | `reference` | 방사형 그라데이션 중심과 각도 시험 | 중심성·강도를 정량 의미처럼 표현 | `auto`; html-labels, gradients |
| [Gradients Applied to Data Struct Example](https://graphviz.org/Gallery/gradient/datastruct.html) | `reference` | 구획 노드에 그라데이션을 적용했을 때 가독성 확인 | 필드 경계보다 장식이 강해지는 스타일 | `auto`; rank-control, gradients |
| [Graph, Cluster and Node Gradients](https://graphviz.org/Gallery/gradient/g_c_n.html) | `reference` | 페이지·그룹·노드 세 수준의 색 배경 조합 시험 | 모든 수준에 강한 그라데이션을 동시 사용 | `auto`; gradients |
| [Linear and Radial Gradient Angles](https://graphviz.org/Gallery/gradient/angles.html) | `reference` | 선형·방사형 표현을 여러 도형에서 비교 | 예제 도형과 색을 하나의 실무 화면에 모두 사용 | `auto`; clusters, gradients, custom-shapes |
| [Sample Gradient Color Schemes](https://graphviz.org/Gallery/gradient/colors.html) | `reference` | 그라데이션 팔레트 후보를 렌더러에서 비교 | 대비·브랜드 검토 없이 예제 팔레트 채택 | `auto`; clusters, gradients |
| [Table and Cell Gradients](https://graphviz.org/Gallery/gradient/table.html) | `reference` | HTML-like 표와 셀 배경의 렌더링 확인 | 데이터 셀마다 장식적 색을 달리해 표 판독 방해 | `auto`; html-labels, gradients |

## Verification boundary

The catalog proves that each indexed page was retrieved and assigned a use/avoid decision. It does not prove every historical example is aesthetically suitable, licensed for redistribution, deterministic across Graphviz versions, or legible after Korean relabeling. Open and render the selected source with the current runtime, then apply the skill's topology and final-size checks.
