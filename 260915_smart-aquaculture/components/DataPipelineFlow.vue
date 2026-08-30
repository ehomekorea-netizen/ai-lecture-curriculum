<script setup lang="ts">
defineProps<{
  activeStep?: number
}>()

const steps = [
  { id: 1, title: '1. 센싱 (Sensing)', desc: '수온, DO, 염분, 탁도 수중센서 측정', icon: 'i-carbon-sensor', color: 'text-sky-400', border: 'border-sky-500/30' },
  { id: 2, title: '2. 수집·저장 (IoT)', desc: '게이트웨이 전송, 동별 시계열 DB 적재', icon: 'i-carbon-data-base', color: 'text-indigo-400', border: 'border-indigo-500/30' },
  { id: 3, title: '3. AI 분석 (Analysis)', desc: '머신러닝 이상탐지 & 폐사 예측 모델', icon: 'i-carbon-analytics', color: 'text-purple-400', border: 'border-purple-500/30' },
  { id: 4, title: '4. 제어·행동 (Action)', desc: '차광막 하강, 액화산소 가동, 사료 조절', icon: 'i-carbon-dashboard', color: 'text-emerald-400', border: 'border-emerald-500/30' },
]
</script>

<template>
  <div class="my-3">
    <div class="grid grid-cols-4 gap-2">
      <div
        v-for="s in steps"
        :key="s.id"
        class="glass-card p-3 rounded-xl border flex flex-col justify-between transition-all"
        :class="s.border"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span :class="[s.icon, s.color, 'text-lg']"></span>
            <span class="text-[10px] font-mono font-bold text-white/40">STEP 0{{ s.id }}</span>
          </div>
          <h4 class="font-bold text-white text-xs mb-1">{{ s.title }}</h4>
          <p class="text-[10px] text-white/70 leading-relaxed">{{ s.desc }}</p>
        </div>
        <div class="mt-2 pt-1 border-t border-white/10 text-[9px] font-medium" :class="s.color">
          {{ s.id === 3 ? '⭐ AI의 핵심 위치' : '데이터 전/후 체계' }}
        </div>
      </div>
    </div>
  </div>
</template>
