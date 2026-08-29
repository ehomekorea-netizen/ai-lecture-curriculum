---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: "실전 SKILL 응용: Antigravity & GPTwork 실습과 직무별 모범 사례"
exportFilename: session-02-skill-practical-applications
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
glow: full
glowOpacity: 0.5
glowSeed: 201
routerMode: hash
defaults:
  layout: default
  transition: fade-out
---
<!-- slide:S01 -->

<div class="flex items-center justify-center flex-col text-center">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-xs font-mono font-bold tracking-wider uppercase mb-4">
    <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
    Session 02 · 50 Minutes Hands-on
  </div>
  <h1 class="m-0 text-white text-4xl lg:text-5xl font-black leading-tight tracking-tight font-cover">
    실전 SKILL 응용<br/>
    <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-emerald-400">Antigravity & GPTwork 실습과 직무별 모범 사례</span>
  </h1>
  <p class="mt-4 text-slate-100 text-lg font-medium max-w-2xl leading-relaxed">
    사내 지식(references/)과 보조 도구(scripts/)를 결합하여<br/>
    기획·마케팅·인사·운영 전 직무의 강력한 AI 업무 비서를 구축하고 디버깅합니다.
  </p>
  <div class="flex items-center justify-center flex-wrap gap-4 mt-6 text-xs text-slate-300 font-mono font-medium">
    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-white">
      <img src="/icons/antigravity-color.svg" class="w-4 h-4 inline-block" alt="Antigravity" />
      Google Antigravity
    </span>
    <span class="text-white/20">|</span>
    <div class="inline-flex items-center gap-2.5">
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-black/60 border border-white/10 text-sky-300 font-bold">
        <span class="i-carbon:flash text-amber-400"></span>
        GPTwork $skill creator
      </span>
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-black/60 border border-white/10 text-emerald-300">
        <span class="i-carbon:notebook text-emerald-400"></span>
        직무별 Best Practice
      </span>
    </div>
  </div>
</div>

<!--
[발표자]
안녕하세요! 2세션에 오신 것을 환영합니다.
1세션에서 SKILL의 기본 원리와 100토큰 점진적 로딩 구조를 배웠다면, 이번 2세션에서는 Antigravity와 GPTwork 환경에서 직접 스킬을 돌려보고, 오작동을 스스로 고치는 디버깅 기법과 직무별 모범 사례를 마스터해보겠습니다.
-->

---
transition: fade-out
title: 문제 제기: 스킬 실행 시 마주하는 현실
glowSeed: 205
clicks: 3
---
<!-- slide:S02 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Tension & Real-world Friction</div>
  <h2 class="text-2xl font-black text-white mt-1">스킬을 만들었는데 왜 내 맘대로 안 움직일까?</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">처음 스킬을 만들어 실행할 때 누구나 마주치는 3대 오작동 증상</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-rose-950/90 border border-rose-400/70 text-rose-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:warning-alt-filled text-xs"></span> 증상 1 · 호출 실패
      </div>
      <h3 class="text-base font-bold text-white m-0">스킬 호출 실패</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        질문을 던졌는데 AI가 스킬을 펴보지도 않고 평소처럼 뻔한 일반 답변을 내놓는 현상.
      </p>
    </div>
    <div class="mt-2.5 p-2.5 rounded bg-black/60 border border-white/10 text-[11px] text-rose-200 min-h-[48px] flex items-center gap-1.5">
      <span class="i-carbon:arrow-right text-rose-400 shrink-0"></span>
      <span><strong>원인:</strong> Description에 사용자가 부를 핵심 키워드가 빠져 있음.</span>
    </div>
  </div>
  <div class="glass-card p-4 border-amber-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-amber-950/90 border border-amber-400/70 text-amber-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:warning-alt-filled text-xs"></span> 증상 2 · 포맷 이탈
      </div>
      <h3 class="text-base font-bold text-white m-0">출력 양식 이탈</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        표나 불릿으로 정리하라고 했는데 장문의 줄글로 장황하게 답하거나 누락이 생기는 현상.
      </p>
    </div>
    <div class="mt-2.5 p-2.5 rounded bg-black/60 border border-white/10 text-[11px] text-amber-200 min-h-[48px] flex items-center gap-1.5">
      <span class="i-carbon:arrow-right text-amber-400 shrink-0"></span>
      <span><strong>원인:</strong> 출력 예시(Few-shot) 없이 말로만 설명했기 때문.</span>
    </div>
  </div>
  <div class="glass-card p-4 border-purple-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-purple-950/90 border border-purple-400/70 text-purple-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:warning-alt-filled text-xs"></span> 증상 3 · 지식 오염
      </div>
      <h3 class="text-base font-bold text-white m-0">사내 규정 왜곡</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        사내 휴가 일수나 결재 라인을 물었는데 AI가 세상 일반적인 지식으로 그럴듯하게 답함.
      </p>
    </div>
    <div class="mt-2.5 p-2.5 rounded bg-black/60 border border-white/10 text-[11px] text-purple-200 min-h-[48px] flex items-center gap-1.5">
      <span class="i-carbon:arrow-right text-purple-400 shrink-0"></span>
      <span><strong>원인:</strong> 규정 문서(references/)를 파일로 주입하지 않음.</span>
    </div>
  </div>
</v-clicks>
</div>

<div class="mt-4 p-3 rounded-xl bg-white/5 border border-white/10 text-center text-xs text-slate-100 font-bold">
  "스킬은 한 번에 완성되지 않습니다. 실행 과정을 이해하고 구조적으로 점검하면 100% 통제할 수 있습니다."
</div>

<!--
[발표자]
스킬을 처음 만들어보면 '어? 왜 내가 만든 스킬을 안 쓰지?', '왜 양식을 안 지키지?' 하고 당황하게 됩니다.
[click] 첫째, 설명(Description)에 트리거 키워드가 없어서 호출 자체를 안 하거나,
[click] 둘째, 출력 예시가 없어서 포맷이 깨지거나,
[click] 셋째, 회사 규정을 몰라서 할루시네이션(거짓 정보)을 뱉는 것입니다. 오늘 이 3가지를 완벽히 해결해보겠습니다.
-->

