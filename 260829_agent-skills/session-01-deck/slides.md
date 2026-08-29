---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: "AI 에이전트 업무 매뉴얼: SKILL 기초와 핵심 아키텍처"
exportFilename: session-01-skill-foundations
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glow: full
glowOpacity: 0.5
glowSeed: 101
routerMode: hash
defaults:
  layout: default
  transition: fade-out
---
<!-- slide:S01 -->

<div class="flex items-center justify-center flex-col text-center">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-xs font-mono font-bold tracking-wider uppercase mb-4">
    <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
    Session 01 · 50 Minutes Hands-on
  </div>
  <h1 class="m-0 text-white text-4xl lg:text-5xl font-black leading-tight tracking-tight font-cover">
    AI 에이전트 업무 매뉴얼<br/>
    <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-emerald-400">SKILL 기초와 핵심 아키텍처</span>
  </h1>
  <p class="mt-4 text-slate-100 text-lg font-medium max-w-2xl leading-relaxed">
    반복 프롬프트 복붙에서 벗어나, 점진적 로딩(Progressive Disclosure) 기반의<br/>
    표준 업무 절차서(SOP)를 설계하고 실습합니다.
  </p>
  <div class="flex items-center justify-center flex-wrap gap-4 mt-6 text-xs text-slate-300 font-mono font-medium">
    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-white">
      <img src="/icons/claude-color.svg" class="w-4 h-4 inline-block" alt="Claude" />
      Anthropic Open Standard
    </span>
    <span class="text-white/20">|</span>
    <div class="inline-flex items-center gap-2.5">
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-black/60 border border-white/10 text-white">
        <img src="/icons/claudecode-color.svg" class="w-4 h-4 inline-block" alt="Claude Code" />
        Claude Code
      </span>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-black/60 border border-white/10 text-white">
        <img src="/icons/antigravity-color.svg" class="w-4 h-4 inline-block" alt="Antigravity" />
        Antigravity
      </span>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-black/60 border border-white/10 text-white">
        <img src="/icons/cursor.svg" class="w-4 h-4 inline-block filter invert" alt="Cursor" />
        Cursor
      </span>
    </div>
  </div>
</div>

<!--
[발표자]
안녕하세요 여러분! 오늘 1세션에서는 AI 에이전트에게 매번 장문의 프롬프트를 복사-붙여넣기하던 방식에서 벗어나, 점진적 로딩(Progressive Disclosure) 기반의 표준 업무 매뉴얼 SKILL을 설계하고 실습해보겠습니다.
-->

---
transition: fade-out
title: 문제 제기: 프롬프트 반복의 한계
glowSeed: 105
clicks: 3
---
<!-- slide:S02 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Tension & Friction</div>
  <h2 class="text-2xl font-black text-white mt-1">왜 우리는 매번 같은 프롬프트를 복사하고 있는가?</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">단순 텍스트 프롬프트 기반 워크플로우가 프로덕션에서 겪는 3가지 구조적 한계</p>
</div>

<div class="grid grid-cols-3 gap-4">
<v-clicks>
  <div class="glass-card p-5 border-rose-500/40">
    <div class="w-10 h-10 rounded-lg bg-rose-950/90 border border-rose-400/70 flex items-center justify-center text-rose-400 mb-3">
      <span class="i-carbon:warning-alt-filled text-xl"></span>
    </div>
    <div class="text-xs font-mono text-rose-300 font-bold uppercase mb-1">01. Fragility</div>
    <h3 class="text-base font-bold text-white m-0">휘발성과 일관성 결여</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      매번 미세하게 달라지는 입력 문구로 인해 에이전트의 출력 품질과 포맷에 지속적인 편차가 발생합니다.
    </p>
  </div>
  <div class="glass-card p-5 border-amber-500/40">
    <div class="w-10 h-10 rounded-lg bg-amber-950/90 border border-amber-400/70 flex items-center justify-center text-amber-400 mb-3">
      <span class="i-carbon:data-blob text-xl"></span>
    </div>
    <div class="text-xs font-mono text-amber-300 font-bold uppercase mb-1">02. Context Bloat</div>
    <h3 class="text-base font-bold text-white m-0">컨텍스트 창 낭비</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      당장 쓰이지 않는 방대한 가이드라인을 매 대화마다 시스템 프롬프트에 주입하여 토큰과 비용이 낭비됩니다.
    </p>
  </div>
  <div class="glass-card p-5 border-sky-500/40">
    <div class="w-10 h-10 rounded-lg bg-sky-950/90 border border-sky-400/70 flex items-center justify-center text-sky-400 mb-3">
      <span class="i-carbon:locked text-xl"></span>
    </div>
    <div class="text-xs font-mono text-sky-300 font-bold uppercase mb-1">03. Siloed Knowledge</div>
    <h3 class="text-base font-bold text-white m-0">팀 공유 및 버전 관리 불가</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      프롬프트가 개인 메모장이나 슬랙에 파편화되어 있어, 조직 차원의 Git 버전 관리나 표준화가 불가능합니다.
    </p>
  </div>
</v-clicks>
</div>

<!--
[발표자]
우리가 매일 겪는 프롬프트의 한계는 명확합니다.
[click] 첫째, 매번 복붙하는 프롬프트는 휴먼 에러를 유발하고 일관성을 해칩니다.
[click] 둘째, 쓰이지도 않는 수천 토큰의 지침을 매번 주입하면서 비용이 폭증하고 컨텍스트가 오염됩니다.
[click] 셋째, 지식이 개인 메모장에 갇혀 팀 단위 버전 관리가 불가능합니다.
-->

