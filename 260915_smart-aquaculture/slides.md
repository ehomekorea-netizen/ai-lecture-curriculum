---
layout: default
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: '수산양식과 인공지능 활용'
exportFilename: '스마트수산업_수산양식과_인공지능_활용_강의덱'
info: |
  스마트수산업 전문가 양성과정
  수산양식과 인공지능 활용
  집필: 오진실 (퍼블릭에이아이)
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: true
routerMode: hash
---
<!-- slide:01-Cover -->

<CoverSlide />

<!--
[강사 오프닝]
안녕하십니까, 스마트수산업 전문가 양성과정 교육생 여러분. 반갑습니다.
오늘 우리가 함께 다룰 주제는 제15장 '수산양식과 인공지능 활용'입니다.
우리는 AI 개발자가 되려는 것이 아닙니다.
현장 관리자로서 "수많은 양식 데이터 중 AI가 무엇을 해줄 수 있고, AI 경보를 어떻게 올바르게 읽으며, 생성형 AI와 에이전트로 일지 작성과 사육 관리를 어떻게 혁신할 것인가?" 그 실무적인 안목과 활용 능력을 기르는 여정을 시작해 보겠습니다.
-->

---
layout: default
---
<!-- slide:02-Roadmap-Total -->

<div class="mb-4">
  <h2 class="stage-title">스마트양식 AI 마스터 로드맵</h2>
  <p class="stage-subtitle">데이터의 본질 이해부터 현장 경보 검증, 일지 자동화, 06시 브리핑 에이전트까지 4단계 완성</p>
</div>

<div class="grid grid-cols-4 gap-4 my-4">
<v-clicks>
  <div class="glass-card p-4.5 flex flex-col justify-between border-t-2 border-t-sky-400">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-sky-400 font-bold uppercase tracking-wider whitespace-nowrap">Session 01</span>
        <span class="i-carbon-data-volume text-sky-400 text-lg"></span>
      </div>
      <h3 class="font-bold text-white text-[15px] mt-1 mb-2 whitespace-nowrap">데이터와 ML·DL 원리</h3>
      <p class="text-xs text-white/70 leading-relaxed m-0">"양식장 빅데이터와 머신러닝·딥러닝의 본질"</p>
    </div>
    <div class="text-[11px] text-white/60 border-t border-white/10 pt-2.5 mt-3 leading-relaxed whitespace-nowrap">
      • 가두리 40만 행 데이터<br>• 규칙 기반 vs 머신러닝<br>• 딥러닝과 수중영상 인식
    </div>
  </div>

  <div class="glass-card p-4.5 flex flex-col justify-between border-t-2 border-t-indigo-400">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-indigo-400 font-bold uppercase tracking-wider whitespace-nowrap">Session 02</span>
        <span class="i-carbon-dashboard text-indigo-400 text-lg"></span>
      </div>
      <h3 class="font-bold text-white text-[15px] mt-1 mb-2 whitespace-nowrap">AI 4유형과 도입 검증</h3>
      <p class="text-xs text-white/70 leading-relaxed m-0">"해상가두리 AI 4유형과 정확도 97%의 함정"</p>
    </div>
    <div class="text-[11px] text-white/60 border-t border-white/10 pt-2.5 mt-3 leading-relaxed whitespace-nowrap">
      • 예측/인식/최적화/문서<br>• 경보 읽는 4대 원칙<br>• 재현율 vs 정밀도 체크
    </div>
  </div>

  <div class="glass-card p-4.5 flex flex-col justify-between border-t-2 border-t-amber-400">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-amber-400 font-bold uppercase tracking-wider whitespace-nowrap">Session 03</span>
        <span class="i-carbon-chat-bot text-amber-400 text-lg"></span>
      </div>
      <h3 class="font-bold text-white text-[15px] mt-1 mb-2 whitespace-nowrap">생성형 AI와 RCTF</h3>
      <p class="text-xs text-white/70 leading-relaxed m-0">"양식일지 자동화와 환각 잡는 RAG"</p>
    </div>
    <div class="text-[11px] text-white/60 border-t border-white/10 pt-2.5 mt-3 leading-relaxed whitespace-nowrap">
      • 확률적 문장생성 & 환각<br>• RCTF 지시문 & Few-Shot<br>• CSV 데이터 분석 & RAG
    </div>
  </div>

  <div class="glass-card p-4.5 flex flex-col justify-between border-t-2 border-t-emerald-400">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-emerald-400 font-bold uppercase tracking-wider whitespace-nowrap">Session 04</span>
        <span class="i-carbon-bot text-emerald-400 text-lg"></span>
      </div>
      <h3 class="font-bold text-white text-[15px] mt-1 mb-2 whitespace-nowrap">에이전트 & 로드맵</h3>
      <p class="text-xs text-white/70 leading-relaxed m-0">"아침 06시 자동 브리핑과 단계별 도입"</p>
    </div>
    <div class="text-[11px] text-white/60 border-t border-white/10 pt-2.5 mt-3 leading-relaxed whitespace-nowrap">
      • 챗봇 vs AI 에이전트<br>• 06:00 브리핑 시뮬레이션<br>• 4단계 현실적 도입 로드맵
    </div>
  </div>
</v-clicks>
</div>

<!--
[click] [강사] 1차시에서는 양식장에서 쏟아지는 데이터의 규모를 보고, 규칙 기반 자동화와 머신러닝·딥러닝이 어떻게 다른지 원리를 파악합니다.
[click] 2차시에서는 해상가두리 AI 4가지 유형과 경보 해석법, 그리고 공급업체의 '정확도 97%' 마케팅에 속지 않는 검증법을 배웁니다.
[click] 3차시에서는 생성형 AI로 거친 현장 메모를 깔끔한 양식일지로 바꾸고, 환각을 막는 RAG 오픈북 기법을 익힙니다.
[click] 4차시에서는 매일 아침 수질과 폐사를 스스로 분석해 보고하는 AI 에이전트와 현실적인 4단계 도입 로드맵을 확정합니다.
-->

---
layout: default
---
<!-- slide:03-Philosophy -->

<div class="mb-4">
  <h2 class="stage-title">스마트수산업 전문가의 3대 역할 정의</h2>
  <p class="stage-subtitle">“우리는 AI 개발자가 아니라, AI를 부리는 현장 최고 책임자입니다.”</p>
</div>

<div class="grid grid-cols-3 gap-5 my-4">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-3">
        <div class="w-9 h-9 rounded-xl bg-sky-500/20 text-sky-300 flex items-center justify-center font-bold text-sm">1</div>
        <span class="i-carbon-decision-tree text-sky-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mb-2">필요 기능의 판별</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        비싼 솔루션을 무작정 사는 것이 아니라, 우리 어장에 지금 필요한 것이 센서 예측인지, 영상 인식인지, 단순 일지 자동화인지 정확히 결정합니다.
      </p>
    </div>
    <div class="text-xs text-sky-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      도입 타당성 평가 역량
    </div>
  </div>

  <div class="glass-card border-emerald-500/20 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-3">
        <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-emerald-300 flex items-center justify-center font-bold text-sm">2</div>
        <span class="i-carbon-certificate-check text-emerald-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mb-2">결과의 올바른 해석</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        AI 경보와 예측 수치를 맹신하지 않고, 확률 신호의 의미를 파악하여 현장 육안 점검 및 실측값과 대조하여 최종 사육 조치를 내립니다.
      </p>
    </div>
    <div class="text-xs text-emerald-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      경보 해석 및 현장 검증 역량
    </div>
  </div>

  <div class="glass-card border-purple-500/20 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-3">
        <div class="w-9 h-9 rounded-xl bg-purple-500/20 text-purple-300 flex items-center justify-center font-bold text-sm">3</div>
        <span class="i-carbon-data-structured text-purple-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mb-2">학습 재료의 기록 관리</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        AI가 똑똑해지는 유일한 밑천은 현장의 정제된 데이터입니다. 동별 분리, 숫자 표기, 결측치 구분을 통해 고품질 사육 기록을 유지합니다.
      </p>
    </div>
    <div class="text-xs text-purple-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      데이터 자산화 관리 역량
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
현장 전문가의 3대 역할입니다.
무엇이 필요한지 고르고, 나온 결과를 의심하며 실측으로 검증하고, AI의 밥이 되는 기록을 깨끗하게 유지하는 것, 이것이 우리가 이번 과정을 통해 얻어갈 핵심 역량입니다.
-->

---
layout: center
class: text-center
---
<!-- slide:04-S01-01-Title -->

<div class="flex flex-col items-center justify-center">
  <span class="text-sky-400 font-mono text-sm tracking-widest uppercase mb-3">Session 01</span>
  <h2 class="text-5xl font-black text-white tracking-tight mb-4 leading-tight">
    스마트양식 데이터와<br />머신러닝·딥러닝의 원리
  </h2>
  <p class="text-white/75 text-lg font-light max-w-xl leading-relaxed">
    “양식장은 상시적인 빅데이터 생산자 : 규칙을 짜는 방식에서 데이터를 배우는 방식으로”
  </p>
</div>

<!--
[강사]
1차시를 시작하겠습니다.
해상가두리 양식장은 이미 거대한 빅데이터 공장입니다.
왜 사람이 수작업으로 규칙을 다 짤 수 없는지, 머신러닝과 딥러닝이 그 한계를 어떻게 돌파하는지 살펴보겠습니다.
-->

---
layout: default
---
<!-- slide:05-S01-02-Aquaculture3V -->

<div class="mb-3">
  <h2 class="stage-title">해상가두리 양식장 데이터의 규모 (빅데이터 3V)</h2>
  <p class="stage-subtitle">수질센서가 10분 간격으로 기록할 때 발생하는 데이터의 실체</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4">
