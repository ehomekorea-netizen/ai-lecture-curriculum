<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStep = computed(() => props.stage ?? 0)

const steps = [
  {
    id: 'retrieve',
    num: '1',
    title: '검색 (Retrieve)',
    desc: '사용자 질문과 관련된 사내 규정 및 데이터베이스 문서를 실시간으로 검색합니다.',
    tag: '관련 문서 추출',
    color: 'cyan',
  },
  {
    id: 'augment',
    num: '2',
    title: '증강 (Augment)',
    desc: '추출한 원본 텍스트를 AI 컨텍스트 윈도우에 주입해 오픈북 환경을 만듭니다.',
    tag: '컨텍스트 주입',
    color: 'blue',
  },
  {
    id: 'generate',
    num: '3',
    title: '생성 (Generate)',
    desc: '주입된 문서에만 근거하여 출처와 조항을 명시한 사실 기반 정답을 작성합니다.',
    tag: '근거 기반 정답 생성',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none py-1">
    <!-- Top Row: Closed-Book vs Open-Book Comparison -->
    <div class="grid grid-cols-12 gap-5 items-stretch mb-3">
      <!-- Left: Closed-Book -->
      <div class="col-span-5">
        <LiquidGlass glow="neutral" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-28">
            <div class="flex items-center gap-2 text-white/70 font-bold text-xs border-b border-white/10 pb-1.5">
              <span class="i-carbon:book text-sm"></span>
              <span>일반 LLM (클로즈드북)</span>
            </div>
            <p class="text-[11px] text-white/60 m-0 leading-relaxed">
              사전 학습된 기억에만 의존하므로 최신 정보나 사내 보안 정보 질문에 환각이 발생합니다.
            </p>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: Open-Book RAG -->
      <div class="col-span-7">
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-28">
            <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs border-b border-cyan-500/20 pb-1.5">
              <span class="i-carbon:catalog text-sm"></span>
              <span>RAG 시스템 (오픈북)</span>
            </div>
            <p class="text-[11px] text-white/80 m-0 leading-relaxed">
              사내 문서를 펼쳐놓고 <strong class="text-cyan-200">해당 페이지만 확인한 뒤 답변</strong>하므로 최신 규정과 데이터를 정확히 인용합니다.
            </p>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Center Stage: 3-Step RAG Pipeline with Flow Lines -->
    <div class="relative py-2">
      <div class="grid grid-cols-3 gap-5 relative z-10">
        <div
          v-for="(step, idx) in steps"
          :key="step.id"
          class="transition-all duration-500 transform"
          :class="[
            currentStep >= (idx + 1)
              ? 'opacity-100 translate-y-0 scale-100'
              : 'opacity-25 translate-y-2 scale-98',
          ]"
        >
          <LiquidGlass
            :glow="step.color === 'cyan' ? 'cyan' : step.color === 'blue' ? 'blue' : 'emerald'"
            :radius="16"
          >
            <div class="p-4 flex flex-col justify-between h-42">
              <div>
                <div class="flex items-center gap-2 mb-2 pb-1.5 border-b border-white/10">
                  <span
                    class="w-5 h-5 rounded-full flex items-center justify-center font-mono text-xs font-bold transition-colors duration-300"
                    :class="currentStep >= (idx + 1) ? (step.color === 'cyan' ? 'bg-cyan-500/30 text-cyan-300' : step.color === 'blue' ? 'bg-blue-500/30 text-blue-300' : 'bg-emerald-500/30 text-emerald-300') : 'bg-white/10 text-white/50'"
                  >
                    {{ step.num }}
                  </span>
                  <strong class="text-xs text-white">{{ step.title }}</strong>
                </div>
                <p class="text-[11px] text-white/75 m-0 leading-relaxed">
                  {{ step.desc }}
                </p>
              </div>

              <div class="pt-2 border-t border-white/10 flex items-center justify-between text-[10px] font-mono">
                <span class="text-white/40">Step 0{{ step.num }}</span>
                <span class="font-bold" :class="step.color === 'cyan' ? 'text-cyan-300' : step.color === 'blue' ? 'text-blue-300' : 'text-emerald-300'">
                  {{ step.tag }}
                </span>
              </div>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>

    <!-- Bottom Example -->
    <div
      class="mt-2 transition-all duration-500"
      :class="[currentStep >= 3 ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2 text-white/80">
            <span class="i-carbon:terminal text-cyan-400"></span>
            <span><strong>지시 예시:</strong> "사내 취업규칙 제15조를 참조하여, 3년 근속 직원의 연차 일수와 신청 절차를 답변하라."</span>
          </div>
          <span class="text-[10px] font-mono text-emerald-300 font-bold">오픈북 팩트 검증</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