---
transition: fade-out
title: 개념 정의: AI용 표준 업무 절차서 (SOP)
glowSeed: 120
clicks: 2
---
<!-- slide:S03 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Mental Model</div>
  <h2 class="text-2xl font-black text-white mt-1">SKILL: AI 에이전트를 위한 표준 업무 절차서 (SOP)</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">일회성 지시어에서 구조화된 재사용 지침 패키지로의 패러다임 전환</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/30 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-rose-950/90 border border-rose-400/70 text-rose-300 text-xs font-bold font-mono mb-2">
        <span class="i-carbon:close-outline"></span> 전통적 프롬프트 방식
      </div>
      <h3 class="text-base font-bold text-white m-0">일회성 텍스트 복사-붙여넣기</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-2"><span class="text-rose-400 font-bold font-mono shrink-0">✕</span><span class="leading-relaxed">매 대화마다 장문의 지시어를 복사하여 전송</span></li>
        <li class="flex items-start gap-2"><span class="text-rose-400 font-bold font-mono shrink-0">✕</span><span class="leading-relaxed">세션 시작 시 수천~수만 토큰을 항시 점유</span></li>
        <li class="flex items-start gap-2"><span class="text-rose-400 font-bold font-mono shrink-0">✕</span><span class="leading-relaxed">사용자가 직접 지시어를 기억하고 수동 입력</span></li>
      </ul>
    </div>
    <div class="mt-3 p-2 rounded-lg bg-black/70 border border-rose-500/30 text-slate-300 text-xs font-mono font-medium">
      결과: 높은 토큰 비용 + 일관성 저하 + 수동 개입
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-bold font-mono mb-2">
        <span class="i-carbon:checkmark-outline"></span> 표준 SKILL 패키지
      </div>
      <h3 class="text-base font-bold text-white m-0">규격화된 SOP 폴더 패키지</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold font-mono shrink-0">✓</span><span class="leading-relaxed">SKILL.md + 보조 스크립트 기반의 모듈화</span></li>
        <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold font-mono shrink-0">✓</span><span class="leading-relaxed">점진적 로딩으로 평소 100토큰만 점유</span></li>
        <li class="flex items-start gap-2"><span class="text-emerald-400 font-bold font-mono shrink-0">✓</span><span class="leading-relaxed">에이전트가 문맥을 파악하여 자동으로 최적 스킬 호출</span></li>
      </ul>
    </div>
    <div class="mt-3 p-2 rounded-lg bg-black/70 border border-emerald-500/30 text-emerald-300 text-xs font-mono font-medium">
      결과: 토큰 최적화 + 표준화된 고품질 출력 + 자동화
    </div>
  </div>
</v-clicks>
</div>

<div class="mt-3 glass-card px-4 py-2 border-cyan-500/30 flex items-center justify-between">
  <span class="text-xs text-slate-200 font-medium">
    <strong class="text-cyan-300 font-mono font-bold">Anthropic 공식 정의:</strong> "Claude가 특정 작업에서 성능을 향상시키기 위해 동적으로 로드하는 지침, 스크립트, 리소스가 담긴 폴더"
  </span>
</div>

<!--
[발표자]
스킬은 단순한 프롬프트가 아닙니다. 조직의 SOP(표준업무절차서)와 같습니다.
[click] 기존에는 매번 지침을 복사해서 붙여넣느라 토큰을 낭비했다면,
[click] 스킬은 폴더 단위로 규격화되어 에이전트가 필요할 때 스스로 꺼내어 읽는 업무 매뉴얼입니다.
-->

---
transition: fade-out
title: 핵심 아키텍처: 점진적 로딩 (Progressive Disclosure)
glowSeed: 233
clicks: 2
---
<!-- slide:S04 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Core Mechanism</div>
  <h2 class="text-2xl font-black text-white mt-0.5">점진적 로딩 (Progressive Disclosure)의 마법</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">수백 개의 스킬을 상시 탑재해도 컨텍스트가 넘치지 않는 2단계 로딩 구조</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
  <!-- 1단계: 세션 초기화 -->
  <div class="glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-[11px] font-mono font-bold mb-2">
        STAGE 1 : 세션 초기화 (Preload)
      </div>
      <div class="mt-1 text-center py-1">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-black/70 border border-white/15 text-cyan-300 font-mono text-xs mb-2">
          <span class="i-carbon:tag-group text-sm"></span> YAML Frontmatter (~100 Tokens)
        </div>
        <div class="text-white text-sm font-bold mt-0.5">이름(name) + 설명(description)만 로드</div>
        <p class="text-slate-200 font-medium text-xs mt-1.5 leading-relaxed m-0">
          100개 스킬을 등록해도 단 <strong>10k 토큰</strong>만 소비.<br/>
          에이전트는 어떤 스킬이 존재하는지만 인지하고 대기합니다.
        </p>
      </div>
    </div>
  </div>
  <!-- 2단계: 온디맨드 로딩 -->
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between" v-click="1">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-[11px] font-mono font-bold mb-2">
        STAGE 2 : 온디맨드 실행 (Just-In-Time)
      </div>
      <div class="mt-1 text-center py-1">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-lg bg-black/70 border border-emerald-500/30 text-emerald-300 font-mono text-xs mb-2">
          <span class="i-carbon:document-view text-sm"></span> SKILL.md 본문 + scripts/ + references/
        </div>
        <div class="text-white text-sm font-bold mt-0.5">관련 작업 요청 시에만 전체 지침 로드</div>
        <p class="text-slate-200 font-medium text-xs mt-1.5 leading-relaxed m-0">
          사용자의 질문/명령 키워드가 매칭되는 순간,<br/>
          해당 스킬의 세부 절차와 스크립트를 즉시 활성화합니다.
        </p>
      </div>
    </div>
  </div>