<v-clicks>
  <div class="glass-card flex flex-col justify-between border-sky-500/20 p-5">
    <div>
      <div class="flex items-center gap-2 text-sm text-sky-300 font-bold mb-3">
        <span class="i-carbon-chart-line text-lg"></span>
        <span>데이터 생산량 시뮬레이션</span>
      </div>
      <div class="p-3.5 bg-black/40 rounded-xl text-xs space-y-2.5 font-mono">
        <div>• <strong>가두리 1개 동:</strong> 6회/시간 × 24시간 × 365일 ≈ <span class="text-sky-300 font-bold text-sm">연간 52,560 행</span></div>
        <div>• <strong>가두리 8개 동:</strong> 8개 동 운영 시 ≈ <span class="text-emerald-300 font-bold text-sm">연간 420,480 행</span></div>
      </div>
      <p class="text-xs text-white/75 mt-3 leading-relaxed m-0">
        연간 40만 행은 <strong>사람이 엑셀을 열고 눈으로 훑어서 패턴을 찾을 수 있는 한계를 완전히 넘어선 규모</strong>입니다.
      </p>
    </div>
    <div class="p-2.5 bg-white/5 rounded-lg text-xs text-white/85 border border-white/10 mt-3">
      👉 <strong>현장 분업의 원칙:</strong> 대량 데이터 판독은 <strong>AI</strong>가 수행하고, 사람은 사육 조치와 경영 판단을 내린다.
    </div>
  </div>

  <div class="glass-card border-indigo-500/20 bg-indigo-950/10 flex flex-col justify-between p-5">
    <div>
      <div class="flex items-center gap-2 text-sm text-indigo-300 font-bold mb-3">
        <span class="i-carbon-layers text-lg"></span>
        <span>양식장 빅데이터의 3V 특성</span>
      </div>
      <ul class="space-y-2.5 text-xs text-white/90 p-0 m-0 list-none">
        <li class="p-2.5 bg-black/40 rounded-lg flex items-start gap-2.5">
          <span class="i-carbon-data-volume text-sky-400 text-xl flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-sky-300 text-sm">1. 규모 (Volume):</strong><br>
            <span class="text-white/75 text-xs">8개 동 연간 40만 행, 수중영상 수만 프레임의 대용량</span>
          </div>
        </li>
        <li class="p-2.5 bg-black/40 rounded-lg flex items-start gap-2.5">
          <span class="i-carbon-meter-alt text-emerald-400 text-xl flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-emerald-300 text-sm">2. 속도 (Velocity):</strong><br>
            <span class="text-white/75 text-xs">10분 단위 실시간 연속 스트리밍 수집</span>
          </div>
        </li>
        <li class="p-2.5 bg-black/40 rounded-lg flex items-start gap-2.5">
          <span class="i-carbon-category text-purple-400 text-xl flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-purple-300 text-sm">3. 다양성 (Variety):</strong><br>
            <span class="text-white/75 text-xs">수온/DO 수치 + 수중영상 + 구어체 일지 텍스트 결합</span>
          </div>
        </li>
      </ul>
    </div>
    <div class="text-xs text-indigo-300 font-mono text-center mt-2.5 font-bold whitespace-nowrap">
      해상가두리는 이미 거대한 빅데이터 생산 공장입니다.
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
가두리 8개 동만 굴려도 1년에 40만 줄의 데이터가 쌓입니다.
사람이 이걸 일일이 볼 수 없습니다.
-->

---
layout: default
---
<!-- slide:06-S01-03-RecordRule -->

<div class="mb-3">
  <h2 class="stage-title">AI 도입의 성패를 가르는 기록의 4대 원칙</h2>
  <p class="stage-subtitle">“기록 방식이 AI 도입 가능 여부를 100% 결정합니다.”</p>
</div>

<div class="grid grid-cols-2 gap-5 my-3">
  <div class="glass-card border-rose-500/20 bg-rose-950/10 p-4.5 flex flex-col justify-between">
    <div>
      <div class="text-sm text-rose-300 font-bold mb-2.5 flex items-center gap-2">
        <span class="i-carbon-close-filled text-rose-400 text-base"></span>
        <span>❌ AI가 절대 읽을 수 없는 불량 기록</span>
      </div>
      <ul class="space-y-2.5 text-xs text-white/80 p-0 m-0 list-none">
        <li class="p-2.5 bg-black/40 rounded-lg">
          <strong class="text-rose-300 text-[13px]">"오늘 A동 폐사 좀 많았음"</strong><br>
          <span class="text-white/60 text-xs">→ 주관적 서술형 표현은 머신러닝 학습 불가</span>
        </li>
        <li class="p-2.5 bg-black/40 rounded-lg">
          <strong class="text-rose-300 text-[13px]">"전체 가두리 합산 폐사 150마리"</strong><br>
          <span class="text-white/60 text-xs">→ 어느 동에서 터졌는지 위치 식별 불가</span>
        </li>
        <li class="p-2.5 bg-black/40 rounded-lg">
          <strong class="text-rose-300 text-[13px]">"측정 안 한 날은 그냥 0으로 적음"</strong><br>
          <span class="text-white/60 text-xs">→ 수온 0℃로 오인식하여 모델 왜곡 유발</span>
        </li>
      </ul>
    </div>
  </div>

  <div class="glass-card border-emerald-500/20 bg-emerald-950/10 p-4.5 flex flex-col justify-between">
    <div>
      <div class="text-sm text-emerald-300 font-bold mb-2.5 flex items-center gap-2">
        <span class="i-carbon-checkmark-filled text-emerald-400 text-base"></span>
        <span>⭕ AI가 즉시 학습 가능한 표준 기록 4원칙</span>
      </div>
      <ul class="space-y-2 text-xs text-white/90 p-0 m-0 list-none">
        <li class="p-2 bg-black/40 rounded-lg flex items-start gap-2">
          <span class="i-carbon-grid text-emerald-400 text-base flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-emerald-300 text-xs">1. 가두리 동별 분리 기록:</strong>
            <span class="text-white/75 text-[11px] block">A-01, A-02 가두리별로 발생 위치를 명확히 분리</span>
          </div>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-start gap-2">
          <span class="i-carbon-string-integer text-emerald-400 text-base flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-emerald-300 text-xs">2. 정량 수치 표기:</strong>
            <span class="text-white/75 text-[11px] block">"폐사 42미", "급이 120kg" 숫자로 정확히 기록</span>
          </div>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-start gap-2">
          <span class="i-carbon-rule text-emerald-400 text-base flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-emerald-300 text-xs">3. 결측치(빈칸) 구분:</strong>
            <span class="text-white/75 text-[11px] block">측정하지 못한 값은 0이 아닌 빈칸(결측) 처리</span>
          </div>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-start gap-2">
          <span class="i-carbon-table-split text-emerald-400 text-base flex-shrink-0 mt-0.5"></span>
          <div>
            <strong class="text-emerald-300 text-xs">4. 1행 1관측 체계:</strong>
            <span class="text-white/75 text-[11px] block">셀 병합 금지, 시점별 독립 행 유지</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>

<!--
[강사]
서술형으로 적거나 셀을 병합해 버리면 아무리 비싼 AI도 쓸모가 없습니다.
동별로, 숫자로, 빈칸을 구분해서 적는 것이 AI 양식의 출발점입니다.
-->

---
layout: default
---
<!-- slide:07-S01-04-DataInventory -->

<div class="mb-3">
  <h2 class="stage-title">우리 양식장 데이터 인벤토리 점검표</h2>
  <p class="stage-subtitle">알고리즘 선택보다 먼저 우리 어장에 어떤 데이터가 축적되어 있는지 파악해야 합니다.</p>
</div>

<div class="glass-card p-3.5 my-3 text-xs text-white/85">
  <table class="w-full text-left border-collapse text-xs">
    <thead>
      <tr class="border-b border-white/20 text-white/50 text-xs whitespace-nowrap">
        <th class="py-2 px-3">데이터 항목</th>
        <th class="py-2 px-3">자동 수집</th>
        <th class="py-2 px-3">수기 기록</th>
        <th class="py-2 px-3">AI 활용 가능성 & 목적</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/10">
      <tr class="hover:bg-white/5">
        <td class="py-2.5 px-3 font-bold text-white text-sm whitespace-nowrap">수온 · DO · 염분</td>
        <td class="py-2.5 px-3 text-sky-300 font-mono whitespace-nowrap">센서 (10분)</td>
        <td class="py-2.5 px-3 text-white/50">-</td>
        <td class="py-2.5 px-3 text-emerald-300 font-medium">수질 이상탐지 및 고수온 조기 경보</td>
      </tr>
      <tr class="hover:bg-white/5">
        <td class="py-2.5 px-3 font-bold text-white text-sm whitespace-nowrap">급이량 (동별)</td>
        <td class="py-2.5 px-3 text-white/50">-</td>
        <td class="py-2.5 px-3 text-amber-300 font-mono whitespace-nowrap">일지 (kg)</td>
        <td class="py-2.5 px-3 text-emerald-300 font-medium">사료 계수(FCR) 및 성장 곡선 분석</td>
      </tr>
      <tr class="hover:bg-white/5">
        <td class="py-2.5 px-3 font-bold text-white text-sm whitespace-nowrap">폐사수 (동별·일별)</td>
        <td class="py-2.5 px-3 text-white/50">-</td>
        <td class="py-2.5 px-3 text-amber-300 font-mono whitespace-nowrap">수거 기록</td>
        <td class="py-2.5 px-3 text-rose-300 font-medium font-bold">폐사 위험 예측 모델의 정답(Label) 데이터</td>
      </tr>
      <tr class="hover:bg-white/5">
        <td class="py-2.5 px-3 font-bold text-white text-sm whitespace-nowrap">수중 영상</td>
        <td class="py-2.5 px-3 text-sky-300 font-mono whitespace-nowrap">수중 카메라</td>
        <td class="py-2.5 px-3 text-white/50">-</td>
        <td class="py-2.5 px-3 text-purple-300 font-medium">딥러닝 어체 계수, 체중 추정, 질병 탐지</td>
      </tr>
      <tr class="hover:bg-white/5">
        <td class="py-2.5 px-3 font-bold text-white text-sm whitespace-nowrap">작업일지 메모</td>
        <td class="py-2.5 px-3 text-white/50">-</td>
        <td class="py-2.5 px-3 text-amber-300 font-mono whitespace-nowrap">구어체 메모</td>
        <td class="py-2.5 px-3 text-amber-300 font-medium">생성형 AI 일지 자동 정리 및 RAG 재료</td>
      </tr>
    </tbody>
  </table>
</div>

<!--
[강사]
인벤토리를 보시면, 폐사수 기록이 있어야 폐사 예측 AI를 만들 수 있습니다.
정답 데이터가 없으면 어떤 비싼 AI도 돌아가지 않습니다.
-->

---
layout: default
---
<!-- slide:08-S01-05-DataPipeline -->

<div class="mb-3">
  <h2 class="stage-title">스마트양식 4단계 데이터 파이프라인</h2>
  <p class="stage-subtitle">AI는 독립된 장치가 아니라 센싱부터 제어까지 이어지는 데이터 사슬의 분석 단계입니다.</p>
</div>

<DataPipelineFlow />

<div class="p-2.5 bg-white/5 rounded-xl text-xs text-white/85 border border-white/10 text-center mt-3">
  💡 <strong>교재 제12·13·14장과의 연계:</strong> 앞단의 수집·저장이 부실하면 AI 분석이 불가능하고, 뒷단의 제어 시스템이 없으면 AI 분석 결과가 사육 조치로 이어지지 않습니다.
</div>

<!--
[강사]
AI만 산다고 스마트양식이 되지 않습니다.
센서가 측정하고, IoT로 모아서, AI가 분석하고, 사람이 차광막과 산소를 제어하는 사슬 전체가 맞물려야 합니다.
-->

---
layout: default
---
<!-- slide:09-S01-06-HierarchyImage -->

<div class="mb-3">
  <h2 class="stage-title">인공지능 vs 머신러닝 vs 딥러닝 포함 관계</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/ai-ml-dl-hierarchy.png" alt="인공지능 머신러닝 딥러닝 포함 관계" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  인공지능(AI)이라는 가장 큰 우산 아래 머신러닝(ML)이 있고, 머신러닝 안에 딥러닝(DL)이 존재합니다.
