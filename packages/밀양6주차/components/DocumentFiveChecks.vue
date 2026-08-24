<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'

const props = withDefaults(
  defineProps<{
    stage?: number
  }>(),
  {
    stage: 0
  }
)

const currentStage = computed(() => Number(props.stage ?? 0))
const isApproved = computed(() => currentStage.value >= 1)

const checklist = [
  {
    id: 0,
    name: '근거',
    question: '원자료에 있는 내용인가요?'
  },
  {
    id: 1,
    name: '수치',
    question: '본문과 표의 숫자가 맞나요?'
  },
  {
    id: 2,
    name: '개인정보',
    question: '개인을 알아볼 수 없나요?'
  },
  {
    id: 3,
    name: '서식',
    question: '읽고 쓰기 쉽게 정리됐나요?'
  },
  {
    id: 4,
    name: '버전',
    question: '최종 파일이 맞나요?'
  }
]

const loopIndex = ref(0)
let loopTimer: any = null

function startLoop() {
  if (loopTimer) clearInterval(loopTimer)
  loopTimer = setInterval(() => {
    loopIndex.value = (loopIndex.value + 1) % checklist.length
  }, 1500)
}

function stopLoop() {
  if (loopTimer) {
    clearInterval(loopTimer)
    loopTimer = null
  }
}

onMounted(() => {
  startLoop()
})

onUnmounted(() => {
  stopLoop()
})

// When approved ($clicks >= 1), stop loop and lock onto last check (버전)
watch(isApproved, (newVal) => {
  if (newVal) {
    stopLoop()
    loopIndex.value = 4 // lock on 5th item (버전)
  } else {
    startLoop()
  }
})

const activeIndex = computed(() => {
  return isApproved.value ? 4 : loopIndex.value
})

const activeItem = computed(() => checklist[activeIndex.value])
</script>

<template>
  <div class="w-full flex flex-col justify-between items-center select-none font-sans text-slate-800 text-center h-[330px] my-auto">
    <!-- ── Top Horizontal 1-Line Navigation (근거 — 수치 — 개인정보 — 서식 — 버전) ── -->
    <div class="w-full max-w-2xl flex items-center justify-center gap-3 pt-2">
      <template v-for="(item, idx) in checklist" :key="item.id">
        <span
          class="text-sm md:text-base font-serif transition-all duration-300 px-3.5 py-1 rounded-full"
          :class="[
            activeIndex === idx
              ? 'text-blue-600 font-bold bg-blue-50 border border-blue-200 shadow-2xs scale-105'
              : 'text-slate-400 font-medium'
          ]"
        >
          {{ item.name }}
        </span>
        <span v-if="idx < checklist.length - 1" class="text-slate-300 font-mono text-xs select-none">
          —
        </span>
      </template>
    </div>

    <!-- ── Center Stage: Grand Question (Auto Loops every 1.5s) ── -->
    <div class="w-full max-w-3xl flex-1 flex flex-col items-center justify-center relative overflow-hidden py-4">
      <Transition name="question-fade" mode="out-in">
        <div :key="activeIndex" class="flex flex-col items-center justify-center px-4">
          <span class="text-xs md:text-sm font-mono font-bold text-blue-500 mb-2 uppercase tracking-wider">
            Check 0{{ activeIndex + 1 }} · {{ activeItem.name }}
          </span>
          <h2 class="text-3xl md:text-4xl lg:text-[42px] font-bold font-serif text-slate-900 tracking-tight leading-tight break-keep">
            {{ activeItem.question }}
          </h2>
        </div>
      </Transition>
    </div>

    <!-- ── Bottom Area: Positioned on the BOTTOM RIGHT on 1st Click ── -->
    <div class="w-full h-[65px] flex items-center justify-end px-8 pb-2">
      <Transition name="signature-pop">
        <div
          v-if="isApproved"
          class="flex items-center gap-3.5 px-6 py-2 rounded-2xl bg-gradient-to-r from-amber-50/95 via-orange-50/90 to-amber-50/95 border border-amber-200/90 shadow-md"
        >
          <!-- Prefix Label -->
          <span class="text-xs md:text-sm font-serif font-bold text-slate-700 tracking-wider">
            최종 승인 :
          </span>

          <!-- Animated Handwritten Signature Container with Overlapping Stamp -->
          <div class="relative inline-flex items-center justify-center pl-1 pr-4">
            <!-- Handwritten Signature -->
            <span class="signature-text">
              작성자
            </span>

            <!-- Hand-drawn Ink Underline SVG -->
            <svg class="absolute -bottom-1 left-0 w-full h-3 overflow-visible pointer-events-none" viewBox="0 0 100 12" fill="none">
              <path
                d="M 2 8 Q 45 1, 95 6 Q 65 11, 75 4"
                stroke="#ea580c"
                stroke-width="2.2"
                stroke-linecap="round"
                class="signature-underline"
              />
            </svg>

            <!-- Large Circular Red Approval Stamp Stamped Directly OVER "담당자" -->
            <div class="stamp-seal absolute -top-3.5 right-0 w-11 h-11 rounded-full border-[2.5px] border-rose-600 text-rose-600 flex items-center justify-center font-serif font-bold text-sm shadow-2xs select-none pointer-events-none mix-blend-multiply bg-rose-500/10">
              <span class="leading-none tracking-tight">승인</span>
            </div>
          </div>
        </div>
      </Transition>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');

/* ── Apple Keynote Question Smooth Fade ── */
.question-fade-enter-active,
.question-fade-leave-active {
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.question-fade-enter-from {
  opacity: 0;
  transform: translateY(14px) scale(0.98);
}

.question-fade-leave-to {
  opacity: 0;
  transform: translateY(-14px) scale(0.98);
}

/* ── Signature Box Entry (Bottom Right Slide-In) ── */
.signature-pop-enter-active {
  transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.signature-pop-enter-from {
  opacity: 0;
  transform: translateY(12px) scale(0.95);
}

/* ── Real-Time Ink Drawing Animation ── */
@keyframes write-ink {
  0% {
    clip-path: inset(0 100% 0 0);
    opacity: 0;
    transform: scale(0.92) rotate(-3deg);
  }
  15% {
    opacity: 1;
  }
  100% {
    clip-path: inset(0 0 0 0);
    opacity: 1;
    transform: scale(1) rotate(0deg);
  }
}

.signature-text {
  font-family: 'Nanum Pen Script', cursive;
  font-size: 34px;
  font-weight: 700;
  color: #ea580c;
  line-height: 1;
  letter-spacing: 0.05em;
  display: inline-block;
  white-space: nowrap;
  animation: write-ink 0.9s cubic-bezier(0.2, 0.8, 0.4, 1) 0.15s both;
}

/* ── Ink Underline SVG Path Drawing ── */
@keyframes draw-underline {
  0% {
    stroke-dashoffset: 120;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

.signature-underline {
  stroke-dasharray: 120;
  stroke-dashoffset: 120;
  animation: draw-underline 0.6s cubic-bezier(0.2, 0.8, 0.4, 1) 0.8s both;
}

/* ── Large Circular Red Stamp Impact Stamped Directly Over Text ── */
@keyframes stamp-impact {
  0% {
    opacity: 0;
    transform: scale(2.6) rotate(-25deg);
  }
  65% {
    opacity: 0.95;
    transform: scale(0.92) rotate(14deg);
  }
  100% {
    opacity: 0.9;
    transform: scale(1) rotate(12deg);
  }
}

.stamp-seal {
  animation: stamp-impact 0.45s cubic-bezier(0.16, 1, 0.3, 1) 1.05s both;
}
</style>
