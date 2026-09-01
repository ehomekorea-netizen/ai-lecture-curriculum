<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showG = computed(() => (props.stage ?? 0) >= 0)
const showP = computed(() => (props.stage ?? 0) >= 1)
const showT = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-3 gap-5 items-stretch">
      <!-- G: Generative -->
      <div
        class="transition-all duration-500 transform"
        :class="[showG ? 'opacity-100 translate-y-0' : 'opacity-20 translate-y-3']"
      >
        <LiquidGlass glow="cyan" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center gap-2.5 mb-3 border-b border-cyan-500/20 pb-2 whitespace-nowrap">
                <span class="text-3xl font-mono font-black text-cyan-400">G</span>
                <span class="text-sm font-bold text-white">Generative (생성형)</span>
              </div>
              <p class="text-xs text-white/80 leading-relaxed m-0 break-keep">
                기존 데이터를 복사하지 않고, 통계적 패턴을 바탕으로 <strong>새로운 텍스트·코드·문서를 직접 합성</strong>합니다.
              </p>
            </div>
            <div class="pt-2.5 border-t border-white/10 text-xs font-mono text-cyan-300 flex items-center justify-between whitespace-nowrap">
              <span>핵심 기능</span>
              <span class="font-bold">신규 콘텐츠 합성</span>
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- P: Pre-trained -->
      <div
        class="transition-all duration-500 transform"
        :class="[showP ? 'opacity-100 translate-y-0' : 'opacity-20 translate-y-3']"
      >
        <LiquidGlass glow="blue" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center gap-2.5 mb-3 border-b border-blue-500/20 pb-2 whitespace-nowrap">
                <span class="text-3xl font-mono font-black text-blue-400">P</span>
                <span class="text-sm font-bold text-white">Pre-trained (사전학습)</span>
              </div>
              <p class="text-xs text-white/80 leading-relaxed m-0 break-keep">
                인터넷의 방대한 공개 데이터와 전문 지식을 미리 공부해 <strong>폭넓은 배경지식과 언어 체계</strong>를 갖췄습니다.
              </p>
            </div>
            <div class="pt-2.5 border-t border-white/10 text-xs font-mono text-blue-300 flex items-center justify-between whitespace-nowrap">
              <span>핵심 기능</span>
              <span class="font-bold">방대한 배경지식</span>
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- T: Transformer -->
      <div
        class="transition-all duration-500 transform"
        :class="[showT ? 'opacity-100 translate-y-0' : 'opacity-20 translate-y-3']"
      >
        <LiquidGlass glow="emerald" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center gap-2.5 mb-3 border-b border-emerald-500/20 pb-2 whitespace-nowrap">
                <span class="text-3xl font-mono font-black text-emerald-400">T</span>
                <span class="text-sm font-bold text-white">Transformer (신경망)</span>
              </div>
              <p class="text-xs text-white/80 leading-relaxed m-0 break-keep">
                단어 간 문맥(Attention)을 종합 파악하여 질문에 이어질 <strong>가장 적절한 다음 단어를 예측</strong>합니다.
              </p>
            </div>
            <div class="pt-2.5 border-t border-white/15 text-xs font-mono font-bold text-emerald-300 flex items-center justify-between whitespace-nowrap">
              <span>핵심 기능</span>
              <span class="font-bold">문맥 추론 & 단어 예측</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Flow Formula -->
    <div
      class="mt-4 transition-all duration-500"
      :class="[showT ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2">
            <span class="i-carbon:chip text-base text-cyan-400"></span>
            <span class="break-keep"><strong>작동 메커니즘:</strong> 사전학습 지식(P) ➔ 문맥 추론(T) ➔ 최적 단어 생성(G)</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold whitespace-nowrap">확률적 문맥 완성</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