</p>

<!--
[강사]
교재의 첫 번째 핵심 그림입니다.
인공지능 안에 머신러닝이 있고, 머신러닝 안에 딥러닝이 있습니다.
-->

---
layout: default
---
<!-- slide:10-S01-07-HierarchyDesc -->

<div class="mb-3">
  <h2 class="stage-title">AI · ML · DL 3대 개념의 현장 의미</h2>
  <p class="stage-subtitle">인공지능의 큰 틀에서 머신러닝과 딥러닝이 맡는 역할의 명확한 구분</p>
</div>

<div class="grid grid-cols-3 gap-4 my-4">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-4.5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-sky-300 font-bold uppercase tracking-wider whitespace-nowrap">Concept 01</span>
        <span class="i-carbon-machine-learning-model text-sky-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mt-1.5 mb-2 whitespace-nowrap">인공지능 (AI)</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        인간이 가지는 지적 능력(학습, 추론, 인지)을 컴퓨터를 통해 구현하는 가장 포괄적인 기술 범주
      </p>
    </div>
    <div class="text-xs text-sky-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      현장 적용: 스마트양식 자동화 전체
    </div>
  </div>

  <div class="glass-card border-indigo-500/20 p-4.5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-indigo-300 font-bold uppercase tracking-wider whitespace-nowrap">Concept 02</span>
        <span class="i-carbon-chart-multitype text-indigo-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mt-1.5 mb-2 whitespace-nowrap">머신러닝 (ML)</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        사람이 규칙을 직접 코딩하지 않고, 축적된 표 형태 데이터에서 컴퓨터가 스스로 위험 패턴과 규칙을 도출
      </p>
    </div>
    <div class="text-xs text-indigo-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      현장 적용: 수온/DO 기반 폐사 조기 예측
    </div>
  </div>

  <div class="glass-card border-purple-500/20 p-4.5 flex flex-col justify-between">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono text-purple-300 font-bold uppercase tracking-wider whitespace-nowrap">Concept 03</span>
        <span class="i-carbon-network-4 text-purple-400 text-xl"></span>
      </div>
      <h3 class="text-base font-bold text-white mt-1.5 mb-2 whitespace-nowrap">딥러닝 (DL)</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        인공신경망을 다층으로 쌓아, 수중영상 등 복잡한 비정형 데이터에서 특징을 스스로 추출하고 판별
      </p>
    </div>
    <div class="text-xs text-purple-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      현장 적용: 수중 어체 계수 & 질병 탐지
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
수온 센서 데이터는 머신러닝으로 충분하고, 수중 카메라는 딥러닝입니다.
-->

---
layout: default
---
<!-- slide:11-S01-08-RuleVsMLImage -->

<div class="mb-3">
  <h2 class="stage-title">지금까지의 자동화(규칙) vs 머신러닝(학습)</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/rule-vs-ml.png" alt="규칙 기반 vs 머신러닝" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  과거에는 사람이 규칙을 주입했지만, 머신러닝은 3년 치 기록 데이터를 주면 컴퓨터가 규칙 모델을 만듭니다.
</p>

<!--
[강사]
교재의 두 번째 핵심 다이어그램입니다.
규칙을 만드는 주체가 사람에서 데이터로 바뀌었습니다.
-->

---
layout: default
---
<!-- slide:12-S01-09-RuleBasedLimit -->

<div class="mb-3">
  <h2 class="stage-title">기존 규칙 기반(Rule-based) 경보의 한계</h2>
  <p class="stage-subtitle">단일 조건문 방식의 경보가 실제 현장의 복합 재난을 막지 못하는 이유</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4">
<v-clicks>
  <div class="glass-card border-rose-500/20 bg-rose-950/15 p-5 flex flex-col justify-between">
    <div>
      <div class="text-sm text-rose-300 font-bold mb-3 flex items-center gap-1.5">
        <span class="i-carbon-warning-alt text-base"></span>
        <span>단순 조건식 경보의 현실</span>
      </div>
      <div class="p-3 bg-black/40 rounded-xl text-xs font-mono text-rose-300 mb-3 whitespace-nowrap">
        IF 용존산소(DO) &lt; 4.0 mg/L THEN 비상 경보 발령
      </div>
      <p class="text-xs text-white/75 leading-relaxed m-0">
        조건이 단순할 때는 명확하지만, 실제 대량 폐사는 <strong>수온 27℃ 이상 + 조류 정체 + 사료 급이 직후 + 높은 사육밀도</strong> 등 수십 개 변수가 복합적으로 중첩되어 발생합니다.
      </p>
    </div>
    <div class="text-xs text-rose-400 font-bold border-t border-rose-500/20 pt-2.5 mt-3 whitespace-nowrap">
      결과: 조건이 늘어날수록 모든 조합의 예외 규칙을 작성할 수 없음
    </div>
  </div>

  <div class="glass-card border-emerald-500/20 bg-emerald-950/15 p-5 flex flex-col justify-between">
    <div>
      <div class="text-sm text-emerald-300 font-bold mb-3 flex items-center gap-1.5">
        <span class="i-carbon-idea text-base"></span>
        <span>머신러닝의 역전 발상</span>
      </div>
      <div class="p-3 bg-black/40 rounded-xl text-xs font-mono text-emerald-300 mb-3 whitespace-nowrap">
        과거 3년 센서 기록 + 폐사 여부 결과 ➔ 복합 위험 패턴 도출
      </div>
      <p class="text-xs text-white/85 leading-relaxed m-0">
        사람이 일일이 if문을 작성하지 않아도, 컴퓨터가 과거 폐사 사례들의 공통적인 복합 환경 패턴을 스스로 학습하여 위험 모델을 생성합니다.
      </p>
    </div>
    <div class="text-xs text-emerald-300 font-bold border-t border-emerald-500/20 pt-2.5 mt-3 whitespace-nowrap">
      효과: 사람이 미처 생각하지 못한 다차원 이상 징후 조기 포착
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
단순한 기준치는 사람도 짭니다.
하지만 실제 대량 폐사는 수온과 조류와 사료가 얽혀 터집니다.
이 복합 규칙을 찾는 것이 머신러닝입니다.
-->

---
layout: default
---
<!-- slide:13-S01-10-MachineLearning -->

<div class="mb-3">
  <h2 class="stage-title">학습(Learning)의 실체 : "오차의 최소화"</h2>
  <p class="stage-subtitle">모델은 정답을 ‘아는’ 것이 아니라, 오차가 가장 작은 답을 ‘선택’하는 것입니다.</p>
</div>

<div class="grid grid-cols-4 gap-3.5 my-4">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-4 text-center">
    <span class="text-[11px] font-mono text-sky-300 font-bold whitespace-nowrap">STEP 01</span>
    <h4 class="text-sm font-bold text-white mt-1.5 mb-1.5 whitespace-nowrap">예측값 산출</h4>
    <p class="text-xs text-white/65 m-0 leading-relaxed">현재 모델이 폐사 위험 확률을 계산</p>
  </div>
  <div class="glass-card border-sky-500/20 p-4 text-center">
    <span class="text-[11px] font-mono text-sky-300 font-bold whitespace-nowrap">STEP 02</span>
    <h4 class="text-sm font-bold text-white mt-1.5 mb-1.5 whitespace-nowrap">오차(Error) 측정</h4>
    <p class="text-xs text-white/65 m-0 leading-relaxed">실제 폐사 발생 여부와 차이 계산</p>
  </div>
  <div class="glass-card border-sky-500/20 p-4 text-center">
    <span class="text-[11px] font-mono text-sky-300 font-bold whitespace-nowrap">STEP 03</span>
    <h4 class="text-sm font-bold text-white mt-1.5 mb-1.5 whitespace-nowrap">가중치 미세 조정</h4>
    <p class="text-xs text-white/65 m-0 leading-relaxed">오차가 줄어드는 방향으로 내부 값 수정</p>
  </div>
  <div class="glass-card border-emerald-500/20 p-4 text-center">
    <span class="text-[11px] font-mono text-emerald-300 font-bold whitespace-nowrap">STEP 04</span>
    <h4 class="text-sm font-bold text-white mt-1.5 mb-1.5 whitespace-nowrap">반복 최적화</h4>
    <p class="text-xs text-white/65 m-0 leading-relaxed">전체 데이터에 대해 수천 번 반복 완료</p>
  </div>
</v-clicks>
</div>

<div class="grid grid-cols-2 gap-4 text-xs mt-3">
  <div class="p-3 bg-rose-950/20 border border-rose-500/20 rounded-xl">
    <strong class="text-rose-300 text-sm">실무적 함의 1:</strong>
    <span class="text-white/75 text-xs leading-relaxed block mt-1">오차가 최소인 답을 고를 뿐이므로 항상 확률적 오류 가능성이 존재함</span>
  </div>
  <div class="p-3 bg-amber-950/20 border border-amber-500/20 rounded-xl">
    <strong class="text-amber-300 text-sm">실무적 함의 2:</strong>
    <span class="text-white/75 text-xs leading-relaxed block mt-1">과거 데이터에 한 번도 없었던 이례적 냉수대나 태풍은 예측 불가</span>
  </div>
</div>

<!--
[강사]
머신러닝은 마법이 아니라 오차를 줄여나가는 계산기입니다.
따라서 과거 기록에 없던 사건은 맞출 수 없습니다.
-->

---
layout: default
---
<!-- slide:14-S01-11-MLvsDLImage -->

<div class="mb-3">
  <h2 class="stage-title">머신러닝 vs 딥러닝 : 특징 추출 주체의 차이</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/ml-vs-dl.png" alt="머신러닝 딥러닝 차이점" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  머신러닝은 사람이 수온/DO 특징을 지정하지만, 딥러닝은 인공신경망이 영상에서 궤양/지느러미 특징을 스스로 찾습니다.
</p>

<!--
[강사]
교재의 세 번째 핵심 그림입니다.
카메라 영상 속 물고기 특징을 컴퓨터가 스스로 추출합니다.
-->

---
layout: default
---
<!-- slide:15-S01-12-DeepLearningVision -->

<div class="mb-3">
  <h2 class="stage-title">딥러닝이 여는 수중영상 인식 4대 기능</h2>
  <p class="stage-subtitle">수면 아래를 직접 보기 어려운 해상가두리 환경에서 딥러닝이 제공하는 실무 가치</p>
</div>

