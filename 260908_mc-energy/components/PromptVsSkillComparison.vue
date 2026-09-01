<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showSkill = computed(() => (props.stage ?? 0) >= 1)
const showTakeaway = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-2 select-none">
    
    <div class="grid grid-cols-12 gap-8 items-stretch">
      
      <!-- Left: Prompt -->
      <div class="col-span-5 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-80">
        <div>
          <div class="flex items-center gap-2 mb-4 border-b border-white/10 pb-3">
            <span class="i-carbon:terminal text-base text-white/60"></span>
            <span class="text-sm font-bold text-white tracking-wide">PROMPT (1회성 지시)</span>
          </div>

          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-white/80 border border-white/10 mb-3">
            "이번에 이 업무 처리해줘."
          </div>

          <ul class="text-xs text-white/60 space-y-1.5 pl-4 m-0 leading-relaxed">
            <li>업무마다 매번 프롬프트를 다시 작성</li>
            <li>작성자의 숙련도에 따라 품질 편차 발생</li>
            <li>대화창이 닫히면 사라지는 휘발성 지시</li>
          </ul>
        </div>

        <div class="pt-3 border-t border-white/10 text-xs font-mono text-white/40">개인 단위 1회성 실행</div>
      </div>

      <!-- Center Arrow -->
      <div class="col-span-2 flex flex-col items-center justify-center">
        <div
          class="w-12 h-12 rounded-full border border-white/15 bg-white/5 flex items-center justify-center text-white/70 shadow-md transition-all duration-500"
          :class="[showSkill ? 'scale-110 border-blue-400/50 bg-blue-500/10 text-blue-400' : 'opacity-30']"
        >
          <span class="i-carbon:arrow-right text-xl hidden md:block"></span>
          <span class="i-carbon:arrow-down text-xl md:hidden"></span>
        </div>
        <span class="text-[11px] font-mono text-cyan-300 font-bold mt-2">업무 자산화</span>
      </div>

      <!-- Right: Skill -->
      <div
        class="col-span-5 p-6 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-xl flex flex-col justify-between h-80 transition-all duration-500"
        :class="[showSkill ? 'opacity-100 translate-x-0' : 'opacity-20 translate-x-2']"
      >
        <div>
          <div class="flex items-center gap-2 mb-4 border-b border-blue-500/20 pb-3">
            <span class="i-carbon:catalog text-base text-blue-400"></span>
            <span class="text-sm font-bold text-blue-300 tracking-wide">SKILL (재사용 업무 매뉴얼)</span>
          </div>

          <div class="p-3.5 rounded-xl bg-black/40 font-mono text-xs text-blue-200 border border-blue-500/20 mb-3">
            "앞으로 이 업무는 항상 이 프로세스로 수행하라."
          </div>

          <ul class="text-xs text-white/80 space-y-1.5 pl-4 m-0 leading-relaxed">
            <li><strong>목적·자료·절차·결과물 기준</strong>이 사전 고정됨</li>
            <li>누가 실행해도 100% 동일한 고품질 보장</li>
            <li>팀과 조직 전체에 공유하여 즉시 재사용</li>
          </ul>
        </div>

        <div class="pt-3 border-t border-blue-500/20 text-xs font-mono font-bold text-blue-300">조직 단위 표준 자산</div>
      </div>

    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-4 p-3 px-4 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showTakeaway ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
        <span><strong>Prompt</strong>는 1회성 요청이고, <strong>Skill</strong>은 반복 가능한 표준 업무 매뉴얼입니다.</span>
      </div>
      <span class="text-[11px] font-mono text-cyan-300 font-bold">업무 표준 자산화</span>
    </div>

  </div>
</template>
