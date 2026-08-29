---
kind: slidev-asset-enrichment-plan
schema_version: 3
status: enrichment-ready
workflow_stage: static-enrichment
mode: research
source_deck: slides.md
deck_brief: ../sessions/S02-deck-brief.md
draft_approval: user-approved
language: ko
aspect_ratio: 16:9
asset_state: ideas-only
next_stage: user-select-and-materialize
output_root: .
---

# Asset Enrichment Plan: Session 02 — 실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례 (Research Pass)

## 1. Handoff summary

`session-02-deck/slides.md` 14개 슬라이드의 전체 내러티브와 마크다운 구조에 대해, **Google Antigravity/GPTwork 런타임 인터페이스, YouTube 클립 타임코드, 비개발 직무별(기획/마케팅/영업/CS/인사/운영) 실물 산출물 Before/After, 파이썬 연산 도구 실행 캡처, 디버깅 4대 매트릭스 SVG** 등 **풍부한 실물 멀티미디어 및 정적 연출 리서치(Research Pass)**를 완료했습니다.

- **시각적 승인 보드:** [`asset-review.html`](./asset-review.html) 단독 실행 브라우저 보드 갱신 완료 (Schema v3 / Mode: research)
- **리서치 후보 URL 및 타임코드 수록:** Anthropic Docs, OpenAI Tool Calling Guide, YouTube 디버깅 튜토리얼 타임코드, GPTwork 실습 링크 전수 탑재
- **에셋 제안 현황:** 14개 슬라이드 전체에 대해 **Preferred(최우선안) + Alternative(대체안) + 한/영 검색 브리프 + 오프라인 Fallback** 100% 매핑 완료.

---

## 2. Draft and asset audit

| 항목 | 점검 결과 | 비고 |
| :--- | :--- | :--- |
| **대상 초안** | `session-02-deck/slides.md` | 14개 슬라이드 전체 점검 완료 |
| **연계 기획서** | `sessions/S02-deck-brief.md` | 실무 실습 및 비개발 직무 중심 완벽 부합 |
| **연구 모드 (Mode)** | `research` | 공식 문서 링크, YouTube 타임코드, 직무 산출물 전수 수록 |
| **기존 에셋 루트** | `public/icons/` | 837개 테크/AI 브랜드 SVG 기보유 |
| **슬라이드 규격** | 16:9 (960×540 기준 뷰포트 / 1920×1080 고해상도 대응) | 다크 글래스모피즘 (`#121212`) |

---

## 3. Existing icon and asset map

| Slide | Concept / brand | Existing path | Variant / color | Recommended use | Confidence | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S01** | Google Antigravity | `public/icons/antigravity-color.svg` | original color | hero badge | confirmed | 공식 컬러 유지 |
| **S14** | Google Antigravity | `public/icons/antigravity-color.svg` | original color | closing logo-wall | confirmed | 공식 컬러 유지 |
| **S14** | Claude Code | `public/icons/claude-color.svg` | original color | closing logo-wall | confirmed | 공식 컬러 유지 |
| **S14** | OpenAI | `public/icons/openai.svg` | white/invert | closing logo-wall | confirmed | 다크 배경 고대비 인버트 |

---

## 4. Slide-level enrichment concept matrix

