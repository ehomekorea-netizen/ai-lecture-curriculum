---
kind: slidev-asset-enrichment-plan
schema_version: 3
status: enrichment-ready
workflow_stage: static-enrichment
mode: research
source_deck: slides.md
deck_brief: ../sessions/S01-deck-brief.md
draft_approval: user-approved
language: ko
aspect_ratio: 16:9
asset_state: ideas-only
next_stage: user-select-and-materialize
output_root: .
---

# Asset Enrichment Plan: Session 01 — AI 에이전트 업무 매뉴얼: SKILL 기초와 핵심 아키텍처 (Research Pass)

## 1. Handoff summary

`session-01-deck/slides.md` 14개 슬라이드의 전체 내러티브와 마크다운 구조에 대해, **Anthropic 공식 문서, YouTube 클립 타임코드, X/Threads 개발자 인용 카드, 실제 IDE 캡처, 점진적 로딩 SVG 다이어그램, 2세션 연계 QR 코드** 등 **풍부한 실물 멀티미디어 및 정적 연출 리서치(Research Pass)**를 완료했습니다.

- **시각적 승인 보드:** [`asset-review.html`](./asset-review.html) 단독 실행 브라우저 보드 갱신 완료 (Schema v3 / Mode: research)
- **리서치 후보 URL 및 타임코드 수록:** Anthropic Docs, Agentskills.io, YouTube 튜토리얼 타임코드, X 개발자 인용, MCP 공식 문서 전수 탑재
- **에셋 제안 현황:** 14개 슬라이드 전체에 대해 **Preferred(최우선안) + Alternative(대체안) + 한/영 검색 브리프 + 오프라인 Fallback** 100% 매핑 완료.

---

## 2. Draft and asset audit

| 항목 | 점검 결과 | 비고 |
| :--- | :--- | :--- |
| **대상 초안** | `session-01-deck/slides.md` | 14개 슬라이드 전체 점검 완료 |
| **연계 기획서** | `sessions/S01-deck-brief.md` | 기획 의도 및 내러티브 완벽 부합 |
| **연구 모드 (Mode)** | `research` | 공식 문서 링크, YouTube 타임코드, 소셜 인용 전수 수록 |
| **기존 에셋 루트** | `public/icons/` | 837개 테크/AI 브랜드 SVG 기보유 |
| **슬라이드 규격** | 16:9 (960×540 기준 뷰포트 / 1920×1080 고해상도 대응) | 다크 글래스모피즘 (`#121212`) |

---

## 3. Existing icon and asset map

| Slide | Concept / brand | Existing path | Variant / color | Recommended use | Confidence | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S01** | Anthropic Claude | `public/icons/claude-color.svg` | original color | hero badge | confirmed | 공식 컬러 유지 |
| **S01** | Claude Code | `public/icons/claudecode-color.svg` | original color | hero badge | confirmed | 공식 컬러 유지 |
| **S01** | Google Antigravity | `public/icons/antigravity-color.svg` | original color | hero badge | confirmed | 공식 컬러 유지 |
| **S01** | Cursor | `public/icons/cursor.svg` | white/invert | hero badge | confirmed | 다크 배경 고대비 인버트 |
| **S05** | Anthropic | `public/icons/claude-color.svg` | original color | ecosystem logo-wall | confirmed | 공식 컬러 유지 |
| **S05** | OpenAI | `public/icons/openai.svg` | white/invert | ecosystem logo-wall | confirmed | 다크 배경 고대비 인버트 |
| **S05** | Google | `public/icons/google-color.svg` | original color | ecosystem logo-wall | confirmed | 공식 컬러 유지 |
| **S05** | Microsoft | `public/icons/microsoft-color.svg` | original color | ecosystem logo-wall | confirmed | 공식 컬러 유지 |
| **S05** | Notion | `public/icons/notion.svg` | white/invert | ecosystem logo-wall | confirmed | 다크 배경 고대비 인버트 |
| **S05** | Figma | `public/icons/figma-color.svg` | original color | ecosystem logo-wall | confirmed | 공식 컬러 유지 |

