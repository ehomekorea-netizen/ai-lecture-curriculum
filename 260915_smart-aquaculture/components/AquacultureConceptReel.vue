<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const items = [
  { text: '센서 빅데이터 수집', icon: 'i-carbon-data-enrichment', color: 'text-sky-400', bg: 'bg-sky-500/10', border: 'border-sky-500/30' },
  { text: '머신러닝 폐사 조기경보', icon: 'i-carbon-chart-line', color: 'text-indigo-400', bg: 'bg-indigo-500/10', border: 'border-indigo-500/30' },
  { text: '딥러닝 수중영상 어체 계수', icon: 'i-carbon-view', color: 'text-purple-400', bg: 'bg-purple-500/10', border: 'border-purple-500/30' },
  { text: 'RCTF 양식일지 자동화', icon: 'i-carbon-script', color: 'text-amber-400', bg: 'bg-amber-500/10', border: 'border-amber-500/30' },
  { text: '06:00 수질 브리핑 에이전트', icon: 'i-carbon-bot', color: 'text-emerald-400', bg: 'bg-emerald-500/10', border: 'border-emerald-500/30' },
]

const currentIndex = ref(0)
const isAnimating = ref(false)
let timer: number | undefined

onMounted(() => {
  timer = window.setInterval(() => {
    isAnimating.value = true
    setTimeout(() => {
      currentIndex.value = (currentIndex.value + 1) % items.length
      isAnimating.value = false
    }, 250)
  }, 2600)
})

onBeforeUnmount(() => {
  if (timer) clearInterval(timer)
})
</script>

<template>
  <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full border transition-all duration-500 backdrop-blur-md shadow-lg"
    :class="[items[currentIndex].bg, items[currentIndex].border]">
    <div class="flex items-center gap-2 text-xs text-white/90 transition-all duration-300 transform"
      :class="isAnimating ? 'opacity-0 -translate-y-2' : 'opacity-100 translate-y-0'">
      <span :class="[items[currentIndex].icon, items[currentIndex].color, 'text-sm']"></span>
      <span class="font-bold tracking-wide font-mono">{{ items[currentIndex].text }}</span>
    </div>
  </div>
</template>
