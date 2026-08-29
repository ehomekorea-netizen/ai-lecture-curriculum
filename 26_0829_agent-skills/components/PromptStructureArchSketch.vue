<script setup lang="ts">
import { markRaw } from 'vue'
import {
  UserCheck,
  Target,
  FileText,
  Sliders,
  LayoutGrid
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

type PromptElement = {
  id: string
  num: string
  title: string
  eng: string
  sub: string
  color: string
  textColor: string
  bgHighlight: string
  icon: any
  stage: number
  promptSentence: string
}

const elements: PromptElement[] = [
  {
    id: 'role',
    num: '01',
    title: '역할',
    eng: 'Role',
    sub: '누구의 관점인가?',
    color: '#38BDF8',
    textColor: 'text-sky-300',
    bgHighlight: 'bg-sky-500/25 text-white ring-2 ring-sky-400 border border-sky-400 shadow-md',
    icon: markRaw(UserCheck),
    stage: 2,
    promptSentence: '당신은 목포종합사회복지관 5년 차 아동복지 전문 기획관입니다.'
  },
  {
    id: 'goal',
    num: '02',
    title: '목표',
    eng: 'Goal',
    sub: '무엇을 달성할 것인가?',
    color: '#34D399',
    textColor: 'text-emerald-300',
    bgHighlight: 'bg-emerald-500/25 text-white ring-2 ring-emerald-400 border border-emerald-400 shadow-md',
    icon: markRaw(Target),
    stage: 3,
    promptSentence: '2026년 취약계층 아동 방과후 특별돌봄 사업계획서 초안을 기획하십시오.'
  },
  {
    id: 'context',
    num: '03',
    title: '맥락',
    eng: 'Context',
    sub: '배경 상황 · 참고 자료',
    color: '#FBBF24',
    textColor: 'text-amber-300',
    bgHighlight: 'bg-amber-500/25 text-white ring-2 ring-amber-400 border border-amber-400 shadow-md',
    icon: markRaw(FileText),
    stage: 4,
    promptSentence: '대상은 목포시 취약 아동 20명이며, 총 예산은 500만 원으로 제한됩니다.'
  },
  {
    id: 'constraint',
    num: '04',
    title: '제약',
    eng: 'Constraint',
    sub: '분량 · 어조 · 제외 조건',
    color: '#C084FC',
    textColor: 'text-purple-300',
    bgHighlight: 'bg-purple-500/25 text-white ring-2 ring-purple-400 border border-purple-400 shadow-md',
    icon: markRaw(Sliders),
    stage: 5,
    promptSentence: '어미는 공문서 격식체(~함)로 통일하고, 규정 외 내용은 날조하지 마십시오.'
  },
  {
    id: 'output',
    num: '05',
    title: '출력 형식',
    eng: 'Output',
    sub: '표 · 개조식 · 서식',
    color: '#F472B6',
    textColor: 'text-pink-300',
    bgHighlight: 'bg-pink-500/25 text-white ring-2 ring-pink-400 border border-pink-400 shadow-md',
    icon: markRaw(LayoutGrid),
    stage: 6,
    promptSentence: '출력은 [1.사업개요, 2.세부일정, 3.예산표] 3단 양식을 엄격히 준수하십시오.'
  },
]
</script>

<template>
  <div class="w-full flex flex-col items-center justify-center select-none my-auto h-[340px] relative">
    <!-- ── PROLOGUE: Pure Minimalist Naive 1-Line Prompt Statement (Stages 0 & 1) ── -->
    <div
      class="absolute inset-0 flex flex-col items-center justify-center transition-all duration-500 z-30 px-6"
      :class="stage <= 1
        ? 'opacity-100 scale-100 pointer-events-auto'
        : 'opacity-0 scale-95 pointer-events-none'"
    >
      <div
        class="w-full max-w-xl rounded-3xl border-2 p-8 flex flex-col items-center justify-center text-center shadow-xl transition-all duration-500 bg-white/6"
        :class="stage >= 1
          ? 'border-rose-300 bg-rose-950/40 ring-4 ring-rose-500/10'
          : 'border-white/15 bg-white/6 shadow-md'"
      >
        <!-- Pure Bold Statement with Strikethrough on Stage 1 (No distracting badges or footer notes) -->
        <h3
          class="text-xl md:text-2xl font-serif font-black tracking-tight leading-relaxed transition-all duration-300 py-1"
          :class="stage >= 1
            ? 'text-rose-600 line-through decoration-rose-500 decoration-[3.5px]'
            : 'text-white'"
        >
          “ 목포 복지관 방과후 프로그램 사업계획서 하나 써줘 ”
        </h3>
      </div>
    </div>

    <!-- ── MAIN: Structured Prompt 5 Cards + Zero-Shift Master Prompt Quote (Stages 2 to 6) ── -->
    <div
      class="relative w-full h-[320px] flex flex-col justify-between transition-all duration-500"
      :class="stage >= 2
        ? 'opacity-100 scale-100 pointer-events-auto'
        : 'opacity-0 scale-95 pointer-events-none'"
    >
      <!-- 1. Top Row: 5 Process Concept Cards (Height: 115px) -->
      <div class="w-full grid grid-cols-5 gap-3.5 h-[115px]">
        <div
          v-for="b in elements"
          :key="b.id"
          class="rounded-2xl border-2 p-3.5 flex flex-col justify-between bg-white/6 transition-all duration-500 shadow-xs"
          :class="stage >= b.stage
            ? 'opacity-100 scale-100 translate-y-0 shadow-md ring-2 ring-slate-100'
            : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
          :style="stage >= b.stage ? { borderColor: b.color } : {}"
        >
          <!-- Top Tag & Clean SVG Icon -->
          <div class="flex items-center justify-between pb-1 border-b border-slate-100">
            <span
              class="w-6 h-6 rounded-full flex items-center justify-center font-bold text-xs text-white shadow-2xs"
              :style="{ backgroundColor: b.color, fontFamily: `'Kalam', cursive` }"
            >
              {{ b.num }}
            </span>
            <div
              class="w-7 h-7 rounded-lg flex items-center justify-center shadow-2xs"
              :style="{ backgroundColor: `${b.color}15`, color: b.color }"
            >
              <component :is="b.icon" :size="15" />
            </div>
          </div>

          <!-- Title -->
          <div class="my-auto">
            <div class="font-black text-white text-sm md:text-[15px] leading-tight">
              {{ b.title }}
            </div>
            <div
              class="text-[10px] font-mono font-bold mt-0.5"
              :style="{ color: b.color }"
            >
              ({{ b.eng }})
            </div>
          </div>

          <!-- Sub -->
          <p class="text-[10px] text-slate-400 font-medium leading-tight truncate">
            {{ b.sub }}
          </p>
        </div>
      </div>

      <!-- 2. Bottom Row: Rock-Solid Zero-Shift Pre-Allocated Master Prompt Quote (Height: ~165px) -->
      <div
        class="w-full h-[165px] rounded-2xl bg-white/6 border-2 border-white/12 shadow-xl p-5 px-6 flex items-center justify-center transition-all duration-500 relative"
        :class="stage >= 7 ? 'ring-2 ring-cyan-400/50 bg-white/8' : stage >= 2 ? 'opacity-100' : 'opacity-20'"
      >
        <!-- Stage 7 Tag: 100% Unified Final Master Prompt Badge -->
        <div v-if="stage >= 7" class="absolute -top-3 right-5 px-2.5 py-0.5 rounded-full bg-cyan-950 border border-cyan-400 text-cyan-300 text-[10.5px] font-mono font-bold shadow-md flex items-center gap-1">
          <span>✓ 완성된 5단 구조화 표준 프롬프트</span>
        </div>

        <!-- Single Continuous Pre-Rendered Paragraph (Unified Pure White on Stage >= 7) -->
        <p class="text-[14px] md:text-[15px] leading-[1.9] font-sans text-left w-full">
          <span class="text-slate-400 font-serif font-black text-xl select-none leading-none mr-1">“</span>

          <!-- Sentence 1: Role -->
          <span
            class="transition-all duration-500 rounded px-1.5 py-0.5 font-bold"
            :class="[
              stage >= 2 ? 'opacity-100' : 'opacity-0 select-none pointer-events-none',
              stage >= 7 ? 'text-white' : stage === 2 ? elements[0].bgHighlight : elements[0].textColor
            ]"
          >{{ elements[0].promptSentence }}</span>

          <span class="inline-block w-1"></span>

          <!-- Sentence 2: Goal -->
          <span
            class="transition-all duration-500 rounded px-1.5 py-0.5 font-bold"
            :class="[
              stage >= 3 ? 'opacity-100' : 'opacity-0 select-none pointer-events-none',
              stage >= 7 ? 'text-white' : stage === 3 ? elements[1].bgHighlight : elements[1].textColor
            ]"
          >{{ elements[1].promptSentence }}</span>

          <span class="inline-block w-1"></span>

          <!-- Sentence 3: Context -->
          <span
            class="transition-all duration-500 rounded px-1.5 py-0.5 font-bold"
            :class="[
              stage >= 4 ? 'opacity-100' : 'opacity-0 select-none pointer-events-none',
              stage >= 7 ? 'text-white' : stage === 4 ? elements[2].bgHighlight : elements[2].textColor
            ]"
          >{{ elements[2].promptSentence }}</span>

          <span class="inline-block w-1"></span>

          <!-- Sentence 4: Constraint -->
          <span
            class="transition-all duration-500 rounded px-1.5 py-0.5 font-bold"
            :class="[
              stage >= 5 ? 'opacity-100' : 'opacity-0 select-none pointer-events-none',
              stage >= 7 ? 'text-white' : stage === 5 ? elements[3].bgHighlight : elements[3].textColor
            ]"
          >{{ elements[3].promptSentence }}</span>

          <span class="inline-block w-1"></span>

          <!-- Sentence 5: Output -->
          <span
            class="transition-all duration-500 rounded px-1.5 py-0.5 font-bold"
            :class="[
              stage >= 6 ? 'opacity-100' : 'opacity-0 select-none pointer-events-none',
              stage >= 7 ? 'text-white' : stage === 6 ? elements[4].bgHighlight : elements[4].textColor
            ]"
          >{{ elements[4].promptSentence }}</span>

          <span class="text-slate-400 font-serif font-black text-xl select-none leading-none ml-1">”</span>
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
