<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0,
})

const slideContext = useSlideContext()
const currentStage = computed(() => {
  const ctxClicks = slideContext?.$clicks?.value ?? slideContext?.$nav?.clicks ?? 0
  return Math.max(props.stage ?? 0, ctxClicks)
})

const showCard1 = computed(() => currentStage.value >= 1)
const showCard2 = computed(() => currentStage.value >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none py-1">
    <!-- Top: Direct UI Screenshot -->
    <div class="w-full flex justify-center mb-3">
      <img
        src="/gemini-notebook-ui.png"
        alt="Gemini Notebook UI"
        class="rounded-xl w-full max-w-4xl max-h-56 object-contain select-none"
      />
    </div>

    <!-- Bottom: 2 Key Pillar Cards (Interactive Clicks) -->
    <div class="grid grid-cols-2 gap-4 w-full max-w-4xl mx-auto">
      <!-- Feature 1: Grounding -->
      <div
        class="transition-all duration-500 transform"
        :class="[showCard1 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="showCard1 ? 'cyan' : 'neutral'" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div>
              <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs mb-1 border-b border-cyan-500/20 pb-1">
                <span class="i-carbon:catalog text-sm"></span>
                <span>Grounding on Your Sources (내 문서 근거 답변)</span>
              </div>
              <p class="text-xs text-white/80 m-0 leading-relaxed">
                인터넷의 불확실한 지식이 아니라, <strong class="text-cyan-200">직접 업로드한 사내 문서·PDF 안에서만 답변</strong>을 도출하고 각주를 표시합니다.
              </p>
            </div>
            <div class="text-[10px] font-mono text-cyan-300/80 pt-1 border-t border-white/10">
              100% 팩트 보장
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Feature 2: Instant RAG Practice -->
      <div
        class="transition-all duration-500 transform"
        :class="[showCard2 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="showCard2 ? 'emerald' : 'neutral'" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div>
              <div class="flex items-center gap-2 text-emerald-300 font-bold text-xs mb-1 border-b border-emerald-500/20 pb-1">
                <span class="i-carbon:locked text-sm"></span>
                <span>코딩 없는 즉시 구축형 RAG 솔루션</span>
              </div>
              <p class="text-xs text-white/90 m-0 leading-relaxed">
                복잡한 벡터 DB나 코딩 구축 없이, <strong class="text-emerald-200">파일 드래그 앤 드롭만으로 사내 전용 RAG 시스템</strong>이 즉시 완성됩니다.
              </p>
            </div>
            <div class="text-[10px] font-mono text-emerald-300 font-bold pt-1 border-t border-white/10">
              실무 즉시 도입 가능
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