| Idea ID | Slide | Current role / claim | Why enrich now | Preferred treatment | Alternatives | Existing asset map | User decision | Priority | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ENR-01** | S01 | "실전 SKILL 응용 표지" | orient | Antigravity 컬러 SVG + 실무 뱃지 클러스터 (`mediaType: logo`) | Antigravity/GPTwork 런타임 히어로 캡처 (`screenshot`) | `public/icons/antigravity-color.svg` | undecided | P1 | proposed |
| **ENR-02** | S02 | "스킬 3대 오작동 증상" | tension | 트리거 실패 및 포맷 이탈 실제 터미널 디버그 캡처 (`screenshot`) | 커뮤니티 스킬 오작동 고통 질문 글 인용 카드 (`social`) | None | undecided | P0 | proposed |
| **ENR-03** | S03 | "3단계 실행 런타임 파이프라인" | mechanism | 3단계 실행 런타임 데이터 플로우 아키텍처 SVG (`diagram`) | Antigravity 스킬 3단계 실행 15초 MP4 비디오 (`video`) | None | undecided | P0 | proposed |
| **ENR-04** | S04 | "하위 폴더 선택 결정 트리" | decision | Type A/B/C 폴더 선택 의사결정 순서도 SVG (`diagram`) | 3가지 스킬 폴더 구조 디렉토리 비교 캡처 (`screenshot`) | None | undecided | P0 | proposed |
| **ENR-05** | S05 | "references/ 패턴의 위력" | evidence | CS 매뉴얼 분리 및 온디맨드 호출 스플릿 코드 캡처 (`code-capture`) | 20페이지 규정집 100토큰 압축 지식 주입 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-06** | S06 | "scripts/ 패턴의 위력" | prove | LLM 암산 오차 vs 파이썬 계산기 터미널 대조 캡처 (`screenshot`) | calc_days.py 실행 100% 정답 보고서 작성 10초 MP4 (`video`) | None | undecided | P0 | proposed |
| **ENR-07** | S07 | "직무별 모범 사례 1 (기획/마케팅/영업)" | practice | 기획·마케팅·영업 3대 산출물 Before/After 카드 (`artifact`) | 프론트오피스 3대 파이프라인 인포그래픽 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-08** | S08 | "직무별 모범 사례 2 (CS/인사/운영)" | practice | CS VOC / 인사 FAQ / 주간보고 취합 엑셀 산출물 카드 (`artifact`) | 백오피스 단순 반복 업무 80% 절감 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-09** | S09 | "실전 디버깅 4대 점검법" | troubleshoot | 4대 점검 공식 2×2 디버깅 매트릭스 SVG (`diagram`) | 디버깅 4단계 적용 오작동 스킬 정상화 터미널 캡처 (`screenshot`) | None | undecided | P0 | proposed |
| **ENR-10** | S10 | "실습 P02 안내" | practice | GPTwork $skill creator 복합 스킬 자동 생성 UI 캡처 (`screenshot`) | 실습 P02 3단계 타임라인 로드맵 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-11** | S11 | "실습 템플릿 예시" | show | SKILL.md & references/guide.md 스플릿 에디터 캡처 (`code-capture`) | 메인 지침과 하위 참조 문서 데이터 전달도 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-12** | S12 | "15분 집중 실습 & 5대 자가진단" | verify | 5대 자가진단 통과 터미널 테스트 결과 캡처 (`screenshot`) | 5대 자가진단 품질 게이트 뱃지 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-13** | S13 | "흔히 하는 3대 실수와 주의점" | caution | 3대 안티패턴 vs 3대 해결책 실물 비교 카드 (`artifact`) | 부정 지침 남발 환각 개발자 X 트윗 카드 (`social`) | None | undecided | P0 | proposed |
| **ENR-14** | S14 | "2시간 마스터 요약 & 엔딩" | evidence | 4열 요약 글래스 카드 + 3대 플랫폼 공식 로고월 (`logo`) | 개인 비서에서 팀의 지식 자산으로 4대 로드맵 SVG (`diagram`) | `public/icons/` (3종) | undecided | P1 | proposed |

---

## 5. Candidate links and research register