</div>

<div class="mt-3 glass-card px-4 py-2 border-white/15" v-click="2">
  <div class="flex items-center justify-between text-xs font-mono">
    <span class="text-slate-200 font-medium">💡 <strong class="text-white">토큰 절감 효과:</strong> 50개 스킬 상주 기준</span>
    <span class="text-rose-400 font-medium line-through">전체 로드 시: ~250,000 토큰</span>
    <span class="text-emerald-300 font-bold">점진적 로드 시: ~5,000 토큰 (98% 절감)</span>
  </div>
</div>

<!--
[발표자]
점진적 로딩이 왜 혁신적인지 살펴보겠습니다.
[click] 세션이 시작될 때는 스킬의 이름과 설명(약 100토큰)만 가볍게 올려둡니다.
[click] 그러다 사용자가 관련 작업을 요청할 때만 전체 지침과 스크립트를 불러옵니다. 이로써 98% 이상의 토큰을 아끼면서 수백 개의 스킬을 동시 운용할 수 있습니다.
-->

---
transition: fade-out
title: 글로벌 오픈 표준과 생태계
glowSeed: 155
clicks: 2
---
<!-- slide:S05 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Open Standard & Ecosystem</div>
  <h2 class="text-2xl font-black text-white mt-1">글로벌 오픈 에이전트 스킬 생태계</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">특정 벤더 종속 없이 모든 AI 도구와 호환되는 범용 아키텍처</p>
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="glass-card p-5 border-cyan-500/40">
    <div class="w-8 h-8 rounded bg-cyan-950/90 border border-cyan-400/70 flex items-center justify-center text-cyan-300 font-mono font-bold text-xs mb-3">
      2025
    </div>
    <h3 class="text-base font-bold text-white m-0">오픈 표준 제정</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      2025년 10월 Anthropic 도입 후 12월 <strong>Agent Skills Open Standard</strong>로 발표되어 크로스 플랫폼 표준으로 정립.
    </p>
  </div>
  <div class="glass-card p-5 border-sky-500/40" v-click="1">
    <div class="w-8 h-8 rounded bg-sky-950/90 border border-sky-400/70 flex items-center justify-center text-sky-300 font-mono font-bold text-xs mb-3">
      IDE
    </div>
    <h3 class="text-base font-bold text-white m-0">다양한 플랫폼 지원</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      Claude Code, Antigravity, OpenAI Codex, Cursor 등 주요 AI 코딩 에이전트에서 동일한 SKILL.md 호환 지원.
    </p>
  </div>
  <div class="glass-card p-5 border-purple-500/40" v-click="2">
    <div class="w-8 h-8 rounded bg-purple-950/90 border border-purple-400/70 flex items-center justify-center text-purple-300 font-mono font-bold text-xs mb-3">
      HUB
    </div>
    <h3 class="text-base font-bold text-white m-0">파트너 & 엔터프라이즈</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      Notion, Figma, Atlassian 등 글로벌 SaaS 기업들이 공식 스킬을 제공하며 업무 워크플로우를 가속화.
    </p>
  </div>
</div>

<div class="mt-4 p-3 rounded-xl bg-black/60 border border-white/15 flex items-center justify-around flex-wrap gap-3">
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/claude-color.svg" class="w-4.5 h-4.5 inline-block" /> Anthropic
  </span>
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/openai.svg" class="w-4.5 h-4.5 inline-block filter invert" /> OpenAI
  </span>
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/google-color.svg" class="w-4.5 h-4.5 inline-block" /> Google
  </span>
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/microsoft-color.svg" class="w-4.5 h-4.5 inline-block" /> Microsoft
  </span>
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/notion.svg" class="w-4.5 h-4.5 inline-block filter invert" /> Notion
  </span>
  <span class="flex items-center gap-2 text-xs text-white font-mono font-medium">
    <img src="/icons/figma-color.svg" class="w-4.5 h-4.5 inline-block" /> Figma
  </span>
</div>

<!--
[발표자]
스킬은 이제 특정 툴에 갇힌 기능이 아닙니다.
[click] 2025년 말 오픈 표준으로 발표되어 Claude Code, Cursor, Google Antigravity 등 다양한 도구에서 호환됩니다.
[click] Notion, Figma 같은 주요 SaaS 기업들도 공식 스킬을 배포하고 있습니다.
-->

---
transition: fade-out
title: SKILL.md 구조 해부
glowSeed: 180
clicks: 2
---
<!-- slide:S06 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Package Anatomy</div>
  <h2 class="text-2xl font-black text-white mt-1">SKILL.md의 구조: YAML 헤더와 본문 절차</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">에이전트가 읽고 실행하는 표준 파일 및 디렉토리 계층</p>
</div>

