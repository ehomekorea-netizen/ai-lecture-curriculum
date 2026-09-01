---
layout: default
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: '생성형 AI를 통한 실무능력 향상'
exportFilename: MC에너지-2026-생성형AI를-통한-실무능력-향상
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
routerMode: hash
---
<!-- slide:01-Cover -->

<CoverSlide />

<style>
/* Global Korean typography & orphan wrap prevention */
.slidev-layout, p, span, div, strong, li, h1, h2, h3, h4 {
  word-break: keep-all;
  overflow-wrap: break-word;
}
</style>

<!--
[오프닝]
안녕하십니까. 1차시 강의를 시작하겠습니다.
이번 시간에는 생성형 AI의 기본 구조를 이해하고, 업무에서 사실에 기반한 결과물을 얻기 위한 프롬프트 작성법과 결과 검증 체계를 살펴보겠습니다.
-->

---
layout: default
glow: none
---
<!-- slide:02-Divider-Session-1 -->

<SectionPartDivider
  part="1차시"
  title="생성형 AI 알아보기"
  subtitle="AI의 기본 작동 구조를 이해하고, 사실에 기반한 업무 결과물을 얻기 위한 프롬프트 작성법과 결과 검증 체계 확립"
  image="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop"
/>

<!--
[강사 멘트]
첫 번째 파트, 생성형 AI 알아보기 세션을 시작하겠습니다.
AI의 작동 원리와 한계를 명확히 짚고, 실무 프롬프트 작성법과 결과 검증 체계를 함께 다져보겠습니다.
-->

---
title: 프롬프트 어조와 정답률 실험
layout: default
class: px-16 py-8
glowSeed: 105
clicks: 2
---
<!-- slide:03-Hook -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  프롬프트 어조와 정답률 실험
</h2>

<HookToneExperiment :stage="$clicks" />

<!--
[강사 멘트]
2025년 최신 연구('Mind Your Tone')에 따르면, 프롬프트의 어조가 AI의 정확도에 직접적인 영향을 미칩니다.
[click 1] 지나치게 공손한 부탁조 표현("검토해주시겠습니까")은 불필요한 토큰으로 주의를 분산시켜 정답률이 80.8%로 가장 낮았습니다.
[click 2] 반면 감정적 미사여구를 뺀 단도직입적이고 명확한 지시문은 84.8%로 최고 정답률을 기록했습니다.
AI를 다룰 때는 감정이나 미사여구가 아닌, '군더더기 없는 명확한 지시(Direct Prompting)'가 핵심입니다.
-->

---
title: 인공지능(AI)과 생성형 AI 계층 구조
layout: default
class: px-16 py-8
glowSeed: 201
clicks: 3
---
<!-- slide:04-AI-Hierarchy -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  인공지능(AI)과 생성형 AI 계층 구조
</h2>

<div class="grid grid-cols-12 gap-8 items-center mt-2">
  <div class="col-span-5 flex items-center justify-center">
    <img src="/ai-ml-dl-hierarchy.png" alt="AI Hierarchy" class="rounded-xl w-full max-h-80 object-contain select-none" />
  </div>
  <div class="col-span-7 flex flex-col justify-between h-84">
    <div class="space-y-2.5">
      <div v-click="1">
        <LiquidGlass glow="blue" :radius="12">
          <div class="p-3.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-blue-400">1. 인공지능 (AI)</span>
              <span class="text-[11px] font-mono text-white/50">가장 포괄적인 개념</span>
            </div>
            <p class="text-xs text-white/80 m-0 mt-1.5 leading-relaxed">
              인간의 학습, 추론, 지각 능력을 컴퓨터 프로그램으로 모방한 모든 기술의 총칭
            </p>
          </div>
        </LiquidGlass>
      </div>
      <div v-click="2">
        <LiquidGlass glow="cyan" :radius="12">
          <div class="p-3.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-cyan-400">2. 머신러닝 & 딥러닝 (ML/DL)</span>
              <span class="text-[11px] font-mono text-white/50">데이터 기반 학습</span>
            </div>
            <p class="text-xs text-white/80 m-0 mt-1.5 leading-relaxed">
              규칙을 직접 코딩하지 않고 데이터를 통해 패턴을 학습(ML)하며, 다층 신경망으로 복잡한 특징을 추출(DL)
            </p>
          </div>
        </LiquidGlass>
      </div>
      <div v-click="3">
        <LiquidGlass glow="emerald" :radius="12">
          <div class="p-3.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-emerald-400">3. 생성형 AI (Generative AI)</span>
              <span class="text-[11px] font-mono text-emerald-300 font-bold">2026 실무 핵심</span>
            </div>
            <p class="text-xs text-white/90 m-0 mt-1.5 leading-relaxed">
              단순 분류·예측을 넘어 <strong>텍스트, 코드, 이미지 등 새로운 산출물을 직접 합성</strong>해내는 최신 딥러닝 기술
            </p>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
AI라는 가장 큰 그릇 안에 데이터를 학습하는 머신러닝이 있고, 그 안에 신경망을 모방한 딥러닝이 있으며, 오늘 우리가 다루는 생성형 AI는 딥러닝을 바탕으로 새로운 결과물을 만들어내는 가장 진화된 영역입니다.
-->

---
title: 머신러닝과 딥러닝 비교
layout: default
class: px-16 py-8
glowSeed: 202
clicks: 1
---
<!-- slide:05-ML-vs-DL -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  머신러닝(ML)과 딥러닝(DL) 비교
</h2>

<div class="flex items-center justify-center my-2">
  <img src="/ml-vs-dl.png" alt="머신러닝 vs 딥러닝" class="rounded-xl max-h-80 w-auto object-contain select-none" />
</div>

<div v-click="1" class="mt-3">
  <LiquidGlass glow="neutral" :radius="12">
    <div class="p-3 px-5 flex items-center justify-center gap-6 text-xs font-mono font-bold text-white/90">
      <span class="text-cyan-400">머신러닝: 사람이 특징(Feature)을 직접 정의</span>
      <span class="text-white/40">vs</span>
      <span class="text-emerald-400 font-bold">딥러닝: 인공신경망이 스스로 복합 특징을 추출 및 분류</span>
    </div>
  </LiquidGlass>
</div>

<!--
[강사 멘트]
머신러닝은 사람이 특징을 골라줘야 했지만, 딥러닝은 심층 신경망을 통해 스스로 데이터의 맥락과 규칙을 찾아냅니다.
이것이 생성형 AI가 인간의 복잡한 문맥을 이해할 수 있는 기술적 기초입니다.
-->

---
title: ChatGPT 어원과 작동 원리 (G·P·T)
layout: default
class: px-16 py-8
glowSeed: 203
clicks: 2
---
<!-- slide:06-GPT-Etymology -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  ChatGPT 어원과 작동 원리 (G·P·T)
</h2>

<PromptEtymologyGlow :stage="$clicks" />

<!--
[강사 멘트]
GPT의 세 글자(G-P-T)는 생성(Generative), 사전학습(Pre-trained), 문맥신경망(Transformer)을 의미합니다.
[click 1] P(Pre-trained): 인터넷 상의 방대한 지식을 미리 공부했습니다.
[click 2] T(Transformer): 단어 간 문맥(Attention)을 파악해 가장 알맞은 다음 단어를 확률적으로 조립하여 새로운 문장을 완성합니다.
-->

---
title: 2026 AI 4대 패러다임 변화
layout: default
class: px-16 py-8
glowSeed: 204
clicks: 2
---
<!-- slide:07-2026-Trends -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  2026 AI 4대 패러다임 변화
</h2>

<div class="grid grid-cols-4 gap-4 mt-3">
  <div v-click="1">
    <LiquidGlass glow="cyan" :radius="14">
      <div class="p-4.5 flex flex-col justify-between h-64">
        <div>
          <div class="mb-3 pb-2 border-b border-cyan-500/20 text-sm font-bold text-cyan-300 whitespace-nowrap">
            ① 사고 모델 (추론)
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            단순 암기 답변을 넘어 스스로 논리를 검증하고 깊이 추론하는 <strong>사고형 모델</strong> 보편화
          </p>
        </div>
        <div class="flex items-center justify-between text-[11px] font-mono text-cyan-300/90 pt-2.5 border-t border-white/10">
          <span>Deep Think</span>
          <span class="font-bold">논리 오차 최소화</span>
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="14">
      <div class="p-4.5 flex flex-col justify-between h-64">
        <div>
          <div class="mb-3 pb-2 border-b border-blue-500/20 text-sm font-bold text-blue-300 whitespace-nowrap">
            ② 에이전트 (실행)
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            텍스트 말대꾸를 넘어 실제 <strong>파일을 읽고, 분석하고, 결과 파일(DOCX/XLSX)을 완결</strong>하는 실행 체계
          </p>
        </div>
        <div class="flex items-center justify-between text-[11px] font-mono text-blue-300/90 pt-2.5 border-t border-white/10">
          <span>ChatGPT Work</span>
          <span class="font-bold">업무 직접 완결</span>
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="2">
    <LiquidGlass glow="emerald" :radius="14">
      <div class="p-4.5 flex flex-col justify-between h-64">
        <div>
          <div class="mb-3 pb-2 border-b border-emerald-500/20 text-sm font-bold text-emerald-300 whitespace-nowrap">
            ③ RAG 지식 (검증)
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            사내 지식 베이스와 업로드 문서를 오픈북으로 대조하는 <strong>Gemini Notebook</strong>의 기본 탑재
          </p>
        </div>
        <div class="flex items-center justify-between text-[11px] font-mono text-emerald-300/90 pt-2.5 border-t border-white/10">
          <span>Notebook RAG</span>
          <span class="font-bold">100% 팩트 보장</span>
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="2">
    <LiquidGlass glow="violet" :radius="14">
      <div class="p-4.5 flex flex-col justify-between h-64">
        <div>
          <div class="mb-3 pb-2 border-b border-purple-500/20 text-sm font-bold text-purple-300 whitespace-nowrap">
            ④ 도구 연동 (확장)
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            @visualize 차트, @document 보고서, 사내 시스템을 <strong>단일 대화창에서 원클릭 제어</strong>
          </p>
        </div>
        <div class="flex items-center justify-between text-[11px] font-mono text-purple-300/90 pt-2.5 border-t border-white/10">
          <span>MCP & Tools</span>
          <span class="font-bold">올인원 제어</span>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
