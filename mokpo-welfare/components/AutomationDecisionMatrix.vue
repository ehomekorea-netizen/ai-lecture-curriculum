<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  HelpCircle,
  TrendingUp,
  Clock,
  RotateCcw,
  AlertOctagon,
  Percent,
  CheckCircle2,
  SlidersHorizontal
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const criteria = [
  {
    title: '반복 빈도',
    q: '주간·월간·회차별로 정기 반복되는가?',
    signal: '정기 보고서 ➔ 자동화 최우선 타깃',
    color: '#3B82F6'
  },
  {
    title: '데이터 구조',
    q: '입력자료와 출력양식이 일정한가?',
    signal: '표·열 구조가 고정될수록 자동화 성공률 ↑',
    color: '#8B5CF6'
  },
  {
    title: '오류 위험도',
    q: '오류 발생 시 기관/외부 영향이 큰가?',
    signal: '영향이 크면 반드시 [사람 승인 단계] 배치',
    color: '#F59E0B'
  },
  {
    title: '예외 발생률',
    q: '매번 특이사항과 예외 처리가 많은가?',
    signal: '예외가 많으면 [반자동 템플릿]이 적합',
    color: '#EC4899'
  }
]

const metrics = [
  {
    label: '총 소요 시간',
    unit: 'Time Saved',
    desc: '자료 정리 시작부터 최종 기관 승인까지의 실제 시간 측정',
    icon: Clock,
    color: '#3B82F6'
  },
  {
    label: '재작업 횟수',
    unit: 'Rework Count',
    desc: '수치·서식·문장 수정을 다시 요청한 피드백 루프 횟수',
    icon: RotateCcw,
    color: '#8B5CF6'
  },
  {
    label: '오류 발생 건수',
    unit: 'Error Rate',
    desc: '수치 불일치, 오탈자, 개인정보 노출, 서식 깨짐 수',
    icon: AlertOctagon,
    color: '#EF4444'
  },
  {
    label: '1차 검수 통과율',
    unit: 'Pass Rate',
    desc: '초안 생성 후 첫 번째 검수에서 통과한 항목의 비율',
    icon: Percent,
    color: '#10B981'
  }
]
</script>

<template>
  <div class="w-full flex items-stretch gap-4 h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Left Column (50%): 4 Decision Criteria -->
    <div class="w-1/2 flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3.5 shadow-sm">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold text-white font-serif flex items-center gap-1.5">
            <SlidersHorizontal :size="14" class="text-blue-600" />
            <span>자동화 대상 판단 4대 기준</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-blue-950/40 text-blue-400">
            도입 평가
          </span>
        </div>

        <div class="space-y-2">
          <div
            v-for="item in criteria"
            :key="item.title"
            class="p-2 px-2.5 rounded-xl bg-white/6 border border-white/10 flex flex-col justify-between"
          >
            <div class="flex items-center justify-between mb-0.5">
              <span class="text-xs font-bold text-white font-serif">{{ item.title }}</span>
              <span class="text-[9.5px] font-mono text-slate-400">{{ item.q }}</span>
            </div>
            <div class="text-[10px] font-bold mt-0.5" :style="{ color: item.color }">
              ➔ {{ item.signal }}
            </div>
          </div>
        </div>
      </div>

      <div class="bg-blue-950/40 p-2 rounded-xl border border-blue-100 text-[10px] text-blue-200 font-medium leading-tight">
        💡 <strong>핵심</strong>: '완전 무인 자동화'가 아니라 <strong>'사람이 쉽게 검토하는 반자동 템플릿'</strong>이 실무에 가장 안전합니다.
      </div>
    </div>

    <!-- Right Column (50%): 4 Quantitative Metrics -->
    <div class="w-1/2 flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3.5 shadow-sm">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold text-white font-serif flex items-center gap-1.5">
            <TrendingUp :size="14" class="text-emerald-600" />
            <span>도입 성과 정량 측정 4대 지표</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-emerald-950/40 text-emerald-400">
            KPI 지표
          </span>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div
            v-for="m in metrics"
            :key="m.label"
            class="p-2.5 rounded-xl border border-slate-100 bg-white/6 flex flex-col justify-between"
          >
            <div>
              <div class="flex items-center justify-between mb-1">
                <component :is="m.icon" :size="14" :style="{ color: m.color }" />
                <span class="text-[9px] font-mono text-slate-400 font-bold uppercase">{{ m.unit }}</span>
              </div>
              <h5 class="text-xs font-bold text-white font-serif mb-0.5">
                {{ m.label }}
              </h5>
            </div>
            <p class="text-[9.5px] text-slate-400 leading-tight mt-1">
              {{ m.desc }}
            </p>
          </div>
        </div>
      </div>

      <div class="bg-emerald-950/40 p-2 rounded-xl border border-emerald-100 text-[10px] text-emerald-200 font-medium leading-tight">
        📊 <strong>측정 원칙</strong>: 사전 추정치가 아닌, <strong>'도입 전 시간 vs 템플릿 적용 후 시간'</strong>을 직접 기록하여 검증합니다.
      </div>
    </div>
  </div>
</template>
