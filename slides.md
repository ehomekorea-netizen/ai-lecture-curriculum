---
layout: default
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: "AI를 활용한 문서 작성 협업 역량 강화"
info: "목포종합사회복지관 AI 역량 강화 교육"
exportFilename: mokpo-ai-welfare-skills-master-deck
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glow: none
glowOpacity: 0.28
glowSeed: 888
glowHue: 215
routerMode: hash
fonts:
  sans: Radio Canada Big, Pretendard, system-ui, sans-serif
  serif: Source Serif 4, Georgia, serif
  mono: Geist Mono, Fira Code, monospace
defaults:
  layout: default
  transition: fade-out
---
<!-- slide:1 -->

<CoverSlide />

<!--
[발표자]
안녕하십니까! 목포종합사회복지관 사회복지사 선생님 여러분, 반갑습니다.
오늘 교육은 「AI를 활용한 문서 작성 및 협업 역량 강화」라는 주제로, 우리 복지관의 실제 업무 현장에서 AI를 안전하고 확실한 협업 파트너로 활용하는 실전 역량을 함께 완성해 보겠습니다.
-->

---
title: 목차
glow: none
---
<!-- slide:2 -->

# 목차

<p class="subtitle">AI의 본질에서 실무 프롬프트, 플러그인 협업, 그리고 <strong>스킬 자산화까지</strong></p>

<script setup>
const tocItems = [
  { num: '01', title: '생성형 AI와 에이전트의 본질', en: 'Principles & Agent' },
  { num: '02', title: 'Gemini Notebook으로 시작하는 자료 기반 AI 문서 작성', en: 'NotebookLM & Deep Research' },
  { num: '03', title: 'ChatGPT Work 도구 및 5대 검토 체계', en: 'Work Tools & Review' },
  { num: '04', title: '나만의 스킬 구축과 업무 자산화 (인수인계 매뉴얼)', en: 'Skill & Welfare Assetization' },
]
</script>

<div class="slide-body mt-2">
  <div class="flex flex-col gap-3 max-w-780px mx-auto">
    <div
      v-for="item in tocItems"
      :key="item.num"
      class="glass-card px-5 py-3.5 flex items-center justify-between transition-all duration-300 hover:border-cyan-500/50 hover:bg-white/8"
    >
      <div class="flex items-center gap-5">
        <span class="font-mono text-2xl font-bold text-cyan-400 min-w-10">{{ item.num }}</span>
        <span class="text-lg font-bold text-white tracking-tight">{{ item.title }}</span>
      </div>
      <span class="font-mono text-xs font-semibold text-slate-400 tracking-wider uppercase">{{ item.en }}</span>
    </div>
  </div>
</div>

<!--
[발표자]
오늘 교육은 크게 네 가지 파트로 구성되어 있습니다.
1부에서는 AI의 기본 원리와 에이전트의 구조를 다지고,
2부에서는 Gemini Notebook(NotebookLM)을 활용한 근거 기반 문서 작성을 배우며,
3부에서는 ChatGPT Work와 플러그인 실무 및 5대 검토 체계를,
4부에서는 우리 복지관만의 반복 업무를 전용 인수인계 매뉴얼 스킬로 자산화하는 실습을 진행합니다.
-->

---
layout: default
glow: none
---
<!-- slide:3 -->

<SectionPartDivider
  title="생성형 AI의 본질에서 AI에이전트까지"
  subtitle="단순 프롬프트 작성을 넘어, AI의 작동 원리와 할루시네이션(RAG), 그리고 스스로 일하는 에이전트 시대로의 도약"
  image="/premium_photo-1764699342973-5d518dede42b.avif"
/>

<!--
[발표자]
첫 번째 파트, 생성형 AI의 본질에서 스스로 일하는 AI 에이전트 시대로의 도약부터 시작하겠습니다.
-->

---
clicks: 3
glow: none
---
<!-- slide:4 -->

# AI를 이해하는 가장 간단한 그림

<p class="subtitle">인공지능(AI)이라는 거대한 우산 안에서 생성형 AI의 정확한 위치를 파악합니다.</p>

<div class="slide-body">
  <AiConcentricRings :stage="$clicks" />
  <div class="slide-footer quote-box text-xs text-center font-medium">
    <strong>핵심 흐름</strong>: 인공지능 (스스로 판단) ➔ 머신러닝 (데이터 학습) ➔ 딥러닝 (뇌 신경망 모방) ➔ <strong>생성형 AI (새로운 콘텐츠 생성)</strong>
  </div>
</div>

<!--
[click] [1] 가장 큰 그릇은 인공지능입니다.
[click] [2] 그 안에 데이터를 학습하는 머신러닝과 딥러닝이 있습니다.
[click] [3] 그리고 오늘 우리가 집중적으로 다룰 생성형 AI는 기존 지식을 조합해 새로운 문서와 양식을 창작하는 최신 기술입니다.
-->

---
clicks: 10
glow: none
---
<!-- slide:5 -->

# 생성형 AI의 본질: 무엇을 만들어내는가?

<p class="subtitle">학습한 데이터의 패턴을 바탕으로 <strong>새로운 합성 콘텐츠(Synthetic Content)</strong>를 생성합니다.</p>

<div class="slide-body">
  <GenerativeAiArchSketch :stage="$clicks" />
</div>

<!--
[발표자]
생성형 AI는 단순히 데이터를 검색하는 것이 아니라, 수많은 학습 데이터의 통계적 패턴을 바탕으로 텍스트, 이미지, 서식 등 새로운 합성 콘텐츠를 직접 생성해 냅니다.
-->

---
glow: none
---
<!-- slide:6 -->

# 우리가 쓰는 ChatGPT의 'GPT'는 무슨 뜻인가?

<p class="subtitle">알파벳 세 글자 속에 모델의 3대 핵심 작동 원리가 모두 담겨 있습니다.</p>

<div class="slide-body">
  <GptFlipCards />
  <div class="slide-footer quote-box text-xs">
    <strong>한 줄 결론</strong>: GPT는 <strong>“사전 학습된 문맥 신경망(Transformer)을 통해 질문에 맞춰 다음 단어를 확률적으로 조립하는 생성(Generative) 모델”</strong>입니다.
  </div>
</div>

<!--
[발표자]
G는 새로운 문장을 만들어 낸다는 뜻(Generative)이고,
P는 방대한 지식을 미리 공부했다는 뜻(Pre-trained)이며,
T는 문맥을 파악해 가장 적절한 다음 단어를 연결해 나가는 신경망(Transformer) 구조입니다.
-->

---
clicks: 2
glow: none
---
<!-- slide:7 -->

# GPT는 '검색엔진'이 아닙니다

<p class="subtitle">검색과 생성의 차이를 이해하지 못하면 AI를 실무에 잘못 활용하게 됩니다.</p>

<div class="slide-body">
  <SearchVsLlmComparison :stage="$clicks" />
  <div class="slide-footer quote-box text-xs">
    <strong>2026년 실무 표준</strong>: 검색(사실 확보)과 생성(문서 작성)을 결합한 <strong>RAG(검색 증강 생성)</strong>로 진화했습니다!
  </div>
</div>

<!--
[click] 검색엔진은 링크를 찾아주는 도구이고,
[click] 생성형 AI는 문서를 대신 작성해 주는 두뇌입니다. 두 기술의 결합이 바로 RAG입니다.
-->

---
clicks: 4
glow: none
---
<!-- slide:8 -->

# 검색(Search) vs 생성(Generation) 비교

<p class="subtitle">두 기술의 장단점을 명확히 알고 결합해서 쓰는 것이 실무자의 핵심 경쟁력입니다.</p>

<div class="slide-body">
  <ComparisonTableSlide7 :stage="$clicks" />
</div>

<!--
[발표자]
검색과 생성의 차이점을 표로 명확히 비교해 보겠습니다.
정확한 사실 확인은 검색으로, 기획서 초안과 문서 정리는 생성형 AI로 결합해 사용하는 것이 실무자의 경쟁력입니다.
-->

---
clicks: 3
glow: none
---
<!-- slide:9 -->

# AI 할루시네이션 (Hallucination)

<p class="subtitle">학습 데이터에 없는 내용도 <strong>너무나 그럴듯하고 자신 있게 지어내는 현상</strong>입니다.</p>

<div class="slide-body">
  <HallucinationSimulator :stage="$clicks" />
</div>

<!--
[발표자]
AI는 모르는 질문을 받아도 “모릅니다”라고 하기보다, 확률적으로 가장 그럴듯한 문장을 지어내는 본질적 특성(할루시네이션)이 있습니다.
-->

---
clicks: 5
glow: none
---
<!-- slide:10 -->

# 할루시네이션을 극복하는 4단계 안전장치

<p class="subtitle">AI가 거짓말을 하지 못하도록 만드는 실무 검증 프레임워크입니다.</p>

<div class="slide-body">
  <HallucinationSafeguardsSketch :stage="$clicks" />
