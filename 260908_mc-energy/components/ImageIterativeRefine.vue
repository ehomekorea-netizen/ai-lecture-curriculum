<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showFeedback = computed(() => (props.stage ?? 0) >= 1)
const showResult = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-2 select-none">
    
    <div class="grid grid-cols-12 gap-5 items-stretch">
      
      <!-- 1st Draft -->
      <div class="col-span-4 p-5 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md flex flex-col justify-between h-80">
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
            <span class="text-xs font-mono font-bold text-white/70">1차 시도: 단순 요청</span>
            <span class="text-[10px] font-mono text-white/40">초안</span>
          </div>
          <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-white/70 border border-white/10 mb-3">
            "홍보 포스터 만들어줘."
          </div>
          <ul class="text-xs text-white/50 space-y-1.5 pl-4 m-0 leading-relaxed">
            <li>불필요한 글자가 많아 산만함</li>
            <li>핵심 일정·장소가 묻힘</li>
            <li>모바일 가독성 저하</li>
          </ul>
        </div>
        <div class="pt-2 border-t border-white/10 text-xs font-mono text-white/40">개선 필요</div>
      </div>

      <!-- Feedback -->
      <div
        class="col-span-4 p-5 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md flex flex-col justify-between h-80 transition-all duration-500"
        :class="[showFeedback ? 'opacity-100' : 'opacity-20']"
      >
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-blue-500/20 pb-2">
            <span class="text-xs font-mono font-bold text-blue-300">2차 수정: 구조화된 피드백</span>
            <span class="text-[10px] font-mono text-blue-400">지침</span>
          </div>
          <div class="p-3 rounded-xl bg-black/40 font-mono text-xs text-blue-200 border border-blue-500/20 leading-relaxed mb-2">
            "1. 메인 타이틀을 2배 키우고<br/>
            2. 핵심 일정과 장소만 박스로 강조<br/>
            3. 복잡한 배경 장식 제거"
          </div>
        </div>
        <div class="pt-2 border-t border-blue-500/20 text-xs font-mono text-blue-300">시각 위계 조정</div>
      </div>

      <!-- Final Result -->
      <div
        class="col-span-4 p-5 rounded-2xl border border-emerald-500/30 bg-emerald-950/20 backdrop-blur-md shadow-xl flex flex-col justify-between h-80 transition-all duration-700"
        :class="[showResult ? 'opacity-100 translate-y-0' : 'opacity-20 translate-y-2']"
      >
        <div>
          <div class="flex items-center justify-between mb-3 border-b border-emerald-500/20 pb-2">
            <span class="text-xs font-mono font-bold text-emerald-300">최종 완성: 최적화된 결과</span>
            <span class="text-[10px] font-mono text-emerald-400">완성</span>
          </div>
          <ul class="text-xs text-white/80 space-y-2 pl-4 m-0 leading-relaxed my-2">
            <li>헤드라인 가독성 극대화</li>
            <li>일정·장소 3초 내 인지 완료</li>
            <li>모바일 최적화 규격 충족</li>
          </ul>
        </div>
        <div class="pt-2 border-t border-emerald-500/20 text-xs font-mono font-bold text-emerald-300">실무 배포용 완성</div>
      </div>

    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showResult ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
        <span>이미지 생성 AI는 한 번에 완성하는 것이 아니라, <strong>'생성 ➔ 평가 ➔ 수정 지시'</strong>를 거치며 완성됩니다.</span>
      </div>
      <span class="text-[11px] font-mono text-white/40">Iterative Refinement</span>
    </div>

  </div>
</template>
