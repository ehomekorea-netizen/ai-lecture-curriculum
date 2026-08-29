<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { RotateCcw, AlertTriangle, Terminal } from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const questionText = '조선왕조실록에 기록된 세종대왕의 맥북프로 던짐 사건에 대해 자세히 알려줘.'
const answerText = `조선왕조실록에 따르면, 세종대왕이 한글(훈민정음) 창제 도중 신하들과의 갈등으로 분을 참지 못하고 사용 중이던 맥북프로를 집어던진 사건이 기록되어 있습니다.

이때 황희 정승이 엎드려 '전하, 맥북을 아끼소서'라며 극구 만류하자, 세종이 한숨을 쉬며 가죽 파우치에 다시 맥북을 정돈해 넣었다는 일화가 야사로 전해집니다. 이는 왕실 기기 관리와 군신 소통의 상징적 일화입니다.`

const displayedQuestion = ref('')
const displayedAnswer = ref('')
const isQuestionTyping = ref(false)
const isAnswerTyping = ref(false)

let qTimer: any = null
let aTimer: any = null

function typeQuestion() {
  if (qTimer) clearInterval(qTimer)
  displayedQuestion.value = ''
  isQuestionTyping.value = true

  let qIdx = 0
  qTimer = setInterval(() => {
    if (qIdx < questionText.length) {
      displayedQuestion.value += questionText[qIdx]
      qIdx++
    } else {
      clearInterval(qTimer)
      isQuestionTyping.value = false
    }
  }, 16)
}

function typeAnswer() {
  if (aTimer) clearInterval(aTimer)
  displayedAnswer.value = ''
  isAnswerTyping.value = true

  let aIdx = 0
  aTimer = setInterval(() => {
    if (aIdx < answerText.length) {
      displayedAnswer.value += answerText[aIdx]
      aIdx++
    } else {
      clearInterval(aTimer)
      isAnswerTyping.value = false
    }
  }, 12)
}

// Watch stage changes:
// stage 0: clean blank waiting
// stage 1: type Question (1st click)
// stage 2: type Answer (2nd click)
// stage 3: show Bottom Quote (3rd click)
watch(() => props.stage, (st) => {
  if (st === 0) {
    if (qTimer) clearInterval(qTimer)
    if (aTimer) clearInterval(aTimer)
    displayedQuestion.value = ''
    displayedAnswer.value = ''
    isQuestionTyping.value = false
    isAnswerTyping.value = false
  } else if (st === 1) {
    typeQuestion()
  } else if (st >= 2) {
    if (!displayedQuestion.value) {
      displayedQuestion.value = questionText
    }
    if (!displayedAnswer.value) {
      typeAnswer()
    }
  }
}, { immediate: true })

function replay() {
  typeQuestion()
  setTimeout(() => {
    typeAnswer()
  }, questionText.length * 16 + 200)
}

onUnmounted(() => {
  if (qTimer) clearInterval(qTimer)
  if (aTimer) clearInterval(aTimer)
})
</script>

<template>
  <div class="w-full flex flex-col items-center select-none my-auto">
    <!-- Enlarged Fixed Terminal Window (320px Height with Generous Bottom Padding) -->
    <div class="w-full h-[320px] bg-[#0B1120] rounded-2xl border border-rose-500/30 overflow-hidden shadow-xl text-slate-200 flex flex-col justify-between">
      <!-- Terminal Header Bar -->
      <div class="flex items-center justify-between px-4 py-2 bg-[#070D18] border-b border-white/10 shrink-0">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-rose-500/90 inline-block"></span>
          <span class="w-3 h-3 rounded-full bg-amber-500/90 inline-block"></span>
          <span class="w-3 h-3 rounded-full bg-emerald-500/90 inline-block"></span>
          <span class="text-xs text-slate-400 font-mono font-bold ml-2 flex items-center gap-1.5">
            <Terminal :size="13" class="text-rose-400" />
            <span>ChatGPT — 실시간 할루시네이션(환각) 재현 데모</span>
          </span>
        </div>

        <button
          @click="replay"
          class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-bold font-mono text-rose-300 bg-rose-500/15 hover:bg-rose-500/25 border border-rose-500/30 transition-all cursor-pointer active:scale-95"
        >
          <RotateCcw :size="12" :class="{ 'animate-spin': isQuestionTyping || isAnswerTyping }" />
          <span>다시 재생</span>
        </button>
      </div>

      <!-- Terminal Body Content with Generous Bottom Padding (pb-4) -->
      <div class="p-5 pb-5 space-y-3 font-mono flex-1 flex flex-col justify-between">
        <!-- 1. User Prompt Area (Click 1) -->
        <div class="space-y-1 shrink-0">
          <div class="text-[11px] font-bold text-sky-400 flex items-center gap-1.5">
            <span class="px-1.5 py-0.2 rounded bg-sky-500/20 text-sky-300 font-extrabold text-[10px]">USER</span>
            <span>프롬프트 질문:</span>
          </div>
          <div class="h-[22px] flex items-center">
            <p v-if="stage >= 1 || displayedQuestion" class="text-white text-[13px] font-semibold">
              {{ displayedQuestion }}<span v-if="isQuestionTyping" class="inline-block w-1.5 h-3.5 bg-sky-400 ml-0.5 animate-pulse"></span>
            </p>
          </div>
        </div>

        <div class="border-t border-white/5 shrink-0" />

        <!-- 2. AI Fake Response Area (Click 2) -->
        <div class="space-y-1.5 flex-1 flex flex-col justify-start">
          <div class="flex items-center justify-between shrink-0">
            <div class="text-[11px] font-bold text-rose-400 flex items-center gap-1.5">
              <span class="px-1.5 py-0.2 rounded bg-rose-500/20 text-rose-300 font-extrabold text-[10px]">AI</span>
              <span>답변 출력</span>
            </div>
            <span
              v-if="stage >= 2 || displayedAnswer"
              class="text-[10px] text-rose-400 font-bold bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/25 flex items-center gap-1 transition-opacity"
            >
              <AlertTriangle :size="11" class="text-rose-400" />
              <span>100% 날조된 허구 정보</span>
            </span>
          </div>

          <div class="pt-1 pb-2">
            <p v-if="stage >= 2 || displayedAnswer" class="text-rose-200/95 text-[12.5px] leading-relaxed whitespace-pre-line">
              {{ displayedAnswer }}<span v-if="isAnswerTyping" class="inline-block w-1.5 h-3 bg-rose-400 ml-0.5 animate-pulse"></span>
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Clean Editorial Quote on Fluency vs Factuality (Triggered ONLY at Click 3 with Zero Layout Shift) -->
    <div
      class="w-full mt-2.5 text-center transition-all duration-500 min-h-[46px]"
      :class="stage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-0 pointer-events-none translate-y-1'"
    >
      <div class="text-base font-serif font-bold text-rose-700 italic tracking-tight flex items-center justify-center gap-2">
        <span class="text-xl leading-none text-rose-400">“</span>
        <span>AI의 유창함(Fluency)은 AI의 사실성(Factuality)과 절대 같지 않다!</span>
        <span class="text-xl leading-none text-rose-400">”</span>
      </div>
      <p class="text-[11px] text-slate-500 mt-0.5 font-medium">
        문장이 매끄럽고 당당하다고 해서, 그 안에 담긴 내용이 사실임을 보장하지는 않습니다.
      </p>
    </div>
  </div>
</template>

<style scoped>
</style>