</div>

<!--
[click] [1] 근거 자료 직접 제공,
[click] [2] 엄격한 제약 프롬프트,
[click] [3] 단계별 검증 질의,
[click] [4] 담당자의 최종 확인으로 환각을 100% 방지할 수 있습니다.
-->

---
clicks: 6
glow: none
---
<!-- slide:11 -->

# RAG란 무엇인가? (검색 증강 생성)

<p class="subtitle">Retrieval-Augmented Generation — <strong>기억으로만 치는 시험 vs 교재를 펼쳐놓고 푸는 오픈북 시험</strong></p>

<div class="slide-body">
  <RagOpenBookSimulator :stage="$clicks" />
</div>

<!--
[발표자]
RAG는 기억에만 의존해 치르는 시험 대신, 우리 복지관 규정집과 지침서를 책상 위에 펼쳐놓고 찾아가며 답안을 작성하게 만드는 오픈북 시험 방식입니다.
-->

---
clicks: 7
glow: none
---
<!-- slide:12 -->

# 그래서 프롬프트(Prompt)가 중요합니다

<p class="subtitle">좋은 프롬프트는 “말을 예쁘게 길게 쓰는 것”이 아니라 <strong>구조화된 지시서</strong>를 작성하는 것입니다.</p>

<div class="slide-body">
  <PromptStructureArchSketch :stage="$clicks" />
</div>

<!--
[발표자]
역할, 배경, 지시, 출력 서식의 4대 표준 구조를 갖춘 구조화된 지시서를 작성해야 정확한 실무 결과물을 얻을 수 있습니다.
-->

---
clicks: 5
glow: none
---
<!-- slide:13 -->

# AI의 발전 4세대: 어디까지 진화했는가?

<p class="subtitle">단순 텍스트 생성을 넘어, 스스로 생각하고 도구를 다루는 <strong>에이전트(Agent) 시대</strong>로 진입했습니다.</p>

<div class="slide-body">
  <AiEvolutionTimelineWave :stage="$clicks" />
</div>

<!--
[발표자]
1세대 규칙 기반부터 3세대 챗봇을 거쳐, 이제 4세대 AI 에이전트는 도구를 다루며 자율적으로 과업을 완수하는 단계로 발전했습니다.
-->

---
glow: none
---
<!-- slide:14 -->

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
      <span class="i-carbon:video text-rose-400 mr-1 inline-block vertical-middle" /> MBC 뉴스데스크 (2026. 02. 06 보도)
    </span>
  </div>
</div>

<!--
[발표자]
실제 글로벌 방송 뉴스에서 보도된 AI 에이전트의 업무 자동화 시연 영상입니다.
-->

---
clicks: 2
glow: none
---
<!-- slide:15 -->

# AI 에이전트는 실제로 어떻게 일하는가?

<p class="subtitle">단 1번의 지시로 <strong>[탐색 ➔ 연산 ➔ 규정검증 ➔ 문서생성]</strong>을 완수하는 자율 실행 시뮬레이터</p>

<div class="slide-body">
  <AiAgentWorkflowDirector :stage="$clicks" />
</div>

<!--
[click] [1] 탐색 및 연산,
[click] [2] 규정 검증과 최종 완성형 문서 생성까지 1번의 지시로 완수합니다.
-->

---
layout: default
glow: none
---
<!-- slide:16 -->

<SectionPartDivider
  title="Gemini Notebook으로 시작하는 자료 기반 AI 문서 작성"
  subtitle="자료가 없는 상태에서 AI와 함께 Deep Research부터 사업계획서 초안 및 AI 검토까지 완성하는 실전 워크플로우"
  image="/image-3_6e6716.webp"
/>

<!--
[발표자]
2부에서는 복지관 실무 자료를 완벽하게 근거로 삼는 Gemini Notebook (NotebookLM) 실무 워크플로우를 진행하겠습니다.
-->

---
clicks: 4
glow: none
---
<!-- slide:17 -->

# Gemini Notebook이란 무엇인가?

<p class="subtitle">내가 제공한 자료를 중심으로 읽고, 찾고, 비교하고, 정리해 주는 <strong>AI 연구·사고 도구</strong></p>

<div class="slide-body">
  <NotebookLmUseCasesShowcase :stage="$clicks" />
</div>

<!--
[발표자]
내가 업로드한 자료만을 기반으로 읽고 비교하여, 100% 출처와 함께 답변해 주는 든든한 연구 조수입니다.
-->

---
clicks: 5
glow: none
---
<!-- slide:18 -->

# 일반 생성형 AI vs Gemini Notebook 비교

<p class="subtitle break-keep"><span class="whitespace-nowrap">“무엇이든 묻는 AI”</span>와 <strong><span class="whitespace-nowrap">“내 자료를 기준으로 묻는 AI”</span></strong>의 결정적 차이</p>

<div class="slide-body">
  <ComparisonTableSlide17 :stage="$clicks" />
</div>

<!--
[발표자]
일반 AI와 NotebookLM의 결정적 차이를 비교하여 우리 복지관 업무에 알맞게 선택하는 기준을 제시합니다.
-->

---
glow: none
---
<!-- slide:19 -->

# Gemini Notebook의 3분할 기본 구조:<br>Sources / Chat / Studio

<p class="subtitle">화면을 세 영역으로 기억하면 끝납니다 — <strong>자료 관리, 심층 질문, 결과물 제작</strong></p>

<div class="slide-body">
  <NotebookLmTriSplitArchitecture />
</div>

<!--
[발표자]
왼쪽의 자료 관리(Sources), 중앙의 심층 질문(Chat), 오른쪽의 결과물 제작(Studio) 3분할 구조입니다.
-->

---
clicks: 5
glow: none
---
<!-- slide:20 -->

# 실전 실습: 자료가 없는 상태에서 사업 문서 만들기

<p class="subtitle">종합사회복지관 신규 사업 기획 — <strong>자료조사 ➔ 선별 ➔ 분석 ➔ 정리 메모를 새 자료로 ➔ 초안 ➔ 검토</strong></p>

<div class="slide-body">
  <GeminiNotebookPracticeWorkflow :stage="$clicks" />
</div>

<!--
[click] 자료조사부터 선별, 분석, 초안 작성, 모의 심사 검토까지 6단계 실습 워크플로우입니다.
-->

---
layout: default
glow: none
---
<!-- slide:21 -->

<SectionPartDivider
  title="ChatGPT Work 환경과 다중 파일 기반 실무 문서 작성"
  subtitle="단순 대화를 넘어, 로컬 폴더 연결과 플러그인·스킬로 완성하는 고품질 결과보고서(DOCX)"
  video="/chatgpt-work-select-1080p-v1.mp4"
/>

<!--
[발표자]
3부에서는 ChatGPT Work 환경과 플러그인을 활용한 다중 파일 기반 실무 문서 작성법을 다룹니다.
-->

---
clicks: 4
glow: none
---
<!-- slide:22 -->

# ChatGPT Work란?

<p class="subtitle">단순 대화를 넘어 <strong>실제 업무(기획서·슬라이드·분석표)를 위임</strong>하고 완성형 파일을 받는 업무 실행 환경</p>

<div class="slide-body">
  <ChatGPTWorkIntro :stage="$clicks" />
</div>

<!--
[발표자]
내 컴퓨터 폴더를 연결하여 워드, 파워포인트, 엑셀 파일을 직접 다운로드받을 수 있는 업무 실행 환경입니다.
-->

---
clicks: 15
glow: none
---
<!-- slide:23 -->

# Chat vs Work vs Codex 3대 실행 환경 비교

<p class="subtitle">단순 대화(Chat), <strong>로컬 파일 기반 산출물 제작(Work)</strong>, 개발 환경(Codex)의 명확한 역할과 최소 권한 원칙</p>

<div class="slide-body">
  <ChatWorkCodexComparison :stage="$clicks" />
</div>

<!--
[발표자]
Chat, Work, Codex의 3대 실행 환경 비교와 사회복지사 실무에 최적화된 Work 모드의 역할을 설명합니다.
-->

---
glow: none
---
<!-- slide:24 -->

# 무엇을 먼저 시도해볼까요?

<p class="subtitle">ChatGPT Work로 즉시 시작할 수 있는 <strong>3대 실무 스타터 유스케이스</strong>와 실전 프롬프트</p>

<div class="slide-body">
  <WhatToTryFirst />
</div>

<!--
[발표자]
내일 출근해서 바로 써먹을 수 있는 3대 실무 스타터 유스케이스입니다.
-->

---
glow: none
---
<!-- slide:25 -->

# 연결이 만드는 차이: 플러그인

<p class="subtitle">단순 대화를 넘어 <strong>외부 도구와 실시간 데이터를 연결해 완결형 업무를 수행하는 공식 시연</strong></p>

<div class="slide-body">
  <VideoPluginsDemo />
</div>

<!--
[발표자]
외부 도구와 플러그인이 결합했을 때 나타나는 완결형 업무 시연 영상입니다.
-->

