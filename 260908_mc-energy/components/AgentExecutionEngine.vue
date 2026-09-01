<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

const loopNodes = [
  {
    step: '1',
    name: '목표 수신',
    eng: 'Goal Intake',
    icon: 'i-carbon:user-activity',
    desc: '"월별 매출 추이 분석해서 임원 보고서와 차트 만들어줘"',
    color: 'amber',
  },
  {
    step: '2',
    name: '상태 관찰',
    eng: 'Observe',
    icon: 'i-carbon:view',
    desc: '업로드된 파일 열기, 열(Column) 구조 및 결측치 파악',
    color: 'cyan',
  },
  {
    step: '3',
    name: '계획 수립',
    eng: 'Plan & Reason',
    icon: 'i-carbon:flow-stream',
    desc: '데이터 집계 ➔ 차트 생성 ➔ 보고서 작성 순서 결정',
    color: 'violet',
  },
  {
    step: '4',
    name: '도구 실행',
    eng: 'Act / Tool Call',
    icon: 'i-carbon:tools',
    desc: '@visualize 차트 생성 + @document 보고서 작성',
    color: 'blue',
  },
  {
    step: '5',
    name: '자체 검토',
    eng: 'Reflect & Eval',
    icon: 'i-carbon:rule-test',
    desc: '계산 오류 및 서식 누락 여부 자체 검증 및 수정',
    color: 'pink',
  },
  {
    step: '6',
    name: '산출물 완결',
    eng: 'Deliver',
    icon: 'i-carbon:document-export',
    desc: '최종 완성형 DOCX · XLSX · PNG 파일 링크 제공',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- SVG Connection Paths -->
    <div class="relative py-1">
      <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 900 210" fill="none">
        <path
          d="M 140 60 L 270 60 M 410 60 L 540 60 M 680 60 L 810 60"
          stroke="rgba(34, 211, 238, 0.4)"
          stroke-width="3"
          stroke-dasharray="6 4"
        />
        <path
          d="M 760 110 C 760 170, 140 170, 140 110"
          stroke="rgba(16, 185, 129, 0.3)"
          stroke-width="2.5"
          stroke-dasharray="8 4"
        />
      </svg>

      <!-- 6-Step Action Loop Grid -->
      <div class="grid grid-cols-6 gap-2.5 relative z-10">
        <div
          v-for="(node, idx) in loopNodes"
          :key="node.step"
          class="transition-all duration-500 transform"
          :class="[
            currentStage >= idx ? 'opacity-100 translate-y-0 scale-100' : 'opacity-25 translate-y-2 scale-95',
          ]"
        >
          <LiquidGlass
            :glow="node.color === 'amber' ? 'amber' : node.color === 'cyan' ? 'cyan' : node.color === 'violet' ? 'violet' : node.color === 'blue' ? 'blue' : node.color === 'pink' ? 'pink' : 'emerald'"
            :radius="12"
            class="h-full"
          >
            <div class="p-3 flex flex-col justify-between h-56">
              <div>
                <div class="flex items-center justify-between mb-2 pb-1 border-b border-white/10">
                  <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center font-mono text-[10px] font-bold text-white">
                    {{ node.step }}
                  </span>
                  <span :class="[node.icon, 'text-sm']"></span>
                </div>
                <div class="text-[11px] font-bold text-white mb-0.5">{{ node.name }}</div>
                <div class="text-[9px] font-mono text-white/50 mb-1.5">{{ node.eng }}</div>
                <p class="text-[10px] text-white/70 m-0 leading-tight">
                  {{ node.desc }}
                </p>
              </div>

              <div class="pt-1.5 border-t border-white/10 text-[9px] font-mono text-right" :class="node.color === 'emerald' ? 'text-emerald-300 font-bold' : 'text-white/40'">
                {{ node.color === 'emerald' ? '완결 산출물 ✓' : `Step 0${node.step}` }}
              </div>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>

    <!-- Bottom Architectural Takeaway -->
    <div
      class="mt-3.5 transition-all duration-500"
      :class="[currentStage >= 4 ? 'opacity-100 translate-y-0' : 'opacity-40 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-2.5 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2">
            <span class="i-carbon:cyclone text-cyan-400 text-base"></span>
            <span><strong>에이전트의 본질:</strong> 인간의 개입 없이 <strong>[관찰 ➔ 추론 ➔ 도구 호출 ➔ 검토]</strong> 루프를 백그라운드에서 자율 완결합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold">Autonomous Loop</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