<div class="grid grid-cols-2 gap-4 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-4">
    <div class="flex items-center gap-2 text-sky-300 font-bold text-sm mb-1.5">
      <span class="i-carbon-user-identification text-lg"></span>
      <span class="whitespace-nowrap">1. 어체 개체수 계수 (Counting)</span>
    </div>
    <p class="text-white/75 text-xs leading-relaxed m-0">
      입식 시 마릿수 자동 확인 및 매일 폐사 누계 검증으로 정확한 사육 밀도 유지
    </p>
  </div>

  <div class="glass-card border-indigo-500/20 p-4">
    <div class="flex items-center gap-2 text-indigo-300 font-bold text-sm mb-1.5">
      <span class="i-carbon-scale text-lg"></span>
      <span class="whitespace-nowrap">2. 체장 · 체중 비접촉 추정</span>
    </div>
    <p class="text-white/75 text-xs leading-relaxed m-0">
      스트레스를 주는 뜰채 샘플링 없이 카메라 영상만으로 어체 성장 속도 실시간 추정
    </p>
  </div>

  <div class="glass-card border-purple-500/20 p-4">
    <div class="flex items-center gap-2 text-purple-300 font-bold text-sm mb-1.5">
      <span class="i-carbon-warning-alt text-lg"></span>
      <span class="whitespace-nowrap">3. 체표 궤양 · 지느러미 질병 판별</span>
    </div>
    <p class="text-white/75 text-xs leading-relaxed m-0">
      넙치 쿠도아충, 조피볼락 아가미 부식 등 체표 이상 증상을 육안 확인 전 조기 탐지
    </p>
  </div>

  <div class="glass-card border-emerald-500/20 p-4">
    <div class="flex items-center gap-2 text-emerald-300 font-bold text-sm mb-1.5">
      <span class="i-carbon-restaurant text-lg"></span>
      <span class="whitespace-nowrap">4. 사료 섭이 행동 분석</span>
    </div>
    <p class="text-white/75 text-xs leading-relaxed m-0">
      물고기가 사료를 먹는 활성도를 분석하여 급이 중단 시점을 판단 → 사료비 15% 이상 절감
    </p>
  </div>
</v-clicks>
</div>

<!--
[강사]
수중 카메라로 뜰채 없이 몸무게를 재고, 궤양을 찾아내며, 사료를 다 먹었는지 보고 급이를 멈춥니다.
-->

---
layout: default
---
<!-- slide:16-S01-13-SpeciesMatrix -->

<div class="mb-3">
  <h2 class="stage-title">주요 어종별 스마트양식 AI 적합도</h2>
  <p class="stage-subtitle">어종의 사육 형태와 취약 환경에 따라 최우선 AI 과제가 달라집니다.</p>
</div>

<AquacultureMatrix />

<div class="grid grid-cols-2 gap-4 text-xs mt-3">
  <div class="p-3 bg-white/5 rounded-xl border border-white/10">
    <strong class="text-sky-300 text-sm whitespace-nowrap">해상가두리 (조피볼락/돔):</strong>
    <span class="text-white/75 text-xs mt-1 block leading-relaxed">자연 해역 노출로 수온 급변·적조·저산소 조기 경보가 생존의 핵심</span>
  </div>
  <div class="p-3 bg-white/5 rounded-xl border border-white/10">
    <strong class="text-purple-300 text-sm whitespace-nowrap">육상수조 (넙치):</strong>
    <span class="text-white/75 text-xs mt-1 block leading-relaxed">수조 조명과 시야 확보가 유리하여 수중영상 어체 계수와 섭이 분석 우선 도입</span>
  </div>
</div>

<!--
[강사]
조피볼락 가두리는 여름철 고수온 조기 경보가 최우선이고,
넙치 육상수조는 사료 낭비를 줄이는 섭이 행동 영상 분석이 핵심입니다.
-->

---
layout: default
---
<!-- slide:17-S01-14-SessionSummary -->

<div class="mb-4">
  <h2 class="stage-title">1차시 핵심 내용 총정리</h2>
</div>

<div class="max-w-3xl mx-auto glass-card p-6 my-6 space-y-4 text-sm text-white/90">
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-sky-500/20 text-sky-300 flex items-center justify-center text-sm font-bold flex-shrink-0">1</span>
    <p class="leading-relaxed m-0"><strong>가두리 양식장은 상시 빅데이터 생산자:</strong> 8개 동 연간 40만 행 데이터는 AI와 분업해야 관리 가능</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-indigo-500/20 text-indigo-300 flex items-center justify-center text-sm font-bold flex-shrink-0">2</span>
    <p class="leading-relaxed m-0"><strong>기록의 4대 원칙:</strong> 동별 분리, 숫자 기록, 결측 구분, 1행 1관측이 지켜져야 AI가 성립함</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-purple-500/20 text-purple-300 flex items-center justify-center text-sm font-bold flex-shrink-0">3</span>
    <p class="leading-relaxed m-0"><strong>머신러닝 vs 딥러닝:</strong> 센서 수치는 머신러닝으로 충분, 카메라 영상이 개입할 때 딥러닝 도입</p>
  </div>
</div>

<!--
[강사]
1차시 요약입니다.
기록이 없으면 AI도 없습니다.
-->

---
layout: center
class: text-center
---
<!-- slide:18-S02-01-Title -->

<div class="flex flex-col items-center justify-center">
  <span class="text-indigo-400 font-mono text-sm tracking-widest uppercase mb-3">Session 02</span>
  <h2 class="text-5xl font-black text-white tracking-tight mb-4 leading-tight">
    해상가두리 AI 4유형과<br />경보 해석 & 솔루션 도입 검증
  </h2>
  <p class="text-white/75 text-lg font-light max-w-xl leading-relaxed">
    “AI 경보 올바르게 읽는 4원칙과 공급업체 정확도 97%의 함정 파헤치기”
  </p>
</div>

<!--
[강사]
2차시를 시작하겠습니다.
2차시에서는 해상가두리 양식장에서 AI가 활약하는 4가지 유형 지도를 확인하고,
위험 경보가 떴을 때의 행동 요령, 그리고 솔루션 도입 시 업체의 과장 광고를 검증하는 체크리스트를 살펴보겠습니다.
-->

---
layout: default
---
<!-- slide:19-S02-02-4TypesMap -->

<div class="mb-3">
  <h2 class="stage-title">해상가두리 양식장의 AI 활용 4유형 지도</h2>
  <p class="stage-subtitle">어장 인프라와 목적에 따른 4대 AI 활용 영역의 분류</p>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/aquaculture-4types.png" alt="해상가두리 AI 활용 4유형" class="rounded-2xl max-h-80 w-auto object-contain shadow-2xl select-none" />
</div>

<div class="grid grid-cols-4 gap-3 text-xs text-center text-white/80 mt-2">
<v-clicks>
  <div class="p-2 bg-sky-950/20 border border-sky-500/20 rounded-lg font-medium whitespace-nowrap">① 예측형: 미리 아는 것</div>
  <div class="p-2 bg-indigo-950/20 border border-indigo-500/20 rounded-lg font-medium whitespace-nowrap">② 인식형: 보이지 않는 것 확인</div>
  <div class="p-2 bg-emerald-950/20 border border-emerald-500/20 rounded-lg font-medium whitespace-nowrap">③ 최적화형: 최적 선택 도출</div>
  <div class="p-2 bg-amber-950/20 border border-amber-500/20 rounded-lg font-medium whitespace-nowrap">④ 문서·소통: 즉시 도입 가능</div>
</v-clicks>
</div>

<!--
[강사]
교재에 실린 해상가두리 AI 4유형 지도입니다.
①~③은 센서와 카메라 장비가 필요하지만,
④ 문서·소통형은 오늘 당장 스마트폰만 있으면 시작할 수 있습니다.
-->

---
layout: default
---
<!-- slide:20-S02-03-4TypesDetail -->

<div class="mb-3">
  <h2 class="stage-title">해상가두리 AI 4유형 상세 인터랙션</h2>
  <p class="stage-subtitle">각 탭을 클릭하여 인프라 요건과 실무적 가치를 비교하세요.</p>
</div>

<Aquaculture4Types />

<!--
[강사]
탭을 하나씩 눌러보며 우리 양식장에 지금 당장 필요한 기능이 무엇인지 확인해 보세요.
-->

---
layout: default
---
<!-- slide:21-S02-04-PredictiveValue -->

<div class="mb-3">
  <h2 class="stage-title">예측형 AI의 본질: "대응 골든타임 확보"</h2>
  <p class="stage-subtitle">수온 상승과 실제 대량 폐사 폭발 사이의 시차(Time-lag)를 활용한 선제 방어</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4">
<v-clicks>
  <div class="glass-card p-5 flex flex-col justify-between border-sky-500/20">
    <div>
      <div class="text-sm text-sky-300 font-bold mb-3 flex items-center gap-1.5">
        <span class="i-carbon-time text-base"></span>
        <span>수온 상승과 폐사 발생의 시차 (Time-lag)</span>
      </div>
      <div class="p-3.5 bg-black/40 rounded-xl text-xs space-y-2 text-white/85 font-mono">
        <div>• <strong>8월 1일:</strong> 표층 수온 27.5℃ 돌파 (고수온 진입)</div>
        <div>• <strong>8월 2~3일:</strong> 스트레스 누적, 어체 면역력 저하</div>
        <div>• <strong>8월 5일:</strong> <span class="text-rose-400 font-bold">A-03 가두리 대량 폐사 폭발 (41미)</span></div>
      </div>
      <p class="text-xs text-white/75 mt-3 leading-relaxed m-0">
        고수온이 온 당일 바로 죽는 것이 아닙니다. <strong>폐사는 수일의 시차를 두고 폭발</strong>합니다. AI 예측의 가치는 적중률 그 자체보다 <strong>"1~2일 앞서 인지하는 대응 시간 확보"</strong>에 있습니다.
      </p>
    </div>
    <div class="p-2.5 bg-sky-950/30 border border-sky-500/20 rounded-lg text-xs text-sky-300 font-medium whitespace-nowrap">
      ⏱️ 1~2일 전 사전 인지 ➔ 차광막 하강, 액화산소 비축, 급이 감량 완료!
    </div>
  </div>

  <div class="glass-card p-5 flex flex-col justify-between border-emerald-500/20 bg-emerald-950/10">
    <div>
      <div class="text-sm text-emerald-300 font-bold mb-3 flex items-center gap-1.5">
        <span class="i-carbon-task-complete text-base"></span>
        <span>현장 선제 대응 행동 시나리오</span>
      </div>
      <ul class="space-y-2.5 text-xs text-white/90 p-0 m-0 list-none">
        <li class="p-2 bg-black/40 rounded-lg flex items-center gap-2">
          <span class="i-carbon-sun text-amber-400 text-base flex-shrink-0"></span>
          <span><strong class="text-emerald-300">1. 차광막 전면 하강:</strong> 직사광선 차단 및 표층 수온 완화</span>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-center gap-2">
          <span class="i-carbon-cut text-sky-400 text-base flex-shrink-0"></span>
          <span><strong class="text-emerald-300">2. 사료 급이 50% 감량 / 절식:</strong> 소화 대사열 발생 억제</span>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-center gap-2">
          <span class="i-carbon-chemistry text-teal-400 text-base flex-shrink-0"></span>
          <span><strong class="text-emerald-300">3. 액화산소 라인 점검:</strong> 야간 저산소 대비 토출 밸브 개방</span>
        </li>
        <li class="p-2 bg-black/40 rounded-lg flex items-center gap-2">
          <span class="i-carbon-flash text-purple-400 text-base flex-shrink-0"></span>
          <span><strong class="text-emerald-300">4. 비상 발전기 시운전:</strong> 정전 대비 유류 잔량 확인</span>
        </li>
      </ul>
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
고수온이 왔다고 물고기가 그날 바로 다 죽지 않습니다.
수온이 오르고 2~3일간 스트레스가 쌓이다가 4~5일 차에 대량 폐사가 터집니다.
AI가 2일 전에만 알려줘도 차광막을 내리고 사료를 줄여 폐사를 막을 수 있습니다.
-->