---
glow: none
---
<!-- slide:26 -->

# 주방 요리로 보는 완벽한 1:1 대비: 스킬 vs 플러그인

<p class="subtitle">개인의 <strong>비법 레시피(스킬)</strong>에서 팀 전체가 함께 쓰는 <strong>밀키트 패키지(플러그인)</strong>로의 확장</p>

<div class="slide-body">
  <SkillPluginCulinaryMetaphor />
</div>

<!--
[발표자]
스킬은 나만의 비법 레시피이고, 플러그인은 도구와 재료가 모두 담긴 밀키트 패키지입니다.
-->

---
glow: none
---
<!-- slide:27 -->

# 실무에서 둘의 차이점 한눈에 비교

<p class="subtitle">세부 지침서인 <strong>스킬(Skill)</strong>과 도구·데이터 번들인 <strong>플러그인(Plugin)</strong>의 5대 핵심 차이</p>

<div class="slide-body">
  <SkillPluginComparisonTable />
</div>

<!--
[발표자]
스킬과 플러그인의 5대 핵심 차이점을 실무 관점에서 명확히 짚어봅니다.
-->

---
clicks: 1
glow: none
---
<!-- slide:28 -->

# 플러그인 호출의 실무 표준: 자연어 vs @명시적 호출

<p class="subtitle">의도 왜곡과 오차를 없애고 <strong>100% 완성형 파일</strong>을 얻는 <strong>@도구이름 명시적 호출 원칙</strong></p>

<div class="slide-body">
  <PluginExplicitCallingStandard :stage="$clicks" />
</div>

<!--
[click] 모호한 자연어 대신 @Documents, @Presentations 처럼 도구 이름을 명시적으로 호출해야 합니다.
-->

---
glow: none
---
<!-- slide:29 -->

# 실무 Use Case: 신규 복지 정책·지침 분석 및 사업기획서 작성

<p class="subtitle">방대한 정책 지침서(PDF)를 <strong>@Documents & @Presentations</strong>로 분석하여 <strong>기획서와 보고자료</strong> 동시 완성</p>

<div class="slide-body">
  <WelfarePolicyUseCase />
</div>

<!--
[발표자]
신규 정책 지침서 PDF를 분석하여 기획서(DOCX)와 발표 슬라이드(PPTX)를 동시에 도출하는 실전 사례입니다.
-->

---
glow: none
---
<!-- slide:30 -->

# 실무 Use Case 2: 설문 결과 분석 및 요약 보고서 작성

<p class="subtitle">기본 데이터 분석 기능으로 통계·차트를 도출하고, <strong>@Documents</strong>로 1쪽 요약 보고서(DOCX) 완성</p>

<div class="slide-body">
  <DataAnalysisUseCase />
</div>

<!--
[발표자]
만족도 설문 엑셀 데이터를 바탕으로 통계 차트와 1쪽 요약 보고서를 완성하는 유스케이스입니다.
-->

---
glow: none
---
<!-- slide:31 -->

# 이제, 여러분의 방식대로 해보세요

<p class="subtitle">오늘 배운 플러그인을 자유롭게 조합해 <strong>업무의 작은 불편 하나를 해결해봅니다.</strong></p>

<div class="slide-body">
  <FreePracticeInspiration />
</div>

<!--
[발표자]
자유 실습을 통해 우리 복지관 업무의 작은 불편 하나를 직접 해결해 봅니다.
-->

---
clicks: 1
glow: none
---
<!-- slide:32 -->

# 보고서 제출 전, 다섯 가지만 확인합니다

<p class="subtitle">AI가 만든 문서는 초안입니다. <strong>최종 확인은 담당자가 합니다.</strong></p>

<div class="slide-body">
  <DocumentFiveChecks :stage="$clicks" />
</div>

<!--
[click] 사실 대조, 기관명, 개인정보 비식별화, 예산 단가, 서식 규격 5가지를 반드시 점검합니다.
-->

---
layout: default
glow: none
---
<!-- slide:33 -->

<SectionPartDivider
  title="나만의 스킬 구축과 업무 자산화"
  subtitle="반복되는 복지 업무를 SKILL.md 매뉴얼로 패키징하고, 복지관 동료들과 함께 쓰는 지속 가능한 지식 자산으로 전환"
  image="/skillcreator.png"
/>

<!--
[발표자]
마지막 4부, 나만의 스킬 구축과 업무 자산화 파트입니다.
-->

---
transition: fade-out
title: 문제 제기: 복지 현장의 반복 문서 고충
glow: none
clicks: 2
class: flex flex-col justify-center items-center relative
---
<!-- slide:34 -->

<h1 class="text-3xl lg:text-4xl font-black text-center absolute transition-all duration-500 ease-in-out max-w-3xl leading-tight"
  :class="$clicks < 1 ? 'top-1/2 -translate-y-1/2 text-white scale-100' : 'top-8 -translate-y-0 text-white/70 scale-75'">
  왜 우리는 매번 같은 복지 양식을 복사하고 있을까?
</h1>

<div class="w-full mt-24" :class="$clicks < 1 ? 'opacity-0 pointer-events-none' : 'opacity-100 transition-opacity duration-500'">
  <div class="grid grid-cols-3 gap-4">
  <v-clicks>
    <div class="glass-card p-5 border-rose-500/40">
      <div class="w-10 h-10 rounded-lg bg-rose-950/90 border border-rose-400/70 flex items-center justify-center text-rose-400 mb-3">
        <span class="i-carbon:time text-xl"></span>
      </div>
      <div class="text-xs font-mono text-rose-300 font-bold uppercase mb-1">01. 문서 야근의 굴레</div>
      <h3 class="text-base font-bold text-white m-0">매번 처음부터 쓰는 고통</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        이용자 상담과 프로그램 진행 후, 밤늦게까지 기획서와 보고서 양식을 채우느라 소진됩니다.
      </p>
    </div>
    <div class="glass-card p-5 border-amber-500/40">
      <div class="w-10 h-10 rounded-lg bg-amber-950/90 border border-amber-400/70 flex items-center justify-center text-amber-400 mb-3">
        <span class="i-carbon:chat-operational text-xl"></span>
      </div>
      <div class="text-xs font-mono text-amber-300 font-bold uppercase mb-1">02. 프롬프트 복붙 한계</div>
      <h3 class="text-base font-bold text-white m-0">매번 달라지는 AI 답변</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        메모장에 저장된 긴 프롬프트를 복사해 넣어도, 양식이 미세하게 틀어지고 사족이 붙어 다시 고쳐야 합니다.
      </p>
    </div>
    <div class="glass-card p-5 border-sky-500/40">
      <div class="w-10 h-10 rounded-lg bg-sky-950/90 border border-sky-400/70 flex items-center justify-center text-sky-400 mb-3">
        <span class="i-carbon:user-avatar text-xl"></span>
      </div>
      <div class="text-xs font-mono text-sky-300 font-bold uppercase mb-1">03. 인수인계 단절</div>
      <h3 class="text-base font-bold text-white m-0">담당자 변경 시 지식 유실</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        선임 복지사의 우수한 기획 노하우가 개인 PC에만 남아있어, 후임자가 오면 다시 맨땅에 헤딩합니다.
      </p>
    </div>
  </v-clicks>
  </div>
</div>

<!--
[발표자]
[click] 복지 현장에서 우리가 겪는 어려움은 너무나 명확합니다.
[click] 첫째, 본연의 복지 서비스보다 서류 작성에 쫓겨 야근이 잦습니다. 둘째, 챗GPT를 써봐도 매번 양식이 깨져서 손이 더 갑니다. 셋째, 담당자가 바뀌면 그동안 쌓인 기획 노하우가 사라집니다.
-->

