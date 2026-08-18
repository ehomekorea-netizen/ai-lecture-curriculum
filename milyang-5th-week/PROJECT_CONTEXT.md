# 🧠 밀양시 5주차 AI 교육 프로젝트 컨텍스트 (PROJECT_CONTEXT.md)

> **이 문서는 다른 PC나 새로운 AI 환경에서 작업을 이어갈 때, 이전 대화 및 설계 맥락을 100% 온전히 복원하기 위한 핵심 핸드오프 문서입니다.**  
> 새로운 PC에서 작업 시: AI에게 **`"PROJECT_CONTEXT.md 읽고 맥락 파악한 뒤 시작하자"`**라고 지시하면 됩니다.

---

## 1. 📌 프로젝트 기본 개요

* **교육 과정명**: 밀양시 취업역량 강화교육 5주차
* **강의 주제**: 나만의 웹 포트폴리오 빌딩 & 생성형 AI 에이전트 바이브 코딩 실무
* **총 교육 시간**: 6시간 (Day 1 수요일 3시간 + Day 2 목요일 3시간)
* **교육 대상**: 밀양시 청년·구직자 (비전공자 및 취업준비생)
* **프레젠테이션 프레임워크**: [Slidev](https://sli.dev/) (Vue 3 + Vite 기반 인터랙티브 웹 슬라이드)
* **호스팅 플랫폼**: Vercel Monorepo (`https://ai-lecture-curriculum.vercel.app/milyang-5th-week/`)
* **핵심 기술 스택**: Vue 3, TailwindCSS / UnoCSS, Rough.js (손그림 효과), Lucide Icons, Lucide Vue

---

## 2. 🗺️ 전체 44개 슬라이드 커리큘럼 아키텍처

```
[Slide 01~03] 🚀 인트로: 5주차 타이틀 ➔ 6시간 여정 로드맵 ➔ 4주차 자산과의 연결고리
----------------------------------------------------------------------------------
[Slide 04~09] 🔵 DAY 1 · 1교시: Notion 공식 템플릿 & 웹 포트폴리오 빌딩
  - Slide 05: 채용담당자 관점 노션 선호 3대 핵심 타당성 (NotionValueCards 자동 순차 팝업)
  - Slide 06: 공식 템플릿 갤러리 탐색 & 우수 레퍼런스 3단 구조 해체 (DevFrame 맥북)
  - Slide 07: 템플릿 복제부터 웹 게시까지 4단계 실습 파이프라인 (NotionFlowSketch 손그림)
  - Slide 08: 화려한 템플릿보다 중요한 경험 DB 이식 3대 원칙 & 벤치마킹 기준
  - Slide 09: [실습 1] 나만의 노션 웹 포트폴리오 빌딩 & 웹에 게시 (LiveDemoTrigger)

[Slide 10~13] 🔵 DAY 1 · 2교시: 3초 만에 각인시키는 마이크로 랜딩 (Littly)
  - Slide 11: 모바일 포트폴리오 3-30-3 탐색 퍼널 (3초 첫인상 / 30초 탐색 / 3분 검증)
  - Slide 12: 면접관의 눈길을 사로잡는 3대 핵심 블록 (LittlyInteractivePhone 모바일 폰 뷰어)
  - Slide 13: [실습 2] 4주차 자산 기반 리틀리 올인원 모바일 프로필 빌딩 (LiveDemoTrigger)

[Slide 14~23] 🔵 DAY 1 · 3교시: Gemini Canvas 바이브 코딩 & Netlify 1분 배포
  - Slide 15: 취업 포트폴리오를 위한 웹의 5대 필수 기본 영역 (Hero-About-Project-Skill-Contact)
  - Slide 16~20: Gemini Canvas 실전 대화 프롬프트 5단계 (초안 ➔ 톤앤매너 ➔ 성과 ➔ 인터랙션 ➔ 디버깅)
  - Slide 21: Gemini Canvas ➔ Netlify 1분 배포 파이프라인 (DeployFlowSketch)
  - Slide 22: Netlify 무료 호스팅 및 고유 도메인 라이브 배포 원리
  - Slide 23: [실습 3] 웹 포트폴리오 전 세계 라이브 배포 실습 (LiveDemoTrigger)
----------------------------------------------------------------------------------
[Slide 24~32] 🟣 DAY 2 · 1교시: AI 에이전트 패러다임 전환 (개념 & 원리)
  - Slide 24: Day 2 · Session 1 커버 (SectionCard)
  - Slide 25: "AI 시대 더 좁아진 취업문? 달라진 역할에 집중하라" [SBS 8뉴스] (NewsVideoEmbed)
  - Slide 26: 1. AI 패러다임 변화: 대화에서 '행동'으로 (AIEvolutionCards 3단계 진화)
  - Slide 27: 2. 개념 비교: LLM vs AI Agent (AgentVsLLMCard)
  - Slide 28: 3. 왜 AI Agent인가? (LLM 3대 한계 극복)
  - Slide 29: [실습] AI 에이전트 360° 핸들 조작 자율주행 시뮬레이터 (AutonomousDriveSim)
  - Slide 30: 4. AI Agent 작동 아키텍처 & ReAct 메커니즘 (AgentLoopFlow 자율 순환 루프)
  - Slide 31: 5. 직무별 실무 적용 시나리오 Before & After (AgentJobScenarios 3D 플립카드)
  - Slide 32: 6. 취업준비생의 3대 미래 에이전트 역량 (AgentCareerStrategy)

[Slide 33~37] 🟣 DAY 2 · 2교시: Meta AI 에이전트를 활용한 웹 포트폴리오 제작 (입문 실습)
  - Slide 33: Day 2 · Session 2 커버 (SectionCard)
  - Slide 34: Meta AI(Llama 3) 에이전트의 특성과 웹 포트폴리오 생성 원리 (무료/실시간 렌더링)
  - Slide 35: 자연어 프롬프트로 웹 와이어프레임 & 3단 레이아웃 설계하기 (Hero-Projects-Skills)
  - Slide 36: 4주차 나의 이력 DB ➔ Meta AI 프롬프트 주입 공식 & 튜닝 팁
  - Slide 37: [실습 4] Meta AI 에이전트 기반 웹 포트폴리오 제작 실습 (LiveDemoTrigger)

[Slide 38~44] 🟣 DAY 2 · 3교시: 바이브 코딩(Vibe Coding)의 정석 with Manus.ai (완제품 심화 빌딩)
  - Slide 38: Day 2 · Session 3 커버 (SectionCard)
  - Slide 39: "가장 핫한 새로운 개발 언어는 영어다" 안드레 카파시 선언 (InstagramEmbed)
  - Slide 40: "웹페이지 제작에 몇 시간을 쓸 필요가 없습니다" (ManusShowcaseVideo 인트로 영상)
  - Slide 41: Manus 에이전트 기반 실전 웹 포트폴리오 5단계 제작 로드맵 (ManusWorkflowGuide)
  - Slide 42: 로컬 에셋 집결: 내 폴더에 모든 경험 자산 모아두기 (ManusAssetFolderViz 손그림)
  - Slide 43: Manus Plan 모드 & 만능 포트폴리오 생성 프롬프트 (SimpleAgentPromptQuote 애플 타이핑)
  - Slide 44: [실습 5] Manus.ai 자율 코딩 포트폴리오 완제품 빌딩 실습 (LiveDemoTrigger)
```

---

## 3. 🧩 핵심 인터랙티브 컴포넌트 동작 명세

1. **`NotionValueCards.vue` (Slide 05)**:
   - 슬라이드 진입 시 채용담당자 관점의 3대 타당성 카드가 `0.7초` 간격으로 부드럽게 순차 자동 등장(`Staggered Pop-in`).
   - 상단 불필요한 뱃지나 진행 바 없이 3개 카드에 시선 집중.
2. **`AgentLoopFlow.vue` (Slide 29)**:
   - 상단 4단 탭 버튼 및 카드 헤더의 눈/뇌/손 이모지 제거 (클린한 텍스트 기반).
   - 하단 `인간 신체 비유 (눈/오감 ➔ 뇌/기획 ➔ 손/발 ➔ 눈/학습)` 영역은 온전 보존.
3. **`ManusShowcaseVideo.vue` (Slide 39)**:
   - `public/video/Manus_web_intro.mp4` 비디오 단독 재생.
   - 가짜 브라우저 주소창, 3-Step 바, 재생 오버레이 박스 등 불필요 장식 100% 제거.
   - 슬라이드 진입 시 정지 상태 + 음소거 OFF(소리 켜짐 대기)로 설정되어 클릭 시 바로 사운드 출력.
4. **`ManusAssetFolderViz.vue` (Slide 41)**:
   - 좌측: 내 컴퓨터 폴더 에셋 (노션 DB, PDF 이력서, 수료증 사진)
   - 우측: Manus Desktop 에이전트의 Plan 모드 자율 파싱
   - Rough.js 손그림 스타일의 점선 화살표 연결.
5. **`SimpleAgentPromptQuote.vue` (Slide 42)**:
   - 상단 Kicker 및 안내글 삭제.
   - 클릭 전에는 깜빡이는 커서(`|`)만 표시 ➔ 클릭 시 커서가 완전히 사라지고 애플 키노트 스타일 실시간 타이핑 애니메이션 실행.
6. **`AgentJobScenarios.vue` (Slide 30)**:
   - 기획/마케팅/개발/데이터 직무별 AI 적용 전(Before)과 자율 에이전트 적용 후(After)를 클릭 시 3D 뒤집기로 비교.
7. **`AutonomousDriveSim.vue` (Slide 28)**:
   - 360° 마우스 드래그 핸들 조작으로 AI 에이전트의 상황 인식 ➔ 판단 ➔ 조작 루프를 게임처럼 체험.

---

## 4. 🎨 사용자 디자인 철학 및 금기 규칙 (Design Guardrails)

* ❌ **과도한 이모지 남발 금지**: 제목이나 탭 옆의 불필요한 이모지는 제거하고, 정갈하고 미니멀한 타이포그래피 유지.
* ❌ **불필요한 장식용 바/오버레이 금지**: 영상 위의 반투명 플레이 버튼 오버레이나 카드 위의 무의미한 상단 라벨 바는 즉시 삭제.
* ❌ **더미 텍스트 배제**: 실제 글로벌/국내 채용 시장의 리서치 데이터와 4주차 경험 DB 이식 실무 논거를 구체적으로 제시.
* ✅ **16:9 슬라이드 비율 최적화**: 폰트 체급과 패딩을 정밀 조율하여 여백 없이 꽉 차고 가독성 높은 애플 스타일 레이아웃 구현.

---

## 5. 🛠️ 로컬 개발 & 배포 명령어 가이드

```bash
# 1. 로컬 개발 서버 실행
cd milyang-5th-week
npm install
npm run dev
# 브라우저: http://localhost:3050

# 2. Vercel 배포용 정적 SPA 빌드
node node_modules/@slidev/cli/bin/slidev.mjs build --base /milyang-5th-week/ --out dist

# 3. 저장소 배포 링크
# https://ai-lecture-curriculum.vercel.app/milyang-5th-week/
```
