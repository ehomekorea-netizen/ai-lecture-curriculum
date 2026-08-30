<script setup lang="ts">
import { computed, ref } from 'vue'

const totalDays = 100
const dangerDays = ref(3) // 1~10일
const selectedModel = ref<'dummy' | 'smart'>('dummy')

const normalDays = computed(() => totalDays - dangerDays.value)

// 깡통 모델 (무조건 '안전'만 출력)
const dummyAccuracy = computed(() => ((normalDays.value / totalDays) * 100).toFixed(0))
const dummyRecall = 0 // 실제 위험 중 잡은 건 0%

// 스마트 모델 (위험일 모두 탐지, 약간의 오경보 3건)
const smartFalseAlarms = 4
const smartAccuracy = computed(() => (((totalDays - smartFalseAlarms) / totalDays) * 100).toFixed(0))
const smartRecall = 100
</script>

<template>
  <div class="glass-card p-4 my-2 flex flex-col gap-3">
    <!-- Header & Interactive Slider -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2">
      <div class="flex items-center gap-2 font-bold text-white text-xs">
        <span class="i-carbon-calculator text-rose-400 text-sm"></span>
        <span>정확도(Accuracy)의 함정 실시간 계산 시뮬레이터</span>
      </div>
      <div class="flex items-center gap-2 text-xs">
        <span class="text-white/70">100일 중 실제 폐사 위험일:</span>
        <input
          v-model.number="dangerDays"
          type="range"
          min="1"
          max="10"
          class="w-24 accent-rose-500 cursor-pointer"
        />
        <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-mono font-bold">{{ dangerDays }}일</span>
      </div>
    </div>

    <!-- Model Toggle Buttons -->
    <div class="grid grid-cols-2 gap-3">
      <!-- Dummy Model Card -->
      <div
        class="p-3 rounded-xl border transition-all cursor-pointer flex flex-col justify-between"
        :class="selectedModel === 'dummy' ? 'bg-rose-950/30 border-rose-500/50 shadow-lg' : 'bg-black/30 border-white/10 opacity-70 hover:opacity-100'"
        @click="selectedModel = 'dummy'"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-rose-300 flex items-center gap-1">
              <span class="i-carbon-bot text-sm"></span>
              A사 깡통 AI ("무조건 안전함"만 답변)
            </span>
            <span class="text-[10px] px-1.5 py-0.2 rounded bg-rose-500/20 text-rose-300 font-mono">가짜 고성능</span>
          </div>
          <p class="text-[11px] text-white/70 leading-tight">위험을 감지하지 않고 365일 내내 "안전합니다"만 출력하는 모델</p>
        </div>

        <div class="mt-2.5 pt-2 border-t border-white/10 grid grid-cols-2 gap-2 text-center">
          <div class="p-1.5 bg-black/40 rounded">
            <div class="text-[10px] text-white/50">겉보기 정확도</div>
            <div class="text-base font-extrabold text-amber-300 font-mono">{{ dummyAccuracy }}%</div>
          </div>
          <div class="p-1.5 bg-rose-950/40 rounded border border-rose-500/30">
            <div class="text-[10px] text-rose-300">실제 위험 재현율</div>
            <div class="text-base font-extrabold text-rose-400 font-mono">{{ dummyRecall }}% 🚨</div>
          </div>
        </div>
      </div>

      <!-- Smart Model Card -->
      <div
        class="p-3 rounded-xl border transition-all cursor-pointer flex flex-col justify-between"
        :class="selectedModel === 'smart' ? 'bg-emerald-950/30 border-emerald-500/50 shadow-lg' : 'bg-black/30 border-white/10 opacity-70 hover:opacity-100'"
        @click="selectedModel = 'smart'"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-xs font-bold text-emerald-300 flex items-center gap-1">
              <span class="i-carbon-certificate-check text-sm"></span>
              B사 정상 AI (위험 적극 감지)
            </span>
            <span class="text-[10px] px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300 font-mono">실무 추천</span>
          </div>
          <p class="text-[11px] text-white/70 leading-tight">오경보가 가끔 있어도 실제 폐사 위험 {{ dangerDays }}일을 100% 잡아냄</p>
        </div>

        <div class="mt-2.5 pt-2 border-t border-white/10 grid grid-cols-2 gap-2 text-center">
          <div class="p-1.5 bg-black/40 rounded">
            <div class="text-[10px] text-white/50">겉보기 정확도</div>
            <div class="text-base font-extrabold text-white/80 font-mono">{{ smartAccuracy }}%</div>
          </div>
          <div class="p-1.5 bg-emerald-950/40 rounded border border-emerald-500/30">
            <div class="text-[10px] text-emerald-300">실제 위험 재현율</div>
            <div class="text-base font-extrabold text-emerald-400 font-mono">{{ smartRecall }}% ✅</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Insight Box -->
    <div class="p-2.5 bg-white/5 rounded-lg border border-white/10 text-xs text-white/85 flex items-center gap-2">
      <span class="i-carbon-warning-alt text-amber-400 text-lg flex-shrink-0"></span>
      <span>
        양식장 솔루션 도입 시 <strong>"정확도가 몇 %인가요?"</strong>가 아니라 <strong>"실제 위험 발생 시 재현율(Recall)이 몇 %인가요?"</strong>를 질문해야 합니다.
      </span>
    </div>
  </div>
</template>
