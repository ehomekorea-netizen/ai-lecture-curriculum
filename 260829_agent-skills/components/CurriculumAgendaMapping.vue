<script setup lang="ts">
import {
  Sparkles,
  Bot,
  Search,
  FileText,
  Layers,
  ArrowRight,
  ShieldCheck,
  CheckCircle2,
  Target
} from 'lucide-vue-next'

const parts = [
  {
    partNum: 'PART 01',
    badge: '1차시 정규 교육',
    badgeClass: 'pill-sapphire',
    title: '생성형 AI의 본질에서 AI 에이전트까지',
    summary: 'AI 작동 원리와 RAG, 그리고 스스로 일하는 에이전트 혁명의 이해',
    color: 'blue',
    items: [
      { num: '01', title: 'AI & GPT의 본질', desc: '규칙 기반 계산에서 확률적 생성으로의 패러다임 전환' },
      { num: '02', numColor: 'text-indigo-600', title: '검색 vs 생성 & RAG', desc: '할루시네이션 극복과 오픈북 시험 방식(RAG)의 필요성' },
      { num: '03', numColor: 'text-purple-600', title: '구조화된 프롬프트', desc: '단순 대화가 아닌 명확한 지시서(프롬프트) 작성법' },
      { num: '04', numColor: 'text-blue-600', title: 'AI 에이전트의 등장', desc: '단 1번의 지시로 탐색·연산·문서를 완수하는 자율 실행' }
    ]
  },
  {
    partNum: 'PART 02',
    badge: '2차시 정규 교육',
    badgeClass: 'pill-mint',
    title: '자료 기반 AI 문서 작성 & 실전 실습',
    summary: 'Gemini Notebook을 활용하여 자료가 없는 상태에서 사업 문서 완성',
    color: 'emerald',
    items: [
      { num: '01', title: 'Gemini Notebook의 이해', desc: '무엇이든 묻는 AI vs 내 자료를 기준으로 묻는 AI' },
      { num: '02', numColor: 'text-emerald-600', title: '일반 AI vs Notebook 비교', desc: '출처 각주 기반 100% 팩트 검증 및 오디오 브리핑' },
      { num: '03', numColor: 'text-teal-600', title: '3분할 핵심 구조', desc: 'Sources(자료) ➔ Chat(질문) ➔ Studio(제작)' },
      { num: '04', numColor: 'text-emerald-600', title: '실전 복지관 사업기획 실습', desc: '자료조사 ➔ 선별 ➔ 분석 ➔ 정리 메모를 새 자료로 ➔ 초안 ➔ 검토' }
    ]
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[305px] select-none font-sans text-slate-100 py-1">
    <!-- 2 Column Part Cards -->
    <div class="grid grid-cols-2 gap-5 w-full">
      <div
        v-for="p in parts"
        :key="p.partNum"
        class="bg-white/6 rounded-2xl border border-white/10 shadow-sm p-4 flex flex-col justify-between h-[255px] text-left relative overflow-hidden"
      >
        <!-- Top Badge & Title Header -->
        <div>
          <div class="flex items-center justify-between mb-2">
            <div class="inline-flex items-center gap-2">
              <span class="pill" :class="p.badgeClass">{{ p.badge }}</span>
              <span class="text-[11px] font-mono font-bold text-slate-400 tracking-wider uppercase">{{ p.partNum }}</span>
            </div>
          </div>

          <h3 class="text-[16px] md:text-[17px] font-serif font-bold text-white leading-snug tracking-tight mb-1">
            {{ p.title }}
          </h3>
          <p class="text-[11px] text-slate-400 font-medium leading-tight mb-2.5">
            {{ p.summary }}
          </p>
        </div>

        <!-- 4 Section Items List -->
        <div class="space-y-1.5 my-auto">
          <div
            v-for="item in p.items"
            :key="item.num"
            class="flex items-start gap-2.5 p-1.5 px-2.5 rounded-lg bg-white/5 border border-slate-100"
          >
            <span
              class="text-[10px] font-mono font-bold shrink-0 mt-0.5 px-1 py-0.2 rounded"
              :class="p.color === 'blue' ? 'bg-blue-100 text-blue-300' : 'bg-emerald-100 text-emerald-300'"
            >
              {{ item.num }}
            </span>
            <div class="leading-tight">
              <span class="text-[11.5px] font-bold text-slate-100 mr-1.5">{{ item.title }}</span>
              <span class="text-[10.5px] text-slate-400 font-medium">{{ item.desc }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Footer Quote Box -->
    <div class="slide-footer quote-box text-xs font-medium text-center py-1 mt-1">
      <Target :size="13" class="inline text-rose-400 mr-1" /><strong>전체 교육 목표</strong>: "AI에게 무엇을 물어볼까?"를 넘어, <strong>"AI의 원리를 이해하고 실제 업무 문서를 어떻게 함께 완성할 것인가?"</strong>를 체득합니다.
    </div>
  </div>
</template>
