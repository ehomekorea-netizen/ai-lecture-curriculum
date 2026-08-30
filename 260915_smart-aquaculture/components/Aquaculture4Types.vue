<script setup lang="ts">
import { ref } from 'vue'

const activeType = ref<1 | 2 | 3 | 4>(1)

const types = [
  {
    id: 1,
    title: '① 예측형',
    subtitle: '미리 아는 것 (대응 시간 확보)',
    desc: '고수온·저산소 조기 경보, 폐사 위험 사전 알림, 성장 곡선 예측',
    infra: '수질 센서 로그 + 과거 기록 1년 이상 >> 전용 솔루션/서비스 도입',
    workValue: '수온 상승 후 폐사까지 수일의 시차가 존재하므로, 선제적 차광막 설치·급이 조절·비상 산소 공급 골든타임 확보',
    color: 'border-sky-500/30 bg-sky-950/20 text-sky-300',
    tagColor: 'bg-sky-500/20 text-sky-300',
    icon: 'i-carbon-chart-line',
  },
  {
    id: 2,
    title: '② 인식형',
    subtitle: '보이지 않는 것을 보는 것',
    desc: '수중영상 어체 계수(마릿수), 체장·체중 추정, 질병 증상 판별, 사료 섭이 반응 분석',
    infra: '수중 카메라 + 딥러닝 영상인식 전용 솔루션',
    workValue: '뜰채 계측 없이 스트레스 없는 성장 확인, 체표 궤양 조기 발견, 사료 낭비 방지로 사료비 15% 이상 절감',
    color: 'border-indigo-500/30 bg-indigo-950/20 text-indigo-300',
    tagColor: 'bg-indigo-500/20 text-indigo-300',
    icon: 'i-carbon-view',
  },
  {
    id: 3,
    title: '③ 최적화형',
    subtitle: '더 나은 선택을 찾는 것',
    desc: '최적 급이량 조절 제안, 어가 시세 기반 출하 시기 시나리오 비교',
    infra: '복합 솔루션 + 경영자 최종 판단',
    workValue: '사육 환경과 시장 단가를 종합 분석하여 이익을 극대화하는 출하 시점 의사결정 지원',
    color: 'border-emerald-500/30 bg-emerald-950/20 text-emerald-300',
    tagColor: 'bg-emerald-500/20 text-emerald-300',
    icon: 'i-carbon-data-enrichment',
  },
  {
    id: 4,
    title: '④ 문서·소통형',
    subtitle: '오늘부터 스마트폰으로 쓸 수 있는 것',
    desc: '구어체 작업일지 서식 정리, 어촌계 보고서 초안, 지자체 지원사업 신청서, 매뉴얼 질의응답',
    infra: '별도 장비/개발 불필요 >> 스마트폰·PC 무료 AI로 즉시 가능!',
    workValue: '일지 작성 및 공문서 정리 시간을 80% 단축하고, 규정 고시문을 즉시 찾아내는 행정 비서',
    color: 'border-amber-500/30 bg-amber-950/20 text-amber-300',
    tagColor: 'bg-amber-500/20 text-amber-300',
    icon: 'i-carbon-chat-bot',
  },
]
</script>

<template>
  <div class="my-3 flex flex-col gap-3">
    <!-- Type Navigation Tabs -->
    <div class="grid grid-cols-4 gap-2">
      <button
        v-for="t in types"
        :key="t.id"
        class="p-2.5 rounded-xl border text-left transition-all flex flex-col justify-between"
        :class="activeType === t.id ? `${t.color} border-current shadow-lg scale-[1.02] font-bold` : 'bg-white/5 border-white/10 text-white/60 hover:bg-white/10'"
        @click="activeType = t.id as 1 | 2 | 3 | 4"
      >
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold">{{ t.title }}</span>
          <span :class="[t.icon, 'text-base']"></span>
        </div>
        <div class="text-[11px] mt-1 truncate">{{ t.subtitle }}</div>
      </button>
    </div>

    <!-- Active Type Detail Card -->
    <div
      v-for="t in types.filter(t => t.id === activeType)"
      :key="t.id"
      class="glass-card p-5 border flex flex-col gap-3"
      :class="t.color"
    >
      <div class="flex items-center justify-between border-b border-white/10 pb-2">
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 rounded-full text-xs font-bold uppercase" :class="t.tagColor">
            {{ t.title }}
          </span>
          <span class="text-white text-base font-bold">{{ t.subtitle }}</span>
        </div>
        <span class="text-xs text-white/50 font-mono">해상가두리 적용 유형</span>
      </div>

      <div class="grid grid-cols-2 gap-4 text-xs">
        <div class="p-3 bg-black/40 rounded-lg border border-white/10">
          <div class="text-white/50 font-bold mb-1">주요 기능 및 적용 분야</div>
          <p class="text-white/90 leading-relaxed">{{ t.desc }}</p>
        </div>
        <div class="p-3 bg-black/40 rounded-lg border border-white/10">
          <div class="text-white/50 font-bold mb-1">도입 인프라 및 전제 조건</div>
          <p class="text-white/90 leading-relaxed font-medium">{{ t.infra }}</p>
        </div>
      </div>

      <div class="p-3 bg-white/5 rounded-lg border border-white/10 text-xs text-white/90 flex items-start gap-2">
        <span class="i-carbon-idea text-amber-300 text-base mt-0.5 flex-shrink-0"></span>
        <div>
          <strong class="text-white">현장 실무 가치:</strong> {{ t.workValue }}
        </div>
      </div>
    </div>
  </div>
</template>
