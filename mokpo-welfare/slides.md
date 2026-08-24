---
theme: default
title: AI를 활용한 문서 작성 협업 역량 강화
info: 목포종합사회복지관 AI 역량 강화 교육 - 1차시
colorSchema: light
transition: slide-left
mdc: true
fonts:
  sans: Radio Canada Big, system-ui, sans-serif
  serif: Source Serif 4, Georgia, serif
  mono: Geist Mono, monospace
---

<CoverSlide />

---

# 목차

<p class="subtitle">AI의 본질에서 실무 프롬프트, 플러그인 협업, 그리고 <strong>스킬 자산화까지</strong></p>

<script setup>
const tocItems = [
  { num: '01', title: '생성형 AI와 에이전트의 본질', en: 'Principles & Agent' },
  { num: '02', title: '실무 프롬프트 엔지니어링 표준', en: 'Prompt Engineering' },
  { num: '03', title: 'ChatGPT Work 도구 및 5대 검토 체계', en: 'Work Tools & Review' },
  { num: '04', title: '나만의 스킬 구축과 업무 자산화', en: 'Skill & Assetization' },
]
</script>

<div class="slide-body">
  <div style="display:flex;flex-direction:column;width:100%;max-width:760px;margin:0 auto;">
    <div v-for="item in tocItems" :key="item.num" style="display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1.5px solid #e2e8f0;">
      <div style="display:flex;align-items:center;gap:24px;">
        <span style="font-family:'Geist Mono',monospace;font-size:2rem;font-weight:700;color:#2563eb;min-width:52px;line-height:1;">{{ item.num }}</span>
        <span style="font-family:'Source Serif 4',Georgia,serif;font-size:1.45rem;font-weight:700;color:#0f172a;line-height:1.2;">{{ item.title }}</span>
      </div>
      <span style="font-family:'Geist Mono',monospace;font-size:0.68rem;font-weight:600;color:#94a3b8;letter-spacing:0.1em;text-transform:uppercase;white-space:nowrap;padding-left:16px;">{{ item.en }}</span>
    </div>
  </div>
</div>

---
layout: default
---

<SectionPartDivider
  title="생성형 AI의 본질에서 AI에이전트까지"
  subtitle="단순 프롬프트 작성을 넘어, AI의 작동 원리와 할루시네이션(RAG), 그리고 스스로 일하는 에이전트 시대로의 도약"
  image="/premium_photo-1764699342973-5d518dede42b.avif"
/>

---
clicks: 3
---

# AI를 이해하는 가장 간단한 그림

<p class="subtitle">인공지능(AI)이라는 거대한 우산 안에서 생성형 AI의 정확한 위치를 파악합니다.</p>

<div class="slide-body">
  <AiConcentricRings :stage="$clicks" />
  <div class="slide-footer quote-box text-xs text-center font-medium">
    <strong>핵심 흐름</strong>: 인공지능 (스스로 판단) ➔ 머신러닝 (데이터 학습) ➔ 딥러닝 (뇌 신경망 모방) ➔ <strong>생성형 AI (새로운 콘텐츠 생성)</strong>
  </div>
</div>

---
clicks: 10
---

# 생성형 AI의 본질: 무엇을 만들어내는가?

<p class="subtitle">학습한 데이터의 패턴을 바탕으로 <strong>새로운 합성 콘텐츠(Synthetic Content)</strong>를 생성합니다.</p>

<div class="slide-body">
  <GenerativeAiArchSketch :stage="$clicks" />
</div>



---

# 우리가 쓰는 ChatGPT의 'GPT'는 무슨 뜻인가?

<p class="subtitle">알파벳 세 글자 속에 모델의 3대 핵심 작동 원리가 모두 담겨 있습니다.</p>

<div class="slide-body">
  <GptFlipCards />
  <div class="slide-footer quote-box text-xs">
    <strong>한 줄 결론</strong>: GPT는 <strong>"사전 학습된 문맥 신경망(Transformer)을 통해 질문에 맞춰 다음 단어를 확률적으로 조립하는 생성(Generative) 모델"</strong>입니다.
  </div>
</div>

