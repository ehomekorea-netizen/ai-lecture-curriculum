---
layout: default
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: '생성형 AI를 통한 실무능력 향상'
exportFilename: MC에너지-2026-1차시-생성형AI를-통한-실무능력-향상
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
class: px-16 py-10
glowSeed: 105
clicks: 2
---
<!-- slide:03-Hook -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  프롬프트 어조와 정답률: 지시문의 명확성이 미치는 영향
</h2>

<div class="grid grid-cols-12 gap-10 items-center">
  <div class="col-span-5 flex justify-center">
    <div class="rounded-2xl overflow-hidden border border-white/20 shadow-2xl bg-zinc-950 p-2">
      <img src="/0002820859_002_20260831071212490.jpg" alt="프롬프트 어조별 정답률" class="rounded-xl w-full max-h-100 object-contain" />
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between h-96">
    <div class="space-y-4">
      <div v-click="1" class="p-4 rounded-xl border border-rose-500/30 bg-rose-950/20 backdrop-blur-md">
        <div class="flex items-center gap-2 text-rose-400 font-bold text-sm mb-1">
          <span class="i-carbon:close-filled"></span>
          <span>부정적·위협적 어조 (정답률 56.6%)</span>
        </div>
        <p class="text-xs text-white/70 m-0 leading-relaxed">
          "틀리면 해고야", "제대로 안 하면 불이익을 준다" 등 감정적 압박을 가할 때 정답률이 15% 이상 급락했습니다.
        </p>
      </div>
      <div v-click="2" class="p-4 rounded-xl border border-emerald-500/30 bg-emerald-950/20 backdrop-blur-md">
        <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm mb-1">
          <span class="i-carbon:checkmark-filled"></span>
          <span>긍정적·보상적 어조 (정답률 71.9%)</span>
        </div>
        <p class="text-xs text-white/70 m-0 leading-relaxed">
          "정확하게 답변하면 보너스를 주겠다", "최고의 전문가처럼 답변하라" 등 명확하고 긍정적인 역할 부여 시 최상의 성능을 기록했습니다.
        </p>
      </div>
    </div>
    <div class="p-4 rounded-xl border border-cyan-500/30 bg-cyan-950/25 flex items-center justify-between text-xs text-white/90">
      <div class="flex items-center gap-2">
        <span class="i-carbon:information-filled text-cyan-400"></span>
        <span><strong>핵심 결론:</strong> AI는 감정적 압박이 아닌 <strong>명확한 역할 부여와 구체적 지시 체계</strong>에 반응합니다.</span>
      </div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
실제 실험 결과, 위협적 프롬프트는 정답률을 떨어뜨립니다.
AI를 다룰 때는 감정이 아니라 '명확한 역할(Role)과 맥락(Context)'을 설계하는 것이 핵심입니다.
-->

---
title: 인공지능 · 머신러닝 · 딥러닝 · 생성형 AI 계층도
layout: default
class: px-16 py-9
glowSeed: 201
clicks: 3
---
<!-- slide:03-AI-Hierarchy -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  인공지능 생태계 속 생성형 AI의 정확한 위치
</h2>

<div class="grid grid-cols-12 gap-8 items-center mt-2">
  <div class="col-span-5 flex justify-center">
    <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-3 shadow-2xl">
      <img src="/ai-ml-dl-hierarchy.png" alt="AI Hierarchy" class="rounded-xl w-full max-h-80 object-contain" />
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between h-84">
    <div class="space-y-2.5">
      <div v-click="1" class="p-3 rounded-xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-blue-400">1. 인공지능 (AI)</span>
          <span class="text-[11px] font-mono text-white/50">가장 포괄적인 개념</span>
        </div>
        <p class="text-xs text-white/80 m-0 leading-relaxed">
          인간의 학습, 추론, 지각 능력을 컴퓨터 프로그램으로 모방한 모든 기술의 총칭
        </p>
      </div>
      <div v-click="2" class="p-3 rounded-xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-cyan-400">2. 머신러닝 & 딥러닝 (ML/DL)</span>
          <span class="text-[11px] font-mono text-white/50">데이터 기반 학습</span>
        </div>
        <p class="text-xs text-white/80 m-0 leading-relaxed">
          규칙을 직접 코딩하지 않고 데이터를 통해 패턴을 학습(ML)하며, 다층 신경망으로 복잡한 특징을 추출(DL)
        </p>
      </div>
      <div v-click="3" class="p-3 rounded-xl border border-emerald-500/40 border-t-3 border-t-emerald-400 bg-emerald-950/30 backdrop-blur-md shadow-lg">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-emerald-400">3. 생성형 AI (Generative AI)</span>
          <span class="text-[11px] font-mono text-emerald-300 font-bold">2026 실무 핵심</span>
        </div>
        <p class="text-xs text-white/90 m-0 leading-relaxed">
          단순 분류·예측을 넘어 <strong>텍스트, 코드, 이미지 등 새로운 창작물을 직접 합성</strong>해내는 최신 딥러닝 기술
        </p>
      </div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
AI라는 가장 큰 그릇 안에 데이터를 학습하는 머신러닝이 있고, 그 안에 신경망을 모방한 딥러닝이 있으며, 오늘 우리가 다루는 생성형 AI는 딥러닝을 바탕으로 새로운 결과물을 만들어내는 가장 진화된 영역입니다.
-->

---
title: 머신러닝과 딥러닝의 특징 비교
layout: default
class: px-16 py-8
glowSeed: 202
clicks: 1
---
<!-- slide:04-ML-vs-DL -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  머신러닝과 딥러닝의 특징 및 작동 방식 비교
</h2>

<div class="flex items-center justify-center my-3">
  <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-4 shadow-2xl transition-all duration-300">
    <img src="/ml-vs-dl.png" alt="머신러닝 vs 딥러닝" class="rounded-xl max-h-76 w-auto object-contain" />
  </div>
</div>

<div v-click="1" class="flex items-center justify-center gap-6 text-xs font-mono font-bold text-white/80 mt-3 border-t border-white/10 pt-3">
  <span class="text-cyan-400">머신러닝: 사람이 특징(Feature)을 직접 정의</span>
  <span class="text-white/40">vs</span>
  <span class="text-emerald-400 font-bold">딥러닝: 인공신경망이 스스로 복합 특징을 추출 및 분류</span>
</div>

<!--
[강사 멘트]
머신러닝은 사람이 특징을 골라줘야 했지만, 딥러닝은 심층 신경망을 통해 스스로 데이터의 맥락과 규칙을 찾아냅니다.
이것이 생성형 AI가 인간의 복잡한 문맥을 이해할 수 있는 기술적 기초입니다.
-->

---
title: ChatGPT의 3대 핵심 어원과 작동 원리
layout: default
class: px-16 py-8
glowSeed: 203
clicks: 3
---
<!-- slide:05-GPT-Etymology -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  ChatGPT의 3대 핵심 어원과 작동 원리
</h2>

<div class="grid grid-cols-3 gap-6">
  <div v-click="1" class="p-6 rounded-2xl border border-cyan-500/30 border-t-4 border-t-cyan-400 bg-cyan-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="text-3xl font-mono font-black text-cyan-400 mb-2">G</div>
      <div class="text-sm font-bold text-white mb-2">Generative (생성형)</div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        기존 데이터를 그대로 복사해 붙여넣는 것이 아니라, 학습된 통계적 패턴을 바탕으로 새로운 문장과 코드를 직접 합성하여 생성합니다.
      </p>
    </div>
    <div class="pt-3 border-t border-white/10 text-xs font-mono text-cyan-300">새로운 콘텐츠 창작</div>
  </div>
  <div v-click="2" class="p-6 rounded-2xl border border-blue-500/30 border-t-4 border-t-blue-400 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="text-3xl font-mono font-black text-blue-400 mb-2">P</div>
      <div class="text-sm font-bold text-white mb-2">Pre-trained (사전학습)</div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        인터넷 상의 방대한 공개 텍스트와 지식을 사전에 미리 공부하여, 인간의 언어 구조와 세상에 대한 폭넓은 배경 지식을 갖추었습니다.
      </p>
    </div>
    <div class="pt-3 border-t border-white/10 text-xs font-mono text-blue-300">방대한 지식 베이스 구축</div>
  </div>
  <div v-click="3" class="p-6 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="text-3xl font-mono font-black text-emerald-400 mb-2">T</div>
      <div class="text-sm font-bold text-white mb-2">Transformer (신경망)</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        문장 내 단어들 간의 관계와 문맥(Attention)을 파악하여, 사용자의 질문에 가장 적절하게 이어질 다음 단어를 확률적으로 조립합니다.
      </p>
    </div>
    <div class="pt-3 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">문맥 이해 및 단어 예측</div>
  </div>
</div>

<!--
[강사 멘트]
GPT의 세 글자(G-P-T)는 생성(Generative), 사전학습(Pre-trained), 문맥신경망(Transformer)을 의미합니다.
지식을 외운 상태에서 질문 문맥에 가장 알맞은 다음 단어를 확률적으로 계산해 문장을 완성하는 원리입니다.
-->

---
title: 2026 AI 활용 환경의 변화
layout: default
class: px-16 py-9
glowSeed: 204
clicks: 2
---
<!-- slide:06-2026-Trends -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  2026 AI 활용 환경의 변화: 질문에서 협업으로
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase mb-2">과거 (~2023)</div>
      <div class="text-lg font-bold text-white mb-3">단순 챗봇 질의응답 (Q&A)</div>
      <ul class="text-xs text-white/70 space-y-2 pl-4 m-0 leading-relaxed">
        <li>단일 질문에 대한 단순 텍스트 답변 생성</li>
        <li>최신 정보 접근 제한 및 빈번한 할루시네이션 발생</li>
        <li>사용자가 복사·붙여넣기로 직접 문서를 취합해야 하는 번거로움</li>
      </ul>
    </div>
    <div class="pt-3 border-t border-white/10 text-xs font-mono text-white/50">단방향 텍스트 생성 도구</div>
  </div>
  <div v-click="1" class="p-6 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="text-xs font-mono text-cyan-400 font-bold uppercase mb-2">현재 (2026 실무 표준)</div>
      <div class="text-lg font-bold text-white mb-3">다중 파일 기반 AI 에이전트 협업</div>
      <ul class="text-xs text-white/85 space-y-2 pl-4 m-0 leading-relaxed">
        <li><strong>로컬 폴더 및 다중 문서 연동:</strong> 대용량 사내 문서를 직접 읽고 분석</li>
        <li><strong>RAG & 심층 리서치 결합:</strong> 출처 링크 및 인용(Citation)으로 검증 가능</li>
        <li><strong>자동화 산출물 완성:</strong> 기획서(DOCX), 표, 프레젠테이션 직접 작성</li>
      </ul>
    </div>
    <div class="pt-3 border-t border-white/15 text-xs font-mono font-bold text-cyan-300">스스로 일하는 실무 파트너</div>
  </div>
</div>

<!--
[강사 멘트]
2026년 현재 AI는 더 이상 단순 대화창이 아닙니다.
내 컴퓨터의 폴더와 보고서 파일을 연결하여, 출처를 검증해가며 완성형 문서를 함께 만드는 협업 에이전트 시대입니다.
-->

---
title: 검색과 생성형 AI의 본질적 차이
layout: default
class: px-16 py-8
glowSeed: 205
clicks: 2
---
<!-- slide:07-Search-vs-GenAI -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  검색과 생성형 AI는 어떻게 다를까?
</h2>

<div class="grid grid-cols-2 gap-8 mt-2">
  <div class="p-5 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-78">
    <div>
      <div class="flex items-center gap-2 text-white/80 font-bold text-base mb-2">
        <span class="i-carbon:search text-lg"></span>
        <span>인터넷 검색엔진 (Search Engine)</span>
      </div>
      <div class="text-xs font-mono text-white/50 mb-3">"이미 존재하는 문서를 찾아주는 도구"</div>
      <ul class="text-xs text-white/70 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li>인터넷에 등록된 웹페이지 링크와 원문을 색인하여 나열</li>
        <li>사용자가 직접 여러 링크를 클릭해 읽고 요약·정리해야 함</li>
        <li><strong>강점:</strong> 원천 사실(Fact), 최신 단가, 실시간 공시 확인에 최적화</li>
      </ul>
    </div>
    <div class="pt-3 border-t border-white/10 flex items-center justify-between">
      <span class="text-xs font-mono text-white/50">데이터 '탐색' 엔진</span>
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-white/10 border border-white/15 text-xs font-bold text-white">
          <span class="i-simple-icons:naver text-[#03C75A] text-sm"></span>
          <span>NAVER</span>
        </div>
        <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-white/10 border border-white/15 text-xs font-bold text-white">
          <span class="i-logos:google text-sm"></span>
          <span>Google</span>
        </div>
      </div>
    </div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-78">
    <div>
      <div class="flex items-center gap-2 text-cyan-400 font-bold text-base mb-2">
        <span class="i-carbon:bot text-lg"></span>
        <span>생성형 AI (Generative AI)</span>
      </div>
      <div class="text-xs font-mono text-cyan-300 mb-3">"지식을 가공해 새 문서를 만들어주는 두뇌"</div>
      <ul class="text-xs text-white/85 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li>질문의 문맥을 파악해 기획서 초안, 표, 요약본을 직접 작성</li>
        <li>자료의 논리적 구조화, 어조 변경, 아이디어 발굴에 탁월</li>
        <li><strong>주의점:</strong> 원본 근거 없이 지시하면 허위 정보를 지어낼 위험 존재</li>
      </ul>
    </div>
    <div class="pt-3 border-t border-white/15 flex items-center justify-between">
      <span class="text-xs font-mono font-bold text-cyan-300">데이터 '가공·생성' 엔진</span>
      <div class="flex items-center gap-2">
        <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-cyan-500/15 border border-cyan-500/30 text-xs font-bold text-cyan-200">
          <span class="i-logos:openai-icon text-sm"></span>
          <span>ChatGPT</span>
        </div>
        <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-cyan-500/15 border border-cyan-500/30 text-xs font-bold text-cyan-200">
          <span class="i-logos:google-gemini text-sm"></span>
          <span>Gemini</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div v-click="2" class="mt-3 p-3 rounded-xl border border-cyan-500/30 bg-cyan-950/20 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:idea text-base text-cyan-300"></span>
    <span><strong>2026년 실무 정답:</strong> 검색(신뢰 자료 확보)과 생성(문서 작성)을 결합한 <strong>RAG(검색 증강 생성)</strong>로 일합니다.</span>
  </div>
</div>

<!--
[강사 멘트]
검색엔진은 도서관의 사서처럼 책의 위치를 알려주고, 생성형 AI는 작가처럼 글을 대신 써줍니다.
가장 이상적인 업무 방식은 두 가지를 결합해 정확한 자료를 주고 글을 쓰게 하는 것입니다.
-->

---
title: 할루시네이션의 원인과 현상
layout: default
class: px-16 py-9
glowSeed: 206
clicks: 2
---
<!-- slide:08-Hallucination -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  할루시네이션(환각) 현상과 왜 발생하는가?
</h2>

