<script setup lang="ts">
import { Sparkles, Heart } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between items-center select-none font-sans text-slate-800 text-center h-[370px] my-auto py-2">
    <!-- ── Top Subtle Badge ── -->
    <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-50/90 border border-blue-200/80 text-blue-700 text-xs font-mono font-bold shadow-2xs">
      <Sparkles :size="13" class="text-blue-600" />
      <span>AI COLLABORATION STANDARD</span>
    </div>

    <!-- ── Grand Center Statement Typography ── -->
    <div class="my-auto space-y-4 max-w-4xl px-4">
      <h1 class="text-4xl md:text-5xl lg:text-[54px] font-bold font-serif text-slate-900 tracking-tight leading-[1.25] break-keep">
        AI는 초안을 쓰고,<br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-sky-600 to-blue-700 underline decoration-blue-200 decoration-wavy decoration-from-font underline-offset-8">
          가치는 담당자가 담습니다.
        </span>
      </h1>

      <p class="text-base md:text-xl text-slate-500 font-serif font-normal max-w-2xl mx-auto leading-relaxed break-keep pt-2">
        오늘 정의한 <strong>나만의 스킬 하나</strong>가,<br class="hidden sm:inline">
        내일 여러분의 가장 든든한 동료가 됩니다.
      </p>
    </div>

    <!-- ── Bottom Closing Signature & Gratitude ── -->
    <div class="w-full max-w-xl pt-3 border-t border-slate-200/90 flex items-center justify-between text-xs text-slate-400 font-medium">
      <span class="font-mono text-slate-400">Q&A · 경청해 주셔서 감사합니다</span>
      <span class="flex items-center gap-1 text-slate-500 font-serif">
        사회복지 실무자를 위한 AI 협업 실무
      </span>
    </div>
  </div>
</template>

<style scoped>
/* ── Text Shimmer Gradient ── */
@keyframes text-glow {
  0%, 100% { filter: drop-shadow(0 2px 12px rgba(37, 99, 235, 0.12)); }
  50% { filter: drop-shadow(0 4px 20px rgba(37, 99, 235, 0.25)); }
}

h1 {
  animation: text-glow 4s ease-in-out infinite;
}
</style>
