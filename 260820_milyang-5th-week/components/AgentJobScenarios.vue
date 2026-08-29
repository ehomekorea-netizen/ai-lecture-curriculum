<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const props = defineProps<{
  stage?: number
}>()

// Track flipped state for each of the 3 cards
const flippedCards = ref<boolean[]>([false, false, false])

// Sync with Slidev $clicks if stage is passed
watch(
  () => props.stage,
  (val) => {
    if (val === undefined || val === null || val <= 0) {
      flippedCards.value = [false, false, false]
    } else if (val === 1) {
      flippedCards.value = [true, false, false]
    } else if (val === 2) {
      flippedCards.value = [true, true, false]
    } else if (val >= 3) {
      flippedCards.value = [true, true, true]
    }
  },
  { immediate: true }
)

function toggleCard(idx: number) {
  flippedCards.value[idx] = !flippedCards.value[idx]
}

function flipAll(state: boolean) {
  flippedCards.value = [state, state, state]
}

const allFlipped = computed(() => flippedCards.value.every(v => v))

const jobs = [
  {
    icon: '💻',
    title: '개발 / 기술 직무',
    role: 'Software & Web',
    color: 'blue',
    themeClass: 'from-blue-50/50 to-white border-blue-500 ring-2 ring-blue-500/20',
    beforeTitle: '수작업 코딩 & 수동 디버깅',
    beforeDesc: '개발자가 기획서를 보고 한 줄씩 코드를 직접 타이핑하고, 콘솔 에러가 나면 구글링하며 수동으로 디버깅합니다.',
    beforePill: '⚠️ 단순 반복 코딩에 시간의 70% 소모',
    afterTitle: '명세 전달 ➔ 자율 코딩 & 테스트',
    afterDesc: 'Agent에게 기능 명세와 요구사항을 자연어로 전달하면, <b>코드 작성부터 단위 테스트, 에러 자가 수정까지 자율 완수</b>합니다.',
    afterPill: '✨ 개발자는 핵심 비즈니스 로직 설계에만 집중'
  },
  {
    icon: '📊',
    title: '마케팅 / 기획 직무',
    role: 'Growth & Planning',
    color: 'amber',
    themeClass: 'from-amber-50/50 to-white border-amber-500 ring-2 ring-amber-500/20',
    beforeTitle: '툴 파편화 & 수동 취합',
    beforeDesc: '트렌드 조사 ➔ 카피 작성 ➔ 이미지 제작을 각각 다른 웹사이트와 툴에서 사람이 하나하나 복사·붙여넣기하며 취합합니다.',
    beforePill: '⚠️ 여러 툴을 오가며 파편화된 수작업',
    afterTitle: '캠페인 기획 단일 워크플로우',
    afterDesc: '"신제품 마케팅 캠페인 기획해줘" 프롬프트 1번에 <b>실시간 자료 수집, 카피 시안 작성, 이미지 생성까지 한 번에 완료</b>합니다.',
    afterPill: '✨ 기획자는 전략적 타겟팅과 메시지 톤 검수에 집중'
  },
  {
    icon: '👥',
    title: 'HR / 경영지원 직무',
    role: 'People & Operations',
    color: 'emerald',
    themeClass: 'from-emerald-50/50 to-white border-emerald-500 ring-2 ring-emerald-500/20',
    beforeTitle: '서류 수동 검토 & 메일 조율',
    beforeDesc: '수백 건의 이력서를 일일이 눈으로 검토하고, 면접관과 지원자 사이에서 수십 통의 이메일을 주고받으며 일정을 조율합니다.',
    beforePill: '⚠️ 단순 일정 조율과 필터링에 극심한 시간 소모',
    afterTitle: '자동 스크리닝 & 캘린더 연동',
    afterDesc: '이력서 조건별 자동 스크리닝 & <b>지원자의 캘린더 및 이메일과 직접 연동하여 최적 면접 일정을 자동 확정</b>합니다.',
    afterPill: '✨ 인사팀은 심층 면접 질문과 지원자 경험 관리에 집중'
  }
]
</script>

