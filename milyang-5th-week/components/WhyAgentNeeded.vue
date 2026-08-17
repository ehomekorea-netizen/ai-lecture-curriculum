<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const props = defineProps<{
  stage?: number
}>()

// Stage mapping:
// stage 0 -> 0 cards revealed (all 3 slots clean & empty)
// stage 1 -> Card 1 revealed
// stage 2 -> Card 1, 2 revealed
// stage 3 -> Card 1, 2, 3 all revealed
const revealedCount = computed(() => {
  if (props.stage === undefined || props.stage === null || props.stage <= 0) return 0
  return Math.min(3, Math.max(0, props.stage))
})

const activeCard = ref(0)

// Automatically focus on the newly revealed card
watch(
  revealedCount,
  (val) => {
    if (val > 0) {
      activeCard.value = val - 1
    } else {
      activeCard.value = 0
    }
  },
  { immediate: true }
)

function selectStep(idx: number) {
  if (idx < revealedCount.value) {
    activeCard.value = idx
  }
}

const points = [
  {
    num: '01',
    shortName: '01. 심층 탐색 & 사내 연동',
    title: '심층 다단계 탐색 & 사내 시스템 연동',
    tag: 'Multi-Hop Research & APIs',
    icon: '🌐',
    cardActive: 'border-2 border-blue-500 ring-3 ring-blue-500/20 shadow-xl scale-[1.01] -translate-y-0.5',
    btnActive: 'bg-blue-600 text-white border-blue-600 shadow-xs',
    llmTitle: '단순 LLM / 챗봇 검색',
    llmText: '1회성 키워드 웹 검색에 그치며, 사내 비공개 DB나 로컬 파일시스템에 직접 접근해 수정 불가',
    agentTitle: 'AI Agent의 심층 탐색 & 조작',
    agentText: '원하는 정보가 나올 때까지 검색어를 스스로 바꿔가며 심층 탐색 + 사내 DB/API/파일 직접 가공',
    coreDifferentiator: '다단계 자율 탐색 & 사내 비공개 연동'
  },
  {
    num: '02',
    shortName: '02. 과업 자동 분해 & 연속 실행',
    title: '다단계 과업 분해 & 자율 연속 실행',
    tag: 'Task Decomposition & Planning',
    icon: '🧩',
    cardActive: 'border-2 border-amber-500 ring-3 ring-amber-500/20 shadow-xl scale-[1.01] -translate-y-0.5',
    btnActive: 'bg-amber-500 text-white border-amber-500 shadow-xs',
    llmTitle: '단순 LLM / 챗봇 방식',
    llmText: '1번 묻고 1번 답하면 종료. 복잡한 다단계 업무는 중간에 끊기며 사람이 다음 지시를 내려야 함',
    agentTitle: 'AI Agent의 자율 분해',
    agentText: '최종 목표를 4~5개 세부 과업으로 스스로 분해하여, 사람 개입 없이 처음부터 끝까지 연속 완결',
    coreDifferentiator: '목표의 하위 과업 분해 & 무중단 완결'
  },
  {
    num: '03',
    shortName: '03. 실제 디지털 환경 직접 제어',
    title: '실제 디지털 환경 및 컴퓨터 직접 제어',
    tag: 'Computer & Tool Action Execution',
    icon: '💻',
    cardActive: 'border-2 border-emerald-500 ring-3 ring-emerald-500/20 shadow-xl scale-[1.01] -translate-y-0.5',
    btnActive: 'bg-emerald-600 text-white border-emerald-600 shadow-xs',
    llmTitle: '단순 LLM / 챗봇 방식',
    llmText: '화면에 텍스트나 코드 조각을 제안하는 출력에만 머무름 (사람이 복사하여 파일 만들고 실행)',
    agentTitle: 'AI Agent의 실제 조작',
    agentText: '코드 파일 직접 생성/저장, 터미널 명령어 실행, 브라우저 클릭 및 배포까지 알아서 완결',
    coreDifferentiator: '파일 생성 · 터미널 구동 · 브라우저 제어'
  }
]
</script>