<div class="grid grid-cols-12 gap-4 items-stretch">
  <div class="col-span-7 glass-card p-4 border-cyan-500/30 flex flex-col justify-between">
    <div>
      <div class="text-[11px] font-mono text-cyan-300 font-bold mb-1.5 flex items-center justify-between">
        <span>SKILL.md 파일 구조 예시</span>
        <span class="text-slate-300">YAML + Markdown</span>
      </div>
      <div class="p-3 rounded-lg bg-black/80 border border-white/10 text-[11.5px] font-mono text-slate-100 leading-relaxed overflow-hidden">
        <div class="text-amber-400 font-bold">---</div>
        <div class="text-cyan-300 font-bold">name: <span class="text-white font-bold">processing-pdfs</span></div>
        <div class="text-cyan-300 font-bold">description: <span class="text-slate-200">PDF에서 텍스트와 표를 추출합니다.</span></div>
        <div class="text-amber-400 font-bold">---</div>
        <div class="text-slate-300 font-bold mt-2"># PDF 처리 절차 가이드</div>
        <div class="text-slate-200 font-medium mt-1">## 1. 입력 검증 및 요구분석</div>
        <div class="text-slate-200 font-medium">## 2. 단계별 처리 규칙 (SOP)</div>
      </div>
    </div>
    <div class="mt-2.5 px-2.5 py-1.5 rounded bg-cyan-950/50 border border-cyan-500/40 text-[11px] text-cyan-200 font-medium leading-tight">
      <strong class="text-cyan-300 font-mono font-bold">* SOP (Standard Operating Procedure):</strong> 항상 동일한 고품질 결과를 내도록 작업 순서, 제약 조건, 출력 양식을 표준화한 '실무 업무 매뉴얼/절차서'
    </div>
  </div>
  <div class="col-span-5 flex flex-col gap-3">
    <div class="glass-card p-3.5 border-amber-500/30 flex-1" v-click="1">
      <div class="text-xs font-mono text-amber-300 font-bold uppercase mb-1">1. YAML Frontmatter</div>
      <p class="text-xs text-slate-100 font-medium leading-relaxed m-0">
        • <strong>name</strong>: 스킬 고유 식별자<br/>
        • <strong>description</strong>: 에이전트 자동 트리거 핵심 검색 인덱스 (100토큰)
      </p>
    </div>
    <div class="glass-card p-3.5 border-emerald-500/30 flex-1" v-click="2">
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase mb-1">2. 폴더 구성 (선택 사항)</div>
      <div class="text-xs text-slate-100 font-mono text-[11px] leading-relaxed mt-1">
        📂 my-skill/<br/>
        &nbsp;&nbsp;├── 📄 <strong>SKILL.md</strong> (필수 지침)<br/>
        &nbsp;&nbsp;├── 📁 <strong>scripts/</strong> (실행 스크립트)<br/>
        &nbsp;&nbsp;└── 📁 <strong>references/</strong> (참조 데이터)
      </div>
    </div>
  </div>
</div>

<!--
[발표자]
SKILL.md의 구조를 보겠습니다.
[click] 상단의 YAML Frontmatter는 에이전트가 언제 이 스킬을 쓸지 결정하는 색인입니다.
[click] 하단 마크다운 본문에는 구체적인 작업 절차와 필요 시 실행할 스크립트, 참조 문서를 배치합니다.
-->

---
transition: fade-out
title: 좋은 스킬 설계 원칙: Name & Description
glowSeed: 210
clicks: 3
---
<!-- slide:S07 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Design Rules</div>
  <h2 class="text-2xl font-black text-white mt-1">트리거율을 결정짓는 Name과 Description 작성법</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">에이전트가 놓치지 않고 정확하게 스킬을 호출하게 만드는 공식</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
  <div class="glass-card p-4 border-cyan-500/30" v-click="1">
    <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-xs font-mono font-bold mb-2">
      Rule 1 · Name 명명법
    </div>
    <h3 class="text-base font-bold text-white m-0">동작 형태의 명명 (-ing 형태 권장)</h3>
    <ul class="mt-2 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
      <li>• 64자 이하, 소문자/숫자/하이픈(<code>-</code>)만 사용</li>
      <li>• <strong>좋은 예:</strong> <code>processing-pdfs</code>, <code>reviewing-code</code></li>
      <li>• <strong>나쁜 예:</strong> <code>PDFTool</code>, <code>my_script_v2</code></li>
    </ul>
  </div>
  <div class="glass-card p-4 border-emerald-500/30" v-click="2">
    <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-mono font-bold mb-2">
      Rule 2 · Description 공식
    </div>
    <h3 class="text-base font-bold text-white m-0">"무엇을 하는지" + "언제 쓰는지"</h3>
    <ul class="mt-2 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
      <li>• 3인칭으로 작성 (주어/불필요한 수식어 제거)</li>
      <li>• 사용자가 입력할 가능성이 높은 핵심 키워드 포함</li>
      <li>• 필요 시 부정 조건 명시 ("~작업에는 쓰지 마세요")</li>
    </ul>
  </div>
</div>

<div class="mt-4 glass-card p-3.5 border-white/15" v-click="3">
  <div class="grid grid-cols-2 gap-4 text-xs">
    <div class="p-2.5 rounded-lg bg-rose-950/50 border border-rose-500/40">
      <span class="text-rose-300 font-bold font-mono">❌ 나쁜 Description:</span>
      <p class="text-slate-200 font-medium mt-1 m-0">"이것은 PDF 관련 작업을 돕는 도구입니다. 유용하게 쓰세요."</p>
    </div>
    <div class="p-2.5 rounded-lg bg-emerald-950/50 border border-emerald-500/40">
      <span class="text-emerald-300 font-bold font-mono">✅ 좋은 Description:</span>
      <p class="text-slate-100 font-medium mt-1 m-0">"PDF 파일에서 텍스트와 표를 추출하고 양식을 작성합니다. PDF 분석, 추출 요청 시 사용하세요."</p>
    </div>
  </div>
</div>