<div class="grid grid-cols-12 gap-8 items-center">
  <div class="col-span-5 flex justify-center">
    <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-2 shadow-2xl">
      <img src="/hallucination-macbook.png" alt="Hallucination Concept" class="rounded-xl w-full max-h-76 object-contain" />
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between h-80">
    <div class="space-y-3">
      <div class="p-4 rounded-xl border border-rose-500/30 bg-rose-950/20 backdrop-blur-md">
        <div class="text-xs font-mono font-bold text-rose-400 uppercase mb-1">정의</div>
        <p class="text-xs text-white/80 m-0 leading-relaxed">
          AI가 실제 사실이 아니거나 존재하지 않는 정보를 <strong>마치 완벽한 사실인 것처럼 그럴듯하게 답변</strong>하는 오류 현상
        </p>
      </div>
      <div v-click="1" class="p-4 rounded-xl border border-white/15 bg-white/5 backdrop-blur-md">
        <div class="text-xs font-mono font-bold text-white/60 uppercase mb-1">발생 원인</div>
        <p class="text-xs text-white/70 m-0 leading-relaxed">
          LLM은 참/거짓을 검증하는 판단 시스템이 아니라, <strong>통계적으로 가장 자연스러운 다음 단어를 확률 조립</strong>하기 때문
        </p>
      </div>
    </div>
    <div v-click="2" class="p-3.5 rounded-xl border border-amber-500/30 bg-amber-950/20 flex items-center justify-between text-xs text-amber-200">
      <div class="flex items-center gap-2">
        <span class="i-carbon:warning-alt-filled text-base text-amber-400"></span>
        <span><strong>실무 주의사항:</strong> AI가 출력한 수치, 법령, 규정 조항은 <strong>반드시 원문 대조 검증</strong>이 필수적입니다.</span>
      </div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
AI는 거짓말을 하려고 속이는 것이 아닙니다. 문장의 자연스러움을 완성하려다 보니 없는 사실을 그럴듯하게 지어내는 것입니다.
따라서 AI를 쓸 때는 검증 체계가 반드시 함께 작동해야 합니다.
-->

---
title: AI 답변 결과 검증 3단계
layout: default
class: px-16 py-9
glowSeed: 207
clicks: 3
---
<!-- slide:09-Verification-Criteria -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI의 답변, 어떻게 검증해야 할까? 3단계 검증 체계
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div v-click="1" class="p-5 rounded-2xl border border-blue-500/30 border-t-4 border-t-blue-400 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono font-bold text-blue-400 uppercase mb-1">Step 01</div>
      <div class="text-base font-bold text-white mb-2">원문 출처 대조</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        AI가 제시한 수치, 통계, 규정 조항을 사내 원천 문서나 공식 사이트 원문과 1:1 대조합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-blue-300">사실(Fact) 유효성 확인</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-cyan-500/30 border-t-4 border-t-cyan-400 bg-cyan-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono font-bold text-cyan-400 uppercase mb-1">Step 02</div>
      <div class="text-base font-bold text-white mb-2">논리 및 전후 맥락 검증</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        전체 보고서의 주장과 결론이 논리적으로 비약 없이 일관되게 전개되는지 흐름을 검토합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-cyan-300">논리적 일관성 확보</div>
  </div>
  <div v-click="3" class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono font-bold text-emerald-400 uppercase mb-1">Step 03</div>
      <div class="text-base font-bold text-white mb-2">실무 적합성 및 법적 검토</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        사내 보안 규정, 관련 법령, 조직의 실질적 실행 가능성을 최종 검수하여 문서화합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">최종 승인 및 배포</div>
  </div>
</div>

<!--
[강사 멘트]
1단계 원문 대조, 2단계 논리 흐름 점검, 3단계 사내 규정 적합성을 거치면 실무 실수를 100% 차단할 수 있습니다.
-->

---
title: RAG 시스템의 작동 구조
layout: default
class: px-16 py-8
glowSeed: 208
clicks: 1
---
<!-- slide:10-RAG-Architecture -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  RAG(검색 증강 생성) 시스템의 작동 구조
</h2>

<div class="flex items-center justify-center my-3">
  <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-3 shadow-2xl transition-all duration-300">
    <img src="/rag-architecture.png" alt="RAG 시스템 아키텍처" class="rounded-xl max-h-74 w-auto object-contain" />
  </div>
</div>

<div v-click="1" class="flex items-center justify-center gap-6 text-xs font-mono font-bold text-white/80 mt-2 border-t border-white/10 pt-2.5">
  <span class="text-cyan-400">1. 질의(Query) 입력</span>
  <span class="text-white/40">➔</span>
  <span class="text-amber-400">2. 사내 DB 검색(Retrieval)</span>
  <span class="text-white/40">➔</span>
  <span class="text-emerald-400 font-bold">3. 근거 결합 및 답변 생성(Augmentation & Generation)</span>
</div>

<!--
[강사 멘트]
RAG는 질문이 들어왔을 때 모델의 기억에만 의존하지 않고, 사내 문서 DB에서 정확한 자료를 먼저 찾아서 함께 전달하는 기술입니다.
-->

---
title: RAG의 3단계 핵심 메커니즘과 오픈북 원리
layout: default
class: px-16 py-9
glowSeed: 209
clicks: 3
---
<!-- slide:11-RAG-Mechanisms -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  RAG의 3단계 핵심 메커니즘과 오픈북 원리
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div v-click="1" class="p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="w-8 h-8 rounded-lg bg-cyan-500/20 flex items-center justify-center mb-3 text-cyan-400">
        <span class="i-carbon:search text-xl"></span>
      </div>
      <div class="text-base font-bold text-white mb-2">1. Retrieval (검색)</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        사용자가 질문하면 LLM에 바로 넘기지 않고, 사내 문서·규정집 DB에서 가장 관련 있는 본문 조각(Chunk)을 실시간 탐색합니다.
      </p>
    </div>
    <div class="pt-2.5 border-t border-white/15">
      <span class="text-xs font-mono font-bold text-cyan-300">사내 최신 지식 탐색</span>
    </div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-amber-500/40 border-t-4 border-t-amber-400 bg-amber-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="w-8 h-8 rounded-lg bg-amber-500/20 flex items-center justify-center mb-3 text-amber-400">
        <span class="i-carbon:data-enrichment text-xl"></span>
      </div>
      <div class="text-base font-bold text-white mb-2">2. Augmentation (증강)</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        사용자의 원래 질문에 검색해 온 공식 사내 규정 원문을 합쳐서 프롬프트의 배경 맥락(Context)을 대폭 보강합니다.
      </p>
    </div>
    <div class="pt-2.5 border-t border-white/15">
      <span class="text-xs font-mono font-bold text-amber-300">공식 근거 문서 결합</span>
    </div>
  </div>
  <div v-click="3" class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="w-8 h-8 rounded-lg bg-emerald-500/20 flex items-center justify-center mb-3 text-emerald-400">
        <span class="i-carbon:document-view text-xl"></span>
      </div>
      <div class="text-base font-bold text-white mb-2">3. Generation (생성)</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        LLM에게 "제공된 사내 문서 내용에 우선하여 답하라"고 지시하여 사실성과 검증 가능성을 크게 높입니다.
      </p>
    </div>
    <div class="pt-2.5 border-t border-white/15">
      <span class="text-xs font-mono font-bold text-emerald-300">근거 우선 답변 작성</span>
    </div>
  </div>
</div>

<div v-click="3" class="p-3.5 rounded-xl border border-blue-500/30 bg-blue-950/25 flex items-center justify-between text-xs text-white/90 mt-4">
  <div class="flex items-center gap-2">
    <span class="i-carbon:checkmark-filled text-base text-cyan-400"></span>
    <span><strong>핵심 멘탈 모델:</strong> 기억에만 의존하는 암기 시험이 아닌, <strong>승인된 사내 문서를 펼쳐놓고 치는 '오픈북 시험'</strong> 방식으로 사실성을 높입니다. (※ 단, RAG 역시 원본 문서 오류까지 자동 해결하지는 못하므로 검증 필요)</span>
  </div>
</div>

<!--
[강사 멘트]
[click 1] 1단계(Retrieval): 질문이 들어오면 사내 DB에서 관련 문서를 실시간으로 먼저 찾습니다.
[click 2] 2단계(Augmentation): 찾아낸 공식 문서 텍스트를 질문과 하나로 합쳐 프롬프트에 주입합니다.
[click 3] 3단계(Generation): 모델에게 "오직 이 문서에 적힌 사실만으로 답하라"고 지시해 검증 가능성을 높입니다.
-->

---
title: 프롬프트의 본질과 역할
layout: default
class: px-16 py-9
glowSeed: 210
clicks: 3
---
<!-- slide:12-Prompt-As-Work-Order -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  프롬프트는 단순 질문이 아니라 AI에게 주는 '업무지시서'다
</h2>

<div class="grid grid-cols-4 gap-4 mt-4">
  <div class="p-4 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <span class="text-xs font-mono text-white/50 font-bold uppercase">1단계: 막연한 지시</span>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-rose-300 mt-2 mb-2 border border-rose-500/20">
        "홍보문 작성해줘."
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        대상, 채널, 목적이 없어 누구나 아는 뻔한 내용만 나열됩니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-rose-400">품질 최하 (재작업)</div>
  </div>
  <div v-click="1" class="p-4 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <span class="text-xs font-mono text-white/50 font-bold uppercase">2단계: 대상 추가</span>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-amber-300 mt-2 mb-2 border border-amber-500/20">
        "30대 직장인을 위한 홍보문을 작성해줘."
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        타깃은 생겼으나 발신자의 톤앤매너와 핵심 혜택이 모호합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-amber-400">품질 보통 (수정 필요)</div>
  </div>
  <div v-click="2" class="p-4 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <span class="text-xs font-mono text-white/50 font-bold uppercase">3단계: 관점 추가</span>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-sky-300 mt-2 mb-2 border border-sky-500/20">
        "마케팅 담당자 입장에서 30대 직장인용 홍보문 작성해줘."
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        전문적 어조는 갖추었으나 구체적인 출력 서식이 빠져 있습니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-sky-300">품질 양호</div>
  </div>
  <div v-click="3" class="p-4 rounded-2xl border border-cyan-500/50 border-t-4 border-t-cyan-400 bg-cyan-950/30 backdrop-blur-md flex flex-col justify-between h-76 shadow-lg">
    <div>
      <span class="text-xs font-mono text-cyan-400 font-bold uppercase">4단계: 업무지시서(RCTF)</span>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-cyan-300 mt-2 mb-2 border border-cyan-500/30">
        "역할 + 배경 맥락 + 구체적 작업 + 결과물 형식 + 제약 조건"
      </div>
      <p class="text-[11.5px] text-white/85 leading-relaxed m-0">
        원하는 결과물의 규격과 금지 사항을 명확히 정의해 한 번에 완성합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-cyan-300">실무 완성형</div>
  </div>
</div>

<!--
[강사 멘트]
[click 1] 2단계로 대상을 추가하고,
[click 2] 3단계로 관점을 지정하며,
[click 3] 4단계로 역할, 배경, 작업, 형식, 제약조건을 완전하게 갖추었을 때 실무에서 재작업 없는 완벽한 결과물을 얻을 수 있습니다.
-->

---
title: 실무 지시문 구성 원칙 (RCTF)
layout: default
class: px-16 py-8
glowSeed: 211
clicks: 1
---
<!-- slide:13-RCTF-Framework -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실무 지시문의 4가지 기본 틀 (RCTF 프레임워크)
</h2>

<div class="flex items-center justify-center my-3">
  <div class="rounded-2xl overflow-hidden border border-white/20 bg-white p-3 shadow-2xl transition-all duration-300">
    <img src="/rctf.png" alt="RCTF 프레임워크" class="rounded-xl max-h-74 w-auto object-contain" />
  </div>
</div>

<div v-click="1" class="flex items-center justify-center gap-4 text-xs font-mono font-bold text-white/80 mt-2 border-t border-white/10 pt-2.5">
  <span class="text-blue-400">R: 역할 부여</span>
  <span class="text-white/40">→</span>
  <span class="text-cyan-300">C: 배경 맥락 및 규정</span>
  <span class="text-white/40">→</span>
  <span class="text-sky-400">T: 구체적 작업 지시</span>
  <span class="text-white/40">→</span>
  <span class="text-indigo-300 font-bold">F: 표/양식 지정</span>
  <span class="text-white/40">|</span>
  <span class="text-amber-300">+ 제약 조건(Constraints)</span>
</div>

<!--
[강사 멘트]
RCTF는 프롬프트를 구조화하는 가장 검증된 실무용 기본 틀입니다.
역할(Role), 배경 맥락(Context), 구체적 작업(Task), 출력 형식(Format)에 더해 '제약 조건'을 명시하면 재질의 없이 원하는 결과물을 한 번에 얻을 수 있습니다.
-->

---
title: 좋은 프롬프트의 3대 필수 요소
layout: default
class: px-16 py-9
glowSeed: 212
clicks: 2
---
<!-- slide:14-Instruction-Data-Criteria -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  좋은 프롬프트의 3대 필수 요소: 지시 + 자료 + 기준
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="p-5 rounded-2xl border border-rose-500/30 bg-rose-950/20 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-rose-400 font-bold text-sm mb-2">
        <span class="i-carbon:close-filled text-base"></span>
        <span>단순 지시만 있는 경우</span>
      </div>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-white/80 mb-2 border border-rose-500/20">
        "매출 분석해줘."
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        분석할 원본 데이터와 판단 기준이 없어 피상적인 일반론만 답변합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-rose-400">자료·기준 누락</div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-amber-500/30 bg-amber-950/20 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-amber-400 font-bold text-sm mb-2">
        <span class="i-carbon:help-filled text-base"></span>
        <span>자료만 첨부한 경우</span>
      </div>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-white/80 mb-2 border border-amber-500/20">
        "다음 매출 데이터를 분석해줘. [데이터 첨부]"
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        데이터는 있으나 어떤 지표(증감률/원인 등)를 어떤 형식으로 볼지 기준이 모호합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-amber-400">판단 기준 모호</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm mb-2">
        <span class="i-carbon:checkmark-filled text-base"></span>
        <span>지시 + 자료 + 기준 결합</span>
      </div>
      <div class="p-3 rounded-xl bg-black/60 text-xs font-mono text-emerald-300 mb-2 border border-emerald-500/20 leading-relaxed text-[11px]">
        "다음 매출 데이터를 분석하되,<br/>
        1. 전년 대비 증감률을 계산하고<br/>
        2. 상위 3개 요인을 표로 정리하라."
      </div>
      <p class="text-[11.5px] text-white/85 leading-relaxed m-0">
        명확한 계산 기준과 서식이 주어져 바로 보고서에 쓸 수 있는 결과가 완성됩니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">실무 표준 프롬프트</div>
  </div>
</div>

<!--
[강사 멘트]
AI에게 질문할 때는 항상 지시(Task) + 자료(Data) + 기준(Criteria)의 3박자를 갖추었는지 점검해야 합니다.
-->

---
title: 프롬프트 품질 고도화: Zero-shot vs Few-shot
layout: default
class: px-16 py-9
glowSeed: 213
clicks: 1
---
<!-- slide:15-Few-Shot-Prompting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  프롬프트 품질 고도화: Zero-shot vs Few-shot
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-5 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-white/70 font-bold text-sm mb-2">
        <span class="i-carbon:flash text-base"></span>
        <span>Zero-shot (예시 없는 직접 지시)</span>
      </div>
      <div class="p-3 rounded-xl bg-black/60 font-mono text-xs text-white/80 mb-2 border border-white/10">
        "이 고객 문의를 분류해줘: [문의 내용]"
      </div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        모델이 자체 판단으로 분류하므로 사내에서 원하는 특정 분류 코드나 형식과 어긋날 수 있습니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/50">단순 질의 시 활용</div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-cyan-400 font-bold text-sm mb-2">
        <span class="i-carbon:data-table text-base"></span>
        <span>Few-shot (1~2개 예시 제공)</span>
      </div>
      <div class="p-3 rounded-xl bg-black/60 font-mono text-[11px] text-cyan-300 mb-2 border border-cyan-500/20 leading-relaxed">
        "예시 1: '결제 오류' ➔ [시스템/긴급]<br/>
        예시 2: '단가 문의' ➔ [영업/일반]<br/>
        위 기준에 따라 다음 문의를 분류하라: [문의 내용]"
      </div>
      <p class="text-xs text-white/85 leading-relaxed m-0">
        원하는 패턴과 출력 형식을 예시로 학습시켜 <strong>일관성과 정확도를 95% 이상으로 극대화</strong>합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-cyan-300">정형 업무 표준화에 필수</div>
  </div>
