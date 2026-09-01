---
layout: center
highlighter: shiki
css: unocss
colorSchema: dark
transition: fade-out
title: Lecture Deck Kit
exportFilename: lecture-deck-kit-starter
lineNumbers: false
drawings:
  persist: false
mdc: true
clicks: 0
preload: false
routerMode: hash
glow: bottom
glowHue: 170
glowOpacity: 0.32
---
<!-- slide:cover -->

<div class="mx-auto max-w-5xl text-center">
  <div class="i-carbon:flash mx-auto mb-8 text-7xl text-cyan-300/75" />
  <div class="deck-kicker">Lecture Deck Kit · Slidev starter</div>
  <h1 class="mt-5 text-6xl! leading-none!">한 장에는 하나의 장면</h1>
  <p class="mx-auto mt-6 max-w-2xl text-xl deck-muted">
    흐름과 재료를 넣으면, 설명을 돕는 미니멀한 발표 초안으로 확장하는 기본 골격
  </p>
  <div class="deck-rule mx-auto" />
</div>

<!--
[강사 멘트]
이 슬라이드는 킷의 기본 표지 예시입니다.
-->

---
layout: default
glow: right
glowHue: 190
---
<!-- slide:divider -->

<SectionDivider
  section="01"
  title="핵심 개념을 장면으로 바꾸기"
  subtitle="텍스트를 늘리기보다, 관객이 다음 질문을 자연스럽게 따라오도록 구성합니다."
/>

---
layout: default
class: flex flex-col
clicks: 3
glow: bottom
---
<!-- slide:reveal-list -->

<div class="deck-kicker">Narrative rhythm</div>
<h2 class="mt-3">설명은 한 번에 다 보여주지 않습니다</h2>
<p class="mt-2 deck-subtitle">발표자의 설명 순서와 화면의 등장 순서를 맞춥니다.</p>

<RevealList
  class="mt-0"
  :stage="$clicks"
  :items="[
    { icon: 'i-carbon:flash', title: '질문을 먼저 세운다', body: '관객이 다음 내용을 궁금해하게 만듭니다.' },
    { icon: 'i-carbon:document-view', title: '근거를 보여준다', body: '이미지, 수치, 화면 캡처가 주장을 지지하게 합니다.' },
    { icon: 'i-carbon:arrow-right', title: '적용 장면으로 이동한다', body: '개념을 실제 업무나 행동으로 연결합니다.' },
  ]"
/>

---
layout: default
class: flex flex-col
clicks: 2
glow: center
glowHue: 155
---
<!-- slide:comparison -->

<div class="deck-kicker">Composition pattern</div>
<h2 class="mt-3">비교는 차이를 보여주는 순간에만 사용합니다</h2>

<Comparison
  class="mt-10"
  :stage="$clicks"
  left-title="기존 방식"
  left-body="자료와 설명이 한 화면에 동시에 쌓입니다."
  right-title="발표형 방식"
  right-body="핵심 주장, 근거, 다음 행동이 순서대로 드러납니다."
  takeaway="화면은 발표자의 생각을 대신하지 않고, 생각의 순서를 도와야 합니다."
/>

---
layout: default
class: flex flex-col
clicks: 3
glow: left
glowHue: 205
---
<!-- slide:demo -->

<div class="deck-kicker">Demo cue</div>
<h2 class="mt-3">시연 슬라이드는 설명보다 행동을 선명하게 만듭니다</h2>

<DemoCue
  class="mt-10"
  :stage="$clicks"
  title="실제 자료를 넣고 결과가 바뀌는 순간을 보여주세요"
  duration="03:00"
  :steps="[
    '화면 공유로 실제 도구를 연다',
    '사용자의 자료를 한 번에 넣는다',
    '결과를 검토하고 다음 질문을 던진다',
  ]"
/>

---
layout: center
glow: full
glowHue: 165
---
<!-- slide:takeaway -->

<Takeaway
  kicker="The anchor"
  title="흐름은 사람이 정하고, 장면은 킷이 돕습니다."
  detail="좋은 초안은 완성된 취향이 아니라, 빠르게 고칠 수 있는 첫 번째 무대입니다."
/>
