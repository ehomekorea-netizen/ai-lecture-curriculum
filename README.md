# 📚 AI 교육 및 실습 커리큘럼 모음 (AI Lecture Curriculum)

각 교육 기관 및 청중 대상별 맞춤형 **생성형 AI 실무 교육 교안 및 인터랙티브 웹 프레젠테이션**을 통합 관리하는 모노레포(Monorepo) 저장소입니다.

---

## 🔗 AI 교육과정 현황 및 교안 바로가기

| 일시 | 기관 | 장소 | 대상 | 교육 주제 | 웹 교안 링크 |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **8/28(목)** | 목포종합사회복지관 | [목포종합사회복지관](https://map.naver.com/p/search/%EB%AA%A9%ED%8F%AC%EC%20%EC%A2%85%ED%95%A9%EC%82%AC%ED%92%8D%EC%A7%80%EA%B4%80) | 🏛️ 사회복지 실무자 (복지관 종사자) | **AI를 활용한 문서 작성 협업 역량 강화 (1차시)** | [교안 바로가기](https://ai-lecture-curriculum.vercel.app/mokpo-welfare/) |
| **8/12(수) ~ 8/27(목)**<br>(총 6회 / 매주 수·목) | AJ인포텍 | [밀양소통협력센터](https://map.naver.com/p/search/%EB%B0%80%EC%96%91%EC%86%8C%ED%86%B5%ED%98%91%EB%A0%89%EC%84%BC%ED%84%B0) | 👦👧 밀양시 청년·구직자 | **웹 포트폴리오 빌딩 & AI 에이전트 바이브 코딩 (5주차)** | [5주차 바로가기](https://ai-lecture-curriculum.vercel.app/milyang-5th-week/) |
| **7/28(화)** | 퍼블릭AI | [전남해양수산과학원 고흥](https://map.naver.com/p/search/%EC%A0%84%EB%82%A8%ED%95%B4%EC%96%91%EC%88%98%EC%82%B0%EA%B3%BC%ED%95%99%EC%9B%90%20%EA%B3%A0%ED%9D%A5) | ⚓ 수산업 종사자 (어업인) | 수산업 종사자를 위한 생성형 AI | [교안 바로가기](https://ai-lecture-curriculum.vercel.app/jeonnam-maritime/) |
| **7/21(화), 23(목)** | 이음미래교육원 | [한울직업전문학교](https://map.naver.com/p/search/%ED%95%9C%EC%9A%B8%EC%A7%81%EC%97%85%EC%A0%84%EB%AC%B8%ED%95%99%EA%B5%90) | 👔 KIA 일반직 임직원 | 엑셀 활용 AI 업무 효율 향상 | [교안 바로가기](https://ai-lecture-curriculum.vercel.app/kiamotors-excel/) |
| **7/15(수) ~ 16(목)** | 전남대 앵커사업단 / 링크21 | [남부대학교](https://map.naver.com/p/search/%EB%82%A8%EB%B6%80%EB%8C%80%ED%95%99%EA%B5%90) | 🏫 지역아동센터 기관장·센터장 | AI 사업계획서 기획 및 실습 | [교안 바로가기](https://ai-lecture-curriculum.vercel.app/nambu-univ/) |

---

## 🏛️ 목포종합사회복지관: AI를 활용한 문서 작성 협업 역량 강화 (`mokpo-welfare`)

> **"사회복지 실무자를 위한 ChatGPT Work & AI 협업 실무 (1차시)"**  
> 단순한 프롬프트 작성을 넘어, 생성형 AI의 본질 이해부터 실무 표준 지시 프레임워크, 플러그인 협업 및 5대 검토 체계, 그리고 재사용 가능한 나만의 '스킬(Skill)' 자산화까지 실무 중심의 4단계 로드맵으로 구성된 Slidev 인터랙티브 프레젠테이션입니다.

### 📑 핵심 교육 커리큘럼 로드맵 (4대 파트)
1. **Part 01 · 생성형 AI와 에이전트의 본질 (Principles & Agent)**
   - AI 우산 속 생성형 AI의 위치 및 3대 핵심 작동 원리 (`AiConcentricRings`, `GptFlipCards`)
   - 검색엔진과 생성 모델의 근본적 차이 & RAG(검색 증강 생성) 오픈북 시험 모델
   - 할루시네이션 극복 4단계 실무 안전장치 & 지능형 에이전트(Agent) 순환 루프로의 진화
2. **Part 02 · 실무 프롬프트 엔지니어링 표준 (Prompt Engineering)**
   - 공문서 품질을 결정짓는 5대 핵심 지시 요소 (역할, 맥락, 목표, 제약, 출력형식)
   - 복지 실무 공문서 톤앤매너 및 제약조건 구조화 템플릿
3. **Part 03 · ChatGPT Work 도구 및 5대 검토 체계 (Work Tools & Review)**
   - 명시적 플러그인 호출 표준 (@Documents, @Presentations)
   - 실무 Use Case 1: 신규 복지 정책·지침 분석 및 사업기획서 작성 (`WelfarePolicyUseCase`)
   - 실무 Use Case 2: 만족도 설문 결과 분석 및 요약 보고서 작성 (`DataAnalysisUseCase`)
   - 공문서 제출 전 5대 검토 체크리스트 및 최종 책임 승인 체계 (`DocumentFiveChecks`)
4. **Part 04 · 나만의 스킬 구축과 업무 자산화 (Skill & Assetization)**
   - 스킬의 정의 수식: `반복되는 업무 + 정해진 처리 방식 + 원하는 결과 기준 = 나만의 Skill` (`SkillMeaningDefinition`)
   - 나만의 스킬 4단계 구축 워크플로우 & `SKILL.md` 중심의 표준 패키지 구조 (`SkillCreationProcess`, `SkillDirectoryStructure`)
   - 실무 Use Case: 프로그램 결과보고 자동화 스킬 실전 & 나만의 스킬 초안 완성 (`ProgramReportSkillUseCase`, `CreateMyOwnSkill`)
   - Final Statement: *"AI는 초안을 쓰고, 가치는 담당자가 담습니다."*

---

## 🚀 밀양시 5주차: 웹 포트폴리오 & AI 에이전트 바이브 코딩 (`milyang-5th-week`)

> **"나만의 웹 포트폴리오 빌딩 & 생성형 AI 에이전트 바이브 코딩 실무 (총 6시간)"**  
> Slidev 기반의 고반응형 인터랙티브 웹 슬라이드로 제작되었으며, 이론 ➔ 시연 ➔ 실습 3박자로 진행됩니다.

### 📅 DAY 1 : 나만의 웹 포트폴리오 빌딩 & 배포 (3시간)
1. **1교시 · Notion 공식 템플릿 & 웹 포트폴리오 빌딩**
   - 채용담당자가 노션 웹 포트폴리오를 선호하는 3대 핵심 타당성 (`NotionValueCards`)
   - 공식 템플릿 갤러리 탐색 및 웹 구조 해체
   - 템플릿 복제부터 웹 게시까지 4단계 실습 파이프라인 (`NotionFlowSketch`)
   - 화려한 템플릿보다 중요한 경험 DB 이식의 3대 원칙
   - 💻 **[실습]** 노션 공식 템플릿 기반 실시간 웹 포트폴리오 런칭
2. **2교시 · 3초 만에 각인시키는 마이크로 랜딩 (Littly)**
   - 3-30-3 시선 포획 법칙 (3초 첫인상 / 30초 탐색 / 3분 검증)
   - 모바일 인터랙티브 폰 뷰어 (`LittlyInteractivePhone`)
   - 📱 **[실습]** 4주차 자산 기반 리틀리 올인원 모바일 프로필 빌딩
3. **3교시 · Gemini Canvas 바이브 코딩 & Netlify 1분 무료 배포**
   - 포트폴리오 표준 5대 영역 및 Gemini 2.0 Canvas 실시간 코딩 원리
   - 단계별 프롬프트 (초안 생성 ➔ 디자인 톤앤매너 ➔ 성과 강조 ➔ 편의 기능 ➔ 대화형 디버깅)
   - Netlify 드래그 앤 드롭 1분 무료 배포 파이프라인 (`DeployFlowSketch`)
   - 🌐 **[실습]** 나만의 웹사이트 전 세계 실시간 무료 런칭

---

### 📅 DAY 2 : AI 에이전트와 바이브 코딩 실무 (3시간)
1. **1교시 · AI 에이전트 패러다임 전환 (개념 & 원리)**
   - 생성형 AI 3단계 진화 (LLM ➔ 워크플로우 ➔ 자율 에이전트 `AIEvolutionCards`)
   - LLM vs Agent 개념 비교 및 LLM 3대 한계 극복
   - 직무별 Before & After 3D 인터랙티브 플립카드 (`AgentJobScenarios`)
   - 4단계 자율 순환 루프 (`AgentLoopFlow`: Sense ➔ Plan ➔ Act ➔ Feedback)
   - 🚗 **[실습]** 360° 자율주행 시뮬레이터 조작을 통한 에이전트 루프 체감
2. **2교시 · Meta AI 에이전트를 활용한 웹 포트폴리오 제작 (입문 실습)**
   - Llama 3 오픈 에이전트의 무료 접근성과 대화형 코드 렌더링 특성
   - 자연어 대화로 3단 와이어프레임(Hero, Projects, Skills) 레이아웃 설계
   - 4주차 나의 이력 DB ➔ Meta AI 프롬프트 주입 공식 & 실시간 튜닝
   - 🤖 **[실습]** Meta AI 에이전트로 5분 만에 인터랙티브 웹 포트폴리오 초안 완성
3. **3교시 · 바이브 코딩(Vibe Coding)의 정석 with Manus.ai (완제품 심화 빌딩)**
   - "가장 핫한 새로운 개발 언어는 영어다" 안드레 카파시 바이브 코딩 선언
   - 마누스 웹 템플릿 인트로 비디오 쇼케이스 (`ManusShowcaseVideo`)
   - 4주차 노션 DB ➔ GPT PDF ➔ Manus Desktop 5단계 제작 로드맵 (`ManusWorkflowGuide`)
   - 로컬 에셋 집결 손그림 다이어그램 (`ManusAssetFolderViz`)
   - 애플 키노트 스타일 단 한 줄의 마스터 프롬프트 타이핑 (`SimpleAgentPromptQuote`)
   - 🚀 **[실습]** Manus.ai Plan 모드 자율 코딩을 통한 완제품 포트폴리오 빌딩 & 배포

---

## 🛠️ 디렉토리 구조 (Repository Layout)

```bash
ai-lecture-curriculum/
├── mokpo-welfare/            # 🏛️ [NEW] 목포종합사회복지관 1차시 Slidev 기반 인터랙티브 웹 교안 (Live)
│   ├── index.html            # Vercel 배포용 SPA 엔트리
│   ├── slides.md             # 37개 슬라이드 전체 마크다운 소스 (TOC 포함)
│   ├── components/           # Vue 3 인터랙티브 에디토리얼 컴포넌트 모음
│   ├── layouts/              # statement.vue 등 전용 레이아웃
│   ├── assets/               # 정적 번들 에셋
│   └── package.json          # Slidev 환경 설정
│
├── milyang-5th-week/         # 🌟 밀양 5주차 Slidev 기반 인터랙티브 웹 교안 (Live)
├── milyang-notion-resume/    # 🗄️ [Legacy] 이전 제작된 노션 이력서 DB 교안 아카이브 (별도 보존)
├── nambu-univ/               # 남부대학교 지역아동센터 AI 사업계획서 교안
├── kiamotors-excel/          # 기아자동차 임직원 엑셀 AI 업무 효율화 교안
├── jeonnam-maritime/         # 전남해양수산과학원 수산업 생성형 AI 교안
└── README.md                 # 본 통합 안내 문서
```

---

## 💻 로컬 개발 및 실행 방법 (mokpo-welfare)

```bash
# 1. 목포 1차시 디렉토리로 이동
cd mokpo-welfare

# 2. 의존성 패키지 설치
pnpm install

# 3. 로컬 Slidev 개발 서버 실행
pnpm dev
# 브라우저 접속: http://localhost:3030

# 4. 정적 SPA 빌드 (Vercel 배포용)
pnpm run build --base /mokpo-welfare/ --out ./dist
```

---

### 🌐 Tech Stack
- **Framework**: Slidev, Vue 3, Vite
- **Styling**: TailwindCSS, Geist Mono, Source Serif 4, Radio Canada Big
- **Graphics & Icons**: Lucide Icons, Rough.js, Rough SVG
- **Deployment**: Vercel
