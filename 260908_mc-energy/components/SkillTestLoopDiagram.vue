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
        <span class="text-xs font-mono font-bold text-white/80 uppercase tracking-wider">Skill 검증 및 개선 사이클</span>
        <span class="text-[11px] font-mono text-white/40">Refinement Loop</span>
      </div>

      <div class="grid grid-cols-6 gap-3">
        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">01</div>
          <div class="text-xs font-bold text-white mb-1">초안 생성</div>
          <div class="text-[10px] text-white/50">4대 기준 정의</div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">02</div>
          <div class="text-xs font-bold text-white mb-1">실제 실행</div>
          <div class="text-[10px] text-white/50">데이터 주입</div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">03</div>
          <div class="text-xs font-bold text-white mb-1">결과 확인</div>
          <div class="text-[10px] text-white/50">품질 점검</div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">04</div>
          <div class="text-xs font-bold text-white mb-1">문제 발견</div>
          <div class="text-[10px] text-white/50">오차 파악</div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/40 border border-white/10 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-white/40 mb-1">05</div>
          <div class="text-xs font-bold text-white mb-1">지침 수정</div>
          <div class="text-[10px] text-white/50">제약 구체화</div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/40 border border-emerald-500/30 flex flex-col justify-between text-center">
          <div class="text-xs font-mono font-bold text-emerald-400 mb-1">06</div>
          <div class="text-xs font-bold text-emerald-300 mb-1">표준화 확정</div>
          <div class="text-[10px] text-emerald-200/60">재사용 등록</div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showTakeaway ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-emerald-400"></span>
        <span>좋은 Skill은 한 번에 완성되지 않습니다. <strong>실제 실행 ➔ 문제 발견 ➔ 지침 수정</strong>을 통해 표준 매뉴얼로 진화합니다.</span>
      </div>
      <span class="text-[11px] font-mono text-white/40">Continuous Refinement</span>
    </div>

  </div>
</template>