<!--
[발표자]
스킬이 제대로 동작하려면 두 가지가 핵심입니다.
[click] 첫째, 이름은 동작 중심 명명(processing-pdfs처럼 -ing 형태)으로 직관적으로 짓습니다.
[click] 둘째, 설명에는 무엇을 하는지와 언제 사용할지를 명시해야 에이전트가 정확히 트리거합니다.
[click] 하단의 좋은 예시처럼 구체적인 키워드를 반드시 넣어주어야 합니다.
-->

---
transition: fade-out
title: 작업 자유도 (Freedom Level) 제어
glowSeed: 250
clicks: 2
---
<!-- slide:S08 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Prompt Engineering in SKILL</div>
  <h2 class="text-2xl font-black text-white mt-1">작업 자유도(Freedom Level)에 따른 지침 설계</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">업무 특성에 맞춰 에이전트에게 부여할 자율성의 범위를 조절하는 기술</p>
</div>

<div class="grid grid-cols-2 gap-5 items-stretch">
  <div class="glass-card p-5 border-purple-500/40 flex flex-col justify-between" v-click="1">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-purple-950/90 border border-purple-400/70 text-purple-300 text-xs font-mono font-bold mb-2">
        High Freedom · 높은 자유도
      </div>
      <h3 class="text-lg font-bold text-white m-0">창의적 분석 및 문제 해결</h3>
      <p class="text-xs text-purple-200 font-mono font-bold mt-1">코드 리뷰, 기획서 작성, 전략 수립</p>
      <div class="mt-3 p-3 rounded-lg bg-black/70 border border-white/15 text-xs text-slate-100 leading-relaxed">
        <strong class="text-purple-300">작성 방식:</strong> 엄격한 순서 대신 <strong>핵심 평가 기준, 원칙, 휴리스틱(*)</strong>을 제시.<br/>
        <em class="text-slate-200">"보안 취약점과 성능 병목을 우선 검토하고 개선안을 제안한다."</em>
      </div>
      <div class="mt-2.5 px-2.5 py-1.5 rounded bg-purple-950/40 border border-purple-500/30 text-[11px] text-purple-200 font-medium leading-tight">
        <strong>* 휴리스틱(Heuristics):</strong> 완벽한 정답 공식 대신, 경험적으로 가장 합리적인 해결책을 찾도록 돕는 실용적 판단 규칙
      </div>
    </div>
    <div class="mt-2.5 text-[11px] text-slate-300 font-mono font-medium">적용: 전략적 판단이 필요한 고차원 업무</div>
  </div>
  <div class="glass-card p-5 border-cyan-500/40 flex flex-col justify-between" v-click="2">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-xs font-mono font-bold mb-2">
        Low Freedom · 낮은 자유도
      </div>
      <h3 class="text-lg font-bold text-white m-0">엄격한 절차와 결정론적 실행</h3>
      <p class="text-xs text-cyan-200 font-mono font-bold mt-1">DB 마이그레이션, 정형 데이터 변환</p>
      <div class="mt-3 p-3 rounded-lg bg-black/70 border border-white/15 text-xs text-slate-100 leading-relaxed">
        <strong class="text-cyan-300">작성 방식:</strong> 단계별 실행 순서, <strong>CLI 명령어, 고정 입출력 포맷</strong>을 강제.<br/>
        <em class="text-slate-200">"1단계: 스키마 검증 실행 ➔ 2단계: 백업 생성 ➔ 3단계: 쿼리 적용"</em>
      </div>
      <div class="mt-2.5 px-2.5 py-1.5 rounded bg-cyan-950/40 border border-cyan-500/30 text-[11px] text-cyan-200 font-medium leading-tight">
        <strong>* 결정론적 실행:</strong> 동일한 입력에 대해 언제나 오차 없이 정확히 같은 결과를 산출하는 방식
      </div>
    </div>
    <div class="mt-2.5 text-[11px] text-slate-300 font-mono font-medium">적용: 실수가 용납되지 않는 미션 크리티컬 업무</div>
  </div>
</div>

<!--
[발표자]
스킬을 작성할 때 모든 작업에 같은 방식을 쓰면 안 됩니다.
[click] 코드 리뷰나 기획처럼 창의성이 필요할 때는 높은 자유도로 원칙과 휴리스틱(경험적 가이드)을 주고,
[click] DB 마이그레이션처럼 정밀해야 할 때는 낮은 자유도로 1단계부터 3단계까지 명령어와 포맷을 강제해야 안전합니다.
-->

---
transition: fade-out
title: 실습 P01 안내
glowSeed: 300
clicks: 0
---
<!-- slide:S09 -->