---
transition: fade-out
title: 개념 정의: AI에게 주는 인수인계 매뉴얼
glow: none
clicks: 2
---
<!-- slide:35 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-1">스킬(Skill): AI를 위한 나만의 업무 인수인계서</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">일회성 질문에서 벗어나, 기관 표준 양식을 영구적인 디지털 자산으로 만듭니다.</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-rose-950/90 border border-rose-400/70 text-rose-300 text-xs font-bold font-mono mb-2">
        <span class="i-carbon:close-outline"></span> 전통적인 방식 (Reality)
      </div>
      <h3 class="text-base font-bold text-white m-0">매번 긴 지시어 복사-붙여넣기</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-2"><span class="i-carbon:close text-rose-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">대화창을 열 때마다 복지관 양식과 지침을 수동 복사</span></li>
        <li class="flex items-start gap-2"><span class="i-carbon:close text-rose-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">지시어가 조금만 빠져도 엉뚱하고 장황한 문체 출력</span></li>
        <li class="flex items-start gap-2"><span class="i-carbon:close text-rose-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">나 혼자만 쓰고 동료 복지사와 공유하기 어려움</span></li>
      </ul>
    </div>
    <div class="mt-3 p-2 rounded-lg bg-black/70 border border-rose-500/30 text-slate-300 text-xs font-mono font-medium">
      결과: 문서 작업 시간 과다 + 들쭉날쭉한 품질
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-bold font-mono mb-2">
        <span class="i-carbon:checkmark-outline"></span> 나만의 복지 매뉴얼 (Expectation)
      </div>
      <h3 class="text-base font-bold text-white m-0">한 번 등록해두는 표준 인수인계서</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-2"><span class="i-carbon:checkmark text-emerald-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">복지관 양식과 작성 규칙을 '인수인계서'로 딱 한 번 저장</span></li>
        <li class="flex items-start gap-2"><span class="i-carbon:checkmark text-emerald-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">"어르신 나들이 기획서 써줘" 한마디에 표준 양식 즉시 완성</span></li>
        <li class="flex items-start gap-2"><span class="i-carbon:checkmark text-emerald-400 font-bold shrink-0 text-sm"></span><span class="leading-relaxed">기관 내 다른 복지사들과 파일 하나로 완벽 공유</span></li>
      </ul>
    </div>
    <div class="mt-3 p-2 rounded-lg bg-black/70 border border-emerald-500/30 text-emerald-300 text-xs font-mono font-medium">
      결과: 기획서 작성 4시간 ➔ 15분 단축 + 기관 표준화
    </div>
  </div>
</v-clicks>
</div>

<div class="mt-3 glass-card px-4 py-2 border-cyan-500/30 flex items-center justify-between">
  <span class="text-xs text-slate-200 font-medium">
    <strong class="text-cyan-300 font-bold">핵심 공식:</strong> "신입 복지사에게 인수인계하듯 규칙을 적어두면, AI가 언제나 똑 부러지게 일합니다."
  </span>
</div>

<!--
[발표자]
스킬이란 복잡한 코딩이 아닙니다.
[click] 신입 복지사가 왔을 때 "우리 복지관 기획서는 이렇게 쓰는 거야"라고 건네주는 업무 인수인계 매뉴얼과 똑같습니다.
[click] 이 매뉴얼을 AI에게 한 번만 쥐여주면, 매번 길게 설명할 필요 없이 단 한 줄만 말해도 완벽한 문서를 만들어냅니다.
-->

---
transition: fade-out
title: 핵심 원리: 필요할 때만 꺼내보는 서류함
glow: none
clicks: 2
---
<!-- slide:36 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">인수인계 매뉴얼의 2단계 작동 원리</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">수십 개의 업무 매뉴얼을 등록해두어도 AI가 헷갈리지 않는 이유</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
  <!-- 1단계: 서류함 대기 -->
  <div class="glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-[11px] font-mono font-bold mb-2">
        1단계 : 서류함에서 대기 (색인표 인지)
      </div>
      <div class="mt-1 text-center py-1">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-black/70 border border-white/15 text-cyan-300 text-xs mb-2">
          <span class="i-carbon:tag-group text-sm"></span> 매뉴얼 명찰 (이름 + 한 줄 설명)
        </div>
        <div class="text-white text-sm font-bold mt-0.5">평소에는 이름표만 기억하고 대기</div>
        <p class="text-slate-200 font-medium text-xs mt-1.5 leading-relaxed m-0">
          기획서, 결과보고서, 설문분석 등 50개 매뉴얼이 있어도<br/>
          AI는 서류함에 어떤 매뉴얼이 있는지만 파악하고 가볍게 대기합니다.
        </p>
      </div>
    </div>
  </div>
  <!-- 2단계: 자동 실행 -->
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between" v-click="1">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-[11px] font-mono font-bold mb-2">
        2단계 : 필요할 때 즉시 펼치기 (자동 활성화)
      </div>
      <div class="mt-1 text-center py-1">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-black/70 border border-emerald-500/30 text-emerald-300 text-xs mb-2">
          <span class="i-carbon:document-view text-sm"></span> 전체 양식 및 작성 규칙 주입
        </div>
        <div class="text-white text-sm font-bold mt-0.5">관련 요청이 들어오는 순간 매뉴얼 펼침</div>
        <p class="text-slate-200 font-medium text-xs mt-1.5 leading-relaxed m-0">
          "어르신 나들이 기획서 써줘"라고 말하는 즉시,<br/>
          해당 기획서 매뉴얼을 꺼내어 기관 양식대로 일사천리로 작성합니다.
        </p>
      </div>
    </div>
  </div>
</div>

<div class="mt-3 glass-card px-4 py-2 border-white/15" v-click="2">
  <div class="flex items-center justify-between text-xs">
    <span class="text-slate-200 font-medium"><span class="i-carbon:idea text-amber-300 mr-1" /> <strong class="text-white">실무 효과:</strong> 복잡한 지시어를 매번 외우거나 복사할 필요가 없습니다.</span>
    <span class="text-emerald-300 font-bold">단 한마디로 기관 표준 양식 100% 자동 호출</span>
  </div>
</div>

<!--
[발표자]
AI가 어떻게 수많은 복지 업무를 헷갈리지 않고 처리할까요?
[click] 평소에는 서류함에 매뉴얼 이름표만 꽂아두고 가볍게 기다립니다.
[click] 그러다 여러분이 "결과보고서 써줘"라고 말하는 순간, 보고서 매뉴얼을 척 꺼내서 서식대로 채워 넣습니다.
-->

---
transition: fade-out
title: 실습 환경: GPTwork 데스크톱 앱
glow: none
clicks: 3
---
<!-- slide:37 -->

<div class="mb-4">
  <h2 class="text-2xl font-black text-white mt-1">우리가 실습할 GPTwork 데스크톱 환경</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">기관 컴퓨터에서 안전하고 간편하게 나만의 매뉴얼을 만드는 실무 도구</p>
</div>

<div class="grid grid-cols-3 gap-4">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/30">
    <div class="flex items-center gap-2 mb-3">
      <div class="w-8 h-8 rounded-lg bg-cyan-950/90 border border-cyan-400/60 flex items-center justify-center text-cyan-300">
        <span class="i-carbon:application text-lg"></span>
      </div>
      <div>
        <h3 class="text-sm font-bold text-white m-0">GPTwork 데스크톱</h3>
        <div class="text-[10px] text-cyan-300 font-mono">로컬 전용 실행기</div>
      </div>
    </div>
    <p class="text-xs text-slate-200 font-medium leading-relaxed m-0">
      복지관 PC에 설치하여 파일 탐색기 및 한글(HWP)/엑셀 자료와 즉시 연동되는 업무 데스크톱.
    </p>
  </div>
  <div class="glass-card p-4 border-emerald-500/30">
    <div class="flex items-center gap-2 mb-3">
      <div class="w-8 h-8 rounded-lg bg-emerald-950/90 border border-emerald-400/60 flex items-center justify-center text-emerald-300">
        <span class="i-carbon:magic-wand text-lg"></span>
      </div>
      <div>
        <h3 class="text-sm font-bold text-white m-0">$skill creator 명령어</h3>
        <div class="text-[10px] text-emerald-300 font-mono">마법사 기능</div>
      </div>
    </div>
    <p class="text-xs text-slate-200 font-medium leading-relaxed m-0">
      채팅창에 `$skill creator`를 입력하면, 대화하듯 질문에 답하면서 나만의 매뉴얼을 자동 생성.
    </p>
  </div>
  <div class="glass-card p-4 border-purple-500/30">
    <div class="flex items-center gap-2 mb-3">
      <div class="w-8 h-8 rounded-lg bg-purple-950/90 border border-purple-400/60 flex items-center justify-center text-purple-300">
        <span class="i-carbon:folder-shared text-lg"></span>
      </div>
      <div>
        <h3 class="text-sm font-bold text-white m-0">폴더 공유 자산화</h3>
        <div class="text-[10px] text-purple-300 font-mono">팀 인수인계</div>
      </div>
    </div>
    <p class="text-xs text-slate-200 font-medium leading-relaxed m-0">
      만들어진 매뉴얼 폴더를 복사해서 동료 복지사에게 전달하면, 팀 전체가 똑같은 품질로 활용 가능.
    </p>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 오늘 실습은 GPTwork 데스크톱 환경에서 진행됩니다.
[click] 복잡한 설정 없이 $skill creator 마법사를 통해 대화하듯 매뉴얼을 뚝딱 만들 수 있습니다.
[click] 만든 매뉴얼은 파일로 저장되어 동료 복지사들과 그대로 공유할 수 있습니다.
-->

---
transition: fade-out
title: 매뉴얼 구조: 이름표와 표준 절차
glow: none
clicks: 2
---
<!-- slide:38 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">인수인계 매뉴얼(SKILL.md)의 2단 구조</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">상단 명찰(언제 쓸까?)과 하단 표준 절차(어떻게 쓸까?)의 명쾌한 구성</p>
</div>

<div class="grid grid-cols-[1.35fr_1fr] items-center gap-4">
  <div class="text-xs font-mono">

