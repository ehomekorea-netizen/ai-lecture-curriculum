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
    <!-- Top: Direct Crisp Visual (No Shell Wrapper) -->
    <div class="w-full flex justify-center mb-3">
      <img
        src="/hallucination-macbook.png"
        alt="환각(Hallucination) 사례 화면: 세종대왕 맥북프로 던짐 사건"
        class="rounded-xl w-full max-w-4xl max-h-56 object-contain select-none"
      />
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
                <span>발생 원인: 확률적 서사 조립의 한계</span>
              </div>
              <p class="text-xs text-white/80 m-0 leading-relaxed">
                위 화면처럼 질문의 허위 전제를 검증하지 않고, <strong class="text-rose-200">문맥상 그럴듯한 다음 단어(1434년 발생 등)를 확률적으로 지어내어</strong> 확신에 차서 답변합니다.
              </p>
            </div>
            <div class="text-[10px] font-mono text-rose-300/80 pt-1 border-t border-white/10">
              허위 전제 무비판 수용
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
                <span>실무 해결책: 근거 문서(RAG) + 제약 조건 주입</span>
              </div>
              <p class="text-xs text-white/90 m-0 leading-relaxed">
                "사내 문서에 없는 사실은 추측하지 말고 모른다고 답하라"는 <strong class="text-cyan-200">네거티브 제약(Negative Constraint)</strong>과 공식 문서를 주입해 환각을 100% 차단합니다.
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