---
clicks: 2
---

# GPT는 '검색엔진'이 아닙니다

<p class="subtitle">검색과 생성의 차이를 이해하지 못하면 AI를 실무에 잘못 활용하게 됩니다.</p>

<div class="slide-body">
  <SearchVsLlmComparison :stage="$clicks" />
  <div class="slide-footer quote-box text-xs">
    <strong>2026년 실무 표준</strong>: 검색(사실 확보)과 생성(문서 작성)을 결합한 <strong>RAG(검색 증강 생성)</strong>로 진화했습니다!
  </div>
</div>

---
clicks: 4
---

# 검색(Search) vs 생성(Generation) 비교

<p class="subtitle">두 기술의 장단점을 명확히 알고 결합해서 쓰는 것이 실무자의 핵심 경쟁력입니다.</p>

<div class="slide-body">
  <ComparisonTableSlide7 :stage="$clicks" />
</div>


---
clicks: 3
---

# AI 할루시네이션 (Hallucination)

<p class="subtitle">학습 데이터에 없는 내용도 <strong>너무나 그럴듯하고 자신 있게 지어내는 현상</strong>입니다.</p>

<div class="slide-body">
  <HallucinationSimulator :stage="$clicks" />
</div>



---
clicks: 5
---

# 할루시네이션을 극복하는 4단계 안전장치

<p class="subtitle">AI가 거짓말을 하지 못하도록 만드는 실무 검증 프레임워크입니다.</p>

<div class="slide-body">
  <HallucinationSafeguardsSketch :stage="$clicks" />
</div>


---
clicks: 6
---

# RAG란 무엇인가? (검색 증강 생성)

<p class="subtitle">Retrieval-Augmented Generation — <strong>기억으로만 치는 시험 vs 교재를 펼쳐놓고 푸는 오픈북 시험</strong></p>

<div class="slide-body">
  <RagOpenBookSimulator :stage="$clicks" />
</div>


---
clicks: 6
---

# 그래서 프롬프트(Prompt)가 중요합니다

<p class="subtitle">좋은 프롬프트는 "말을 예쁘게 길게 쓰는 것"이 아니라 <strong>구조화된 지시서</strong>를 작성하는 것입니다.</p>

<div class="slide-body">
  <PromptStructureArchSketch :stage="$clicks" />
</div>


---
clicks: 5
---

# AI의 발전 4세대: 어디까지 진화했는가?

<p class="subtitle">단순 텍스트 생성을 넘어, 스스로 생각하고 도구를 다루는 <strong>에이전트(Agent) 시대</strong>로 진입했습니다.</p>

<div class="slide-body">
  <AiEvolutionTimelineWave :stage="$clicks" />
</div>


---

# 글로벌 시장을 뒤흔든 AI 에이전트의 실체

<p class="subtitle">단순 대화를 넘어 실제 완성된 결과물을 도출하는 <strong>자율 업무 혁명 (Anthropic Claude Cowork 보도)</strong></p>

<div class="slide-body flex flex-col items-center justify-center">
  <div class="w-[620px] aspect-video rounded-2xl overflow-hidden shadow-2xl border-2 border-slate-800 bg-black">
    <iframe
      src="https://www.youtube.com/embed/brtbMmCkghM?rel=0"
      class="w-full h-full"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen
    ></iframe>
  </div>
  <div class="w-[620px] flex justify-end mt-2">
    <span class="text-xs font-bold text-slate-700 font-mono bg-slate-100/90 px-2.5 py-0.5 rounded-md border border-slate-300 shadow-2xs">
      📺 MBC 뉴스데스크 (2026. 02. 06 보도)
    </span>
  </div>
</div>

---
clicks: 2
---

# AI 에이전트는 실제로 어떻게 일하는가?

<p class="subtitle">단 1번의 지시로 <strong>[탐색 ➔ 연산 ➔ 규정검증 ➔ 문서생성]</strong>을 완수하는 자율 실행 시뮬레이터</p>

<div class="slide-body">
  <AiAgentWorkflowDirector :stage="$clicks" />
</div>

---
layout: default
---

