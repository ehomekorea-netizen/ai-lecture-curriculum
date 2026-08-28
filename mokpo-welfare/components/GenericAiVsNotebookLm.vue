<script setup lang="ts">
import { MessageSquare, FileCheck, AlertTriangle, CheckCircle2, ArrowRight } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[255px] select-none font-sans text-slate-100">
    <!-- 2 Column Comparison Cards -->
    <div class="grid grid-cols-2 gap-3.5 my-auto">
      <!-- Left: Generic AI -->
      <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 shadow-xs flex flex-col justify-between h-[200px]">
        <div>
          <!-- Card Header -->
          <div class="flex items-center justify-between pb-1.5 border-b border-white/10 mb-2">
            <span class="text-xs font-bold text-rose-400 flex items-center gap-1.5">
              <MessageSquare :size="13" class="text-rose-600" />
              <span>일반 범용 생성형 AI (ChatGPT / Gemini)</span>
            </span>
            <span class="px-2 py-0.5 rounded-full bg-rose-100 text-rose-300 text-[9.5px] font-bold">
              열린 지식
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-1.5 px-2.5 rounded-md bg-white/6 border border-white/10 text-[11px] font-mono text-slate-300 mb-2 leading-tight">
            "2026년 사회복지관 아동 돌봄 사업계획서 예시 작성해 줘."
          </div>

          <!-- Bullets -->
          <div class="space-y-1 text-[11px] text-slate-400 leading-snug">
            <div>• <strong>장점</strong>: 창의적 아이디어, 일반적인 작문 능력 우수</div>
            <div>• <strong>한계</strong>: 우리 복지관 내부 지침·예산 한도를 전혀 모름</div>
            <div class="text-rose-600 font-bold">• <strong>위험</strong>: 그럴듯하지만 기관 규정과 맞지 않는 <strong>거짓말(할루시네이션)</strong> 발생</div>
          </div>
        </div>

        <!-- Bottom Verdict -->
        <div class="p-1 px-2 rounded bg-rose-950/40 border border-rose-200 text-[10px] text-rose-300 font-bold text-center">
          ➔ 실무자가 일일이 사실 확인(Fact Check)을 다시 해야 함
        </div>
      </div>

      <!-- Right: NotebookLM -->
      <div class="p-3.5 rounded-xl bg-emerald-950/40 border-2 border-emerald-400/80 shadow-xs flex flex-col justify-between h-[200px]">
        <div>
          <!-- Card Header -->
          <div class="flex items-center justify-between pb-1.5 border-b border-emerald-200 mb-2">
            <span class="text-xs font-bold text-emerald-300 flex items-center gap-1.5">
              <FileCheck :size="13" class="text-emerald-400" />
              <span>자료 기반 AI (Google NotebookLM)</span>
            </span>
            <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-300 text-[9.5px] font-bold">
              100% 팩트 근거
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-1.5 px-2.5 rounded-md bg-white/6 border border-emerald-300 text-[11px] font-mono text-emerald-300 mb-2 leading-tight">
            "내가 올린 [2026 운영규정]과 [2025 결과보고서]를 기준으로 작성해 줘."
          </div>

          <!-- Bullets -->
          <div class="space-y-1 text-[11px] text-emerald-300 leading-snug">
            <div>• <strong>장점</strong>: 우리 복지관의 실제 예산 수치와 규정 조항만 인용</div>
            <div>• <strong>투명성</strong>: 모든 문장마다 원문 페이지 번호 각주 [1] [2] 제공</div>
            <div class="text-emerald-300 font-bold">• <strong>안전성</strong>: 자료 밖의 내용은 지어내지 않고 "자료에 없음"을 보고</div>
          </div>
        </div>

        <!-- Bottom Verdict -->
        <div class="p-1 px-2 rounded bg-emerald-100/90 border border-emerald-300 text-[10px] text-emerald-200 font-bold text-center">
          ➔ 실무자가 100% 신뢰하고 바로 결재 보고서에 활용 가능
        </div>
      </div>
    </div>

    <!-- Bottom Summary Bar -->
    <div class="p-1.5 px-3 rounded-lg bg-white/5 border border-white/10 text-xs text-slate-300 text-center font-medium shrink-0">
      🎯 <strong>핵심 공식</strong>: 범용 AI가 <strong>"도서관 전체에서 찾아오는 AI"</strong>라면, NotebookLM은 <strong>"내가 건넨 서류철만 정독하는 AI"</strong>입니다.
    </div>
  </div>
</template>
