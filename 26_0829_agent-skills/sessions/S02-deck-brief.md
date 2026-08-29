---
kind: slidev-deck-brief
schema_version: 1
status: ready-for-build
scope: session
workflow_stage: plan-first
asset_state: resolved
course_id: "agent-skill-mastery-2h"
session_id: "S02"
session_title: "실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례"
title: "Antigravity & GPTwork 환경에서의 실전 스킬 실습과 직무별 활용"
thesis: "SKILL은 사내 지식(references/)과 보조 도구(scripts/)가 결합될 때 기획·마케팅·인사·운영 등 전 직무의 강력한 업무 비서가 되며, Antigravity와 GPTwork 환경에서의 실전 테스트와 디버깅을 거쳐 완성된다."
language: ko
audience: "1세션에서 SKILL 기초를 익히고, Antigravity와 GPTwork에서 자신의 직무(기획, 마케팅, 인사, CS, 운영 등)에 맞는 실전 스킬을 제작·실행·디버깅하려는 실무자 및 일반 수강생"
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
asset_slot_count: 2
---

# Session 2: 실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례

## 1. Handoff summary

- **Session Thesis:** SKILL은 사내 지식(`references/`)과 보조 도구(`scripts/`)가 결합될 때 기획·마케팅·인사·운영 등 전 직무의 강력한 업무 비서가 되며, Antigravity와 GPTwork 환경에서의 실전 테스트와 디버깅을 거쳐 완성된다.
- **Audience Outcome:** 수강생은 복잡한 CLI나 개발 지식 없이도 Antigravity/GPTwork에서 스킬을 직접 실행하고 테스트할 수 있으며, 언제 `references/`나 `scripts/`를 분리해야 하는지 판단하고, 직무별(마케팅, 인사, 영업, 운영 등) 모범 사례를 바탕으로 오작동을 스스로 디버깅할 수 있다.
- **Timing:** 총 50분 (Antigravity/GPTwork 런타임 & 디버깅 감각 10분 → `references/` & `scripts/` 분리 기준 12분 → 직무별 실전 모범 사례 13분 → [실습 P02] 내 직무 스킬 제작 & 테스트 15분)
- **Practice:** 슬라이드 내 포함된 15분 핸즈온 [P02] (Antigravity / GPTwork에서 직접 돌려보는 내 직무 맞춤형 `SKILL.md` + `references/` 작성 및 디버깅).

---

## 2. Build contract

- **Session Duration:** 50분
- **Target Slide Count:** 14장
- **Tone:** 친절하고 실용적이며 직무 중심적인 실전 워크숍 톤 (개발 용어 최소화, 비즈니스 언어 중심)
- **Delivery Format:** 라이브 핸즈온 세션 (Antigravity / GPTwork 화면 실습)
- **Visual Style:** nekomeowww 퓨어 블랙 무대, 네온 시안/에메랄드/스카이블루 액센트, 고대비 글래스 카드, 직무별 아이콘 및 직관적인 Do & Don't 대비 뷰
- **Boundary:** 어려운 Git 커밋이나 CLI 환경은 배제하고, GUI/웹 프롬프트 환경(Antigravity, GPTwork)에서 파일과 폴더를 통해 실습 완결.

---

## 3. Thesis and outcomes

### Thesis
SKILL은 사내 지식(`references/`)과 보조 도구(`scripts/`)가 결합될 때 기획·마케팅·인사·운영 등 전 직무의 강력한 업무 비서가 되며, Antigravity와 GPTwork 환경에서의 실전 테스트와 디버깅을 거쳐 완성된다.

### Audience outcomes
1. **[O-01]** Antigravity와 GPTwork에서 스킬이 인식되고 호출되는 과정을 이해하고, 프롬프트 입력 후 스킬이 제대로 작동하는지 확인하는 검증 방법을 설명할 수 있다.
2. **[O-02]** 언제 단일 `SKILL.md`로 끝내고, 언제 `references/`(규정·양식)나 `scripts/`(자동화 계산)를 추가해야 하는지 명확한 판단 기준을 가질 수 있다.
3. **[O-03]** 기획, 마케팅, 인사, CS, 영업 등 다양한 비즈니스 직무에서 바로 활용 가능한 모범 사례(Best Practice)를 자신의 업무에 맞게 적용할 수 있다.
4. **[O-04]** 스킬이 엉뚱한 답변을 하거나 지침을 무시할 때, 원인(지침 모호성, 예외 누락 등)을 진단하고 `SKILL.md`를 수정하여 고치는 실전 디버깅 능력을 확보한다.