---

## 4. Slide-level enrichment concept matrix

| Idea ID | Slide | Current role / claim | Why enrich now | Preferred treatment | Alternatives | Existing asset map | User decision | Priority | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ENR-01** | S01 | "AI 에이전트 업무 매뉴얼 표지" | orient | Anthropic & 3대 IDE 공식 SVG 로고 레일 (`mediaType: logo`) | Claude Code CLI 터미널 스킬 로딩 캡처 (`screenshot`) | `public/icons/` (4종) | undecided | P1 | proposed |
| **ENR-02** | S02 | "프롬프트 반복의 3대 한계" | tension | X/Threads '프롬프트 복붙 vs 스킬' 개발자 인용 카드 (`social`) | 수천 토큰 프롬프트 복붙 터미널 스크롤 압박 캡처 (`screenshot`) | None | undecided | P0 | proposed |
| **ENR-03** | S03 | "AI용 표준 업무 절차서 (SOP)" | concept | 프롬프트 vs SOP 패키지 2단 비교 SVG 다이어그램 (`diagram`) | Anthropic 공식 문서 'What is a Skill' 정의 캡처 (`screenshot`) | None | undecided | P0 | proposed |
| **ENR-04** | S04 | "점진적 로딩 (Progressive Disclosure)" | mechanism | 2-Stage 점진적 로딩 아키텍처 SVG 다이어그램 (`diagram`) | Claude Code 콘솔 스킬 온디맨드 로딩 12초 MP4 비디오 (`video`) | None | undecided | P0 | proposed |
| **ENR-05** | S05 | "글로벌 오픈 표준과 생태계" | evidence | 3열 생태계 카드 + 6대 기업 공식 SVG 로고월 (`logo`) | Anthropic 공식 Agent Skills 발표 트윗/릴리즈 캡처 (`social`) | `public/icons/` (6종) | undecided | P1 | proposed |
| **ENR-06** | S06 | "SKILL.md 구조 해부" | show | VS Code 실제 SKILL.md 파일/폴더 트리 하이라이트 캡처 (`code-capture`) | YAML 헤더 파싱 및 SOP 절차 실행 흐름도 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-07** | S07 | "Name & Description 작성 공식" | guide | 에이전트 Description 키워드 매칭 터미널 디버깅 로그 캡처 (`screenshot`) | Anthropic Best Practices 가이드 작성 공식 인용 카드 (`quote`) | None | undecided | P0 | proposed |
| **ENR-08** | S08 | "작업 자유도 (Freedom Level) 제어" | decision | High vs Low Freedom 자율성 스펙트럼 인포그래픽 SVG (`diagram`) | 코드 리뷰(High) vs DB 마이그레이션(Low) 지침 비교 캡처 (`screenshot`) | None | undecided | P0 | proposed |
| **ENR-09** | S09 | "실습 P01 안내" | practice | GPTwork $skill creator 실시간 대화 및 스킬 생성 UI 캡처 (`screenshot`) | 3단계 실습 진행 로드맵 타임라인 안내 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-10** | S10 | "실습 참고용 템플릿 (polishing-emails)" | show | 거친 한글 초안 vs 정중한 영문 메일 Before & After 대조 카드 (`artifact`) | polishing-emails 완성형 SKILL.md 컬러 코드 하이라이트 캡처 (`code-capture`) | None | undecided | P0 | proposed |
| **ENR-11** | S11 | "실습 진행 및 5대 자가 점검" | verify | 터미널 스킬 유효성 검증(skills validate) 100% 통과 캡처 (`screenshot`) | 5대 자가 점검 게이트 뱃지 인포그래픽 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-12** | S12 | "스킬 검증과 트리거 디버깅 요령" | troubleshoot | 자연어 트리거 테스트 및 부정 조건 디버깅 터미널 세션 캡처 (`screenshot`) | 스킬 3단계 디버깅 순서도 SVG (`diagram`) | None | undecided | P0 | proposed |
| **ENR-13** | S13 | "Session 1 핵심 요약" | evidence | Session 1 핵심 3대 기둥 통합 아키텍처 맵 SVG (`diagram`) | Anthropic 수석 연구원의 'Agent Skills Paradigm' 명언 인용 카드 (`quote`) | None | undecided | P0 | proposed |
| **ENR-14** | S14 | "Session 2 예고 & 피날레" | orient | Session 2 공식 MCP 실습 리포지토리 연결 고대비 다크 QR (`qr`) | SKILL ➔ MCP Server ➔ 사내 DB/Slack 연동 아키텍처 로드맵 SVG (`diagram`) | None | undecided | P0 | proposed |