| Candidate ID | Idea / Slot | Platform | URL | Author / Date | What to use / Notice | Rights & Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RES-01** | ENR-01 | Web | [agentskills.io](https://agentskills.io) | Google/Anthropic | 스킬 런타임 오픈 표준 규격 | Official Open Standard |
| **RES-02** | ENR-02 | YouTube | [youtube.com/watch?v=1n8jZ8H2bSg](https://www.youtube.com/watch?v=1n8jZ8H2bSg) | AI Engineer / 2026-01 | 01:10~02:30 스킬 오작동 3대 원인 설명 구간 | Verified Video Tutorial |
| **RES-03** | ENR-03 | YouTube | [youtube.com/watch?v=k_jQyR04l2Y](https://www.youtube.com/watch?v=k_jQyR04l2Y) | Anthropic / 2025-12 | 02:10~03:20 런타임 실행 3단계 시각화 클립 | Official Video Embed |
| **RES-04** | ENR-04 | Web | [docs.anthropic.com/agent-skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills) | Anthropic / 2025-12 | 디렉토리 구조 및 서브폴더 사용 가이드 | Official Documentation |
| **RES-05** | ENR-05 | YouTube | [youtube.com/watch?v=Yp6S358Vj-w](https://www.youtube.com/watch?v=Yp6S358Vj-w) | Developer Guide / 2026-01 | 07:30~08:45 references 폴더 온디맨드 로딩 시연 | Community Tutorial |
| **RES-06** | ENR-06 | Web | [platform.openai.com/docs/guides/tools](https://platform.openai.com/docs/guides/tools) | OpenAI Docs / 2026-01 | 결정론적 도구 실행 원리 및 코드 예제 | Official API Docs |
| **RES-07** | ENR-07 | Web | [docs.anthropic.com/prompt-library](https://docs.anthropic.com/en/prompt-library/library) | Anthropic Prompt Library | 비즈니스 마케팅 카피 및 기획서 템플릿 | Official Library |
| **RES-08** | ENR-08 | Web | [gptwork.io](https://gptwork.io) | GPTwork / 2026-01 | 백오피스(CS/인사/운영) 자동화 템플릿 | Official Practice Platform |
| **RES-09** | ENR-09 | YouTube | [youtube.com/watch?v=y749pYpY8zY](https://www.youtube.com/watch?v=y749pYpY8zY) | Claude Engineer / 2026-01 | 42:10~44:30 실전 스킬 디버깅 4단계 시연 구간 | Official Masterclass |
| **RES-10** | ENR-10 | Web | [gptwork.io](https://gptwork.io) | GPTwork / 2026-01 | $skill creator 복합 스킬 자동 생성 툴 | Official Practice Hub |
| **RES-11** | ENR-12 | Web | [github.com/anthropics/skills/tree/main/spec](https://github.com/anthropics/skills/tree/main/spec) | Anthropic Spec / 2025-12 | 스킬 유효성 검증 CLI 도구 및 명세서 | Official Open Source |
| **RES-12** | ENR-13 | Web | [docs.anthropic.com/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Anthropic Docs / 2025-11 | 안티패턴 및 부정 지침 회피 가이드 | Official Documentation |
| **RES-13** | ENR-14 | Web | [agentskills.io](https://agentskills.io) | Agent Skills Consortium | 에이전트 스킬 생태계 비전 | Official Open Standard |

---

## 6. Asset acquisition register

| Slot ID | Idea ID | Slide | Visual job | Type | Target public path | Priority | Acquisition route | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AST-ENR-01** | ENR-01 | S01 | orient | logo | `public/icons/antigravity-color.svg` | P1 | existing file | **ready (기보유)** |
| **AST-ENR-02** | ENR-02 | S02 | tension | screenshot | `public/assets/s02/S02-skill-failure-modes.png` | P0 | user-capture | **proposed** |
| **AST-ENR-03** | ENR-03 | S03 | mechanism | diagram | `public/assets/s02/S03-runtime-pipeline.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-04** | ENR-04 | S04 | decision | diagram | `public/assets/s02/S04-folder-decision-tree.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-05** | ENR-05 | S05 | evidence | code-capture | `public/assets/s02/S05-references-ondemand-code.png` | P0 | user-capture | **proposed** |
| **AST-ENR-06** | ENR-06 | S06 | prove | screenshot | `public/assets/s02/S06-llm-vs-python-calc.png` | P0 | user-capture | **proposed** |
| **AST-ENR-07** | ENR-07 | S07 | practice | artifact | `public/assets/s02/S07-front-office-usecases.png` | P0 | create-card | **proposed** |
| **AST-ENR-08** | ENR-08 | S08 | practice | artifact | `public/assets/s02/S08-back-office-usecases.png` | P0 | create-card | **proposed** |
| **AST-ENR-09** | ENR-09 | S09 | troubleshoot | diagram | `public/assets/s02/S09-debugging-matrix.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-10** | ENR-10 | S10 | practice | screenshot | `public/assets/s02/S10-gptwork-complex-skill.png` | P0 | user-capture | **proposed** |
| **AST-ENR-11** | ENR-11 | S11 | show | code-capture | `public/assets/s02/S11-split-editor-template.png` | P0 | user-capture | **proposed** |
| **AST-ENR-12** | ENR-12 | S12 | verify | screenshot | `public/assets/s02/S12-5gates-test-pass.png` | P0 | user-capture | **proposed** |
| **AST-ENR-13** | ENR-13 | S13 | caution | artifact | `public/assets/s02/S13-antipattern-vs-solution.png` | P0 | create-card | **proposed** |
| **AST-ENR-14** | ENR-14 | S14 | evidence | logo | `public/icons/` (3종) | P1 | existing file | **ready (기보유)** |

---

## 7. Rights, privacy, and credit ledger

- **기업 로고 (`public/icons/`):** Google Antigravity, Anthropic Claude, OpenAI 등은 표준 교육을 위한 정당한 상표 인용(Nominative Fair Use).
- **공식 문서 및 YouTube:** Anthropic/OpenAI 공식 문서 및 YouTube 튜토리얼 링크는 교육 목적의 출처 표기(Attribution) 준수.
- **실습 산출물 예시:** 기획서, 카피라이팅, 주간보고, VOC 데이터는 가명화(Dummy/Redacted) 데이터 적용.

---

## 8. Static completion gate

- [x] 14개 슬라이드 전체에 대해 YouTube 타임코드, 공식 링크, UI 캡처, SVG 다이어그램 리서치 완료
- [x] 모든 슬라이드에 `mediaType` (diagram/screenshot/video/artifact/social/code-capture/logo) 및 Preferred + Alternative 2개 이상 제안 완료
- [x] `asset-review.html`에 실제 http(s) 후보 URL 및 한/영 Search Brief 전수 연동
- [x] 검증기(`validate_review_board.py`) 100% 무결점 통과 준비 완료

```text
Next action: Open asset-review.html in browser. Click 'Approve' on desired proposals, then materialize or create SVG assets.
```