---
transition: fade-out
title: Antigravity & GPTwork 런타임
glowSeed: 215
clicks: 3
---
<!-- slide:S03 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Runtime & Execution Pipeline</div>
  <h2 class="text-2xl font-black text-white mt-1">Antigravity & GPTwork에서 스킬이 실행되는 3단계</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">사용자 질문부터 최종 결과물 산출까지 이어지는 내부 동작 메커니즘</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/30 flex flex-col justify-between">
    <div>
      <div class="w-7 h-7 rounded-full bg-cyan-950/90 border border-cyan-400/70 flex items-center justify-center text-cyan-300 font-mono font-bold text-xs mb-3">
        1
      </div>
      <h3 class="text-base font-bold text-white m-0">질문 인입 & 트리거 감지</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        사용자가 채팅창에 질문을 입력하면, AI가 상시 대기 중인 <strong>수백 개 스킬의 Description(100토큰)</strong>을 0.1초 만에 훑어보고 매칭.
      </p>
    </div>
    <div class="mt-3 p-2 rounded bg-black/60 border border-white/10 text-[11px] text-cyan-300 font-mono flex items-center gap-1.5">
      <span class="i-carbon:chat text-cyan-400 shrink-0"></span>
      <span>"지난주 VOC 요약해줘" <span class="text-slate-500">➔</span> [voc-analysis] 매칭!</span>
    </div>
  </div>
  <div class="glass-card p-4 border-sky-500/30 flex flex-col justify-between">
    <div>
      <div class="w-7 h-7 rounded-full bg-sky-950/90 border border-sky-400/70 flex items-center justify-center text-sky-300 font-mono font-bold text-xs mb-3">
        2
      </div>
      <h3 class="text-base font-bold text-white m-0">SOP 지침 온디맨드 주입</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        매칭된 스킬의 <strong>SKILL.md 본문과 필요한 references/ 문서</strong>를 작업 컨텍스트에 즉시 로드하여 표준 절차를 숙지.
      </p>
    </div>
    <div class="mt-3 p-2 rounded bg-black/60 border border-white/10 text-[11px] text-sky-300 font-mono flex items-center gap-1.5">
      <span class="i-carbon:document text-sky-400 shrink-0"></span>
      <span>SKILL.md + references/voc_categories.md</span>
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/30 flex flex-col justify-between">
    <div>
      <div class="w-7 h-7 rounded-full bg-emerald-950/90 border border-emerald-400/70 flex items-center justify-center text-emerald-300 font-mono font-bold text-xs mb-3">
        3
      </div>
      <h3 class="text-base font-bold text-white m-0">표준 규칙 기반 완수</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        스킬에 명시된 <strong>단계별 순서(Step 1~3)와 Few-shot 양식</strong>에 따라 오차 없이 일관된 고품질 결과물을 생성.
      </p>
    </div>
    <div class="mt-3 p-2 rounded bg-black/60 border border-white/10 text-[11px] text-emerald-300 font-mono flex items-center gap-1.5">
      <span class="i-carbon:checkmark-filled text-emerald-400 shrink-0"></span>
      <span>5단계 심각도 분류표 + Action Item 출력</span>
    </div>
  </div>
</v-clicks>
</div>

<div class="mt-4 px-3 py-2 rounded-lg bg-cyan-950/40 border border-cyan-500/30 text-xs text-cyan-200 font-medium flex items-center gap-2">
  <span class="i-carbon:idea text-cyan-300 text-sm shrink-0"></span>
  <span><strong>핵심 요약:</strong> 우리는 AI에게 일일이 "이렇게 해라" 지시하지 않고, <strong>"언제 켜지고(Description) 어떻게 일할지(Body)"</strong>를 미리 정의해 둘 뿐입니다.</span>
</div>

<!--
[발표자]
Antigravity나 GPTwork에서 스킬은 3단계로 돌아갑니다.
[click] 첫째, 사용자가 질문을 던지면 AI가 100토큰짜리 Description을 보고 '아, 이 스킬을 쓸 차례구나' 감지합니다.
[click] 둘째, 그제서야 해당 폴더의 SKILL.md 본문과 참고 문서를 읽어옵니다.
[click] 셋째, 지침에 적힌 양식 그대로 완벽한 결과를 출력합니다.
-->

---
transition: fade-out
title: 하위 폴더 선택 기준: 결정 트리
glowSeed: 230
clicks: 3
---
<!-- slide:S04 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Architecture Decision Guide</div>
  <h2 class="text-2xl font-black text-white mt-1">하위 폴더 선택 기준: 언제 무엇을 넣어야 하는가?</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">복잡하게 만들지 않고 내 업무에 딱 맞는 가장 심플한 구조를 선택하는 기준</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-slate-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-slate-800 border border-slate-400/60 text-slate-200 text-xs font-mono font-bold mb-2">
        Type A · 단일 파일
      </div>
      <h3 class="text-base font-bold text-white m-0 flex items-center gap-1.5">
        <span class="i-carbon:document text-slate-300"></span> SKILL.md 만 작성
      </h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        <strong>추천 대상:</strong> 절차와 규칙이 단순하고 외부 문서나 계산이 필요 없는 일반 업무.
      </p>
      <ul class="mt-2 text-xs text-slate-300 space-y-1 list-none p-0">
        <li>• 영문 이메일 톤 정중화</li>
        <li>• 회의록 3줄 요약 & Action 정리</li>
        <li>• 마케팅 블로그 초안 생성</li>
      </ul>
    </div>
    <div class="mt-2 text-[11px] text-emerald-300 font-bold flex items-center gap-1">
      <span class="i-carbon:checkmark text-emerald-400"></span> 80%의 업무는 이것만으로 충분!
    </div>
  </div>
  <div class="glass-card p-4 border-sky-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-sky-950/90 border border-sky-400/70 text-sky-300 text-xs font-mono font-bold mb-2">
        Type B · 지식 확장
      </div>
      <h3 class="text-base font-bold text-white m-0 flex items-center gap-1.5">
        <span class="i-carbon:folder text-sky-400"></span> references/ 추가
      </h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        <strong>추천 대상:</strong> 분량이 많아 본문에 다 넣으면 토큰이 낭비되는 규정집, 양식, 용어 사전.
      </p>
      <ul class="mt-2 text-xs text-slate-300 space-y-1 list-none p-0">
        <li>• 사내 복지 규정 / 취업규칙 전문</li>
        <li>• 회사 공식 제안서 템플릿(Markdown)</li>
        <li>• 업계 전문 용어집 (Glossary)</li>
      </ul>
    </div>
    <div class="mt-2 text-[11px] text-sky-300 font-bold flex items-center gap-1">
      <span class="i-carbon:flash text-sky-400"></span> 필요할 때만 읽혀 토큰 98% 절감!
    </div>
  </div>
  <div class="glass-card p-4 border-amber-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-amber-950/90 border border-amber-400/70 text-amber-300 text-xs font-mono font-bold mb-2">
        Type C · 도구 확장
      </div>
      <h3 class="text-base font-bold text-white m-0 flex items-center gap-1.5">
        <span class="i-carbon:terminal text-amber-400"></span> scripts/ 추가
      </h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        <strong>추천 대상:</strong> AI가 계산을 틀리거나 텍스트 변환 시 정밀성이 요구되는 보조 작업.
      </p>
      <ul class="mt-2 text-xs text-slate-300 space-y-1 list-none p-0">
        <li>• 날짜/근속연수/환율 정확한 계산</li>
        <li>• 대용량 CSV 파일 정제 및 필터링</li>
        <li>• 텍스트 내 특정 태그 일괄 치환</li>
      </ul>
    </div>
    <div class="mt-2 text-[11px] text-amber-300 font-bold flex items-center gap-1">
      <span class="i-carbon:tools text-amber-400"></span> AI의 연산 한계를 도구로 극복!
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
스킬을 만들 때 가장 많이 묻는 질문이 '언제 폴더를 만들어야 하나요?'입니다.
[click] 첫째, 80%의 업무는 SKILL.md 파일 하나면 끝납니다. 억지로 폴더를 만들 필요가 없습니다.
[click] 둘째, 회사의 긴 규정이나 템플릿 양식은 references/ 폴더에 넣어야 토큰을 아낄 수 있습니다.
[click] 셋째, AI가 계산을 자꾸 틀리거나 대용량 엑셀을 다룰 때만 scripts/에 도구를 쥐여줍니다.
-->

