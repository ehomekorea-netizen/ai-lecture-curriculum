---
kind: slidev-deck-brief
schema_version: 1
status: ready-for-build
scope: session
workflow_stage: plan-first
asset_state: planned
course_id: "agent-skill-mastery-2h"
session_id: "S01"
session_title: "AI 에이전트의 업무 매뉴얼: SKILL 기초와 핵심 아키텍처"
title: "SKILL 기초 및 설계 실습"
thesis: "SKILL은 AI에게 반복 작업을 가르치는 표준 지침이며, 100토큰의 점진적 로딩으로 컨텍스트 낭비 없이 완벽한 업무 수행을 보장한다."
language: ko
audience: "AI 에이전트를 활용해 반복 업무를 자동화하려는 기획자, 개발자, 엔지니어"
duration_minutes: 50
target_slide_count: "14-16"
delivery: live
practice_in_slides: required
assessment: none-by-default
teacher_guide: separate
learner_handout: separate
next_skill: "$nekomeowww-slidev-deck"
source_count: 1
asset_count: 0
asset_slot_count: 4
---

# Session 1: AI 에이전트의 업무 매뉴얼, SKILL 기초와 핵심 아키텍처

## 1. Handoff summary

- **Session Thesis:** 매번 장문의 프롬프트를 복사-붙여넣기할 필요 없이, 표준 `SKILL.md`를 정의해 두면 점진적 로딩(Progressive Disclosure)을 통해 100토큰만으로 수백 개의 스킬을 상시 대기시키고 필요 시에만 호출하여 정확히 수행한다.
- **Audience Outcome:** 수강생은 SKILL의 정의와 동작 원리를 이해하고, 규격화된 YAML Frontmatter 및 단계별 절차를 갖춘 첫 `SKILL.md`를 직접 작성·검증할 수 있다.
- **Timing:** 총 50분 (도입 5분 → 개념 및 원리 15분 → 설계 원칙 및 작성법 15분 → [실습 P01] 15분)
- **Practice:** 슬라이드 내 포함된 15분 핸즈온 [P01] (단일 업무 자동화 `SKILL.md` 작성 및 시뮬레이션).

---

## 2. Build contract

- **Session Duration:** 50분
- **Target Slide Count:** 14장
- **Tone:** 명확하고 실용적인 엔지니어링 가이드 톤
- **Delivery Format:** 라이브 핸즈온 세션
- **Visual Style:** nekomeowww 퓨어 블랙 무대, 고대비 타이포그래피, 단계별 클릭(`v-click`) 연출
- **Boundary:** 별도 채점 기준이나 유인물 제작 없이 슬라이드 내 실습 가이드로 완결.

---

## 3. Thesis and outcomes

## Thesis
SKILL은 AI에게 반복 업무를 가르치는 표준 지침이며, 100토큰의 점진적 로딩으로 컨텍스트 낭비 없이 완벽한 업무 수행을 보장한다.

## Audience outcomes
1. **[O-01]** AI 에이전트 환경에서 단순 프롬프트와 SKILL 패키지의 차이점을 SOP(표준업무절차서) 관점에서 설명할 수 있다.
2. **[O-02]** 점진적 로딩(Progressive Disclosure) 메커니즘을 설명하고, 왜 수백 개 스킬을 등록해도 토큰이 절약되는지 도식화할 수 있다.
3. **[O-03]** 올바른 명명 규칙(`name`)과 트리거 설명(`description`), 자유도에 따른 단계별 절차를 갖춘 유효한 `SKILL.md`를 작성할 수 있다.

---

## 4. Narrative spine

