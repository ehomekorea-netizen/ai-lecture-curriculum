<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

interface CardItem {
  kicker: string
  kickerColor: string
  badgeBg: string
  title: string
  desc: string
  highlight: string
  icon: string
  borderAccent: string
}

const cards: CardItem[] = [
  {
    kicker: '01. DIGITAL FLUENCY',
    kickerColor: 'text-blue-600',
    badgeBg: 'bg-blue-50 text-blue-600',
    title: '실무 디지털 협업력의 무언의 증명',
    desc: 'IT·기획·마케팅 현장에서 노션은 기본 협업 툴입니다. 템플릿과 DB를 다루는 포트폴리오 자체가',
    highlight: '"현업 툴에 즉시 적응 가능한 인재"',
    icon: '💻',
    borderAccent: 'hover:border-blue-300 group-hover:shadow-blue-500/10'
  },
  {
    kicker: '02. 2-TIER DEEP DIVE',
    kickerColor: 'text-emerald-600',
    badgeBg: 'bg-emerald-50 text-emerald-600',
    title: '3초 스캔 & 심층 탐색의 양립',
    desc: '수십 장짜리 PDF의 피로도 없이, 첫 화면에서',
    highlight: '핵심 수치를 3초 만에 스캔하고 토글로 심층 검증(Deep-Dive)',
    icon: '🔍',
    borderAccent: 'hover:border-emerald-300 group-hover:shadow-emerald-500/10'
  },
  {
    kicker: '03. LIVE EVIDENCE',
    kickerColor: 'text-purple-600',
    badgeBg: 'bg-purple-50 text-purple-600',
    title: '살아있는 결과물 임베드 & 증빙',
    desc: '단순 텍스트 나열을 넘어 실제 작업한',
    highlight: '기획서, 설문 대시보드, 영상, 링크를 페이지 내에 실시간 연동',
    icon: '🔗',
    borderAccent: 'hover:border-purple-300 group-hover:shadow-purple-500/10'
  }
]

const visibleIndex = ref(0)
let timer: any = null

function triggerSequentialReveal() {
  visibleIndex.value = 0
  
  // 1번 카드 즉시 등장
  timer = setTimeout(() => {
    visibleIndex.value = 1
    
    // 2번 카드 등장
    timer = setTimeout(() => {
      visibleIndex.value = 2
      
      // 3번 카드 등장
      timer = setTimeout(() => {
        visibleIndex.value = 3
      }, 700)
    }, 700)
  }, 250)
}

onMounted(() => {
  triggerSequentialReveal()
})

onUnmounted(() => {
  clearTimeout(timer)
})
</script>

<template>
  <div class="notion-value-cards-container w-full select-none mt-2">
    <!-- 3 Progressive Cards Grid (No top clutter) -->
    <div class="grid grid-cols-3 gap-3.5 h-[315px]">
      <div
        v-for="(card, i) in cards"
        :key="i"
        class="card-box relative p-4.5 rounded-2xl bg-white border shadow-sm flex flex-col justify-between transition-all duration-700 ease-out"
        :class="[
          visibleIndex > i
            ? 'opacity-100 translate-y-0 shadow-md border-slate-200'
            : 'opacity-0 translate-y-6 pointer-events-none border-transparent'
        ]"
      >
        <!-- Card Top -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono tracking-tight" :class="card.badgeBg">
              {{ card.kicker }}
            </span>
            <span class="text-xl p-1 rounded-lg bg-slate-50 border border-slate-100 shadow-2xs">{{ card.icon }}</span>
          </div>

          <h3 class="text-sm font-extrabold text-slate-900 leading-snug mb-2 mt-1">
            {{ card.title }}
          </h3>

          <p class="text-[11.5px] text-slate-600 leading-relaxed m-0">
            {{ card.desc }}
            <b class="text-slate-900 font-bold block mt-1.5 p-2 rounded-lg bg-slate-50 border border-slate-100 text-slate-800 text-[11px]">
              {{ card.highlight }}
            </b>
          </p>
        </div>

        <!-- Card Bottom Indicator -->
        <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-400 font-mono">
          <span>STEP 0{{ i + 1 }}</span>
          <span class="text-emerald-600 font-bold flex items-center gap-1">
            <span>✓</span>
            <span>채용 검증 완료</span>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-box {
  will-change: transform, opacity;
}
</style>
