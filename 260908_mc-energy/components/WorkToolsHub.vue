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
  <div class="w-full flex flex-col justify-between py-1 select-none">
    
    <div class="p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl">
      <div class="grid grid-cols-12 gap-4 items-center">
        
        <!-- Left: User -->
        <div class="col-span-3 p-4 rounded-xl bg-black/40 border border-white/10 flex flex-col items-center justify-center text-center h-48">
          <div class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center text-white mb-2">
            <span class="i-carbon:user text-xl"></span>
          </div>
          <span class="text-xs font-bold text-white mb-0.5">사용자</span>
          <span class="text-[10px] text-white/50">자연어 업무 지시</span>
        </div>

        <!-- Center: Work Orchestrator -->
        <div class="col-span-4 flex flex-col items-center justify-center">
          <div class="p-4 rounded-xl border border-blue-500/30 bg-blue-950/20 shadow-md flex flex-col items-center justify-center text-center w-full h-48">
            <div class="h-6 flex items-center bg-white px-2.5 py-0.5 rounded-lg shadow-sm mb-2">
              <img src="/gptwork.png" alt="ChatGPT Work" class="h-4 w-auto object-contain" />
            </div>
            <span class="text-xs font-bold text-white mb-1">중앙 오케스트레이션</span>
            <span class="text-[10px] font-mono text-blue-300">작업 분해 & 도구 호출</span>
          </div>
        </div>

        <!-- Right: Connected Tools -->
        <div
          class="col-span-5 space-y-1.5 transition-all duration-500"
          :class="[showTools ? 'opacity-100 translate-x-0' : 'opacity-20 translate-x-2']"
        >
          <div class="p-2 px-3 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
            <span class="font-mono font-semibold text-white">@document</span>
            <span class="text-[10px] text-white/50">문서 편집</span>
          </div>

          <div class="p-2 px-3 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
            <span class="font-mono font-semibold text-white">@spreadsheet</span>
            <span class="text-[10px] text-white/50">데이터 분석</span>
          </div>

          <div class="p-2 px-3 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-xs">
            <span class="font-mono font-semibold text-white">@visualize</span>
            <span class="text-[10px] text-white/50">차트 시각화</span>
          </div>

          <div class="p-2 px-3 rounded-lg bg-black/40 border border-blue-500/20 flex items-center justify-between text-xs">
            <span class="font-mono font-semibold text-blue-300">외부 Apps & Connectors</span>
            <span class="text-[10px] text-blue-300/60">기기·서비스 연동</span>
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-3 p-3 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/80 transition-all duration-500"
      :class="[showTakeaway ? 'opacity-100' : 'opacity-20']"
    >
      <span>AI 모델 자체가 모든 것을 다 하는 것이 아니라, <strong>사용 가능한 전문 도구가 연결·확장되는 생태계</strong>입니다.</span>
      <span class="text-[11px] font-mono text-white/40">Tool Ecosystem</span>
    </div>

  </div>
</template>