2026년의 AI는 단순한 챗봇이 아닙니다.
스스로 생각하고(Reasoning), 실제 파일을 수정하며(Work), 사내 지식을 대조하고(RAG), 도구를 자유자재로 다루는(Tools) 완벽한 업무 파트너입니다.
-->

---
title: 웹검색과 생성형 AI의 차이
layout: default
class: px-16 py-8
glowSeed: 205
clicks: 1
---
<!-- slide:08-Search-vs-GenAI -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  기존 웹검색 vs 생성형 AI
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2.5">
        <div class="flex items-center gap-2 text-white/90 font-bold text-base">
          <span class="i-carbon:search text-white/60"></span>
          <span>기존 포털 검색</span>
        </div>
        <div class="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-white/10 border border-white/15">
          <span class="i-logos:google text-base"></span>
          <span class="i-simple-icons:naver text-[#03C75A] text-base"></span>
        </div>
      </div>
      <div class="space-y-2.5 text-[13px] text-white/80">
        <p class="m-0 leading-relaxed">✓ 웹상의 수많은 링크와 원문 문서를 사람이 일일이 직접 탐색</p>
        <p class="m-0 leading-relaxed">✓ 정보 수집, 선별, 요약, 문서 작성을 사용자가 100% 직접 수행</p>
        <p class="m-0 leading-relaxed">✓ "어디에 정보가 있는가?"를 찾는 링크 제공 도구</p>
      </div>
    </div>
    <div class="pt-3 border-t border-white/10 text-xs font-mono text-white/50">
      작업 주체: 사용자가 모든 과정을 직접 완결
    </div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="cyan" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-cyan-500/20 pb-2.5">
            <div class="flex items-center gap-2 text-cyan-300 font-bold text-base">
              <span class="i-carbon:chat-bot text-cyan-400"></span>
              <span>생성형 AI</span>
            </div>
            <div class="flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-cyan-500/10 border border-cyan-500/30">
              <span class="i-simple-icons:openai text-base text-[#10A37F]"></span>
              <span class="i-simple-icons:googlegemini text-base text-[#1BA1E3]"></span>
              <span class="text-xs font-mono font-bold text-white/90">GPT · Gemini</span>
            </div>
          </div>
          <div class="space-y-2.5 text-[13px] text-white/90">
            <p class="m-0 leading-relaxed">✓ 방대한 데이터를 추론하여 요구조건에 맞는 산출물을 직접 합성</p>
            <p class="m-0 leading-relaxed">✓ 단순 정보 나열이 아닌 비교표, 기획서, 실무 파일 형태로 가공</p>
            <p class="m-0 leading-relaxed">✓ "원하는 결과물을 어떻게 만들 것인가?"를 해결하는 실행 엔진</p>
          </div>
        </div>
        <div class="pt-3 border-t border-cyan-500/20 text-xs font-mono font-bold text-cyan-300">
          작업 주체: AI가 분석과 초안 작성을 자율 대행
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
검색은 자료가 있는 곳을 알려줄 뿐이지만, 생성형 AI는 그 자료들을 읽고 우리 회사에 맞는 보고서 형태로 직접 가공해 주는 차이가 있습니다.
-->

---
title: AI 환각의 원인과 해결책
layout: default
class: px-16 py-8
glowSeed: 206
clicks: 1
---
<!-- slide:09-Hallucination -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 환각(Hallucination)의 원인과 해결책
</h2>

<HallucinationShowcase :stage="$clicks" />

<!--
[강사 멘트]
AI는 거짓말을 치려는 게 아니라, 그럴듯한 문장을 확률적으로 완성하려다 보니 틀린 답을 냅니다.
따라서 실무에서는 "없는 사실은 추측하지 마라"는 제약과 사내 문서를 반드시 함께 주입해야 합니다.
-->

---
title: AI 결과 검증 3단계
layout: default
class: px-16 py-8
glowSeed: 207
clicks: 2
---
<!-- slide:10-Verification-Criteria -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 답변 결과 검증 3단계
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div>
    <LiquidGlass glow="cyan" :radius="14">
      <div class="p-5 flex flex-col justify-between h-64">
        <div>
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-cyan-500/20 text-sm font-bold text-cyan-300">
            <span class="i-carbon:catalog text-base"></span>
            <span>1단계: 출처 및 수치 확인</span>
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            답변에 포함된 통계 수치, 날짜, 법률/규정 조항이 실제 원본 출처와 정확히 일치하는지 1차 확인합니다.
          </p>
        </div>
        <div class="text-[11px] font-mono text-cyan-300/90 pt-2.5 border-t border-white/10">단순 수치 오타 방지</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="14">
      <div class="p-5 flex flex-col justify-between h-64">
        <div>
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-blue-500/20 text-sm font-bold text-blue-300">
            <span class="i-carbon:compare text-base"></span>
            <span>2단계: 교차 검증 (Cross-Check)</span>
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            검색 엔진이나 사내 타 부서 공식 자료와 대조하여 상충되는 정보나 최신 개정 사항이 없는지 확인합니다.
          </p>
        </div>
        <div class="text-[11px] font-mono text-blue-300/90 pt-2.5 border-t border-white/10">최신성 및 정합성 검증</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="2">
    <LiquidGlass glow="emerald" :radius="14">
      <div class="p-5 flex flex-col justify-between h-64">
        <div>
          <div class="flex items-center gap-2 mb-3 pb-2 border-b border-emerald-500/20 text-sm font-bold text-emerald-300">
            <span class="i-carbon:rule-test text-base"></span>
            <span>3단계: 논리적 인과 점검</span>
          </div>
          <p class="text-[13px] text-white/85 m-0 leading-relaxed">
            전제와 결론 사이에 논리적 비약이 없는지, 제시된 해결책이 우리 회사 현업에 실현 가능한지 점검합니다.
          </p>
        </div>
        <div class="text-[11px] font-mono text-emerald-300 font-bold pt-2.5 border-t border-white/10">실무 채택 최종 승인</div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
AI 결과물은 반드시 [1단계 수치 확인 ➔ 2단계 교차 검증 ➔ 3단계 논리 점검]의 3단 필터를 거쳐 보고서에 반영해야 안전합니다.
-->

---
title: RAG 작동 구조: 사실 기반 오픈북 AI
layout: default
class: px-16 py-8
glowSeed: 208
clicks: 3
---
<!-- slide:11-RAG-Interactive-Stage -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  RAG 작동 구조: 사실 기반 오픈북 AI
</h2>

<RagInteractiveStage :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>
<div v-click="3" class="hidden"></div>

<!--
[강사 멘트]
RAG는 AI에게 오픈북 시험을 치르게 하는 기술입니다.
[click 1] 1단계 검색(Retrieve): 사내 규정집이나 데이터베이스에서 질문과 관련된 정확한 문서를 찾습니다.
[click 2] 2단계 증강(Augment) & 3단계 생성(Generate): 찾아낸 원본 문서를 AI의 컨텍스트에 주입하여, 오직 그 문서에 근거해서만 정확한 정답을 작성하게 만듭니다.
-->

---
title: 프롬프트의 본질: 업무 위임장
layout: default
class: px-16 py-8
glowSeed: 209
clicks: 1
---
<!-- slide:12-Prompt-As-Work-Order -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  프롬프트의 본질: 업무 위임장
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <span class="text-xs font-mono font-bold text-white/70 uppercase">단순 질문 (Chat 방식)</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-white/80 border border-white/5 mb-3">
        "신재생에너지 정책 요약해줘."
      </div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        배경, 목적, 청중, 출력 서식이 없어 교과서적인 뻔한 줄글 답변만 돌아옵니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">재질문 반복 발생</div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-blue-500/20 pb-2">
            <span class="text-xs font-mono font-bold text-blue-300 uppercase">업무 위임 (Work Order 방식)</span>
          </div>
          <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-blue-200 leading-relaxed border border-blue-500/20 mb-2">
            "너는 에너지 정책 분석관이다. MC에너지 임원 보고용으로 2026년 RPS 의무공급비율 개정안의 핵심 영향을 표(항목|현행|개정안|영향)로 1페이지 정리하라."
          </div>
        </div>
        <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">
          단 한 번에 실무 즉시 채택 가능한 보고서 도출
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
프롬프트는 검색창 질문이 아니라 부하 직원에게 건네는 '업무 지시서'입니다.
목적, 청중, 결과물 서식을 명시해야 100점짜리 결과물이 한 번에 나옵니다.
-->

---
title: 실전 프롬프트 4대 기둥 (RCTF)
layout: default
class: px-16 py-8
glowSeed: 210
clicks: 3
---
<!-- slide:13-Rctf-Master-Stage -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실전 프롬프트 4대 기둥 (RCTF)
</h2>

<RctfMasterStage :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>
<div v-click="3" class="hidden"></div>

<!--
[강사 멘트]
모든 프롬프트는 RCTF 4개 기둥만 기억하시면 됩니다.
[click 1] R(역할)과 C(맥락)로 AI에게 전문성과 상황을 심어주고,
[click 2] T(과업)와 F(형식)로 구체적인 작업과 엄격한 서식 제약을 명령합니다.
[click 3] 이 4가지가 결합될 때 재작업 없는 완벽한 실무 산출물이 완성됩니다.
-->

