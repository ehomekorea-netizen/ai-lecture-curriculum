<script setup lang="ts">
import { BookOpen, Search, Sparkles, CheckCircle2, ShieldCheck } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[255px] select-none font-sans text-slate-800">
    <!-- Top Hero Card -->
    <div class="p-3 px-4 rounded-xl bg-blue-50/70 border border-blue-200 flex items-center justify-between shadow-xs shrink-0">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-lg bg-blue-600 flex items-center justify-center text-white font-bold text-sm shadow-xs">
          NL
        </div>
        <div>
          <div class="font-serif text-sm md:text-base font-bold text-slate-900 leading-tight">
            “내 자료를 100% 읽어주는 나만의 AI 전담 비서”
          </div>
          <div class="text-[10.5px] text-slate-600 mt-0.5">
            Google이 개발한 출처 기반(Source-Grounded) 지식 탐색 및 문서 작성 플랫폼
          </div>
        </div>
      </div>
      <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-800 text-[10.5px] font-bold border border-blue-200">
        Google 무료 제공
      </span>
    </div>

    <!-- 3 Core Pillars Grid -->
    <div class="grid grid-cols-3 gap-3 my-auto">
      <!-- Pillar 1 -->
      <div class="p-3 rounded-xl bg-white border border-slate-200/90 shadow-xs flex flex-col justify-between h-[135px]">
        <div>
          <div class="text-blue-700 font-bold text-xs mb-1 flex items-center gap-1.5">
            <ShieldCheck :size="14" class="text-blue-600" />
            <span>1. 원천 근거 (Grounding)</span>
          </div>
          <p class="text-[11px] text-slate-600 leading-relaxed">
            인터넷의 불확실한 정보가 아닌, <strong>내가 올린 문서 범위 내에서만</strong> 답변합니다.
          </p>
        </div>
        <div class="text-[10px] text-blue-700 font-mono font-bold bg-blue-50 px-2 py-0.5 rounded border border-blue-100">
          할루시네이션 원천 차단
        </div>
      </div>

      <!-- Pillar 2 -->
      <div class="p-3 rounded-xl bg-white border border-slate-200/90 shadow-xs flex flex-col justify-between h-[135px]">
        <div>
          <div class="text-purple-700 font-bold text-xs mb-1 flex items-center gap-1.5">
            <Search :size="14" class="text-purple-600" />
            <span>2. 출처 각주 (Citations)</span>
          </div>
          <p class="text-[11px] text-slate-600 leading-relaxed">
            모든 문장마다 <strong>원문 몇 페이지 어느 문장인지</strong> 클릭 가능한 각주 [1], [2]를 제공합니다.
          </p>
        </div>
        <div class="text-[10px] text-purple-700 font-mono font-bold bg-purple-50 px-2 py-0.5 rounded border border-purple-100">
          1초 만에 팩트 검증 완료
        </div>
      </div>

      <!-- Pillar 3 -->
      <div class="p-3 rounded-xl bg-white border border-slate-200/90 shadow-xs flex flex-col justify-between h-[135px]">
        <div>
          <div class="text-emerald-700 font-bold text-xs mb-1 flex items-center gap-1.5">
            <Sparkles :size="14" class="text-emerald-600" />
            <span>3. 문서 합성 (Synthesis)</span>
          </div>
          <p class="text-[11px] text-slate-600 leading-relaxed">
            수백 장의 방대한 자료를 <strong>요약본, 비교표, 브리핑 메모, 오디오 팟캐스트</strong>로 고속 변환합니다.
          </p>
        </div>
        <div class="text-[10px] text-emerald-700 font-mono font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-100">
          문서 작성 시간 90% 단축
        </div>
      </div>
    </div>

    <!-- Bottom Footer Box -->
    <div class="p-2 px-3 rounded-lg bg-slate-50 border border-slate-200 text-xs text-slate-700 flex items-center justify-between shrink-0">
      <span>💡 <strong>실무자 정의</strong>: 복지관 운영규정과 사업계획서를 완벽히 숙지한 <strong>나만의 1년 차 수석 기획 비서</strong></span>
      <span class="font-bold text-blue-600 text-[11px]">NotebookLM Core</span>
    </div>
  </div>
</template>
