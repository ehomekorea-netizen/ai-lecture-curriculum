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
    subtitle: '사내 문서 · 벡터 DB 탐색',
    desc: '사용자 질문과 가장 유사한 고품질 사내 규정/DB 문서 청크(Chunk)를 실시간 검색 추출합니다.',
    tag: '사내 지식 추출',
    color: 'cyan',
  },
  {
    id: 'augment',
    num: '2',
    title: '증강 (Augment)',
    subtitle: '컨텍스트 윈도우 주입',
    desc: '추출된 원본 텍스트를 LLM의 프롬프트 컨텍스트(Context Window)에 직접 주입하여 오픈북 환경을 만듭니다.',
    tag: '오픈북 환경 구성',
    color: 'blue',
  },
  {
    id: 'generate',
    num: '3',
    title: '생성 (Generate)',
    subtitle: '근거 기반 답변 합성',
    desc: 'AI가 주입받은 근거 문서를 바탕으로 출처와 조항을 명시하며 왜곡 없는 사실 기반 정답을 생성합니다.',
    tag: '사실 기반 답변',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none">
    <!-- Top Row: Closed-Book vs Open-Book (RAG) Comparison -->
    <div class="grid grid-cols-12 gap-5 items-stretch mb-3.5">
      <!-- Left: Closed-Book (기존 LLM) -->
      <div class="col-span-5">
        <LiquidGlass glow="neutral" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
              <div class="flex items-center gap-2 text-white/70 font-bold text-xs">
                <span class="i-carbon:book text-sm"></span>
                <span>기존 LLM (Closed-Book 시험)</span>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-rose-500/20 text-rose-300">할루시네이션 위험</span>
            </div>
            <p class="text-[11px] text-white/60 m-0 leading-relaxed">
              자신의 기억력(사전학습 가중치)에만 의존하여 모르는 최신 정보나 사내 기밀 질문에도 그럴듯한 거짓말을 만들어낼 수 있습니다.
            </p>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: Open-Book RAG -->
      <div class="col-span-7">
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-3.5 px-4 flex flex-col justify-between h-30">
            <div class="flex items-center justify-between border-b border-cyan-500/20 pb-1.5">
              <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs">
                <span class="i-carbon:catalog text-sm"></span>
                <span>RAG 시스템 (Open-Book 시험)</span>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold">100% 사실 기반 무결성</span>
            </div>
            <p class="text-[11px] text-white/80 m-0 leading-relaxed">
              교과서(사내 DB/문서)를 펼쳐두고 <strong>해당 페이지를 실시간 확인한 뒤 답을 작성</strong>하므로 최신 정보와 사내 규정에 대한 100% 사실 기반 신뢰성을 보장합니다.
            </p>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Center Stage: 3-Step RAG Pipeline with Animated Pulse Stream -->
    <div class="relative py-2">
      <!-- SVG Connecting Lines -->
      <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 900 130" fill="none">
        <path
          d="M 285 65 L 335 65"
          stroke="rgba(34, 211, 238, 0.4)"
          stroke-width="3"
          stroke-dasharray="6 4"
        />
        <path
          d="M 585 65 L 635 65"
          stroke="rgba(16, 185, 129, 0.4)"
          stroke-width="3"
          stroke-dasharray="6 4"
        />
      </svg>

      <div class="grid grid-cols-3 gap-5 relative z-10">
        <div
          v-for="(step, idx) in steps"
          :key="step.id"
          class="transition-all duration-500 transform"
          :class="[
            currentStep >= idx ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2',
          ]"
        >
          <LiquidGlass
            :glow="step.color === 'cyan' ? 'cyan' : step.color === 'blue' ? 'blue' : 'emerald'"
            :radius="16"
          >
            <div class="p-4 flex flex-col justify-between h-46">
              <div>
                <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
                  <div class="flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center font-mono text-xs font-bold text-white">
                      {{ step.num }}
                    </span>
                    <strong class="text-xs text-white">{{ step.title }}</strong>
                  </div>
                  <span class="text-[10px] font-mono text-white/50">{{ step.subtitle }}</span>
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

    <!-- Bottom Flow Live Prompt Example -->
    <div
      class="mt-3 transition-all duration-500"
      :class="[currentStep >= 2 ? 'opacity-100 translate-y-0' : 'opacity-40 translate-y-1']"
    >
      <LiquidGlass glow="neutral" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2 text-white/80">
            <span class="i-carbon:terminal text-cyan-400"></span>
            <span><strong>실전 적용 예시:</strong> "사내 취업규칙 제15조를 참조하여, 3년 근속 직원의 연차 일수와 신청 절차를 답변하라."</span>
          </div>
          <span class="text-[10px] font-mono text-emerald-300 font-bold">오픈북 팩트 검증 완료</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
