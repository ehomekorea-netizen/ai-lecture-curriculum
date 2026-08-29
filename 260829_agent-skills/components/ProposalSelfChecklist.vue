<script setup lang="ts">
import { ref } from 'vue'
import { Check, ShieldCheck, Sparkles } from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const checklistItems = [
  {
    num: '01',
    title: '명확한 이름 명명',
    code: 'writing-welfare-proposals',
    desc: '모호한 단어 대신 구체적인 행위(action) 기반 명칭으로 지정되었는가?',
    tag: 'Name Rule',
  },
  {
    num: '02',
    title: '호출 키워드 풍부화',
    code: 'description 보강',
    desc: '설명에 "사업계획서, 프로포절, 배분신청서, 공모사업"이 모두 기재되었는가?',
    tag: 'Trigger',
  },
  {
    num: '03',
    title: '단계별 작성 순서화',
    code: '1, 2, 3 단계 번호화',
    desc: '사전 분석 ➔ 세부 지침 ➔ 서식 출력의 논리적 절차가 구조화되었는가?',
    tag: 'Workflow',
  },
  {
    num: '04',
    title: '필수 4대 목차 포함',
    code: '개요 / 필요성 / 세부사업 / 기대효과',
    desc: '사업 필요성(두괄식), SMART 성과목표, 복지 예산 비목이 누락 없이 명시되었는가?',
    tag: 'Format',
  },
  {
    num: '05',
    title: '단 한 줄 자동 실행',
    code: '"나들이 기획서 써줘"',
    desc: '긴 설명 없이 짧은 일상어로 요청해도 우리 기관 표준 양식이 100% 자동 출력되는가?',
    tag: 'Automation',
  },
]
</script>

<template>
  <div class="w-full flex flex-col gap-1.5 max-w-[860px] mx-auto select-none mt-1">
    <!-- Checklist Items Grid/List -->
    <div class="flex flex-col gap-1.5">
      <div
        v-for="(item, idx) in checklistItems"
        :key="item.num"
        class="glass-card px-3.5 py-1.5 flex items-center justify-between transition-all duration-500 rounded-xl"
        :class="[
          stage > idx
            ? 'border-emerald-400/80 bg-emerald-950/30 shadow-[0_0_15px_rgba(16,185,129,0.2)] translate-x-0 opacity-100'
            : 'border-white/10 bg-white/4 opacity-40 translate-x-1'
        ]"
      >
        <!-- Left: Check Icon + Number + Title -->
        <div class="flex items-center gap-3">
          <!-- Animated Check Box -->
          <div
            class="w-6 h-6 rounded-lg flex items-center justify-center transition-all duration-500 shrink-0"
            :class="[
              stage > idx
                ? 'bg-emerald-400 text-black shadow-[0_0_10px_rgba(16,185,129,0.8)] scale-105 font-black'
                : 'bg-white/10 text-slate-400 border border-white/15'
            ]"
          >
            <Check v-if="stage > idx" :size="14" class="stroke-[3.5]" />
            <span v-else class="font-mono text-[11px] font-bold">{{ item.num }}</span>
          </div>

          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-white tracking-tight">{{ item.title }}</span>
              <span class="font-mono text-[10px] font-bold px-1.5 py-0.2 rounded bg-black/70 text-cyan-300 border border-cyan-500/40">
                {{ item.code }}
              </span>
            </div>
            <p class="text-[10.5px] text-slate-200 font-medium m-0 leading-tight">
              {{ item.desc }}
            </p>
          </div>
        </div>

        <!-- Right Tag Badge -->
        <div class="shrink-0 pl-2">
          <span
            class="font-mono text-[9.5px] font-bold px-2 py-0.5 rounded-full transition-colors duration-300"
            :class="[
              stage > idx
                ? 'bg-emerald-950/90 text-emerald-300 border border-emerald-400/80 shadow-2xs'
                : 'bg-white/5 text-slate-400 border border-white/10'
            ]"
          >
            {{ stage > idx ? 'PASS ✓' : item.tag }}
          </span>
        </div>
      </div>
    </div>

    <!-- Bottom Result Banner (Stage 5 completion) -->
    <div
      class="glass-card px-3.5 py-1.5 border-emerald-400/60 bg-gradient-to-r from-emerald-950/50 via-cyan-950/40 to-emerald-950/50 flex items-center justify-between transition-all duration-500 rounded-xl"
      :class="[
        stage >= 5
          ? 'opacity-100 scale-100 translate-y-0 shadow-[0_0_20px_rgba(16,185,129,0.3)]'
          : 'opacity-0 pointer-events-none translate-y-1'
      ]"
    >
      <div class="flex items-center gap-2">
        <ShieldCheck :size="16" class="text-emerald-400" />
        <span class="text-[11.5px] font-bold text-white">
          5대 항목 점검 완료: <strong class="text-emerald-300">목포종합사회복지관 표준 매뉴얼 공식 등록 승인</strong>
        </span>
      </div>
      <span class="inline-flex items-center gap-1 text-[10px] font-mono font-bold text-cyan-300 bg-black/70 px-2 py-0.5 rounded-md border border-cyan-400/50">
        <Sparkles :size="11" class="text-amber-300" /> READY TO DEPLOY
      </span>
    </div>
  </div>
</template>
