<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const cases = [
  {
    id: 1,
    title: 'AI 오디오 오버뷰로 어디서나 학습',
    desc: '클릭 한 번으로 문서를 청취 가능한 개요로 변환해 보세요. 멀티태스킹 중이거나 들으면서 학습하는 것을 선호하는 경우 콘텐츠의 핵심을 빠르게 파악할 수 있습니다.',
    image: '/AI 오디오 오버뷰로 어디서나 학습.webp',
    imagePosition: 'left'
  },
  {
    id: 2,
    title: '경영진을 위한 인사이트 및 전략 계획 가속화',
    desc: '재무 보고서, 시장 분석, 내부 전략 문서를 업로드하여 핵심 요약 작성, 측정항목 추출, 전략적 영향 파악 등을 요청합니다.',
    image: '/경영진을 위한 인사이트 및 전략 계획의 가속화.webp',
    imagePosition: 'right'
  },
  {
    id: 3,
    title: '연구 간소화 및 더 빠른 격차 파악',
    desc: '주요 연구 결과를 요약하고, 트렌드를 파악하거나 다양한 접근방식을 비교해 달라고 요청할 수 있으며, 이 모든 작업에는 검증을 위한 인용이 포함됩니다.',
    image: '/연구 간소화 및 더 빠른 격차 파악.webp',
    imagePosition: 'left'
  },
  {
    id: 4,
    title: '온보딩 가속화 및 교육 간소화',
    desc: '교육 매뉴얼, 가이드, 정책 문서, FAQ를 업로드합니다. 신입 사원은 이를 활용해 방대한 문서에 숨은 정보를 빠르게 찾거나, 특정 프로세스에 대해 질문할 수 있습니다.',
    image: '/온보딩 가속화 및 교육 간소화.webp',
    imagePosition: 'right'
  },
  {
    id: 5,
    title: '빠르고 정확한 정보로 실무·영업팀 역량 강화',
    desc: '제품 사양 및 시장 조사를 Gemini Notebook에 업로드합니다. 맞춤형 계획을 손쉽게 세우고 관련 질문에 답해 달라고 요청하면 더 자신감 있게 실무 및 영업 상담을 진행할 수 있습니다.',
    image: '/빠르고 정확한 정보로 영업팀의 역량 강화.webp',
    imagePosition: 'left'
  }
]

const currentCase = computed(() => {
  const stage = props.stage ?? 0
  const idx = Math.min(Math.max(stage, 0), cases.length - 1)
  return cases[idx]
})
</script>

<template>
  <div class="w-full h-[290px] flex items-center justify-center select-none font-sans relative overflow-hidden">
    <Transition name="statement-fade" mode="out-in">
      <div
        :key="currentCase.id"
        class="w-full flex items-center justify-between gap-8"
      >
        <!-- Layout: Image Left / Text Right -->
        <template v-if="currentCase.imagePosition === 'left'">
          <div class="w-[45%] flex items-center justify-center">
            <img
              :src="currentCase.image"
              :alt="currentCase.title"
              class="w-full max-h-[290px] object-contain rounded-xl"
            />
          </div>
          <div class="w-[55%] text-left space-y-3 pr-1">
            <h2 class="text-[23px] md:text-[25px] font-serif font-bold text-slate-900 leading-snug tracking-tight break-keep">
              {{ currentCase.title }}
            </h2>
            <p class="text-[14.5px] md:text-[15px] font-sans font-medium text-slate-800 leading-relaxed break-keep">
              {{ currentCase.desc }}
            </p>
          </div>
        </template>

        <!-- Layout: Text Left / Image Right -->
        <template v-else>
          <div class="w-[55%] text-left space-y-3 pl-1">
            <h2 class="text-[23px] md:text-[25px] font-serif font-bold text-slate-900 leading-snug tracking-tight break-keep">
              {{ currentCase.title }}
            </h2>
            <p class="text-[14.5px] md:text-[15px] font-sans font-medium text-slate-800 leading-relaxed break-keep">
              {{ currentCase.desc }}
            </p>
          </div>
          <div class="w-[45%] flex items-center justify-center">
            <img
              :src="currentCase.image"
              :alt="currentCase.title"
              class="w-full max-h-[290px] object-contain rounded-xl"
            />
          </div>
        </template>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.statement-fade-enter-active,
.statement-fade-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.statement-fade-enter-from {
  opacity: 0;
  transform: translateY(12px) scale(0.985);
}

.statement-fade-leave-to {
  opacity: 0;
  transform: translateY(-12px) scale(0.985);
}
</style>
