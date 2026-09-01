<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showWork = computed(() => (props.stage ?? 0) >= 1)
const showTakeaway = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-2 select-none">
    <div class="grid grid-cols-12 gap-8 items-stretch">
      
      <!-- Left: CHAT Mode -->
      <div class="col-span-5 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-80">
        <div>
          <div class="flex items-center justify-between mb-4 border-b border-white/10 pb-3">
            <span class="text-xs font-mono font-bold text-white/70 uppercase tracking-wider">CHAT (대화 모드)</span>
            <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-white/10 text-white/50">도움을 받는 것</span>
          </div>

          <div class="space-y-2.5 my-3 text-xs">
            <div class="p-2.5 rounded-xl bg-black/30 border border-white/5 flex items-center justify-between text-white/80">
              <span class="font-semibold">1. 질문 입력</span>
              <span class="text-white/40 font-mono text-[11px]">"정보 알려줘"</span>
            </div>
            <div class="p-2.5 rounded-xl bg-black/30 border border-white/5 flex items-center justify-between text-white/80">
              <span class="font-semibold">2. 텍스트 답변</span>
              <span class="text-white/40 font-mono text-[11px]">화면 표시</span>
            </div>
            <div class="p-2.5 rounded-xl bg-black/30 border border-rose-500/20 flex items-center justify-between text-rose-300">
              <span class="font-semibold">3. 사람의 직접 실행</span>
              <span class="text-rose-300/60 font-mono text-[11px]">복사 / 붙여넣기</span>
            </div>
          </div>
        </div>

        <div class="pt-3 border-t border-white/10 text-xs text-white/50 flex items-center justify-between">
          <span>작업 주체</span>
          <span class="font-semibold text-white/80">사용자가 직접 완결</span>
        </div>
      </div>

      <!-- Center Divider Arrow -->
      <div class="col-span-2 flex flex-col items-center justify-center">
        <div
          class="w-12 h-12 rounded-full border border-white/15 bg-white/5 flex items-center justify-center text-white/70 shadow-md transition-all duration-500"
          :class="[showWork ? 'scale-110 border-blue-400/50 bg-blue-500/10 text-blue-400' : 'opacity-30']"
        >
          <span class="i-carbon:arrow-right text-xl hidden md:block"></span>
          <span class="i-carbon:arrow-down text-xl md:hidden"></span>
        </div>
        <span class="text-[11px] font-mono text-white/40 mt-2">패러다임 전환</span>
      </div>

      <!-- Right: WORK Mode -->
      <div
        class="col-span-5 p-6 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-xl flex flex-col justify-between h-80 transition-all duration-500"
        :class="[showWork ? 'opacity-100 translate-x-0' : 'opacity-20 translate-x-2']"
      >
        <div>
          <div class="flex items-center justify-between mb-4 border-b border-blue-500/20 pb-3">
            <span class="text-xs font-mono font-bold text-blue-300 uppercase tracking-wider">WORK (실행 모드)</span>
            <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold">일을 맡기는 것</span>
          </div>

          <div class="space-y-1.5 my-2 text-xs">
            <div class="p-2 rounded-xl bg-black/40 border border-white/5 text-white/90 flex items-center justify-between">
              <span>① 목표 전달 및 맥락 제시</span>
              <span class="text-[10px] font-mono text-white/40">Goal</span>
            </div>
            <div class="p-2 rounded-xl bg-black/40 border border-white/5 text-white/90 flex items-center justify-between">
              <span>② 다단계 도구 실행 및 분석</span>
              <span class="text-[10px] font-mono text-white/40">Execution</span>
            </div>
            <div class="p-2 rounded-xl bg-black/40 border border-emerald-500/30 text-emerald-300 font-semibold flex items-center justify-between">
              <span>③ 완성형 파일 및 산출물 생성</span>
              <span class="text-[10px] font-mono text-emerald-400">DOCX · XLSX</span>
            </div>
          </div>
        </div>

        <div class="pt-3 border-t border-blue-500/20 text-xs text-blue-300/80 flex items-center justify-between">
          <span>작업 주체</span>
          <span class="font-bold text-blue-300">AI가 작업을 스스로 완결</span>
        </div>
      </div>

    </div>

    <!-- Bottom Takeaway Callout -->
    <div
      class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showTakeaway ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2.5">
        <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
        <span><strong>핵심 공식:</strong> <strong>Chat</strong>은 질문에 답을 구하는 것이고, <strong>Work</strong>는 실제 완성형 결과물을 맡기는 것입니다.</span>
      </div>
      <span class="text-[11px] font-mono text-white/40">Chat ➔ Work</span>
    </div>
  </div>
</template>
