<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

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
        class="transition-all duration-500 transform"
        :class="[
          currentStage >= 0 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1',
        ]"
      >
        <LiquidGlass
          :glow="elem.color === 'cyan' ? 'cyan' : elem.color === 'blue' ? 'blue' : elem.color === 'violet' ? 'violet' : 'emerald'"
          :radius="12"
          class="h-full"
        >
          <div class="p-3 flex flex-col justify-between h-42">
            <div>
              <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-white/10">
                <span class="text-xs font-bold text-white">{{ elem.num }} {{ elem.name }}</span>
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-white/10 text-white/60">필수</span>
              </div>
              <div class="text-[10px] text-white/70 mb-1.5 leading-snug">{{ elem.desc }}</div>
              <div class="p-1.5 rounded bg-black/40 border border-white/5 font-mono text-[9px] text-white/90">
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
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="pink" :radius="14" class="h-full">
          <div class="p-3.5 flex flex-col justify-between h-40">
            <div>
              <div class="flex items-center justify-between border-b border-rose-500/20 pb-1 mb-1.5">
                <span class="text-xs font-bold text-rose-300">초기 지침 (개선 전)</span>
                <span class="text-[9px] font-mono text-rose-400">1차 실행</span>
              </div>
              <div class="p-2 rounded bg-black/40 font-mono text-[10px] text-rose-200 mb-1.5 border border-rose-500/20">
                "매주 팀 업무보고서를 작성해줘."
              </div>
              <p class="text-[10px] text-white/60 m-0 leading-tight">
                <strong>문제점:</strong> 장황한 줄글, 사소한 잡무 나열로 임원 보고 불가
              </p>
            </div>
            <div class="text-[9px] font-mono text-rose-400/70 pt-1">지침 수정 필요</div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: After (4단 고정 규격 스킬) -->
      <div
        class="col-span-7 transition-all duration-500 transform"
        :class="[currentStage >= 2 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="emerald" :radius="14" class="h-full">
          <div class="p-3.5 flex flex-col justify-between h-40">
            <div>
              <div class="flex items-center justify-between border-b border-emerald-500/20 pb-1 mb-1.5">
                <span class="text-xs font-bold text-emerald-300">개선된 스킬 지침 (4단 고정 표준화)</span>
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">영구 자산</span>
              </div>
              <div class="p-2 rounded bg-black/40 font-mono text-[10px] text-emerald-100 leading-snug border border-emerald-500/20">
                "반드시 4단 구조(①핵심 성과 ②주요 완료 ③발생 문제·대응 ④차주 계획)로 작성하고 항목당 글머리 기호 3개 이내로 제한할 것."
              </div>
            </div>
            <div class="text-[10px] font-mono text-emerald-300 font-bold pt-1">
              ✓ 팀원 누구나 원클릭 실행 시 동일한 최고 품질 보장
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
