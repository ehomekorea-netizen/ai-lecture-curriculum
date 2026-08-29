# 🤖 AI 에이전트 마스터코스: SKILL 기초와 핵심 아키텍처부터 실전 응용까지 (`26_0829_agent-skills`)

> **"반복되는 프롬프트 복붙에서 벗어나, 조직의 재사용 가능한 업무 표준 절차서(SOP)와 도구 연동 자산화까지"**  
> Anthropic Open Standard 기반의 Agent Skills 표준 규격, 100토큰 점진적 로딩(Progressive Disclosure) 아키텍처, GPTwork $skill creator 및 Google Antigravity 실습, 그리고 기획·마케팅·영업·CS·인사·운영 전 직무별 모범 사례와 4대 디버깅 기법을 다루는 2시간 완결형 Slidev 인터랙티브 프레젠테이션입니다.

---

## 📑 교육 커리큘럼 구성 (2개 세션 + 28슬라이드 마스터덱)

| 세션 | 주제 | 대상 및 목표 | 슬라이드덱 경로 |
| :---: | :--- | :--- | :---: |
| **Session 01** (50분) | **AI 에이전트 업무 매뉴얼: SKILL 기초와 핵심 아키텍처** | 프롬프트 한계 극복, SOP 개념, 점진적 로딩(100토큰), SKILL.md 구조 해부, polishing-emails 실습 | [`./session-01-deck`](./session-01-deck) |
| **Session 02** (50분) | **실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례** | 3단계 런타임, `references/` 지식 분리, `scripts/` 파이썬 연산 도구, 직무별(기획/마케팅/CS/인사/운영) 산출물 자동화, 4대 디버깅 | [`./session-02-deck`](./session-02-deck) |
| **Master Deck** (통합) | **AI 에이전트 마스터코스 28 슬라이드 통합 프레젠테이션** | 1차시 + 2차시 전체를 쉬는 시간 없이 2시간 연속 진행하는 올인원 마스터 슬라이드덱 | [`./master-deck`](./master-deck) |

---

## 🌟 핵심 교육 내용 상세

### 1️⃣ Session 01 : SKILL 기초와 핵심 아키텍처
1. **문제 제기 (Tension):** 일회성 프롬프트 복붙의 3대 한계 (휘발성, 2,000토큰 낭비, 팀 공유 불가)
2. **개념 정의 (Concept):** AI를 위한 업무 표준 절차서(SOP)로서의 SKILL 패키지 패러다임 전환
3. **핵심 메커니즘 (Mechanism):** 세션 초기화 시 이름/설명만 100토큰으로 상시 대기하고 필요할 때만 온디맨드 로딩하는 점진적 로딩(Progressive Disclosure) 원리
4. **글로벌 오픈 표준 (Ecosystem):** Anthropic, OpenAI, Google, Microsoft, Notion, Figma 등 글로벌 생태계 호환성
5. **구조 해부 (Show):** `SKILL.md` (YAML Frontmatter + SOP 지침)와 `scripts/`, `references/` 디렉토리 계층
6. **설계 원칙 (Guide & Decision):** 동사 형태 명명(-ing), 목적+시점 공식, High vs Low Freedom 자율성 스펙트럼 제어
7. **실습 P01 (Practice & Verify):** GPTwork `$skill creator` 활용 `polishing-emails` 템플릿 작성 및 5대 자가점검 게이트
8. **디버깅 & 피날레:** 트리거 디버깅 3단계 및 Anthropic 공식 아키텍처 다이어그램 장착

---

### 2️⃣ Session 02 : 실전 SKILL 응용과 직무별 모범 사례
1. **오작동 진단 (Tension):** 트리거 실패, 포맷 이탈, 지식 왜곡 3대 증상과 원인
2. **3단계 런타임 (Mechanism):** 0.1초 트리거 감지 ➔ 온디맨드 지식 로드 ➔ Few-shot 규칙 완수
3. **폴더 선택 결정 트리 (Decision):** 단순 지침(단일 SKILL.md) vs 사내 규정(`references/`) vs 계산 도구(`scripts/`)
4. **`references/` 패턴의 위력 (Evidence):** 20페이지 CS 규정집을 본문에서 분리하여 100토큰으로 압축 유지
5. **`scripts/` 패턴의 위력 (Prove):** LLM 영업일 계산 실수 vs 5줄 파이썬 도구의 100% 정밀 연산 대조
6. **직무별 실전 사례 (Practice):**
   * **프론트오피스:** 기획서 초안(4시간 ➔ 10분), 채널별 마케팅 카피, 미팅 팔로업 메일 자동화
   * **백오피스:** CS VOC 자동 분류, 인사 온보딩 FAQ(문의응대 80% 절감), 주간보고 취합 자동화
7. **디버깅 4대 점검법 (Troubleshoot):** Description 키워드 ➔ 단계 번호화 ➔ Few-shot ➔ 예외 처리
8. **실습 P02 & 피날레 (Practice & Closing):** 사내 지식 연동 복합 스킬 제작, 5대 자가진단, 3대 안티패턴 극복 및 엔터프라이즈 로드맵

---

## 🛠️ 프로젝트 디렉토리 구조

```bash
26_0829_agent-skills/
├── master-deck/              # 🌟 1차시 + 2차시 28슬라이드 통합 마스터덱
│   ├── slides.md             # 28개 슬라이드 전체 마크다운 소스
│   ├── asset-review.html     # 시각적 멀티미디어 승인 대시보드 (Schema v3)
│   ├── asset-enrichment-plan.md
│   ├── style.css             # 다크 글래스모피즘 CSS 베이스라인
│   ├── global-bottom.vue     # 앰비언트 오로라 백그라운드 엔진
│   ├── components/           # 공용 컴포넌트
│   └── public/               # 837개 SVG 아이콘 및 아키텍처 다이어그램
│
├── session-01-deck/          # 1차시 단독 실행 Slidev 덱 (14 슬라이드)
├── session-02-deck/          # 2차시 단독 실행 Slidev 덱 (14 슬라이드)
├── sessions/                 # 세션별 deck-brief 기획서
├── course-brief.md           # 전체 코스 브리프
├── deep-research-report.md   # 심층 리서치 보고서
└── asset-acquisition-plan.md # 에셋 수급 계획서
```

---

## 💻 로컬 개발 및 실행 방법

### 1. 통합 마스터 덱 실행 (28 슬라이드)
```bash
cd 26_0829_agent-skills/master-deck
pnpm install
pnpm dev
# 브라우저 접속: http://localhost:3030
```

### 2. 1차시 덱 단독 실행 (14 슬라이드)
```bash
cd 26_0829_agent-skills/session-01-deck
pnpm install
pnpm dev
```

### 3. 2차시 덱 단독 실행 (14 슬라이드)
```bash
cd 26_0829_agent-skills/session-02-deck
pnpm install
pnpm dev
```

### 4. 정적 SPA 빌드 (배포용)
```bash
pnpm run build
```

---

### 🌐 Tech Stack
* **Framework:** Slidev, Vue 3, Vite
* **Styling:** UnoCSS, Shiki Syntax Highlighter, 다크 글래스모피즘
* **Standard & Reference:** Anthropic Agent Skills Open Standard (`agentskills.io`), Model Context Protocol (`modelcontextprotocol.io`)