<SectionPartDivider
  title="Gemini Notebook으로 시작하는 자료 기반 AI 문서 작성"
  subtitle="자료가 없는 상태에서 AI와 함께 Deep Research부터 사업계획서 초안 및 AI 검토까지 완성하는 실전 워크플로우"
  image="/image-3_6e6716.webp"
/>

---
clicks: 4
---

# Gemini Notebook이란 무엇인가?

<p class="subtitle">내가 제공한 자료를 중심으로 읽고, 찾고, 비교하고, 정리해 주는 <strong>AI 연구·사고 도구</strong></p>

<div class="slide-body">
  <NotebookLmUseCasesShowcase :stage="$clicks" />
</div>

---
clicks: 5
---

# 일반 생성형 AI vs Gemini Notebook 비교

<p class="subtitle break-keep"><span class="whitespace-nowrap">"무엇이든 묻는 AI"</span>와 <strong><span class="whitespace-nowrap">"내 자료를 기준으로 묻는 AI"</span></strong>의 결정적 차이</p>

<div class="slide-body">
  <ComparisonTableSlide17 :stage="$clicks" />
</div>

---

# Gemini Notebook의 3분할 기본 구조:<br>Sources / Chat / Studio

<p class="subtitle">화면을 세 영역으로 기억하면 끝납니다 — <strong>자료 관리, 심층 질문, 결과물 제작</strong></p>

<div class="slide-body">
  <NotebookLmTriSplitArchitecture />
</div>

---
clicks: 5
---

# 실전 실습: 자료가 없는 상태에서 사업 문서 만들기

<p class="subtitle">종합사회복지관 신규 사업 기획 — <strong>자료조사 ➔ 선별 ➔ 분석 ➔ 지식환류 ➔ 초안 ➔ 검토</strong></p>

<div class="slide-body">
  <GeminiNotebookPracticeWorkflow :stage="$clicks" />
</div>

---
layout: default
---

<SectionPartDivider
  title="ChatGPT Work 환경과 다중 파일 기반 실무 문서 작성"
  subtitle="단순 대화를 넘어, 로컬 폴더 연결과 플러그인·스킬로 완성하는 고품질 결과보고서(DOCX)"
  video="/chatgpt-work-select-1080p-v1.mp4"
/>

---
clicks: 4
---

# ChatGPT Work란?

<p class="subtitle">단순 대화를 넘어 <strong>실제 업무(기획서·슬라이드·분석표)를 위임</strong>하고 완성형 파일을 받는 업무 실행 환경</p>

<div class="slide-body">
  <ChatGPTWorkIntro :stage="$clicks" />
</div>

---
clicks: 15
---

# Chat vs Work vs Codex 3대 실행 환경 비교

<p class="subtitle">단순 대화(Chat), <strong>로컬 파일 기반 산출물 제작(Work)</strong>, 개발 환경(Codex)의 명확한 역할과 최소 권한 원칙</p>

<div class="slide-body">
  <ChatWorkCodexComparison :stage="$clicks" />
</div>

---

# 무엇을 먼저 시도해볼까요?

<p class="subtitle">ChatGPT Work로 즉시 시작할 수 있는 <strong>3대 실무 스타터 유스케이스</strong>와 실전 프롬프트</p>

<div class="slide-body">
  <WhatToTryFirst />
</div>

---

# 연결이 만드는 차이: 플러그인

<p class="subtitle">단순 대화를 넘어 <strong>외부 도구와 실시간 데이터를 연결해 완결형 업무를 수행하는 공식 시연</strong></p>

<div class="slide-body">
  <VideoPluginsDemo />
</div>

---

# 주방 요리로 보는 완벽한 1:1 대비: 스킬 vs 플러그인

<p class="subtitle">개인의 <strong>비법 레시피(스킬)</strong>에서 팀 전체가 함께 쓰는 <strong>밀키트 패키지(플러그인)</strong>로의 확장</p>

<div class="slide-body">
  <SkillPluginCulinaryMetaphor />
</div>

---

# 실무에서 둘의 차이점 한눈에 비교