---

## 4. Narrative spine

1. **Cold Open (S01~S02):** "스킬을 만들었는데 왜 내 맘대로 안 움직일까?" — 첫 실행 시 겪는 당혹감과 실전 테스트/디버깅의 필요성.
2. **Runtime & Flow (S03):** Antigravity & GPTwork에서 스킬이 돌아가는 3단계 (트리거 감지 ➔ 지침 해석 ➔ 결과물 산출).
3. **Folder Architecture (S04~S06):** 하위 폴더 선택 기준: 언제 `references/`(사내 지식)를 넣고, 언제 `scripts/`(간단 도구)를 넣는가?
4. **Job-Specific Best Practices (S07~S08):** 전 직무 실전 모범 사례 (기획/마케팅/영업 ➔ 인사/총무/CS/운영).
5. **Debugging Guide (S09):** 스킬 오작동 시 확인해야 할 4대 핵심 점검 포인트와 주의점.
6. **Practice (S10~S12):** [실습 P02] Antigravity / GPTwork에서 직접 돌려보는 내 직무 복합 스킬 제작 & 디버깅 (15분).
7. **Mistakes & Mastery (S13~S14):** 흔히 하는 3대 실수 회피법 및 나만의 스킬에서 팀 공유로 확장하는 로드맵.

---

## 5. Slide map