1. **Cold Open (S01~S02):** "매번 프롬프트를 복붙하고 계십니까?" 반복 업무의 피로와 AI의 한계.
2. **Tension & Concept (S03):** 해결책으로서의 SKILL: AI를 위한 표준 업무 매뉴얼(SOP).
3. **Mental Model (S04~S05):** 점진적 로딩(Progressive Disclosure)의 마법 — 100토큰의 상시 대기와 온디맨드 로드.
4. **Structure & Rules (S06~S08):** `SKILL.md`의 해부학 — YAML Frontmatter, 명명법, 자유도(Freedom Level) 제어.
5. **Practice (S09~S12):** [실습 P01] 15분 동안 나만의 첫 `SKILL.md` 작성 및 트리거 시뮬레이션.
6. **Wrap-up & Bridge (S13~S14):** 세션 1 요약 및 세션 2(플러그인, MCP 연동)로의 연결.

---

## 5. Slide map

| ID | Role | Title / claim | Audience takeaway | Sees | Sources | Assets / slots | Practice | Click stages | Layout / staging | Component hint | Slide intent / cue | Evidence / citation | Risk / status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **S01** | cover | AI 에이전트 업무 매뉴얼: SKILL 기초와 핵심 아키텍처 | 세션 주제와 핵심 가치 확인 | 타이틀, 서브타이틀, 강사/세션 메타정보 | SRC-01 | — | — | 0 | center | markdown | 오프닝 임팩트 | SRC-01: 교안 | ready |
| **S02** | tension | 왜 매번 프롬프트를 다시 작성해야 하는가? | 단순 프롬프트의 재사용성·일관성 한계 체감 | 3가지 프롬프트 페인포인트 카드 (일관성 부족, 토큰 낭비, 공유 불가) | SRC-01 | — | — | 3 (문제 순차 노출) | default | markdown | 문제 공감대 형성 | SRC-01: 1장 | ready |
| **S03** | concept | SKILL: AI 에이전트를 위한 표준 업무 절차서(SOP) | SKILL이 단순 텍스트가 아닌 구조화된 지침 패키지임을 이해 | 전통적 프롬프트 vs SKILL 패키지 비교 다이어그램 | SRC-01 | AST-TBD-01 | — | 2 (전통 vs SKILL 대비) | split | svg-flow | 개념 정의 | SRC-01: 1, 7장 | ready |
| **S04** | mechanism | 핵심 원리: 점진적 로딩 (Progressive Disclosure) | 100토큰만으로 수백 개 스킬을 상시 탑재하는 원리 파악 | 2단계 로딩 다이어그램 (세션 시작 시 메타데이터 → 필요 시 전체 로드) | SRC-01 | AST-TBD-02 | — | 2 (1단계 프리로드 → 2단계 온디맨드) | default | svg-flow | 기술 메커니즘 설명 | SRC-01: 1장 | ready |
| **S05** | evidence | 글로벌 오픈 표준과 생태계 확장 | Claude뿐 아니라 OpenAI Codex, Gemini 등 범용 표준임을 확인 | 표준 타임라인 (2025.10 도입 → 12 오픈표준) 및 주요 파트너 생태계 | SRC-01 | — | — | 2 (타임라인 → 지원 플랫폼) | default | markdown | 신뢰성 및 확장성 강조 | SRC-01: 1장 | ready |
| **S06** | structure | `SKILL.md`의 구조: YAML 헤더와 마크다운 본문 | 스킬 파일의 필수 구성 요소와 디렉토리 계층 이해 | `SKILL.md` 코드 뷰 + 보조 폴더(`scripts/`, `references/`) 구조 | SRC-01 | AST-TBD-03 | — | 2 (YAML 헤더 강조 → 본문 및 폴더 강조) | split | vue | 구체적 스펙 제시 | SRC-01: 1, 2장 | ready |
| **S07** | rules | 좋은 스킬의 설계 원칙: 명명(Name)과 설명(Description) | 트리거율을 결정짓는 `name`과 `description` 작성 규칙 습득 | 동사 현재분사 명명법 및 3인칭 목적/시점 기술 가이드 | SRC-01 | — | — | 3 (규칙 1: Name → 규칙 2: Description → 좋은 예/나쁜 예) | default | markdown | 핵심 작성 스킬 전수 | SRC-01: 2장 | ready |
| **S08** | deepdive | 작업 자유도(Freedom Level)에 따른 지침 작성법 | High/Low Freedom에 따른 지침 구체성 조절 노하우 습득 | 2열 비교 카드: 창의적 작업(높은 자유도) vs 엄격한 절차(낮은 자유도) | SRC-01 | — | — | 2 (High vs Low Freedom) | split | markdown | 실무 최적화 팁 | SRC-01: 2장 | ready |
| **S09** | practice-intro | [실습 P01] 나만의 첫 `SKILL.md` 작성하기 (15분) | 실습 목표와 3단계 워크플로우 숙지 | 3열 실습 안내 카드: ① 업무 선정 → ② YAML 작성 → ③ 절차 기술 | SRC-01 | AST-TBD-04 | P01 | 0 | default | vue | 실습 돌입 | SRC-01: 8장 | ready |
| **S10** | practice-spec | 실습 템플릿 및 예제 시나리오 | 구체적 템플릿 코드를 보고 작성 시작 | "정중한 비즈니스 영문 이메일 변환기" 템플릿 코드 블록 | SRC-01 | — | P01 | 1 (템플릿 강조) | default | markdown | 작성 가이드라인 | SRC-01: 8장 | ready |
| **S11** | practice-timer | [실습 진행] 15분 타이머 및 작성 체크리스트 | 타이머를 보며 실습 수행 및 체크리스트 점검 | 타이머 위젯 + 5대 자가 점검 체크리스트 | SRC-01 | — | P01 | 0 | default | vue | 집중 실습 진행 | SRC-01: 2, 7장 | ready |
| **S12** | review | 실습 결과 검증 및 트리거 최적화 | 작성한 스킬이 제대로 트리거되는지 검증하는 법 습득 | 프롬프트 테스트 3개 시나리오 및 디버깅 요령 | SRC-01 | — | P01 | 2 (테스트 시나리오 → 디버깅 팁) | default | markdown | 피드백 및 검증 | SRC-01: 2장 | ready |
| **S13** | summary | Session 1 핵심 요약 | 1세션의 핵심 배움 3가지 리마인드 | 3개 키 테이크어웨이 카드 (SOP 지침, 100토큰 로딩, 명확한 트리거) | SRC-01 | — | — | 3 (카드 순차 등장) | default | markdown | 학습 정리 | SRC-01: 1~2장 | ready |
| **S14** | bridge | Next: 외부 시스템과 연결되는 지능형 스킬 | 2세션의 확장 주제(MCP/플러그인/보안)에 대한 기대감 고조 | 세션 2 예고: SKILL + API/커넥터 = 완전 자동화 | SRC-01 | — | — | 1 (세션 2 핵심 키워드 공개) | center | markdown | 자연스러운 전환 | SRC-01: 4~5장 | ready |

