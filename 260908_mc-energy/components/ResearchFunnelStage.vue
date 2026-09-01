<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

const steps = [
  {
    step: '01',
    name: '질문 구체화',
    eng: 'Clarify',
    icon: 'i-carbon:help',
    desc: '검색 목적, 핵심 키워드, 최신 타깃 시점(2026년)을 명확히 정의',
    action: '모호한 키워드 ➔ 세부 타깃 쿼리 변환',
    color: 'cyan',
  },
  {
    step: '02',
    name: '다중 소스 수집',
    eng: 'Collect',
    icon: 'i-carbon:data-volume',
    desc: '공공 통계, 학술 보고서, 전문 뉴스, 사내 DB 등 다각도 자료 확보',
    action: '단일 검색결과 의존 탈피',
    color: 'blue',
  },
  {
    step: '03',
    name: '교차 검증',
    eng: 'Verify',
    icon: 'i-carbon:rule-test',
    desc: '서로 다른 출처 간 상충되는 수치와 발행 시점 대조 검증',
    action: '오차 및 할루시네이션 원천 차단',
    color: 'violet',
  },
  {
    step: '04',
    name: '종합 보고서화',
    eng: 'Synthesize',
    icon: 'i-carbon:document-sentiment',
    desc: '3줄 핵심 결론, 비교 분석표, 실무 시사점 및 액션플랜 도출',
    action: '의사결정용 1페이지 완성',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- SVG Stream Connector -->
    <div class="relative py-2">
      <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 900 180" fill="none">
        <path
          d="M 215 90 L 255 90 M 440 90 L 480 90 M 665 90 L 705 90"
          stroke="rgba(34, 211, 238, 0.4)"
          stroke-width="3"
          stroke-dasharray="6 4"
        />
      </svg>

      <div class="grid grid-cols-4 gap-4 relative z-10">
        <div
          v-for="(item, idx) in steps"
          :key="item.step"
          class="transition-all duration-500 transform"
          :class="[
            currentStage >= idx ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2',
          ]"
        >
          <LiquidGlass
            :glow="item.color === 'cyan' ? 'cyan' : item.color === 'blue' ? 'blue' : item.color === 'violet' ? 'violet' : 'emerald'"
            :radius="14"
            class="h-full"
          >
            <div class="p-4 flex flex-col justify-between h-70">
              <div>
                <div class="flex items-center justify-between mb-2.5 pb-2 border-b border-white/10">
                  <div class="flex items-center gap-1.5">
                    <span :class="[item.icon, 'text-base', item.color === 'cyan' ? 'text-cyan-400' : item.color === 'blue' ? 'text-blue-400' : item.color === 'violet' ? 'text-purple-400' : 'text-emerald-400']"></span>
                    <strong class="text-xs text-white">{{ item.name }}</strong>
                  </div>
                  <span class="text-[10px] font-mono text-white/50">{{ item.eng }}</span>
                </div>

                <div class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-black/40 border border-white/5 text-white/80 mb-2">
                  Step {{ item.step }}
                </div>

                <p class="text-[11px] text-white/70 m-0 leading-relaxed mb-2">
                  {{ item.desc }}
                </p>
              </div>

              <div class="pt-2 border-t border-white/10 text-[10px] font-mono" :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'">
                ✓ {{ item.action }}
              </div>
            </div>
          </LiquidGlass>
        </div>
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
            <span><strong>단순 검색과의 차이:</strong> 단순 검색은 '링크 나열'에서 끝나지만, 심층 리서치는 <strong>'신뢰도 검증을 거친 종합 인사이트'</strong>를 완성합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold">인사이트 완결</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
