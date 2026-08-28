<script setup lang="ts">
import { markRaw } from 'vue'
import {
  Search,
  Sparkles,
  BookOpen,
  Bot,
  ArrowRight
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

type WaveStep = {
  id: string
  generation: string
  year: string
  title: string
  eng: string
  keyword: string
  desc: string
  subDesc: string
  color: string
  accentBg: string
  icon: any
  stage: number
}

const steps: WaveStep[] = [
  {
    id: 'gen1',
    generation: '1세대',
    year: '~ 2022',
    title: '검색 AI',
    eng: 'Search',
    keyword: '“ 찾아줘 ”',
    desc: '키워드 매칭 및 웹 링크 나열',
    subDesc: '정답을 사람이 직접 찾아야 함',
    color: '#64748B',
    accentBg: 'bg-white/8 text-slate-300',
    icon: markRaw(Search),
    stage: 1
  },
  {
    id: 'gen2',
    generation: '2세대',
    year: '2022 ~ 2023',
    title: '생성 AI',
    eng: 'Generative LLM',
    keyword: '“ 써줘 / 만들어줘 ”',
    desc: '확률 기반 텍스트·이미지 생성',
    subDesc: '초안 고속 작성 (단, 환각 위험)',
    color: '#3B82F6',
    accentBg: 'bg-blue-100 text-blue-300',
    icon: markRaw(Sparkles),
    stage: 2
  },
  {
    id: 'gen3',
    generation: '3세대',
    year: '2024 ~ 2025',
    title: 'RAG & Tool',
    eng: 'Retrieval Augmented',
    keyword: '“ 참고해서 만들어줘 ”',
    desc: '내부 규정 문서(PDF) 팩트 검색',
    subDesc: '오픈북처럼 명확한 출처 인증',
    color: '#10B981',
    accentBg: 'bg-emerald-100 text-emerald-300',
    icon: markRaw(BookOpen),
    stage: 3
  },
  {
    id: 'gen4',
    generation: '4세대 (현재)',
    year: '2026 ~',
    title: 'AI 에이전트',
    eng: 'Autonomous Agent',
    keyword: '“ 목표를 알아서 완수해줘 ”',
    desc: '스스로 계획 ➔ 도구 호출 ➔ 검증',
    subDesc: '사람 개입 없이 목표 자율 완수',
    color: '#6366F1',
    accentBg: 'bg-indigo-100 text-indigo-300',
    icon: markRaw(Bot),
    stage: 4
  }
]
</script>

<template>
  <div class="w-full flex flex-col items-center justify-between select-none my-auto h-[345px]">
    <!-- 4 Timeline Waves Grid with Pure Arrows and Radiant Card Glow -->
    <div class="relative w-full h-[260px] flex items-center justify-between">
      <template v-for="(st, idx) in steps" :key="st.id">
        <!-- Step Card -->
        <div
          class="w-[22.5%] h-[255px] rounded-3xl border-2 p-3.5 flex flex-col justify-between bg-white/6 transition-all duration-600 relative"
          :class="[
            stage >= st.stage
              ? 'opacity-100 scale-100 translate-y-0 shadow-md'
              : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent',
            st.stage === 4 && stage >= 4
              ? 'border-indigo-500 ring-2 ring-indigo-400/50 bg-linear-to-b from-white/10 via-indigo-950/30 to-indigo-950/40 glow-card z-20 scale-[1.02]'
              : ''
          ]"
          :style="stage >= st.stage ? { borderColor: st.color } : {}"
        >
          <!-- Top Header: Tag, Year, Icon -->
          <div class="flex items-center justify-between pb-1.5 border-b border-slate-100">
            <div class="flex items-center gap-1.5">
              <span
                class="px-1.5 py-0.5 rounded-md text-[10px] font-mono font-extrabold"
                :class="st.accentBg"
              >
                {{ st.generation }}
              </span>
              <span class="text-[9.5px] font-mono text-slate-400 font-bold">
                {{ st.year }}
              </span>
            </div>

            <!-- Icon Badge -->
            <div
              class="w-6.5 h-6.5 rounded-lg flex items-center justify-center shadow-2xs"
              :style="{ backgroundColor: `${st.color}15`, color: st.color }"
            >
              <component :is="st.icon" :size="14" />
            </div>
          </div>

          <!-- Main Title & Single-line English Tag -->
          <div class="my-auto py-1">
            <h3 class="text-base font-black text-white leading-tight">
              {{ st.title }}
            </h3>
            <div
              class="text-[10px] font-mono font-bold mt-0.5"
              :style="{ color: st.color }"
            >
              ({{ st.eng }})
            </div>

            <!-- Distinctive Speech Bubble Keyword -->
            <div
              class="mt-2 px-2 py-1.5 rounded-xl text-xs font-serif font-black tracking-tight text-center transition-all duration-300 shadow-2xs"
              :style="{ backgroundColor: `${st.color}15`, color: st.color, border: `1.5px solid ${st.color}35` }"
            >
              {{ st.keyword }}
            </div>
          </div>

          <!-- Bottom Description -->
          <div class="pt-2 border-t border-slate-100 text-[10.5px] space-y-0.5 leading-snug">
            <p class="font-bold text-slate-100 truncate">
              • {{ st.desc }}
            </p>
            <p
              class="text-[10px] truncate"
              :class="st.stage === 4 ? 'text-indigo-300 font-bold' : 'text-slate-400'"
            >
              {{ st.subDesc }}
            </p>
          </div>
        </div>

        <!-- Clean Pure Arrow without enclosing circle -->
        <div
          v-if="idx < 3"
          class="flex items-center justify-center transition-all duration-500 px-0.5"
          :class="stage >= idx + 2
            ? 'opacity-100 translate-x-0'
            : 'opacity-0 -translate-x-1 pointer-events-none'"
        >
          <ArrowRight :size="18" class="text-slate-400/90" />
        </div>
      </template>
    </div>

    <!-- Bottom Core Insight Banner (Stage >= 5) -->
    <div
      class="w-full mt-2.5 text-center transition-all duration-600 min-h-[40px] px-2"
      :class="stage >= 5 ? 'opacity-100 translate-y-0' : 'opacity-0 pointer-events-none translate-y-1'"
    >
      <div class="text-[14px] md:text-[15.5px] font-serif font-extrabold text-slate-100 tracking-tight flex items-center justify-center gap-1.5 flex-wrap">
        <span>“ AI는 단순한 대화 상대를 넘어, </span>
        <span
          class="inline-block px-2.5 py-0.5 rounded-md text-indigo-300 font-black tracking-tight transition-all duration-700"
          style="background: linear-gradient(104deg, rgba(99, 102, 241, 0.15) 0%, rgba(129, 140, 248, 0.35) 20%, rgba(99, 102, 241, 0.28) 85%, rgba(99, 102, 241, 0.12) 100%); border-bottom: 2.5px solid #6366F1;"
        >
          목표를 스스로 끝까지 완수하는 자율 에이전트(Agent)
        </span>
        <span>로 진화했습니다. ”</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.glow-card {
  box-shadow: 0 0 35px -2px rgba(99, 102, 241, 0.5), 0 0 15px rgba(99, 102, 241, 0.35), 0 10px 25px -5px rgba(99, 102, 241, 0.25);
  animation: card-pulse 3s ease-in-out infinite;
}

@keyframes card-pulse {
  0%, 100% {
    box-shadow: 0 0 32px -2px rgba(99, 102, 241, 0.45), 0 0 15px rgba(99, 102, 241, 0.3);
  }
  50% {
    box-shadow: 0 0 50px 2px rgba(99, 102, 241, 0.65), 0 0 25px rgba(99, 102, 241, 0.45);
  }
}
</style>