---
title: Zero-shot vs Few-shot (예시 주입)
layout: default
class: px-16 py-8
glowSeed: 211
clicks: 1
---
<!-- slide:14-Few-Shot-Prompting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Zero-shot vs Few-shot (예시 주입)
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 mb-3 border-b border-white/10 pb-2.5">
        <span class="i-carbon:close-outline text-white/50 text-base"></span>
        <span class="text-sm font-bold text-white/90">Zero-shot (예시 없는 단순 요청)</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-white/80 border border-white/5 mb-3 leading-relaxed">
        "MC에너지 거래처 문의를 요약하고 유형을 분류해줘."
      </div>
      <p class="text-[13px] text-white/70 leading-relaxed m-0">
        AI가 문장마다 서식을 제각각 생성하여, <strong>사내 시스템이나 엑셀에 자동으로 연동할 수 없습니다.</strong>
      </p>
    </div>
    <div class="pt-2.5 border-t border-white/10 text-xs font-mono text-rose-400">
      출력 형식 불일치 ➔ 수작업 재가공 필요
    </div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="emerald" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center gap-2 mb-3 border-b border-emerald-500/20 pb-2.5">
            <span class="i-carbon:checkmark-outline text-emerald-400 text-base"></span>
            <span class="text-sm font-bold text-emerald-300">Few-shot (1~2개 표준 예시 주입)</span>
          </div>
          <div class="p-2.5 rounded-xl bg-black/40 font-mono text-[11px] text-emerald-100 leading-relaxed border border-emerald-500/20 mb-2">
            [예시1] "송전 점검 일정" ➔ [유형: 시설운영] [담당: 계통운영팀]<br/>
            [예시2] "요금 정산 문의" ➔ [유형: 정산관리] [담당: 재무기획팀]<br/>
            [입력] "ESS 배터리 충전 이상" ➔ <strong>[유형: 설비장애] [담당: 기술운영팀]</strong>
          </div>
          <p class="text-[12.5px] text-white/85 leading-relaxed m-0">
            표준 샘플을 보고 <strong>사내 DB 규격에 맞는 정형 데이터로 100% 일관되게 출력</strong>합니다.
          </p>
        </div>
        <div class="pt-2.5 border-t border-emerald-500/20 text-xs font-mono font-bold text-emerald-300">
          사내 DB / 엑셀 즉시 자동 연동 완료
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
원하는 서식이나 분류 기준이 있다면 말로 길게 설명하기보다, 화면처럼 1~2개의 완벽한 입출력 샘플(Few-shot)을 보여주는 것이 가장 빠르고 확실합니다.
-->

---
title: 사용자 맞춤설정 (Custom Instructions)
layout: default
class: px-16 py-8
glowSeed: 212
clicks: 1
---
<!-- slide:15-Custom-Instructions -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  사용자 맞춤설정 (Custom Instructions)
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <span class="text-xs font-bold text-cyan-300 uppercase">1영역: 나의 직무 및 소속 정보</span>
        <span class="text-[10px] font-mono text-white/40">Profile Context</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-white/90 leading-relaxed border border-white/5 mb-2">
        "나는 에너지 기업 MC에너지의 기획팀 실무자다.<br/>
        신재생에너지, 전력 계통 수급, 에너지 정책 분석 업무를 담당한다."
      </div>
      <p class="text-[11px] text-white/60 m-0 leading-tight">
        모든 대화 시작 시 AI가 기본 전제로 인지
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-cyan-300">
      직무 배경 기본 탑재
    </div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="emerald" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-emerald-500/20 pb-2">
            <span class="text-xs font-bold text-emerald-300 uppercase">2영역: 답변의 기본 형식 및 어조</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">Default Output</span>
          </div>
          <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-emerald-100 leading-relaxed border border-emerald-500/20 mb-2">
            "답변 시 장황한 미사여구는 생략하고 결론 우선 3줄 개조식으로 요약하라.<br/>
            불확실한 내용은 임의 추측하지 말고 표(Table) 서식을 적극 활용하라."
          </div>
        </div>
        <div class="pt-2 border-t border-emerald-500/20 text-xs font-mono font-bold text-emerald-300">
          모든 프롬프트에 자동 적용되는 황금 서식
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
맞춤설정을 해두면 매번 '나는 에너지 기업 실무자고, 개조식으로 써줘'라고 반복할 필요가 없습니다.
-->

---
title: AI 입력 전 3초 보안 점검과 마스킹
layout: default
class: px-16 py-8
glowSeed: 213
clicks: 1
---
<!-- slide:16-Security-Check -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 입력 전 3초 보안 점검과 마스킹
</h2>

<SecurityMaskingDemo :stage="$clicks" />

<!--
[강사 멘트]
AI에 자료를 넣기 전 딱 3초만 확인하십시오.
사내 프로젝트 코드명, 고객 전화번호, 원가 데이터는 [고객사A], [담당자B]처럼 가명 처리하여 안전하게 분석해야 합니다.
-->

---
title: 실무 프롬프트 5대 체크리스트
layout: default
class: px-14 py-7
glowSeed: 214
clicks: 4
---
<!-- slide:17-Prompt-Checklist -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실무 프롬프트 5대 체크리스트
</h2>

<PromptChecklistInteractive :stage="$clicks" />

<!--
[강사 멘트]
프롬프트를 전송하기 전에 이 5가지 체크리스트(역할, 맥락, 과업, 서식, 보안 마스킹)를 점검하는 습관을 들이시기 바랍니다.
-->

---
title: 1차시 실습 과제 및 루브릭
layout: default
class: px-16 py-8
glowSeed: 215
clicks: 1
---
<!-- slide:18-Mission-Card -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  1차시 실습: 사내 맞춤형 RCTF 프롬프트 작성
</h2>

<div class="grid grid-cols-12 gap-6 mt-2">
  <div class="col-span-6">
    <LiquidGlass glow="blue" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-blue-500/20 pb-2">
            <span class="text-xs font-bold text-blue-300">실습 미션 지침</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-200">실습 20분</span>
          </div>
          <div class="space-y-2 text-xs text-white/90 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>1. 주제 선정:</strong> 본인의 실제 반복 업무 중 하나(보고서, 공문, 데이터 요약 등)를 선정
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>2. RCTF 작성:</strong> Role, Context, Task, Format 요소를 모두 갖춘 프롬프트 완성
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>3. 보안 점검:</strong> 사내 기밀 및 개인정보 마스킹 여부 확인 후 AI 실행
            </div>
          </div>
        </div>
        <div class="text-[10px] font-mono text-blue-300/70 pt-2 border-t border-white/10">개인별 실습 진행</div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-6" v-click="1">
    <LiquidGlass glow="emerald" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-emerald-500/20 pb-2">
            <span class="text-xs font-bold text-emerald-300">평가 루브릭 (수료 기준)</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">100점 만점</span>
          </div>
          <div class="space-y-2 text-xs text-white/90">
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>① RCTF 4대 요소 충실도</span>
              <span class="font-mono text-emerald-300 font-bold">40점</span>
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>② 출력 형식 및 제약 조건의 구체성</span>
              <span class="font-mono text-emerald-300 font-bold">30점</span>
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>③ 보안 마스킹 및 실무 채택 적합성</span>
              <span class="font-mono text-emerald-300 font-bold">30점</span>
            </div>
          </div>
        </div>
        <div class="p-2 rounded-lg bg-black/40 border border-emerald-500/30 text-[11px] text-emerald-200 font-bold flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="i-carbon:award text-emerald-400 text-sm"></span>
            <span>80점 이상 시 1차시 실무 인증 완료</span>
          </div>
          <span class="font-mono">Pass Criteria</span>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
20분 동안 본인의 실무 업무를 바탕으로 RCTF 프롬프트를 작성하고 결과를 검증해 보겠습니다.
-->

---
title: 프롬프트 2대 오류 해결 가이드
layout: default
class: px-16 py-8
glowSeed: 216
clicks: 1
---
<!-- slide:19-Troubleshooting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  프롬프트 2대 오류 해결 가이드
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-2 border-b border-rose-500/20 pb-1.5">
        <span class="text-xs font-bold text-rose-300">오류 ① 답변이 너무 길고 뻔한 소리만 할 때</span>
        <span class="text-[10px] font-mono text-rose-400">장황함</span>
      </div>
      <p class="text-xs text-white/70 leading-relaxed mb-3">
        <strong>원인:</strong> 분량 및 서식 제약(Format)이 누락되어 교과서 전체를 서술함.
      </p>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-cyan-200 border border-cyan-500/20">
        <div class="flex items-center gap-1 text-cyan-400 font-bold mb-1">
          <span class="i-carbon:light"></span>
          <span>처방 프롬프트:</span>
        </div>
        "미사여구를 모두 빼고, 실무 결론만 3줄 개조식으로 요약하라. 각 항목은 50자 이내로 제한하라."
      </div>
    </div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="emerald" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-2 border-b border-emerald-500/20 pb-1.5">
            <span class="text-xs font-bold text-emerald-300">오류 ② 없는 수치를 지어내거나 추측할 때</span>
            <span class="text-[10px] font-mono text-emerald-400">환각</span>
          </div>
          <p class="text-xs text-white/80 leading-relaxed mb-3">
            <strong>원인:</strong> 근거 자료 부재 또는 네거티브 제약 미설정.
          </p>
          <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-emerald-100 border border-emerald-500/20">
            <div class="flex items-center gap-1 text-emerald-400 font-bold mb-1">
              <span class="i-carbon:light"></span>
              <span>처방 프롬프트:</span>
            </div>
            "첨부한 파일의 내용에만 근거하여 답변하라. 데이터에 없는 사실은 임의 추측하지 말고 '확인 불가'로 표시하라."
          </div>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
