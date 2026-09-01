<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showTools = computed(() => (props.stage ?? 0) >= 1)
const showTakeaway = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between h-full select-none">
    <div class="p-3.5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-full space-y-2.5">
      <!-- User & Orchestrator Flow -->
      <div class="grid grid-cols-2 gap-2">
        <div class="p-2.5 rounded-xl bg-black/40 border border-white/10 flex flex-col items-center justify-center text-center">
          <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center text-white mb-1">
            <span class="i-carbon:user text-base"></span>
          </div>
          <span class="text-xs font-bold text-white">사용자</span>
          <span class="text-[10px] text-white/50">자연어 지시</span>
        </div>

        <div class="p-2.5 rounded-xl border border-blue-500/40 bg-blue-950/30 flex flex-col items-center justify-center text-center">
          <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 mb-1">
            <span class="i-carbon:network-4 text-base"></span>
          </div>
          <span class="text-xs font-bold text-blue-300">오케스트레이션</span>
          <span class="text-[10px] text-blue-300/70">도구 자율 매칭</span>
        </div>
      </div>

      <!-- Connected Tools -->
      <div
        class="space-y-1.5 transition-all duration-500"
        :class="[showTools ? 'opacity-100' : 'opacity-30']"
      >
        <div class="p-1.5 px-2.5 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
          <span class="font-mono font-semibold text-white">@document</span>
          <span class="text-[10px] text-white/50">문서 편집</span>
        </div>
        <div class="p-1.5 px-2.5 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
          <span class="font-mono font-semibold text-white">@spreadsheet</span>
          <span class="text-[10px] text-white/50">데이터 분석</span>
        </div>
        <div class="p-1.5 px-2.5 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
          <span class="font-mono font-semibold text-white">@visualize</span>
          <span class="text-[10px] text-white/50">차트 시각화</span>
        </div>
        <div class="p-1.5 px-2.5 rounded-lg bg-blue-950/40 border border-blue-500/30 flex items-center justify-between text-xs">
          <span class="font-mono font-bold text-cyan-300">@LG ThinQ</span>
          <span class="text-[10px] text-cyan-300/80 font-bold">기기 직접 제어</span>
        </div>
      </div>

      <!-- Bottom Principle -->
      <div
        class="p-2 rounded-xl bg-black/40 border border-white/10 text-[10.5px] text-white/70 leading-relaxed transition-all duration-500"
        :class="[showTakeaway ? 'opacity-100' : 'opacity-40']"
      >
        AI가 모든 작업을 직접 하지 않고, <strong>연결된 전문 도구를 호출하여 업무를 완결</strong>합니다.
      </div>
    </div>
  </div>
</template>