<template>
  <div class="job-scenarios w-full mt-2">
    <!-- 3D Flip Card Grid -->
    <div class="grid grid-cols-3 gap-3.5 items-stretch h-[310px]">
      <div
        v-for="(j, idx) in jobs"
        :key="j.title"
        class="flip-card-container h-full cursor-pointer select-none"
        @click="toggleCard(idx)"
      >
        <div class="flip-card-inner h-full" :class="{ 'is-flipped': flippedCards[idx] }">
          
          <!-- ── 1. FRONT FACE (Before) ── -->
          <div class="flip-card-front p-3.5 bg-white rounded-2xl border border-red-200/80 shadow-sm flex flex-col justify-between hover:border-red-400 transition-colors">
            <div>
              <!-- Header -->
              <div class="flex items-center justify-between mb-2">
                <div class="flex items-center gap-1.5">
                  <span class="text-base">{{ j.icon }}</span>
                  <h3 class="text-sm font-bold text-slate-900 m-0 opacity-100">{{ j.title }}</h3>
                </div>
                <span class="px-2 py-0.5 rounded bg-red-100 text-red-700 text-[10px] font-bold font-mono border border-red-200">
                  ❌ BEFORE
                </span>
              </div>

              <!-- Subtitle -->
              <h4 class="text-xs font-bold text-red-700 mb-1.5">
                {{ j.beforeTitle }}
              </h4>

              <!-- Body Description -->
              <p class="text-[11px] text-slate-600 leading-snug m-0">
                {{ j.beforeDesc }}
              </p>
            </div>

            <!-- Bottom Painpoint Pill & Flip Hint -->
            <div>
              <div class="p-1.5 rounded-lg bg-red-50 border border-red-100 text-[10px] text-red-700 font-medium mb-2">
                {{ j.beforePill }}
              </div>
              <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-400">
                <span>클릭하여 After 확인</span>
                <span class="font-bold text-blue-600 flex items-center gap-0.5">
                  <span>뒤집기</span>
                  <span class="text-xs">🔄</span>
                </span>
              </div>
            </div>
          </div>

          <!-- ── 2. BACK FACE (After) ── -->
          <div class="flip-card-back p-3.5 bg-gradient-to-b from-emerald-50/60 via-white to-white rounded-2xl border-2 border-emerald-500 shadow-md flex flex-col justify-between">
            <div>
              <!-- Header -->
              <div class="flex items-center justify-between mb-2">
                <div class="flex items-center gap-1.5">
                  <span class="text-base">{{ j.icon }}</span>
                  <h3 class="text-sm font-bold text-slate-900 m-0 opacity-100">{{ j.title }}</h3>
                </div>
                <span class="px-2 py-0.5 rounded bg-emerald-500 text-white text-[10px] font-bold font-mono shadow-2xs">
                  ✨ AFTER (AGENT)
                </span>
              </div>

              <!-- Subtitle -->
              <h4 class="text-xs font-bold text-emerald-800 mb-1.5">
                {{ j.afterTitle }}
              </h4>

              <!-- Body Description -->
              <p class="text-[11px] text-slate-800 leading-snug m-0" v-html="j.afterDesc" />
            </div>

            <!-- Bottom Innovation Pill & Flip Back -->
            <div>
              <div class="p-1.5 rounded-lg bg-emerald-100/70 border border-emerald-200 text-[10px] text-emerald-950 font-bold mb-2">
                {{ j.afterPill }}
              </div>
              <div class="pt-1.5 border-t border-emerald-100 flex items-center justify-between text-[10px] text-emerald-700">
                <span class="font-bold">인간: 최종 의사결정</span>
                <span class="text-slate-400 flex items-center gap-0.5">
                  <span>다시 Before</span>
                  <span class="text-xs">↩️</span>
                </span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- Bottom Key Takeaway -->
    <div class="mt-2.5 py-1.5 px-3 rounded-xl bg-slate-900 text-white shadow-xs flex items-center justify-between border border-slate-800">
      <div class="flex items-center gap-2 text-xs">
        <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-mono text-[10px] font-bold">CORE INSIGHT</span>
        <span class="text-slate-200 text-[11px]">
          단순 반복 작업(입력·탐색·취합)은 에이전트가 완수하고, <b>인간은 목표 설정과 최종 검수(Quality Control)</b>를 담당합니다.
        </span>
      </div>
      <div class="text-[10px] text-emerald-400 font-mono font-bold bg-white/10 px-2 py-0.5 rounded">
        뒤집힌 카드: {{ flippedCards.filter(Boolean).length }} / 3
      </div>
    </div>
  </div>
</template>

<style scoped>
.flip-card-container {
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.55s cubic-bezier(0.4, 0.0, 0.2, 1);
  transform-style: preserve-3d;
}

.flip-card-inner.is-flipped {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  box-sizing: border-box;
}

.flip-card-back {
  transform: rotateY(180deg);
}
</style>