---

## 6. Source register

| ID | Type | Original path / URL | Title / Author | Relevant pages / sections | What it supports | Extraction method | Confidence | Rights / privacy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SRC-01** | Local Markdown | `C:\Users\IN\Desktop\두견\스킬강의\deep-research-report.md` | SKILL(스킬) 심층 분석 보고서 | 1장(개념/역사), 2장(설계원칙), 7장(체크리스트), 8장(교안) | 정의, Progressive Disclosure 원리, YAML 사양, 자유도, 실습 1 | 로컬 파일 정밀 분석 | confirmed | 사내 리서치 보고서 |

---

## 7. Asset acquisition plan

| Priority | Slot ID | Slide/Session | Visual Job | Required Asset | Composition / Minimum Spec | Acquisition Route | Rights | Fallback | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **P0** | `AST-TBD-01` | S03 | 단순 프롬프트 vs SKILL 패키지 개념 대비 | SVG 다이어그램 | 16:9 다크 테마, 좌: 휘발성 텍스트 / 우: 재사용 가능한 SOP 폴더 | 인라인 SVG / Mermaid | 없음 | 텍스트 비교 카드 | planned |
| **P0** | `AST-TBD-02` | S04 | 점진적 로딩 2단계 구조 시각화 | SVG 아키텍처 다이어그램 | 1단계: 100토큰 메타 로드 → 2단계: 온디맨드 전체 로드 | 인라인 SVG 그래픽 | 없음 | Mermaid graph LR | planned |
| **P1** | `AST-TBD-03` | S06 | `SKILL.md` 및 폴더 구조 | 코드/디렉토리 하이라이트 | YAML frontmatter + 마크다운 본문 + `scripts/` 폴더 | Slidev 코드 블록 컴포넌트 | 없음 | 마크다운 코드 블록 | planned |
| **P1** | `AST-TBD-04` | S09 | [실습 P01] 3단계 워크플로우 가이드 | 3열 글래스 카드 UI | 요구분석 → YAML 정의 → 지침 기술 3단계 카드 | Tailwind CSS Grid UI | 없음 | 불릿 텍스트 | planned |

