<script setup lang="ts">
import {
  Sparkles,
  BookOpen,
  Briefcase,
  Layers,
  CheckCircle2,
  Quote,
  ShieldCheck
} from 'lucide-vue-next'

const parts = [
  {
    num: 'PART 01',
    title: '본질에서 AI 에이전트까지',
    focus: '확률적 생성 이해 · RAG 컨텍스트 · 자율 에이전트 흐름',
    color: '#3B82F6',
    icon: Sparkles
  },
  {
    num: 'PART 02',
    title: 'Gemini Notebook 실전 분석',
    focus: 'Deep Research · 3분할 스튜디오 · 무자료 사업기획 초안',
    color: '#8B5CF6',
    icon: BookOpen
  },
  {
    num: 'PART 03',
    title: 'Work 다중 파일 보고서 (DOCX)',
    focus: '데스크톱 로컬 파일 · @Documents · 5대 검수 체크리스트',
    color: '#10B981',
    icon: Briefcase
  },
  {
    num: 'PART 04',
    title: 'PPTX 에디팅 루프 & 템플릿',
    focus: '5단계 에디팅 루프 · 발표자 노트 · 기관 서식 자산화',
    color: '#F59E0B',
    icon: Layers
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Top: 4-Part Journey Recap Grid -->
    <div class="grid grid-cols-4 gap-3 mb-2.5">
      <div
        v-for="p in parts"
        :key="p.num"
        class="bg-white/6 rounded-2xl border border-white/10 p-3 shadow-2xs flex flex-col justify-between"
      >
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-mono font-bold" :style="{ color: p.color }">
              {{ p.num }}
            </span>
            <div
              class="w-6 h-6 rounded-lg flex items-center justify-center shadow-2xs"
              :style="{ background: p.color + '15', color: p.color }"
            >
              <component :is="p.icon" :size="13" />
            </div>
          </div>

          <h4 class="text-xs font-bold text-white font-serif leading-tight mb-1.5">
            {{ p.title }}
          </h4>
        </div>

        <p class="text-[10px] text-slate-400 leading-relaxed border-t border-slate-100 pt-2 mt-1">
          {{ p.focus }}
        </p>
      </div>
    </div>

    <!-- Bottom: Grand Closing Philosophy Statement Box -->
    <div class="quote-box p-4 rounded-2xl bg-gradient-to-br from-[#FAF8F4] via-white to-blue-50/40 border border-white/10 shadow-sm relative overflow-hidden">
      <div class="flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-slate-900 text-white flex items-center justify-center shrink-0 mt-0.5 shadow-xs">
          <Quote :size="16" />
        </div>
        <div class="space-y-1.5">
          <h4 class="text-sm font-bold text-white font-serif">
            "생성형 AI 협업은 프롬프트를 잘 쓰는 데서 끝나지 않습니다."
          </h4>
          <p class="text-[11.5px] text-slate-300 leading-relaxed font-serif break-keep">
            필요한 파일을 선택하고, <strong>권한과 개인정보를 철저히 통제</strong>하며, 결과물을 엄밀하게 검수하고, 
            반복 업무를 템플릿으로 축적하는 <strong>기관 고유의 실무 운영 체계(Operating System)</strong>를 만드는 일입니다.
          </p>
          <div class="flex items-center gap-3 pt-1 text-[10.5px] font-mono text-slate-400 font-bold">
            <span>최종 책임: 업무 담당자(Human-in-the-Loop)</span>
            <span>•</span>
            <span class="text-blue-400">목포종합사회복지관 교육 과정 수료</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