---
layout: default
---
<!-- slide:22-S02-05-PredictiveRules -->

<div class="mb-3">
  <h2 class="stage-title">예측 운용의 4대 철칙</h2>
  <p class="stage-subtitle">AI 예측 수치를 현장 사육 조치로 연결할 때 반드시 지켜야 할 원칙</p>
</div>

<div class="grid grid-cols-2 gap-4 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-4">
    <strong class="text-sky-300 text-sm whitespace-nowrap">1. 예측값은 점이 아니라 '범위'로 해석</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      "3일 후 27.2℃"라는 예측은 정확히 27.2℃가 된다는 뜻이 아니라, <strong>±1.5℃ 구간(25.7~28.7℃)의 상승 가능성</strong>이 높다는 의미로 해석해야 합니다.
    </p>
  </div>

  <div class="glass-card border-emerald-500/20 p-4">
    <strong class="text-emerald-300 text-sm whitespace-nowrap">2. 조치의 최종 근거는 '현장 실측값'</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      AI 예측은 준비를 앞당기는 용도이며, <strong>약품 투여나 조기 출하 같은 비가역적 조치는 반드시 휴대용 측정기와 육안 실측</strong>을 거친 후 결정합니다.
    </p>
  </div>

  <div class="glass-card border-amber-500/20 p-4">
    <strong class="text-amber-300 text-sm whitespace-nowrap">3. 과거에 없던 이례적 사건 주의</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      유례없는 급격한 냉수대 유입, 초대형 태풍 등 <strong>과거 학습 데이터에 존재하지 않았던 극한 환경에서는 예측 성능이 급락</strong>함을 상시 인지합니다.
    </p>
  </div>

  <div class="glass-card border-purple-500/20 p-4">
    <strong class="text-purple-300 text-sm whitespace-nowrap">4. 연 1회 이상 모델 재평가 요구</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      어장 주변 해류나 사육 밀도가 변하면 모델 유효성도 저하되므로, <strong>공급업체에 최신 1년 데이터로 재학습(Re-training)</strong>을 요구해야 합니다.
    </p>
  </div>
</v-clicks>
</div>

<!--
[강사]
예측은 범위로 보고, 최종 조치는 실측으로 검증합니다.
-->

---
layout: default
---
<!-- slide:23-S02-06-AlertDosAndDonts -->

<div class="mb-3">
  <h2 class="stage-title">AI 위험 경보 발생 시 올바른 해석과 행동</h2>
</div>

<AlertReadingGuide />

<!--
[강사]
경보가 울렸다고 당황해서 확인도 안 하고 약품을 붓거나 조기 출하를 해버리면 안 됩니다.
경보는 '현장 육안 점검을 나가라는 알람'입니다.
-->

---
layout: default
---
<!-- slide:24-S02-07-AccuracyTrap -->

<div class="mb-3">
  <h2 class="stage-title">공급업체 "정확도 97%"의 치명적인 함정</h2>
  <p class="stage-subtitle">“100일 중 위험일이 3일뿐이면, 365일 안전하다고만 답해도 정확도는 97%입니다!”</p>
</div>

<AccuracyTrapCalc />

<!--
[강사]
업체 영업사원이 "저희 폐사 예측 AI는 정확도가 97%입니다"라고 하면 속으시면 안 됩니다.
100일 중 폐사 나는 날이 3일뿐이면, 1년 내내 안전하다고만 답해도 정확도는 97%입니다.
-->

---
layout: default
---
<!-- slide:25-S02-08-RecallVsPrecision -->

<div class="mb-3">
  <h2 class="stage-title">수산양식 최우선 지표: 재현율 vs 정밀도</h2>
  <p class="stage-subtitle">대량 폐사 방지를 위해 수산 분야에서 재현율(Recall)을 최우선으로 검증해야 하는 이유</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-emerald-500/30 bg-emerald-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="text-emerald-300 font-bold text-base mb-1.5 flex items-center gap-2">
        <span class="i-carbon-target text-xl text-emerald-400"></span>
        <span class="whitespace-nowrap">재현율 (Recall) ⭐ 수산양식 최우선 지표</span>
      </div>
      <div class="text-xs text-white/60 mb-3 font-mono whitespace-nowrap">
        공식: [AI가 잡은 위험일] / [실제 위험일 전체]
      </div>
      <div class="p-3 bg-black/40 rounded-xl text-emerald-200 text-xs space-y-1.5 leading-relaxed">
        <div>• <strong>의미:</strong> 진짜 위험한 10번 중 몇 번을 경보로 울렸는가?</div>
        <div>• <strong>낮으면:</strong> <strong>위험을 놓침 → 대량 폐사 직격타!</strong></div>
      </div>
    </div>
    <div class="mt-3 text-xs text-emerald-300 font-bold border-t border-emerald-500/20 pt-2.5 whitespace-nowrap">
      폐사·질병 예측 과제에서는 재현율이 최소 90% 이상이어야 함
    </div>
  </div>

  <div class="glass-card border-sky-500/30 bg-sky-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="text-sky-300 font-bold text-base mb-1.5 flex items-center gap-2">
        <span class="i-carbon-filter text-xl text-sky-400"></span>
        <span class="whitespace-nowrap">정밀도 (Precision)</span>
      </div>
      <div class="text-xs text-white/60 mb-3 font-mono whitespace-nowrap">
        공식: [진짜 위험했던 경보] / [AI가 울린 전체 경보]
      </div>
      <div class="p-3 bg-black/40 rounded-xl text-sky-200 text-xs space-y-1.5 leading-relaxed">
        <div>• <strong>의미:</strong> 울린 10번의 경보 중 몇 번이 진짜였는가?</div>
        <div>• <strong>낮으면:</strong> <strong>헛경보 누적 → 현장 인력 피로 및 불신</strong></div>
      </div>
    </div>
    <div class="mt-3 text-xs text-sky-300 font-bold border-t border-sky-500/20 pt-2.5 whitespace-nowrap">
      비용이 많이 드는 조기 출하, 대규모 이동 판단에서 중시
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
위험을 놓쳤을 때의 대량 폐사 피해가 훨씬 크기 때문에, 수산양식에서는 무조건 재현율(Recall)을 1순위로 봅니다.
-->

---
layout: default
---
<!-- slide:26-S02-09-Finetuning -->

<div class="mb-3">
  <h2 class="stage-title">"수산 특화 AI"의 실체 : 사전학습 vs 파인튜닝</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/pretraining-vs-finetuning.png" alt="사전학습과 파인튜닝 구조" class="rounded-2xl max-h-76 w-auto object-contain shadow-2xl select-none" />
</div>

<div class="p-3 bg-white/5 rounded-xl border border-white/10 text-xs text-white/85 leading-relaxed text-center mt-2">
  업체가 주장하는 "수산 전용 AI"는 대부분 범용 Base 모델에 소량의 수산 데이터를 덧붙인 <strong>파인튜닝(Fine-tuning)</strong>입니다.<br>
  💡 <strong>검증 질문:</strong> "어떤 해역, 몇 건의 어종 데이터로 파인튜닝했는지 실증 데이터를 공개할 수 있는가?"
</div>

<!--
[강사]
수산 특화 AI의 실체는 파인튜닝입니다.
어떤 데이터로 튜닝했는지 검증해야 합니다.
-->

---
layout: default
---
<!-- slide:27-S02-10-AuditChecklist -->

<div class="mb-3">
  <h2 class="stage-title">AI 솔루션 도입 검토 10대 체크리스트</h2>
</div>

<SolutionAuditMatrix />

<!--
[강사]
업체 제안서를 검토할 때 이 10개 질문을 던지세요.
7개 미만이면 도입을 재검토해야 합니다.
-->


---
layout: default
---
<!-- slide:29-S02-12-MarineNetwork -->

<div class="mb-3">
  <h2 class="stage-title">해상 통신 두절(망 단절) 대비 엣지 AI 전략</h2>
  <p class="stage-subtitle">돌풍이나 태풍으로 통신이 끊겨도 현장 자율 방어가 가능해야 합니다.</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4 items-center">
<v-clicks>
  <div class="glass-card border-rose-500/20 p-5 text-xs flex flex-col justify-between">
    <div>
      <div class="text-rose-300 font-bold text-sm mb-2 flex items-center gap-2">
        <span class="i-carbon-cloud-offline text-rose-400 text-lg"></span>
        <span class="whitespace-nowrap">클라우드 의존형의 위험</span>
      </div>
      <p class="text-white/75 text-xs leading-relaxed m-0">
        태풍이나 돌풍으로 해상 통신망(LTE/5G)이 끊기면, 클라우드 AI 서버와 연결이 두절되어 <strong>가두리 현장에서 경보가 멈추는 치명적 사고</strong>가 발생합니다.
      </p>
    </div>
    <div class="mt-3 pt-2 border-t border-rose-500/20 text-rose-400 font-bold whitespace-nowrap">
      위험: 통신 장애 시 산소 공급 제어 중단
    </div>
  </div>

  <div class="glass-card border-emerald-500/20 bg-emerald-950/15 p-5 text-xs flex flex-col justify-between">
    <div>
      <div class="text-emerald-300 font-bold text-sm mb-2 flex items-center gap-2">
        <span class="i-carbon-devices text-emerald-400 text-lg"></span>
        <span class="whitespace-nowrap">현장 엣지(Edge) AI 백업 체계</span>
      </div>
      <p class="text-white/85 text-xs leading-relaxed m-0">
        가두리 관리사 현장 PC/단말기에 <strong>경량 AI 모델을 탑재하여 인터넷이 끊겨도 로컬 센서 기반 긴급 경보와 산소 밸브 제어가 독립 작동</strong>하도록 설계해야 합니다.
      </p>
    </div>
    <div class="mt-3 pt-2 border-t border-emerald-500/20 text-emerald-300 font-bold whitespace-nowrap">
      보장: 망 단절 시에도 현장 긴급 경보 100% 작동
    </div>
  </div>
</v-clicks>
</div>

<div class="p-2.5 bg-white/5 rounded-xl text-xs text-white/85 border border-white/10 text-center mt-3">
  💡 <strong>필수 점검:</strong> 인터넷이 끊겨도 현장 가두리에서 소리 경보와 산소 공급기 제어가 독립 구동되는가?