---
transition: fade-out
title: references/ 패턴의 위력
glowSeed: 245
clicks: 1
---
<!-- slide:S05 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Knowledge Layer Design</div>
  <h2 class="text-2xl font-black text-white mt-1"><code>references/</code>의 힘: 사내 규정·양식·톤앤매너 주입</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">회사의 방대한 매뉴얼을 토큰 낭비 없이 완벽하게 전달하는 지식 분리 기법</p>
</div>

<div class="grid grid-cols-12 gap-4 items-stretch">
  <div class="col-span-6 glass-card p-4 border-sky-500/30 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-sky-300 font-bold mb-2 flex items-center gap-1.5">
        <span class="i-carbon:folder text-sky-400"></span> 폴더 구조 예시 (사내 CS 스킬)
      </div>
      <div class="p-3 rounded-lg bg-black/80 border border-white/10 text-xs font-mono text-slate-100 leading-relaxed">
        <span class="text-cyan-400">📁</span> customer-support/<br/>
        &nbsp;&nbsp;├── <span class="text-emerald-300">📄 SKILL.md</span> <span class="text-slate-400">(응대 절차 및 트리거)</span><br/>
        &nbsp;&nbsp;└── <span class="text-sky-300">📁 references/</span><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── <span class="text-amber-300">📄 refund_policy.md</span> <span class="text-slate-400">(환불 규정 20p)</span><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── <span class="text-amber-300">📄 tone_and_voice.md</span> <span class="text-slate-400">(공식 어조 가이드)</span><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── <span class="text-amber-300">📄 email_template.md</span> <span class="text-slate-400">(표준 메일 서식)</span>
      </div>
    </div>
    <div class="mt-3 p-2 rounded bg-sky-950/40 border border-sky-500/30 text-[11.5px] text-sky-200 flex items-center gap-1.5">
      <span class="i-carbon:idea text-sky-300 shrink-0"></span>
      <span><strong>동작 방식:</strong> 평소엔 100토큰만 쓰다가, 사용자가 "환불 어떻게 해요?"라고 물을 때만 <code>refund_policy.md</code>를 펴서 정확한 조항을 인용함.</span>
    </div>
  </div>
  <div class="col-span-6 glass-card p-4 border-emerald-500/30 flex flex-col justify-between">
  <v-clicks>
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold mb-2 flex items-center gap-1.5">
        <span class="i-carbon:edit text-emerald-400"></span> SKILL.md 본문에서 references 호출하는 법
      </div>
      <div class="p-3 rounded-lg bg-black/80 border border-white/10 text-[11.5px] font-mono text-slate-100 leading-relaxed">
        <span class="text-slate-400"># 고객 응대 절차</span><br/>
        <br/>
        <span class="text-cyan-300">## 1. 문의 유형 분류</span><br/>
        - 환불/결제 문의인 경우 <strong>references/refund_policy.md</strong>를 확인하여 가능 여부를 판정하세요.<br/>
        <br/>
        <span class="text-cyan-300">## 2. 답변 작성 규칙</span><br/>
        - <strong>references/tone_and_voice.md</strong>에 명시된 정중하고 공감하는 어조를 사용하세요.<br/>
        - 최종 답변은 <strong>references/email_template.md</strong> 양식에 맞추어 출력하세요.
      </div>
    </div>
    <div class="mt-3 p-2 rounded bg-emerald-950/40 border border-emerald-500/30 text-[11.5px] text-emerald-200 flex items-center gap-1.5">
      <span class="i-carbon:star-filled text-emerald-300 shrink-0"></span>
      <span><strong>효과:</strong> AI가 규정을 상상해서 지어내지 않고, 회사의 최신 정책 그대로 100% 일관되게 응대.</span>
    </div>
  </v-clicks>
  </div>
</div>

<!--
[발표자]
references 폴더를 쓰면 엄청난 이점이 생깁니다.
[click] 환불 규정이 20페이지나 되더라도, 평소에는 토큰을 단 1개도 소모하지 않습니다.
[click] 고객이 '환불'이라는 단어를 꺼냈을 때만 AI가 refund_policy.md를 쏙 꺼내서 읽고 답합니다. 회사 규정이 바뀌면 이 파일 하나만 수정하면 전사 AI가 즉시 업데이트됩니다.
-->