</div>

<!--
[강사 멘트]
반복 업무나 정형화된 보고서를 만들 때는 1~2개의 모범 예시를 주는 Few-shot 기법을 쓰면 원하는 서식을 한 번에 고정할 수 있습니다.
-->

---
title: 사용자 맞춤설정 (Custom Instructions)
layout: default
class: px-16 py-10
glowSeed: 214
clicks: 2
---
<!-- slide:16-Custom-Instructions -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  사용자 맞춤설정: 매번 반복하지 않는 기본 업무 환경 구축
</h2>

<div class="grid grid-cols-2 gap-8">
  <div v-click="1" class="p-6 rounded-2xl border border-blue-500/30 border-t-4 border-t-blue-400 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-blue-400 font-bold text-sm mb-3">
        <span class="i-carbon:user-profile text-base"></span>
        <span>1. 나의 기본 정보 & 역할 정의</span>
      </div>
      <p class="text-xs text-white/70 leading-relaxed m-0 mb-4">
        "내가 누구인지, 어떤 업무를 주로 담당하는지"를 미리 등록해 두면 모든 대화에서 AI가 자동으로 내 역할을 인지합니다.
      </p>
    </div>
    <div class="p-3 rounded-xl bg-black/60 font-mono text-xs text-blue-300 border border-blue-500/20">
      "국내 에너지 및 제조 기업의 실무 담당자 관점에서 답변할 것"
    </div>
  </div>
  <div v-click="2" class="p-6 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm mb-3">
        <span class="i-carbon:settings-adjust text-base"></span>
        <span>2. 기본 출력 규칙 & 서식 고정</span>
      </div>
      <p class="text-xs text-white/70 leading-relaxed m-0 mb-4">
        "AI가 어떻게 대답해야 하는지" 기본 톤앤매너와 양식을 고정하여 매번 긴 프롬프트를 칠 필요를 없앱니다.
      </p>
    </div>
    <div class="p-3 rounded-xl bg-black/60 font-mono text-xs text-emerald-300 border border-emerald-500/20">
      "보고서용 격식체(~함, ~음), 불필요한 미사여구 제거, 표 우선 출력"
    </div>
  </div>
</div>

<!--
[강사 멘트]
맞춤설정을 한 번만 세팅해 두면 "전문가 입장에서 써줘", "표로 만들어줘"라는 지시를 매번 반복할 필요가 없습니다.
-->

---
title: AI 입력 전 3초 점검
layout: default
class: px-16 py-9
glowSeed: 215
clicks: 3
---
<!-- slide:17-Security-Check -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI 입력 전 필수 3초 점검: 정보 유출 방지와 회사 자산 보호
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div v-click="1" class="p-5 rounded-2xl border border-rose-500/40 border-t-4 border-t-rose-400 bg-rose-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-rose-400 font-bold text-sm mb-2">
        <span class="i-carbon:user-avatar-filled-alt text-base"></span>
        <span>1. 개인정보 익명화</span>
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        고객 이름, 주민번호, 전화번호, 이메일, 계좌번호 등 개인 식별 정보를 '○○○' 또는 가명으로 마스킹 후 입력합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-rose-400">개인정보보호법 준수</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-amber-500/40 border-t-4 border-t-amber-400 bg-amber-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-amber-400 font-bold text-sm mb-2">
        <span class="i-carbon:locked text-base"></span>
        <span>2. 기업 대외비 및 단가 보호</span>
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        미공개 사업계획, 공급 원가, 내부 결재선, 고객사 계약 조건 등 민감한 경영 정보의 입력을 엄격히 금지합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-amber-300">영업비밀 보호</div>
  </div>
  <div v-click="3" class="p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-cyan-400 font-bold text-sm mb-2">
        <span class="i-carbon:data-check text-base"></span>
        <span>3. 학습 제외(Opt-out) 설정</span>
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        도구 설정에서 '데이터 분석 및 모델 학습에 대화 내용 활용 금지' 옵션을 활성화하여 기업 데이터를 보호합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-cyan-300">보안 옵션 기본 설정</div>
  </div>
</div>

<!--
[강사 멘트]
AI 프롬프트를 전송하기 전 3초만 점검하십시오. 개인정보 마스킹, 대외비 단가 제외, 학습 제외 설정 3가지는 사내 보안의 기본입니다.
-->

---
title: 실습 전 점검: 실무 프롬프트 5초 체크리스트
layout: default
class: px-14 py-7
glowSeed: 301
---
<!-- slide:18-Prompt-Checklist -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  실습 전 점검: 실무 프롬프트 5초 체크리스트
</h2>

<PromptChecklistInteractive />

<!--
[강사 멘트]
본격적인 실습에 들어가기 전, 우리가 작성한 프롬프트가 5대 기준을 충족하는지 직접 클릭하여 점검해 보겠습니다.
-->

---
title: 실습 과제 및 루브릭
layout: default
class: px-14 py-7
glowSeed: 302
---
<!-- slide:19-Mission-Card -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  1차시 실습: 내 업무에 바로 쓰는 RCTF 실무 프롬프트 작성
</h2>

<div class="grid grid-cols-12 gap-5 mt-2">
  <div class="col-span-5 p-4 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-400 uppercase font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon:task text-base"></span>
        <span>실습 과제 (택 1)</span>
      </div>
      <ul class="text-xs text-white/85 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li><strong>과제 A:</strong> 사내 업무 효율화를 위한 신규 소프트웨어 도입 기획서 초안 작성 프롬프트</li>
        <li><strong>과제 B:</strong> 최근 시장 동향 보고서 요약 및 3대 시사점 도출 비교표 생성 프롬프트</li>
        <li><strong>과제 C:</strong> 고객사 문의 유형별 표준 대응 매뉴얼(FAQ) 작성 프롬프트</li>
      </ul>
    </div>
    <div class="text-[11px] text-cyan-300/80 mt-2">
      ※ 본인의 실제 담당 업무를 주제로 자유롭게 작성하셔도 좋습니다.
    </div>
  </div>
  <div class="col-span-7 p-4 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-400 uppercase font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon:rule text-base"></span>
        <span>평가 기준 (Rubric)</span>
      </div>
      <div class="space-y-1.5 text-xs text-white/90">
        <div class="p-2 rounded bg-black/40 border border-white/10">
          <strong>① 역할 & 맥락 (30점):</strong> 발신자 역할과 배경 상황이 구체적으로 제시되었는가?
        </div>
        <div class="p-2 rounded bg-black/40 border border-white/10">
          <strong>② 작업 & 서식 (40점):</strong> 명확한 동사 지시와 표/글머리 출력 양식이 지정되었는가?
        </div>
        <div class="p-2 rounded bg-black/40 border border-white/10">
          <strong>③ 제약 & 보안 (30점):</strong> 금지 사항(분량, 어조, 개인정보 마스킹)이 완비되었는가?
        </div>
      </div>
    </div>
  </div>
</div>

<div class="mt-2.5 p-2.5 rounded-xl border border-white/15 bg-white/5 flex items-center justify-between text-xs text-white/80">
  <span>💡 작성한 프롬프트를 AI 도구(ChatGPT, Gemini 등)에 직접 입력하고 출력 결과를 확인합니다.</span>
  <span class="font-mono text-cyan-300 font-bold">실습 시간: 15분</span>
</div>

<!--
[실습 안내]
15분 동안 본인의 실무 주제를 선택하여 RCTF 구조의 프롬프트를 작성하고 AI에 입력해 보시기 바랍니다.
-->

---
title: 실습 중 자주 발생하는 2대 오류 해결 가이드
layout: default
class: px-16 py-9
glowSeed: 303
clicks: 2
---
<!-- slide:20-Troubleshooting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-6">
  실습 중 자주 발생하는 2대 오류 및 해결 방법
</h2>

<div class="grid grid-cols-2 gap-8">
  <div v-click="1" class="p-6 rounded-2xl border border-rose-500/30 border-t-4 border-t-rose-400 bg-rose-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-rose-400 font-bold text-sm mb-3">
        <span class="i-carbon:warning-filled text-base"></span>
        <span>오류 1: 답변이 너무 뻔하고 원론적인 경우</span>
      </div>
      <p class="text-xs text-white/80 leading-relaxed mb-3">
        지시문이 너무 단순하여 인터넷의 일반적인 상식 수준에서 대답하는 현상입니다.
      </p>
    </div>
    <div class="p-3.5 rounded-xl bg-black/60 border border-rose-500/30 text-xs text-rose-300 font-mono">
      해결: 배경 맥락(Context)에 사내 현황, 대상 고객군, 해결하려는 구체적 문제를 추가합니다.
    </div>
  </div>
  <div v-click="2" class="p-6 rounded-2xl border border-amber-500/30 border-t-4 border-t-amber-400 bg-amber-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-amber-400 font-bold text-sm mb-3">
        <span class="i-carbon:misuse text-base"></span>
        <span>오류 2: AI가 없는 사실을 지어내는 경우</span>
      </div>
      <p class="text-xs text-white/80 leading-relaxed mb-3">
        확인되지 않은 비용이나 세부 규정을 물었을 때 모델이 임의의 수치를 생성할 수 있습니다.
      </p>
    </div>
    <div class="p-3.5 rounded-xl bg-black/60 border border-amber-500/30 text-xs text-amber-300 font-mono">
      해결: "명시되지 않은 항목은 '담당자 확인 필요'로 표기할 것" 제약 조건을 지시문에 명시합니다.
    </div>
  </div>
</div>

<!--
[강사 멘트]
실습 중 답변이 모호하다면 맥락(C)을 보강하고, 허위 답변이 발생한다면 '확인 불가 시 보류' 제약 조건을 지시문에 추가해 주시면 됩니다.
-->

---
title: 1차시 핵심 요약 및 공식
layout: center
class: text-center px-12
glowSeed: 401
---
<!-- slide:21-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-xs font-mono text-cyan-300 mb-5">
    <span>1차시 핵심 공식</span>
  </div>
  <div class="p-6 rounded-2xl border border-white/20 bg-white/5 backdrop-blur-md shadow-2xl max-w-3xl mb-6">
    <div class="text-2xl font-black text-white tracking-tight leading-relaxed">
      좋은 AI 활용 = <span class="text-cyan-400">좋은 지시(RCTF)</span> + <span class="text-amber-400">좋은 자료(근거)</span> + <span class="text-emerald-400">결과 검증</span>
    </div>
  </div>
  <h3 class="text-lg font-medium text-white/80 leading-relaxed max-w-2xl mb-6">
    AI는 알아서 정답을 알려주는 도구가 아니라,<br/>
    우리가 제공한 <strong>지시·자료·기준</strong>을 바탕으로 결과를 만드는 도구입니다.
  </h3>

  <div class="flex items-center gap-4 text-xs text-white/50 font-mono">
    <span class="px-4 py-1.5 rounded-xl bg-white/5 border border-white/10">다음 차시 예고: 구글 제미나이 노트북과 심층 리서치 실무 활용</span>
  </div>
</div>

<!--
[마무리]
1차시 수고하셨습니다.
AI 활용의 본질은 "좋은 지시 + 좋은 자료 + 결과 검증"입니다.
다음 2차시에서는 구글 제미나이 노트북과 심층 리서치를 활용해 대용량 문서를 분석하고 신뢰할 수 있는 리포트를 작성하는 실무를 다루겠습니다.
-->

---
layout: default
glow: none
---
<!-- slide:22-Divider-Session-2 -->

<SectionPartDivider
  part="2차시"
  title="생성형 AI로 조사하고 정리하기"
  subtitle="검색에서 리서치, 리서치에서 결과물까지: ChatGPT 웹검색 · 심층 리서치 · Gemini Notebook · Canvas"
  image="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop"
/>

<!--
[강사 멘트]
2차시를 시작하겠습니다.
1차시에서 'AI에게 일을 잘 시키는 지시법(RCTF)'을 배웠다면, 2차시는 'AI에게 좋은 자료를 찾아주고 그 자료를 근거로 일을 시키는 법'을 직접 도구로 실습하는 시간입니다.
-->

---
title: 검색과 리서치의 차이
layout: default
class: px-16 py-9
glowSeed: 502
clicks: 2
---
<!-- slide:24-Search-vs-Research -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  검색과 리서치는 어떻게 다를까?
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="p-5 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-white/70 font-bold text-sm mb-2">
        <span class="i-carbon:search text-lg"></span>
        <span>1. 일반 검색</span>
      </div>
      <div class="text-xs font-mono text-white/50 mb-3">"무엇이 있는가?"</div>
      <ul class="text-xs text-white/75 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li>키워드 기반 링크 및 웹페이지 나열</li>
        <li>사용자가 문서를 직접 클릭하여 확인</li>
        <li>단편적인 사실이나 최신 단가 확인에 적합</li>
      </ul>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/50">단순 링크 탐색</div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-cyan-300 font-bold text-sm mb-2">
        <span class="i-carbon:bot text-lg text-cyan-400"></span>
        <span>2. AI 웹검색</span>
      </div>
      <div class="text-xs font-mono text-cyan-300 mb-3">"핵심만 빠르게 요약"</div>
      <ul class="text-xs text-white/80 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li>검색된 여러 웹 문서를 LLM이 종합 요약</li>
        <li>출처 링크와 함께 핵심 내용 제시</li>
        <li>빠른 트렌드 파악 및 배경 조사에 적합</li>
      </ul>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-cyan-300 font-bold">자료 탐색 및 요약</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm mb-2">
        <span class="i-carbon:data-structured text-lg text-emerald-400"></span>
        <span>3. 심층 리서치 (Deep Research)</span>
      </div>
      <div class="text-xs font-mono text-emerald-300 mb-3">"비교·분석하여 보고서화"</div>
      <ul class="text-xs text-white/85 space-y-1.5 pl-4 m-0 leading-relaxed">
        <li>수십 개 원천 문서를 심층 탐색 및 대조</li>
        <li>상충되는 정보 검증 및 데이터 종합</li>
        <li>판단 가능한 구조화된 실무 리포트 생성</li>
      </ul>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono text-emerald-300 font-bold">의사결정용 결과물 완성</div>
  </div>
</div>

<div v-click="2" class="mt-4 p-3 rounded-xl border border-cyan-500/30 bg-cyan-950/25 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:checkmark-filled text-base text-cyan-400"></span>
    <span><strong>핵심 차이:</strong> <strong>검색</strong>은 '자료를 찾는 것'이고, <strong>리서치</strong>는 '자료를 조사하여 판단 가능한 형태로 정리하는 것'입니다.</span>
  </div>
</div>

<!--
[강사 멘트]
검색은 링크를 찾는 단계이지만, 리서치는 여러 자료를 비교 검증하여 업무에 바로 쓸 수 있는 보고서 형태로 만드는 과정입니다.
-->

---
title: 좋은 리서치의 4단계
layout: default
class: px-16 py-9
glowSeed: 503
clicks: 3
---
<!-- slide:25-Research-4-Steps -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  신뢰할 수 있는 업무 리서치의 4단계 흐름
</h2>

<div class="grid grid-cols-4 gap-4 mt-4">
  <div class="p-4 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-blue-400 font-bold uppercase">Step 01</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">질문 정의</div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        무엇을 알고 싶은지 명확한 목표와 범위를 구체적으로 설정합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-blue-300">조사 목적 명확화</div>
  </div>
  <div v-click="1" class="p-4 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-cyan-400 font-bold uppercase">Step 02</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">자료 탐색</div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        신뢰할 수 있는 공공 데이터, 전문 보고서, 공식 문서를 다각도로 수집합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-cyan-300">신뢰 소스 확보</div>
  </div>
  <div v-click="2" class="p-4 rounded-2xl border border-amber-500/30 bg-amber-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-amber-400 font-bold uppercase">Step 03</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">자료 비교·검증</div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        자료 간 수치 차이나 상충 내용을 대조하여 사실 여부를 교차 확인합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-amber-300">교차 대조 및 검증</div>
  </div>
  <div v-click="3" class="p-4 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md flex flex-col justify-between h-72 shadow-lg">
    <div>
      <span class="text-xs font-mono text-emerald-400 font-bold uppercase">Step 04</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">결과물 작성</div>
      <p class="text-xs text-white/85 leading-relaxed m-0">
        수집된 근거를 바탕으로 보고서, 표, 브리핑 자료로 체계화합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">실무 문서 완성</div>
  </div>
