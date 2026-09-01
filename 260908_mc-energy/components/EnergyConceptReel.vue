<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

const items = [
  { text: 'MC에너지 실무 역량 강화', icon: 'i-carbon:flash', color: 'text-blue-400', bg: 'bg-blue-500/10', border: 'border-blue-500/30' },
  { text: '2026 최신 AI 트렌드 & 본질', icon: 'i-carbon:network-enterprise', color: 'text-cyan-400', bg: 'bg-cyan-500/10', border: 'border-cyan-500/30' },
  { text: '개인 맞춤설정 & 직무 기본값 고정', icon: 'i-carbon:settings-adjust', color: 'text-sky-400', bg: 'bg-sky-500/10', border: 'border-sky-500/30' },
  { text: '정보보안 마스킹 & 사내 RAG', icon: 'i-carbon:locked', color: 'text-indigo-400', bg: 'bg-indigo-500/10', border: 'border-indigo-500/30' },
  { text: 'RCTF 4대 기둥 실전 지시법', icon: 'i-carbon:task-complete', color: 'text-purple-400', bg: 'bg-purple-500/10', border: 'border-purple-500/30' },
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