답변이 길어지면 글머리 기호 3개 제약을 걸고, 거짓말을 하면 '첨부 파일에만 근거하라'는 문장을 추가하십시오.
-->

---
title: 1차시 핵심 요약 및 공식
layout: center
class: text-center px-12
glowSeed: 217
---
<!-- slide:20-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-xs font-mono text-cyan-300 mb-4">
    <span>1차시 핵심 공식</span>
  </div>
  <div class="p-6 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md shadow-2xl max-w-3xl mb-5">
    <div class="text-2xl font-black text-white tracking-tight leading-relaxed">
      지시문은 <span class="text-cyan-400">RCTF</span>로 뼈대를 세우고,<br/>
      지식은 <span class="text-emerald-400">RAG(오픈북)</span>로 채우며,<br/>
      결과는 <span class="text-blue-400">3단계 검증</span>으로 완성한다.
    </div>
  </div>
  <div class="text-xs text-white/50 font-mono">
    2차시에서는 사내 자료를 직접 오픈북으로 연결하는 Gemini Notebook 실무를 학습합니다.
  </div>
</div>

<!--
[1차시 마무리]
1차시 수고하셨습니다.
잠시 휴식 후 2차시 심층 리서치 및 Gemini Notebook 실무로 이어가겠습니다.
-->

---
layout: default
glow: none
---
<!-- slide:21-Divider-Session-2 -->

<SectionPartDivider
  part="2차시"
  title="심층 리서치 & Gemini Notebook"
  subtitle="단순 검색을 넘어선 심층 리서치 방법론과 Gemini Notebook을 활용한 나만의 사내 맞춤형 지식 베이스 구축"
  image="/Gemini-notebook-768x432.webp"
/>

<!--
[2차시 오프닝]
2차시 세션을 시작하겠습니다.
이번 시간에는 웹 검색과 심층 리서치의 차이를 이해하고, Gemini Notebook을 활용해 사내 문서를 안전하게 분석하는 법을 실습하겠습니다.
-->

---
title: 단순 웹검색 vs 심층 리서치
layout: default
class: px-16 py-8
glowSeed: 301
clicks: 1
---
<!-- slide:22-Search-vs-Research -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  단순 웹검색 vs 심층 리서치
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <span class="text-xs font-bold text-white/70 uppercase">단순 웹검색 (Search)</span>
        <span class="text-[10px] font-mono text-white/40">단일 사실 확인</span>
      </div>
      <div class="space-y-2 text-xs text-white/70">
        <p class="m-0 leading-relaxed">✓ "2026년 SMP 전력시장 상한 가격은 얼마인가?"</p>
        <p class="m-0 leading-relaxed">✓ 1~2개 웹사이트의 특정 수치나 단일 정의를 즉시 확인</p>
        <p class="m-0 leading-relaxed">✓ 소요 시간: 10초 이내</p>
      </div>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">단편 정보 확인</div>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="16">
      <div class="p-6 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-blue-500/20 pb-2">
            <span class="text-xs font-bold text-blue-300 uppercase">심층 리서치 (Deep Research)</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold">다각도 종합 분석</span>
          </div>
          <div class="space-y-2 text-xs text-white/90">
            <p class="m-0 leading-relaxed">✓ "2026년 글로벌 LNG 도입 단가 변동이 국내 전력시장에 미칠 3대 파급 효과와 MC에너지 대응 전략"</p>
            <p class="m-0 leading-relaxed">✓ 수십 개 공공 통계, 학술 논문, 산업 보고서 다각도 교차 검증</p>
            <p class="m-0 leading-relaxed">✓ 의사결정용 1페이지 완성 보고서 도출 (소요 시간: 5~10분)</p>
          </div>
        </div>
        <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">
          종합 의사결정 인텔리전스
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
단순 검색은 '단일 사실'을 찾는 것이고, 심층 리서치는 여러 출처를 교차 분석하여 '비즈니스 시사점과 결론'을 도출하는 행위입니다.
-->

---
title: 리서치 4단계 파이프라인
layout: default
class: px-16 py-8
glowSeed: 302
clicks: 3
---
<!-- slide:23-Research-4-Steps -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  리서치 4단계 파이프라인
</h2>

<ResearchFunnelStage :stage="$clicks" />

<!--
[강사 멘트]
리서치는 [1단계 질문 구체화 ➔ 2단계 다중 소스 수집 ➔ 3단계 교차 검증 ➔ 4단계 종합 보고서화]의 4단계를 밟을 때 가장 신뢰할 수 있는 결과가 나옵니다.
-->

---
title: AI 웹검색 3대 질문 공식
layout: default
class: px-16 py-8
glowSeed: 303
clicks: 2
---
<!-- slide:24-Search-Prompting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 웹검색 3대 질문 공식
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div>
    <LiquidGlass glow="cyan" :radius="14">
      <div class="p-4 flex flex-col justify-between h-72">
        <div>
          <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-cyan-500/20 text-xs font-bold text-cyan-300">
            <span class="i-carbon:calendar text-sm"></span>
            <span>공식 ① 기준 연도 명시</span>
          </div>
          <div class="p-2 rounded bg-black/40 font-mono text-[10px] text-cyan-100 mb-2 border border-cyan-500/20">
            "2026년 최신 기준 국내 태양광 REC 가격 추이를 검색하라."
          </div>
          <p class="text-[11px] text-white/70 m-0 leading-relaxed">
            과거 2022~2024년 레거시 데이터가 검색되는 것을 원천 차단합니다.
          </p>
        </div>
        <div class="text-[10px] font-mono text-cyan-300/80 pt-2 border-t border-white/10">최신성 보장</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="14">
      <div class="p-4 flex flex-col justify-between h-72">
        <div>
          <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-blue-500/20 text-xs font-bold text-blue-300">
            <span class="i-carbon:security text-sm"></span>
            <span>공식 ② 공신력 출처 한정</span>
          </div>
          <div class="p-2 rounded bg-black/40 font-mono text-[10px] text-blue-100 mb-2 border border-blue-500/20">
            "산업통상자원부, 전력거래소(KPX), 한국에너지공단 공식 발표만 인용하라."
          </div>
          <p class="text-[11px] text-white/70 m-0 leading-relaxed">
            개인 블로그나 확인되지 않은 커뮤니티 발 노이즈 정보를 배제합니다.
          </p>
        </div>
        <div class="text-[10px] font-mono text-blue-300/80 pt-2 border-t border-white/10">공신력 확보</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="2">
    <LiquidGlass glow="emerald" :radius="14">
      <div class="p-4 flex flex-col justify-between h-72">
        <div>
          <div class="flex items-center gap-1.5 mb-2.5 pb-1.5 border-b border-emerald-500/20 text-xs font-bold text-emerald-300">
            <span class="i-carbon:table-split text-sm"></span>
            <span>공식 ③ 비교 및 출처 표기</span>
          </div>
          <div class="p-2 rounded bg-black/40 font-mono text-[10px] text-emerald-100 mb-2 border border-emerald-500/20">
            "각 수치 뒤에 `[출처: KPX 2026.03 보고서]` 형식으로 링크와 함께 표로 정리하라."
          </div>
          <p class="text-[11px] text-white/80 m-0 leading-relaxed">
            보고서 작성 시 즉시 팩트체크가 가능한 완벽한 인라인 각주 생성.
          </p>
        </div>
        <div class="text-[10px] font-mono text-emerald-300 font-bold pt-2 border-t border-white/10">검증 편의성 극대화</div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
AI에게 검색을 시킬 때는 [1. 기준 연도 ➔ 2. 공신력 출처 ➔ 3. 각주 표기]의 3가지를 반드시 포함해야 고품질 리서치가 완성됩니다.
-->

---
title: Google AI 브랜드 진화와 포지셔닝
layout: default
class: px-16 py-8
glowSeed: 304
clicks: 1
---
<!-- slide:25-Brand-Evolution -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Google AI 브랜드 진화와 포지셔닝
</h2>

<BrandEvolution :stage="$clicks" />

<!--
[강사 멘트]
과거 실험적 프로젝트였던 NotebookLM이 이제 Google의 정식 엔터프라이즈 브랜드인 Gemini Notebook으로 완전히 진화했습니다.
사내 지식 베이스를 구축하는 가장 완벽한 솔루션입니다.
-->

---
title: Gemini Notebook: 사내 문서 기반 지식 비서
layout: default
class: px-16 py-8
glowSeed: 305
clicks: 2
---
<!-- slide:26-Gemini-Notebook-RAG -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Gemini Notebook: 사내 문서 기반 지식 비서
</h2>

<GeminiNotebookRAG :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>

<!--
[강사 멘트]
Gemini Notebook은 사내 문서를 지식 자산으로 전환하는 가장 강력한 노코드 RAG 도구입니다.
[click 1] 첫째, Grounding: 인터넷의 불확실한 소스가 아니라, 우리가 직접 업로드한 사내 규정집·보고서 안에서만 답변을 찾고 인라인 각주를 표시합니다.
[click 2] 둘째, Instant RAG: 복잡한 코딩이나 벡터 DB 구축 없이 파일 드래그 앤 드롭만으로 사내 전용 RAG 환경이 즉시 완성됩니다.
-->

---
title: Gemini Notebook 핵심 구조와 3원칙
layout: default
class: px-14 py-7
glowSeed: 306
clicks: 3
---
<!-- slide:27-Notebook-Studio-Stage -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Gemini Notebook 핵심 구조와 3원칙
</h2>

<GeminiNotebookStudio :stage="$clicks" />