</div>

<div v-click="3" class="mt-4 p-3.5 rounded-xl border border-rose-500/30 bg-rose-950/20 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:warning-filled text-base text-rose-400"></span>
    <span><strong>주의 원칙:</strong> AI가 요약해 주었다고 해서 리서치가 끝난 것이 아닙니다. <strong>원본 출처와의 교차 검증</strong>이 반드시 수반되어야 합니다.</span>
  </div>
</div>

<!--
[강사 멘트]
AI는 자료 탐색과 초안 정리를 도와주는 조수입니다.
AI가 만든 문장을 그대로 믿기보다 3단계 비교 검증을 거치는 것이 실무자의 핵심 역할입니다.
-->

---
title: 웹검색을 잘하는 질문법
layout: default
class: px-16 py-9
glowSeed: 504
clicks: 2
---
<!-- slide:26-Search-Prompting -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  웹검색을 잘하는 질문: 검색도 결국 프롬프트다
</h2>

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="p-6 rounded-2xl border border-rose-500/40 border-t-4 border-t-rose-400 bg-rose-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-rose-400 font-bold text-base mb-3">
        <span class="i-carbon:close-filled text-xl"></span>
        <span>단순 검색 (정보의 홍수)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-black/60 font-mono text-xs text-white/80 mb-3 border border-rose-500/20">
        "2026년 AI 트렌드 알려줘."
      </div>
      <p class="text-xs text-white/70 m-0 leading-relaxed">
        범위와 관점이 없어 포괄적이고 피상적인 인터넷 뉴스 헤드라인만 단순 나열됩니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-rose-400">실무 활용도 낮음</div>
  </div>
  <div v-click="1" class="p-6 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center gap-2 text-emerald-400 font-bold text-base mb-3">
        <span class="i-carbon:checkmark-filled text-xl"></span>
        <span>좋은 검색 질문 (구조화된 지시)</span>
      </div>
      <div class="p-3.5 rounded-xl bg-black/60 font-mono text-[11px] text-emerald-300 mb-3 border border-emerald-500/20 leading-relaxed">
        "2026년 국내 중소기업의 생성형 AI 활용 트렌드를 조사하라.<br/>
        1. 최근 6개월 내 자료를 우선 반영할 것<br/>
        2. 실제 기업 활용 사례와 도입 효과를 구분하여 정리할 것<br/>
        3. 각 주장마다 원문 출처(URL)를 제시할 것"
      </div>
      <p class="text-xs text-white/80 m-0 leading-relaxed">
        시기, 대상, 출력 기준, 출처 요구조건이 명시되어 바로 보고서에 인용할 수 있습니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono text-emerald-300 font-bold">1차시 RCTF의 검색 적용</div>
  </div>
</div>

<div v-click="2" class="mt-4 p-3 rounded-xl border border-cyan-500/30 bg-cyan-950/25 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:light text-base text-cyan-400"></span>
    <span><strong>핵심 포인트:</strong> 검색 엔진에 넣는 질문도 결국 <strong>1차시에서 배운 RCTF 구조의 프롬프트</strong>입니다.</span>
  </div>
</div>

<!--
[강사 멘트]
검색창에 단어 하나만 치는 것이 아니라, 우리가 원하는 시기와 대상, 출처 요구사항을 함께 명시하면 훨씬 정교한 리서치 결과를 얻을 수 있습니다.
-->

---
title: NotebookLM에서 Gemini Notebook으로의 진화
layout: default
class: px-16 py-8 text-center flex flex-col justify-center items-center
glowSeed: 501
clicks: 1
---
<!-- slide:23-Brand-Evolution -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4 text-center">
  Google NotebookLM에서 Gemini Notebook으로의 진화
</h2>

<BrandEvolution :stage="$clicks" />

<!--
[강사 멘트]
구글의 강력한 문서 기반 AI 도구였던 'NotebookLM'이 최근 'Gemini Notebook'으로 공식 진화했습니다.
[click] 기존의 RAG 분석 엔진에 최신 Gemini 1.5 Pro 모델과 9가지 실무 Studio 생성 기능이 결합되어 실무 리서치 생산성을 극대화합니다.
-->

---
title: Gemini Notebook의 개념과 정의
layout: default
class: px-16 py-9
glowSeed: 505
clicks: 1
---
<!-- slide:27-Gemini-Notebook-Intro -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  Gemini Notebook: 내가 제공한 자료 기반의 AI 작업공간
</h2>

<div class="p-6 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/20 backdrop-blur-md shadow-xl mt-3">
  <div class="text-lg font-bold text-white mb-2 leading-relaxed">
    "검색하는 AI가 아니라, <span class="text-cyan-300">내가 가진 자료를 구조화해주는 AI</span>"
  </div>
  <p class="text-xs text-white/80 m-0 leading-relaxed mb-6">
    사용자가 직접 업로드한 PDF, 웹 URL, 회의록, 유튜브 영상만을 '기반 지식'으로 삼아 <strong>할루시네이션(환각) 리스크를 3배 이상 낮추고</strong>, 클릭 가능한 번호 인용(Citation)으로 완벽한 사실 검증을 제공합니다.
  </p>
  <div class="grid grid-cols-4 gap-4 pt-4 border-t border-white/10 text-center">
    <div class="p-3.5 rounded-xl bg-black/50 border border-white/10">
      <div class="text-xs font-mono text-cyan-400 font-bold mb-1">1. 자료 넣기 (Source)</div>
      <div class="text-xs text-white/90 font-bold">PDF · 웹 · 유튜브 등록</div>
    </div>
    <div class="p-3.5 rounded-xl bg-black/50 border border-white/10">
      <div class="text-xs font-mono text-cyan-400 font-bold mb-1">2. 질문하기 (Chat)</div>
      <div class="text-xs text-white/90 font-bold">자료 기반 심층 질의</div>
    </div>
    <div class="p-3.5 rounded-xl bg-black/50 border border-white/10">
      <div class="text-xs font-mono text-cyan-400 font-bold mb-1">3. 근거 확인 (Citation)</div>
      <div class="text-xs text-white/90 font-bold">원문 인용 페이지 대조</div>
    </div>
    <div class="p-3.5 rounded-xl bg-black/50 border border-emerald-500/30 text-center">
      <div class="text-xs font-mono text-emerald-400 font-bold mb-1">4. 결과 생성 (Studio)</div>
      <div class="text-xs text-white/90 font-bold">9대 실무 문서 변환</div>
    </div>
  </div>
</div>

<div v-click="1" class="mt-4 p-3.5 rounded-xl border border-white/15 bg-white/5 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:idea text-base text-cyan-300"></span>
    <span><strong>핵심 차별점:</strong> 인터넷의 불확실한 지식이 아닌, <strong>내가 선별한 승인 문서만을 진실의 기준</strong>으로 삼아 작업합니다.</span>
  </div>
  <span class="text-xs font-mono text-cyan-300 font-bold">RAG 기반 무(無)환각 작업공간</span>
</div>

<!--
[강사 멘트]
Gemini Notebook은 인터넷 전체가 아니라, 내가 직접 넣은 문서만을 바탕으로 작동하기 때문에 오답과 거짓말을 획기적으로 줄여줍니다.
-->

---
title: 1차시 RAG 이론의 실제 도구 구현 다이어그램
layout: default
class: px-16 py-7
glowSeed: 506
clicks: 2
---
<!-- slide:28-RAG-in-Notebook -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  1차시 RAG 이론 ➔ 2차시 Gemini Notebook 구현 다이어그램
</h2>

<RagToNotebookDiagram :stage="$clicks" />

<!--
[강사 멘트]
1차시에서 배웠던 RAG 이론의 3단계(검색-증강-생성)가,
[click 1] Gemini Notebook에서는 '자료 업로드(Source) ➔ 자동 색인 ➔ 질의(Chat) ➔ 원문 인용(Citation)'이라는 4단계 워크플로우로 1:1 자동 구현됩니다.
[click 2] 복잡한 RAG 개발 없이도 누구나 '자료를 넣고 묻는다'는 직관적인 방식으로 RAG를 업무에 활용할 수 있습니다.
-->

---
title: Gemini Notebook 3단 화면 구조와 4대 핵심 기능
layout: default
class: px-14 py-5
glowSeed: 507
clicks: 3
---
<!-- slide:29-Notebook-4-Features -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-1 text-center">
  Gemini Notebook의 3단 화면 구조와 4대 핵심 기능
</h2>

<div class="flex flex-col items-center justify-center">
  <div class="rounded-2xl overflow-hidden border border-white/20 bg-white p-1.5 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.7)] flex items-center justify-center my-1.5">
    <img
      src="/gemini-notebook-ui.png"
      alt="Gemini Notebook 3단 UI"
      class="rounded-xl h-60 w-auto object-contain select-none shadow-sm aspect-[1024/488]"
    />
  </div>
  <div class="grid grid-cols-3 gap-3.5 w-full max-w-4xl mt-2">
    <div v-click="1" class="p-2.5 rounded-xl border border-blue-500/30 border-t-3 border-t-blue-400 bg-blue-950/30 backdrop-blur-md text-left">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-mono font-bold text-blue-400">① Source (좌측 패널)</span>
        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-300">자료 등록</span>
      </div>
      <p class="text-[11px] text-white/80 m-0 leading-tight">PDF 문서, 웹 URL, 유튜브 링크 등 분석할 원본 문서 등록 및 선별</p>
    </div>
    <div v-click="2" class="p-2.5 rounded-xl border border-cyan-500/30 border-t-3 border-t-cyan-400 bg-cyan-950/30 backdrop-blur-md text-left">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-mono font-bold text-cyan-400">② Chat & ③ Citation (중앙)</span>
        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300">질문 & 대조</span>
      </div>
      <p class="text-[11px] text-white/80 m-0 leading-tight">자료 기반 질문 및 답변 번호 인용구 클릭 원문 즉시 확인</p>
    </div>
    <div v-click="3" class="p-2.5 rounded-xl border border-emerald-500/40 border-t-3 border-t-emerald-400 bg-emerald-950/30 backdrop-blur-md shadow-lg text-left">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-mono font-bold text-emerald-400">④ Studio (우측 패널)</span>
        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300">산출물 변환</span>
      </div>
      <p class="text-[11px] text-white/85 m-0 leading-tight">보고서, 마인드맵, 오디오 등 9대 실무 산출물 원클릭 생성</p>
    </div>
  </div>
</div>

<!--
[강사 멘트]
화면에 보이는 3단 구조가 Gemini Notebook의 핵심 작업대입니다.
[click 1] 좌측 Source에서 자료를 올리고,
[click 2] 중앙 Chat에서 묻고 Citation으로 원문을 확인하며,
[click 3] 우측 Studio에서 9대 맞춤형 산출물로 즉시 변환합니다.
-->

---
title: Gemini Notebook을 잘 쓰는 3가지 원칙
layout: default
class: px-16 py-9
glowSeed: 508
clicks: 3
---
<!-- slide:30-Notebook-3-Rules -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Gemini Notebook을 효과적으로 활용하는 3가지 실무 원칙
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div v-click="1" class="p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-cyan-400 font-bold uppercase mb-1">원칙 01</div>
      <div class="text-sm font-bold text-white mb-2">입력 자료 품질이 곧 결과의 품질</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        AI는 제공된 문서만을 기준으로 판단합니다. 오래된 규정이나 버전이 다른 문서를 섞어두면 그대로 인용하므로, <strong>사전 문서 정리 후 선별 업로드</strong>가 핵심입니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono text-cyan-300">자료의 양보다 신선도·정확성</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-amber-500/40 border-t-4 border-t-amber-400 bg-amber-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-amber-400 font-bold uppercase mb-1">원칙 02</div>
      <div class="text-sm font-bold text-white mb-2">질문은 구체적으로 (S-A-F)</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        단순히 "요약해줘"보다 "A문서와 B문서의 차이점을 표로 정리하고, 정책 변화 3가지의 원문 근거를 찾아줘"처럼 명확한 비교 작업을 지시합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono text-amber-300">구체적 지시문(S-A-F) 작성</div>
  </div>
  <div v-click="3" class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-emerald-400 font-bold uppercase mb-1">원칙 03</div>
      <div class="text-sm font-bold text-white mb-2">해석은 AI가, 최종 판단은 사람이</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        NotebookLM은 읽고 정리하는 시간을 단축하는 도구입니다. 답변에 달린 번호 인용(Citation)을 클릭해 원문 위치를 반드시 눈으로 확인하고 최종 의사결정을 내립니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono text-emerald-300">원문 대조 및 책임성 검증</div>
  </div>
</div>

<!--
[강사 멘트]
자료를 잘 골라 넣고, 구체적으로 묻고, 인용을 클릭해 원문을 확인하는 것. 이 세 가지만 지키면 업무 실수를 100% 방지할 수 있습니다.
-->

---
title: Gemini Notebook 프롬프트 공식 (S-A-F)
layout: default
class: px-16 py-9
glowSeed: 509
clicks: 2
---
<!-- slide:31-SAF-Framework -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Gemini Notebook 프롬프트 공식: S-A-F
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-5 p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-400 uppercase font-bold mb-2">1차시 RCTF의 Notebook 간소화</div>
      <div class="space-y-3">
        <div class="p-2.5 rounded-lg bg-black/50 border border-blue-500/30">
          <span class="text-xs font-mono font-bold text-blue-400">S (Source):</span>
          <span class="text-xs text-white/85 block mt-0.5">어떤 자료를 기준으로 분석할 것인가?</span>
        </div>
        <div class="p-2.5 rounded-lg bg-black/50 border border-sky-500/30">
          <span class="text-xs font-mono font-bold text-sky-400">A (Action):</span>
          <span class="text-xs text-white/85 block mt-0.5">자료에서 무엇을 추출하고 비교할 것인가?</span>
        </div>
        <div class="p-2.5 rounded-lg bg-black/50 border border-emerald-500/30">
          <span class="text-xs font-mono font-bold text-emerald-400">F (Format):</span>
          <span class="text-xs text-white/85 block mt-0.5">어떤 양식(표, 글머리, 비교표)으로 받을 것인가?</span>
        </div>
      </div>
    </div>
    <div class="text-[11px] font-mono text-cyan-300 pt-2 border-t border-white/10">
      1차시 지시 체계 ➔ 2차시 자료 분석 체계
    </div>
  </div>
  <div v-click="1" class="col-span-7 p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-400 uppercase font-bold mb-2">실무 적용 예시 (S-A-F)</div>
      <div class="p-4 rounded-xl bg-black/60 font-mono text-xs text-emerald-300 leading-relaxed border border-emerald-500/20">
        [Source]<br/>
        업로드된 '2026 국내 에너지 산업 동향 보고서'를 기준으로,<br/><br/>
        [Action]<br/>
        1. 최근 주요 시장 변화 5가지를 도출하고<br/>
        2. 각 항목마다 근거가 된 출처(페이지 번호)를 명시할 것<br/><br/>
        [Format]<br/>
        결과는 `표(변화 항목 | 세부 내용 | 원문 출처 | 시사점)` 형태로 정리하라.
      </div>
    </div>
    <div class="text-xs text-white/70 pt-2 border-t border-white/10">
      출처와 형식을 한 번에 고정하여 재작업 없이 즉시 문서화합니다.
    </div>
  </div>
