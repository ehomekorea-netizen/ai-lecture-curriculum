<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0,
})

const showSolution = computed(() => (props.stage ?? 0) >= 1)
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none py-1">
    <!-- Top: Enlarged Crisp Visual Showcase -->
    <div class="w-full flex justify-center mb-3">
      <div class="w-full max-w-4xl flex items-center justify-center">
        <img
          src="/hallucination-macbook.png"
          alt="환각(Hallucination) 사례 화면"
          class="rounded-xl w-full max-h-52 object-contain select-none drop-shadow-2xl"
        />
      </div>
    </div>

    <!-- Bottom: 2 Minimal Clear Pillar Cards (Cause vs Solution) -->
    <div class="grid grid-cols-2 gap-4 w-full max-w-4xl mx-auto">
      <!-- Cause Card -->
      <div class="transition-all duration-500">
        <LiquidGlass glow="pink" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div>
              <div class="flex items-center gap-2 text-rose-300 font-bold text-xs mb-1 border-b border-rose-500/20 pb-1">
                <span class="i-carbon:warning-alt-filled text-sm"></span>
                <span>발생 원인: 확률적 단어 조합의 한계</span>
              </div>
              <p class="text-xs text-white/80 m-0 leading-relaxed">
                진실을 인지하는 것이 아니라, 문맥상 <strong class="text-rose-200">가장 그럴듯한 다음 단어를 확률적으로 조립</strong>하기 때문에 오답을 확신에 차서 생성합니다.
              </p>
            </div>
            <div class="text-[10px] font-mono text-rose-300/80 pt-1 border-t border-white/10">
              통계적 환각 발생
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Solution Card -->
      <div
        class="transition-all duration-500 transform"
        :class="[showSolution ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
      >
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div>
              <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs mb-1 border-b border-cyan-500/20 pb-1">
                <span class="i-carbon:security text-sm"></span>
                <span>실무 해결책: 제약 조건 + 근거 자료(RAG) 주입</span>
              </div>
              <p class="text-xs text-white/90 m-0 leading-relaxed">
                "문서에 없는 사실은 추측 금지"라는 <strong class="text-cyan-200">네거티브 제약</strong>과 사내 공식 문서를 함께 제공하여 환각을 완벽히 차단합니다.
              </p>
            </div>
            <div class="text-[10px] font-mono text-cyan-300 font-bold pt-1 border-t border-white/10">
              100% 팩트 통제
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
