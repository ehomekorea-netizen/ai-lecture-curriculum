<script setup lang="ts">
import { FileText, FolderOpen, ArrowRight, CheckCircle2, Sparkles, Files } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[255px] select-none font-sans text-slate-100">
    <!-- 2 Column Layout -->
    <div class="grid grid-cols-2 gap-3.5 my-auto">
      <!-- Left: Welfare Document 5 Types -->
      <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 shadow-xs flex flex-col justify-between h-[200px]">
        <div class="flex items-center justify-between pb-1 border-b border-white/10 mb-1.5">
          <span class="text-xs font-bold text-blue-300 flex items-center gap-1.5">
            <Files :size="13" class="text-blue-600" />
            <span>📁 복지관 실무 서류 5종 세트 (Sources)</span>
          </span>
          <span class="text-[9px] font-bold text-blue-400 bg-blue-950/40 px-1.5 py-0.2 rounded">단일 노트북</span>
        </div>

        <div class="space-y-1">
          <div class="p-1 px-2 rounded bg-white/6 border border-white/10 flex items-center justify-between text-[10.5px]">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-blue-400">1. 사업계획서</span>
              <span class="text-slate-400 text-[10px]">연간 계획, 목표 지표, 세부 사업</span>
            </div>
            <span class="text-[9px] text-blue-600 font-bold">기획</span>
          </div>

          <div class="p-1 px-2 rounded bg-white/6 border border-white/10 flex items-center justify-between text-[10.5px]">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-emerald-400">2. 결과보고서</span>
              <span class="text-slate-400 text-[10px]">전년도 집행 실적, 결산, 사업 평가</span>
            </div>
            <span class="text-[9px] text-emerald-600 font-bold">실적</span>
          </div>

          <div class="p-1 px-2 rounded bg-white/6 border border-white/10 flex items-center justify-between text-[10.5px]">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-purple-700">3. 지침 및 규정</span>
              <span class="text-slate-400 text-[10px]">보건복지부 안내, 복지관 운영규정</span>
            </div>
            <span class="text-[9px] text-purple-600 font-bold">규정</span>
          </div>

          <div class="p-1 px-2 rounded bg-white/6 border border-white/10 flex items-center justify-between text-[10.5px]">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-amber-700">4. 만족도 조사</span>
              <span class="text-slate-400 text-[10px]">이용자 설문 피드백, 주민 건의사항</span>
            </div>
            <span class="text-[9px] text-amber-600 font-bold">주민</span>
          </div>

          <div class="p-1 px-2 rounded bg-white/6 border border-white/10 flex items-center justify-between text-[10.5px]">
            <div class="flex items-center gap-1.5">
              <span class="font-bold text-slate-300">5. 운영일지·회의록</span>
              <span class="text-slate-400 text-[10px]">실무자 관찰 기록, 팀 회의 결과</span>
            </div>
            <span class="text-[9px] text-slate-400 font-bold">기록</span>
          </div>
        </div>
      </div>

      <!-- Right: Synergy in Practice -->
      <div class="p-3.5 rounded-xl bg-emerald-950/40 border-2 border-emerald-300 shadow-xs flex flex-col justify-between h-[200px]">
        <div class="flex items-center justify-between pb-1 border-b border-emerald-200 mb-1.5">
          <span class="text-xs font-bold text-emerald-200 flex items-center gap-1.5">
            <Sparkles :size="13" class="text-emerald-600" />
            <span>🚀 한곳에 모았을 때 일어나는 실무의 기적</span>
          </span>
          <span class="text-[9px] font-bold text-emerald-300 bg-emerald-100 px-1.5 py-0.2 rounded">전담 AI 동료</span>
        </div>

        <div class="space-y-1.5 text-[10.5px] text-slate-300">
          <div class="p-1.5 rounded bg-white/6 border border-emerald-200">
            <div class="font-bold text-emerald-300 mb-0.5">① 교차 비교 질의</div>
            <p class="text-slate-400 leading-tight">
              "작년 만족도 조사 지적사항이 이번 2026 사업계획서에 어떻게 보완되었는가?"
            </p>
          </div>

          <div class="p-1.5 rounded bg-white/6 border border-emerald-200">
            <div class="font-bold text-emerald-300 mb-0.5">② 신규 지침 검증</div>
            <p class="text-slate-400 leading-tight">
              "2026년 복지부 신규 지침과 우리 기관 규정 사이에 상충되는 조항 탐색"
            </p>
          </div>

          <div class="p-1.5 rounded bg-white/6 border border-emerald-200">
            <div class="font-bold text-emerald-300 mb-0.5">③ 초고속 결재 보고서 작성</div>
            <p class="text-slate-400 leading-tight">
              "5개 문서를 종합하여 '2026 사업추진 로드맵' 1장 요약표 원클릭 제작"
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Action Bar -->
    <div class="p-2 px-3 rounded-lg bg-emerald-100/70 border border-emerald-300 text-xs text-emerald-300 flex items-center justify-between shrink-0">
      <span>👉 <strong>실습 전환</strong>: 이제 브라우저를 열고, <strong>실제 Google NotebookLM 화면에서 직접 문서를 올리고 실습</strong>을 시작합니다!</span>
      <span class="font-bold text-emerald-300 text-[11px]">Live Demo ➔</span>
    </div>
  </div>
</template>