</div>

<!--
[강사 멘트]
새로운 이론을 배울 필요 없습니다. 1차시에서 배운 틀을 '자료(Source) + 작업(Action) + 형식(Format)'으로 간결하게 줄여서 쓰시면 됩니다.
-->

---
title: 실습 ① ChatGPT 웹검색
layout: default
class: px-16 py-9
glowSeed: 601
---
<!-- slide:32-Practice-WebSearch -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ① ChatGPT 웹검색: 출처 확인과 핵심 추출
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-5 p-5 rounded-2xl border border-rose-500/30 bg-rose-950/20 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-rose-400 uppercase font-bold mb-2">Step 1: 단순 질문 테스트</div>
      <div class="p-3.5 rounded-xl bg-black/60 font-mono text-xs text-white/80 border border-rose-500/20 mb-3">
        "2026년 생성형 AI의 직장인 업무 활용 사례를 조사해줘."
      </div>
      <p class="text-xs text-white/70 leading-relaxed m-0">
        일반적인 검색 결과를 확인하고 출처의 구체성과 깊이를 관찰합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-rose-400">초기 질문 실행</div>
  </div>
  <div class="col-span-7 p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md flex flex-col justify-between h-76 shadow-lg">
    <div>
      <div class="text-xs font-mono text-cyan-400 uppercase font-bold mb-2">Step 2: 구조화된 개선 질문 실행</div>
      <div class="p-3.5 rounded-xl bg-black/60 font-mono text-[11px] text-cyan-300 border border-cyan-500/20 leading-relaxed mb-2">
        "2026년 국내 기업의 생성형 AI 도입 실무 사례를 웹에서 조사하라.<br/>
        1. 공공/민간 기업의 실제 적용 업무 분야 3개를 도출할 것<br/>
        2. 도입 전/후 업무 시간 단축 효과를 수치로 명시할 것<br/>
        3. 각 사례별 공식 보도자료 또는 리포트 링크를 표에 첨부할 것"
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        <strong>실습 목표:</strong> 검색 결과에서 자료 발견 ➔ 출처 URL 확인 ➔ 핵심 수치 추출까지 완료
      </p>
    </div>
    <div class="text-xs font-mono text-cyan-300 font-bold">실습 시간: 10분</div>
  </div>
</div>

<!--
[실습 안내]
10분간 ChatGPT 웹검색을 진행합니다. 단순 질문과 개선 질문의 차이를 직접 비교해 보시기 바랍니다.
-->

---
title: 실습 ② ChatGPT 심층 리서치 (Deep Research)
layout: default
class: px-16 py-8
glowSeed: 602
---
<!-- slide:33-Practice-DeepResearch -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  실습 ② ChatGPT 심층 리서치: 다각도 조사 및 리포트화
</h2>

<div class="grid grid-cols-12 gap-6 items-center">
  <div class="col-span-6 p-4 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/20 backdrop-blur-md shadow-xl flex flex-col justify-between h-80">
    <div>
      <div class="text-xs font-mono text-emerald-400 font-bold uppercase mb-1.5">실습 주제 선택 (택 1)</div>
      <div class="space-y-2 mb-3">
        <div class="p-2.5 rounded-lg bg-black/50 border border-white/10 text-xs text-white/90">
          <strong>주제 A:</strong> "생성형 AI가 기업 업무 생산성에 미치는 영향과 도입 장애요인"
        </div>
        <div class="p-2.5 rounded-lg bg-black/50 border border-white/10 text-xs text-white/90">
          <strong>주제 B:</strong> "2026년 국내 에너지 및 제조업 분야 AI 전환 트렌드"
        </div>
      </div>
      <p class="text-[11.5px] text-white/75 m-0 leading-relaxed">
        입력창의 <strong>[Deep research]</strong> 버튼을 활성화한 뒤 연구 질문을 입력합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-emerald-300 font-bold pt-2 border-t border-white/10">
      실습 시간: 15분 (다각도 웹 수십 개 문서 분석)
    </div>
  </div>
  <div class="col-span-6 flex flex-col items-center justify-center p-3 rounded-2xl border border-white/20 bg-white/5 backdrop-blur-md shadow-2xl h-80">
    <div class="rounded-xl overflow-hidden border border-white/20 shadow-lg bg-black/40">
      <img src="/de269090-e238-11ef-b53f-c8a9c246552c.png" alt="ChatGPT Deep Research UI" class="rounded-xl max-h-56 w-auto object-contain" />
    </div>
    <span class="text-[11px] font-mono text-cyan-300 mt-2">ChatGPT 입력창 하단 [Deep research] 활성화</span>
  </div>
</div>

<!--
[실습 안내]
15분간 심층 리서치를 실행하고, 생성된 다각도 분석 결과를 복사해 두시기 바랍니다.
-->

---
title: 실습 ③ Gemini Notebook에 다중 소스 등록
layout: default
class: px-16 py-9
glowSeed: 603
---
<!-- slide:34-Practice-Notebook-Sources -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ③ Gemini Notebook에 자료 넣기 (다중 소스 구축)
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-blue-400 font-bold text-sm mb-2">
        <span class="i-carbon:document-pdf text-lg"></span>
        <span>1. 문서 파일 (PDF)</span>
      </div>
      <p class="text-xs text-white/75 leading-relaxed m-0 mb-3">
        사내 가이드라인, 정부 정책 보고서, 연구 보고서 PDF 2~3개를 업로드합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-blue-300">공식 문서 색인</div>
  </div>
  <div class="p-5 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-cyan-400 font-bold text-sm mb-2">
        <span class="i-carbon:link text-lg"></span>
        <span>2. 웹사이트 링크 (URL)</span>
      </div>
      <p class="text-xs text-white/75 leading-relaxed m-0 mb-3">
        앞서 웹검색과 리서치에서 확인한 최신 통계 및 보도자료 URL 2~3개를 등록합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-cyan-300">최신 웹 소스 연동</div>
  </div>
  <div class="p-5 rounded-2xl border border-purple-500/30 bg-purple-950/20 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <div class="flex items-center gap-2 text-purple-400 font-bold text-sm mb-2">
        <span class="i-carbon:video text-lg"></span>
        <span>3. 영상/미디어 (YouTube)</span>
      </div>
      <p class="text-xs text-white/75 leading-relaxed m-0 mb-3">
        세미나 영상이나 설명회 유튜브 링크 1개를 등록하여 자막 텍스트를 즉시 추출합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-purple-300">영상 자막 자동 분석</div>
  </div>
</div>

<div class="mt-4 p-3.5 rounded-xl border border-cyan-500/30 bg-cyan-950/25 flex items-center justify-between text-xs text-white/90">
  <div class="flex items-center gap-2">
    <span class="i-carbon:settings-adjust text-base text-cyan-400"></span>
    <span><strong>실습 팁:</strong> 좌측 소스 목록에서 체크박스를 켜고 끔으로써 <strong>원하는 특정 자료만 선택해서 질문</strong>할 수 있습니다. (무료 계정 최대 50개 소스 지원)</span>
  </div>
  <span class="font-mono text-cyan-300 font-bold">실습 시간: 10분</span>
</div>

<!--
[실습 안내]
새 노트북을 만들고 제공된 실습 자료(PDF, 웹, 유튜브)를 등록해 보겠습니다.
-->

---
title: 실습 ④ 자료에 질문하기 (3단계 심화)
layout: default
class: px-16 py-9
glowSeed: 604
---
<!-- slide:35-Practice-Deep-Questioning -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ④ 자료에 질문하기: 질문의 깊이에 따른 3단계 실습
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="p-5 rounded-2xl border border-white/15 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-white/50 font-bold uppercase mb-1">Level 1: 기본 요약</div>
      <div class="p-3 rounded-xl bg-black/60 font-mono text-xs text-white/80 border border-white/10 mb-2">
        "이 자료의 핵심 내용을 3줄로 요약해줘."
      </div>
      <p class="text-[11.5px] text-white/70 leading-relaxed m-0">
        전체 문서의 기본 개요와 주제를 빠르게 파악합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/50">개요 파악</div>
  </div>
  <div class="p-5 rounded-2xl border border-cyan-500/30 bg-cyan-950/20 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-cyan-300 font-bold uppercase mb-1">Level 2: 핵심 주장 추출</div>
      <div class="p-3 rounded-xl bg-black/60 font-mono text-xs text-cyan-200 border border-cyan-500/20 mb-2">
        "이 자료에서 가장 중요한 핵심 주장 5개와 근거를 찾아줘."
      </div>
      <p class="text-[11.5px] text-white/80 leading-relaxed m-0">
        문서 내 주요 논점과 수치 데이터를 체계적으로 추출합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-cyan-300">구체적 근거 확보</div>
  </div>
  <div class="p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md flex flex-col justify-between h-76 shadow-lg">
    <div>
      <div class="text-xs font-mono text-emerald-300 font-bold uppercase mb-1">Level 3: 교차 검증 및 대조</div>
      <div class="p-3 rounded-xl bg-black/60 font-mono text-[11px] text-emerald-300 border border-emerald-500/20 mb-2 leading-relaxed">
        "PDF와 웹자료의 수치를 대조하고, 서로 다른 주장이 있다면 비교표로 정리해줘."
      </div>
      <p class="text-[11.5px] text-white/85 leading-relaxed m-0">
        여러 문서 간 상충점을 분석하고 <strong>번호 인용구를 클릭해 원문을 직접 검증</strong>합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/15 text-xs font-mono font-bold text-emerald-300">원문 인용 교차 검증</div>
  </div>
</div>

<!--
[실습 안내]
Level 1부터 Level 3까지 질문을 점진적으로 고도화하며 답변에 달리는 인용 버튼을 직접 클릭해 보겠습니다.
-->

---
title: 실습 ⑤ Studio 9대 맞춤형 결과물 변환
layout: default
class: px-14 py-7
glowSeed: 605
---
<!-- slide:36-Practice-Studio-Outputs -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  실습 ⑤ Studio: 9대 맞춤형 결과물 원클릭 변환
</h2>

<div class="grid grid-cols-12 gap-5 items-center">
  <div class="col-span-5 flex justify-center">
    <div class="rounded-2xl overflow-hidden border border-white/20 bg-white p-2 shadow-2xl w-full">
      <img src="/20223753r0xNU.jpg" alt="NotebookLM 9대 Studio 기능" class="rounded-xl w-full max-h-84 object-contain" />
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between h-84">
    <div class="grid grid-cols-1 gap-1.5 text-[11px] leading-tight">
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-blue-500/30 flex items-center justify-between">
        <span><strong class="text-blue-300">① AI 오디오 오버뷰:</strong> 긴 문서를 2인 대화형 팟캐스트 음성으로 요약 청취</span>
        <span class="text-[9px] font-mono text-blue-300">Audio</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-emerald-500/30 flex items-center justify-between">
        <span><strong class="text-emerald-300">② 동영상 개요:</strong> 시각적 슬라이드와 나레이션이 포함된 영상 설명 제작</span>
        <span class="text-[9px] font-mono text-emerald-300">Video</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-cyan-500/30 flex items-center justify-between">
        <span><strong class="text-cyan-300">③ 마인드맵:</strong> 복잡한 자료의 핵심 논리 구조를 시각적 노드 트리로 정리</span>
        <span class="text-[9px] font-mono text-cyan-300">Mind Map</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-indigo-500/30 flex items-center justify-between">
        <span><strong class="text-indigo-300">④ 보고서:</strong> 브리핑, 요약본, FAQ 등 정식 실무 보고서 초안 생성</span>
        <span class="text-[9px] font-mono text-indigo-300">Report</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-pink-500/30 flex items-center justify-between">
        <span><strong class="text-pink-300">⑤ 플래시카드:</strong> 핵심 개념과 용어를 질문-답변 카드로 자동 변환</span>
        <span class="text-[9px] font-mono text-pink-300">Flashcard</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-sky-500/30 flex items-center justify-between">
        <span><strong class="text-sky-300">⑥ 퀴즈:</strong> 내용 숙지 및 이해도 점검을 위한 셀프 테스트 문제 생성</span>
        <span class="text-[9px] font-mono text-sky-300">Quiz</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-purple-500/30 flex items-center justify-between">
        <span><strong class="text-purple-300">⑦ 인포그래픽 (베타):</strong> 복잡한 내용을 한 장의 시각적 요약 이미지로 생성</span>
        <span class="text-[9px] font-mono text-purple-300">Infographic</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-orange-500/30 flex items-center justify-between">
        <span><strong class="text-orange-300">⑧ 슬라이드 자료 (베타):</strong> 보고서 내용을 바탕으로 발표용 PPT 구조 자동 구성</span>
        <span class="text-[9px] font-mono text-orange-300">Slides</span>
      </div>
      <div class="p-1.5 px-2.5 rounded-lg bg-black/50 border border-amber-500/30 flex items-center justify-between">
        <span><strong class="text-amber-300">⑨ 데이터 표:</strong> 흩어진 비교 정보를 표로 정리하고 구글 시트로 내보내기</span>
        <span class="text-[9px] font-mono text-amber-300">Data Table</span>
      </div>
    </div>
    <div class="text-[10px] text-white/60 pt-1.5 border-t border-white/10 flex items-center justify-between">
      <span>💡 <strong>원칙:</strong> 동일한 원본 자료를 실무 목적에 맞춰 다양한 산출물로 즉시 변환</span>
      <span class="font-mono text-emerald-300 font-bold">실습 시간: 10분</span>
    </div>
  </div>
</div>

<!--
[실습 안내]
화면에 보이는 9가지 메뉴 중 원하는 형식(보고서, 마인드맵, 데이터 표 등)을 직접 클릭하여 결과를 확인해 보겠습니다.
-->

---
title: 실습 ⑥ 리서치 결과를 Canvas에서 정리하기
layout: default
class: px-16 py-9
glowSeed: 606
---
<!-- slide:37-Practice-Canvas -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ⑥ Canvas를 활용한 최종 업무 결과물 완성
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-5 p-5 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-400 uppercase font-bold mb-2">2차시 전체 리서치 워크플로우</div>
      <div class="space-y-2 text-xs font-mono">
        <div class="p-2 rounded bg-black/40 border border-white/10 text-white/70">1. ChatGPT 웹검색 (자료 탐색)</div>
        <div class="p-2 rounded bg-black/40 border border-white/10 text-white/70">2. Deep Research (심층 보고서)</div>
        <div class="p-2 rounded bg-black/40 border border-cyan-500/30 text-cyan-300">3. Gemini Notebook (자료 검증)</div>
        <div class="p-2 rounded bg-black/40 border border-emerald-500/30 text-emerald-300 font-bold">4. Canvas (최종 문서 편집)</div>
      </div>
    </div>
    <div class="text-xs text-white/60 pt-2 border-t border-white/10">
      단순 질의응답을 넘어 완결된 1개 문서를 완성
    </div>
  </div>
  <div class="col-span-7 p-5 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-400 uppercase font-bold mb-2">Canvas 실무 편집 4대 기능</div>
      <ul class="text-xs text-white/90 space-y-2 pl-4 m-0 leading-relaxed">
        <li><strong>부분 수정:</strong> 특정 문단만 드래그하여 "더 전문적인 어조로 수정"</li>
        <li><strong>길이 조절:</strong> "보고서용으로 50% 요약" 또는 "상세 근거 추가"</li>
        <li><strong>서식 변환:</strong> 줄글 문장을 "표(Table) 또는 글머리 기호"로 변경</li>
        <li><strong>문서 내보내기:</strong> 완성된 기획안을 클립보드 또는 구글 문서로 복사</li>
      </ul>
    </div>
    <div class="mt-3 p-2.5 rounded-lg bg-black/50 font-mono text-xs text-emerald-300 border border-emerald-500/30">
      목표: 바로 상사에게 보고할 수 있는 실무 문서 1종 완성
    </div>
  </div>