<p class="subtitle">세부 지침서인 <strong>스킬(Skill)</strong>과 도구·데이터 번들인 <strong>플러그인(Plugin)</strong>의 5대 핵심 차이</p>

<div class="slide-body">
  <SkillPluginComparisonTable />
</div>

---
clicks: 1
---

# 플러그인 호출의 실무 표준: 자연어 vs @명시적 호출

<p class="subtitle">의도 왜곡과 오차를 없애고 <strong>100% 완성형 파일</strong>을 얻는 <strong>@도구이름 명시적 호출 원칙</strong></p>

<div class="slide-body">
  <PluginExplicitCallingStandard :stage="$clicks" />
</div>

---

# 실무 Use Case: 신규 복지 정책·지침 분석 및 사업기획서 작성

<p class="subtitle">방대한 정책 지침서(PDF)를 <strong>@Documents & @Presentations</strong>로 분석하여 <strong>기획서와 보고자료</strong> 동시 완성</p>

<div class="slide-body">
  <WelfarePolicyUseCase />
</div>

---

# 실무 Use Case 2: 설문 결과 분석 및 요약 보고서 작성

<p class="subtitle">기본 데이터 분석 기능으로 통계·차트를 도출하고, <strong>@Documents</strong>로 1쪽 요약 보고서(DOCX) 완성</p>

<div class="slide-body">
  <DataAnalysisUseCase />
</div>

---

# 이제, 여러분의 방식대로 해보세요

<p class="subtitle">오늘 배운 플러그인을 자유롭게 조합해 <strong>업무의 작은 불편 하나를 해결해봅니다.</strong></p>

<div class="slide-body">
  <FreePracticeInspiration />
</div>

---
clicks: 1
---

# 보고서 제출 전, 다섯 가지만 확인합니다

<p class="subtitle">AI가 만든 문서는 초안입니다. <strong>최종 확인은 담당자가 합니다.</strong></p>

<div class="slide-body">
  <DocumentFiveChecks :stage="$clicks" />
</div>

---

# 스킬의 의미

<p class="subtitle">스킬은 한 번의 답변이 아니라, <strong>반복되는 업무의 방식</strong>입니다</p>

<div class="slide-body">
  <SkillMeaningDefinition />
</div>

---
clicks: 3
---

# 스킬을 만드는 과정

<p class="subtitle">나의 업무 방식을 스킬로 만드는 <strong>4단계 워크플로우</strong></p>

<div class="slide-body">
  <SkillCreationProcess :stage="$clicks" />
</div>

---

# 스킬 패키지 디렉토리 구조

<p class="subtitle"><strong>SKILL.md</strong> 중심으로 구성되는 ChatGPT 스킬의 표준 파일 및 폴더 체계</p>

<div class="slide-body">
  <SkillDirectoryStructure />
</div>

---

# 실무 Use Case: 반복되는 프로그램 결과보고 스킬 제작

<p class="subtitle">매달 작성하는 운영일지와 만족도 데이터를 <strong>@skill-creator</strong>로 나만의 전용 보고서 스킬로 자산화</p>

<div class="slide-body">
  <ProgramReportSkillUseCase />
</div>

---

# 나만의 스킬 만들기

<p class="subtitle">이제, 나의 반복 업무 하나를 <strong>스킬로 만들어보세요</strong></p>

<div class="slide-body">
  <CreateMyOwnSkill />
</div>

---

# "가장 핫한 새로운 개발 언어는 '영어(자연어)'다"

<p class="subtitle">OpenAI 공동창업자이자 테슬라 전 AI 디렉터 <strong>안드레 카파시(Andrej Karpathy)</strong>가 촉발한 <strong>바이브 코딩(Vibe Coding)</strong> 혁명</p>

<div class="slide-body">
  <InstagramEmbed postId="DYlyHEAFLR7" />
</div>

---

# 바이브 코딩(Vibe Coding) 실전 프로젝트 쇼케이스

<p class="subtitle">비개발자도 프롬프트와 기획 의도(PRD)만으로 완성한 <strong>3대 실전 라이브 웹 서비스</strong></p>

<div class="slide-body">
  <VibeCodingProjectsShowcase />
</div>

---

<EndingSlide />


