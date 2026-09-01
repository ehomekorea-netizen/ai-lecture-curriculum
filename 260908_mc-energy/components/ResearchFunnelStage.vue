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

const steps = [
  {
    step: '01',
    name: '질문 구체화',
    icon: 'i-carbon:help',
    desc: '검색 목적과 핵심 키워드, 타깃 연도를 명확히 정의',
    action: '모호한 키워드 ➔ 타깃 쿼리 변환',
    color: 'cyan',
  },
  {
    step: '02',
    name: '다중 소스 수집',
    icon: 'i-carbon:data-volume',
    desc: '공공 통계, 전문 보고서, 사내 DB 등 다각도 자료 확보',
    action: '단일 검색결과 의존 탈피',
    color: 'blue',
  },
  {
    step: '03',
    name: '교차 검증',
    icon: 'i-carbon:rule-test',
    desc: '서로 다른 출처 간 상충 수치와 발행 시점 대조 검증',
    action: '오차 및 할루시네이션 원천 차단',
    color: 'violet',
  },
  {
    step: '04',
    name: '종합 보고서화',
    icon: 'i-carbon:document-sentiment',
    desc: '3줄 핵심 결론, 비교 분석표, 실무 시사점 도출',
    action: '의사결정용 1페이지 완성',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- 4-Step Cards (Clean Headers, No Orphan Line Wrap) -->
    <div class="grid grid-cols-4 gap-4 my-2">
      <div
        v-for="(item, idx) in steps"
        :key="item.step"
        class="transition-all duration-500 transform"
        :class="[
          currentStage >= idx ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98',
        ]"
      >
        <LiquidGlass
          :glow="currentStage >= idx ? (item.color === 'cyan' ? 'cyan' : item.color === 'blue' ? 'blue' : item.color === 'violet' ? 'violet' : 'emerald') : 'neutral'"
          :radius="14"
          class="h-full"
        >
          <div class="p-4 flex flex-col justify-between h-68">
            <div>
              <div class="flex items-center gap-2 mb-2.5 pb-2 border-b border-white/10 whitespace-nowrap">
                <span :class="[item.icon, 'text-base', item.color === 'cyan' ? 'text-cyan-400' : item.color === 'blue' ? 'text-blue-400' : item.color === 'violet' ? 'text-purple-400' : 'text-emerald-400']"></span>
                <strong class="text-xs text-white">{{ item.name }}</strong>
              </div>

              <div class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-black/40 border border-white/5 text-white/80 mb-2 inline-block">
                Step {{ item.step }}
              </div>

              <p class="text-[11px] text-white/70 m-0 leading-relaxed mb-2 break-keep">
                {{ item.desc }}
              </p>
            </div>

            <div class="pt-2 border-t border-white/10 text-[10px] font-mono whitespace-nowrap overflow-hidden text-ellipsis" :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'">
              ✓ {{ item.action }}
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Callout -->
    <div
      class="mt-3 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2.5">
            <span class="i-carbon:idea text-base text-cyan-400"></span>
            <span class="break-keep"><strong>단순 검색과의 차이:</strong> 단순 검색은 '링크 나열'에서 끝나지만, 심층 리서치는 <strong>'신뢰도 검증을 거친 종합 인사이트'</strong>를 완성합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold whitespace-nowrap">인사이트 완결</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
