<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref<'all' | 'llm' | 'agent'>('all')
</script>

<template>
  <div class="agent-vs-llm mt-1">
    <!-- Comparison 2 Cards Grid -->
    <div class="grid grid-cols-2 gap-4 items-stretch">
      <!-- 1. LLM (이론가) -->
      <div
        class="p-4 bg-white rounded-2xl border transition-all duration-300 shadow-sm flex flex-col justify-between"
        :class="activeTab === 'llm' ? 'border-blue-500 ring-4 ring-blue-500/20 shadow-xl scale-[1.01]' : 'border-slate-200'"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-700 text-[10.5px] font-bold font-mono">
              LLM (거대 언어 모델)
            </span>
            <span class="text-xs font-bold text-slate-400">단일 두뇌</span>
          </div>

          <!-- Metaphor Banner -->
          <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 mb-3">
            <div class="text-xs font-bold text-slate-800 flex items-center gap-1.5">
              <span>🎓</span>
              <span>비유: 백과사전을 통째로 외운 <b>"박학다식한 이론가"</b></span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1 leading-snug">
              아는 것은 매우 많지만, 질문을 받기 전까지는 스스로 움직이지 못합니다.
            </p>
          </div>

          <!-- Key Spec Rows -->
          <div class="space-y-2 text-xs">
            <div class="p-2 rounded-lg bg-slate-50 border border-slate-100 flex items-start gap-2">
              <span class="text-slate-400 font-bold flex-shrink-0 text-[10.5px]">작동 방식</span>
              <span class="text-slate-700 font-medium text-[11px]">프롬프트 입력에 대한 <b>1회성 단발성 텍스트 응답</b></span>
            </div>
            <div class="p-2 rounded-lg bg-slate-50 border border-slate-100 flex items-start gap-2">
              <span class="text-slate-400 font-bold flex-shrink-0 text-[10.5px]">구성 요소</span>
              <span class="text-slate-700 font-medium text-[11px]">신경망 가중치 (언어 및 지식 엔진)</span>
            </div>
            <div class="p-2 rounded-lg bg-slate-50 border border-slate-100 flex items-start gap-2">
              <span class="text-slate-400 font-bold flex-shrink-0 text-[10.5px]">주요 강점</span>
              <span class="text-slate-700 font-medium text-[11px]">언어 이해, 문맥 요약, 텍스트 및 코드 초안 생성</span>
            </div>
          </div>
        </div>

        <!-- Bottom Limitation Tag -->
        <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
          <span class="text-slate-400">실무 한계</span>
          <span class="text-red-600 font-semibold">⚠️ 텍스트 답변 후 종료 (사람이 복붙·수정)</span>
        </div>
      </div>

      <!-- 2. AI Agent (실무자) -->
      <div
        class="p-4 bg-gradient-to-b from-emerald-50/40 to-white rounded-2xl border-2 border-emerald-500 transition-all duration-300 shadow-md flex flex-col justify-between"
        :class="activeTab === 'agent' ? 'ring-4 ring-emerald-500/20 shadow-2xl scale-[1.01]' : ''"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="px-2 py-0.5 rounded bg-emerald-500 text-white text-[10.5px] font-bold font-mono">
              AI Agent (AI 에이전트)
            </span>
            <span class="text-xs font-bold text-emerald-600">두뇌 + 손발(도구)</span>
          </div>

          <!-- Metaphor Banner -->
          <div class="p-2.5 rounded-xl bg-emerald-100/70 border border-emerald-200 mb-3">
            <div class="text-xs font-bold text-emerald-950 flex items-center gap-1.5">
              <span>💼</span>
              <span>비유: 이론적 지식에 손과 발이 달린 <b>"실행력 있는 실무자"</b></span>
            </div>
            <p class="text-[11px] text-emerald-800 mt-1 leading-snug">
              최종 목표만 주면 알아서 계획을 세우고 도구를 써서 결과를 납품합니다.
            </p>
          </div>

          <!-- Key Spec Rows -->
          <div class="space-y-2 text-xs">
            <div class="p-2 rounded-lg bg-white border border-emerald-100 flex items-start gap-2 shadow-2xs">
              <span class="text-emerald-700 font-bold flex-shrink-0 text-[10.5px]">작동 방식</span>
              <span class="text-slate-800 font-bold text-[11px]">목표 달성을 위한 <b>연속적인 자율 행동 루프 (Self-Loop)</b></span>
            </div>
            <div class="p-2 rounded-lg bg-white border border-emerald-100 flex items-start gap-2 shadow-2xs">
              <span class="text-emerald-700 font-bold flex-shrink-0 text-[10.5px]">구성 요소</span>
              <span class="text-emerald-950 font-bold text-[11px]">🧠 LLM(두뇌) + 📋 기획 + 💾 메모리 + 🛠️ 도구(API)</span>
            </div>
            <div class="p-2 rounded-lg bg-white border border-emerald-100 flex items-start gap-2 shadow-2xs">
              <span class="text-emerald-700 font-bold flex-shrink-0 text-[10.5px]">주요 강점</span>
              <span class="text-slate-800 font-medium text-[11px]">외부 시스템 연동, 자율적 오류 수정 및 완제품 완수</span>
            </div>
          </div>
        </div>

        <!-- Bottom Advantage Tag -->
        <div class="mt-3 pt-2 border-t border-emerald-100 flex items-center justify-between text-[11px]">
          <span class="text-emerald-700 font-medium">실무 혁신</span>
          <span class="text-emerald-700 font-bold">✨ 검색·코드작성·파일생성까지 자율 완결</span>
        </div>
      </div>
    </div>

    <!-- Bottom Concrete Example Box -->
    <div class="mt-3 p-2.5 rounded-xl bg-slate-900 text-white shadow-sm flex items-center justify-between border border-slate-800">
      <div class="flex items-center gap-2 text-xs">
        <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 font-mono text-[10px] font-bold">실무 예시</span>
        <span class="text-slate-300">
          "경쟁사 동향 분석해 줘" ➔
          <span class="text-slate-400">LLM: 텍스트 답변 생성 후 끝</span> vs
          <b class="text-emerald-400">Agent: 웹 검색 ➔ 데이터 정리 ➔ 최종 보고서 파일 생성까지 완료!</b>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