```yaml {1-5|6-14}
---
name: writing-welfare-proposals
description: >-
  사회복지 프로그램 사업계획서(프로포절) 초안을 작성하고 기관 양식에 맞춰 검토할 때 사용합니다.
---

# 복지 프로그램 사업계획서 표준 작성 절차

## 1. 기본 분석
- 사업 대상자(독거노인, 다문화아동 등)와 핵심 욕구 파악

## 2. 세부 작성 규칙
- 사업 필요성을 두괄식으로 서술하고 명확한 산출/성과 목표 제시
- 예산 항목과 사업 일정표를 표 형태로 구조화

## 3. 출력 서식
- [사업개요] / [사업필요성] / [세부사업내용] / [기대효과]
```

  </div>

  <div class="flex flex-col gap-3">
    <div v-click="1" class="glass-card p-3 border-cyan-500/40 bg-cyan-950/20">
      <div class="flex items-center gap-2 mb-1">
        <span class="i-carbon:tag text-cyan-300"></span>
        <h4 class="text-xs font-bold text-white m-0">1. 매뉴얼 명찰 (상단 1~5행)</h4>
      </div>
      <p class="text-[11px] text-slate-200 font-medium leading-relaxed m-0">
        AI가 <strong>"이 매뉴얼을 언제 꺼내야 하는지"</strong> 알려주는 이름과 상황 설명입니다.
      </p>
    </div>
    <div v-click="2" class="glass-card p-3 border-emerald-500/40 bg-emerald-950/20">
      <div class="flex items-center gap-2 mb-1">
        <span class="i-carbon:document-tasks text-emerald-300"></span>
        <h4 class="text-xs font-bold text-white m-0">2. 표준 절차서 (하단 6행~)</h4>
      </div>
      <p class="text-[11px] text-slate-200 font-medium leading-relaxed m-0">
        AI가 지켜야 할 <strong>단계별 복지관 양식, 작성 순서, 필수 포함 항목</strong>입니다.
      </p>
    </div>
  </div>
</div>

<!--
[발표자]
인수인계 매뉴얼은 딱 두 덩어리입니다.
[click] 위쪽은 AI가 언제 이 매뉴얼을 펼쳐야 하는지 적어둔 '명찰'입니다.
[click] 아래쪽은 우리 복지관 양식에 맞춰 단계별로 어떻게 써야 하는지 적어둔 '표준 절차서'입니다.
-->

---
transition: fade-out
title: 작성 공식: 좋은 복지 매뉴얼의 3원칙
glow: none
clicks: 3
---
<!-- slide:39 -->

<div class="mb-4">
  <h2 class="text-2xl font-black text-white mt-1">실패 없는 복지 매뉴얼 작성 3대 공식</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">AI가 찰떡같이 알아듣고 정확한 양식으로 작성하게 만드는 비결</p>
</div>

<div class="grid grid-cols-3 gap-4">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/30">
    <div class="w-8 h-8 rounded bg-cyan-950/90 border border-cyan-400/60 flex items-center justify-center text-cyan-300 font-bold text-sm mb-3">
      1
    </div>
    <h3 class="text-sm font-bold text-white m-0">구체적 행동으로 이름 짓기</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      단순히 `proposal`이라고 쓰지 않고, `writing-welfare-proposals`처럼 구체적인 행위로 명명.
    </p>
    <div class="mt-2 p-1.5 rounded bg-black/60 text-[10px] text-cyan-300">
      <span class="i-carbon:checkmark-filled text-cyan-300 inline-block mr-1"></span> writing-welfare-proposals<br/>
      <span class="i-carbon:close-filled text-rose-400 inline-block mr-1"></span> welfare-helper (모호함)
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/30">
    <div class="w-8 h-8 rounded bg-emerald-950/90 border border-emerald-400/60 flex items-center justify-center text-emerald-300 font-bold text-sm mb-3">
      2
    </div>
    <h3 class="text-sm font-bold text-white m-0">'~할 때 사용합니다' 명시</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      설명(description)에 어떤 상황에서 이 매뉴얼을 꺼내야 하는지 구체적인 키워드를 기재.
    </p>
    <div class="mt-2 p-1.5 rounded bg-black/60 text-[10px] text-emerald-300">
      "사업계획서, 프로포절, 배분신청서 작성 시 사용합니다"
    </div>
  </div>
  <div class="glass-card p-4 border-purple-500/30">
    <div class="w-8 h-8 rounded bg-purple-950/90 border border-purple-400/60 flex items-center justify-center text-purple-300 font-bold text-sm mb-3">
      3
    </div>
    <h3 class="text-sm font-bold text-white m-0">1개 매뉴얼 = 1개 업무</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      기획서와 결과보고서를 한 파일에 섞지 않고, 업무별로 1개씩 깔끔하게 분리.
    </p>
    <div class="mt-2 p-1.5 rounded bg-black/60 text-[10px] text-purple-300">
      기획서 매뉴얼 1개 + 결과보고서 매뉴얼 1개
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
매뉴얼을 만들 때 이 3가지만 지키시면 절대 실패하지 않습니다.
[click] 첫째, 이름은 구체적인 행동으로 짓습니다.
[click] 둘째, 설명에는 '언제 써야 하는지' 상황 키워드를 넉넉히 넣습니다.
[click] 셋째, 기획서와 보고서를 섞지 말고 하나의 업무당 매뉴얼 하나씩 만듭니다.
-->

---
transition: fade-out
title: 작성 요령: 창의적 기획 vs 엄격한 규정
glow: none
clicks: 2
---
<!-- slide:40 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">복지 업무 성격에 따른 매뉴얼 작성법</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">참신한 아이디어가 필요할 때와 엄격한 규정이 필요할 때의 차이</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-amber-500/40">
    <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-amber-950/90 border border-amber-400/70 text-amber-300 text-xs font-bold mb-2">
      자율형 매뉴얼 (아이디어 발굴)
    </div>
    <h3 class="text-sm font-bold text-white m-0">신규 프로그램 기획 & 프로포절</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      핵심 방향과 대상자만 제시하고, 참신한 프로그램 활동 내용은 AI가 풍부하게 제안하도록 유도.
    </p>
    <ul class="mt-2 space-y-1 text-xs text-slate-300 font-medium list-none p-0">
      <li>• 고립가구 발굴 프로그램 아이디어 브레인스토밍</li>
      <li>• 아동 정서지원 체험활동 기획</li>
      <li>• 후원자 모금 캠페인 카피 다변화</li>
    </ul>
  </div>
  <div class="glass-card p-4 border-sky-500/40">
    <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-sky-950/90 border border-sky-400/70 text-sky-300 text-xs font-bold mb-2">
      엄격형 매뉴얼 (규정 & 양식 준수)
    </div>
    <h3 class="text-sm font-bold text-white m-0">공문서, 예산 정산, 결과보고서</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      정해진 기관 서식과 예산 비목, 공문서 격식체를 100% 준수하도록 엄격히 통제.
    </p>
    <ul class="mt-2 space-y-1 text-xs text-slate-300 font-medium list-none p-0">
      <li>• 보조금 정산 및 지출결의서 명세 요약</li>
      <li>• 시·군·구청 제출용 공문서 양식 준수</li>
      <li>• 외부 지원사업 표준 결과보고서 양식 출력</li>
    </ul>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 신규 프로그램 기획서는 AI에게 아이디어를 넓게 내도록 자율성을 주고,
[click] 공문서나 예산 보고서는 서식을 토씨 하나 안 틀리게 지키도록 엄격하게 작성 지침을 주는 것이 좋습니다.
-->

---
transition: fade-out
title: 실습 가이드: P01 복지 프로그램 기획서 매뉴얼
glow: none
---
<!-- slide:41 -->

<div class="mb-4">
  <h2 class="text-3xl font-black text-white mt-1">실습 P01: 프로포절(사업기획서) 자동화 매뉴얼 만들기</h2>
  <p class="text-sm text-slate-200 font-medium mt-1">GPTwork 데스크톱에서 복지관 맞춤형 기획서 매뉴얼을 직접 생성합니다.</p>
</div>

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="glass-card p-4 border-cyan-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-cyan-950/90 border border-cyan-400/70 flex items-center justify-center text-cyan-300 font-bold mx-auto mb-3">1</div>
    <h4 class="text-sm font-bold text-white m-0">매뉴얼 마법사 호출</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">GPTwork 채팅창에 `$skill creator` 입력 후 실행</p>
  </div>
  <div class="glass-card p-4 border-emerald-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-emerald-950/90 border border-emerald-400/70 flex items-center justify-center text-emerald-300 font-bold mx-auto mb-3">2</div>
    <h4 class="text-sm font-bold text-white m-0">기획서 규칙 주입</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">우리 복지관 사업계획서 필수 목차 및 작성 원칙 입력</p>
  </div>
  <div class="glass-card p-4 border-purple-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-purple-950/90 border border-purple-400/70 flex items-center justify-center text-purple-300 font-bold mx-auto mb-3">3</div>
    <h4 class="text-sm font-bold text-white m-0">단 한 줄로 테스트</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">"독거 어르신 나들이 기획서 써줘" 입력 후 출력 검증</p>
  </div>