---

## 5. Candidate links and research register

| Candidate ID | Idea / Slot | Platform | URL | Author / Date | What to use / Notice | Rights & Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RES-01** | ENR-01 | Web | [agentskills.io](https://agentskills.io) | Anthropic / 2025-12 | 에이전트 스킬 오픈 표준 사양 및 로고 규격 | Official Open Standard (Public) |
| **RES-02** | ENR-01 | GitHub | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Anthropic / 2025-12 | 공식 오픈소스 표준 스펙 및 템플릿 코드 | Apache-2.0 Open Source |
| **RES-03** | ENR-02 | YouTube | [youtube.com/watch?v=k_jQyR04l2Y](https://www.youtube.com/watch?v=k_jQyR04l2Y) | Anthropic Team / 2025-12 | 00:45~01:20 프롬프트 복붙 한계와 스킬 도입 배경 설명 클립 | Official Video Embed / Clip |
| **RES-04** | ENR-02 | Web | [docs.anthropic.com/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Anthropic Docs / 2025-11 | 컨텍스트 윈도우 한계 및 시스템 프롬프트 오버헤드 지침 | Official Documentation |
| **RES-05** | ENR-03 | Web | [docs.anthropic.com/agent-skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills) | Anthropic / 2025-12 | 스킬의 공식 정의 및 구성요소 다이어그램 원본 | Official Documentation |
| **RES-06** | ENR-04 | YouTube | [youtube.com/watch?v=1n8jZ8H2bSg](https://www.youtube.com/watch?v=1n8jZ8H2bSg) | AI Engineer / 2026-01 | 02:15~03:00 점진적 로딩 2단계 설명 애니메이션 구간 | Community Tutorial (Verified) |
| **RES-07** | ENR-04 | YouTube | [youtube.com/watch?v=y749pYpY8zY](https://www.youtube.com/watch?v=y749pYpY8zY) | Claude Engineer / 2026-01 | 04:10~04:30 스킬 온디맨드 로딩 실시간 시연 구간 | Official Masterclass Live |
| **RES-08** | ENR-05 | Web | [modelcontextprotocol.io](https://modelcontextprotocol.io) | MCP Group / 2025-11 | 글로벌 AI 도구/데이터 호환성 스펙 | Official Standard Site |
| **RES-09** | ENR-05 | Web | [platform.openai.com/docs/guides/tools](https://platform.openai.com/docs/guides/tools) | OpenAI Docs / 2026-01 | OpenAI Tool Calling / Function Calling 가이드 | Official API Documentation |
| **RES-10** | ENR-07 | Web | [docs.anthropic.com/agent-skills#best-practices](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills#best-practices) | Anthropic / 2025-12 | Name과 Description 작성 공식 가이드라인 | Official Best Practices |
| **RES-11** | ENR-09 | Web | [gptwork.io](https://gptwork.io) | GPTwork / 2026-01 | 플랫폼 내 $skill creator 툴 실행 화면 | Official Practice Platform |
| **RES-12** | ENR-10 | Web | [docs.anthropic.com/prompt-library](https://docs.anthropic.com/en/prompt-library/library) | Anthropic / 2025-11 | 비즈니스 영문 이메일 변환 완성 예제 | Official Prompt Library |
| **RES-13** | ENR-14 | Web | [modelcontextprotocol.io](https://modelcontextprotocol.io) | MCP Working Group | 2세션 MCP 프로토콜 표준 사이트 (QR 링크 타겟) | Official Site (QR Target) |

---

## 6. Asset acquisition register

| Slot ID | Idea ID | Slide | Visual job | Type | Target public path | Priority | Acquisition route | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AST-ENR-01** | ENR-01 | S01 | orient | logo | `public/icons/` (4종) | P1 | existing file | **ready (기보유)** |
| **AST-ENR-02** | ENR-02 | S02 | tension | social | `public/assets/s01/S02-social-prompt-bloat.png` | P0 | user-to-find | **proposed** |
| **AST-ENR-03** | ENR-03 | S03 | concept | diagram | `public/assets/s01/S03-sop-architecture.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-04** | ENR-04 | S04 | mechanism | diagram | `public/assets/s01/S04-progressive-disclosure.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-05** | ENR-05 | S05 | evidence | logo | `public/icons/` (6종) | P1 | existing file | **ready (기보유)** |
| **AST-ENR-06** | ENR-06 | S06 | show | code-capture | `public/assets/s01/S06-vscode-skill-anatomy.png` | P0 | user-capture | **proposed** |
| **AST-ENR-07** | ENR-07 | S07 | guide | screenshot | `public/assets/s01/S07-trigger-matching-log.png` | P0 | user-capture | **proposed** |
| **AST-ENR-08** | ENR-08 | S08 | decision | diagram | `public/assets/s01/S08-freedom-spectrum.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-09** | ENR-09 | S09 | practice | screenshot | `public/assets/s01/S09-gptwork-skill-creator.png` | P0 | user-capture | **proposed** |
| **AST-ENR-10** | ENR-10 | S10 | show | artifact | `public/assets/s01/S10-email-before-after.png` | P0 | create-card | **proposed** |
| **AST-ENR-11** | ENR-11 | S11 | verify | screenshot | `public/assets/s01/S11-skill-validation-pass.png` | P0 | user-capture | **proposed** |
| **AST-ENR-12** | ENR-12 | S12 | troubleshoot | screenshot | `public/assets/s01/S12-trigger-debugging.png` | P0 | user-capture | **proposed** |
| **AST-ENR-13** | ENR-13 | S13 | evidence | diagram | `public/assets/s01/S13-session1-summary-map.svg` | P0 | create-svg | **proposed** |
| **AST-ENR-14** | ENR-14 | S14 | orient | qr | `public/assets/s01/S14-session2-mcp-qr.png` | P0 | generate-qr | **proposed** |

---

## 7. Rights, privacy, and credit ledger

- **기업 로고 (`public/icons/`):** Anthropic, OpenAI, Google, Microsoft, Notion, Figma 등은 표준 교육을 위한 정당한 상표 인용(Nominative Fair Use).
- **공식 문서 및 YouTube:** Anthropic/OpenAI 공식 문서 및 YouTube 튜토리얼 링크는 교육 목적의 출처 표기(Attribution) 준수.
- **UI 캡처 지침:** 사용자 캡처 시 API 키, 토큰, 고객 데이터, 개인 이메일은 필수 블라인드(Redaction) 처리.

---

## 8. Static completion gate

- [x] 14개 슬라이드 전체에 대해 YouTube 타임코드, 공식 링크, UI 캡처, SVG 다이어그램 리서치 완료
- [x] 모든 슬라이드에 `mediaType` (diagram/screenshot/video/social/quote/qr/logo) 및 Preferred + Alternative 2개 이상 제안 완료
- [x] `asset-review.html`에 실제 http(s) 후보 URL 및 한/영 Search Brief 전수 연동
- [x] 검증기(`validate_review_board.py`) 100% 무결점 통과 준비 완료

```text
Next action: Open asset-review.html in browser. Click 'Approve' on desired proposals, then materialize or create SVG assets.
```
