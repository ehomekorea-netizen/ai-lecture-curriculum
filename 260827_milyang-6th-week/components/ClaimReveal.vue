<script setup lang="ts">
import { ref } from 'vue'

const step = ref(0)
// step 0: 둘 다 미표시, step 1: wrong에 취소선, step 2: 전체 공개
function advance() {
  if (step.value < 2) step.value++
}
</script>

<template>
  <div
    class="relative select-none cursor-pointer"
    @click="advance"
  >
    <!-- Click hint -->
    <div v-if="step === 0" class="absolute -top-5 left-0 text-[11px] text-slate-400 font-mono flex items-center gap-1 animate-pulse">
      <span>👆</span> 클릭하여 확인
    </div>

    <div class="flex items-center gap-3 flex-wrap" style="font-size:1.05rem; font-weight:600;">
      <!-- Wrong claim -->
      <span
        class="relative transition-all duration-500"
        :class="step >= 1 ? 'text-slate-400' : 'text-slate-700'"
        style="font-family: 'Kalam', 'Noto Sans KR', cursive;"
      >
        AI는 저장된 문장을 복사해서 꺼내온다
        <!-- Red strikethrough drawn as SVG line -->
        <svg
          v-if="step >= 1"
          class="absolute inset-0 w-full h-full pointer-events-none"
          xmlns="http://www.w3.org/2000/svg"
          preserveAspectRatio="none"
        >
          <line
            x1="0" y1="55%" x2="100%" y2="45%"
            stroke="#F5512E"
            stroke-width="2.5"
            stroke-linecap="round"
            style="stroke-dasharray:800; stroke-dashoffset:0; animation: drawLine 0.45s ease forwards;"
          />
        </svg>
      </span>

      <!-- Arrow -->
      <span
        v-if="step >= 2"
        class="text-slate-400 transition-all duration-300"
        style="font-size:0.9rem; font-style:italic;"
      >is really</span>

      <!-- Truth -->
      <span
        v-if="step >= 2"
        class="transition-all duration-500"
        style="color:var(--sapphire); font-weight:700;"
      >
        다음에 올 가능성이 가장 높은 단어를 계속 예측하여 조립한다
      </span>
    </div>
  </div>
</template>

<style scoped>
@keyframes drawLine {
  from { stroke-dashoffset: 800; }
  to   { stroke-dashoffset: 0; }
}
</style>