---
transition: fade-out
title: scripts/ 패턴의 위력
glowSeed: 260
clicks: 1
---
<!-- slide:S06 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Deterministic Tooling</div>
  <h2 class="text-2xl font-black text-white mt-1"><code>scripts/</code>의 힘: AI의 계산 실수와 포맷 오류 없애기</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">AI에게 어려운 수학적 연산이나 데이터 정제 작업을 전용 도구로 해결하는 원리</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
  <div class="glass-card p-4 border-rose-500/30 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-rose-950/90 border border-rose-400/70 text-rose-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:warning-alt-filled text-xs"></span> AI가 취약한 영역 (확률적 모델)
      </div>
      <ul class="mt-2 space-y-2 text-xs text-slate-200 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="i-carbon:close-outline text-rose-400 shrink-0 mt-0.5"></span><span>복잡한 날짜/영업일 계산 (예: "오늘부터 영업일 기준 D+14일은?")</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:close-outline text-rose-400 shrink-0 mt-0.5"></span><span>수천 줄의 CSV 파일에서 특정 조건 행만 정확히 필터링하기</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:close-outline text-rose-400 shrink-0 mt-0.5"></span><span>특정 규칙에 따른 정밀한 수치 합산 및 세금 계산</span></li>
      </ul>
    </div>
    <div class="p-2.5 rounded bg-black/60 border border-white/10 text-[11px] text-slate-300">
      결과: 확률적으로 계산하다 보니 가끔 1~2일씩 오차가 발생함.
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/30 flex flex-col justify-between">
  <v-clicks>
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:terminal text-xs"></span> scripts/ 보조 도구로 해결
      </div>
      <ul class="mt-2 space-y-2 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><code>calc_days.py</code>로 0.001초 만에 100% 정답 계산</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><code>filter.py</code>로 대용량 엑셀을 토큰 낭비 없이 고속 추출</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span>AI는 '판단/작성'만 하고, '계산'은 스크립트에 위임</span></li>
      </ul>
    </div>
    <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-[11px] text-emerald-200 font-bold flex items-center gap-1.5">
      <span class="i-carbon:idea text-emerald-300 shrink-0"></span>
      <span>"AI에게 암산을 시키지 말고, 계산기를 손에 쥐여주세요!"</span>
    </div>
  </v-clicks>
  </div>
</div>

<div class="mt-3 p-3 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 leading-relaxed flex items-center gap-2">
  <span class="i-carbon:information text-cyan-300 shrink-0"></span>
  <span><strong>작성 팁:</strong> 스크립트를 직접 짤 줄 몰라도 괜찮습니다! GPTwork나 Antigravity에게 <em>"이 계산을 해주는 간단한 파이썬 스크립트 하나 만들어줘"</em>라고 요청해서 <code>scripts/</code> 폴더에 넣어두기만 하면 됩니다.</span>
</div>

<!--
[발표자]
AI는 문장을 매끄럽게 쓰는 데는 천재지만, 날짜 계산이나 복잡한 덧셈에서는 가끔 실수를 합니다.
[click] 이때 scripts 폴더에 5줄짜리 간단한 파이썬 계산기를 넣어두면, AI가 스스로 계산기를 켜서 돌리고 100% 완벽한 정답을 보고서에 적어냅니다.
-->

---
transition: fade-out
title: 직무별 모범 사례 1: 기획 · 마케팅 · 영업
glowSeed: 280
clicks: 3
---
<!-- slide:S07 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Real-world Use Cases 1</div>
  <h2 class="text-2xl font-black text-white mt-1">직무별 모범 사례: 기획 · 마케팅 · 영업</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">비즈니스 현업에서 즉시 생산성을 10배 끌어올리는 실전 스킬 레시피</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-cyan-950/90 border border-cyan-400/70 text-cyan-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:chart-line text-xs"></span> 기획 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">사업 기획서 초안 생성</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        아이디어 1줄만 던져도 사내 표준 기획 양식(문제 정의 ➔ 타겟 ➔ 솔루션 ➔ 수익 모델)으로 완성.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/biz_template.md</div>
      <div class="text-cyan-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-cyan-400 shrink-0"></span> "기획서 초안 10분 만에 완성"</div>
    </div>
  </div>
  <div class="glass-card p-4 border-pink-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-pink-950/90 border border-pink-400/70 text-pink-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:bullhorn text-xs"></span> 마케팅 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">채널별 맞춤 카피 작성</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        제품 설명 1개를 인스타그램, 링크드인, 뉴스레터, 블로그 등 각 채널별 톤앤매너에 맞게 원클릭 변환.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/tone_guide.md</div>
      <div class="text-pink-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-pink-400 shrink-0"></span> "채널별 맞춤 카피 즉시 생성"</div>
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:user-multiple text-xs"></span> 영업 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">바이어 맞춤 제안 요약</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        고객사 미팅 메모를 입력하면 핵심 니즈 추출, 제안 가격표 자동 매핑 후 후속 이메일 초안 작성.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/pricing_table.md</div>
      <div class="text-emerald-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-emerald-400 shrink-0"></span> "미팅 직후 5분 만에 팔로업"</div>
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
실제 현업에서는 이렇게 씁니다.
[click] 기획자는 회사 표준 템플릿을 references에 넣어두고 아이디어만 던져 기획서 초안을 뽑습니다.
[click] 마케터는 인스타 톤, 링크드인 톤 가이드를 넣어두고 원클릭으로 멀티 채널 카피를 만듭니다.
[click] 영업 담당자는 가격표와 팔로업 메일 양식을 매핑해 미팅 끝나자마자 5분 만에 제안서를 보냅니다.
-->