<div class="mb-4">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-mono font-bold uppercase mb-2">
    <span class="i-carbon:code text-sm"></span> Hands-on Practice P01 · 15 Minutes
  </div>
  <h2 class="text-3xl font-black text-white mt-1">나만의 첫 SKILL.md 직접 작성하기</h2>
  <p class="text-sm text-slate-200 font-medium mt-1">자신의 반복 업무를 하나 선정하여 표준 규격의 스킬 파일로 완성합니다.</p>
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-1">STEP 1 (3분)</div>
      <h3 class="text-base font-bold text-white m-0">업무 선정 & 분석</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="text-cyan-400 shrink-0">•</span><span class="leading-relaxed">영문 이메일 정중화 변환</span></li>
        <li class="flex items-start gap-1.5"><span class="text-cyan-400 shrink-0">•</span><span class="leading-relaxed">회의록 핵심 요약 & Action 도출</span></li>
        <li class="flex items-start gap-1.5"><span class="text-cyan-400 shrink-0">•</span><span class="leading-relaxed">Git 커밋 메시지 규칙 검증기</span></li>
      </ul>
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase mb-1">STEP 2 (5분)</div>
      <h3 class="text-base font-bold text-white m-0">YAML 헤더 정의</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="text-emerald-400 shrink-0">•</span><span class="leading-relaxed">동작 형태 명명(<code>-ing</code>) <code>name</code> 설정</span></li>
        <li class="flex items-start gap-1.5"><span class="text-emerald-400 shrink-0">•</span><span class="leading-relaxed">목적과 트리거 시점이 포함된 3인칭 <code>description</code> 작성</span></li>
      </ul>
    </div>
  </div>
  <div class="glass-card p-4 border-purple-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-purple-300 font-bold uppercase mb-1">STEP 3 (7분)</div>
      <h3 class="text-base font-bold text-white m-0">단계별 SOP 작성</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="text-purple-400 shrink-0">•</span><span class="leading-relaxed">작업 단계(Step 1~3) 순차 기술</span></li>
        <li class="flex items-start gap-1.5"><span class="text-purple-400 shrink-0">•</span><span class="leading-relaxed">Few-shot 입출력 템플릿 제공</span></li>
        <li class="flex items-start gap-1.5"><span class="text-purple-400 shrink-0">•</span><span class="leading-relaxed">예외 상황 대응 규칙 명시</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="mt-3.5 glass-card p-3 border-sky-500/30 bg-black/60 flex items-center justify-between">
  <div class="flex items-center gap-3">
    <div class="px-3 py-1.5 rounded-lg bg-sky-950/90 border border-sky-400/60 flex items-center gap-1.5 text-sky-300 font-mono font-bold text-xs shrink-0">
      <span class="i-carbon:cube text-sm text-sky-400"></span> Skill Creator
    </div>
    <div class="text-xs text-slate-200 leading-relaxed">
      <strong class="text-white font-bold">GPTwork 활용 꿀팁:</strong> 프롬프트 창에서 <code class="text-sky-300 bg-sky-950/70 px-1.5 py-0.5 rounded border border-sky-500/30 font-mono font-bold">$skill creator</code>를 호출하고 '자동화할 업무'를 대화하듯 설명하면, 표준 규격의 <code class="text-amber-300 font-mono">SKILL.md</code> 초안을 AI가 즉시 자동 생성해 줍니다.
    </div>
  </div>
</div>

<!--
[발표자]
이제 직접 실습에 들어가겠습니다! 15분 동안 나만의 첫 SKILL.md를 작성해봅니다.
선정, 헤더 정의, 본문 작성 3단계로 진행되며, 다음 슬라이드의 템플릿을 참고하시면 됩니다.
-->

---
transition: fade-out
title: 실습 템플릿: 비즈니스 영문 이메일 변환기
glowSeed: 320
clicks: 0
---
<!-- slide:S10 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Reference Template</div>
  <h2 class="text-2xl font-black text-white mt-1">실습 참고용 템플릿: polishing-emails</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">아래 구조를 참고하여 자신만의 스킬로 커스텀 작성하세요.</p>
</div>

<div class="glass-card p-4 border-cyan-500/40">
  <div class="p-3 rounded-lg bg-black/80 border border-white/15 text-[11.5px] font-mono text-slate-100 leading-relaxed overflow-y-auto max-h-[300px]">
    <div class="text-amber-400 font-bold">---</div>
    <div class="text-cyan-300 font-bold">name: <span class="text-white font-bold">polishing-emails</span></div>
    <div class="text-cyan-300 font-bold">description: <span class="text-slate-200">거친 초안을 정중하고 명확한 글로벌 비즈니스 영문 이메일로 변환합니다. 이메일 작성 시 사용하세요.</span></div>
    <div class="text-amber-400 font-bold">---</div>
    <div class="text-slate-300 font-bold mt-2"># 비즈니스 영문 이메일 교정 가이드</div>
    <div class="text-slate-200 font-medium mt-1">## 1. 입력 확인: 수신인, 핵심 목적, 기한 파악</div>
    <div class="text-slate-200 font-medium">## 2. 변환 규칙: 정중한 인사, 불릿 구조화, 명확한 CTA</div>
    <div class="text-slate-200 font-medium">## 3. 출력 포맷: 영문 메일 본문 + 변경 사유 요약 제공</div>
  </div>
</div>

<!--
[발표자]
이메일 변환기 템플릿입니다. 이 구조를 보면서 각자의 에디터(VS Code, 메모장 등)에 작성해 보세요!
-->

---
transition: fade-out
title: 실습 진행 및 자가 점검 체크리스트
glowSeed: 340
clicks: 0
---
<!-- slide:S11 -->

<div class="mb-4 flex items-center justify-between">
  <div>
    <div class="text-xs font-mono text-emerald-400 uppercase tracking-widest font-bold">Live Coding</div>
    <h2 class="text-2xl font-black text-white mt-1">실습 진행 중: SKILL.md 작성 및 검증</h2>
  </div>
  <div class="px-4 py-2 rounded-xl bg-emerald-950/90 border border-emerald-400 text-emerald-300 font-mono font-bold text-lg">
    ⏱️ 15:00 Live
  </div>
</div>

