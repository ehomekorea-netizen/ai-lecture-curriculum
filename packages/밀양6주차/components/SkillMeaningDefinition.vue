<script setup lang="ts">
import { Sparkles } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between items-center select-none font-sans text-slate-800 text-center h-[310px] my-auto py-1">
    <!-- ── Center Stage: Pure Editorial Equation Card ── -->
    <div class="w-full max-w-2xl bg-white rounded-3xl border border-slate-200/90 p-6 px-10 shadow-sm flex flex-col justify-between h-[235px] text-left">
      <!-- Equation Lines -->
      <div class="space-y-2.5 font-serif">
        <!-- Line 1 -->
        <div class="flex items-center text-xl md:text-2xl font-bold text-slate-800">
          <span class="w-8 font-mono text-transparent shrink-0">·</span>
          <span>반복되는 업무</span>
        </div>

        <!-- Line 2 -->
        <div class="flex items-center text-xl md:text-2xl font-bold text-slate-800">
          <span class="w-8 font-mono text-blue-600 font-bold shrink-0 text-xl">+</span>
          <span>정해진 처리 방식</span>
        </div>

        <!-- Line 3 -->
        <div class="flex items-center text-xl md:text-2xl font-bold text-slate-800">
          <span class="w-8 font-mono text-blue-600 font-bold shrink-0 text-xl">+</span>
          <span>원하는 결과 기준</span>
        </div>
      </div>

      <!-- Equals Divider & Final Outcome -->
      <div class="pt-3 border-t-2 border-slate-100 flex items-center justify-between">
        <div class="flex items-center text-2xl md:text-3xl font-bold font-serif text-blue-600">
          <span class="w-8 font-mono text-blue-600 font-bold shrink-0">=</span>
          <span class="tracking-tight">나만의 Skill</span>
        </div>
        <span class="text-xs font-mono font-bold text-blue-700 bg-blue-50 px-3.5 py-1 rounded-full border border-blue-200">
          재사용 업무 자산
        </span>
      </div>
    </div>

    <!-- ── Subtext (Official Insight) ── -->
    <p class="text-xs md:text-sm text-slate-500 font-medium max-w-2xl leading-relaxed text-center break-keep">
      단순 반복을 넘어, <strong>"같은 방식이 반복되어야 좋은 결과가 나오는 업무"</strong>를 위한 재사용 가능한 업무 흐름입니다.
    </p>
  </div>
</template>