</div>

<!--
[강사]
바다 위에서는 인터넷이 끊길 때가 많습니다.
통신이 죽어도 현장에서 경보가 울리는 엣지 시스템이어야 합니다.
-->

---
layout: default
---
<!-- slide:30-S02-13-SessionSummary -->

<div class="mb-4">
  <h2 class="stage-title">2차시 핵심 내용 총정리</h2>
</div>

<div class="max-w-3xl mx-auto glass-card p-6 my-6 space-y-4 text-sm text-white/90">
<v-clicks>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-indigo-500/20 text-indigo-300 flex items-center justify-center text-sm font-bold flex-shrink-0">1</span>
    <p class="leading-relaxed m-0"><strong>예측의 가치는 골든타임 확보:</strong> 수온 상승 후 폐사까지 수일의 시차가 있으므로 1~2일 전 사전 인지가 생명</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-sm font-bold flex-shrink-0">2</span>
    <p class="leading-relaxed m-0"><strong>정확도 97%의 함정 극복:</strong> 폐사·질병 예방에서는 재현율(Recall)을 최우선으로 검증</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center text-sm font-bold flex-shrink-0">3</span>
    <p class="leading-relaxed m-0"><strong>도입 체크리스트 7개 이상:</strong> 데이터 소유권, 재학습 비용, 오작동 책임 한계를 반드시 계약서에 명시</p>
  </div>
</v-clicks>
</div>

<!--
[강사]
2차시를 마칩니다.
정확도에 속지 말고 재현율을 따지세요.
-->

---
layout: default
---
<!-- slide:31-S02-14-WorkshopIntro -->

<div class="mb-3">
  <h2 class="stage-title">실습 과제 : 내 어장 AI 도입 우선순위 워크시트</h2>
  <p class="stage-subtitle">우리 양식장의 사육 주기와 현장 위험을 토대로 도입 우선순위 도출</p>
</div>

<div class="glass-card p-5 my-4 text-xs text-white/85 space-y-3">
  <p class="text-sm leading-relaxed text-white m-0">
    교재 부록의 <strong>「WS-1 내 업무 AI 활용 지도 워크시트」</strong>를 펼쳐 주시기 바랍니다.
  </p>
  <div class="p-4 bg-black/40 rounded-xl border border-white/10 space-y-2 text-xs">
    <div>1. 우리 양식장의 1년 사육 주기 중 <strong>가장 손실이 큰 위험 이벤트</strong> 작성 (예: 8월 고수온 조피볼락 폐사)</div>
    <div>2. 해당 위험을 막기 위해 <strong>현재 보유 중인 데이터(센서 수치, 수기 일지)</strong> 체크</div>
    <div>3. AI 4유형(예측/인식/최적화/문서) 중 <strong>가장 시급히 도입할 유형</strong> 1개 선택 및 이유 서술</div>
  </div>
</div>

<!--
[강사]
워크시트 WS-1을 꺼내어 각자 어장의 상황을 적어보시기 바랍니다.
-->

---
layout: center
class: text-center
---
<!-- slide:32-S03-01-Title -->

<div class="flex flex-col items-center justify-center">
  <span class="text-amber-400 font-mono text-sm tracking-widest uppercase mb-3">Session 03</span>
  <h2 class="text-5xl font-black text-white tracking-tight mb-4 leading-tight">
    생성형 AI의 양식장 업무 활용 &<br />환각(Hallucination) 극복
  </h2>
  <p class="text-white/75 text-lg font-light max-w-xl leading-relaxed mb-6">
    “확률적 문장생성의 실체와 양식장 전용 RCTF 지시문, Few-Shot 일지 변환”
  </p>

  <div class="flex flex-wrap items-center justify-center gap-2.5 pt-4 border-t border-white/10 text-[11px] font-mono text-white/60">
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-openai-icon text-xs"></span> OpenAI ChatGPT</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-claude-icon text-xs"></span> Anthropic Claude</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-google-gemini text-xs"></span> Google Gemini</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-meta-icon text-xs"></span> Meta Llama</span>
  </div>
</div>

<!--
[강사]
3차시를 시작합니다.
3차시에서는 오늘 당장 스마트폰과 PC로 쓸 수 있는 생성형 AI(ChatGPT, Gemini)의 원리와,
거짓말을 그럴듯하게 지어내는 환각을 잡는 RCTF 공식과 RAG 기법을 실습합니다.
-->

---
layout: default
---
<!-- slide:33-S03-02-LLMPrinciple -->

<div class="mb-3">
  <h2 class="stage-title">생성형 AI의 작동 원리 : "확률적 문장 생성"</h2>
  <p class="stage-subtitle">“지금까지 나온 단어 다음에 올 확률이 가장 높은 말을 이어 붙인다”</p>
</div>

<LLMTokenizer />

<!--
[강사]
생성형 AI는 검색 도구가 아닙니다.
다음에 올 단어를 확률로 이어 붙이는 문장 생성기입니다.
-->

---
layout: default
---
<!-- slide:34-S03-03-HallucinationMacbook -->

<div class="mb-3">
  <h2 class="stage-title">할루시네이션(환각)의 대표 사례</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/hallucination-macbook.png" alt="세종대왕 맥북프로 던짐 사건" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  존재하지 않는 사건을 물어봐도, "1434년 세종실록에..."라며 완벽한 소설을 사실처럼 답변합니다.
</p>

<!--
[강사]
교재의 대표적 그림입니다.
세종대왕 맥북프로 사건처럼, 모르는 것도 당당하게 지어냅니다.
-->

---
layout: default
---
<!-- slide:35-S03-04-AquaHallucination -->

<div class="mb-3">
  <h2 class="stage-title">수산양식 현장에서의 환각 위험 사례</h2>
  <p class="stage-subtitle">양식장 실무에서 생성형 AI 답변을 무비판 수용할 때 발생하는 4대 위험</p>
</div>

<div class="grid grid-cols-2 gap-4 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-rose-500/20 p-4">
    <strong class="text-rose-300 text-sm whitespace-nowrap">1. 존재하지 않는 법령·고시 조항 날조</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      "2026년 조피볼락 스마트양식 표준지침 제7조 3항에 따라 약품을 2배 투여하라" → <strong>해당 지침은 존재하지 않음!</strong>
    </p>
  </div>

  <div class="glass-card border-rose-500/20 p-4">
    <strong class="text-rose-300 text-sm whitespace-nowrap">2. 비공개 양식장 내부 사정 임의 추측</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      우리 가두리 동별 수심이나 사육 마릿수를 입력하지 않았는데도, <strong>AI가 5만 마리로 가정한 뒤 급이량을 계산</strong>하여 사료 낭비 초래
    </p>
  </div>

  <div class="glass-card border-rose-500/20 p-4">
    <strong class="text-rose-300 text-sm whitespace-nowrap">3. 수치 계산 및 단위 환산 오류</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      수산용 약품(포르말린 등) 희석 배율이나 휴약기간(예: 30일)을 잘못 계산하여 <strong>출하 정지 및 잔류 약품 검출 사고</strong> 유발
    </p>
  </div>

  <div class="glass-card border-rose-500/20 p-4">
    <strong class="text-rose-300 text-sm whitespace-nowrap">4. 질문 속 잘못된 전제 무비판 수용</strong>
    <p class="text-white/75 text-xs mt-1.5 leading-relaxed m-0">
      "넙치 적정 수온이 32℃인데 맞지?"라고 틀리게 물어보면, "네, 32℃ 환경에서는..."이라며 <strong>틀린 전제 위에서 거짓 조언을 전개</strong>함
    </p>
  </div>
</v-clicks>
</div>

<!--
[강사]
약품 용량이나 법령은 절대 AI 답변을 그대로 쓰면 안 됩니다.
-->

---
layout: default
---
<!-- slide:36-S03-05-StrengthWeakness -->

<div class="mb-3">
  <h2 class="stage-title">생성형 AI의 강점(쓰는 일) vs 취약점(아는 일)</h2>
  <p class="stage-subtitle">AI가 잘하는 '작성 업무'와 사람이 검증해야 하는 '사실 확인'의 엄격한 분업</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-emerald-500/30 bg-emerald-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="text-emerald-300 font-bold text-base mb-2.5 flex items-center gap-2">
        <span class="i-carbon-document-add text-emerald-400 text-lg"></span>
        <span class="whitespace-nowrap">AI에게 맡길 일 : "쓰는 일 (초안/정리/요약)"</span>
      </div>
      <ul class="space-y-2.5 text-white/90 text-xs p-0 m-0 list-none">
        <li>• 현장 구어체 음성 메모를 깔끔한 일지 서식으로 변환</li>
        <li>• 어촌계 총회 공지문, 태풍 대비 주민 안내 문자 초안</li>
        <li>• 지자체 스마트양식 시설 지원사업 사업계획서 문장 다듬기</li>
        <li>• 긴 어장관리 규정집에서 핵심 3줄 요약 뽑기</li>
      </ul>
    </div>
    <div class="text-xs text-emerald-300 font-bold border-t border-emerald-500/20 pt-2.5 mt-3 whitespace-nowrap">
      효과: 문서 작성 및 행정 소요 시간 80% 단축
    </div>
  </div>

  <div class="glass-card border-rose-500/30 bg-rose-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="text-rose-300 font-bold text-base mb-2.5 flex items-center gap-2">
        <span class="i-carbon-search text-rose-400 text-lg"></span>
        <span class="whitespace-nowrap">사람이 직접 검증할 일 : "아는 일 (수치/사실/판단)"</span>
      </div>
      <ul class="space-y-2.5 text-white/90 text-xs p-0 m-0 list-none">
        <li>• 국립수산과학원 고시 조항 및 법적 규정 확인</li>
        <li>• 어병 치료 약품 정량 및 휴약기간 확인</li>
        <li>• 수온·염분 측정 원시 수치 대조</li>
        <li>• 출하 시기 결정 및 사료 전면 절식 최종 판단</li>
      </ul>
    </div>
    <div class="text-xs text-rose-300 font-bold border-t border-rose-500/20 pt-2.5 mt-3 whitespace-nowrap">
      철칙: 수치와 법령은 반드시 1차 공식 자료로 확인
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
글을 다듬고 정리하는 '쓰는 일'은 AI에게 맡기고,
수치와 법령을 확인하는 '아는 일'은 사람이 지킵니다.
-->

---
layout: default
---
<!-- slide:37-S03-06-RCTFFrameworkImage -->

<div class="mb-3">
  <h2 class="stage-title">좋은 지시문의 4가지 뼈대 (RCTF)</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/rctf-framework.png" alt="RCTF 프레임워크" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  결과 품질을 바꾸는 결정적 요인은 <strong>C(맥락)와 F(형식)</strong>입니다.
</p>

<!--
[강사]
교재의 RCTF 4대 뼈대 다이어그램입니다.
역할, 맥락, 작업, 형식을 지정해 줍니다.
-->