<!--
[강사 멘트]
Gemini Notebook은 좌측 소스 패널, 중앙 근거 채팅, 우측 Studio 9대 산출물 3단으로 구성됩니다.
[click 1] 중앙 채팅창은 각주 번호를 클릭해 원문 대조가 가능하며,
[click 2] 우측 스튜디오에서는 팟캐스트 오디오, 브리핑 문서 등을 원클릭으로 만듭니다.
[click 3] 고품질 문서를 넣고, 각주를 확인하며, 초안으로 활용하는 3원칙을 기억하십시오.
-->

---
title: Gemini Notebook 공식 (S-A-F)
layout: default
class: px-16 py-8
glowSeed: 307
clicks: 2
---
<!-- slide:28-SAF-Framework -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Gemini Notebook 공식 (S-A-F)
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div>
    <LiquidGlass glow="cyan" :radius="14">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-3xl font-mono font-black text-cyan-400 mb-2">S</div>
          <div class="text-sm font-bold text-white mb-2">Source (참조 소스 지정)</div>
          <p class="text-xs text-white/70 leading-relaxed m-0">
            "업로드된 [2026 MC에너지 사업계획서.pdf]와 [전력거래 규정.docx] 파일만 참조하여"
          </p>
        </div>
        <div class="pt-3 border-t border-white/10 text-xs font-mono text-cyan-300">참조 범위 한정</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="1">
    <LiquidGlass glow="blue" :radius="14">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-3xl font-mono font-black text-blue-400 mb-2">A</div>
          <div class="text-sm font-bold text-white mb-2">Action (구체적 분석 과업)</div>
          <p class="text-xs text-white/70 leading-relaxed m-0">
            "두 문서에서 언급된 3분기 예산 증감 항목과 조직 개편의 핵심 변동 사항을 비교 대조하라."
          </p>
        </div>
        <div class="pt-3 border-t border-white/10 text-xs font-mono text-blue-300">명확한 분석 지시</div>
      </div>
    </LiquidGlass>
  </div>

  <div v-click="2">
    <LiquidGlass glow="emerald" :radius="14">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-3xl font-mono font-black text-emerald-400 mb-2">F</div>
          <div class="text-sm font-bold text-white mb-2">Format (산출물 서식 제약)</div>
          <p class="text-xs text-white/80 leading-relaxed m-0">
            "표(구분|사업계획|규정|시사점)로 정리하고 각 항목 뒤에 반드시 문서 페이지 인라인 각주를 달 것."
          </p>
        </div>
        <div class="pt-3 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">각주 포함 표 출력</div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
Notebook에서는 S(Source), A(Action), F(Format)의 3단계로 질문할 때 가장 정확한 인라인 각주 분석표가 생성됩니다.
-->

---
title: 실습 1: ChatGPT 웹검색 (최신 정책 탐색)
layout: default
class: px-16 py-8
glowSeed: 308
clicks: 1
---
<!-- slide:29-Practice-WebSearch -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 1: ChatGPT 웹검색 (최신 정책 탐색)
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="cyan" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-2">실습 프롬프트 입력</div>
          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
            "2026년 최신 기준 국내 신재생에너지 공급의무화제도(RPS) 의무공급비율 개정 사항을 검색하라.<br/><br/>
            1. 산업통상자원부 공식 보도자료 위주로 검색할 것<br/>
            2. 연도별 의무비율 변화를 표로 정리하고 각 항목에 공식 출처 URL을 포함할 것."
          </div>
        </div>
        <div class="text-xs font-mono text-cyan-300 font-bold pt-2 border-t border-white/10">
          최신 정책 팩트 실시간 탐색
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">확인 포인트</div>
          <div class="space-y-2 text-xs text-white/80 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center gap-2">
              <span class="i-carbon:earth text-cyan-400 text-base"></span>
              <span>검색 기능 활성화 및 출처 인용구 링크 확인</span>
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center gap-2">
              <span class="i-carbon:checkmark-outline text-emerald-400 text-base"></span>
              <span>2026년 이전 과거 레거시 수치 배제 여부 검증</span>
            </div>
          </div>
        </div>
        <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
          실습 과제: 최신 검색 검증
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
프롬프트를 입력하고 웹 검색 아이콘이 활성화되며 최신 URL 링크가 달리는지 확인합니다.
-->

---
title: 실습 2: 심층 리서치 (보고서 교차 분석)
layout: default
class: px-16 py-8
glowSeed: 309
clicks: 1
---
<!-- slide:30-Practice-DeepResearch -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 2: 심층 리서치 (보고서 교차 분석)
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="blue" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-blue-300 font-bold uppercase mb-2">심층 리서치 프롬프트</div>
          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
            "2026년 글로벌 LNG 도입 가격 변동 추이가 국내 전력도매가격(SMP)과 MC에너지에 미칠 영향을 심층 분석하라.<br/><br/>
            - 최소 5개 이상의 에너지 전문 연구기관 보고서 교차 검증<br/>
            - 1페이지 임원 보고용 요약(핵심 요인 3가지, 리스크, 실행 대응안) 작성."
          </div>
        </div>
        <div class="text-xs font-mono text-blue-300 font-bold pt-2 border-t border-white/10">
          다각도 심층 인텔리전스 보고서 도출
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">확인 포인트</div>
          <div class="space-y-2 text-xs text-white/80 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              ✓ AI가 질문을 스스로 분해하고 다단계 탐색을 수행하는지 확인
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              ✓ 단순 링크 나열이 아닌 의사결정용 구조화 보고서 완성 여부
            </div>
          </div>
        </div>
        <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
          실습 과제: 심층 보고서 완성
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
Deep Research 기능을 실행하여 다단계 추론과 종합 보고서가 생성되는 과정을 관찰합니다.
-->

---
title: 실습 3: Gemini Notebook 소스 등록
layout: default
class: px-16 py-8
glowSeed: 310
clicks: 1
---
<!-- slide:31-Practice-Notebook-Sources -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 3: Gemini Notebook 소스 등록
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="cyan" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-2">실습 단계 지침</div>
          <div class="space-y-2 text-xs text-white/90 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>1단계:</strong> Gemini Notebook 접속 후 [새 노트북 만들기] 클릭
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>2단계:</strong> 실습용 PDF/문서(사내 규정 샘플, 사업계획서 등) 2~3개 업로드
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>3단계:</strong> 좌측 패널에 소스가 정상 등록되고 AI 가이드 요약이 뜨는지 확인
            </div>
          </div>
        </div>
        <div class="text-xs font-mono text-cyan-300 font-bold pt-2 border-t border-white/10">
          사내 지식 베이스 구축 완료
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">핵심 팁 (Garbage In, Garbage Out)</div>
          <p class="text-xs text-white/70 leading-relaxed m-0">
            문서 스캔본(이미지)보다는 텍스트가 직접 복사되는 원본 PDF나 DOCX 파일을 업로드할 때 검색 정밀도가 극대화됩니다.
          </p>
        </div>
        <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
          실습 과제: 지식 베이스 소스 등록
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
노트북을 생성하고 준비된 실습 파일 2개를 업로드하여 소스 패널을 완성하겠습니다.
-->

---
title: 실습 4: 소스 기반 3단계 질문법
layout: default
class: px-16 py-8
glowSeed: 311
clicks: 2
---
<!-- slide:32-Practice-Deep-Questioning -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 4: 소스 기반 3단계 질문법
</h2>

<div class="grid grid-cols-3 gap-4 mt-3">
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <span class="text-xs font-mono text-cyan-400 font-bold uppercase">1단계: 단순 사실 확인</span>
      <div class="p-2.5 rounded-lg bg-black/40 text-[11px] font-mono text-cyan-200 mt-2 mb-2 border border-white/5">
        "이 규정집에서 출장비 정산 기한과 제출 서류를 조항과 함께 찾아줘."
      </div>
      <p class="text-[11px] text-white/60 m-0 leading-tight">
        인라인 각주 번호 클릭 시 원본 조항 하이라이트 확인
      </p>
    </div>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">팩트 대조</div>
  </div>

  <div v-click="1" class="p-4 rounded-xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <span class="text-xs font-mono text-blue-300 font-bold uppercase">2단계: 다중 문서 비교</span>
      <div class="p-2.5 rounded-lg bg-black/40 text-[11px] font-mono text-blue-200 mt-2 mb-2 border border-blue-500/20">
        "문서A의 추진 일정과 문서B의 예산 집행 계획에서 상충되는 시점이 있는지 찾아줘."
      </div>
      <p class="text-[11px] text-white/70 m-0 leading-tight">
        문서 간 불일치 및 일정 충돌 검증
      </p>
    </div>
    <div class="text-[10px] font-mono text-blue-300 pt-1 border-t border-blue-500/20">교차 대조</div>
  </div>

  <div v-click="2" class="p-4 rounded-xl border border-emerald-500/30 bg-emerald-950/20 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <span class="text-xs font-mono text-emerald-300 font-bold uppercase">3단계: 실무 시사점 도출</span>
      <div class="p-2.5 rounded-lg bg-black/40 text-[11px] font-mono text-emerald-100 mt-2 mb-2 border border-emerald-500/20">
        "업로드된 모든 자료를 종합하여 신임 팀장이 이번 분기에 즉시 실행해야 할 3대 우선과제를 제안해줘."
      </div>
      <p class="text-[11px] text-white/80 m-0 leading-tight">
        근거에 기반한 실무 액션플랜 완성
      </p>
    </div>
    <div class="text-[10px] font-mono text-emerald-300 font-bold pt-1 border-t border-emerald-500/20">액션플랜 도출</div>
  </div>
</div>

<!--
[실습 안내]
1단계 팩트 확인부터 3단계 종합 시사점 도출까지 단계별로 질문을 던져보겠습니다.
-->

