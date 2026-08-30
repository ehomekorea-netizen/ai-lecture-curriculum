<script setup lang="ts">
import { ref } from 'vue'

const examples = [
  {
    raw: '아침에 A동 물색 탁하고 사료 반응이 둔함. 수온 26.8',
    parsed: { cage: 'A-01', temp: '26.8℃', do: '-', status: '탁도 상승', feeding: '섭이 저하', action: '관리자 보고' },
  },
  {
    raw: 'B동 폐사 20마리쯤 증가. 산소 4.2',
    parsed: { cage: 'B-01', temp: '-', do: 'DO 4.2', status: '폐사 20미(증가)', feeding: '-', action: '현장 점검 권고' },
  },
  {
    raw: 'C동 오후에 조류 정체, 사료 절반만 줌. 수온 27.2 산소 3.9',
    parsed: { cage: 'C-01', temp: '27.2℃', do: 'DO 3.9', status: '조류 정체', feeding: '50% 감량 급이', action: '액화산소 공급' },
  },
]
</script>

<template>
  <div class="glass-card p-5 my-2 flex flex-col gap-3.5">
    <div class="flex items-center justify-between border-b border-white/10 pb-2.5">
      <div class="flex items-center gap-2 font-bold text-white text-base">
        <span class="i-carbon-table-split text-sky-400 text-lg"></span>
        <span>Few-Shot 예시 기반: 구어체 현장 메모 → 표준 일지 자동 변환</span>
      </div>
      <span class="text-xs px-2.5 py-1 rounded bg-sky-500/20 text-sky-300 font-mono font-bold">
        Few-Shot Prompting
      </span>
    </div>

    <p class="text-white/80 text-xs leading-relaxed">
      말투나 서식을 길게 설명할 필요 없이, <strong>"입력 → 출력" 예시 2~3개</strong>만 보여주면 AI가 거친 현장 메모를 완벽한 정형 데이터 표로 정리합니다.
    </p>

    <!-- Table comparison -->
    <div class="overflow-x-auto">
      <table class="w-full text-left border-collapse text-xs">
        <thead>
          <tr class="border-b border-white/20 text-white/50 text-xs">
            <th class="py-2 px-2.5 w-[38%]">현장 구어체 메모 (Raw Input)</th>
            <th class="py-2 px-2 w-[12%]">가두리</th>
            <th class="py-2 px-2 w-[14%]">수온/DO</th>
            <th class="py-2 px-2 w-[16%]">수질/상태</th>
            <th class="py-2 px-2.5 w-[20%]">조치 사항</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/10 text-xs">
          <tr v-for="(ex, i) in examples" :key="i"
            :class="i === 0 ? 'bg-amber-950/20' : i === 1 ? 'bg-sky-950/20' : 'bg-emerald-950/10'"
            class="transition-colors border-b border-white/8">
            <td class="py-2.5 px-2.5 text-amber-200 font-mono">
              "{{ ex.raw }}"
            </td>
            <td class="py-2.5 px-2 font-bold text-white">{{ ex.parsed.cage }}</td>
            <td class="py-2.5 px-2 text-sky-300 font-mono">{{ ex.parsed.temp }} {{ ex.parsed.do !== '-' ? ex.parsed.do : '' }}</td>
            <td class="py-2.5 px-2 text-emerald-300">{{ ex.parsed.status }}</td>
            <td class="py-2.5 px-2.5 text-white/90">{{ ex.parsed.feeding !== '-' ? ex.parsed.feeding : ex.parsed.action }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="p-3 bg-emerald-950/20 border border-emerald-500/20 rounded-lg text-xs text-emerald-300 flex items-center gap-2">
      <span class="i-carbon-checkmark-filled text-base flex-shrink-0"></span>
      <span>작업일지 작성 소요 시간: <strong>기존 30분 → 3분 (90% 단축)</strong> + 데이터베이스 자동 누적!</span>
    </div>
  </div>
</template>