---
layout: default
---
<!-- slide:38-S03-07-RCTFLab1 -->

<div class="mb-2">
  <h2 class="stage-title">수산양식 실무 RCTF 프롬프트 랩</h2>
  <p class="stage-subtitle">현장 상황별 프롬프트를 원클릭 복사하여 실습하세요.</p>
</div>

<RctfPromptLab />

<!--
[강사]
화면의 프롬프트 복사 버튼을 눌러 ChatGPT나 Gemini에 그대로 붙여넣어 보세요.
-->

---
layout: default
---
<!-- slide:39-S03-08-FewShotPrinciple -->

<div class="mb-3">
  <h2 class="stage-title">예시 2~3개로 끝내는 Few-Shot 기법</h2>
  <p class="stage-subtitle">“말투나 서식을 길게 설명하지 말고, 입력과 출력 예시 2개를 먼저 보여준다”</p>
</div>

<div class="grid grid-cols-2 gap-5 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-white/10 p-5 flex flex-col justify-between">
    <div>
      <div class="text-white font-bold text-sm mb-2.5 flex items-center gap-2">
        <span class="i-carbon-chat text-white/50 text-base"></span>
        <span class="whitespace-nowrap">Zero-Shot (설명만 길게 늘어놓음)</span>
      </div>
      <div class="p-3 bg-black/40 rounded-xl font-mono text-xs text-white/70 mb-3 leading-relaxed">
        "작업일지 메모를 표로 정리해 줘. 열은 가두리 번호, 수온, DO, 상태로 하고..."
      </div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        설명이 복잡해질수록 AI가 서식을 빼먹거나 엉뚱한 열을 추가하는 오류 발생.
      </p>
    </div>
  </div>

  <div class="glass-card border-sky-500/30 bg-sky-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="text-sky-300 font-bold text-sm mb-2.5 flex items-center gap-2">
        <span class="i-carbon-flash text-sky-400 text-base"></span>
        <span class="whitespace-nowrap">Few-Shot (예시 2개 제시)</span>
      </div>
      <div class="p-3 bg-black/40 rounded-xl font-mono text-xs text-sky-200 mb-3 leading-relaxed">
        예시1) "A동 물색 탁함 수온 26.8" ➔ | A-01 | 26.8℃ | 탁도 상승 |<br>
        예시2) "B동 폐사 20마리 DO 4.2" ➔ | B-01 | DO 4.2 | 폐사 20미 |<br>
        이제 정리해: "C동 조류 정체 수온 27.2 DO 3.9"
      </div>
      <p class="text-xs text-sky-300 font-bold leading-relaxed m-0">
        예시의 패턴을 즉시 모방하여 100% 완벽한 서식의 표를 출력합니다.
      </p>
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
긴 설명보다 예시 2개가 훨씬 강력합니다.
-->

---
layout: default
---
<!-- slide:40-S03-09-FewShotConverter -->

<div class="mb-3">
  <h2 class="stage-title">Few-Shot 실습 : 현장 메모 → 표준 일지 표 변환</h2>
</div>

<FewShotConverter />

<!--
[강사]
바다 위에서 손에 물 묻은 상태로 스마트폰에 "A동 물색 탁함 수온 26.8" 이렇게 음성이나 거친 텍스트로 메모만 해두세요.
AI에게 예시 2개를 보여주면, 이 메모들을 깨끗한 마크다운 표 형태의 공식 작업일지로 한 방에 정리해 줍니다.
-->

---
layout: default
---
<!-- slide:41-S03-10-CSVDataAnalysis -->

<div class="mb-3">
  <h2 class="stage-title">엑셀/CSV 데이터 파일 기반 AI 분석</h2>
  <p class="stage-subtitle">별도의 코딩이나 프로그램 없이, 엑셀 파일을 업로드하고 질문하는 것만으로 분석 가능</p>
</div>

<CsvPlayground />

<!--
[강사]
엑셀 파일을 챗봇에 드래그해 넣고 세 가지를 물어보세요.
데이터 속 이상 징후를 알아서 찾아줍니다.
-->

---
layout: default
---
<!-- slide:42-S03-11-RAGArchitectureImage -->

<div class="mb-3">
  <h2 class="stage-title">RAG (검색증강생성) 시스템 작동 원리</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/rag-architecture.png" alt="RAG 시스템 아키텍처" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  지시문 입력 → 사내 문서 검색(Query) → 관련 정보 반환 → 프롬프트 증강 → LLM 근거 기반 답변 생성
</p>

<!--
[강사]
RAG의 동작 구조도입니다.
질문이 들어오면 우리 양식장 매뉴얼 PDF를 먼저 뒤져서 그 페이지만 모델에 쥐여줍니다.
-->

---
layout: default
---
<!-- slide:43-S03-12-RAGImplementation -->

<div class="mb-3">
  <h2 class="stage-title">스마트폰/PC로 즉시 구축하는 양식장 전용 RAG</h2>
  <p class="stage-subtitle">수산과학원 표준 지침서와 우리 어장 과거 3년 일지 PDF를 탑재한 지식 비서</p>
</div>

<div class="grid grid-cols-3 gap-4 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-white/10 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 text-amber-400 font-bold text-sm mb-2">
        <span class="i-carbon-document-pdf text-lg"></span>
        <span class="whitespace-nowrap">1단계: PDF 문서 준비</span>
      </div>
      <p class="text-white/75 text-xs leading-relaxed m-0">
        국립수산과학원 표준 사육 지침서, 관할 지자체 고수온 대응 매뉴얼, 우리 어장 과거 3년 일지 PDF 준비
      </p>
    </div>
  </div>
  <div class="glass-card border-white/10 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 text-sky-400 font-bold text-sm mb-2">
        <span class="i-carbon-cloud-upload text-lg"></span>
        <span class="whitespace-nowrap">2단계: Notebook 업로드</span>
      </div>
      <p class="text-white/75 text-xs leading-relaxed m-0">
        구글 노트북LM(NotebookLM) 또는 사내 RAG 툴에 문서를 드래그 앤 드롭으로 업로드 (개발 불필요)
      </p>
    </div>
  </div>
  <div class="glass-card border-emerald-500/30 bg-emerald-950/20 p-5 flex flex-col justify-between">
    <div>
      <div class="flex items-center gap-2 text-emerald-300 font-bold text-sm mb-2">
        <span class="i-carbon-chat-bot text-lg"></span>
        <span class="whitespace-nowrap">3단계: 출처 기반 실시간 질의</span>
      </div>
      <p class="text-white/85 text-xs leading-relaxed m-0">
        "조피볼락 고수온 특보 시 몇 번 가두리부터 차광막을 내려야 하지?" → 매뉴얼 14페이지를 인용하며 정확히 답변!
      </p>
    </div>
  </div>
</v-clicks>
</div>

<div class="p-2.5 bg-emerald-950/20 border border-emerald-500/20 rounded-xl text-xs text-emerald-300 text-center mt-3 font-medium">
  ⭐ <strong>비용 0원, 코딩 0줄:</strong> 오늘 강의 끝나고 바로 양식장 전용 AI 지식 비서를 만들 수 있습니다.
</div>

<!--
[강사]
노트북LM에 수과원 매뉴얼만 올려두면 바로 우리 양식장 전용 오픈북 AI가 완성됩니다.
-->

---
layout: center
class: text-center
---
<!-- slide:44-S04-01-Title -->

<div class="flex flex-col items-center justify-center">
  <span class="text-emerald-400 font-mono text-sm tracking-widest uppercase mb-3">Session 04</span>
  <h2 class="text-5xl font-black text-white tracking-tight mb-4 leading-tight">
    AI 에이전트 기반 운영지원 &<br />스마트양식 도입 로드맵
  </h2>
  <p class="text-white/75 text-lg font-light max-w-xl leading-relaxed mb-6">
    “스스로 계획하고 도구를 쓰는 에이전트와 되돌릴 수 없는 행위의 자동화 금지 원칙”
  </p>

  <div class="flex flex-wrap items-center justify-center gap-2.5 pt-4 border-t border-white/10 text-[11px] font-mono text-white/60">
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-python text-xs"></span> Python Ecosystem</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-pytorch-icon text-xs"></span> PyTorch AI</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-logos-hugging-face-icon text-xs"></span> Hugging Face</span>
    <span class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/[0.04] border border-white/10"><span class="i-carbon-bot text-purple-400 text-xs"></span> Autonomous Agent</span>
  </div>
</div>

<!--
[강사]
마지막 4차시입니다.
단순히 질문에 답하는 수준을 넘어, 매일 새벽 스스로 센서와 기상청 데이터를 조회하고 이상 가두리를 찾아 브리핑해 주는 'AI 에이전트'의 실전 시나리오와 단계별 도입 로드맵을 완성해 보겠습니다.
-->

---
layout: default
---
<!-- slide:45-S04-02-AgentArchitectureImage -->

<div class="mb-3">
  <h2 class="stage-title">AI 에이전트의 3대 구성요소와 사고 루프</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/agent-architecture.png" alt="AI 에이전트 구조" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  AI 에이전트 = <strong>두뇌(Model) + 손발(Tools) + 지휘자(Orchestration)</strong> (생각 → 행동 → 관찰 반복)
</p>

<!--
[강사]
에이전트의 3대 요소입니다.
두뇌인 LLM, 손발인 수질 DB/기상 API, 그리고 지휘자가 목표를 달성할 때까지 생각-행동-관찰 루프를 돕니다.
-->

---
layout: default
---
<!-- slide:46-S04-03-AgentScenario -->

<div class="mb-3">
  <h2 class="stage-title">매일 06:00 가두리 일일 브리핑 에이전트</h2>
  <p class="stage-subtitle">관리자가 출근하기 전, 에이전트가 6개 단계를 자동으로 마쳐둡니다.</p>
</div>

<div class="grid grid-cols-3 gap-3.5 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-sky-500/20 p-4">
    <div class="flex items-center gap-1.5 text-sky-300 font-bold text-sm mb-1">
      <span class="i-carbon-data-base text-base"></span>
      <span class="whitespace-nowrap">1. 수질 DB 조회</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">전 가두리 수온·DO 센서 864건 로그 전수 확인</p>
  </div>
  <div class="glass-card border-sky-500/20 p-4">
    <div class="flex items-center gap-1.5 text-sky-300 font-bold text-sm mb-1">
      <span class="i-carbon-analytics text-base"></span>
      <span class="whitespace-nowrap">2. 급변 구간 식별</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">전일 대비 수온 +1.2℃ 상승 및 최저 DO 3.6 포착</p>
  </div>
  <div class="glass-card border-amber-500/20 p-4">
    <div class="flex items-center gap-1.5 text-amber-300 font-bold text-sm mb-1">
      <span class="i-carbon-compare text-base"></span>
      <span class="whitespace-nowrap">3. 일지 대조</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">9/14 일지에서 A-03동 폐사 41미 급증 확인</p>
  </div>
  <div class="glass-card border-amber-500/20 p-4">
    <div class="flex items-center gap-1.5 text-amber-300 font-bold text-sm mb-1">
      <span class="i-carbon-cloudy text-base"></span>
      <span class="whitespace-nowrap">4. 기상청 API 대조</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">풍속 4m/s, 파고 0.4m, 조류 정체 시점 확인</p>
  </div>
  <div class="glass-card border-emerald-500/20 p-4">
    <div class="flex items-center gap-1.5 text-emerald-300 font-bold text-sm mb-1">
      <span class="i-carbon-task text-base"></span>
      <span class="whitespace-nowrap">5. 권고 조치 정리</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">주의 가두리 2개소(A-01, A-03) 우선 점검 권고</p>
  </div>
  <div class="glass-card border-emerald-500/20 p-4">
    <div class="flex items-center gap-1.5 text-emerald-300 font-bold text-sm mb-1">
      <span class="i-carbon-send-alt text-base"></span>
      <span class="whitespace-nowrap">6. 모바일 발송</span>
    </div>
    <p class="text-white/70 text-xs m-0 leading-relaxed">06:00 정각에 관리자 스마트폰으로 전송 완료</p>
  </div>
