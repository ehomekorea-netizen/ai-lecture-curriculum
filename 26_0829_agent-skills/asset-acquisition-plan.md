# Asset Acquisition Plan: AI 에이전트 SKILL 2시간 마스터 코스

본 문서는 `course-brief.md`, `S01-deck-brief.md`, `S02-deck-brief.md`에서 참조하는 모든 시각 에셋 슬롯(`AST-TBD-*`)의 요구 사양, 제작 방식 및 대체안(Fallback)을 정의합니다. (Plan-first 모드)

---

## 1. Asset Slots Summary

| Priority | Slot ID | Session / Slide | Visual Job (역할) | Required Asset | Composition / Minimum Spec | Acquisition Route / Generation Brief | Fallback | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **P0** | `AST-TBD-01` | S01 / S03 | 전통적 프롬프트 vs SKILL 패키지 개념 대비 | 비교 다이어그램 (SVG) | 16:9 다크 테마, 좌: 반복 입력의 한계, 우: 패키지화된 SOP 폴더 구조 | 인라인 SVG 또는 Mermaid 다이어그램 작성 | 텍스트 기반 비교 카드 | planned |
| **P0** | `AST-TBD-02` | S01 / S04 | 점진적 로딩(Progressive Disclosure) 아키텍처 | 2단계 로딩 흐름도 (SVG) | 세션 시작 시 100토큰(이름/설명) 로드 → 키워드 트리거 시 전체 지침 온디맨드 로드 | 인라인 SVG 그래픽 | Mermaid graph LR | planned |
| **P1** | `AST-TBD-03` | S01 / S06 | `SKILL.md` 표준 폴더 및 코드 구조 | IDE 코드 뷰 / 디렉토리 트리 | 16:9 비율, 다크 테마 에디터 룩, YAML frontmatter + Markdown 본문 하이라이트 | Slidev 코드 블록 하이라이트 (`lang="yaml" / lang="md"`) | 마크다운 코드 블록 | planned |
| **P1** | `AST-TBD-04` | S01 / S09 | [실습 P01] 템플릿 및 단계별 작성 가이드 | 3단계 실습 안내 카드 UI | 3열 글래스 카드: ① 요구분석 → ② YAML 정의 → ③ 본문 절차 기술 | Slidev 그리드 컴포넌트 (`grid grid-cols-3`) | 텍스트 불릿 목록 | planned |
| **P0** | `AST-TBD-05` | S02 / S03 | SKILL vs Plugin vs MCP 3자 비교 매트릭스 | 3자 역할 분담 다이어그램 | 3개 영역(지침서 vs 도구상자 vs 통신규격)과 데이터 흐름을 보여주는 인포그래픽 | Vue 커스텀 글래스 카드 또는 인라인 SVG | 마크다운 비교 테이블 | planned |
| **P0** | `AST-TBD-06` | S02 / S05 | SKILL + MCP 커넥터 + 외부 API 데이터 파이프라인 | End-to-End 시퀀스 다이어그램 | User → Claude → Skill → MCP Connector → REST API → Claude → User 6단계 흐름 | Mermaid sequenceDiagram 또는 인라인 SVG | 텍스트 단계 설명 | planned |
| **P1** | `AST-TBD-07` | S02 / S08 | 엔터프라이즈 모니터링 & 보안 스캔 대시보드 룩 | 대시보드 UI 목업 (카드형) | 4개 핵심 지표(호출량, 응답지연, 성공률, 보안경고) 모니터링 위젯 UI | Slidev 글래스 UI 위젯 (Tailwind CSS) | 마크다운 메트릭 표 | planned |
| **P1** | `AST-TBD-08` | S02 / S10 | [실습 P02] 에러 핸들링 및 Mock 연동 구조 | 인터랙티브 실습 가이드 다이어그램 | 입력 → 정상 분기 vs API 오류/권한 에러 분기 Fallback 시각화 | Slidev 분기 다이어그램 (SVG/Mermaid) | 의사코드(Pseudocode) 블록 | planned |

---

## 2. Implementation Guidelines for Downstream Agent (`$nekomeowww-slidev-deck`)

1. **외부 이미지 의존성 최소화:** 위 에셋들은 외부 유료 스톡 이미지를 찾을 필요 없이 Slidev 내장 컴포넌트(Tailwind CSS, Grid, Mermaid, 인라인 SVG, 코드 하이라이트)로 100% 렌더링 가능하도록 설계되었습니다.
2. **다크 모드 일관성:** 모든 다이어그램과 UI 카드는 배경 `#0B0F19`에 어울리는 반투명 글래스(`bg-white/5 border border-white/10 backdrop-blur-md`)와 시안(`#06b6d4`), 에메랄드(`#10b981`), 바이올렛(`#8b5cf6`) 포인트 컬러를 사용합니다.
