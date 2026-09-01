<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

const pillars = [
  {
    letter: 'R',
    name: 'Role',
    kr: '역할 정의',
    example: '"너는 10년 차 에너지 정책 및 전력 수급 분석가다."',
    desc: '답변의 전문 지식 도메인과 톤앤매너를 지정합니다.',
    color: 'cyan',
  },
  {
    letter: 'C',
    name: 'Context',
    kr: '배경·맥락',
    example: '"MC에너지 임원진 주간 경영회의 보고용 자료를 작성 중이다."',
    desc: '보고 대상(청중)과 업무 목적을 제시합니다.',
    color: 'blue',
  },
  {
    letter: 'T',
    name: 'Task',
    kr: '핵심 과업',
    example: '"전력시장 SMP 가격 변동 원인을 3가지로 분석하고 대응안을 제시하라."',
    desc: '구체적인 동사로 실행할 업무를 명시합니다.',
    color: 'violet',
  },
  {
    letter: 'F',
    name: 'Format',
    kr: '출력 서식',
    example: '"A4 1페이지 분량, 결론 요약 후 항목별 비교표로 작성하라."',
    desc: '분량, 서식, 제외 조건 등 출력 규격을 통제합니다.',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top 4 Pillars Grid -->
    <div class="grid grid-cols-4 gap-4 items-stretch">
      <div
        v-for="(item, idx) in pillars"
        :key="item.letter"
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
          <div class="p-4 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-2.5">
                <div class="text-2xl font-mono font-black" :class="item.color === 'cyan' ? 'text-cyan-400' : item.color === 'blue' ? 'text-blue-400' : item.color === 'violet' ? 'text-purple-400' : 'text-emerald-400'">
                  {{ item.letter }}
                </div>
                <div class="text-right">
                  <div class="text-xs font-bold text-white">{{ item.name }}</div>
                  <div class="text-[10px] font-mono text-white/50">{{ item.kr }}</div>
                </div>
              </div>

              <div class="p-2.5 rounded-lg bg-black/40 border border-white/5 font-mono text-[11px] text-white/90 leading-relaxed mb-2.5">
                {{ item.example }}
              </div>

              <p class="text-[11px] text-white/70 m-0 leading-relaxed">
                {{ item.desc }}
              </p>
            </div>

            <div class="pt-2 border-t border-white/10 text-[10px] font-mono text-white/40 flex items-center justify-between">
              <span>Pillar 0{{ idx + 1 }}</span>
              <span class="font-bold text-white/70">{{ item.kr }}</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Master Formula -->
    <div
      class="mt-3.5 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2.5">
            <span class="i-carbon:formula text-cyan-400 text-base"></span>
            <span class="text-white/80"><strong>[Role]</strong>(전문가) + <strong>[Context]</strong>(사내 배경) + <strong>[Task]</strong>(구체적 동사) + <strong>[Format]</strong>(엄격한 서식 제약)</span>
          </div>
          <span class="text-[11px] font-mono text-emerald-300 font-bold">= 실무 즉시 채택 산출물</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