---
transition: fade-out
title: 직무별 모범 사례 2: 인사 · 총무 · CS · 운영
glowSeed: 295
clicks: 3
---
<!-- slide:S08 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Real-world Use Cases 2</div>
  <h2 class="text-2xl font-black text-white mt-1">직무별 모범 사례: 인사 · 총무 · CS · 운영</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">반복 문의와 취합 업무를 자동화하여 본질적인 업무에 집중하는 백오피스 혁신</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-amber-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-amber-950/90 border border-amber-400/70 text-amber-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:headset text-xs"></span> CS 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">고객 VOC 분석 & 답변</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        고객 불만 글을 5단계 심각도로 자동 분류하고, 사내 매뉴얼에 근거한 공감형 1차 답변문 작성.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/cs_manual.md</div>
      <div class="text-amber-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-amber-400 shrink-0"></span> "감정 소모 감소 및 일관성 100%"</div>
    </div>
  </div>
  <div class="glass-card p-4 border-purple-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-purple-950/90 border border-purple-400/70 text-purple-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:user-admin text-xs"></span> 인사 · 총무 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">입사자 온보딩 FAQ</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        "연차 어떻게 써요?", "주차 지원 되나요?" 등 매일 반복되는 사내 질문에 24시간 정확한 규정 답변.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/hr_policy.md</div>
      <div class="text-purple-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-purple-400 shrink-0"></span> "단순 문의 응대 시간 80% 절감"</div>
    </div>
  </div>
  <div class="glass-card p-4 border-blue-500/40 flex flex-col justify-between">
    <div>
      <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-blue-950/90 border border-blue-400/70 text-blue-300 text-xs font-mono font-bold mb-2">
        <span class="i-carbon:workspace text-xs"></span> 운영 · 관리 직무
      </div>
      <h3 class="text-base font-bold text-white m-0">주간 업무 보고서 정제</h3>
      <p class="text-xs text-slate-200 font-medium mt-2 leading-relaxed">
        팀원들이 보낸 중구난방 업무 일지를 취합하여 완료 업무, 진행 중, 이슈/리스크 3단 표로 정제.
      </p>
    </div>
    <div class="mt-2.5 p-2 rounded bg-black/60 border border-white/10 text-[11px] font-mono min-h-[52px] flex flex-col justify-center">
      <div class="text-slate-300 flex items-center gap-1"><span class="i-carbon:folder text-amber-400"></span> references/report_format.md</div>
      <div class="text-blue-300 font-bold flex items-center gap-1 text-[11px] whitespace-nowrap"><span class="i-carbon:flash text-blue-400 shrink-0"></span> "금요일 주간 보고 취합 자동화"</div>
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
백오피스에서도 혁신이 일어납니다.
[click] CS팀은 VOC 분류와 감정 공감 멘트를 매뉴얼대로 자동 생성하고,
[click] 인사팀은 반복되는 사내 규정 질문을 스킬에 맡겨 본연의 인재 관리에 집중합니다.
[click] 운영팀은 팀원들의 거친 주간 업무 일지를 깔끔한 임원 보고용 3단 표로 순식간에 정리합니다.
-->

---
transition: fade-out
title: 실전 디버깅 4대 점검법
glowSeed: 310
clicks: 4
---
<!-- slide:S09 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Troubleshooting Checklist</div>
  <h2 class="text-2xl font-black text-white mt-1">스킬 디버깅 체크리스트: 문제 발생 시 4대 점검법</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">스킬이 제대로 동작하지 않을 때 즉시 원인을 찾고 해결하는 실전 공식</p>
</div>

<div class="grid grid-cols-2 gap-4">
<v-clicks>
  <div class="glass-card p-3.5 border-cyan-500/30">
    <div class="flex items-center gap-2 text-xs font-mono text-cyan-300 font-bold mb-1">
      <span class="w-5 h-5 rounded-full bg-cyan-950/90 border border-cyan-400 flex items-center justify-center text-xs">1</span>
      Description 키워드 점검 (트리거 실패 시)
    </div>
    <p class="text-xs text-slate-100 font-medium leading-relaxed m-0">
      • 사용자가 실제로 입력할 자연어 단어(명사/동사)가 포함되었는가?<br/>
      • <em>"~할 때 이 스킬을 사용하세요"</em>라는 명확한 트리거 시점을 적었는가?
    </p>
  </div>
  <div class="glass-card p-3.5 border-emerald-500/30">
    <div class="flex items-center gap-2 text-xs font-mono text-emerald-300 font-bold mb-1">
      <span class="w-5 h-5 rounded-full bg-emerald-950/90 border border-emerald-400 flex items-center justify-center text-xs">2</span>
      단계 번호화 점검 (순서 누락 시)
    </div>
    <p class="text-xs text-slate-100 font-medium leading-relaxed m-0">
      • 긴 줄글 대신 <code>## 1단계</code>, <code>## 2단계</code>로 번호를 매겼는가?<br/>
      • 선행 작업이 완료되어야 다음 단계로 가도록 조건을 걸었는가?
    </p>
  </div>
  <div class="glass-card p-3.5 border-amber-500/30">
    <div class="flex items-center gap-2 text-xs font-mono text-amber-300 font-bold mb-1">
      <span class="w-5 h-5 rounded-full bg-amber-950/90 border border-amber-400 flex items-center justify-center text-xs">3</span>
      Few-shot 예시 점검 (포맷 붕괴 시)
    </div>
    <p class="text-xs text-slate-100 font-medium leading-relaxed m-0">
      • 말로 설명하는 대신 '이상적인 출력 예시 블록'을 직접 보여주었는가?<br/>
      • 마크다운 표, 불릿 구조를 예시 안에 명확히 박아두었는가?
    </p>
  </div>
  <div class="glass-card p-3.5 border-purple-500/30">
    <div class="flex items-center gap-2 text-xs font-mono text-purple-300 font-bold mb-1">
      <span class="w-5 h-5 rounded-full bg-purple-950/90 border border-purple-400 flex items-center justify-center text-xs">4</span>
      예외 처리 규칙 점검 (거짓 정보 생성 시)
    </div>
    <p class="text-xs text-slate-100 font-medium leading-relaxed m-0">
      • 모르는 정보가 들어왔을 때 상상하지 말고 <em>"규정 외 사항으로 담당자 확인 필요"</em>라고 출력하도록 지침을 주었는가?
    </p>
  </div>
</v-clicks>
</div>

<div class="mt-3.5 p-2.5 rounded-lg bg-black/60 border border-white/10 text-center text-xs text-slate-200 flex items-center justify-center gap-2">
  <span class="i-carbon:idea text-amber-300 text-sm shrink-0"></span>
  <span><strong>디버깅 팁:</strong> 스킬이 말을 안 들으면 프롬프트를 다시 치지 말고, <strong><code>SKILL.md</code> 파일로 돌아가 위 4개 중 빠진 것을 보완</strong>하세요!</span>
</div>

<!--
[발표자]
스킬을 고칠 때는 이 4단계 체크리스트만 보면 됩니다.
[click] 첫째, 스킬이 안 켜지면 Description에 키워드를 더 넣으세요.
[click] 둘째, 순서를 건너뛰면 1단계, 2단계 번호를 매기세요.
[click] 셋째, 양식이 깨지면 백 마디 말보다 Few-shot 예시를 하나 박아 넣으세요.
[click] 넷째, 거짓말을 하면 모를 땐 '담당자 문의 요망'으로 출력하라는 예외 조항을 넣으세요.
-->

---
transition: fade-out
title: 실습 P02 안내
glowSeed: 330
clicks: 0
---
<!-- slide:S10 -->

