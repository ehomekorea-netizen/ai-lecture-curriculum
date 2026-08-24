<script setup lang="ts">
import { ref } from 'vue'

// 클릭할 때마다 items가 하나씩 등장하고, 마지막 클릭에서 NIST 인용구가 나타남
const ITEMS = [
  { icon: '📄', label: '텍스트', sub: '보고서 · 공문', color: '#476BFF' },
  { icon: '🖼️', label: '이미지', sub: '홍보 포스터', color: '#8b5cf6' },
  { icon: '🎙️', label: '음성', sub: '나레이션', color: '#10B981' },
  { icon: '💻', label: '코드 · 데이터', sub: '분석 자동화', color: '#f59e0b' },
]

const step = ref(0) // 0 = 아무것도 없음, 1~4 = 아이템 등장, 5 = NIST 인용구 등장

const base = import.meta.env.BASE_URL || '/'
const resolveAsset = (path: string) => {
  if (!path || path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

const total = ITEMS.length + 1 // 아이템 4개 + NIST 1개

function advance() {
  if (step.value < total) step.value++
}
</script>

<template>
  <div class="select-none" @click="advance">
    <!-- Click hint -->
    <div class="text-[11px] text-slate-400 font-mono mb-2 flex items-center gap-1" :class="step >= total ? 'opacity-0' : 'opacity-100 animate-pulse'">
      👆 클릭하여 단계별 확인 ({{ step }}/{{ total }})
    </div>

    <!-- Items row with arrows -->
    <div class="flex items-center gap-1.5 flex-wrap mb-3">
      <template v-for="(item, i) in ITEMS" :key="i">
        <!-- Item card -->
        <div
          class="transition-all duration-500"
          :style="{ opacity: step > i ? 1 : 0, transform: step > i ? 'translateY(0)' : 'translateY(10px)' }"
        >
          <div
            class="flex flex-col items-center justify-center rounded-xl border-2 px-3 py-2 min-w-[80px]"
            :style="{ borderColor: item.color + '60', background: item.color + '12' }"
            style="font-family: 'Kalam', 'Noto Sans KR', cursive;"
          >
            <span style="font-size:1.4rem;">{{ item.icon }}</span>
            <span class="text-xs font-bold mt-0.5" :style="{ color: item.color }">{{ item.label }}</span>
            <span class="text-[10px] text-slate-500 mt-0.5">{{ item.sub }}</span>
          </div>
        </div>

        <!-- Arrow between items -->
        <div
          v-if="i < ITEMS.length - 1"
          class="text-slate-400 font-bold transition-all duration-300"
          :style="{ opacity: step > i + 1 ? 1 : 0.15 }"
          style="font-size:1.1rem;"
        >
          →
        </div>

        <!-- Final arrow to NIST -->
        <div
          v-if="i === ITEMS.length - 1"
          class="text-slate-400 font-bold transition-all duration-300"
          :style="{ opacity: step >= total ? 1 : 0.15 }"
          style="font-size:1.1rem;"
        >
          →
        </div>
      </template>

      <!-- NIST Badge -->
      <div
        class="transition-all duration-500"
        :style="{ opacity: step >= total ? 1 : 0, transform: step >= total ? 'translateY(0)' : 'translateY(10px)' }"
      >
        <div class="flex flex-col items-center justify-center rounded-xl border-2 border-slate-400/40 bg-slate-100 px-3 py-2 min-w-[68px]">
          <img :src="resolveAsset('/nist-logo.png')" class="h-7 object-contain" alt="NIST" />
          <span class="text-[10px] font-bold text-slate-600 mt-0.5">공식 정의</span>
        </div>
      </div>
    </div>

    <!-- NIST 인용구 -->
    <div
      class="transition-all duration-700"
      :style="{ opacity: step >= total ? 1 : 0, transform: step >= total ? 'translateY(0)' : 'translateY(12px)' }"
    >
      <div class="quote-box text-xs text-slate-700 font-medium leading-relaxed" style="border-left-color: #857B6E;">
        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block mb-1">NIST Generative AI Framework (2023)</span>
        "학습 데이터의 구조와 특성을 분석하여, 이를 바탕으로 새롭고 독창적인 합성 콘텐츠를 생성해내는 AI 기술"
      </div>
    </div>
  </div>
</template>