</div>

<!--
[실습 안내]
Notebook에서 추출한 인사이트를 Canvas로 가져와 문단을 다듬고 정식 보고서 양식으로 완성해 보겠습니다.
-->

---
title: 2차시 최종 실습 과제 (Mission)
layout: default
class: px-14 py-8
glowSeed: 701
---
<!-- slide:38-Session2-Mission -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  2차시 종합 실습: 내 업무에 바로 쓰는 리서치 결과물 완성
</h2>

<div class="grid grid-cols-12 gap-5 mt-2">
  <div class="col-span-5 p-4 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-cyan-400 uppercase font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon:task text-base"></span>
        <span>리서치 주제 선택 (택 1)</span>
      </div>
      <ul class="text-xs text-white/85 space-y-1 pl-4 m-0 leading-relaxed">
        <li>1. 국내외 에너지 시장 동향 및 가격 추이 조사</li>
        <li>2. 경쟁사 및 동종업계 서비스/기술 비교 분석</li>
        <li>3. 정부 신재생에너지 정책 및 지원제도 조사</li>
        <li>4. 기업 고객 AI 도입 성공 사례 및 효과 분석</li>
        <li>5. 업무 관련 최신 규정 및 법령 개정안 조사</li>
      </ul>
    </div>
    <div class="text-[11px] text-cyan-300/80 mt-2">
      ※ 본인의 실제 실무와 가장 밀접한 주제를 자유롭게 선택해도 좋습니다.
    </div>
  </div>
  <div class="col-span-7 p-4 rounded-2xl border border-emerald-500/40 border-t-4 border-t-emerald-400 bg-emerald-950/25 backdrop-blur-md shadow-lg flex flex-col justify-between">
    <div>
      <div class="text-xs font-mono text-emerald-400 uppercase font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon:task-complete text-base"></span>
        <span>최종 제출 결과물 (4단계 산출물)</span>
      </div>
      <div class="space-y-1.5 text-xs text-white/90">
        <div class="p-1.5 rounded bg-black/40 border border-white/10">
          <strong>① 검색/리서치 소스:</strong> 선별한 핵심 웹 URL 및 문서 2~3건
        </div>
        <div class="p-1.5 rounded bg-black/40 border border-white/10">
          <strong>② Gemini Notebook:</strong> 소스 등록 후 도출한 핵심 인사이트 3개
        </div>
        <div class="p-1.5 rounded bg-black/40 border border-white/10">
          <strong>③ 원문 인용 검증:</strong> 수치나 주장의 원문 대조 확인 1건 이상
        </div>
        <div class="p-1.5 rounded bg-black/40 border border-emerald-500/30 text-emerald-300">
          <strong>④ Canvas 완성본:</strong> 1페이지 분량의 정식 실무 보고서/기획안
        </div>
      </div>
    </div>
  </div>
</div>

<div class="mt-2.5 p-2.5 rounded-xl border border-white/15 bg-white/5 flex items-center justify-between text-[11px] text-white/70">
  <span><strong>실습 4대 평가 기준:</strong> ① 소스 신뢰성 ② 원문 인용 대조 정확도 ③ S-A-F 질문 구체성 ④ Canvas 최종본 완성도</span>
  <span class="font-mono text-emerald-300 font-bold">실습 시간: 25분</span>
</div>

<!--
[실습 안내]
25분간 종합 실습을 진행합니다. 4단계 도구를 유기적으로 활용해 완성도 높은 1장의 실무 결과물을 완성해 보시기 바랍니다.
-->

---
title: 2차시 핵심 요약 및 공식
layout: center
class: text-center px-12
glowSeed: 801
---
<!-- slide:39-Session2-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-xs font-mono text-cyan-300 mb-5">
    <span>2차시 핵심 공식</span>
  </div>
  <div class="p-6 rounded-2xl border border-white/20 bg-white/5 backdrop-blur-md shadow-2xl max-w-3xl mb-6">
    <div class="text-2xl font-black text-white tracking-tight leading-relaxed">
      신뢰할 수 있는 리서치 = <span class="text-blue-400">좋은 자료 탐색</span> + <span class="text-cyan-300">원문 인용 검증</span> + <span class="text-emerald-400">구조화된 결과물</span>
    </div>
  </div>
  <h3 class="text-lg font-medium text-white/80 leading-relaxed max-w-2xl mb-6">
    AI 활용의 핵심은 답을 빨리 받는 것이 아니라,<br/>
    <strong>좋은 자료를 찾고, 근거를 확인하고, 내 업무 결과물로 만드는 것</strong>입니다.
  </h3>

  <div class="flex items-center gap-4 text-xs text-white/50 font-mono">
    <span class="px-4 py-1.5 rounded-xl bg-white/5 border border-white/10">1차시: 지시(RCTF) ➔ 2차시: 근거자료(S-A-F) ➔ 3차시 예고: ChatGPT Work 도구 및 5대 검토 체계</span>
  </div>
</div>

<!--
[마무리]
2차시 수고하셨습니다.
자료를 직접 주입하고 검증하는 RAG 워크플로우를 익히셨습니다.
다음 3차시에서는 ChatGPT Work 환경과 플러그인을 활용해 실제 다중 파일 기반 실무 문서를 작성하고 5대 검토 체계로 최종 감수하는 실무를 진행하겠습니다.
-->

---
layout: default
glow: none
---

<!-- slide:40-Divider-Session-3-4 -->

<SectionPartDivider
  part="3~4차시"
  title="생성형 AI의 업무 활용 I·II"
  subtitle="AI에게 답을 받는 것을 넘어, 실제 업무를 맡기고 결과물을 완성하다: ChatGPT Work · Excel 분석 · Skill 자동화 · DALL-E 3"
  image="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop"
/>

<!--
[강사 멘트]
3~4차시 통합 세션을 시작하겠습니다.
1차시에서 '지시법(RCTF)'을 배우고 2차시에서 '자료와 근거(S-A-F)'를 다루었다면, 이번 3~4차시는 'AI가 실제 업무를 수행하고 파일과 완성된 결과물을 만들어내는 단계'입니다.
질문하는 'Chat'에서 일을 맡기는 'Work'로의 패러다임 전환을 경험해 보겠습니다.
-->

---
title: 질문에 답하는 AI vs 일을 수행하는 AI
layout: default
class: px-14 py-7
glowSeed: 901
clicks: 2
---
<!-- slide:41-Chat-vs-Work -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  질문에 답하는 AI ➔ 일을 수행하는 AI (Chat vs Work)
</h2>

<ChatVsWorkComparison :stage="$clicks" />

<!--
[강사 멘트]
Chat과 Work의 본질적인 차이를 이해해야 합니다.
[click 1] Chat은 내가 질문하고 답을 받아 직접 일하는 '도움을 받는 도구'입니다. 반면 Work는 목표를 주면 AI가 자료를 보고 계획을 세워 실제 파일(DOCX, XLSX 등)을 만들어내는 '일을 맡기는 도구'입니다.
[click 2] 이제 우리는 질문하는 사람에서 일을 위임하고 검토하는 사람으로 역할을 전환합니다.
-->

---
title: ChatGPT Work 내부 실행 구조
layout: default
class: px-14 py-6
glowSeed: 902
clicks: 1
---
<!-- slide:42-Agent-Inside-Architecture -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-1">
  ChatGPT Work: 에이전트의 내부 실행 환경
</h2>
<p class="text-xs text-white/50 m-0 mb-4 font-mono">
  단순 텍스트 생성을 넘어 내부 도구 엔진을 직접 구동하는 통합 업무 플랫폼
</p>

<div class="grid grid-cols-12 gap-6 items-center">
  <div class="col-span-6 flex justify-center">
    <div class="rounded-2xl overflow-hidden border border-white/10 bg-black/40 p-2 shadow-2xl">
      <img src="/chatgpt-work-inside-architecture.jpg" alt="Inside ChatGPT Work" class="rounded-xl w-full max-h-76 object-contain" />
    </div>
  </div>
  <div class="col-span-6 flex flex-col justify-between h-80 space-y-2.5">
    <div class="p-3.5 rounded-xl bg-black/30 border border-white/10">
      <div class="text-xs font-mono font-bold text-emerald-400 mb-0.5">>_ Code Execution</div>
      <div class="text-xs text-white/80">파이썬 코드를 직접 실행하여 데이터 계산 및 차트 렌더링</div>
    </div>
    <div class="p-3.5 rounded-xl bg-black/30 border border-white/10">
      <div class="text-xs font-mono font-bold text-blue-400 mb-0.5">🌐 Browser</div>
      <div class="text-xs text-white/80">실시간 웹 정보 탐색 및 최신 공식 데이터 수집</div>
    </div>
    <div class="p-3.5 rounded-xl bg-black/30 border border-white/10">
      <div class="text-xs font-mono font-bold text-amber-400 mb-0.5">📁 Filesystem & Your Files</div>
      <div class="text-xs text-white/80">업로드된 엑셀·문서를 안전하게 읽고 편집 가능한 새 파일로 생성</div>
    </div>
    <div class="p-3.5 rounded-xl bg-blue-950/20 border border-blue-500/30">
      <div class="text-xs font-mono font-bold text-blue-300 mb-0.5">⚡ Agent Execution Loop</div>
      <div class="text-xs text-white/90">목표 이해 ➔ 계획 ➔ 도구 선택 ➔ 실행 ➔ 결과 확인 ➔ 피드백 수정</div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
화면에 보이는 그림처럼 ChatGPT Work의 내부에는 코드 실행기, 웹 브라우저, 파일시스템, 내 파일들이 연결되어 있습니다.
에이전트는 이 전문 도구들을 스스로 구동하여 실제 결과물을 완성합니다.
-->

---
title: 에이전트 6단계 작업 실행 루프
layout: default
class: px-14 py-7
glowSeed: 903
clicks: 1
---
<!-- slide:43-Agent-Action-Loop -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  에이전트는 무엇을 하는가? (Agent Action Loop)
</h2>

<AgentLoopDiagram :stage="$clicks" />

<!--
[강사 멘트]
에이전트의 핵심은 '생각하는 것(추론)'만이 아니라, 생각한 내용을 바탕으로 도구를 선택하고 실행하여 파일로 완성한 뒤 피드백을 받아 수정하는 '6단계 실행 루프'입니다.
-->

---
title: Work의 핵심: 파일과 결과물을 만든다
layout: default
class: px-14 py-7
glowSeed: 904
clicks: 2
---
<!-- slide:44-Work-Outputs-Hub -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  Work의 핵심: “답변”이 아니라 “파일과 결과물”을 만든다
</h2>

<WorkOutputsHub :stage="$clicks" />

<!--
[강사 멘트]
ChatGPT Work는 대화창에서 끝나는 텍스트를 주는 것이 아닙니다.
[click 1] 스프레드시트(XLSX), 기획서/보고서(DOCX), 슬라이드(PPTX), 통계 분석, 업무용 이미지까지 실무에서 즉시 활용 가능한 '편집 가능한 완성형 파일'을 직접 산출합니다.
-->

---
title: 도구를 선택하는 AI (Plugins & Apps)
layout: default
class: px-14 py-6
glowSeed: 905
clicks: 2
---
<!-- slide:45-Tools-Selection -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  도구를 선택하는 AI: Plugins · Skills · Apps 실제 환경
</h2>

<div class="grid grid-cols-12 gap-5 items-center">
  <div class="col-span-5 flex flex-col justify-between h-84">
    <div class="rounded-xl overflow-hidden border border-white/20 bg-white p-1.5 shadow-xl">
      <img src="/chatgpt-connectors-image5.webp" alt="ChatGPT Sidebar Plugins" class="rounded-lg w-full max-h-36 object-contain" />
    </div>
    <div class="p-3 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md">
      <div class="text-xs font-mono font-bold text-white/90 mb-1">자연어 도구 호출 (@Mentions)</div>
      <div class="space-y-1 text-[11px] text-white/70">
        <div><strong class="text-blue-300">@document:</strong> 보고서 작성 및 서식 편집</div>
        <div><strong class="text-emerald-300">@spreadsheet:</strong> 엑셀 수식 및 데이터 분석</div>
        <div><strong class="text-amber-300">@visualize:</strong> 인터랙티브 차트 시각화</div>
      </div>
    </div>
  </div>
  <div class="col-span-7 flex flex-col justify-between h-84">
    <div class="rounded-xl overflow-hidden border border-white/20 bg-white p-1.5 shadow-xl">
      <img src="/chatgpt-connectors-image7.webp" alt="OpenAI Plugins & Skills Hub" class="rounded-lg w-full max-h-36 object-contain" />
    </div>
    <div class="space-y-2 mt-1">
      <div v-click="1" class="p-2.5 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md">
        <div class="flex items-center justify-between mb-0.5">
          <span class="text-xs font-mono font-bold text-white/90">1. Plugins (플러그인)</span>
          <span class="text-[10px] font-mono text-white/40">Workflow 단위 패키지</span>
        </div>
        <p class="text-[11px] text-white/70 m-0 leading-tight">
          특정 업무 흐름을 처리하기 위해 여러 Skills와 Apps를 묶은 상위 실행 패키지입니다.
        </p>
      </div>
      <div v-click="2" class="p-2.5 rounded-xl border border-blue-500/20 bg-blue-950/20 backdrop-blur-md">
        <div class="flex items-center justify-between mb-0.5">
          <span class="text-xs font-mono font-bold text-blue-300">2. Skills & Apps (스킬과 앱)</span>
          <span class="text-[10px] font-mono text-blue-400">재사용 지침 & 외부 연동</span>
        </div>
        <p class="text-[11px] text-white/80 m-0 leading-tight">
          <strong>Skills</strong>는 표준 업무 지침을 제공하고, <strong>Apps</strong>는 외부 서비스와 실시간 연동됩니다.
        </p>
      </div>
    </div>
  </div>
</div>

<!--
[강사 멘트]
화면에 보이는 실제 ChatGPT 화면처럼 사이드바의 Plugins 메뉴에서 원하는 도구를 연결할 수 있습니다.
도구 이름을 외우실 필요 없이, 보고서를 쓸 때는 @document, 데이터를 다룰 때는 @spreadsheet, 차트를 그릴 때는 @visualize를 입력하면 AI가 대화창 안에서 전문 프로그램을 다루듯 일합니다.
-->

---
title: “도구를 어떻게 고르는가?”: 업무 중심 도구 매칭
layout: default
class: px-16 py-9
glowSeed: 906
clicks: 2
---
<!-- slide:46-How-To-Choose-Tools -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  “도구를 어떻게 고르는가?”: 업무 정의에서 출발하는 도구 매칭
</h2>

