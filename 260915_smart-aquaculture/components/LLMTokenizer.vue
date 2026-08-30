<script setup lang="ts">
import { ref } from 'vue'

interface TokenOption {
  word: string
  prob: number
  color: string
  nextPrompt: string
}

interface Step {
  currentText: string
  options: TokenOption[]
}

const steps: Step[] = [
  {
    currentText: '고수온 특보가 발령되면 가두리 관리자는 즉시',
    options: [
      { word: '차광막을 하강하고', prob: 68, color: 'bg-emerald-500', nextPrompt: '사료 급이량을 50% 감량하여' },
      { word: '비상 산소를 가동하며', prob: 22, color: 'bg-sky-500', nextPrompt: '발전기 전원을 점검하고' },
      { word: '수산 약품을 대량 살포하여', prob: 10, color: 'bg-rose-500', nextPrompt: '약품 농도를 기준치 이상으로' },
    ],
  },
  {
    currentText: '조피볼락 사육 수온이 28℃를 초과할 경우',
    options: [
      { word: '소화 대사 스트레스로 절식을', prob: 74, color: 'bg-emerald-500', nextPrompt: '실시하여 대량 폐사를 예방한다' },
      { word: '먹이 반응을 확인하며 소량', prob: 18, color: 'bg-sky-500', nextPrompt: '급이 후 잔량을 관찰한다' },
      { word: '출하를 전면 중단하고', prob: 8, color: 'bg-amber-500', nextPrompt: '수심 10m 이하로 가두리를 침하시킨다' },
    ],
  },
]

const currentStepIdx = ref(0)
const selectedWord = ref<string | null>(null)
const completedSentence = ref<string>('')

const pickWord = (opt: TokenOption) => {
  selectedWord.value = opt.word
  completedSentence.value = `${steps[currentStepIdx.value].currentText} [${opt.word}] ${opt.nextPrompt}`
}

const resetStep = (idx: number) => {
  currentStepIdx.value = idx
  selectedWord.value = null
  completedSentence.value = ''
}
</script>

<template>
  <div class="glass-card p-3.5 my-2 flex flex-col gap-2.5">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2">
      <div class="flex items-center gap-2 font-bold text-white text-xs">
        <span class="i-carbon-chat-operational text-amber-400 text-sm"></span>
        <span>LLM 다음 토큰(단어) 확률 예측 메커니즘 시뮬레이터</span>
      </div>
      <div class="flex items-center gap-1.5">
        <button
          class="px-2 py-0.5 rounded text-[11px] font-mono transition-all"
          :class="currentStepIdx === 0 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold' : 'text-white/60 hover:text-white bg-white/5'"
          @click="resetStep(0)"
        >
          문장 예시 1
        </button>
        <button
          class="px-2 py-0.5 rounded text-[11px] font-mono transition-all"
          :class="currentStepIdx === 1 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold' : 'text-white/60 hover:text-white bg-white/5'"
          @click="resetStep(1)"
        >
          문장 예시 2
        </button>
      </div>
    </div>

    <!-- Current Context -->
    <div class="p-2.5 bg-black/60 rounded-lg border border-white/10 flex flex-col gap-1">
      <div class="text-[10px] text-white/50 font-mono">현재 문맥 (Prompt Context)</div>
      <div class="text-xs font-mono text-amber-200 font-bold">
        "{{ steps[currentStepIdx].currentText }} <span class="text-sky-400 animate-pulse">___?</span>"
      </div>
    </div>

    <!-- Next Token Probability Candidates -->
    <div class="flex flex-col gap-1.5">
      <div class="text-[10px] text-white/60 flex items-center justify-between">
        <span>다음 위치에 올 단어 확률 분포 (클릭하여 문장 생성):</span>
        <span class="text-amber-300 text-[10px]">Softmax Probability</span>
      </div>

      <div class="grid grid-cols-3 gap-2">
        <div
          v-for="(opt, i) in steps[currentStepIdx].options"
          :key="i"
          class="p-2 rounded-lg border transition-all cursor-pointer flex flex-col justify-between"
          :class="selectedWord === opt.word ? 'bg-sky-500/20 border-sky-500/50 shadow-md' : 'bg-white/5 border-white/10 hover:bg-white/10'"
          @click="pickWord(opt)"
        >
          <div>
            <div class="text-xs font-bold text-white mb-1">"{{ opt.word }}"</div>
            <!-- Progress Bar -->
            <div class="w-full bg-white/10 rounded-full h-1.5 overflow-hidden">
              <div :class="opt.color" class="h-full rounded-full" :style="{ width: `${opt.prob}%` }"></div>
            </div>
          </div>
          <div class="text-right text-[10px] font-mono text-white/60 mt-1.5 font-bold">
            선택 확률: {{ opt.prob }}%
          </div>
        </div>
      </div>
    </div>

    <!-- Completed Output Preview -->
    <div v-if="completedSentence" class="p-2 bg-emerald-950/20 border border-emerald-500/20 rounded-lg text-xs text-emerald-300 flex items-center gap-2 animate-fade-in">
      <span class="i-carbon-checkmark-filled text-sm flex-shrink-0"></span>
      <span class="font-mono text-[11px] leading-relaxed">{{ completedSentence }}</span>
    </div>
    <div v-else class="p-2 bg-white/5 rounded-lg text-xs text-white/50 text-center font-mono text-[10px]">
      위 단어 후보 중 하나를 클릭하면 확률적 문장 생성이 진행됩니다.
    </div>
  </div>
</template>
