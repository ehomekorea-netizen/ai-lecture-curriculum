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

const skillElements = [
  {
    num: '①',
    name: '목적 (Goal)',
    desc: '해결하려는 업무 목표 정의',
    example: '"매주 팀 주간업무보고서 표준화"',
    color: 'cyan',
  },
  {
    num: '②',
    name: '입력 자료 (Inputs)',
    desc: '주입받을 필수 파일/데이터 지정',
    example: '팀원별 원시 주간 메모 · 실적 데이터',
    color: 'blue',
  },
  {
    num: '③',
    name: '작업 절차 (Workflow)',
    desc: '1~4단계 순차 실행 지침',
    example: '데이터 수집 ➔ 분류 ➔ 요약 ➔ 검토',
    color: 'violet',
  },
  {
    num: '④',
    name: '결과물 기준 (Rubric)',
    desc: '서식 구조 및 분량 제약',
    example: '4단 고정 서식, 항목당 3개 이내',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top Row: 4 Core Elements -->
    <div class="grid grid-cols-4 gap-3.5 items-stretch mb-3">
      <div
        v-for="elem in skillElements"
        :key="elem.name"
        class="transition-all duration-500 transform opacity-100 translate-y-0"
      >
        <LiquidGlass
          :glow="elem.color === 'cyan' ? 'cyan' : elem.color === 'blue' ? 'blue' : elem.color === 'violet' ? 'violet' : 'emerald'"
          :radius="12"
          class="h-full"
        >
          <div class="p-3.5 flex flex-col justify-between h-42">
            <div>
              <div class="flex items-center gap-1.5 mb-2 pb-1.5 border-b border-white/10 text-xs font-bold text-white">
                <span>{{ elem.num }} {{ elem.name }}</span>
              </div>
              <div class="text-[11px] text-white/70 mb-2 leading-snug">{{ elem.desc }}</div>
              <div class="p-2 rounded bg-black/40 border border-white/5 font-mono text-[10px] text-white/90">
                {{ elem.example }}
              </div>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Center/Bottom: Refinement Case Study (Before vs After) -->
    <div class="grid grid-cols-12 gap-4 items-stretch">
      <!-- Left: Before (막연한 1회성 프롬프트) -->
      <div
        class="col-span-5 transition-all duration-500 transform"
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="currentStage >= 1 ? 'pink' : 'neutral'" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-40">
            <div>
              <div class="flex items-center gap-1.5 border-b border-rose-500/20 pb-1.5 mb-2 text-xs font-bold text-rose-300">
                <span class="i-carbon:close-outline text-sm"></span>
                <span>초기 지침 (개선 전)</span>
              </div>
              <div class="p-2.5 rounded bg-black/40 font-mono text-[11px] text-rose-200 mb-1.5 border border-rose-500/20">
                "매주 팀 업무보고서를 작성해줘."
              </div>
              <p class="text-[11px] text-white/70 m-0 leading-tight">
                장황한 줄글, 사소한 잡무 나열로 임원 보고 불가
              </p>
            </div>
            <div class="text-[10px] font-mono text-rose-400/80 pt-1 border-t border-white/10">1차 실행 문제점</div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: After (4단 고정 규격 스킬) -->
      <div
        class="col-span-7 transition-all duration-500 transform"
        :class="[currentStage >= 2 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="currentStage >= 2 ? 'emerald' : 'neutral'" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-40">
            <div>
              <div class="flex items-center gap-1.5 border-b border-emerald-500/20 pb-1.5 mb-2 text-xs font-bold text-emerald-300">
                <span class="i-carbon:checkmark-outline text-sm"></span>
                <span>개선된 스킬 지침 (4단 고정 표준화)</span>
              </div>
              <div class="p-2.5 rounded bg-black/40 font-mono text-[11px] text-emerald-100 leading-snug border border-emerald-500/20">
                "반드시 4단 구조(①성과 ②완료 ③이슈 ④계획)로 작성하고 항목당 글머리 3개로 제한할 것."
              </div>
            </div>
            <div class="text-[10px] font-mono text-emerald-300 font-bold pt-1 border-t border-white/10">
              ✓ 팀원 누구나 원클릭 실행 시 동일한 최고 품질 보장
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