<div class="grid grid-cols-2 gap-5 items-stretch">
  <div class="glass-card p-5 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase mb-2">📋 5대 자가 점검 체크리스트</div>
      <ul class="space-y-2 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-2">
          <span class="w-4 h-4 rounded bg-emerald-950 border border-emerald-400 flex items-center justify-center text-emerald-300 text-[10px] font-bold shrink-0 mt-0.5">✓</span>
          <span class="leading-relaxed"><code>name</code>이 소문자·하이픈의 동작 형태(예: <code>processing-pdfs</code>)인가?</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="w-4 h-4 rounded bg-emerald-950 border border-emerald-400 flex items-center justify-center text-emerald-300 text-[10px] font-bold shrink-0 mt-0.5">✓</span>
          <span class="leading-relaxed"><code>description</code>에 언제 쓰는지 트리거 키워드가 있는가?</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="w-4 h-4 rounded bg-emerald-950 border border-emerald-400 flex items-center justify-center text-emerald-300 text-[10px] font-bold shrink-0 mt-0.5">✓</span>
          <span class="leading-relaxed">단계별 실행 절차가 번호로 명확히 나뉘어 있는가?</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="w-4 h-4 rounded bg-emerald-950 border border-emerald-400 flex items-center justify-center text-emerald-300 text-[10px] font-bold shrink-0 mt-0.5">✓</span>
          <span class="leading-relaxed">입력 예시와 기대 출력 템플릿이 포함되었는가?</span>
        </li>
        <li class="flex items-start gap-2">
          <span class="w-4 h-4 rounded bg-emerald-950 border border-emerald-400 flex items-center justify-center text-emerald-300 text-[10px] font-bold shrink-0 mt-0.5">✓</span>
          <span class="leading-relaxed">API 키나 비밀번호 등 민감정보가 하드코딩되지 않았는가?</span>
        </li>
      </ul>
    </div>
    <div class="text-[11.5px] text-emerald-300 font-bold mt-3">
      💡 완성이 끝나신 분은 체크리스트를 확인하며 문구를 다듬어주세요.
    </div>
  </div>
  <div class="glass-card p-5 border-cyan-500/30 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-2">💡 작성 시 핵심 팁</div>
      <div class="space-y-2 text-xs text-slate-100 font-medium leading-relaxed">
        <p class="m-0">• <strong>배경 설명은 최소화:</strong> "이 스킬은 현대 사회에서..." 같은 긴 서론은 토큰 낭비입니다. 즉시 절차로 들어가세요.</p>
        <p class="m-0">• <strong>파일 경로는 슬래시(<code>/</code>) 사용:</strong> Windows/Mac 공통 호환을 위해 슬래시를 권장합니다.</p>
        <p class="m-0">• <strong>실패 분기 명시:</strong> "정보가 부족할 경우 추가 질문을 요청한다" 같은 Fallback을 넣어주세요.</p>
      </div>
    </div>
    <div class="p-2 rounded bg-black/70 border border-white/15 text-[11px] text-slate-300 font-mono font-medium">
      질문이 있으시면 강사에게 말씀해 주세요.
    </div>
  </div>
</div>

<!--
[발표자]
타이머를 보며 실습을 진행해 주세요. 작성이 완료되신 분들은 좌측의 5대 체크리스트를 바탕으로 검토해 주시기 바랍니다.
-->

---
transition: fade-out
title: 실습 결과 검증 및 디버깅 팁
glowSeed: 360
clicks: 2
---
<!-- slide:S12 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Evaluation & Debugging</div>
  <h2 class="text-2xl font-black text-white mt-1">스킬 검증과 트리거 디버깅 요령</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">내가 만든 스킬이 에이전트에서 완벽히 작동하는지 확인하는 3단계 테스트</p>
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="glass-card p-5 border-cyan-500/40">
    <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-1">01. 의도 트리거 테스트</div>
    <h3 class="text-base font-bold text-white m-0">자연어 호출 검증</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      스킬 이름을 직접 부르지 않고 <em>"외국 바이어한테 납기 일정 연기 메일 써줘"</em>라고 질문했을 때 자동으로 스킬이 로드되는지 확인.
    </p>
  </div>
  <div class="glass-card p-5 border-amber-500/40" v-click="1">
    <div class="text-xs font-mono text-amber-300 font-bold uppercase mb-1">02. 오작동(과호출) 방지</div>
    <h3 class="text-base font-bold text-white m-0">부정 조건 튜닝</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      일반 영작 질문인데도 스킬이 잘못 호출된다면, <code>description</code>에 <em>"단순 번역이 아닌 비즈니스 이메일 작성 시에만 사용"</em> 추가.
    </p>
  </div>
  <div class="glass-card p-5 border-purple-500/40" v-click="2">
    <div class="text-xs font-mono text-purple-300 font-bold uppercase mb-1">03. 멀티모델 일관성</div>
    <h3 class="text-base font-bold text-white m-0">Haiku / Sonnet 테스트</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      가벼운 모델(Haiku)에서도 지침을 건너뛰지 않고 포맷을 유지하는지 테스트하고, 부족하다면 Few-shot 예시 강화.
    </p>
  </div>
</div>

<div class="mt-4 p-3 rounded-xl bg-white/10 border border-white/20 text-center text-xs text-slate-100 font-bold">
  "우수한 스킬은 사용자가 의식하지 않아도 적재적소에 자동으로 실행되어 결과를 만듭니다."
</div>

<!--
[발표자]
스킬을 다 만드셨다면 3가지 방법으로 검증합니다.
[click] 첫째, 자연스럽게 질문했을 때 에이전트가 알아서 스킬을 부르는지 확인합니다.
[click] 둘째, 엉뚱한 질문에 불필요하게 켜지지 않도록 설명의 키워드를 조정합니다.
[click] 셋째, 다양한 모델에서 일관된 포맷을 내는지 확인합니다.
-->

