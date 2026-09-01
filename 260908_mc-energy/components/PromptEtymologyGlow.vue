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
    <div class="grid grid-cols-3 gap-6 items-stretch">
      <!-- G: Generative -->
      <div
        class="transition-all duration-500 transform"
        :class="[showG ? 'opacity-100 translate-y-0' : 'opacity-20 translate-y-3']"
      >
        <LiquidGlass glow="cyan" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-76">
            <div>
              <div class="flex items-center justify-between mb-3 border-b border-cyan-500/20 pb-2">
                <div class="text-4xl font-mono font-black text-cyan-400">G</div>
                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold">창작 엔진</span>
              </div>
              <h3 class="text-sm font-bold text-white mb-2">Generative (생성형)</h3>
              <p class="text-xs text-white/70 leading-relaxed m-0">
                기존 데이터를 그대로 복사해 붙여넣는 것이 아니라, 학습된 통계적 패턴을 바탕으로 <strong>새로운 문장과 코드, 보고서를 직접 합성</strong>하여 생성합니다.
              </p>
            </div>
            <div class="pt-3 border-t border-white/10 text-xs font-mono text-cyan-300 flex items-center justify-between">
              <span>핵심 역할</span>
              <span class="font-bold">새로운 콘텐츠 창작</span>
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
          <div class="p-5 flex flex-col justify-between h-76">
            <div>
              <div class="flex items-center justify-between mb-3 border-b border-blue-500/20 pb-2">
                <div class="text-4xl font-mono font-black text-blue-400">P</div>
                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold">지식 베이스</span>
              </div>
              <h3 class="text-sm font-bold text-white mb-2">Pre-trained (사전학습)</h3>
              <p class="text-xs text-white/70 leading-relaxed m-0">
                인터넷 상의 방대한 공개 텍스트와 전문 지식을 사전에 미리 공부하여, 인간의 언어 구조와 세상에 대한 <strong>폭넓은 배경 지식</strong>을 갖추었습니다.
              </p>
            </div>
            <div class="pt-3 border-t border-white/10 text-xs font-mono text-blue-300 flex items-center justify-between">
              <span>핵심 역할</span>
              <span class="font-bold">방대한 지식 기반 구축</span>
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
          <div class="p-5 flex flex-col justify-between h-76">
            <div>
              <div class="flex items-center justify-between mb-3 border-b border-emerald-500/20 pb-2">
                <div class="text-4xl font-mono font-black text-emerald-400">T</div>
                <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">문맥 추론</span>
              </div>
              <h3 class="text-sm font-bold text-white mb-2">Transformer (신경망)</h3>
              <p class="text-xs text-white/80 leading-relaxed m-0">
                문장 내 단어들 간의 관계와 문맥(Attention)을 파악하여, 사용자의 질문에 가장 적절하게 이어질 <strong>다음 단어를 확률적으로 조립</strong>합니다.
              </p>
            </div>
            <div class="pt-3 border-t border-white/15 text-xs font-mono font-bold text-emerald-300 flex items-center justify-between">
              <span>핵심 역할</span>
              <span class="font-bold">문맥 이해 & 단어 예측</span>
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
            <span><strong>작동 메커니즘:</strong> 사전학습된 지식(Pre-trained) ➔ 질문 문맥 파악(Transformer) ➔ 최적의 다음 단어 확률적 생성(Generative)</span>
          </div>
          <span class="text-[11px] font-mono text-white/50">확률적 문맥 완성</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