| ID | Role | Title / claim | Audience takeaway | Sees | Sources | Assets / slots | Practice | Click stages | Layout / staging | Component hint | Slide intent / cue | Evidence / citation | Risk / status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S01** | cover | 실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례 | 2세션 실무 목표 및 직무별 실습 방향 확인 | 타이틀, Antigravity/GPTwork 뱃지, 직무 태그 | SRC-01 | AST-ENR-01 | — | 0 | center | markdown | 2세션 실습 시작 선언 | SRC-01: 5장 | ready |
| **S02** | tension | 스킬을 만들었는데 왜 내 맘대로 안 움직일까? | 스킬 첫 실행 시 겪는 문제와 디버깅의 필요성 공감 | 3대 오작동 증상 (트리거 무시, 엉뚱한 양식 출력, 지침 임의 생략) | SRC-01 | — | — | 3 (증상 순차 노출) | default | markdown | 디버깅 필요성 부각 | SRC-01: 6장 | ready |
| **S03** | concept | Antigravity & GPTwork에서 스킬이 실행되는 3단계 | AI가 스킬을 감지하고 사용하는 런타임 흐름 체득 | 3단계 흐름: ① 사용자 질문 ➔ ② 메타데이터 매칭 ➔ ③ 본문 지침 온디맨드 수행 | SRC-01 | — | — | 3 (1~3단계 순차 강조) | default | markdown | 런타임 원리 이해 | SRC-01: 1, 5장 | ready |
| **S04** | deepdive | 하위 폴더 선택 기준: 언제 무엇을 넣어야 하는가? | 단일 파일 vs references/ vs scripts/ 구분 기준 정립 | 3갈래 결정 트리 (단일 파일: 단순 SOP / references/: 규정·양식 / scripts/: 계산·정제) | SRC-01 | — | — | 3 (결정 조건 순차 노출) | default | markdown | 폴더 분리 판단 기준 습득 | SRC-01: 2장 | ready |
| **S05** | deepdive | `references/`의 힘: 사내 규정·양식·톤앤매너 주입 | 회사의 방대한 가이드라인을 토큰 낭비 없이 주입하는 법 | `references/` 활용 사례 (사내 복지 규정, 브랜드 보이스 가이드, 보고서 템플릿) | SRC-01 | — | — | 2 (폴더 구조 ➔ 온디맨드 로딩) | split | markdown | 지식 계층 분리 요령 | SRC-01: 2, 5장 | ready |
| **S06** | deepdive | `scripts/`의 힘: AI의 계산 실수와 포맷 오류 없애기 | 언제 간단한 보조 도구를 쥐여주어야 하는지 이해 | `scripts/` 활용 사례 (날짜 계산, CSV 데이터 필터링, 정형 텍스트 치환) | SRC-01 | — | — | 2 (AI 한계 ➔ 스크립트 해결책) | split | markdown | 보조 도구 활용법 습득 | SRC-01: 2, 5장 | ready |
| **S07** | deepdive | 직무별 모범 사례 1: 기획 · 마케팅 · 영업 | 비즈니스 현업에서 즉시 쓰는 실전 스킬 레시피 확인 | 3개 직무 카드 (마케팅 카피 생성기, 바이어 맞춤 제안서 요약기, 시장 조사 리포터) | SRC-01 | — | — | 3 (직무별 카드 순차 노출) | default | markdown | 비즈니스 실전 응용 | SRC-01: 3장 | ready |
| **S08** | deepdive | 직무별 모범 사례 2: 인사 · 총무 · CS · 운영 | 백오피스 및 고객 접점 업무 자동화 패턴 확인 | 3개 직무 카드 (고객 VOC 분류 & 답변기, 신규 입사자 온보딩 FAQ, 주간 업무 보고서 정제) | SRC-01 | — | — | 3 (직무별 카드 순차 노출) | default | markdown | 백오피스 자동화 | SRC-01: 3장 | ready |
| **S09** | deepdive | 스킬 디버깅 체크리스트: 문제 발생 시 4대 점검법 | 오작동 시 스스로 고칠 수 있는 문제 해결 공식 습득 | 4대 점검법 (1. Description 키워드 / 2. 단계 번호화 / 3. Few-shot 예시 / 4. 예외 규정) | SRC-01 | — | — | 4 (체크리스트 순차 노출) | default | markdown | 디버깅 능력 확보 | SRC-01: 6, 8장 | ready |
| **S10** | practice-intro | [실습 P02] 내 직무 맞춤 복합 스킬 직접 만들기 (15분) | 2차 실습 목표(내 업무 맞춤형 지침 + references/ 작성) 파악 | 3단계 실습 미션 (① 업무 선정 ➔ ② `references/` 자료 준비 ➔ ③ `SKILL.md` 작성) | SRC-01 | — | P02 | 0 | default | markdown | 2차 실습 안내 | SRC-01: 8장 | ready |
| **S11** | practice-spec | 실습 템플릿: 직무별 추천 예제 가이드 | 복사해서 바로 쓸 수 있는 실습 템플릿 코드 확인 | "고객 문의 응대 스킬" or "주간 업무 보고서 스킬" 완성형 템플릿 | SRC-01 | — | P02 | 1 (템플릿 구조 강조) | split | markdown | 실습 템플릿 제공 | SRC-01: 8장 | ready |
| **S12** | practice-timer | [실습 진행] 15분 타이머 & Antigravity/GPTwork 검증 | 15분 동안 스킬 작성 후 Antigravity/GPTwork에서 직접 실행 | 15분 타이머 위젯 + 실전 테스트 5대 자가진단표 | SRC-01 | — | P02 | 0 | default | vue | 집중 실습 & 테스트 | SRC-01: 8장 | ready |
| **S13** | review | 스킬 작성 시 흔히 하는 3대 실수와 주의점 | 초보자가 자주 범하는 오류와 명확한 해결책 체득 | 3대 실수 대비 (너무 긴 본문, 충돌하는 지침, 부정어 남발) & 올바른 작성법 | SRC-01 | — | P02 | 3 (실수 ➔ 해결책 순차 대비) | default | markdown | 실패 패턴 예방 | SRC-01: 6장 | ready |
| **S14** | summary | 2시간 마스터 서머리: 나만의 비서에서 팀의 자산으로 | 2시간 전체 핵심 원칙 정리 및 사내 공유 로드맵 | 4대 요약 카드 (SOP 표준화, 점진적 로딩, 직무별 references 확장, 지속적 디버깅) | SRC-01 | — | — | 4 (요약 카드 순차 노출) | center | markdown | 전체 학습 완결 | SRC-01: 1~8장 | ready |

---

## 6. Source register

| ID | Type | Original path / URL | Title / Author | Relevant pages / sections | What it supports | Extraction method | Confidence | Rights / privacy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SRC-01** | Local Markdown | `C:\Users\IN\Desktop\두견\스킬강의\deep-research-report.md` | SKILL(스킬) 심층 분석 보고서 | 2장(디렉토리 구조), 3장(직무별 활용사례), 5장(런타임 아키텍처), 6장(디버깅 및 프롬프트 엔지니어링), 8장(교안) | Antigravity/GPTwork 런타임, 직무별 유즈케이스, references/scripts 기준, 4대 디버깅 점검법, 실습 2 | 로컬 파일 정밀 분석 | confirmed | 사내 리서치 보고서 |

---

## 7. Next step handoff

```text
Use $nekomeowww-slidev-deck with sessions/S02-deck-brief.md to implement the session 2 Slidev deck.
```