</div>

<!--
[발표자]
이제 실습에 들어가겠습니다! 각자 PC의 GPTwork 화면에서 $skill creator를 켜고, 15분간 첫 번째 기획서 매뉴얼을 함께 완성해보겠습니다.
-->

---
transition: fade-out
title: 실습 템플릿: writing-welfare-proposals
glow: none
---
<!-- slide:42 -->

<div class="mb-2">
  <h2 class="text-xl font-black text-white mt-0.5">실습 템플릿: writing-welfare-proposals/SKILL.md</h2>
</div>

<div class="text-xs font-mono">

```yaml
---
name: writing-welfare-proposals
description: >-
  사회복지 프로그램 사업계획서(프로포절, 배분신청서) 초안을 작성하고 기관 양식에 맞춰 검토할 때 사용합니다.
---

# 사회복지 프로그램 사업계획서 표준 작성 절차

## 1. 기본 정보 파악
- 사업 대상(예: 독거어르신, 저소득 아동) 및 핵심 문제/욕구 분석

## 2. 작성 지침
- **사업 필요성**: 지역사회 문제 현황과 사업의 시급성을 두괄식으로 기술
- **목표 설정**: 산출목표(인원/횟수)와 성과목표(변화도/만족도)를 명확히 분리
- **세부 프로그램**: 준비-진행-평가 3단계 일정 및 담당 인력 배치

## 3. 출력 양식
1. 사업개요 (사업명, 대상, 기간, 예산)
2. 사업 필요성 (3가지 핵심 이유)
3. 세부 사업 내용 (표 형태)
4. 기대효과 (이용자, 기관, 지역사회 차원)
```

</div>

<!--
[발표자]
화면에 보이는 템플릿을 참고하여, 여러분 기관에서 평소 자주 쓰는 기획서 목차를 그대로 넣어주시면 됩니다.
-->

---
transition: fade-out
title: 문제 해결: 매뉴얼이 안 켜질 때 처방전
glow: none
clicks: 3
---
<!-- slide:43 -->

<div class="mb-4">
  <h2 class="text-2xl font-black text-white mt-1">매뉴얼이 자동으로 안 켜질 때 3단계 처방전</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">AI가 매뉴얼을 건너뛰고 일반 챗봇처럼 대답할 때 즉시 해결하는 방법</p>
</div>

<div class="grid grid-cols-3 gap-4">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/30">
    <div class="text-xs text-rose-400 font-bold mb-1">1단계 처방</div>
    <h3 class="text-sm font-bold text-white m-0">설명에 복지 단어 추가</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      description에 '사업계획서, 기획서, 프로포절, 프로그램' 등 자주 쓰는 단어를 보강.
    </p>
    <div class="mt-2 text-[10px] text-rose-300">"배분신청서, 공모사업 작성 시..."</div>
  </div>
  <div class="glass-card p-4 border-amber-500/30">
    <div class="text-xs text-amber-400 font-bold mb-1">2단계 처방</div>
    <h3 class="text-sm font-bold text-white m-0">매뉴얼 이름 직접 부르기</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      대화창에 매뉴얼 이름을 직접 언급하여 정상 작동하는지 테스트.
    </p>
    <div class="mt-2 text-[10px] text-amber-300">"writing-welfare-proposals 매뉴얼로 써줘"</div>
  </div>
  <div class="glass-card p-4 border-emerald-500/30">
    <div class="text-xs text-emerald-400 font-bold mb-1">3단계 처방</div>
    <h3 class="text-sm font-bold text-white m-0">좋은 기획서 예시 1개 넣기</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      과거에 통과되었던 우수 기획서 1개를 매뉴얼 하단에 참고 예시로 추가.
    </p>
    <div class="mt-2 text-[10px] text-emerald-300">"예시: 2025년도 어르신 나들이 기획서"</div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 매뉴얼이 안 켜지면 당황하지 마세요.
[click] 1단계: 설명에 키워드를 더 넣거나, 2단계: 이름을 직접 불러보거나,
[click] 3단계: 우리 기관 우수 기획서 예시 하나만 넣어주면 100% 정상 작동합니다.
-->

---
transition: fade-out
title: 2차시 문제 제기: AI 보고서의 3대 불안 요소
glow: none
clicks: 2
class: flex flex-col justify-center items-center relative
---
<!-- slide:44 -->

<h1 class="text-3xl lg:text-4xl font-black text-center absolute transition-all duration-500 ease-in-out max-w-3xl leading-tight"
  :class="$clicks < 1 ? 'top-1/2 -translate-y-1/2 text-white scale-100' : 'top-8 -translate-y-0 text-white/70 scale-75'">
  AI에게 보고서를 맡겼더니 왜 엉뚱한 거짓말을 할까?
</h1>

<div class="w-full mt-24" :class="$clicks < 1 ? 'opacity-0 pointer-events-none' : 'opacity-100 transition-opacity duration-500'">
  <div class="grid grid-cols-3 gap-4">
  <v-clicks>
    <div class="glass-card p-4 border-rose-500/40">
      <div class="w-8 h-8 rounded bg-rose-950/90 border border-rose-400/70 flex items-center justify-center text-rose-400 font-bold mb-2">1</div>
      <h3 class="text-sm font-bold text-white m-0">지침서 환각 (규정 왜곡)</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        복지관 고유 지침을 모른 채 인터넷 일반 지식으로 그럴듯하게 지어내어 답변.
      </p>
    </div>
    <div class="glass-card p-4 border-amber-500/40">
      <div class="w-8 h-8 rounded bg-amber-950/90 border border-amber-400/70 flex items-center justify-center text-amber-400 font-bold mb-2">2</div>
      <h3 class="text-sm font-bold text-white m-0">서식 누락 (양식 무시)</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        결과보고서 필수 항목(참여자 수, 목표 달성도, 예산 집행액)을 건너뛰고 줄글로 출력.
      </p>
    </div>
    <div class="glass-card p-4 border-sky-500/40">
      <div class="w-8 h-8 rounded bg-sky-950/90 border border-sky-400/70 flex items-center justify-center text-sky-400 font-bold mb-2">3</div>
      <h3 class="text-sm font-bold text-white m-0">설문 통계 암산 오류</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        만족도 점수 평균이나 인원수 비율을 계산할 때 단순 챗봇의 덧셈 실수 발생.
      </p>
    </div>
  </v-clicks>
  </div>
</div>

<!--
[발표자]
[click] AI에게 보고서를 쓰게 했을 때 왜 이런 문제가 생길까요?
[click] 우리 복지관 사업지침서를 제대로 쥐여주지 않았거나, 서식 규칙을 단계별로 강제하지 않았기 때문입니다. 이제 이 3대 불안 요소를 완벽히 해결해보겠습니다.
-->

---
transition: fade-out
title: 3단계 런타임: 복지 보고서 자동 완성 흐름
glow: none
clicks: 3
---
<!-- slide:45 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">3단계 무결점 보고서 완성 파이프라인</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">거친 현장 메모에서 완벽한 공문서 결과보고서로 변환되는 3단계 과정</p>
</div>

<div class="grid grid-cols-[1.1fr_1.4fr] gap-6 items-center">
  <div class="glass-card p-4 border-cyan-500/30 flex flex-col justify-center items-center text-center">
    <span class="i-carbon:document-preliminary text-6xl text-cyan-300 mb-3"></span>
    <h3 class="text-base font-bold text-white m-0">거친 메모 ➔ 완벽한 공문서</h3>
    <p class="text-xs text-slate-300 mt-2 leading-relaxed m-0">
      "오늘 20명 어르신 나들이 완료, 만족도 4.8점, 식사 좋았음" 단 3줄 메모만으로 정식 결과보고서 자동 생성.
    </p>
  </div>

  <div class="border-l-2 border-cyan-500/40 pl-6 py-2 flex flex-col gap-4">
  <v-clicks>
    <div class="flex items-start gap-3 relative">
      <div class="w-8 h-8 rounded-full bg-cyan-950/90 border-2 border-cyan-400 text-cyan-300 shadow-[0_0_15px_rgba(6,182,212,0.6)] flex items-center justify-center -ml-10.5 shrink-0">
        <span class="i-carbon:flash-filled text-base" />
      </div>
      <div>
        <div class="text-sm font-bold text-white">1단계 · 보고서 매뉴얼 자동 감지</div>
        <div class="text-xs text-slate-300 mt-0.5">"결과보고서 써줘" 입력 시 복지관 표준 보고서 서식 즉시 호출</div>
      </div>
    </div>
    <div class="flex items-start gap-3 relative">
      <div class="w-8 h-8 rounded-full bg-purple-950/90 border-2 border-purple-400 text-purple-300 shadow-[0_0_15px_rgba(168,85,247,0.6)] flex items-center justify-center -ml-10.5 shrink-0">
        <span class="i-carbon:folder-shared text-base" />
      </div>
      <div>
        <div class="text-sm font-bold text-white">2단계 · 기관 사업지침서 자동 참조</div>
        <div class="text-xs text-slate-300 mt-0.5">보조금 지침 파일(`references/`)을 조회하여 팩트 기반 작성</div>
      </div>
    </div>
    <div class="flex items-start gap-3 relative">
      <div class="w-8 h-8 rounded-full bg-emerald-950/90 border-2 border-emerald-400 text-emerald-300 shadow-[0_0_15px_rgba(16,185,129,0.6)] flex items-center justify-center -ml-10.5 shrink-0">
        <span class="i-carbon:checkmark-filled text-base" />
      </div>
      <div>
        <div class="text-sm font-bold text-white">3단계 · 공문서 5대 검토 및 최종 출력</div>
        <div class="text-xs text-slate-300 mt-0.5">개인정보 비식별화, 예산 항목 일치, 성과 지표 도출 완료</div>
      </div>
    </div>
  </v-clicks>
  </div>