---
title: 실습 5: Studio 실무 포맷 변환
layout: default
class: px-16 py-8
glowSeed: 312
clicks: 2
---
<!-- slide:33-Practice-Studio-Outputs -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 5: Studio 실무 포맷 변환
</h2>

<div class="grid grid-cols-3 gap-4 mt-3">
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <div class="flex items-center gap-1.5 text-xs font-bold text-cyan-300 mb-1.5">
        <span class="i-carbon:microphone text-base"></span>
        <span>오디오 팟캐스트 변환</span>
      </div>
      <p class="text-[11px] text-white/70 leading-relaxed m-0 mb-2">
        두 명의 AI 호스트가 사내 문서를 친절하게 대화형 팟캐스트로 해설 (출퇴근/이동 중 청취)
      </p>
    </div>
    <div class="p-2 rounded bg-black/40 text-[10px] font-mono text-cyan-300 border border-cyan-500/20 flex items-center justify-center gap-1.5">
      <span class="i-carbon:audio-console text-xs"></span>
      <span>원클릭 오디오 생성</span>
    </div>
  </div>

  <div v-click="1" class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <div class="flex items-center gap-1.5 text-xs font-bold text-blue-300 mb-1.5">
        <span class="i-carbon:report text-base"></span>
        <span>브리핑 문서 & FAQ</span>
      </div>
      <p class="text-[11px] text-white/70 leading-relaxed m-0 mb-2">
        복잡한 사내 규정이나 방대한 기술 문서를 신규 입사자도 3분 만에 이해하는 Q&A 및 요약본으로 변환
      </p>
    </div>
    <div class="p-2 rounded bg-black/40 text-[10px] font-mono text-blue-300 border border-blue-500/20 flex items-center justify-center gap-1.5">
      <span class="i-carbon:document-view text-xs"></span>
      <span>실무 배포용 요약집</span>
    </div>
  </div>

  <div v-click="2" class="p-4 rounded-xl border border-emerald-500/30 bg-emerald-950/20 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <div class="flex items-center gap-1.5 text-xs font-bold text-emerald-300 mb-1.5">
        <span class="i-carbon:time text-base"></span>
        <span>타임라인 및 스터디 가이드</span>
      </div>
      <p class="text-[11px] text-white/80 leading-relaxed m-0 mb-2">
        사업 일정표 및 프로젝트 마일스톤을 시간 순서대로 정렬하고 핵심 퀴즈 생성
      </p>
    </div>
    <div class="p-2 rounded bg-black/40 text-[10px] font-mono text-emerald-300 font-bold border border-emerald-500/20 flex items-center justify-center gap-1.5">
      <span class="i-carbon:calendar-tools text-xs"></span>
      <span>일정표 자동 정렬</span>
    </div>
  </div>
</div>

<!--
[실습 안내]
우측 Studio 패널에서 [브리핑 문서]와 [오디오 오버뷰]를 클릭하여 즉시 결과물을 생성해 봅니다.
-->

---
title: 실습 6: Canvas 실시간 문서 편집
layout: default
class: px-16 py-8
glowSeed: 313
clicks: 1
---
<!-- slide:34-Practice-Canvas -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 6: Canvas 실시간 문서 편집
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="blue" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-blue-300 font-bold uppercase mb-2">Canvas 실무 편집 지침</div>
          <div class="space-y-2 text-xs text-white/90 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>1. Canvas 열기:</strong> 대화창에서 "이 내용을 Canvas에서 보고서로 다듬어줘" 입력
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>2. 인라인 수정:</strong> 특정 문단을 마우스로 드래그하여 "임원 보고용으로 톤앤매너 수정" 요청
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>3. 파일 내보내기:</strong> 최종 편집 완료 후 `.docx` 문서 파일로 원클릭 다운로드
            </div>
          </div>
        </div>
        <div class="text-xs font-mono text-blue-300 font-bold pt-2 border-t border-white/10">
          대화창 옆 실시간 문서 워드프로세서
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">Canvas의 장점</div>
          <p class="text-xs text-white/70 leading-relaxed m-0">
            전체 텍스트를 처음부터 다시 생성하지 않고, <strong>수정이 필요한 특정 문장이나 표만 골라서 부분 수정</strong>할 수 있습니다.
          </p>
        </div>
        <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
          실습 과제: Canvas 부분 편집
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
Canvas 화면에서 특정 문단을 선택해 수정해 보고 파일로 내보내겠습니다.
-->

---
title: 2차시 실습: Gemini Notebook 지식 허브
layout: default
class: px-16 py-8
glowSeed: 314
clicks: 1
---
<!-- slide:35-Session2-Mission -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  2차시 실습: Gemini Notebook 지식 허브
</h2>

<div class="grid grid-cols-12 gap-6 mt-2">
  <div class="col-span-6">
    <LiquidGlass glow="cyan" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-cyan-500/20 pb-2">
            <span class="text-xs font-bold text-cyan-300">2차시 실습 미션 지침</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-200">실습 과제</span>
          </div>
          <div class="space-y-2 text-xs text-white/90 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>1. 소스 등록:</strong> 업무 관련 자료 2개 이상 등록
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>2. S-A-F 질의:</strong> 출처 각주가 포함된 비교 분석표 도출
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>3. Studio 변환:</strong> [브리핑 문서] 1페이지 생성 완료
            </div>
          </div>
        </div>
        <div class="text-[10px] font-mono text-cyan-300/70 pt-2 border-t border-white/10">개인별 실습 진행</div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-6" v-click="1">
    <LiquidGlass glow="emerald" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-emerald-500/20 pb-2">
            <span class="text-xs font-bold text-emerald-300">평가 루브릭</span>
            <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">100점 만점</span>
          </div>
          <div class="space-y-2 text-xs text-white/90">
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>① 다중 소스 등록 및 유효성</span>
              <span class="font-mono text-emerald-300 font-bold">30점</span>
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>② S-A-F 프롬프트 각주 정확도</span>
              <span class="font-mono text-emerald-300 font-bold">40점</span>
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center justify-between">
              <span>③ Studio 브리핑 문서 완성도</span>
              <span class="font-mono text-emerald-300 font-bold">30점</span>
            </div>
          </div>
        </div>
        <div class="p-2 rounded-lg bg-black/40 border border-emerald-500/30 text-[11px] text-emerald-200 font-bold flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="i-carbon:award text-emerald-400 text-sm"></span>
            <span>80점 이상 시 2차시 리서치 역량 인증</span>
          </div>
          <span class="font-mono">Pass Criteria</span>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
실습 과제를 수행하고 브리핑 문서를 완성해 보시기 바랍니다.
-->

---
title: 2차시 핵심 요약 및 공식
layout: center
class: text-center px-12
glowSeed: 315
---
<!-- slide:36-Session2-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-xs font-mono text-cyan-300 mb-4">
    <span>2차시 핵심 공식</span>
  </div>
  <div class="p-6 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md shadow-2xl max-w-3xl mb-5">
    <div class="text-2xl font-black text-white tracking-tight leading-relaxed">
      외부 웹은 <span class="text-cyan-400">심층 리서치</span>로 검증하고,<br/>
      사내 문서는 <span class="text-emerald-400">Gemini Notebook</span>으로 자산화하며,<br/>
      결과는 <span class="text-blue-400">S-A-F와 Studio</span>로 완성한다.
    </div>
  </div>
  <div class="text-xs text-white/50 font-mono">
    3~4차시에서는 실제 파일을 만들고 업무를 위임하는 ChatGPT Work와 Skill 패키지를 다룹니다.
  </div>
</div>

<!--
[2차시 마무리]
2차시 수고하셨습니다.
다음 3~4차시에서는 에이전트와 도구를 결합하여 실제 결과물 파일을 완결하는 실전 프로젝트를 진행하겠습니다.
-->

---
layout: default
glow: none
---
<!-- slide:37-Divider-Session-3-4 -->

<SectionPartDivider
  part="3~4차시"
  title="ChatGPT Work, 나만의 Skill & 이미지 생성"
  subtitle="말대꾸를 넘어 실제 파일(DOCX/XLSX/비주얼)을 생성·수정하는 Work 모드와 반복 업무를 자동화하는 나만의 Skill 및 이미지 제작 실습"
  image="/gptwork.png"
/>

<!--
[3~4차시 오프닝]
3~4차시 심화 세션을 시작하겠습니다.
이번 시간에는 대화형 챗봇에서 벗어나 실제 파일을 완결하는 ChatGPT Work와 반복 업무를 영구 자산화하는 Skill을 제작하겠습니다.
-->

---
title: 대화(Chat)에서 실행(Work)으로
layout: default
class: px-14 py-7
glowSeed: 401
clicks: 2
---
<!-- slide:38-Chat-vs-Work -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  대화(Chat)에서 실행(Work)으로
</h2>

<ChatVsWorkComparison :stage="$clicks" />

<!--
[강사 멘트]
Chat은 질문에 텍스트로 답을 구하는 것이라면, Work는 목표를 주고 파일 생성과 분석을 AI에게 완전히 맡기는 것입니다.
-->

---
title: ChatGPT Work 구조와 6단계 에이전트 루프
layout: default
class: px-14 py-7
glowSeed: 402
clicks: 5
---
<!-- slide:39-Agent-Execution-Engine -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  ChatGPT Work 구조와 6단계 에이전트 루프
</h2>

<AgentExecutionEngine :stage="$clicks" />

<!--
[강사 멘트]
Work 모드의 내부에서는 AI가 자율적으로 [목표 수신 ➔ 파일 관찰 ➔ 계획 수립 ➔ 도구 호출 ➔ 검토 ➔ 파일 완결]의 6단계 루프를 돕니다.
-->

