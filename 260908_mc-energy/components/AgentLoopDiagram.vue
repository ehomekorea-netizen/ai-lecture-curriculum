<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showTakeaway = computed(() => (props.stage ?? 0) >= 1)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-2 select-none">
    
    <div class="p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-xl">
      <div class="flex items-center justify-between mb-5 border-b border-white/10 pb-3">
        <span class="text-xs font-mono font-bold text-white/80 uppercase tracking-wider">에이전트 6단계 작업 실행 루프</span>
        <span class="text-[11px] font-mono text-white/40">Action Loop</span>
      </div>

      <div class="grid grid-cols-6 gap-3">
        <!-- Step 1 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">01</div>
          <div class="text-xs font-bold text-white mb-1">목표 이해</div>
          <div class="text-[10px] text-white/50">지시 분석</div>
        </div>

        <!-- Step 2 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">02</div>
          <div class="text-xs font-bold text-white mb-1">계획 수립</div>
          <div class="text-[10px] text-white/50">절차 설계</div>
        </div>

        <!-- Step 3 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">03</div>
          <div class="text-xs font-bold text-white mb-1">도구 선택</div>
          <div class="text-[10px] text-white/50">도구 매칭</div>
        </div>

        <!-- Step 4 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">04</div>
          <div class="text-xs font-bold text-white mb-1">실행</div>
          <div class="text-[10px] text-white/50">파일 생성</div>
        </div>

        <!-- Step 5 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">05</div>
          <div class="text-xs font-bold text-white mb-1">결과 확인</div>
          <div class="text-[10px] text-white/50">품질 검증</div>
        </div>

        <!-- Step 6 -->
        <div class="p-3.5 rounded-xl bg-black/40 border border-blue-500/30 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-blue-400 mb-1">06</div>
          <div class="text-xs font-bold text-blue-300 mb-1">수정 / 개선</div>
          <div class="text-[10px] text-blue-200/60">피드백 반영</div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Callout -->
    <div
      class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex flex-col gap-1 text-xs text-white/80 transition-all duration-500"
      :class="[showTakeaway ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
        <span>에이전트의 본질은 단순히 '생각하는 것'이 아니라, <strong>도구를 활용해 실제 파일과 업무를 완결하는 것</strong>입니다.</span>
      </div>
    </div>

  </div>
</template>