<div class="mb-4">
  <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/90 border border-emerald-400/70 text-emerald-300 text-xs font-mono font-bold uppercase mb-2">
    <span class="i-carbon:tools text-sm"></span> Hands-on Practice P02 · 15 Minutes
  </div>
  <h2 class="text-3xl font-black text-white mt-1">내 직무 맞춤형 실전 복합 스킬 완성하기</h2>
  <p class="text-sm text-slate-200 font-medium mt-1">사내 지식(references/)을 결합한 실전 스킬을 작성하고 Antigravity / GPTwork에서 직접 테스트합니다.</p>
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-1">STEP 1 (3분)</div>
      <h3 class="text-base font-bold text-white m-0">직무 시나리오 선정</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-cyan-400 shrink-0 mt-0.5"></span><span>고객 문의 응대 (CS/영업)</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-cyan-400 shrink-0 mt-0.5"></span><span>주간 업무 보고서 정제 (운영/기획)</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-cyan-400 shrink-0 mt-0.5"></span><span>사내 규정 Q&A 비서 (인사/총무)</span></li>
      </ul>
    </div>
  </div>
  <div class="glass-card p-4 border-sky-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-sky-300 font-bold uppercase mb-1">STEP 2 (5분)</div>
      <h3 class="text-base font-bold text-white m-0">지식 문서 준비</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-sky-400 shrink-0 mt-0.5"></span><span>간단한 가이드라인 1장 작성</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-sky-400 shrink-0 mt-0.5"></span><span>표준 답변 서식 또는 평가 기준</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-sky-400 shrink-0 mt-0.5"></span><span><code>references/guide.md</code>로 저장</span></li>
      </ul>
    </div>
  </div>
  <div class="glass-card p-4 border-emerald-500/40 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase mb-1">STEP 3 (7분)</div>
      <h3 class="text-base font-bold text-white m-0">SKILL.md 작성 및 검증</h3>
      <ul class="mt-2.5 space-y-1.5 text-xs text-slate-100 font-medium list-none p-0">
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-emerald-400 shrink-0 mt-0.5"></span><span>YAML 헤더 + 단계별 SOP 작성</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-emerald-400 shrink-0 mt-0.5"></span><span>Antigravity/GPTwork에서 질문 입력</span></li>
        <li class="flex items-start gap-1.5"><span class="i-carbon:circle-dash text-emerald-400 shrink-0 mt-0.5"></span><span>스킬 호출 및 출력 양식 검증 & 디버깅</span></li>
      </ul>
    </div>
  </div>
</div>

<div class="mt-3.5 glass-card p-3 border-sky-500/30 bg-black/60 flex items-center justify-between">
  <div class="flex items-center gap-3">
    <div class="px-3 py-1.5 rounded-lg bg-sky-950/90 border border-sky-400/60 flex items-center gap-1.5 text-sky-300 font-mono font-bold text-xs shrink-0">
      <span class="i-carbon:cube text-sm text-sky-400"></span> Pro Tip
    </div>
    <div class="text-xs text-slate-200 leading-relaxed">
      GPTwork 사용자는 프롬프트 창에 <code class="text-sky-300 bg-sky-950/70 px-1.5 py-0.5 rounded border border-sky-500/30 font-mono font-bold">$skill creator</code>를 입력하고 원하는 직무 업무를 말하면 초안 작성을 훨씬 빠르게 시작할 수 있습니다.
    </div>
  </div>
</div>

<!--
[발표자]
이제 2차 실습에 들어갑니다! 15분 동안 내 직무에 필요한 references 문서를 하나 만들고, 이를 연동하는 SKILL.md를 작성해 직접 Antigravity나 GPTwork에서 돌려보겠습니다.
-->

---
transition: fade-out
title: 실습 템플릿 예시
glowSeed: 345
clicks: 1
---
<!-- slide:S11 -->

<div class="mb-3">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Ready-to-use Template</div>
  <h2 class="text-2xl font-black text-white mt-1">실습 템플릿: 직무별 완성형 예제 가이드</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">아래 템플릿 구조를 복사하여 자신의 업무 내용에 맞게 키워드와 양식을 수정하세요</p>
</div>

<div class="grid grid-cols-2 gap-4 items-stretch">
  <div class="glass-card p-3.5 border-sky-500/30">
    <div class="text-xs font-mono text-sky-300 font-bold mb-1.5 flex items-center gap-1.5">
      <span class="i-carbon:document text-sky-400"></span> SKILL.md 템플릿
    </div>
    <div class="p-2.5 rounded bg-black/80 border border-white/10 text-[11px] font-mono text-slate-100 leading-relaxed overflow-hidden">
      <div class="text-amber-400 font-bold">---</div>
      <div class="text-cyan-300">name: <span class="text-white font-bold">voc-responder</span></div>
      <div class="text-cyan-300">description: <span class="text-slate-200">고객 문의 및 불만 VOC 분석 및 답변 시 실행</span></div>
      <div class="text-amber-400 font-bold">---</div>
      <div class="text-slate-300 font-bold mt-1"># 고객 문의 처리 SOP</div>
      <div class="text-slate-200 mt-0.5"><span class="text-cyan-300">## 1. 문의 분석:</span> references/guide.md를 참고하여 심각도(1~3단계)를 분류하세요.</div>
      <div class="text-slate-200 mt-0.5"><span class="text-cyan-300">## 2. 답변 작성:</span> 아래 출력 포맷에 맞추어 작성하세요.</div>
      <div class="text-slate-400 mt-1">[출력 포맷: 심각도 / 핵심 요약 / 고객 답변문]</div>
    </div>
  </div>
  <div class="glass-card p-3.5 border-emerald-500/30">
  <v-clicks>
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon:folder text-emerald-400"></span> references/guide.md 템플릿
      </div>
      <div class="p-2.5 rounded bg-black/80 border border-white/10 text-[11px] font-mono text-slate-100 leading-relaxed overflow-hidden">
        <div class="text-emerald-300 font-bold"># 사내 고객 응대 가이드</div>
        <div class="text-slate-200 mt-1">• <strong>1단계 (단순 문의):</strong> 서비스 사용법, 일정 문의 ➔ 친절히 링크 및 일정 안내</div>
        <div class="text-slate-200 mt-1">• <strong>2단계 (기능 오류):</strong> 버그, 결제 실패 ➔ 사과 멘트 + 재발 방지 약속</div>
        <div class="text-slate-200 mt-1">• <strong>3단계 (강한 불만):</strong> 환불 요구, 피해 주장 ➔ 팀장 직통 에스컬레이션 안내</div>
        <div class="text-amber-300 font-bold mt-1.5 flex items-center gap-1">
          <span class="i-carbon:warning-filled text-amber-400"></span> 금지어: "저희 탓이 아닙니다", "어쩔 수 없습니다"
        </div>
      </div>
    </div>
  </v-clicks>
  </div>