<div class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl">
  <div class="grid grid-cols-12 gap-3 text-xs font-mono font-bold text-white/60 border-b border-white/10 pb-2.5 mb-2.5">
    <div class="col-span-4">수행하려는 업무 (Task)</div>
    <div class="col-span-3">적합한 도구 (Tool)</div>
    <div class="col-span-5">실무 산출물 예시 (Output)</div>
  </div>
  <div class="space-y-2 text-xs">
    <div class="grid grid-cols-12 gap-3 p-2 rounded-lg bg-black/40 border border-white/5 items-center">
      <div class="col-span-4 text-white font-semibold">문서 작성 · 기획서 · 보고서 초안</div>
      <div class="col-span-3 font-mono text-blue-300">📄 Document</div>
      <div class="col-span-5 text-white/70">사업 기획서(DOCX), 공문, 주간보고</div>
    </div>
    <div v-click="1" class="grid grid-cols-12 gap-3 p-2 rounded-lg bg-black/40 border border-white/5 items-center">
      <div class="col-span-4 text-white font-semibold">데이터 분석 · 수식 계산 · 통계 비교</div>
      <div class="col-span-3 font-mono text-emerald-300">📊 Spreadsheet</div>
      <div class="col-span-5 text-white/70">매출 분석표(XLSX), 증감률 계산, 예산안</div>
    </div>
    <div v-click="1" class="grid grid-cols-12 gap-3 p-2 rounded-lg bg-black/40 border border-white/5 items-center">
      <div class="col-span-4 text-white font-semibold">차트 · 그래프 · 데이터 시각화</div>
      <div class="col-span-3 font-mono text-amber-300">📈 Visualize</div>
      <div class="col-span-5 text-white/70">월별 추이 꺾은선 그래프, 비중 파이차트</div>
    </div>
    <div v-click="2" class="grid grid-cols-12 gap-3 p-2 rounded-lg bg-black/40 border border-white/5 items-center">
      <div class="col-span-4 text-white font-semibold">심층 조사 · 웹 리서치 · 종합 리포트</div>
      <div class="col-span-3 font-mono text-cyan-300">🔍 Research / Work</div>
      <div class="col-span-5 text-white/70">시장 동향 분석 리포트, 경쟁사 비교표</div>
    </div>
    <div v-click="2" class="grid grid-cols-12 gap-3 p-2 rounded-lg bg-black/40 border border-white/5 items-center">
      <div class="col-span-4 text-white font-semibold">매주/매월 반복되는 정형 업무</div>
      <div class="col-span-3 font-mono text-purple-300">⚡ Skill</div>
      <div class="col-span-5 text-white/70">표준 주간보고서 생성, VOC 자동 분류 매뉴얼</div>
    </div>
  </div>
</div>

<div v-click="2" class="mt-4 p-3 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/80">
  <div class="flex items-center gap-2">
    <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
    <span><strong>핵심 사고방식:</strong> 도구를 먼저 찾는 것이 아니라, <strong>'내가 지금 무슨 일을 완성해야 하는가?'</strong>에서 출발합니다.</span>
  </div>
</div>

<!--
[강사 멘트]
업무를 정의하고 도구를 고르는 것이 실무 에이전트 활용의 첫걸음입니다.
-->

---
title: Excel을 AI에게 맡겨보자: 데이터 분석 실무
layout: default
class: px-16 py-9
glowSeed: 907
clicks: 1
---
<!-- slide:47-Excel-Practice-Intro -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Excel을 AI에게 맡겨보자: 실적 데이터 분석의 시작
</h2>

<div class="grid grid-cols-12 gap-6 items-center">
  <div class="col-span-7 p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl flex flex-col justify-between h-80">
    <div>
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <div class="flex items-center gap-2">
          <span class="i-carbon:document-view text-emerald-400"></span>
          <span class="text-xs font-mono font-bold text-white">2026_월별_사업실적_데이터.xlsx</span>
        </div>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">1,250 행 데이터</span>
      </div>
      <div class="space-y-1.5 font-mono text-[11px] text-white/80">
        <div class="grid grid-cols-5 gap-2 p-1.5 rounded bg-black/40 font-bold text-white/80 border-b border-white/10">
          <span>월 (Month)</span>
          <span>사업부</span>
          <span>매출액(억)</span>
          <span>영업이익</span>
          <span>달성률(%)</span>
        </div>
        <div class="grid grid-cols-5 gap-2 p-1.5 rounded bg-black/20 text-white/70">
          <span>2026-01</span><span>신에너지</span><span>142.5</span><span>18.2</span><span>104.2%</span>
        </div>
        <div class="grid grid-cols-5 gap-2 p-1.5 rounded bg-black/20 text-white/70">
          <span>2026-02</span><span>전력인프라</span><span>98.0</span><span>11.5</span><span>96.8%</span>
        </div>
        <div class="grid grid-cols-5 gap-2 p-1.5 rounded bg-black/20 text-white/70">
          <span>2026-03</span><span>해외사업</span><span>210.4</span><span>32.0</span><span>112.5%</span>
        </div>
      </div>
    </div>
    <div class="text-[11px] text-white/40 pt-2 border-t border-white/10">
      ※ 실제 기업 현장의 다중 컬럼 실적 스프레드시트 원본
    </div>
  </div>
  <div class="col-span-5 flex flex-col justify-between h-80">
    <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl">
      <div class="text-xs font-mono text-white/40 font-bold uppercase mb-2">실무자의 핵심 질문</div>
      <div class="text-lg font-bold text-white mb-3 leading-snug">
        "이 복잡한 데이터를 보고,<br/>
        <span class="text-blue-400">어떻게 핵심 인사이트를 뽑아낼까?</span>"
      </div>
      <p class="text-xs text-white/70 m-0 leading-relaxed">
        엑셀 수식을 하나하나 짜지 않아도, Work 에이전트에게 데이터 점검부터 추이 분석, 이상치 발견, 차트 생성까지 위임할 수 있습니다.
      </p>
    </div>
    <div v-click="1" class="p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90">
      <span>🚀 <strong>다음 단계:</strong> Work에게 엑셀 분석을 올바르게 지시하는 4단계 사고방식</span>
    </div>
  </div>
</div>

<!--
[강사 멘트]
수천 줄의 엑셀 파일을 볼 때 무엇부터 해야 할까요?
AI에게 무작정 '분석해줘'라고 던지는 것이 아니라, 데이터 구조 파악부터 단계적으로 지시하는 방법을 실습하겠습니다.
-->

---
title: 엑셀 분석의 기본 사고방식 4단계
layout: default
class: px-16 py-9
glowSeed: 908
clicks: 3
---
<!-- slide:48-Excel-4-Thinking-Steps -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  AI에게 엑셀을 맡길 때: 4단계 분석 사고방식
</h2>

<div class="grid grid-cols-4 gap-4 mt-4">
  <div class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-white/40 font-bold uppercase">Step 01</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">무엇을 알고 싶은가?</div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        매출 추이, 이익률 저하 원인, 사업부별 달성률 등 분석 목표를 명확히 정의합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">목적 정의</div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-white/40 font-bold uppercase">Step 02</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">어떤 데이터를 볼 것인가?</div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        시트 내 특정 기간(월별), 사업부 컬럼, 결측치 여부를 선별 지정합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">대상 범위 확정</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-72">
    <div>
      <span class="text-xs font-mono text-white/40 font-bold uppercase">Step 03</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">어떤 기준으로 비교할 것인가?</div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        전년 동기 대비 증감률(YoY), 목표 대비 달성률, 상위 5개 요인 기준을 설정합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">비교 기준 수립</div>
  </div>
  <div v-click="3" class="p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-72 shadow-lg">
    <div>
      <span class="text-xs font-mono text-blue-400 font-bold uppercase">Step 04</span>
      <div class="text-sm font-bold text-white mt-1 mb-2">어떤 결과물로 만들 것인가?</div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        요약 비교표, 꺾은선 차트, 임원 보고용 1페이지 요약본 등 형식을 지정합니다.
      </p>
    </div>
    <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">최종 파일 완성</div>
  </div>
</div>

<div v-click="3" class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/80">
  <span><strong>주의:</strong> AI에게 단순히 "분석해줘"라고 하지 마세요. <strong>목적 ➔ 대상 ➔ 기준 ➔ 결과물</strong>의 4단계를 갖출 때 정확한 분석이 완성됩니다.</span>
</div>

<!--
[강사 멘트]
AI에게 무작정 분석을 시키지 말고, 목적, 대상 데이터, 비교 기준, 최종 산출물 형식을 지정해 주는 것이 엑셀 분석 프롬프트의 기본입니다.
-->

---
title: 실습 ① 엑셀 기본 프롬프트: 데이터 상태 파악
layout: default
class: px-16 py-9
glowSeed: 909
clicks: 1
---
<!-- slide:49-Excel-Prompt-1-Inspection -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ① 엑셀 기본 프롬프트: 데이터 상태 및 오류 먼저 파악하기
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">1단계 실습 프롬프트 (데이터 점검)</div>
      <div class="p-4 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
        "첨부한 엑셀 파일의 시트와 열(Column) 구조를 먼저 파악해줘.<br/><br/>
        1. 각 열이 무엇을 의미하는지 한 줄로 정리하고<br/>
        2. 분석 전 확인해야 할 결측값, 이상값, 중복 데이터가 있는지 찾아줘.<br/>
        3. 아직 데이터를 임의로 수정하지 말고, 발견된 문제만 표로 정리해줘."
      </div>
    </div>
    <div class="text-xs font-mono text-white/50 font-bold pt-2 border-t border-white/10">
      데이터 무결성 사전 검증
    </div>
  </div>

  <div class="col-span-5 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">핵심 교육 포인트</div>
      <div class="space-y-2.5 text-xs text-white/80 leading-relaxed">
        <div class="p-2.5 rounded-lg bg-black/40 border border-white/5">
          <strong class="text-white">① 바로 분석 금지:</strong><br/>
          비어있는 셀이나 오타가 있으면 통계 결과가 왜곡됩니다.
        </div>
        <div class="p-2.5 rounded-lg bg-black/40 border border-white/5">
          <strong class="text-white">② 임의 수정 방지:</strong><br/>
          AI가 원본을 제멋대로 바꾸지 않도록 "문제만 표로 정리하라"고 제약합니다.
        </div>
      </div>
    </div>
    <div class="text-xs text-white/40 pt-2 border-t border-white/10 font-mono">
      실습 시간: 5분
    </div>
  </div>
</div>

<!--
[실습 안내]
파일을 업로드하고 1단계 프롬프트를 입력하여 시트 구조와 결측치를 먼저 확인해 보겠습니다.
-->

---
title: 실습 ② 엑셀 기본 프롬프트: 데이터 분석 및 원인 도출
layout: default
class: px-16 py-9
glowSeed: 910
clicks: 1
---
<!-- slide:50-Excel-Prompt-2-Analysis -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ② 엑셀 기본 프롬프트: 추이 분석 및 핵심 요인 도출
</h2>

<div class="grid grid-cols-12 gap-6 mt-3">
  <div class="col-span-7 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">2단계 실습 프롬프트 (추이 & 원인)</div>
      <div class="p-4 rounded-xl bg-black/40 font-mono text-xs text-white/90 leading-relaxed border border-white/10 mb-2">
        "월별 매출 추이를 분석하고 전월 대비 증감률(MoM)을 계산해줘.<br/><br/>
        1. 증감 폭이 가장 큰 상위 5개 항목을 찾아 주요 원인을 데이터에서 확인해줘.<br/>
        2. 데이터에 없는 원인은 임의로 추측하지 말고 '추가 확인 필요'로 표시할 것.<br/>
        3. 결과는 `표(월 | 매출액 | 전월대비 증감률 | 주요 원인)`로 출력하라."
      </div>
    </div>
    <div class="text-xs font-mono text-white/50 font-bold pt-2 border-t border-white/10">
      근거 기반 수치 통계 분석
    </div>
  </div>

  <div class="col-span-5 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">화면 비교 (Before ➔ After)</div>
      <div class="space-y-2 text-xs text-white/80 leading-relaxed">
        <div class="p-2.5 rounded bg-black/40 border border-white/5">
          <strong>좌측 원본:</strong> 수천 줄의 원시 엑셀 데이터
        </div>
        <div class="p-2.5 rounded bg-black/40 border border-blue-500/20 text-blue-200">
          <strong>우측 결과:</strong> 월별 증감률 계산 + 상위 5대 이상치 원인 표 완성
        </div>
      </div>
    </div>
    <div class="p-2.5 rounded-lg bg-black/40 border border-white/10 text-[11px] text-white/70">
      💡 "없는 사실 추측 금지" 제약으로 할루시네이션 완벽 방지
    </div>
  </div>
</div>

<!--
[실습 안내]
2단계 프롬프트를 실행하여 증감률과 원인 분석 표가 자동으로 생성되는지 확인합니다.
-->

---
title: @visualize 플러그인: 실시간 시각화 데모
layout: default
class: px-14 py-6
glowSeed: 911
---
<!-- slide:51-Visualize-Video-Stage -->

<div class="flex items-center justify-between mb-3">
  <div>
    <h2 class="text-2xl font-extrabold text-white tracking-tight">
      @visualize 플러그인: 실시간 시각화 & 뷰 전환
    </h2>
    <p class="text-xs text-white/50 m-0 font-mono">
      대화창 안에서 텍스트 요약을 인터랙티브 타임라인 및 캘린더 뷰로 실시간 전환
    </p>
  </div>
  <span class="text-xs font-mono px-3 py-1 rounded-full bg-white/10 text-white/70">Plugin Demo</span>
</div>

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
영상에서 보시는 것처럼, @visualize 플러그인을 활용하면 대화창 안에서 회의록이나 작업 일정을 타임라인으로 렌더링하고, '캘린더 뷰로 보여줘'라는 한마디에 실시간으로 시각화 양식을 전환할 수 있습니다.
-->

---
title: 실습 ④ 엑셀 기본 프롬프트: 점진적 수정 (Iterative Loop)
layout: default
class: px-16 py-9
glowSeed: 912
clicks: 2
---
<!-- slide:52-Excel-Prompt-4-Iterative-Refine -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  실습 ④ 엑셀 기본 프롬프트: 피드백으로 완성도 높이기 (점진적 수정)
</h2>

<div class="grid grid-cols-3 gap-5 mt-4">
  <div class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <span class="text-xs font-mono text-white/40 font-bold uppercase">1차 요청</span>
      <div class="p-3 rounded-xl bg-black/40 text-xs font-mono text-white/80 mt-2 mb-3 border border-white/5">
        "매출 추이를 시각화해줘."
      </div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        기본 그래프가 생성되었으나 강조점이 약하고 다소 밋밋함
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">초안 생성</div>
  </div>
  <div v-click="1" class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-76">
    <div>
      <span class="text-xs font-mono text-blue-400 font-bold uppercase">2차 수정</span>
      <div class="p-3 rounded-xl bg-black/40 text-xs font-mono text-blue-200 mt-2 mb-3 border border-blue-500/20">
        "월별 변화 추이가 더 눈에 잘 띄도록 꺾은선으로 바꾸고 목표선을 추가해줘."
      </div>
      <p class="text-xs text-white/80 leading-relaxed m-0">
        목표 대비 달성 여부와 추세선이 뚜렷해짐
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-blue-300">비교 기준 보강</div>
  </div>
  <div v-click="2" class="p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-76 shadow-lg">
    <div>
      <span class="text-xs font-mono text-blue-300 font-bold uppercase">3차 수정 (임원 보고용)</span>
      <div class="p-3 rounded-xl bg-black/40 text-[11px] font-mono text-blue-200 mt-2 mb-3 border border-blue-500/30 leading-relaxed">
        "증감이 가장 큰 3월을 빨간색으로 강조하고, 임원 보고용 3줄 인사이트를 하단에 추가해줘."
      </div>
      <p class="text-xs text-white/90 leading-relaxed m-0">
        의사결정자가 3초 만에 파악할 수 있는 완성본 도출
      </p>
    </div>
    <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">최종 보고용 완성</div>
  </div>
</div>

<!--
[강사 멘트]
AI는 한 번에 100점짜리를 뽑는 자판기가 아닙니다.
결과를 보고 2차, 3차 피드백을 주며 원하는 수준으로 다듬어가는 것이 진정한 실무자의 역량입니다.
-->

---
title: “AI 하나 + 여러 도구”: 확장되는 업무 생태계
layout: default
class: px-14 py-6
glowSeed: 913
clicks: 2
---
<!-- slide:53-Work-Tools-Hub -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  “AI 하나 + 여러 도구”: 확장되는 업무 생태계와 실제 실행
</h2>