</div>

<!--
[발표자]
[click] 1단계: 여러분이 거친 메모 몇 줄만 던지면 AI가 결과보고서 매뉴얼을 꺼냅니다.
[click] 2단계: 복지관 사업지침서 파일을 훑어서 올바른 예산 비목과 기준을 확인합니다.
[click] 3단계: 개인정보를 보호하고 성과를 수치화한 완벽한 보고서를 출력합니다.
-->

---
transition: fade-out
title: 지침서 연동: 50페이지 복지 규정 분리의 위력
glow: none
clicks: 2
---
<!-- slide:46 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">지침서 분리 연동: 100% 팩트 기반 보고서</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">복지관 운영 지침서를 매뉴얼과 분리하여 AI의 거짓말(환각)을 완벽 차단</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/30">
    <div class="text-xs text-rose-400 font-bold mb-1">안티패턴: 매뉴얼에 지침을 다 때려넣기</div>
    <h3 class="text-sm font-bold text-white m-0">매번 50페이지 지침서를 복사</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      글자 수가 너무 많아 AI가 지침의 중요한 단서 조항을 놓치고 엉뚱한 규정을 지어냅니다.
    </p>
    <div class="mt-2 p-2 rounded bg-black/60 text-xs text-rose-400">
      위험: 보조금 집행 기준 위반 리스크 발생
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/30">
    <div class="text-xs text-emerald-400 font-bold mb-1">모범 패턴: references/ 지침서 파일 연동</div>
    <h3 class="text-sm font-bold text-white m-0">references/사업지침서.md 별도 보관</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      매뉴얼은 가볍게 유지하고, AI가 필요할 때만 지침서 파일을 열어 해당 조항을 정확히 인용.
    </p>
    <div class="mt-2 p-2 rounded bg-black/60 text-xs text-emerald-300">
      안전: 100% 지침서 조항 기반 무결점 공문서 완성
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 지침서를 매번 대화창에 복사해 넣으면 AI가 내용을 섞어서 엉뚱한 말을 지어냅니다.
[click] 지침서 파일을 references/ 폴더에 따로 꽂아두면, AI가 필요할 때마다 책을 펼치듯 정확한 조항만 확인하고 보고서를 씁니다.
-->

---
transition: fade-out
title: 복지 실무 사례 1: 사례관리 기록 & 상담일지
glow: none
clicks: 2
---
<!-- slide:47 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">사례관리: 거친 상담 메모 ➔ 정식 상담일지</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">개인정보를 철저히 보호하며 핵심 욕구와 개입 계획을 3줄로 구조화</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-cyan-950/90 text-cyan-300 text-xs font-bold mb-2">
      사례관리 매뉴얼 · summarizing-case-notes
    </div>
    <h3 class="text-sm font-bold text-white m-0">상담 메모 ➔ 전문 사례기록 변환</h3>
    <ul class="mt-2 space-y-1.5 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 두서없이 적은 가정방문 메모에서 핵심 문제 추출</li>
      <li>• 경제, 주거, 건강, 정서 4대 영역별 욕구 자동 분류</li>
      <li>• 다음 회기 개입 목표 및 서비스 연계 계획 제안</li>
    </ul>
  </div>
  <div class="glass-card p-4 border-purple-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-purple-950/90 text-purple-300 text-xs font-bold mb-2">
      개인정보 안심 보호 규칙 (Privacy First)
    </div>
    <h3 class="text-sm font-bold text-white m-0">자동 비식별화 필터링</h3>
    <ul class="mt-2 space-y-1.5 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 실명 ➔ 'OOO 어르신', 주민번호 ➔ '70대 남성' 자동 치환</li>
      <li>• 상세 주소 ➔ 'OO동 인근 다세대주택'으로 익명화</li>
      <li>• 외부 유출 걱정 없는 100% 안전한 상담 기록 완성</li>
    </ul>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 가정방문 다녀와서 적은 거친 메모를 매뉴얼에 넣으면, 경제/주거/건강 4대 영역으로 깔끔하게 정리된 상담일지가 나옵니다.
[click] 특히 실명이나 주민번호는 자동으로 'OOO 대상자'로 비식별화되어 개인정보 걱정이 전혀 없습니다.
-->

---
transition: fade-out
title: 복지 실무 사례 2: 후원자 감사편지 & 소식지
glow: none
clicks: 2
---
<!-- slide:48 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">후원·홍보: 맞춤형 감사편지 & 소식지 기사</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">후원자 유형별(개인/기업) 맞춤 편지와 감동적인 복지관 소식지 원고 작성</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-emerald-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-emerald-950/90 text-emerald-300 text-xs font-bold mb-2">
      후원 관리 매뉴얼 · writing-donor-letters
    </div>
    <h3 class="text-sm font-bold text-white m-0">후원자 맞춤형 3단 감사서신</h3>
    <ul class="mt-2 space-y-1 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 개인 정기후원자: 따뜻한 감사 인사와 성과 체감 전달</li>
      <li>• 기업/단체 후원자: 후원금 집행 투명성과 사회공헌 가치 강조</li>
      <li>• 명절/연말 시즌별 맞춤 안부 인사 1분 완성</li>
    </ul>
  </div>
  <div class="glass-card p-4 border-sky-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-sky-950/90 text-sky-300 text-xs font-bold mb-2">
      홍보 기사 매뉴얼 · drafting-newsletter-stories
    </div>
    <h3 class="text-sm font-bold text-white m-0">복지관 소식지 & 보도자료 기사화</h3>
    <ul class="mt-2 space-y-1 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 프로그램 진행 사진 설명 몇 줄 ➔ 감동적인 인터뷰형 기사</li>
      <li>• 지역 언론사 배포용 표준 보도자료 양식 자동 생성</li>
      <li>• 기관 SNS(블로그, 인스타그램)용 카드뉴스 카피 동시 도출</li>
    </ul>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] 매달 보내야 하는 후원자 감사편지도 개인용, 기업용 톤앤매너에 맞춰 즉시 작성됩니다.
[click] 프로그램 사진과 메모 몇 줄만 주면 소식지 기사와 보도자료까지 한 번에 완성됩니다.
-->

---
transition: fade-out
title: 복지 실무 사례 3: 복지관 이용안내 FAQ 자동화
glow: none
clicks: 2
---
<!-- slide:49 -->

<div class="mb-3">
  <h2 class="text-2xl font-black text-white mt-0.5">운영 안내: 복지관 이용안내 FAQ 자동화</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">반복되는 전화 문의와 이용자 질문 응대 시간 80% 절감</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-cyan-950/90 text-cyan-300 text-xs font-bold mb-2">
      이용안내 매뉴얼 · answering-center-faq
    </div>
    <h3 class="text-sm font-bold text-white m-0">복지관 5대 단골 문의 자동 답변</h3>
    <ul class="mt-2 space-y-1 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 셔틀버스 노선 및 시간표 안내</li>
      <li>• 경로식당 이용 대상 및 식권 구매 방법</li>
      <li>• 평생교육 프로그램 수강신청 일정 및 감면 혜택</li>
    </ul>
  </div>
  <div class="glass-card p-4 border-purple-500/30">
    <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-purple-950/90 text-purple-300 text-xs font-bold mb-2">
      복지 혜택 안내 매뉴얼 · guiding-welfare-benefits
    </div>
    <h3 class="text-sm font-bold text-white m-0">맞춤형 복지 서비스 신청 자격 매칭</h3>
    <ul class="mt-2 space-y-1 text-xs text-slate-200 font-medium list-none p-0">
      <li>• 어르신 연령과 소득 기준에 따른 맞춤 돌봄 서비스 안내</li>
      <li>• 동주민센터 및 유관기관 신청 구비서류 목록 자동 출력</li>
      <li>• 복지사가 일일이 찾아보지 않고 정확한 지침 기준 안내</li>
    </ul>
  </div>