---
title: Work 모드 핵심: 완성형 파일 생성
layout: default
class: px-14 py-7
glowSeed: 403
clicks: 2
---
<!-- slide:40-Work-Outputs-Hub -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Work 모드 핵심: 완성형 파일 생성
</h2>

<WorkOutputsHub :stage="$clicks" />

<!--
[강사 멘트]
Work의 최종 목적지는 텍스트 답변이 아니라, 사내 보고에 바로 쓰이는 정형화된 파일(DOCX, XLSX, PNG, Code)입니다.
-->

---
title: 도구 생태계와 업무별 최적 도구 매칭
layout: default
class: px-14 py-7
glowSeed: 404
clicks: 3
---
<!-- slide:41-Tool-Ecosystem-Matrix -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  도구 생태계와 업무별 최적 도구 매칭
</h2>

<ToolEcosystemMatrix :stage="$clicks" />

<!--
[강사 멘트]
수치 분석은 Spreadsheet, 시각화는 @visualize, 기획 문서는 @document, 매주 반복 업무는 Skill로 매칭됩니다.
-->

---
title: 엑셀 데이터 분석 4단계 사고법
layout: default
class: px-14 py-7
glowSeed: 405
clicks: 3
---
<!-- slide:42-Excel-Analysis-Pipeline -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  엑셀 데이터 분석 4단계 사고법
</h2>

<ExcelAnalysisPipeline :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>
<div v-click="3" class="hidden"></div>

<!--
[강사 멘트]
엑셀 데이터를 AI에게 맡길 때는 [1. 데이터 상태 점검 ➔ 2. 증감률 분석 ➔ 3. 차트 시각화 ➔ 4. 보고서 완성]의 순서를 지켜야 합니다.
-->

---
title: 실습 1: 엑셀 데이터 상태 파악
layout: default
class: px-16 py-8
glowSeed: 406
clicks: 1
---
<!-- slide:43-Excel-Prompt-1-Inspection -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 1: 엑셀 데이터 상태 파악
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="cyan" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-2">1단계 실습 프롬프트 (데이터 점검)</div>
          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
            "첨부한 엑셀 파일의 시트와 열(Column) 구조를 먼저 파악해줘.<br/><br/>
            1. 각 열이 무엇을 의미하는지 한 줄로 정리하고<br/>
            2. 분석 전 확인해야 할 결측값, 이상값, 중복 데이터가 있는지 찾아줘.<br/>
            3. 아직 데이터를 임의로 수정하지 말고, 발견된 문제만 표로 정리해줘."
          </div>
        </div>
        <div class="text-xs font-mono text-cyan-300 font-bold pt-2 border-t border-white/10">
          데이터 무결성 사전 검증
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">핵심 포인트</div>
          <div class="space-y-2 text-xs text-white/80 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong class="text-white">① 바로 분석 금지:</strong> 결측치나 오타가 있으면 통계가 왜곡됩니다.
            </div>
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong class="text-white">② 임의 수정 방지:</strong> AI가 원본을 바꾸지 않도록 문제만 정리시킵니다.
            </div>
          </div>
        </div>
        <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
          실습 과제: 원본 데이터 상태 점검
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
파일을 업로드하고 1단계 프롬프트를 입력하여 시트 구조와 결측치를 먼저 확인해 보겠습니다.
-->

---
title: 실습 2: 엑셀 추이 분석 & 원인 도출
layout: default
class: px-16 py-8
glowSeed: 407
clicks: 1
---
<!-- slide:44-Excel-Prompt-2-Analysis -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 2: 엑셀 추이 분석 & 원인 도출
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7">
    <LiquidGlass glow="blue" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-blue-300 font-bold uppercase mb-2">2단계 실습 프롬프트 (추이 & 원인)</div>
          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
            "월별 매출 추이를 분석하고 전월 대비 증감률(MoM)을 계산해줘.<br/><br/>
            1. 증감 폭이 가장 큰 상위 5개 항목을 찾아 주요 원인을 데이터에서 확인해줘.<br/>
            2. 데이터에 없는 원인은 임의로 추측하지 말고 '추가 확인 필요'로 표시할 것.<br/>
            3. 결과는 `표(월 | 매출액 | 전월대비 증감률 | 주요 원인)`로 출력하라."
          </div>
        </div>
        <div class="text-xs font-mono text-blue-300 font-bold pt-2 border-t border-white/10">
          근거 기반 수치 통계 분석
        </div>
      </div>
    </LiquidGlass>
  </div>

  <div class="col-span-5" v-click="1">
    <LiquidGlass glow="neutral" :radius="14" class="h-full">
      <div class="p-5 flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">화면 비교 (Before ➔ After)</div>
          <div class="space-y-2 text-xs text-white/80 leading-relaxed">
            <div class="p-2 rounded bg-black/40 border border-white/5">
              <strong>좌측 원본:</strong> 수천 줄의 원시 엑셀 데이터
            </div>
            <div class="p-2 rounded bg-black/40 border border-blue-500/20 text-blue-200">
              <strong>우측 결과:</strong> 증감률 계산 + 5대 이상치 원인 표 완성
            </div>
          </div>
        </div>
        <div class="p-2 rounded-lg bg-black/40 border border-white/10 text-[11px] text-white/70 flex items-center gap-1.5">
          <span class="i-carbon:checkmark text-emerald-400"></span>
          <span>"추측 금지" 제약으로 환각 완벽 방지</span>
        </div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[실습 안내]
2단계 프롬프트를 실행하여 증감률과 원인 분석 표가 자동으로 생성되는지 확인합니다.
-->

---
title: @visualize 플러그인: 실시간 시각화
layout: default
class: px-14 py-6
glowSeed: 408
---
<!-- slide:45-Visualize-Video-Stage -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  @visualize 플러그인: 실시간 시각화
</h2>

<div class="flex justify-center items-center">
  <div class="rounded-2xl overflow-hidden border border-white/15 bg-black shadow-2xl w-[86%]">
    <video
      src="/chatgpt-work-demo.mp4"
      controls
      autoplay
      loop
      muted
      playsinline
      class="rounded-xl w-full max-h-[390px] object-contain"
    ></video>
  </div>
</div>

<!--
[강사 멘트]
영상에서 보시는 것처럼, @visualize 플러그인을 활용하면 대화창 안에서 회의록이나 작업 일정을 타임라인으로 렌더링하고 실시간으로 시각화 양식을 전환할 수 있습니다.
-->

---
title: 실습 4: 피드백을 통한 점진적 수정
layout: default
class: px-16 py-8
glowSeed: 409
clicks: 2
---
<!-- slide:46-Excel-Prompt-4-Iterative-Refine -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 4: 피드백을 통한 점진적 수정
</h2>

<div class="grid grid-cols-3 gap-5 mt-3">
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <span class="text-xs font-mono text-white/40 font-bold uppercase">1차 요청</span>
      <div class="p-2.5 rounded-lg bg-black/40 text-xs font-mono text-white/80 mt-2 mb-2 border border-white/5">
        "매출 추이를 시각화해줘."
      </div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        기본 그래프가 생성되었으나 강조점이 약함
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">초안 생성</div>
  </div>

  <div v-click="1" class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-74">
    <div>
      <span class="text-xs font-mono text-blue-400 font-bold uppercase">2차 수정</span>
      <div class="p-2.5 rounded-lg bg-black/40 text-xs font-mono text-blue-200 mt-2 mb-2 border border-blue-500/20">
        "월별 변화 추이가 눈에 띄도록 꺾은선으로 바꾸고 목표선을 추가해줘."
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        목표 대비 달성 여부와 추세선이 뚜렷해짐
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-blue-300">비교 기준 보강</div>
  </div>

  <div v-click="2">
    <LiquidGlass glow="blue" :radius="14">
      <div class="p-4 flex flex-col justify-between h-74">
        <div>
          <span class="text-xs font-mono text-blue-300 font-bold uppercase">3차 수정 (임원 보고용)</span>
          <div class="p-2.5 rounded-lg bg-black/40 text-[11px] font-mono text-blue-200 mt-2 mb-2 border border-blue-500/30 leading-relaxed">
            "증감이 가장 큰 달을 빨간색으로 강조하고, 임원 보고용 3줄 인사이트를 하단에 추가해줘."
          </div>
          <p class="text-xs text-white/90 leading-relaxed m-0">
            의사결정자가 3초 만에 파악할 수 있는 완성본 도출
          </p>
        </div>
        <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">최종 보고용 완성</div>
      </div>
    </LiquidGlass>
  </div>
</div>

<!--
[강사 멘트]
AI는 한 번에 100점짜리를 뽑는 자판기가 아닙니다.
결과를 보고 2차, 3차 피드백을 주며 원하는 수준으로 다듬어가는 것이 진정한 실무자의 역량입니다.
-->

---
title: AI 도구 생태계와 실제 실행
layout: default
class: px-14 py-6
glowSeed: 410
clicks: 2
---
<!-- slide:47-Work-Tools-Hub -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 도구 생태계와 실제 실행
</h2>

<div class="grid grid-cols-12 gap-5 items-stretch mt-1">
  <div class="col-span-4">
    <WorkToolsHub :stage="$clicks" />
  </div>
  <div class="col-span-8 flex flex-col justify-between">
    <img src="/chatgpt-app-execution.jpg" alt="Real App Execution (@LG ThinQ)" class="rounded-xl w-full max-h-76 object-contain select-none" />
    <div class="p-2.5 rounded-xl bg-black/40 text-xs text-white/90 border border-white/10 leading-relaxed mt-2">
      <strong>실제 구동 화면:</strong> 대화창에서 <code>@LG ThinQ</code>를 호출하여 사내 에어컨/기기 상태를 조회하고 전원·온도 제어를 직접 수행합니다.
    </div>
  </div>