<div class="grid grid-cols-12 gap-5 items-center">
  <div class="col-span-7">
    <WorkToolsHub :stage="$clicks" />
  </div>
  <div class="col-span-5 flex flex-col justify-between h-84">
    <div class="rounded-xl overflow-hidden border border-white/20 bg-white p-2 shadow-2xl">
      <img src="/chatgpt-app-execution.jpg" alt="Real App Execution" class="rounded-lg w-full max-h-52 object-contain" />
    </div>
    <div class="p-2.5 rounded-xl border border-white/10 bg-white/5 text-xs text-white/80 mt-2">
      <span class="text-white font-semibold">💡 실전 실행 장면:</span>
      대화창에서 자연어 명령으로 외부 앱(@LG ThinQ 등)과 엔터프라이즈 기기 제어 및 데이터 연동을 즉시 수행합니다.
    </div>
  </div>
</div>

<!--
[강사 멘트]
[click 1] 좌측 구조도처럼 사용자는 하나의 대화창에서 지시하지만, 백그라운드에서는 Document, Spreadsheet, Visualize, 외부 앱들이 유기적으로 협업합니다.
[click 2] 우측 실제 실행 화면처럼 자연어로 외부 앱(@LG ThinQ 등)을 직접 제어하고 작업을 완결하는 엔터프라이즈 생태계가 구현됩니다.
-->

---
title: OpenAI Skill 패키지 구조 데모
layout: default
class: px-14 py-6
glowSeed: 914
---
<!-- slide:54-Skill-Video-Stage -->

<div class="flex items-center justify-between mb-3">
  <div>
    <h2 class="text-2xl font-extrabold text-white tracking-tight">
      OpenAI Skill: 반복 업무를 위한 맞춤형 패키지
    </h2>
    <p class="text-xs text-white/50 m-0 font-mono">
      SKILL.md 표준 지침과 참조 문서를 결합하여 대화창에서 원클릭으로 실행
    </p>
  </div>
  <span class="text-xs font-mono px-3 py-1 rounded-full bg-white/10 text-white/70">Skill Package</span>
</div>

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
glowSeed: 915
clicks: 2
---
<!-- slide:55-Prompt-vs-Skill -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  Skill과 Prompt의 차이: 1회성 지시에서 조직의 영구 자산으로
</h2>

<PromptVsSkillComparison :stage="$clicks" />

<!--
[강사 멘트]
[click 1] 프롬프트가 "이번에 이 일 해줘"라면, 스킬은 "앞으로 이 업무는 항상 이 표준으로 해줘"라는 조직의 자산입니다.
[click 2] 개인의 프롬프트 작성 실력에 의존하지 않고, 누가 실행해도 똑같은 퀄리티를 보장합니다.
-->

---
title: 나만의 Skill 만들기 실습: 4대 구성요소
layout: default
class: px-16 py-9
glowSeed: 916
clicks: 1
---
<!-- slide:56-Make-Your-Own-Skill -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-3">
  나만의 Skill 만들기 실습: 4대 핵심 구성요소
</h2>

<div class="grid grid-cols-12 gap-5 mt-2">
  <div class="col-span-5 p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-80">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-2">반복 업무 주제 선택 (택 1)</div>
      <div class="grid grid-cols-2 gap-1.5 text-xs text-white/80">
        <div class="p-1.5 rounded bg-black/40 border border-white/5">1. 주간업무보고</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">2. 고객 문의 정리</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">3. 회의록 정리</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">4. 교육 결과보고</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">5. 홍보문 작성</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">6. 엑셀 실적 분석</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">7. 행사 결과보고서</div>
        <div class="p-1.5 rounded bg-black/40 border border-white/5">8. 정책자료 요약</div>
      </div>
    </div>
    <div class="text-[11px] text-white/40 font-mono pt-2 border-t border-white/10">
      ※ 본인의 실제 반복 업무를 선정하세요.
    </div>
  </div>
  <div class="col-span-7 p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-80">
    <div>
      <div class="text-xs font-mono text-blue-400 uppercase font-bold mb-2">Skill 필수 4대 구성요소</div>
      <div class="space-y-1.5 text-xs text-white/90">
        <div class="p-2 rounded bg-black/40 border border-white/5">
          <strong class="text-blue-300">① 목적 (Goal):</strong> 이 스킬이 해결하는 업무 목표 정의
        </div>
        <div class="p-2 rounded bg-black/40 border border-white/5">
          <strong class="text-blue-300">② 입력 자료 (Inputs):</strong> 사용자로부터 주입받을 필수 파일/데이터
        </div>
        <div class="p-2 rounded bg-black/40 border border-white/5">
          <strong class="text-blue-300">③ 작업 절차 (Workflow):</strong> 1단계부터 4단계까지 순차 실행 지침
        </div>
        <div class="p-2 rounded bg-black/40 border border-blue-500/30 text-blue-200">
          <strong>④ 결과물 기준 (Rubric):</strong> 표/문서 서식 및 분량 제약 조건
        </div>
      </div>
    </div>
    <div class="text-xs font-mono text-blue-300 font-bold pt-2 border-t border-blue-500/20">
      실습 시간: 15분
    </div>
  </div>
</div>

<!--
[실습 안내]
본인이 매주 반복하는 업무를 하나 정해서, 4대 구성요소에 맞춰 스킬 정의서를 작성해 보겠습니다.
-->

---
title: Skill 테스트와 개선 루프 (Refinement Loop)
layout: default
class: px-14 py-7
glowSeed: 917
clicks: 1
---
<!-- slide:57-Skill-Refine-Loop -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  Skill 테스트와 개선 루프: 완성형 매뉴얼로 다듬기
</h2>

<SkillTestLoopDiagram :stage="$clicks" />

<!--
[강사 멘트]
스킬을 만들었다고 끝이 아닙니다.
[click 1] 실제 데이터를 넣어 돌려보고, 결과가 너무 길거나 서식이 틀어지면 지침을 수정하여 완벽한 매뉴얼로 다듬는 과정이 필수적입니다.
-->

---
title: Skill 개선 실습 사례: 주간 업무보고서 고도화
layout: default
class: px-16 py-9
glowSeed: 918
clicks: 1
---
<!-- slide:58-Skill-Improvement-Case -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  Skill 개선 실습 사례: 주간 업무보고서 스킬 고도화
</h2>

<div class="grid grid-cols-2 gap-8 mt-3">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono font-bold text-white/60">초기 스킬 지침 (막연한 지시)</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/10 text-white/50">1차 실행</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-white/80 border border-white/5 mb-2">
        "매주 팀 업무보고서를 작성해줘."
      </div>
      <div class="p-2.5 rounded-lg bg-black/30 text-xs text-white/60">
        <strong>발견된 문제:</strong> 줄글이 너무 길고, 중요하지 않은 잡무까지 장황하게 나열되어 상사 보고용으로 부적합.
      </div>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">개선 필요</div>
  </div>
  <div v-click="1" class="p-6 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono font-bold text-blue-300">개선된 스킬 지침 (4단 고정 규격)</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold">표준화 완료</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-blue-200 border border-blue-500/20 leading-relaxed mb-2">
        "반드시 다음 4단 구조로 작성하라.<br/>
        ① 이번 주 핵심 성과 (수치 기반)<br/>
        ② 주요 완료 업무 (상세 내용)<br/>
        ③ 발생 문제 및 리스크 대응안<br/>
        ④ 다음 주 중점 추진 계획<br/>
        ※ 각 항목당 글머리 기호 3개 이내로 제한할 것."
      </div>
    </div>
    <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">재사용 완결</div>
  </div>
</div>

<!--
[강사 멘트]
처음 만든 스킬이 마음에 안 든다고 포기하지 마세요.
서식 구조와 '항목당 3개 이내' 같은 분량 제약을 추가하면 즉시 실무에 투입 가능한 완벽한 스킬이 됩니다.
-->

---
title: 이미지 생성도 “업무”로 접근: 타깃과 목적 중심 제작
layout: default
class: px-16 py-9
glowSeed: 919
clicks: 1
---
<!-- slide:59-Image-As-Work -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  이미지 생성도 “업무”로 접근: 타깃과 목적이 있는 비주얼 제작
</h2>

<div class="grid grid-cols-2 gap-8 mt-3">
  <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono font-bold text-white/60">단순 이미지 생성 요청</span>
        <span class="text-[10px] font-mono text-white/40">나쁜 예</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-white/80 border border-white/5 mb-3">
        "사내 행사 홍보 포스터 하나 만들어줘."
      </div>
      <p class="text-xs text-white/60 leading-relaxed m-0">
        행사명, 대상, 일시, 장소, 전달하려는 분위기가 없어 쓸모없는 추상적인 그림만 생성됩니다.
      </p>
    </div>
    <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">실무 사용 불가</div>
  </div>
  <div v-click="1" class="p-6 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
    <div>
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-mono font-bold text-blue-300">업무용 구조화 지시문</span>
        <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold">좋은 예</span>
      </div>
      <div class="p-3 rounded-xl bg-black/40 font-mono text-[11px] text-blue-200 border border-blue-500/20 leading-relaxed mb-2">
        "다음 행사 정보를 바탕으로 30~40대 직장인을 위한 사내 AI 세미나 홍보 카드뉴스를 제작하라.<br/>
        1. 메인 카피: 'AI로 끝내는 칼퇴의 기술'<br/>
        2. 일시: 2026년 9월 8일(화) 14:00<br/>
        3. 모바일 화면에서 텍스트가 한눈에 읽히도록 중앙 정렬하고 블루 톤으로 디자인할 것."
      </div>
    </div>
    <div class="pt-2 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">즉시 배포 가능</div>
  </div>
</div>

<!--
[강사 멘트]
이미지 생성도 프롬프트 작성과 똑같습니다.
대상, 핵심 문구, 모바일 가독성 요구조건을 명시해야 업무에 바로 쓰는 홍보물이 나옵니다.
-->

---
title: 이미지 생성의 핵심: 생성 ➔ 평가 ➔ 수정
layout: default
class: px-14 py-7
glowSeed: 920
clicks: 2
---
<!-- slide:60-Image-Iterative-Refinement -->

<h2 class="text-2xl font-extrabold text-white tracking-tight mb-2">
  이미지 생성의 핵심: 생성 ➔ 평가 ➔ 수정 (Iterative Refinement)
</h2>

<ImageIterativeRefine :stage="$clicks" />

<!--
[강사 멘트]
[click 1] 1차 생성 후 글자가 너무 많거나 산만하다면 피드백을 줍니다.
[click 2] 타이틀 확대, 일정 강조, 불필요한 장식 제거를 지시하여 최종 실무용 홍보 비주얼로 완성합니다.
-->

---
title: ★ Final Mission: 3~4차시 통합 실습 과제
layout: default
class: px-14 py-7
glowSeed: 921
---
<!-- slide:61-Final-Mission -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-2">
  ★ Final Mission: 내 업무 올인원 실무 프로젝트 완성
</h2>

<div class="grid grid-cols-12 gap-5 mt-2">
  <div class="col-span-5 p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-84">
    <div>
      <div class="text-xs font-mono text-white/50 uppercase font-bold mb-1.5">종합 업무 시나리오</div>
      <div class="p-3.5 rounded-xl bg-black/40 text-xs font-mono text-white/90 border border-white/10 leading-relaxed mb-2">
        "이번 달 우리 팀의 실적을 분석하여 임원에게 보고하고,<br/>
        이를 기반으로 사내 홍보/안내용 결과물까지 완성하라."
      </div>
      <p class="text-[11px] text-white/60 m-0 leading-relaxed">
        본인의 실제 실무 엑셀 데이터 또는 제공된 실습 샘플을 기반으로 자유롭게 진행합니다.
      </p>
    </div>
    <div class="text-xs font-mono text-white/50 font-bold pt-1.5 border-t border-white/10">
      실습 시간: 35분 (집중 프로젝트)
    </div>
  </div>

  <div class="col-span-7 p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-84">
    <div>
      <div class="text-xs font-mono text-blue-400 uppercase font-bold mb-1.5">7단계 연속 실행 파이프라인</div>
      <div class="space-y-1 text-xs text-white/90">
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 1: Excel 데이터 업로드</span><span class="text-[10px] font-mono text-white/40">자료 주입</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 2: Work에게 데이터 구조 파악 & 결측치 점검 지시</span><span class="text-[10px] font-mono text-white/60">점검</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 3: 증감률 계산 & 상위 5대 이상치 원인 분석</span><span class="text-[10px] font-mono text-white/60">분석</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 4: @visualize 차트 시각화 생성</span><span class="text-[10px] font-mono text-amber-300">시각화</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 5: @document 임원 보고용 1페이지 보고서 완성</span><span class="text-[10px] font-mono text-blue-300">문서화</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-white/5 flex items-center justify-between">
          <span>Step 6: 사내 공유용 홍보/안내 이미지 생성</span><span class="text-[10px] font-mono text-purple-300">비주얼</span>
        </div>
        <div class="p-1.5 rounded bg-black/30 border border-blue-500/20 flex items-center justify-between text-blue-200 font-bold">
          <span>Step 7: 다음 달에도 쓸 수 있도록 Skill로 저장</span><span class="text-[10px] font-mono">자산화</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!--
[실습 안내]
35분간 Final Mission을 진행합니다. 1단계부터 7단계까지 올인원으로 하나의 업무를 완결해 보시기 바랍니다.
-->

---
title: 최종 결과물 제출 6대 산출물
layout: default
class: px-16 py-9
glowSeed: 922
---
<!-- slide:62-Submission-Rubric -->

<h2 class="text-3xl font-extrabold text-white tracking-tight mb-4">
  최종 결과물 제출: 6대 실무 산출물 패키지
</h2>

<div class="grid grid-cols-3 gap-4 mt-3">
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-white mb-1">① 원본 자료</div>
    <p class="text-[11px] text-white/60 m-0 leading-relaxed">분석에 사용한 엑셀 파일 또는 원천 문서</p>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">Input Data</div>
  </div>
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-white mb-1">② AI 업무 지시문</div>
    <p class="text-[11px] text-white/60 m-0 leading-relaxed">RCTF 구조로 작성된 단계별 프롬프트</p>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">Prompts</div>
  </div>
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-white mb-1">③ 분석 결과 표</div>
    <p class="text-[11px] text-white/60 m-0 leading-relaxed">증감률 및 핵심 인사이트 정리 표</p>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">Spreadsheet</div>
  </div>
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-white mb-1">④ 시각화 차트</div>
    <p class="text-[11px] text-white/60 m-0 leading-relaxed">목적이 명확한 꺾은선/막대 그래프</p>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">Visualize</div>
  </div>
  <div class="p-4 rounded-xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-white mb-1">⑤ 최종 실무 보고서</div>
    <p class="text-[11px] text-white/60 m-0 leading-relaxed">상사 보고용 1페이지 완성본 (DOCX)</p>
    <div class="text-[10px] font-mono text-white/40 pt-1 border-t border-white/10">Document</div>
  </div>
  <div class="p-4 rounded-xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg flex flex-col justify-between h-40">
    <div class="text-xs font-bold text-blue-300 mb-1">⑥ 나만의 Skill 매뉴얼</div>
    <p class="text-[11px] text-white/80 m-0 leading-relaxed">다음 달에도 반복 실행할 스킬 지침</p>
    <div class="text-[10px] font-mono font-bold text-blue-300 pt-1 border-t border-blue-500/20">Skill Asset</div>
  </div>
</div>

<div class="mt-4 p-3 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/80">
  <span>🏆 <strong>수료 기준:</strong> 6대 산출물을 완성하여 제출함으로써 AI 기반 실무 완결 역량을 검증합니다.</span>
</div>

<!--
[실습 마무리]
6개 산출물이 모두 완비되었는지 확인하고 제출해 주시기 바랍니다.
-->

---
title: 전체 교육 마스터 Takeaway & 핵심 공식
layout: center
class: text-center px-12
glowSeed: 999
---
<!-- slide:63-Master-Takeaway -->

<div class="flex flex-col items-center justify-center">
  <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 border border-white/15 text-xs font-mono text-white/70 mb-4">
    <span>전체 커리큘럼 핵심 공식 (Master Takeaway)</span>
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
