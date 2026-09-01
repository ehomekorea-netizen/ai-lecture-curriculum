<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const slideContext = useSlideContext()
const currentStage = computed(() => {
  const ctxClicks = slideContext?.$clicks?.value ?? slideContext?.$nav?.clicks ?? 0
  return Math.max(props.stage ?? 0, ctxClicks)
})

const pipelineSteps = [
  {
    step: '1단계',
    title: '데이터 상태 파악',
    eng: 'Inspection',
    icon: 'i-carbon:search',
    prompt: '"각 열의 의미를 파악하고 결측값, 이상값, 중복을 표로 정리해줘. (임의 수정 금지)"',
    core: '데이터 무결성 사전 검증',
    color: 'cyan',
  },
  {
    step: '2단계',
    title: '추이 분석 & 원인',
    eng: 'Analysis',
    icon: 'i-carbon:analytics',
    prompt: '"월별 매출 추이를 분석하고 전월 대비 증감률(MoM)과 상위 5대 항목 원인을 찾아줘."',
    core: '근거 기반 통계 산출',
    color: 'blue',
  },
  {
    step: '3단계',
    title: '시각화 차트 생성',
    eng: 'Visualization',
    icon: 'i-carbon:chart-line',
    prompt: '"@visualize 월별 변화 추이가 눈에 띄도록 꺾은선 차트와 목표선을 추가해줘."',
    core: '의사결정 시각화',
    color: 'amber',
  },
  {
    step: '4단계',
    title: '피드백 점진적 수정',
    eng: 'Iterative Refine',
    icon: 'i-carbon:renew',
    prompt: '"증감이 큰 달을 강조하고, 임원 보고용 3줄 인사이트를 하단에 추가해줘."',
    core: '최종 보고서 완성',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="relative py-2">
      <div class="grid grid-cols-4 gap-4 relative z-10">
        <div
          v-for="(item, idx) in pipelineSteps"
          :key="item.step"
          class="transition-all duration-500 transform"
          :class="[
            currentStage >= idx ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2',
          ]"
        >
          <LiquidGlass
            :glow="item.color === 'cyan' ? 'cyan' : item.color === 'blue' ? 'blue' : item.color === 'amber' ? 'amber' : 'emerald'"
            :radius="14"
            class="h-full"
          >
            <div class="p-4 flex flex-col justify-between h-72">
              <div>
                <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
                  <div class="flex items-center gap-1.5">
                    <span :class="[item.icon, 'text-base', item.color === 'cyan' ? 'text-cyan-400' : item.color === 'blue' ? 'text-blue-400' : item.color === 'amber' ? 'text-amber-400' : 'text-emerald-400']"></span>
                    <strong class="text-xs text-white">{{ item.title }}</strong>
                  </div>
                  <span class="text-[10px] font-mono text-white/50">{{ item.step }}</span>
                </div>

                <div class="p-2 rounded-lg bg-black/40 border border-white/5 font-mono text-[10px] text-white/90 leading-relaxed mb-2">
                  {{ item.prompt }}
                </div>
              </div>

              <div class="pt-2 border-t border-white/10 text-[10px] font-mono" :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'amber' ? 'text-amber-300' : 'text-emerald-300'">
                ✓ {{ item.core }}
              </div>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-2 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-2.5 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2">
            <span class="i-carbon:information-filled text-cyan-400"></span>
            <span><strong>핵심 전략:</strong> 처음부터 완벽한 표를 요구하지 않고, <strong>[점검 ➔ 분석 ➔ 시각화 ➔ 보고서]</strong> 단계로 발전시킵니다.</span>
          </div>
          <span class="text-[10px] font-mono text-cyan-300">4단계 완결형</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
