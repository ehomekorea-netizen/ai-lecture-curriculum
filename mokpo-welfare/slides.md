---
theme: default
themeMode: dark
title: AI를 활용한 문서 작성 협업 역량 강화
info: 목포종합사회복지관 AI 역량 강화 교육 - 1차시
colorSchema: dark
transition: fade-out
highlighter: shiki
css: unocss
mdc: true
glow: none
glowOpacity: 0.28
glowSeed: 888
glowHue: 215
fonts:
  sans: Radio Canada Big, Pretendard, system-ui, sans-serif
  serif: Source Serif 4, Georgia, serif
  mono: Geist Mono, Fira Code, monospace
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
glowSeed: 102
---
<!-- slide:2 -->

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
2부에서는 실무 프롬프트 엔지니어링과 NotebookLM을 배우며,
3부에서는 ChatGPT Work와 플러그인 실무 및 5대 검토 체계를,
4부에서는 우리 복지관만의 반복 업무를 전용 스킬로 자산화하는 방법을 다룹니다.
-->

---
layout: default
glowSeed: 201
glowHue: 220
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
glowSeed: 202
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
glowSeed: 203
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
glowSeed: 204
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
glowSeed: 205
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
glowSeed: 206
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
glowSeed: 207
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
glowSeed: 208
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
glowSeed: 209
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
glowSeed: 210
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
glowSeed: 211
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
glowSeed: 212
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
glowSeed: 213
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
glowSeed: 301
glowHue: 175
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
glowSeed: 302
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
glowSeed: 303
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
glowSeed: 304
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
glowSeed: 305
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
glowSeed: 401
glowHue: 150
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
glowSeed: 402
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
glowSeed: 403
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
glowSeed: 404
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
glowSeed: 405
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
glowSeed: 406
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
glowSeed: 407
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
glowSeed: 408
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
glowSeed: 409
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
glowSeed: 410
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
glowSeed: 411
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
glowSeed: 412
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
glowSeed: 501
glowHue: 270
---
<!-- slide:33 -->

<SectionPartDivider
  title="나만의 스킬 구축과 업무 자산화"
  subtitle="반복되는 업무 방식을 SKILL.md로 패키징하고, 복지관 동료들과 함께 쓰는 지속 가능한 지식 자산으로 전환"
  image="/skillcreator.png"
/>

<!--
[발표자]
마지막 4부, 나만의 스킬 구축과 업무 자산화 파트입니다.
-->

---
glowSeed: 502
---
<!-- slide:34 -->

# 스킬의 의미

<p class="subtitle">스킬은 한 번의 답변이 아니라, <strong>반복되는 업무의 방식</strong>입니다</p>

<div class="slide-body">
  <SkillMeaningDefinition />
</div>

<!--
[발표자]
스킬은 일회성 프롬프트가 아니라 우리 복지관의 일하는 방식을 표준화하는 소중한 자산입니다.
-->

---
clicks: 3
glowSeed: 503
---
<!-- slide:35 -->

# 스킬을 만드는 과정

<p class="subtitle">나의 업무 방식을 스킬로 만드는 <strong>4단계 워크플로우</strong></p>

<div class="slide-body">
  <SkillCreationProcess :stage="$clicks" />
</div>

<!--
[click] [1] 반복 업무 선정 ➔ [2] 표준 지침서 정리 ➔ [3] SKILL.md 작성 ➔ [4] 검증 및 팀 공유 4단계입니다.
-->

---
glowSeed: 504
---
<!-- slide:36 -->

# 스킬 패키지 디렉토리 구조

<p class="subtitle"><strong>SKILL.md</strong> 중심으로 구성되는 ChatGPT 스킬의 표준 파일 및 폴더 체계</p>

<div class="slide-body">
  <SkillDirectoryStructure />
</div>

<!--
[발표자]
SKILL.md를 중심으로 구성되는 표준 스킬 패키지 디렉토리 구조입니다.
-->

---
glowSeed: 505
---
<!-- slide:37 -->

# 실무 Use Case: 반복되는 프로그램 결과보고 스킬 제작

<p class="subtitle">매달 작성하는 운영일지와 만족도 데이터를 <strong>@skill-creator</strong>로 나만의 전용 보고서 스킬로 자산화</p>

<div class="slide-body">
  <ProgramReportSkillUseCase />
</div>

<!--
[발표자]
월간 운영일지와 출석 데이터를 넣으면 공문 표준 서식 보고서로 즉시 변환하는 실전 스킬 유스케이스입니다.
-->

---
glowSeed: 506
---
<!-- slide:38 -->

# 나만의 스킬 만들기

<p class="subtitle">이제, 나의 반복 업무 하나를 <strong>스킬로 만들어보세요</strong></p>

<div class="slide-body">
  <CreateMyOwnSkill />
</div>

<!--
[발표자]
지금 여러분의 반복 업무 하나를 골라 나만의 스킬로 만들어보는 실습 시간입니다.
-->

---
glowSeed: 507
---
<!-- slide:39 -->

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
glowSeed: 508
---
<!-- slide:40 -->

# 바이브 코딩(Vibe Coding) 실전 프로젝트 쇼케이스

<p class="subtitle">비개발자도 프롬프트와 기획 의도(PRD)만으로 완성한 <strong>3대 실전 라이브 웹 서비스</strong></p>

<div class="slide-body">
  <VibeCodingProjectsShowcase />
</div>

<!--
[발표자]
비개발자 사회복지사가 직접 완성한 3대 실전 웹 서비스 쇼케이스입니다.
-->

---
glowSeed: 999
glowHue: 215
---
<!-- slide:41 -->

<EndingSlide />

<!--
[발표자]
이상으로 목포종합사회복지관 AI 역량 강화 교육을 마치겠습니다.
선생님 여러분의 따뜻한 발걸음에 AI가 든든한 날개가 되기를 진심으로 응원합니다.
대단히 감사합니다!
-->
