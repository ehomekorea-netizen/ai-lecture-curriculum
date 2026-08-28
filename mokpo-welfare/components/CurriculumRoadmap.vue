<script setup lang="ts">
import {
  Brain,
  MessageSquareCode,
  Blocks,
  Sparkles,
  ArrowRight,
  CheckCircle2
} from 'lucide-vue-next'

const chapters = [
  {
    num: '01',
    title: '생성형 AI & Agent',
    sub: '원리와 본질의 이해',
    icon: Brain,
    points: [
      'GPT 작동 원리 & 검색과의 차이',
      '할루시네이션 극복 4대 안전장치',
      'RAG(오픈북) & AI Agent 도약'
    ]
  },
  {
    num: '02',
    title: '프롬프트 지시 표준',
    sub: '명확한 제약과 맥락',
    icon: MessageSquareCode,
    points: [
      '문서 품질을 바꾸는 5대 지시 요소',
      '공문서 톤앤매너 구조화 지침',
      '실무 표준 프롬프트 프레임워크'
    ]
  },
  {
    num: '03',
    title: '도구 & 5대 검토',
    sub: '플러그인과 인간의 승인',
    icon: Blocks,
    points: [
      '@Documents & @Presentations',
      '복지정책 및 설문분석 실무 Use Case',
      '근거·수치 등 5대 검토와 최종 승인'
    ]
  },
  {
    num: '04',
    title: '스킬 & 업무 자산화',
    sub: '재사용 영구 워크플로우',
    icon: Sparkles,
    points: [
      '나만의 Skill 수식과 4단계 제작법',
      'SKILL.md 중심 표준 패키지 구조',
      '나만의 전용 스킬 초안 실습'
    ]
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-100 text-left h-[330px] my-auto py-1">
    <!-- ── 4-Stage Architectural Roadmap Grid ── -->
    <div class="grid grid-cols-4 gap-3.5 items-stretch h-[255px]">
      <div
        v-for="(ch, idx) in chapters"
        :key="ch.num"
        class="rounded-3xl border border-white/10 bg-white/6 p-4.5 flex flex-col justify-between shadow-2xs hover:border-blue-300 transition-all group relative"
      >
        <!-- Top Number + Category Subtitle -->
        <div>
          <div class="flex items-center justify-between mb-2.5">
            <span class="w-7 h-7 rounded-xl bg-blue-950/40 text-blue-600 font-mono font-bold text-xs flex items-center justify-center border border-blue-200 group-hover:bg-blue-600 group-hover:text-white transition-colors shadow-2xs">
              {{ ch.num }}
            </span>
            <component :is="ch.icon" :size="15" class="text-slate-400 group-hover:text-blue-600 transition-colors" />
          </div>

          <!-- Chapter Title -->
          <h3 class="text-sm md:text-base font-bold font-serif text-white leading-tight mb-1">
            {{ ch.title }}
          </h3>
          <span class="text-[10px] font-mono text-slate-400 block mb-2.5">
            {{ ch.sub }}
          </span>

          <!-- Key Point Bullets -->
          <ul class="space-y-1.5 text-[11px] text-slate-400 border-t border-slate-100 pt-2.5">
            <li v-for="p in ch.points" :key="p" class="flex items-start gap-1.5 leading-snug">
              <span class="text-blue-500 font-bold mt-0.5">•</span>
              <span class="break-keep">{{ p }}</span>
            </li>
          </ul>
        </div>

        <!-- Footer Tag -->
        <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[10px] font-mono text-slate-400">
          <span v-if="idx < chapters.length - 1" class="text-slate-400 group-hover:text-blue-600 transition-colors">
            Step {{ idx + 1 }} ➔
          </span>
          <span v-else class="text-emerald-600 font-bold flex items-center gap-1">
            <CheckCircle2 :size="12" /> 자산화 완성
          </span>
          <span class="font-bold text-blue-600/80">Part {{ ch.num }}</span>
        </div>
      </div>
    </div>

    <!-- ── Bottom Learning Goal Bar ── -->
    <div class="slide-footer quote-box text-xs py-1.5 px-4 font-medium truncate mt-1">
      💡 <strong>학습 로드맵</strong>: 단순 질의응답을 넘어, <strong>원리 이해 ➔ 지시 표준 ➔ 플러그인 협업 ➔ 스킬 자산화</strong>로 완성하는 실무 체계
    </div>
  </div>
</template>