</v-clicks>
</div>

<!--
[강사]
출근 전에 에이전트가 6단계를 끝내놓기 때문에, 관리자는 배에 타자마자 문제가 있는 가두리로 직행할 수 있습니다.
-->

---
layout: default
---
<!-- slide:47-S04-04-AgentSimulation -->

<div class="mb-3">
  <h2 class="stage-title">06:00 브리핑 에이전트 실행 시뮬레이터</h2>
</div>

<AgentBriefingSim />

<!--
[강사]
화면의 시뮬레이터를 보십시오.
새벽 6시에 에이전트가 24시간 수온/산소 센서 로그를 조회하고, 기상청 풍속과 파고를 대조하여 "A-01동 수온 급상승, A-03동 폐사 급증 주의" 브리핑을 카톡으로 쏴줍니다.
-->

---
layout: default
---
<!-- slide:48-S04-05-AutomationLevelsImage -->

<div class="mb-3">
  <h2 class="stage-title">에이전트에게 어디까지 맡길 것인가 : 4단계 수준</h2>
</div>

<div class="flex items-center justify-center my-3">
  <img src="/automation-4levels.png" alt="자동화 4단계 수준" class="rounded-2xl max-h-82 w-auto object-contain shadow-2xl select-none" />
</div>

<p class="text-white/70 text-xs text-center mt-2">
  L1 알림 → L2 권고 → L3 조건부 실행 → L4 완전 자동 (신뢰가 확인될 때마다 한 단계씩 상향)
</p>

<!--
[강사]
자동화 4단계 계단입니다.
초기에는 L1 알림과 L2 권고까지만 맡기고, 사람이 승인해야 합니다.
-->

---
layout: default
---
<!-- slide:49-S04-06-AbsoluteRule -->

<div class="mb-3">
  <h2 class="stage-title">되돌릴 수 없는 행위의 자동화 금지 원칙</h2>
</div>

<AbsoluteRule />

<!--
[강사]
되돌릴 수 없는 행위는 반드시 사람이 최종 승인해야 합니다.
-->

---
layout: default
---
<!-- slide:50-S04-08-Roadmap4Steps -->

<div class="mb-3">
  <h2 class="stage-title">현실적인 스마트양식 AI 4단계 도입 로드맵</h2>
  <p class="stage-subtitle">가장 흔한 실패는 1·2단계를 건너뛰고 4단계 카메라부터 설치하는 것입니다.</p>
</div>

<div class="grid grid-cols-4 gap-4 my-4">
<v-clicks>
  <div class="glass-card border-t-2 border-t-emerald-400 p-4 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold mb-2 whitespace-nowrap">1단계 (즉시~3개월)</div>
      <h3 class="font-bold text-white text-sm mt-1 mb-2 flex items-center gap-1.5 whitespace-nowrap"><span class="i-carbon-document-tasks text-emerald-400 text-base"></span>문서 업무 + RAG</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">작업일지 Few-shot 정리<br>고시문 RAG 질의응답</p>
    </div>
    <div class="text-xs text-emerald-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      전제: <strong>스마트폰 즉시 가능</strong>
    </div>
  </div>

  <div class="glass-card border-t-2 border-t-sky-400 p-4 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-sky-300 font-bold mb-2 whitespace-nowrap">2단계 (3~12개월)</div>
      <h3 class="font-bold text-white text-sm mt-1 mb-2 flex items-center gap-1.5 whitespace-nowrap"><span class="i-carbon-chart-line-data text-sky-400 text-base"></span>기록 표준화 & 탐지</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">동별·숫자 기록 정착<br>센서 수질 급변 이상탐지</p>
    </div>
    <div class="text-xs text-sky-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      전제: <strong>수질센서 수집 체계</strong>
    </div>
  </div>

  <div class="glass-card border-t-2 border-t-indigo-400 p-4 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-indigo-300 font-bold mb-2 whitespace-nowrap">3단계 (1~2년)</div>
      <h3 class="font-bold text-white text-sm mt-1 mb-2 flex items-center gap-1.5 whitespace-nowrap"><span class="i-carbon-chart-cluster-bar text-indigo-400 text-base"></span>예측 솔루션 도입</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">고수온 조기 경보<br>급이량·성장 곡선 분석</p>
    </div>
    <div class="text-xs text-indigo-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      전제: <strong>동별 기록 1년 이상</strong>
    </div>
  </div>

  <div class="glass-card border-t-2 border-t-purple-400 p-4 flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-purple-300 font-bold mb-2 whitespace-nowrap">4단계 (2년 이후~)</div>
      <h3 class="font-bold text-white text-sm mt-1 mb-2 flex items-center gap-1.5 whitespace-nowrap"><span class="i-carbon-bot text-purple-400 text-base"></span>영상인식 & 에이전트</h3>
      <p class="text-xs text-white/75 leading-relaxed m-0">수중영상 어체 계수<br>급이 연동 자동 브리핑</p>
    </div>
    <div class="text-xs text-purple-300 border-t border-white/10 pt-2.5 mt-3 font-medium whitespace-nowrap">
      전제: <strong>수중 카메라 & 제어 인프라</strong>
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
수산양식 AI 도입의 정석 로드맵입니다.
처음부터 비싼 카메라 달고 4단계로 가면 99% 실패합니다.
스마트폰으로 작업일지 정리(1단계)부터 시작하고, 1년 치 동별 데이터가 쌓인 뒤 예측 솔루션(3단계)으로 가야 합니다.
-->

---
layout: default
---
<!-- slide:51-S04-09-Quizzes -->

<div class="mb-3">
  <h2 class="stage-title">스마트수산업 전문가 3대 실무 학습확인</h2>
  <p class="stage-subtitle">현장 관리자가 반드시 체득해야 할 핵심 판단 원칙 점검</p>
</div>

<div class="grid grid-cols-3 gap-4 my-4 text-xs">
<v-clicks>
  <div class="glass-card border-white/10 p-4.5 flex flex-col justify-between">
    <div>
      <span class="text-amber-300 font-bold text-sm whitespace-nowrap">문제 1: 폐사 경보(0.78) 수신</span>
      <div class="p-3 bg-black/40 rounded-xl mt-2.5 space-y-1.5 text-xs text-white/85 leading-relaxed">
        <div><strong class="text-emerald-300">⭕ 실측 확인:</strong> 근거 데이터 확인 후 현장 육안 점검 및 비상 산소 가동 예비</div>
        <div><strong class="text-rose-300">❌ 금지 행동:</strong> 실측 없이 약품 투여/조기 출하 즉시 시행 금지</div>
      </div>
    </div>
  </div>

  <div class="glass-card border-white/10 p-4.5 flex flex-col justify-between">
    <div>
      <span class="text-amber-300 font-bold text-sm whitespace-nowrap">문제 2: 정확도 97%의 허점</span>
      <div class="p-3 bg-black/40 rounded-xl mt-2.5 space-y-1.5 text-xs text-white/85 leading-relaxed">
        <div>• <strong>이유:</strong> 100일 중 위험 3일이면 "매일 안전함"만 답해도 97% 나옴</div>
        <div>• <strong class="text-emerald-300">재현율(Recall):</strong> 실제 위험 중 잡은 비율 (최우선 확인!)</div>
        <div>• <strong class="text-sky-300">정밀도(Precision):</strong> 경보 중 실제 비율</div>
      </div>
    </div>
  </div>

  <div class="glass-card border-white/10 p-4.5 flex flex-col justify-between">
    <div>
      <span class="text-amber-300 font-bold text-sm whitespace-nowrap">문제 3: 아침 브리핑 에이전트</span>
      <div class="p-3 bg-black/40 rounded-xl mt-2.5 space-y-1.5 text-xs text-white/85 leading-relaxed">
        <div>• <strong>도구:</strong> 수질 DB + 기상 API + 알림 봇</div>
        <div>• <strong class="text-sky-300">초기 수준:</strong> Level 2 (권고까지만)</div>
        <div>• <strong>절차:</strong> 최소 2주간 사람과 병행 운영으로 일치도 검증 후 상향</div>
      </div>
    </div>
  </div>
</v-clicks>
</div>

<!--
[강사]
오늘 배운 핵심 3문제를 종합했습니다.
경보 시 실측 우선, 재현율 확인, 그리고 2주 병행 운영 후 자동화 상향을 기억하십시오.
-->

---
layout: default
---
<!-- slide:52-S04-10-ActionPrinciples -->

<div class="mb-4">
  <h2 class="stage-title">스마트수산업 전문가를 위한 3대 실천 수칙</h2>
</div>

<div class="max-w-3xl mx-auto glass-card p-6 my-6 space-y-4 text-sm text-white/90">
<v-clicks>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-sky-500/20 text-sky-300 flex items-center justify-center text-sm font-bold flex-shrink-0">1</span>
    <p class="leading-relaxed m-0"><strong>기록이 없으면 AI도 없다:</strong> 동별 분리, 숫자 표기, 결측치 구분으로 1년 치 사육 데이터를 축적하세요.</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-indigo-500/20 text-indigo-300 flex items-center justify-center text-sm font-bold flex-shrink-0">2</span>
    <p class="leading-relaxed m-0"><strong>경보는 알람일 뿐, 조치는 실측으로:</strong> 공급업체 정확도 97%에 속지 말고 재현율을 검증하며, 최종 근거는 현장 실측입니다.</p>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-full bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-sm font-bold flex-shrink-0">3</span>
    <p class="leading-relaxed m-0"><strong>되돌릴 수 없는 일은 사람이 승인한다:</strong> AI 에이전트는 분석과 브리핑을 맡기고, 약품 투여와 출하 판단은 사람이 지킵니다.</p>
  </div>
</v-clicks>
</div>

<!--
[강사]
3대 실천 수칙입니다.
기록을 남기고, 실측으로 검증하며, 중요한 조치는 사람이 승인하십시오.
-->
