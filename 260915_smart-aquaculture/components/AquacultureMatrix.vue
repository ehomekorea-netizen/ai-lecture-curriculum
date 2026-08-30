<script setup lang="ts">
const matrix = [
  { species: '조피볼락 (우럭)', habitat: '해상가두리', tech1: '고수온·저산소 조기 경보 (최우선)', tech2: '체표 궤양·아가미 질병 영상 판별', fit: '⭐⭐⭐⭐⭐' },
  { species: '넙치 (광어)', habitat: '육상수조', tech1: '수중영상 체중 계측 & 섭이 행동 분석', tech2: '쿠도아충·바이러스 질병 조기 판별', fit: '⭐⭐⭐⭐⭐' },
  { species: '참돔 / 돌돔', habitat: '해상가두리', tech1: '선별 출하 시기 및 사료비 최적화', tech2: '이상 유영 행동 딥러닝 탐지', fit: '⭐⭐⭐⭐' },
  { species: '전복', habitat: '가두리/육상', tech1: '수온 급변 및 패각 부착 생물 분석', tech2: '먹이(미역/다시마) 잔량 영상 감지', fit: '⭐⭐⭐⭐' },
]
</script>

<template>
  <div class="glass-card p-3 my-2 text-xs">
    <div class="text-white/80 font-bold text-xs mb-2 flex items-center gap-1.5">
      <span class="i-carbon-grid text-sky-400"></span>
      <span>국내 주요 양식 어종별 AI 기술 적합도 매트릭스</span>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left border-collapse text-[11px]">
        <thead>
          <tr class="border-b border-white/20 text-white/50 text-[10px]">
            <th class="py-1 px-2">대상 어종</th>
            <th class="py-1 px-2">사육 형태</th>
            <th class="py-1 px-2">핵심 AI 예측 과제</th>
            <th class="py-1 px-2">영상/딥러닝 과제</th>
            <th class="py-1 px-2 text-right">도입 시급도</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/10">
          <tr v-for="row in matrix" :key="row.species" class="hover:bg-white/5">
            <td class="py-1.5 px-2 font-bold text-white">{{ row.species }}</td>
            <td class="py-1.5 px-2 text-white/60 font-mono">{{ row.habitat }}</td>
            <td class="py-1.5 px-2 text-sky-300">{{ row.tech1 }}</td>
            <td class="py-1.5 px-2 text-purple-300">{{ row.tech2 }}</td>
            <td class="py-1.5 px-2 text-right text-amber-300">{{ row.fit }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