</v-clicks>
</div>

<!--
[발표자]
[click] "셔틀버스 몇 시에 와요?", "식당 밥 어떻게 먹어요?" 매일 반복되는 질문에 복지사님들이 지치실 필요 없습니다.
[click] 규정집을 연동한 FAQ 매뉴얼이 친절하고 정확하게 즉시 안내문을 써줍니다.
-->

---
transition: fade-out
title: 실습 가이드: P02 결과보고서 자동화 매뉴얼
glow: none
---
<!-- slide:50 -->

<div class="mb-4">
  <h2 class="text-3xl font-black text-white mt-1">실습 P02: 프로그램 결과보고서 자동화 매뉴얼 제작</h2>
  <p class="text-sm text-slate-200 font-medium mt-1">현장 메모 3줄을 넣으면 정식 결과보고서로 출력되는 실전 매뉴얼을 만듭니다.</p>
</div>

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="glass-card p-4 border-cyan-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-cyan-950/90 border border-cyan-400/70 flex items-center justify-center text-cyan-300 font-bold mx-auto mb-3">1</div>
    <h4 class="text-sm font-bold text-white m-0">매뉴얼 생성 실행</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">GPTwork에서 `reporting-welfare-results` 매뉴얼 생성</p>
  </div>
  <div class="glass-card p-4 border-emerald-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-emerald-950/90 border border-emerald-400/70 flex items-center justify-center text-emerald-300 font-bold mx-auto mb-3">2</div>
    <h4 class="text-sm font-bold text-white m-0">보고서 양식 주입</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">참여자 수, 목표 달성도, 우수 소감, 개선점 목차 설정</p>
  </div>
  <div class="glass-card p-4 border-purple-500/30 text-center">
    <div class="w-10 h-10 rounded-full bg-purple-950/90 border border-purple-400/70 flex items-center justify-center text-purple-300 font-bold mx-auto mb-3">3</div>
    <h4 class="text-sm font-bold text-white m-0">단 한 줄로 테스트</h4>
    <p class="text-xs text-slate-300 mt-2 m-0">실제 진행했던 프로그램 메모를 넣고 완성본 출력 검증</p>
  </div>
</div>

<!--
[발표자]
2세션 종합 실습입니다! 여러분이 실제로 진행하셨던 프로그램 메모를 바탕으로, 10분 만에 정식 결과보고서를 뽑아내는 매뉴얼을 함께 완성해보겠습니다.
-->

---
transition: fade-out
title: 실습 템플릿: reporting-welfare-results
glow: none
---
<!-- slide:51 -->

<div class="mb-2">
  <h2 class="text-xl font-black text-white mt-0.5">실습 템플릿: reporting-welfare-results/SKILL.md</h2>
</div>

<div class="text-xs font-mono">

```yaml
---
name: reporting-welfare-results
description: >-
  사회복지 프로그램 진행 후 현장 메모와 참여자 반응을 바탕으로 정식 결과보고서 초안을 작성할 때 사용합니다.
---

# 사회복지 프로그램 결과보고서 표준 작성 절차

## 1. 입력 내용 분석
- 입력된 참여 인원, 진행 내용, 참여자 소감 메모 확인

## 2. 작성 지침
- **목표 달성도**: 계획 대비 실제 참여 인원 및 목표 달성률(%) 명시
- **우수 사례**: 참여자의 긍정적 변화와 감동적인 현장 소감 2건 인용
- **평가 및 제언**: 잘된 점(강점)과 차기 사업 개선점(보완사항)을 명확히 제시

## 3. 최종 출력 서식
1. [사업 개요]: 사업명, 일시, 장소, 실참여 인원
2. [사업 진행 성과 요약]: 추진 경과 및 주요 프로그램 내용
3. [만족도 및 정성 평가]: 참여자 주요 반응 및 인터뷰 내용
4. [예산 집행 내역]: 총 예산 대비 실집행액 요약
5. [총평 및 차년도 제언]: 향후 발전 방안
```

</div>

<!--
[발표자]
화면의 템플릿을 복사하여 여러분 복지관의 결과보고서 양식에 맞게 수정해보세요.
-->

---
transition: fade-out
title: 총정리 & 피날레: 복지 업무의 영구 자산화
glow: none
---
<!-- slide:52 -->

<div class="mb-4 text-center">
  <h2 class="text-3xl font-black text-white mt-1">복지관 업무를 영구 자산화하는 4단계 로드맵</h2>
  <p class="text-sm text-slate-200 font-medium mt-1">개인의 노하우에서 출발하여 복지관 전체의 든든한 업무 자산으로 진화</p>
</div>

<div class="grid grid-cols-4 gap-3 mt-6">
  <div class="glass-card p-3.5 border-cyan-500/30 text-center">
    <div class="text-xs font-mono text-cyan-400 font-bold mb-1">STEP 1</div>
    <h4 class="text-sm font-bold text-white m-0">나만의 매뉴얼</h4>
    <p class="text-[11px] text-slate-300 mt-2 m-0">자주 쓰는 기획서, 보고서 양식을 나만의 매뉴얼로 만들기</p>
  </div>
  <div class="glass-card p-3.5 border-emerald-500/30 text-center">
    <div class="text-xs font-mono text-emerald-400 font-bold mb-1">STEP 2</div>
    <h4 class="text-sm font-bold text-white m-0">팀 인수인계 공유</h4>
    <p class="text-[11px] text-slate-300 mt-2 m-0">매뉴얼 폴더를 팀원들과 공유하여 신입 복지사 인수인계 단축</p>
  </div>
  <div class="glass-card p-3.5 border-purple-500/30 text-center">
    <div class="text-xs font-mono text-purple-400 font-bold mb-1">STEP 3</div>
    <h4 class="text-sm font-bold text-white m-0">기관 지침서 자산화</h4>
    <p class="text-[11px] text-slate-300 mt-2 m-0">복지관 운영규정과 지침서를 연동해 100% 팩트 기반 업무 체계 구축</p>
  </div>
  <div class="glass-card p-3.5 border-pink-500/30 text-center">
    <div class="text-xs font-mono text-pink-400 font-bold mb-1">STEP 4</div>
    <h4 class="text-sm font-bold text-white m-0">이용자 중심 복지 실현</h4>
    <p class="text-[11px] text-slate-300 mt-2 m-0">단순 서류 업무 시간을 줄여 이용자를 직접 만나는 복지 본연에 집중</p>
  </div>
</div>

<div class="mt-6 glass-card p-4 border-cyan-400/40 text-center bg-cyan-950/20">
  <h3 class="text-lg font-black text-white m-0">"단순한 프롬프트는 잊히지만, 잘 만든 매뉴얼은 복지관의 든든한 유산이 됩니다."</h3>
  <p class="text-xs text-slate-200 mt-1 m-0">오늘 함께하신 모든 사회복지사 선생님들의 열정과 헌신을 진심으로 응원합니다.</p>
</div>

<!--
[발표자]
오늘 만든 '나만의 복지 인수인계 매뉴얼'을 통해 서류 작업에 쏟던 야근 시간을 획기적으로 줄이고, 현장에서 어르신과 아이들을 따뜻하게 만나는 일에 더 집중하실 수 있기를 진심으로 응원합니다.
-->

---
glow: none
---
<!-- slide:53 -->

# “가장 핫한 새로운 개발 언어는 '영어(자연어)'다”

<p class="subtitle">OpenAI 공동창업자이자 테슬라 전 AI 디렉터 <strong>안드레 카파시(Andrej Karpathy)</strong>가 촉발한 <strong>바이브 코딩(Vibe Coding)</strong> 혁명</p>

<div class="slide-body">
  <InstagramEmbed postId="DYlyHEAFLR7" />
</div>

<!--
[발표자]
코딩 문법을 몰라도 한국어로 의도를 설명하면 프로그램이 만들어지는 바이브 코딩 혁명입니다.
-->

---
glow: none
---
<!-- slide:54 -->

# 바이브 코딩(Vibe Coding) 실전 프로젝트 쇼케이스

<p class="subtitle">비개발자도 프롬프트와 기획 의도(PRD)만으로 완성한 <strong>3대 실전 라이브 웹 서비스</strong></p>

<div class="slide-body">
  <VibeCodingProjectsShowcase />
</div>

<!--
[발표자]
비개발자 사회복지사가 기획 의도(PRD)만으로 직접 완성하고 실제 배포한 3대 실전 라이브 웹 서비스 쇼케이스입니다.
카드를 클릭하시면 배포된 웹사이트로 즉시 연결됩니다.
-->

---
glowSeed: 999
glowHue: 215
glow: none
---
<!-- slide:55 -->

<EndingSlide />

<!--
[발표자]
이상으로 목포종합사회복지관 AI 역량 강화 교육을 마치겠습니다.
선생님 여러분의 따뜻한 발걸음에 AI가 든든한 날개가 되기를 진심으로 응원합니다.
대단히 감사합니다!
-->