---

## 8. Asset register

*(현재 Plan-first 단계이므로 실물 에셋 대신 상기 4개 `AST-TBD-*` 슬롯으로 지정됨)*

---

## 9. Evidence and claim ledger

| ID | Claim / Assertion | Classification | Source IDs | Exact locator | Confidence | Citation text / Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **C-01** | 스킬은 세션 시작 시 이름과 설명(약 100토큰)만 로드하고 필요 시 전체를 로드하는 점진적 로딩을 사용한다. | confirmed | SRC-01 | 1장, l.10 | high | "점진적 로딩(progressive disclosure)... 대략 스킬당 100토큰" |
| **C-02** | Anthropic은 2025년 10월 스킬 도입 후 12월에 오픈 에이전트 스킬 표준으로 발표했다. | confirmed | SRC-01 | 1장, l.12 | high | "2025년 10월 스킬 형식 도입, 12월 Agent Skills 표준 발표" |
| **C-03** | 스킬 이름은 64자 이하 소문자/하이픈의 동사 현재분사(gerund) 형태가 권장된다. | confirmed | SRC-01 | 2장, l.20 | high | "구체적이고 동사 형태의 현재분사(gerund)... 64자 이하" |
| **C-04** | 작업의 자유도(High/Low Freedom)에 따라 절차의 구체성을 다르게 작성해야 한다. | confirmed | SRC-01 | 2장, l.22 | high | "높은 자유도는 일반적 지침, 낮은 자유도는 구체적 명령어까지 제공" |

---

## 10. Practice-in-slide plan

| Practice ID | Slide IDs | Asset slots | Concept applied | Learner action | Materials / inputs | Minutes | Expected visible output/state | In-slide steps and cues | Tool failure fallback | Risk / status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **P01** | S09~S12 | AST-TBD-04 | YAML Frontmatter 및 단계별 SOP 작성 | 1) 업무 선정(예: 이메일 정중화, 회의록 요약 등)<br>2) `name` 및 `description` 작성<br>3) 입력/출력 예시 및 처리 절차 기술 | 슬라이드 제공 템플릿 및 텍스트 에디터 | 15 min | 유효한 YAML 헤더를 포함한 `SKILL.md` 텍스트 완성본 | S09에서 안내 → S10 템플릿 복사 → S11 타이머 구동 및 작성 → S12 검증 체크 | 슬라이드 내 완성본 예시 즉시 표시 | ready |

---

## 11. Design and interaction brief

- **Stage:** 퓨어 블랙(`#0B0F19`) 베이스에 부드러운 시안 글래스 글로우 레이어.
- **Typography:** 헤드라인 순백색(`text-white font-bold`), 본문 연회색(`text-slate-300`).
- **Cards:** 반투명 글래스(`bg-white/5 border border-white/10 rounded-xl backdrop-blur-md`).
- **Click Behavior:** `v-click`을 사용하여 각 개념과 비교 카드가 강사의 발화 타이밍에 맞춰 순차적으로 등장하도록 설계.

---

## 12. Component plan