</div>

<div class="mt-3 p-2.5 rounded-lg bg-white/5 border border-white/10 text-center text-xs text-slate-100 font-medium flex items-center justify-center gap-2">
  <span class="i-carbon:idea text-cyan-300 text-sm shrink-0"></span>
  <span><strong>직무별 변형:</strong> 주간 보고서 스킬을 만들고 싶다면 <code>references/report_format.md</code>에 부서 표준 보고 표 양식을 넣으면 됩니다!</span>
</div>

<!--
[발표자]
왼쪽에는 SKILL.md 본문을, 오른쪽에는 references 가이드를 적습니다.
[click] 오른쪽 가이드에 회사만의 1, 2, 3단계 분류 기준과 금지어를 적어두면, AI가 왼쪽 지침을 따라 완벽한 톤으로 답변을 써냅니다.
-->

---
transition: fade-out
title: 실습 진행 & 5대 자가진단
glowSeed: 360
clicks: 0
---
<!-- slide:S12 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Hands-on Execution & Verification</div>
  <h2 class="text-2xl font-black text-white mt-1">15분 집중 실습 & Antigravity/GPTwork 5대 자가진단</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">스킬을 작성하고 채팅창에 질문을 던져 아래 5개 항목을 스스로 테스트하세요</p>
</div>

<div class="grid grid-cols-12 gap-5 items-stretch">
  <div class="col-span-5 glass-card p-5 border-emerald-500/40 flex flex-col justify-between items-center text-center">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase tracking-wider mb-2">실습 잔여 시간</div>
      <div class="text-5xl font-mono font-black text-white tracking-widest my-2">15:00</div>
      <div class="text-xs text-slate-200 font-medium leading-relaxed">
        Antigravity 폴더에 파일을 저장하거나<br/>
        GPTwork에서 스킬을 생성하세요.
      </div>
    </div>
    <div class="w-full mt-4 p-2.5 rounded-lg bg-emerald-950/80 border border-emerald-400/60 text-xs text-emerald-200 font-bold flex items-center justify-center gap-1.5">
      <span class="i-carbon:bullseye text-emerald-400 shrink-0"></span>
      <span><strong>목표:</strong> 질문 입력 시 스킬 자동 발동 및 표준 서식 출력</span>
    </div>
  </div>
  <div class="col-span-7 glass-card p-4 border-cyan-500/40 flex flex-col justify-between">
    <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-2">실전 테스트 5대 자가진단표</div>
    <ul class="space-y-2 text-xs text-slate-100 font-medium list-none p-0">
      <li class="flex items-start gap-2"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><strong>트리거 확인:</strong> 프롬프트 입력 시 AI가 내 스킬을 인식하고 사용하는가?</span></li>
      <li class="flex items-start gap-2"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><strong>지식 참조:</strong> <code>references/</code>에 적어둔 사내 규칙/가이드가 답변에 반영되는가?</span></li>
      <li class="flex items-start gap-2"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><strong>포맷 준수:</strong> 줄글로 흐르지 않고 내가 정한 표/불릿 서식으로 나오는가?</span></li>
      <li class="flex items-start gap-2"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><strong>예외 처리:</strong> 모르는 내용 질문 시 규정 외 사항이라고 바르게 안내하는가?</span></li>
      <li class="flex items-start gap-2"><span class="i-carbon:checkmark-filled text-emerald-400 shrink-0 mt-0.5"></span><span><strong>재현성:</strong> 같은 질문을 3번 다시 물어봐도 일관된 퀄리티를 유지하는가?</span></li>
    </ul>
    <div class="mt-2 text-[11px] text-slate-400 text-right">오작동 시 S09 디버깅 체크리스트 참고</div>
  </div>
</div>

<!--
[발표자]
지금부터 15분간 실습을 진행합니다!
작성을 마친 분은 우측 5대 자가진단표를 보면서 채팅창에 다양한 질문을 던져보고, 의도한 대로 일관되게 답하는지 테스트해보세요.
-->

---
transition: fade-out
title: 흔히 하는 3대 실수와 주의점
glowSeed: 380
clicks: 3
---
<!-- slide:S13 -->

<div class="mb-4">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Pitfalls & Best Solutions</div>
  <h2 class="text-2xl font-black text-white mt-1">스킬 작성 시 흔히 하는 3대 실수와 주의점</h2>
  <p class="text-xs text-slate-200 font-medium mt-0.5">시행착오를 절반으로 줄여주는 실전 안티패턴(Anti-patterns) 회피 가이드</p>
</div>

<div class="grid grid-cols-3 gap-4 items-stretch">
<v-clicks>
  <div class="glass-card p-4 border-rose-500/30 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-rose-300 font-bold mb-1 flex items-center gap-1.5">
        <span class="i-carbon:warning-filled text-rose-400"></span> 1. 본문 과다 복붙 (토큰 낭비)
      </div>
      <p class="text-xs text-slate-200 font-medium mt-1 leading-relaxed">
        SKILL.md 본문에 수십 장짜리 규정집을 통째로 복붙해 넣어 <strong>토큰 폭탄</strong>을 유발하는 경우.
      </p>
    </div>
    <div class="mt-3 p-2.5 rounded bg-emerald-950/40 border border-emerald-500/40 text-[11.5px] text-emerald-200 flex items-center gap-1.5">
      <span class="i-carbon:checkmark-filled text-emerald-400 shrink-0"></span>
      <span><strong>해결책:</strong> 본문은 슬림하게 두고 긴 문서는 <code>references/</code>로 분리하세요.</span>
    </div>
  </div>
  <div class="glass-card p-4 border-amber-500/30 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-amber-300 font-bold mb-1 flex items-center gap-1.5">
        <span class="i-carbon:warning-filled text-amber-400"></span> 2. 지침 간 상충 및 모호성
      </div>
      <p class="text-xs text-slate-200 font-medium mt-1 leading-relaxed">
        위에서는 "자세히 쓰라"고 하고 아래에서는 "3줄 요약하라"고 하여 <strong>AI를 혼란</strong>에 빠뜨리는 경우.
      </p>
    </div>
    <div class="mt-3 p-2.5 rounded bg-emerald-950/40 border border-emerald-500/40 text-[11.5px] text-emerald-200 flex items-center gap-1.5">
      <span class="i-carbon:checkmark-filled text-emerald-400 shrink-0"></span>
      <span><strong>해결책:</strong> 1, 2, 3단계 순서와 <em>"상충 시 요약 우선"</em> 우선순위를 부여하세요.</span>
    </div>
  </div>
  <div class="glass-card p-4 border-purple-500/30 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-purple-300 font-bold mb-1 flex items-center gap-1.5">
        <span class="i-carbon:warning-filled text-purple-400"></span> 3. 부정어 남발 및 예시 부재
      </div>
      <p class="text-xs text-slate-200 font-medium mt-1 leading-relaxed">
        "~하지 마라"만 10개 적어두고 정작 <strong>어떻게 써야 하는지 표준 양식</strong>을 주지 않는 경우.
      </p>
    </div>
    <div class="mt-3 p-2.5 rounded bg-emerald-950/40 border border-emerald-500/40 text-[11.5px] text-emerald-200 flex items-center gap-1.5">
      <span class="i-carbon:checkmark-filled text-emerald-400 shrink-0"></span>
      <span><strong>해결책:</strong> <em>"이렇게 작성하세요"</em>라는 긍정적 출력 템플릿(Few-shot)을 보여주세요.</span>
    </div>
  </div>