---
transition: fade-out
title: Session 1 핵심 요약
glowSeed: 380
clicks: 3
---
<!-- slide:S13 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Key Takeaways</div>
  <h2 class="text-2xl font-black text-white mt-1">Session 1 핵심 요약</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">오늘 1세션에서 반드시 기억해야 할 3가지 핵심 배움</p>
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="glass-card p-5 border-emerald-500/40" v-click="1">
    <div class="w-8 h-8 rounded bg-emerald-950/90 border border-emerald-400/70 flex items-center justify-center text-emerald-300 font-bold font-mono text-sm mb-3">
      01
    </div>
    <h3 class="text-base font-bold text-white m-0">AI의 업무 표준 절차서</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      SKILL은 일회성 프롬프트 복붙을 조직 차원의 구조화된 SOP 패키지로 전환하는 표준 규격입니다.
    </p>
  </div>
  <div class="glass-card p-5 border-cyan-500/40" v-click="2">
    <div class="w-8 h-8 rounded bg-cyan-950/90 border border-cyan-400/70 flex items-center justify-center text-cyan-300 font-bold font-mono text-sm mb-3">
      02
    </div>
    <h3 class="text-base font-bold text-white m-0">100토큰의 점진적 로딩</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      이름과 설명만 상시 대기시키고 필요할 때만 본문을 로드하여 98% 이상의 토큰 효율성을 달성합니다.
    </p>
  </div>
  <div class="glass-card p-5 border-purple-500/40" v-click="3">
    <div class="w-8 h-8 rounded bg-purple-950/90 border border-purple-400/70 flex items-center justify-center text-purple-300 font-bold font-mono text-sm mb-3">
      03
    </div>
    <h3 class="text-base font-bold text-white m-0">정밀한 트리거 & 자유도</h3>
    <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
      명확한 <code>name</code>/<code>description</code> 공식과 작업 성격에 맞춘 자유도(Freedom Level) 제어가 품질을 결정합니다.
    </p>
  </div>
</div>

<!--
[발표자]
1세션을 요약해 보겠습니다.
[click] 첫째, 스킬은 AI를 위한 업무 표준 절차서(SOP)입니다.
[click] 둘째, 점진적 로딩 덕분에 컨텍스트 낭비 없이 수백 개의 스킬을 동시 탑재할 수 있습니다.
[click] 셋째, 명확한 트리거 설계와 자유도 조절이 성공적인 스킬의 비결입니다.
-->

---
transition: fade-out
layout: default
glowSeed: 400
clicks: 1
---
<!-- slide:S14 -->

<div class="mb-3">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-950/90 border border-purple-400/70 text-purple-300 text-xs font-mono font-bold tracking-wider uppercase mb-1">
    Next Session Preview · Roadmap
  </div>
  <h2 class="text-2xl font-black text-white mt-0.5">외부 시스템과 연결되는 지능형 스킬 생태계</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">Session 2: MCP 커넥터, 플러그인 & 엔터프라이즈 운영 전략</p>
</div>

<div class="grid grid-cols-12 gap-4 items-stretch">
  <div class="col-span-5 flex flex-col justify-between space-y-3">
    <div class="glass-card p-4 border-purple-500/40">
      <h3 class="text-sm font-bold text-white mb-2 flex items-center gap-1.5">
        <span class="i-carbon:connect text-purple-400"></span> 스킬에서 MCP로의 확장
      </h3>
      <p class="text-xs text-slate-200 font-medium leading-relaxed m-0">
        1세션에서 배운 <strong>Skills(지침·SOP)</strong>를 넘어, Slack·CRM·사내 DB를 직접 호출하는 <strong>MCP 커넥터</strong>와 실행 가상머신 연동을 다룹니다.
      </p>
      <div class="flex items-center flex-wrap gap-2 mt-3 text-[11px] font-mono text-cyan-300 font-bold">
        <span class="px-2 py-0.5 rounded bg-white/10 border border-white/20">MCP Protocol</span>
        <span class="px-2 py-0.5 rounded bg-white/10 border border-white/20">plugin.json</span>
        <span class="px-2 py-0.5 rounded bg-white/10 border border-white/20">VM Tools</span>
      </div>
    </div>
    <div class="glass-card p-3 border-emerald-500/40 bg-emerald-950/30 flex items-center justify-between" v-click="1">
      <div class="flex items-center gap-2 text-xs font-bold text-emerald-300">
        <span class="i-carbon:cafe text-base text-amber-400"></span>
        <span>10분 휴식 후 Session 2가 시작됩니다.</span>
      </div>
    </div>
  </div>

  <div class="col-span-7 flex flex-col justify-center">
    <div class="rounded-xl overflow-hidden border border-purple-500/30 bg-black/80 shadow-2xl p-2 flex flex-col items-center justify-center">
      <img src="/assets/agent-skills-architecture.png" class="w-full h-auto max-h-[290px] object-contain rounded-lg" alt="Agent + Skills + Computer Architecture" />
      <div class="w-full text-center mt-1.5 text-[10.5px] font-mono text-slate-300 font-medium">
        Anthropic 공식 아키텍처: Core Prompt + Skills(지침) + MCP(도구) + VM(실행)
      </div>
    </div>
  </div>
</div>

<!--
[발표자]
1세션 수고 많으셨습니다!
오늘 우리가 배운 것은 오른쪽 아키텍처의 skills 폴더 패키지(SKILL.md, references, scripts)였습니다.
[click] 10분 휴식 후 2세션에서는 왼쪽의 MCP 서버와 상단의 Python/Bash 실행 도구를 결합하여 엔터프라이즈 환경으로 확장해 보겠습니다. 감사합니다!
-->