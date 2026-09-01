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
    desc: '자연어 업무 목표 전달 및 요구조건 분석',
    color: 'amber',
  },
  {
    step: '2',
    name: '상태 관찰',
    eng: 'Observe',
    icon: 'i-carbon:view',
    desc: '첨부 파일 구조 확인, 열 파악 및 결측치 점검',
    color: 'cyan',
  },
  {
    step: '3',
    name: '계획 수립',
    eng: 'Plan & Reason',
    icon: 'i-carbon:flow-stream',
    desc: '분석 ➔ 시각화 ➔ 보고서 작성 순서 수립',
    color: 'violet',
  },
  {
    step: '4',
    name: '도구 실행',
    eng: 'Act / Tool Call',
    icon: 'i-carbon:tools',
    desc: '@visualize 및 @document 전문 도구 호출',
    color: 'blue',
  },
  {
    step: '5',
    name: '자체 검토',
    eng: 'Reflect & Eval',
    icon: 'i-carbon:rule-test',
    desc: '계산 오차 및 서식 누락 여부 자체 검증',
    color: 'pink',
  },
  {
    step: '6',
    name: '산출물 완결',
    eng: 'Deliver',
    icon: 'i-carbon:document-export',
    desc: '최종 완성형 DOCX · XLSX 파일 생성 완료',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Clean 6-Step Autonomous Flow Cards (No Messy Background Lines) -->
    <div class="grid grid-cols-6 gap-3 items-stretch my-2">
      <div
        v-for="(node, idx) in loopNodes"
        :key="node.step"
        class="transition-all duration-500 transform flex flex-col"
        :class="[
          currentStage >= idx ? 'opacity-100 translate-y-0 scale-100' : 'opacity-25 translate-y-2 scale-98',
        ]"
      >
        <LiquidGlass
          :glow="node.color === 'amber' ? 'amber' : node.color === 'cyan' ? 'cyan' : node.color === 'violet' ? 'violet' : node.color === 'blue' ? 'blue' : node.color === 'pink' ? 'pink' : 'emerald'"
          :radius="14"
          class="h-full"
        >
          <div class="p-3.5 flex flex-col justify-between h-58">
            <div>
              <!-- Step Header -->
              <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
                <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center font-mono text-[10px] font-bold text-white">
                  {{ node.step }}
                </span>
                <span :class="[node.icon, 'text-base', node.color === 'amber' ? 'text-amber-400' : node.color === 'cyan' ? 'text-cyan-400' : node.color === 'violet' ? 'text-purple-400' : node.color === 'blue' ? 'text-blue-400' : node.color === 'pink' ? 'text-pink-400' : 'text-emerald-400']"></span>
              </div>

              <!-- Name & English -->
              <div class="text-xs font-bold text-white mb-0.5">{{ node.name }}</div>
              <div class="text-[9px] font-mono text-white/50 mb-2">{{ node.eng }}</div>

              <!-- Description -->
              <p class="text-[10.5px] text-white/75 m-0 leading-relaxed">
                {{ node.desc }}
              </p>
            </div>

            <!-- Footer Badge -->
            <div
              class="pt-2 border-t border-white/10 text-[9px] font-mono flex items-center justify-between"
              :class="node.color === 'emerald' ? 'text-emerald-300 font-bold' : 'text-white/40'"
            >
              <span>Step 0{{ node.step }}</span>
              <span>{{ node.color === 'emerald' ? '완결' : '진행' }}</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Architectural Takeaway -->
    <div
      class="mt-3 transition-all duration-500"
      :class="[currentStage >= 4 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2.5">
            <span class="i-carbon:cyclone text-cyan-400 text-base"></span>
            <span><strong>에이전트의 본질:</strong> 인간의 개입 없이 <strong>[관찰 ➔ 추론 ➔ 도구 호출 ➔ 검토]</strong> 루프를 백그라운드에서 자율 완결합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold">Autonomous Loop</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
