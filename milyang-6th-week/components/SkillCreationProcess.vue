<script setup lang="ts">
import { computed } from 'vue'
import { Wand2 } from 'lucide-vue-next'

const props = withDefaults(
  defineProps<{
    stage?: number
  }>(),
  {
    stage: 0
  }
)

const currentStage = computed(() => Number(props.stage ?? 0))

const steps = [
  {
    step: '01',
    title: '업무 하나 선택',
    sub: '대상 지정',
    desc: '일관된 양식과 품질이 필요한 반복·핵심 업무 1개를 고릅니다.'
  },
  {
    step: '02',
    title: '절차 지침 설명',
    sub: '지침 구조화',
    desc: '필수 5대 목차, 원자료 대조 규칙, 공문 톤앤매너를 정리합니다.'
  },
  {
    step: '03',
    title: '실제 요청 테스트',
    sub: '결과 검증',
    desc: '실제 로컬 파일(PDF/XLSX)을 투입해 완성형 문서를 확인합니다.'
  },
  {
    step: '04',
    title: '수정 및 재사용',
    sub: '영구 자산화',
    desc: '부족한 점을 보완하여 SKILL.md로 보관하고 매번 재사용합니다.'
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[320px] my-auto py-1">
    <!-- ── 4-Step Cards + Rough Hand-drawn Arrows ── -->
    <div class="flex items-stretch justify-between gap-1.5 h-[235px]">
      <template v-for="(s, idx) in steps" :key="s.step">
        <!-- ── Step Card ── -->
        <div
          class="flex-1 rounded-3xl p-4.5 flex flex-col justify-between transition-all duration-500 transform overflow-hidden"
          :class="[
            currentStage >= idx
              ? 'opacity-100 translate-y-0 scale-100 bg-white border-[1.5px] border-slate-300 shadow-2xs'
              : 'opacity-25 translate-y-3 scale-95 bg-slate-50/60 border-[1.5px] border-dashed border-slate-200 pointer-events-none'
          ]"
        >
          <!-- Top: Step Number + Subtitle Tag -->
          <div>
            <div class="flex items-center justify-between mb-3">
              <span
                class="w-7 h-7 rounded-xl font-mono font-bold text-xs flex items-center justify-center border transition-colors"
                :class="currentStage >= idx ? 'bg-blue-50 text-blue-600 border-blue-200 shadow-2xs' : 'bg-slate-100 text-slate-400 border-slate-200'"
              >
                {{ s.step }}
              </span>
              <span class="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">
                {{ s.sub }}
              </span>
            </div>

            <!-- Title (Clean Single-Line, No Ugly Wrapping) -->
            <h3 class="text-[14px] md:text-[14.5px] font-bold font-serif text-slate-900 leading-tight mb-2 whitespace-nowrap">
              {{ s.title }}
            </h3>

            <!-- Description (2 Lines Perfectly Balanced) -->
            <p class="text-[11.5px] text-slate-500 leading-relaxed break-keep">
              {{ s.desc }}
            </p>
          </div>

          <!-- Bottom Micro Status Bar (Clean inside card) -->
          <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[10px] font-mono font-bold">
            <span v-if="currentStage === idx" class="text-blue-600">
              ● 진행 단계
            </span>
            <span v-else-if="currentStage > idx" class="text-emerald-600">
              ✓ 준비 완료
            </span>
            <span v-else class="text-slate-300">
              대기
            </span>
          </div>
        </div>

        <!-- ── Rough Hand-drawn SVG Arrow Between Cards ── -->
        <div
          v-if="idx < steps.length - 1"
          class="flex items-center justify-center shrink-0 w-6 transition-all duration-500 transform"
          :class="currentStage >= idx + 1 ? 'opacity-100 scale-100' : 'opacity-15 scale-75'"
        >
          <svg class="w-6 h-6 overflow-visible" viewBox="0 0 24 24" fill="none">
            <!-- Rough hand-drawn wavy shaft -->
            <path
              d="M 2 12 Q 9 10.5, 17 12.5"
              stroke="#2563eb"
              stroke-width="2.6"
              stroke-linecap="round"
              class="rough-arrow-shaft"
            />
            <!-- Rough hand-drawn top head -->
            <path
              d="M 12.5 7.5 Q 16 9.8, 19.5 12"
              stroke="#2563eb"
              stroke-width="2.6"
              stroke-linecap="round"
              class="rough-arrow-head"
            />
            <!-- Rough hand-drawn bottom head -->
            <path
              d="M 12.5 16.5 Q 16 14.2, 19.5 12"
              stroke="#2563eb"
              stroke-width="2.6"
              stroke-linecap="round"
              class="rough-arrow-head"
            />
          </svg>
        </div>
      </template>
    </div>

    <!-- ── Integrated Micro Tip Bar ── -->
    <div class="flex items-center justify-between bg-slate-50 border border-slate-200 px-4 py-2 rounded-2xl text-xs text-slate-600">
      <div class="flex items-center gap-2">
        <Wand2 :size="14" class="text-blue-600 shrink-0" />
        <span>ChatGPT Work에서는 <code class="text-blue-600 font-bold bg-white px-1.5 py-0.5 rounded border border-blue-200 font-mono">@skill-creator</code>에게 대화하듯 요구사항을 말하면 스킬 지침이 자동 생성됩니다.</span>
      </div>
      <span class="text-[10.5px] font-mono text-slate-400 font-medium shrink-0 ml-3">
        4단계 표준 사이클
      </span>
    </div>
  </div>
</template>

<style scoped>
/* ── Rough Hand-drawn Arrow Stroke Drawing ── */
.rough-arrow-shaft {
  stroke-dasharray: 30;
  stroke-dashoffset: 0;
  animation: draw-shaft 0.4s ease-out both;
}

.rough-arrow-head {
  stroke-dasharray: 20;
  stroke-dashoffset: 0;
  animation: draw-head 0.4s ease-out 0.15s both;
}

@keyframes draw-shaft {
  from { stroke-dashoffset: 30; }
  to { stroke-dashoffset: 0; }
}

@keyframes draw-head {
  from { stroke-dashoffset: 20; }
  to { stroke-dashoffset: 0; }
}
</style>
