<script setup lang="ts">
import { MessageSquare, FileCheck, AlertTriangle, CheckCircle2, ArrowRight } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between h-[255px] select-none font-sans text-slate-800">
    <!-- 2 Column Comparison Cards -->
    <div class="grid grid-cols-2 gap-3.5 my-auto">
      <!-- Left: Generic AI -->
      <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 shadow-xs flex flex-col justify-between h-[200px]">
        <div>
          <!-- Card Header -->
          <div class="flex items-center justify-between pb-1.5 border-b border-slate-200 mb-2">
            <span class="text-xs font-bold text-rose-700 flex items-center gap-1.5">
              <MessageSquare :size="13" class="text-rose-600" />
              <span>일반 범용 생성형 AI (ChatGPT / Gemini)</span>
            </span>
            <span class="px-2 py-0.5 rounded-full bg-rose-100 text-rose-800 text-[9.5px] font-bold">
              열린 지식
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-1.5 px-2.5 rounded-md bg-white border border-slate-200 text-[11px] font-mono text-slate-700 mb-2 leading-tight">
            "신입 서비스기획 취업 포트폴리오 예시 작성해 줘."
          </div>

          <!-- Bullets -->
          <div class="space-y-1 text-[11px] text-slate-600 leading-snug">
            <div>• <strong>장점</strong>: 창의적 아이디어, 일반적인 문장 작성 우수</div>
            <div>• <strong>한계</strong>: 수강생인 나의 실제 프로젝트 경험과 스킬을 전혀 모름</div>
            <div class="text-rose-600 font-bold">• <strong>위험</strong>: 그럴듯하지만 내가 하지 않은 <strong>가짜 경험(할루시네이션)</strong> 날조</div>
          </div>
        </div>

        <!-- Bottom Verdict -->
        <div class="p-1 px-2 rounded bg-rose-50 border border-rose-200 text-[10px] text-rose-800 font-bold text-center">
          ➔ 면접장에서 질문받았을 때 답변할 수 없어 큰 위험 초래
        </div>
      </div>

      <!-- Right: NotebookLM -->
      <div class="p-3.5 rounded-xl bg-emerald-50/40 border-2 border-emerald-400/80 shadow-xs flex flex-col justify-between h-[200px]">
        <div>
          <!-- Card Header -->
          <div class="flex items-center justify-between pb-1.5 border-b border-emerald-200 mb-2">
            <span class="text-xs font-bold text-emerald-800 flex items-center gap-1.5">
              <FileCheck :size="13" class="text-emerald-700" />
              <span>자료 기반 AI (Google NotebookLM)</span>
            </span>
            <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[9.5px] font-bold">
              100% 팩트 근거
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-1.5 px-2.5 rounded-md bg-white border border-emerald-300 text-[11px] font-mono text-emerald-950 mb-2 leading-tight">
            "내가 올린 [프로젝트 활동기록]과 [목표기업 채용공고]를 기준으로 작성해 줘."
          </div>

          <!-- Bullets -->
          <div class="space-y-1 text-[11px] text-emerald-950 leading-snug">
            <div>• <strong>장점</strong>: 수강생의 실제 경험 수치와 채용 우대사항만 정밀 매핑</div>
            <div>• <strong>투명성</strong>: 모든 문장마다 내 활동 기록 페이지 번호 각주 [1] [2] 제공</div>
            <div class="text-emerald-800 font-bold">• <strong>안전성</strong>: 내 기록 밖의 내용은 지어내지 않고 100% 진실성 유지</div>
          </div>
        </div>

        <!-- Bottom Verdict -->
        <div class="p-1 px-2 rounded bg-emerald-100/90 border border-emerald-300 text-[10px] text-emerald-900 font-bold text-center">
          ➔ 수강생이 100% 자신 있게 면접관 앞에서 증명 가능한 포트폴리오 완성
        </div>
      </div>
    </div>

    <!-- Bottom Summary Bar -->
    <div class="p-1.5 px-3 rounded-lg bg-slate-50 border border-slate-200 text-xs text-slate-700 text-center font-medium shrink-0">
      🎯 <strong>핵심 공식</strong>: 범용 AI가 <strong>"남의 이야기로 지어내는 AI"</strong>라면, NotebookLM은 <strong>"내가 올린 진짜 내 경험만 분석해 쓰는 나만의 AI"</strong>입니다.
    </div>
  </div>
</template>