</v-clicks>
</div>

<!--
[발표자]
스킬을 만들 때 이 세 가지만 주의하세요.
[click] 첫째, 본문을 너무 길게 쓰지 마세요. 긴 글은 references로 빼야 합니다.
[click] 둘째, 지침끼리 부딪히지 않게 번호와 우선순위를 매기세요.
[click] 셋째, '~하지 마'라고만 하지 말고 '이렇게 써'라는 모범 예시를 하나 주세요.
-->

---
transition: fade-out
title: 2시간 마스터 요약 & 확장 로드맵
glowSeed: 400
clicks: 0
---
<!-- slide:S14 -->

<div class="mb-4 text-center">
  <div class="text-xs font-mono text-cyan-400 uppercase tracking-widest font-bold">Course Summary & Next Horizon</div>
  <h2 class="text-3xl font-black text-white mt-1">나만의 AI 비서에서 팀 전체의 업무 자산으로</h2>
  <p class="text-xs text-slate-200 font-medium mt-1">2시간 동안 학습한 핵심 원칙과 앞으로의 AI 스킬 확장 로드맵</p>
</div>

<div class="grid grid-cols-4 gap-3 text-left">
  <div class="glass-card p-3.5 border-cyan-500/40">
    <div class="text-xs font-mono text-cyan-300 font-bold mb-1 flex items-center gap-1.5">
      <span class="i-carbon:task-complete text-cyan-400"></span> 01. SOP 표준화
    </div>
    <div class="text-[11.5px] text-slate-100 font-medium leading-relaxed">
      매번 복붙하던 프롬프트를 <code>SKILL.md</code> 파일로 규격화하여 업무 일관성 확보.
    </div>
  </div>
  <div class="glass-card p-3.5 border-emerald-500/40">
    <div class="text-xs font-mono text-emerald-300 font-bold mb-1 flex items-center gap-1.5">
      <span class="i-carbon:flash text-emerald-400"></span> 02. 100토큰 대기
    </div>
    <div class="text-[11.5px] text-slate-100 font-medium leading-relaxed">
      수백 개 스킬이 상주해도 비용 걱정 없는 점진적 로딩(Progressive Disclosure) 구조.
    </div>
  </div>
  <div class="glass-card p-3.5 border-sky-500/40">
    <div class="text-xs font-mono text-sky-300 font-bold mb-1 flex items-center gap-1.5">
      <span class="i-carbon:folder text-sky-400"></span> 03. references 확장
    </div>
    <div class="text-[11.5px] text-slate-100 font-medium leading-relaxed">
      사내 규정, 톤앤매너, 양식을 지식 계층으로 분리하여 거짓 답변 원천 차단.
    </div>
  </div>
  <div class="glass-card p-3.5 border-purple-500/40">
    <div class="text-xs font-mono text-purple-300 font-bold mb-1 flex items-center gap-1.5">
      <span class="i-carbon:share text-purple-400"></span> 04. 사내 스킬 공유
    </div>
    <div class="text-[11.5px] text-slate-100 font-medium leading-relaxed">
      내가 만든 고품질 스킬을 폴더 채로 팀원과 공유하여 조직 전체 생산성 극대화.
    </div>
  </div>
</div>

<div class="mt-4 p-4 rounded-xl bg-gradient-to-r from-cyan-950/70 via-black to-emerald-950/70 border border-cyan-400/40 text-center flex flex-col items-center justify-center gap-2">
  <div class="text-white text-sm font-bold flex items-center justify-center gap-2">
    <span class="i-carbon:trophy text-amber-400 text-base"></span>
    <span>수고하셨습니다! 이제 여러분의 모든 반복 업무를 표준 SKILL로 자동화해보세요.</span>
  </div>
  <div class="flex items-center justify-center gap-4 mt-1 text-xs text-slate-300 font-mono">
    <span class="inline-flex items-center gap-1"><img src="/icons/antigravity-color.svg" class="w-3.5 h-3.5 inline-block" /> Google Antigravity</span>
    <span class="text-white/20">·</span>
    <span class="inline-flex items-center gap-1"><img src="/icons/claude-color.svg" class="w-3.5 h-3.5 inline-block" /> Claude Code</span>
    <span class="text-white/20">·</span>
    <span class="inline-flex items-center gap-1"><img src="/icons/openai.svg" class="w-3.5 h-3.5 inline-block" style="filter: invert(1);" /> OpenAI</span>
    <span class="text-white/20">·</span>
    <span class="inline-flex items-center gap-1 text-emerald-300">⚡ Agent Skills Open Standard</span>
  </div>
</div>

<!--
[발표자]
오늘 2시간 동안 여러분은 단순 프롬프트 사용자를 넘어, AI 에이전트의 업무 매뉴얼을 직접 설계하고 통제하는 SKILL 엔지니어로 거듭나셨습니다.
오늘 만든 스킬을 팀원들에게 공유하고, 내일부터 여러분의 반복 업무를 AI에게 믿고 맡겨보세요. 감사합니다!
-->