<template>
  <div class="why-agent w-full">
    <!-- Top 3-Step Clickable Stepper Bar -->
    <div class="flex items-center justify-between gap-2 p-1 bg-slate-100/90 rounded-lg border border-slate-200 mb-2">
      <button
        v-for="(p, idx) in points"
        :key="p.num"
        class="flex-1 py-1 px-2 rounded-md text-[11px] font-bold transition-all flex items-center justify-center gap-1.5 border truncate"
        :class="[
          idx >= revealedCount
            ? 'opacity-40 bg-slate-50 text-slate-400 border-transparent cursor-default'
            : activeCard === idx
              ? `${p.btnActive} cursor-pointer`
              : 'bg-transparent text-slate-600 border-transparent hover:text-slate-900 hover:bg-slate-200/50 cursor-pointer'
        ]"
        @click="selectStep(idx)"
      >
        <span>{{ p.shortName }}</span>
        <span class="text-xs">{{ idx >= revealedCount ? '·' : p.icon }}</span>
      </button>
    </div>

    <!-- 3 Core Limitation Cards Grid (Pure Empty Slots with Zero Layout Shift) -->
    <div class="grid grid-cols-3 gap-2.5 items-stretch min-h-[295px]">
      <div
        v-for="(p, idx) in points"
        :key="p.num"
        class="p-2.5 rounded-xl border transition-all duration-300 flex flex-col justify-between"
        :class="[
          idx < revealedCount
            ? `revealed-card bg-white cursor-pointer ${
                activeCard === idx
                  ? `${p.cardActive} z-10 opacity-100`
                  : 'border-slate-200 bg-slate-50/70 opacity-60 grayscale-[20%] hover:opacity-90'
              }`
            : 'invisible opacity-0 pointer-events-none select-none border-transparent'
        ]"
        @click="selectStep(idx)"
      >
        <div>
          <!-- Header Pill & Icon -->
          <div class="flex items-center justify-between mb-1">
            <span class="px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 text-[9.5px] font-bold font-mono border border-slate-200">
              POINT {{ p.num }}
            </span>
            <span class="text-sm">{{ p.icon }}</span>
          </div>

          <!-- Title Area -->
          <div class="mb-1.5">
            <h3 class="text-[11.5px] font-bold text-slate-900 leading-snug opacity-100 m-0">
              {{ p.title }}
            </h3>
            <p class="text-[9.5px] font-mono text-blue-600 font-semibold m-0 mt-0.5 leading-tight">
              {{ p.tag }}
            </p>
          </div>

          <!-- Comparison Blocks -->
          <div class="space-y-1.5">
            <!-- LLM Box -->
            <div class="p-1.5 rounded-lg bg-red-50/70 border border-red-100 text-[10px]">
              <div class="font-bold text-red-700 mb-0.5 flex items-center gap-1 text-[10px]">
                <span>❌</span>
                <span>{{ p.llmTitle }}</span>
              </div>
              <p class="text-slate-600 leading-tight m-0 text-[10px]">
                {{ p.llmText }}
              </p>
            </div>

            <!-- Agent Box -->
            <div class="p-1.5 rounded-lg bg-emerald-50/80 border border-emerald-200 text-[10px]">
              <div class="font-bold text-emerald-800 mb-0.5 flex items-center gap-1 text-[10px]">
                <span>✨</span>
                <span>{{ p.agentTitle }}</span>
              </div>
              <p class="text-emerald-950 font-medium leading-tight m-0 text-[10px]">
                {{ p.agentText }}
              </p>
            </div>
          </div>
        </div>

        <!-- Footer Tag -->
        <div class="mt-2 pt-1 border-t border-slate-100 flex items-center justify-between text-[9.5px]">
          <span class="text-slate-400 font-medium">차별화 핵심</span>
          <b class="text-emerald-700 font-bold text-[10px]">{{ p.coreDifferentiator }}</b>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Dynamic Banner -->
    <div class="mt-2 py-1.5 px-2.5 rounded-lg bg-slate-900 text-white shadow-xs flex items-center justify-between border border-slate-800">
      <div v-if="revealedCount > 0" class="flex items-center gap-1.5 text-[11px]">
        <span class="px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-400 font-mono text-[9.5px] font-bold">
          POINT {{ points[activeCard].num }}
        </span>
        <span class="text-slate-200 text-[11px]">
          <b class="text-amber-300">{{ points[activeCard].title }}</b>: {{ points[activeCard].coreDifferentiator }}
        </span>
      </div>
      <div v-else class="flex items-center gap-1.5 text-[11px] text-slate-300">
        <span class="px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono text-[9.5px] font-bold">START</span>
        <span>스페이스바나 화면을 클릭하여 단일 LLM의 3대 한계와 AI Agent의 해결책을 확인하세요.</span>
      </div>

      <div class="flex-shrink-0 text-[9.5px] text-emerald-400 font-mono font-bold bg-white/10 px-1.5 py-0.5 rounded">
        {{ revealedCount }} / 3 (스페이스로 다음 카드 오픈)
      </div>
    </div>
  </div>
</template>

<style scoped>
.revealed-card {
  animation: cardAppear 0.28s cubic-bezier(0.2, 1.2, 0.4, 1) both;
}

@keyframes cardAppear {
  from {
    opacity: 0;
    transform: translateY(8px) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>
