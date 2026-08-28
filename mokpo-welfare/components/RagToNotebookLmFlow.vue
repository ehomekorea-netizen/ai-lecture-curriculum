<script setup lang="ts">
import { UploadCloud, FileSpreadsheet, Search, CheckCircle2, ChevronRight, Zap } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[255px] select-none font-sans text-slate-100">
    <!-- 4-Step Chain Row -->
    <div class="grid grid-cols-4 gap-2.5 my-auto">
      <!-- Step 1 -->
      <div class="p-3 rounded-xl bg-white/6 border border-white/10 shadow-xs flex flex-col justify-between h-[155px]">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="w-5 h-5 rounded-full bg-blue-600 text-white text-[10px] font-bold flex items-center justify-center">1</span>
            <span class="text-[9.5px] font-bold text-blue-400 bg-blue-950/40 px-1.5 py-0.2 rounded border border-blue-100">소스 투입</span>
          </div>
          <div class="font-bold text-xs text-white mb-0.5">자료 업로드 (Sources)</div>
          <p class="text-[10.5px] text-slate-400 leading-snug">
            복지관 규정집, 사업계획서, 예산표 PDF/문서 등록
          </p>
        </div>
        <div class="text-[9.5px] font-mono text-blue-400 font-bold bg-blue-950/40 p-1 rounded text-center">
          최대 50개 소스
        </div>
      </div>

      <!-- Step 2 -->
      <div class="p-3 rounded-xl bg-white/6 border border-white/10 shadow-xs flex flex-col justify-between h-[155px]">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="w-5 h-5 rounded-full bg-indigo-600 text-white text-[10px] font-bold flex items-center justify-center">2</span>
            <span class="text-[9.5px] font-bold text-indigo-300 bg-indigo-50 px-1.5 py-0.2 rounded border border-indigo-100">지식 색인</span>
          </div>
          <div class="font-bold text-xs text-white mb-0.5">문단 분할 & 벡터화</div>
          <p class="text-[10.5px] text-slate-400 leading-snug">
            AI가 수백 장 문서를 문단 단위로 쪼개고 의미를 색인
          </p>
        </div>
        <div class="text-[9.5px] font-mono text-indigo-300 font-bold bg-indigo-50/80 p-1 rounded text-center">
          Semantic Indexing
        </div>
      </div>

      <!-- Step 3 -->
      <div class="p-3 rounded-xl bg-white/6 border border-white/10 shadow-xs flex flex-col justify-between h-[155px]">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="w-5 h-5 rounded-full bg-purple-600 text-white text-[10px] font-bold flex items-center justify-center">3</span>
            <span class="text-[9.5px] font-bold text-purple-700 bg-purple-50 px-1.5 py-0.2 rounded border border-purple-100">맥락 검색</span>
          </div>
          <div class="font-bold text-xs text-white mb-0.5">관련 조항 고속 탐색</div>
          <p class="text-[10.5px] text-slate-400 leading-snug">
            질문과 가장 관련 깊은 조항과 실적 데이터를 자동 추출
          </p>
        </div>
        <div class="text-[9.5px] font-mono text-purple-700 font-bold bg-purple-50/80 p-1 rounded text-center">
          Context Retrieval
        </div>
      </div>

      <!-- Step 4 -->
      <div class="p-3 rounded-xl bg-emerald-950/40 border-2 border-emerald-400 shadow-xs flex flex-col justify-between h-[155px]">
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="w-5 h-5 rounded-full bg-emerald-600 text-white text-[10px] font-bold flex items-center justify-center">4</span>
            <span class="text-[9.5px] font-bold text-emerald-300 bg-emerald-100 px-1.5 py-0.2 rounded border border-emerald-300">근거 답변</span>
          </div>
          <div class="font-bold text-xs text-emerald-300 mb-0.5">각주 기반 팩트 생성</div>
          <p class="text-[10.5px] text-emerald-200 leading-snug">
            추출된 근거 문단만 조합하여 100% 팩트 결과물 생성
          </p>
        </div>
        <div class="text-[9.5px] font-mono text-emerald-300 font-bold bg-emerald-100 p-1 rounded text-center">
          Grounded Answer [1]
        </div>
      </div>
    </div>

    <!-- Bottom Synergy Box -->
    <div class="p-2 px-3 rounded-lg bg-blue-950/40 border border-blue-200 text-xs text-slate-100 flex items-center justify-between shrink-0">
      <div class="flex items-center gap-2">
        <Zap :size="13" class="text-blue-600" />
        <span><strong>14번 슬라이드 에이전트와 동일 원리</strong>: 에이전트가 PDF를 읽고 팩트를 대조했던 RAG 파이프라인을 그대로 구현</span>
      </div>
      <span class="text-[10.5px] font-bold text-blue-400">RAG ➔ NotebookLM</span>
    </div>
  </div>
</template>
