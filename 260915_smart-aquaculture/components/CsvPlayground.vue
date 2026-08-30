<script setup lang="ts">
import { ref } from 'vue'

const activeQuery = ref<number>(1)

const queries = [
  {
    id: 1,
    title: '① 이상 패턴 3줄 요약',
    prompt: '7월 말~8월 초 수온 및 폐사 이상 패턴을 3줄로 요약하시오.',
    output: [
      '• 8월 1일부터 전 가두리 표층 수온이 27.5℃를 돌파하며 3일 연속 고수온 경보 유지',
      '• 8월 3일부터 조류 정체 및 야간 최저 DO가 3.8mg/L까지 급락하며 환경 악화',
      '• 수온 상승 3~4일 뒤인 8월 5일, A-03 및 B-02 가두리에서 폐사 급증(총 63미) 관측',
    ],
  },
  {
    id: 2,
    title: '② 폐사 급증 가두리 표',
    prompt: '폐사가 가장 급증한 가두리와 날짜를 표로 추출하시오.',
    table: [
      { date: '08-04', cage: 'A-03', temp: '28.1℃', do: '4.1', feed: '60kg (-40%)', death: '18미 (+14)' },
      { date: '08-05', cage: 'A-03', temp: '28.4℃', do: '3.8', feed: '0kg (절식)', death: '41미 (+23)' },
      { date: '08-05', cage: 'B-02', temp: '28.2℃', do: '3.9', feed: '30kg (-70%)', death: '22미 (+15)' },
    ],
  },
  {
    id: 3,
    title: '③ 선행 이상 신호 추적',
    prompt: '폐사 급증 1~2일 전에 나타난 선행 징후를 분석하시오.',
    output: [
      '• [선행징후 1] 8월 2일 06:00 조간 DO 회복 지연 (정상 5.5 → 4.2mg/L로 24% 저하)',
      '• [선행징후 2] 8월 3일 A-03 가두리 사료 섭이 반응 둔화 (급이 잔량 20% 발생)',
      '• [인사이트] 섭이 저하 및 DO 저하 감지 즉시 차광막 하강 및 절식을 시행했어야 함',
    ],
  },
]
</script>

<template>
  <div class="glass-card p-3.5 my-2 flex flex-col gap-2.5">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2">
      <div class="flex items-center gap-2 font-bold text-white text-xs">
        <span class="i-carbon-document-csv text-emerald-400 text-sm"></span>
        <span>가상 데이터셋 (GH-CAGE-2026.csv) AI 자동 분석 시뮬레이터</span>
      </div>
      <div class="flex items-center gap-1">
        <button
          v-for="q in queries"
          :key="q.id"
          class="px-2 py-0.5 rounded text-[11px] font-mono transition-all"
          :class="activeQuery === q.id ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold' : 'text-white/60 hover:text-white bg-white/5'"
          @click="activeQuery = q.id"
        >
          {{ q.title.split(' ')[0] }}
        </button>
      </div>
    </div>

    <!-- Active Query Prompt -->
    <div class="p-2 bg-black/40 rounded-lg border border-white/10 text-xs">
      <span class="text-white/50 text-[10px] font-mono">실행 프롬프트: </span>
      <span class="text-amber-200 font-bold text-[11px]">"{{ queries[activeQuery - 1].prompt }}"</span>
    </div>

    <!-- AI Output Area -->
    <div class="p-2.5 bg-black/60 rounded-lg border border-emerald-500/30 text-xs">
      <div class="text-[10px] text-emerald-400 font-bold mb-1.5 flex items-center gap-1">
        <span class="i-carbon-bot text-xs"></span>
        <span>AI 데이터 심층 분석 결과</span>
      </div>

      <!-- Text Output (Queries 1 & 3) -->
      <div v-if="queries[activeQuery - 1].output" class="space-y-1.5 text-[11px] text-white/90 leading-relaxed font-sans">
        <div v-for="(line, idx) in queries[activeQuery - 1].output" :key="idx">
          {{ line }}
        </div>
      </div>

      <!-- Table Output (Query 2) -->
      <div v-else-if="queries[activeQuery - 1].table" class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-[11px]">
          <thead>
            <tr class="border-b border-white/15 text-white/50 text-[10px]">
              <th class="py-1 px-1.5">일자</th>
              <th class="py-1 px-1.5">가두리</th>
              <th class="py-1 px-1.5">수온/DO</th>
              <th class="py-1 px-1.5">급이 상태</th>
              <th class="py-1 px-1.5 text-rose-300">폐사 급증</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/8 text-[11px]">
            <tr v-for="(row, rIdx) in queries[activeQuery - 1].table" :key="rIdx" class="hover:bg-white/5">
              <td class="py-1.5 px-1.5 text-white/70 font-mono">{{ row.date }}</td>
              <td class="py-1.5 px-1.5 font-bold text-white">{{ row.cage }}</td>
              <td class="py-1.5 px-1.5 text-sky-300 font-mono">{{ row.temp }} (DO {{ row.do }})</td>
              <td class="py-1.5 px-1.5 text-amber-300 font-mono">{{ row.feed }}</td>
              <td class="py-1.5 px-1.5 text-rose-400 font-bold font-mono">{{ row.death }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Security Warning Note -->
    <div class="p-1.5 bg-rose-950/20 border border-rose-500/20 rounded text-[10px] text-rose-300/90 flex items-center gap-1.5">
      <span class="i-carbon-security text-xs flex-shrink-0"></span>
      <span><strong>보안 수칙:</strong> 어촌계원 연락처나 납품 단가 등 민감한 개인정보/영업비밀 열은 사전에 삭제 후 업로드합니다.</span>
    </div>
  </div>
</template>
