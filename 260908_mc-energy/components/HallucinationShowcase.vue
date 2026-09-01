<script setup lang="ts">
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0,
})
</script>

<template>
  <div class="grid grid-cols-12 gap-8 items-center mt-2">
    <!-- Left: Image Box -->
    <div class="col-span-5 flex justify-center">
      <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-2 shadow-2xl">
        <img
          src="/hallucination-macbook.png"
          alt="Hallucination Example"
          class="rounded-xl w-full max-h-76 object-contain"
        />
      </div>
    </div>

    <!-- Right: LiquidGlass Cards -->
    <div class="col-span-7 flex flex-col justify-between h-80">
      <div class="space-y-4">
        <!-- Cause Card -->
        <div>
          <LiquidGlass glow="pink" :radius="14">
            <div class="p-4">
              <div class="flex items-center gap-2 text-rose-300 font-bold text-xs mb-1.5">
                <span class="i-carbon:warning-alt-filled"></span>
                <span>발생 원인: 확률적 단어 조합의 한계</span>
              </div>
              <p class="text-xs text-white/80 m-0 leading-relaxed">
                AI는 진실을 알고 말하는 것이 아니라, 질문 문맥상 <strong class="text-rose-200">가장 자연스러워 보이는 다음 단어를 통계적으로 이어 붙이기 때문</strong>에 사실이 아닌 것도 확신에 차서 답변합니다.
              </p>
            </div>
          </LiquidGlass>
        </div>

        <!-- Solution Card (Step 1) -->
        <div
          class="transition-all duration-500"
          :class="[
            (props.stage ?? 0) >= 1
              ? 'opacity-100 translate-y-0'
              : 'opacity-20 translate-y-2'
          ]"
        >
          <LiquidGlass glow="cyan" :radius="14">
            <div class="p-4">
              <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs mb-1.5">
                <span class="i-carbon:security"></span>
                <span>실무 해결책: 제약 조건 + 근거 자료(RAG) 주입</span>
              </div>
              <p class="text-xs text-white/90 m-0 leading-relaxed">
                "모르는 내용은 추측하지 말고 모른다고 답하라"는 <strong class="text-cyan-200">네거티브 제약(Negative Constraint)</strong>과 사내 근거 문서를 함께 제공하면 환각을 100% 방지할 수 있습니다.
              </p>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>
