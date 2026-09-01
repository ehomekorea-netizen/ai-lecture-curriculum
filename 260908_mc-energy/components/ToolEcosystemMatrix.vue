<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

const toolRows = [
  {
    icon: 'i-carbon:table',
    task: '엑셀 데이터 분석 · 수치 집계',
    tool: 'Spreadsheet (Python Code)',
    output: '증감률 계산 + 이상치 원인 표',
    format: 'XLSX 파일',
    color: 'emerald',
  },
  {
    icon: 'i-carbon:chart-line-data',
    task: '추이 시각화 · 프로세스 흐름',
    tool: '@visualize 플러그인',
    output: '인터랙티브 꺾은선/막대 차트',
    format: 'HTML/PNG 차트',
    color: 'amber',
  },
  {
    icon: 'i-carbon:document',
    task: '임원 보고서 · 기획서 작성',
    tool: '@document 플러그인',
    output: '서식과 개조식이 완비된 1페이지',
    format: 'DOCX 문서',
    color: 'blue',
  },
  {
    icon: 'i-carbon:skill-level',
    task: '매주 반복되는 정형 보고서',
    tool: 'OpenAI Skill 패키지',
    output: '팀 공통 4단 표준 템플릿 완성',
    format: '조직 영구 자산',
    color: 'violet',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Tool Matrix Grid -->
    <div class="grid grid-cols-4 gap-4 items-stretch mb-3">
      <div
        v-for="(row, idx) in toolRows"
        :key="row.task"
        class="transition-all duration-500 transform"
        :class="[
          currentStage >= idx ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2',
        ]"
      >
        <LiquidGlass
          :glow="row.color === 'emerald' ? 'emerald' : row.color === 'amber' ? 'amber' : row.color === 'blue' ? 'blue' : 'violet'"
          :radius="14"
          class="h-full"
        >
          <div class="p-4 flex flex-col justify-between h-68">
            <div>
              <div class="flex items-center justify-between mb-2.5 pb-2 border-b border-white/10">
                <span :class="[row.icon, 'text-xl', row.color === 'emerald' ? 'text-emerald-400' : row.color === 'amber' ? 'text-amber-400' : row.color === 'blue' ? 'text-blue-400' : 'text-purple-400']"></span>
                <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-white/10 text-white/70">{{ row.format }}</span>
              </div>

              <div class="text-[10px] font-mono text-white/50 uppercase font-bold mb-1">업무 목적</div>
              <div class="text-xs font-bold text-white mb-2 leading-snug">{{ row.task }}</div>

              <div class="p-2 rounded bg-black/40 border border-white/5 mb-2">
                <div class="text-[9px] font-mono text-white/40">호출 도구</div>
                <div class="text-[11px] font-mono font-bold" :class="row.color === 'emerald' ? 'text-emerald-300' : row.color === 'amber' ? 'text-amber-300' : row.color === 'blue' ? 'text-blue-300' : 'text-purple-300'">
                  {{ row.tool }}
                </div>
              </div>
            </div>

            <div class="pt-2 border-t border-white/10 text-[10px] text-white/70 leading-tight">
              <strong>결과물:</strong> {{ row.output }}
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Selection Rule -->
    <div
      class="mt-1 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-40 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2">
            <span class="i-carbon:flash text-cyan-400 text-base"></span>
            <span><strong>도구 선택의 핵심 원칙:</strong> 질문에 맞는 도구를 사람이 고민하지 않고, <strong>자연어 명령 한마디로 AI가 최적의 도구를 자율 매칭</strong>합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold">Smart Dispatching</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
