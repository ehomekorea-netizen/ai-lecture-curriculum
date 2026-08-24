<script setup lang="ts">
import {
  FileX,
  BookOpen,
  AlertTriangle,
  FileText,
  ExternalLink,
  Search,
  Zap,
  CheckCircle2
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })
</script>

<template>
  <div class="w-full flex flex-col items-center select-none my-auto">
    <!-- 0. Question Banner (Always Visible from Start) -->
    <div class="w-full mb-3 px-3 py-1.5 rounded-xl bg-slate-100/90 border border-slate-200 flex items-center justify-between shadow-2xs">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded-md bg-blue-600 text-white font-mono font-bold text-[10px]">
          Q. 질문
        </span>
        <span class="text-xs md:text-[12.5px] font-bold text-slate-800 font-sans">
          "내가 지원하려는 기업의 2026년 신입 채용 서류 마감일과 필수 제출 포트폴리오 양식은 무엇인가요?"
        </span>
      </div>
      <span class="text-[9.5px] font-mono text-slate-500 font-bold hidden sm:inline">
        EXAM QUESTION
      </span>
    </div>

    <!-- 2-Column Split Container (Fixed 210px Height to Prevent ANY Overlap) -->
    <div class="relative w-full grid grid-cols-1 md:grid-cols-2 gap-5">
      <!-- Left Card: 깜깜이 시험 (Closed-Book: 순수 LLM) — Pops in at Stage 1 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative flex flex-col justify-between h-[210px] bg-white shadow-xs"
        :class="stage >= 1
          ? 'opacity-100 scale-100 translate-y-0 border-rose-300 bg-rose-50/25'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <div>
          <!-- Header with Lucide SVG Icon -->
          <div class="flex items-center justify-between pb-1.5 border-b border-rose-100 mb-2">
            <div class="flex items-center gap-1.5 font-bold text-rose-950 text-xs font-serif">
              <FileX :size="15" class="text-rose-500" />
              <span>깜깜이 시험 (기존 순수 LLM)</span>
            </div>
            <span class="text-[9px] font-mono font-bold px-2 py-0.5 rounded-full bg-rose-100 text-rose-700">
              CLOSED-BOOK
            </span>
          </div>

          <!-- Working Process -->
          <div class="space-y-1.5 text-[11.5px] text-slate-700 leading-relaxed">
            <div class="flex items-start gap-1">
              <span class="font-bold text-slate-900 shrink-0">• 방식:</span>
              <span>참고 자료 없이 <strong>모델 내부 과거 기억(2023년)</strong>에만 의존</span>
            </div>
            <div class="flex items-start gap-1">
              <span class="font-bold text-slate-900 shrink-0">• 상태:</span>
              <span class="text-rose-700 font-medium">목표 기업의 최신 2026년 채용 공고가 머릿속에 없어 당황</span>
            </div>
          </div>
        </div>

        <!-- Answer Output Box (Stage 1: Clean answer / Stage 2+: Red Strikethrough & Error Badge) -->
        <div
          class="rounded-xl border p-2 transition-all duration-500 bg-white shadow-xs"
          :class="stage >= 2 ? 'border-rose-300 bg-rose-50/40' : 'border-slate-200'"
        >
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[9.5px] font-mono font-bold text-slate-500">답변 출력:</span>
            <span
              v-if="stage >= 2"
              class="text-[9px] font-bold text-rose-600 bg-rose-100 px-1.5 py-0.2 rounded flex items-center gap-1 transition-opacity duration-300"
            >
              <AlertTriangle :size="10" /> 환각 오류 (근거 없음)
            </span>
          </div>
          <p
            class="text-xs font-bold transition-all duration-300 py-0.5"
            :class="stage >= 2
              ? 'text-rose-600 font-mono line-through decoration-rose-500 decoration-[2.5px]'
              : 'text-slate-800 font-mono'"
          >
            "마감일은 9월 30일이고 자유 양식으로 알고 있습니다."
          </p>
        </div>
      </div>

      <!-- Right Card: 오픈북 시험 (Open-Book: RAG 탑재 LLM) — Pops in at Stage 3 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-600 relative flex flex-col justify-between h-[210px] bg-white"
        :class="stage >= 3
          ? 'opacity-100 scale-100 translate-y-0 border-emerald-500 ring-4 ring-emerald-500/15 shadow-xl bg-linear-to-b from-white to-emerald-50/30'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <div>
          <!-- Header with Lucide SVG Icon & 3 RAG Pipeline Indicators -->
          <div class="flex items-center justify-between pb-1.5 border-b border-emerald-100 mb-1.5">
            <div class="flex items-center gap-1.5 font-bold text-emerald-950 text-xs font-serif">
              <BookOpen :size="15" class="text-emerald-600" />
              <span>오픈북 시험 (RAG 탑재 LLM)</span>
            </div>
            <!-- Step Pills -->
            <div class="flex items-center gap-1 font-mono text-[9px] font-bold">
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 3 ? 'bg-blue-600 text-white shadow-2xs' : 'bg-slate-100 text-slate-400'"
              >
                <Search :size="9" v-if="stage >= 3" />
                <span>1.검색</span>
              </span>
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 4 ? 'bg-emerald-600 text-white shadow-2xs' : 'bg-slate-100 text-slate-400'"
              >
                <Zap :size="9" v-if="stage >= 4" />
                <span>2.증강</span>
              </span>
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 5 ? 'bg-purple-600 text-white shadow-2xs' : 'bg-slate-100 text-slate-400'"
              >
                <CheckCircle2 :size="9" v-if="stage >= 5" />
                <span>3.생성</span>
              </span>
            </div>
          </div>

          <!-- Open Book Simulator Box (Document Viewer) -->
          <div
            class="rounded-xl border p-2 relative overflow-hidden transition-all duration-500"
            :class="stage >= 4
              ? 'border-emerald-300 bg-emerald-950/10 shadow-xs'
              : 'border-blue-200 bg-blue-950/5'"
          >
            <div class="flex items-center justify-between text-[10px] font-mono font-bold mb-1">
              <span class="flex items-center gap-1 text-slate-800 truncate">
                <FileText :size="12" class="text-blue-600 shrink-0" />
                <span class="truncate">2026_희망기업_채용공고.pdf (P.4)</span>
              </span>
            </div>

            <!-- Paragraph with Highlighter at Stage 4+ -->
            <div class="text-[10.5px] text-slate-700 leading-snug font-sans truncate">
              <span>...제4조 </span>
              <span
                class="transition-all duration-700 rounded px-1 py-0.2 font-bold inline-block"
                :class="stage >= 4
                  ? 'bg-amber-300 text-slate-950 ring-1 ring-amber-400/80 shadow-xs'
                  : 'bg-slate-100 text-slate-600'"
              >
                "서류 접수는 8월 31일 18시 마감이며, STAR 문제해결 과정이 포함된 포트폴리오 PDF를 필수 제출해야 한다."
              </span>
            </div>
          </div>
        </div>

        <!-- Answer Output Box with Inline Grounded Citation Badge [규정집 P.4 ↗] (Appears at Stage 5) -->
        <div
          class="rounded-xl border p-2 transition-all duration-500"
          :class="stage >= 5
            ? 'border-emerald-400 bg-white shadow-sm ring-2 ring-emerald-500/20'
            : 'border-slate-200 bg-slate-50'"
        >
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[9.5px] font-mono font-bold text-slate-500">답변 출력:</span>
          </div>
          <div class="text-[11.5px] font-bold transition-colors flex items-center gap-1.5 flex-wrap">
            <template v-if="stage >= 5">
              <span class="text-slate-900">
                "서류 접수 마감은 <strong>8월 31일 18시</strong>이며, <strong>STAR 문제해결 과정이 포함된 포트폴리오 PDF</strong>가 필수입니다."
              </span>
              <!-- Grounded Source Citation Pill (Perplexity / Gemini Citation Style) -->
              <span
                class="inline-flex items-center gap-1 px-1.5 py-0.5 rounded-md bg-emerald-100/90 text-emerald-800 border border-emerald-300/80 font-mono text-[9.5px] font-extrabold shadow-2xs hover:bg-emerald-200 cursor-pointer transition-colors"
                title="출처 근거 문서: 2026_희망기업_채용공고.pdf (4페이지)"
              >
                <FileText :size="9" class="text-emerald-700" />
                <span>공고문 P.4</span>
                <ExternalLink :size="8" class="text-emerald-600" />
              </span>
            </template>
            <span v-else-if="stage === 4" class="text-slate-400 text-xs">
              (팩트 데이터 기반으로 출처 매핑 답변 생성 대기 중...)
            </span>
            <span v-else class="text-slate-400 text-xs">
              (공고문 P.4 검색 완료 ➔ 팩트 추출 대기 중...)
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Core Insight with Emerald Highlighter Marker (Appears on Stage 6) -->
    <div
      class="w-full mt-4 text-center transition-all duration-500 min-h-[38px] px-2"
      :class="stage >= 6 ? 'opacity-100 translate-y-0' : 'opacity-0 pointer-events-none translate-y-1'"
    >
      <div class="text-[14.5px] md:text-[16px] font-serif font-extrabold text-slate-800 tracking-tight flex items-center justify-center gap-1.5 flex-wrap">
        <span>“ AI에게 기억만으로 시험 보게 하지 말고, </span>
        <span
          class="inline-block px-2.5 py-0.5 rounded-md text-emerald-950 font-black tracking-tight transition-all duration-700"
          style="background: linear-gradient(104deg, rgba(16, 185, 129, 0.18) 0%, rgba(52, 211, 153, 0.38) 15%, rgba(16, 185, 129, 0.32) 85%, rgba(16, 185, 129, 0.15) 100%); border-bottom: 2.5px solid #10B981;"
        >
          정답이 적힌 참고서를 손에 쥐여주고(RAG)
        </span>
        <span> 작성하게 하라! ”</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