| Component ID | Slide IDs | Purpose | Inputs / Data | Click model | Renderer | Dependencies | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CMP-01** | S04 | 점진적 로딩 다이어그램 | 단계별 로딩 상태 (Preload vs On-Demand) | 0~2 | Inline SVG / Vue | none | Mermaid graph |
| **CMP-02** | S06 | `SKILL.md` 인터랙티브 코드 뷰 | YAML + Markdown 텍스트 | 0~1 | Slidev Code Highlight | none | Markdown Block |
| **CMP-03** | S11 | 15분 실습 타이머 & 체크리스트 | 15:00 카운트다운 타이머 | 0 | Vue Component | none | 정적 시간 안내 |

---

## 13. Slide delivery cues and timing

| Slide ID | Target time | Slide intent | Click cue | Transition to next |
| --- | --- | --- | --- | --- |
| **S01** | 0:00–1:00 | 강의 오프닝 & 인사 | 0 | 문제 제기로 전환 |
| **S02** | 1:00–3:30 | 프롬프트 반복 작성의 문제점 환기 | click 1, 2, 3 (문제 3개 순차 노출) | 해결책 소개로 전환 |
| **S03** | 3:30–7:00 | SKILL 개념 및 SOP 비유 전달 | click 1 (전통 프롬프트), click 2 (SKILL 패키지) | 핵심 기술 메커니즘으로 이동 |
| **S04** | 7:00–11:00 | 점진적 로딩 원리(100토큰) 강조 | click 1 (프리로드), click 2 (온디맨드 로드) | 오픈 표준 현황으로 이동 |
| **S05** | 11:00–14:00 | 오픈 표준과 생태계 확장성 | click 1 (타임라인), click 2 (플랫폼) | 작성법 섹션으로 전환 |
| **S06** | 14:00–18:00 | `SKILL.md` 내부 구조 설명 | click 1 (YAML), click 2 (Body/Files) | 명명 규칙으로 이동 |
| **S07** | 18:00–21:30 | Name 및 Description 작성 원칙 | click 1 (Name), click 2 (Desc), click 3 (Good/Bad) | 자유도 제어로 이동 |
| **S08** | 21:30–25:00 | 자유도(Freedom Level) 제어 팁 | click 1 (High), click 2 (Low) | 실습 안내로 진입 |
| **S09** | 25:00–27:00 | [실습 P01] 목표 및 흐름 안내 | 0 | 템플릿 공개로 이동 |
| **S10** | 27:00–30:00 | 실습 템플릿 및 예제 시연 | click 1 (코드 블록 강조) | 실습 타이머 가동 |
| **S11** | 30:00–43:00 | 실습 진행 (15분 집중 코딩) | 0 (타이머 실시간 작동) | 결과 검증으로 이동 |
| **S12** | 43:00–46:30 | 작성 결과 검증 및 디버깅 팁 | click 1 (테스트 시나리오), click 2 (팁) | 마무리 요약으로 이동 |
| **S13** | 46:30–48:30 | 세션 1 핵심 요약 | click 1, 2, 3 (요약 카드) | 세션 2 예고로 이동 |
| **S14** | 48:30–50:00 | 세션 2(MCP·플러그인) 브릿지 | click 1 (확장 키워드 노출) | 1세션 종료 및 휴식 |

---

## 14. Questions, assumptions, and risks

- **[P1 Assumption] 에디터 사용:** 수강생이 메모장, VS Code 등 기본 텍스트 편집 도구를 다룰 수 있다고 가정.
- **[P2 Polish] 타이머 컴포넌트:** Vue 기반 인터랙티브 카운트다운 타이머를 슬라이드 내 임베드하여 몰입감 향상.

---

## 15. Handoff

- **Status:** `ready-for-build`
- **Next action:** Use `$nekomeowww-slidev-deck` with `sessions/S01-deck-brief.md`.
- **Implement first:** S01–S04, then S06–S08(작성법), S09–S12(실습 블록).
- **Practice:** P01 실습 템플릿과 자가 진단 체크리스트를 S10~S11에 명확히 렌더링.
- **Verify:** 클릭 단계(v-click) 전환, 코드 블록 하이라이트 문법, 15분 타이머 작동.