</div>

<!--
[강사 멘트]
[click 1] 좌측 구조도처럼 사용자는 하나의 대화창에서 지시하지만, 백그라운드에서는 Document, Spreadsheet, 그리고 외부 앱들이 유기적으로 협업합니다.
[click 2] 우측 실제 실행 화면처럼 @LG ThinQ 커넥터를 통해 자연어로 실제 사물·기기 상태를 확인하고 전원/온도를 제어하는 엔터프라이즈 도구 생태계가 열렸습니다.
-->

---
title: OpenAI Skill: 반복 업무 패키지화
layout: default
class: px-14 py-6
glowSeed: 411
---
<!-- slide:48-Skill-Video-Stage -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  OpenAI Skill: 반복 업무 패키지화
</h2>

<div class="flex justify-center items-center">
  <div class="rounded-2xl overflow-hidden border border-white/15 bg-black shadow-2xl w-[86%]">
    <video
      src="/chatgpt-skill-demo.mp4"
      controls
      autoplay
      loop
      muted
      playsinline
      class="rounded-xl w-full max-h-[390px] object-contain"
    ></video>
  </div>
</div>

<!--
[강사 멘트]
영상에서 보시는 것처럼, Skill은 SKILL.md 지침과 참조 문서(References)를 하나의 패키지로 등록해 두고, 대화창에서 필요할 때마다 원클릭으로 호출해 일관된 표준 결과물을 뽑아내는 도구입니다.
-->

---
title: Skill과 Prompt의 차이
layout: default
class: px-14 py-7
glowSeed: 412
clicks: 2
---
<!-- slide:49-Prompt-vs-Skill -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Skill과 Prompt의 차이
</h2>

<PromptVsSkillComparison :stage="$clicks" />

<!--
[강사 멘트]
[click 1] 프롬프트가 "이번에 이 일 해줘"라면, 스킬은 "앞으로 이 업무는 항상 이 표준으로 해줘"라는 조직의 자산입니다.
[click 2] 개인의 프롬프트 작성 실력에 의존하지 않고, 누가 실행해도 똑같은 퀄리티를 보장합니다.
-->

---
title: 나만의 Skill 설계: 4대 핵심 구성요소
layout: default
class: px-14 py-7
glowSeed: 413
clicks: 2
---
<!-- slide:50-Skill-Engineering-Suite -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  나만의 Skill 설계: 4대 핵심 구성요소
</h2>

<SkillEngineeringSuite :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>

<!--
[강사 멘트]
스킬은 목적, 입력, 절차, 루브릭의 4요소로 설계합니다.
[click 1] 처음 만든 스킬이 마음에 안 든다면 지침에 4단 고정 서식과 분량 제약을 추가하여
[click 2] 팀원 누구나 원클릭으로 실행할 수 있는 완벽한 사내 영구 자산으로 다듬어갑니다.
-->

---
title: ChatGPT Images 2.0: 생각하는 비주얼 엔진의 등장
layout: default
class: px-14 py-6
glowSeed: 414
clicks: 2
---
<!-- slide:51-Gpt-Image-2-Intro -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  ChatGPT Images 2.0: 생각하는 비주얼 엔진의 등장
</h2>

<GptImage2Intro :stage="$clicks" />
<div v-click="1" class="hidden"></div>
<div v-click="2" class="hidden"></div>

<!--
[강사 멘트]
2026년 4월 공개된 ChatGPT Images 2.0(gpt-image-2)은 프롬프트를 깊이 생각(Thinking)하고, 스스로 자가 수정(Self-Correction)을 거쳐 완벽한 한글 텍스트와 2K 초고해상도를 구현하는 차세대 비주얼 모델입니다.
-->

---
title: 글로벌 비주얼 벤치마크 압도적 1위
layout: default
class: px-14 py-6
glowSeed: 415
clicks: 1
---
<!-- slide:52-Gpt-Image-2-Benchmark -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  글로벌 비주얼 벤치마크 압도적 1위
</h2>

<GptImage2Benchmark :stage="$clicks" />
<div v-click="1" class="hidden"></div>

<!--
[강사 멘트]
보시는 것처럼 ChatGPT Images 2.0은 1,512점으로 2위 경쟁 모델 대비 240점 이상의 압도적인 격차로 1위를 기록했습니다.
단순 확산 모델을 넘어선 추론형 비주얼 엔진으로 실무 투입 수준의 완성도를 자랑합니다.
-->

---
title: 실전 한글 비주얼 렌더링 & 사내 안내문 제작
layout: default
class: px-14 py-6
glowSeed: 416
clicks: 1
---
<!-- slide:53-Gpt-Image-2-Showcase -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실전 한글 비주얼 렌더링 & 사내 안내문 제작
</h2>

<GptImage2Showcase :stage="$clicks" />
<div v-click="1" class="hidden"></div>

<!--
[강사 멘트]
실제 생성 사례에서 보시듯, 간판이나 포스터 속 한글 문구와 가격표가 깨짐 없이 완벽하게 인쇄됩니다.
용도 정의, 인쇄할 한글 텍스트, 2K 규격을 지정하면 사내 공지 및 사이니지용 포스터를 단 한 번에 완성할 수 있습니다.
-->

---
title: 역방향 디자인: 대화창에서 @Canva 호출하기
layout: default
class: px-14 py-6
glowSeed: 417
clicks: 1
---
<!-- slide:54-Canva-Reverse-Workflow -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  역방향 디자인: 대화창에서 @Canva 호출하기
</h2>

<CanvaReverseWorkflow :stage="$clicks" />
<div v-click="1" class="hidden"></div>

<!--
[강사 멘트]
디자인을 하러 캔바에 들어가서 수만 개 템플릿을 찾는 것은 과거의 방식입니다.
ChatGPT 대화창에서 기획과 카피를 뽑으며 @Canva를 호출하면 맞춤형 템플릿이 즉시 생성되어 1분 만에 완성됩니다.
-->

---
title: 정적 포스터에서 15초 홍보 숏폼 영상으로 확장
layout: default
class: px-14 py-6
glowSeed: 418
clicks: 1
---
<!-- slide:55-Image-To-Video-Evolution -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  정적 포스터에서 15초 홍보 숏폼 영상으로 확장
</h2>

<ImageToVideoEvolution :stage="$clicks" />
<div v-click="1" class="hidden"></div>

<!--
[강사 멘트]
ChatGPT Images 2.0으로 생성한 정적 포스터를 캔바에서 모션 자막과 음악을 더해 15초 세로형 숏폼 영상으로 확장합니다.
단 하나의 기획으로 사내 안내문과 숏폼 홍보 영상을 동시에 완성하는 1 Source Multi-Use 파이프라인입니다.
-->

---
title: Final Mission: 올인원 실무 프로젝트 완결
layout: default
class: px-14 py-6
glowSeed: 419
clicks: 1
---
<!-- slide:56-Final-Mission-Dashboard -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Final Mission: 올인원 실무 프로젝트 완결
</h2>

<FinalMissionDashboard :stage="$clicks" />
<div v-click="1" class="hidden"></div>

<!--
[실습 안내]
전체 과정을 아우르는 Final Mission을 진행합니다.
데이터 분석부터 시각화, 실무 보고서, Images 2.0 포스터, 그리고 캔바 15초 홍보 영상까지 하나의 업무 패키지로 완성해 보시기 바랍니다.
-->

---
title: 전체 교육 마스터 Takeaway & 핵심 공식
layout: center
class: text-center px-12
glowSeed: 999
---
<!-- slide:57-Master-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 border border-white/15 text-xs font-mono text-white/70 mb-4">
    <span>전체 커리큘럼 핵심 공식</span>
  </div>
  <div class="p-6 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md shadow-2xl max-w-4xl mb-5">
    <div class="text-2xl font-black text-white tracking-tight leading-relaxed">
      Chat ➔ <span class="text-blue-400">Work</span> | 질문자 ➔ <span class="text-emerald-400">업무 위임자</span>
    </div>
    <div class="text-sm font-mono text-white/60 mt-2">
      생성(Generate) ➔ 실행(Execute) ➔ 검토(Review) ➔ 개선(Refine)
    </div>
  </div>
  <div class="grid grid-cols-3 gap-4 max-w-3xl text-left text-xs mb-5">
    <div class="p-4 rounded-xl bg-black/40 border border-white/10">
      <strong class="text-white">1·2차시 기초</strong>
      <p class="text-[11px] text-white/60 m-0 mt-1">지시 체계(RCTF) + 근거 자료(S-A-F)로 정확한 답변을 얻는 법</p>
    </div>
    <div class="p-4 rounded-xl bg-black/40 border border-white/10">
      <strong class="text-white">3·4차시 심화</strong>
      <p class="text-[11px] text-white/60 m-0 mt-1">파일 연동 + 도구 실행으로 실제 결과물과 파일을 완성하는 법</p>
    </div>
    <div class="p-4 rounded-xl bg-black/40 border border-blue-500/30">
      <strong class="text-blue-300">실무 지속 자산화</strong>
      <p class="text-[11px] text-white/70 m-0 mt-1">반복 업무를 Skill로 만들어 팀과 조직의 영구 표준으로 정착</p>
    </div>
  </div>
  <div class="text-xs text-white/40 font-mono">
    MC에너지 2026 생성형 AI 실무능력 향상 과정 수료를 축하합니다.
  </div>
</div>

<!--
[교육 마무리]
수고 많으셨습니다.
생성형 AI는 단순한 질문 상자가 아니라, 여러분의 업무를 대신 수행하고 표준화해 주는 가장 강력한 실무 파트너입니다.
현업에서 AI를 통해 더 가치 있는 일에 집중하시기 바랍니다. 감사합니다.
-->
