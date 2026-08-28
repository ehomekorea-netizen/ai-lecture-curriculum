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
    <div class="w-full mb-3 px-3 py-1.5 rounded-xl bg-white/6 border border-white/10 flex items-center justify-between shadow-2xs">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded-md bg-blue-600 text-white font-mono font-bold text-[10px]">
          Q. 질문
        </span>
        <span class="text-xs md:text-[12.5px] font-bold text-white font-medium font-sans">
          "2026년 목포종합사회복지관 취약계층 아동 방과후 특별 보육 지원 예산은 1인당 얼마인가요?"
        </span>
      </div>
      <span class="text-[9.5px] font-mono text-slate-400 font-bold hidden sm:inline">
        EXAM QUESTION
      </span>
    </div>

    <!-- 2-Column Split Container (Fixed 210px Height to Prevent ANY Overlap) -->
    <div class="relative w-full grid grid-cols-1 md:grid-cols-2 gap-5">
      <!-- Left Card: 깜깜이 시험 (Closed-Book: 순수 LLM) — Pops in at Stage 1 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative flex flex-col justify-between h-[210px] bg-white/6 shadow-xs"
        :class="stage >= 1
          ? 'opacity-100 scale-100 translate-y-0 border-rose-300 bg-rose-950/40'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <div>
          <!-- Header with Lucide SVG Icon -->
          <div class="flex items-center justify-between pb-1.5 border-b border-rose-100 mb-2">
            <div class="flex items-center gap-1.5 font-bold text-rose-300 text-xs font-serif">
              <FileX :size="15" class="text-rose-500" />
              <span>깜깜이 시험 (기존 순수 LLM)</span>
            </div>
            <span class="text-[9px] font-mono font-bold px-2 py-0.5 rounded-full bg-rose-100 text-rose-400">
              CLOSED-BOOK
            </span>
          </div>

          <!-- Working Process -->
          <div class="space-y-1.5 text-[11.5px] text-slate-300 leading-relaxed">
            <div class="flex items-start gap-1">
              <span class="font-bold text-white shrink-0">• 방식:</span>
              <span>참고 자료 없이 <strong>모델 내부 과거 기억(2023년)</strong>에만 의존</span>
            </div>
            <div class="flex items-start gap-1">
              <span class="font-bold text-white shrink-0">• 상태:</span>
              <span class="text-rose-400 font-medium">목포시 최신 복지 지침서가 머릿속에 없어 당황</span>
            </div>
          </div>
        </div>

        <!-- Answer Output Box (Stage 1: Clean answer / Stage 2+: Red Strikethrough & Error Badge) -->
        <div
          class="rounded-xl border p-2 transition-all duration-500 bg-white/6 shadow-xs"
          :class="stage >= 2 ? 'border-rose-300 bg-rose-950/40' : 'border-white/10'"
        >
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[9.5px] font-mono font-bold text-slate-400">답변 출력:</span>
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
              : 'text-slate-100 font-mono'"
          >
            "1인당 연간 25만 원으로 알고 있습니다."
          </p>
        </div>
      </div>

      <!-- Right Card: 오픈북 시험 (Open-Book: RAG 탑재 LLM) — Pops in at Stage 3 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-600 relative flex flex-col justify-between h-[210px] bg-white/6"
        :class="stage >= 3
          ? 'opacity-100 scale-100 translate-y-0 border-emerald-500 ring-4 ring-emerald-500/15 shadow-xl bg-linear-to-b from-white/10 to-emerald-950/30'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <div>
          <!-- Header with Lucide SVG Icon & 3 RAG Pipeline Indicators -->
          <div class="flex items-center justify-between pb-1.5 border-b border-emerald-100 mb-1.5">
            <div class="flex items-center gap-1.5 font-bold text-emerald-300 text-xs font-serif">
              <BookOpen :size="15" class="text-emerald-600" />
              <span>오픈북 시험 (RAG 탑재 LLM)</span>
            </div>
            <!-- Step Pills -->
            <div class="flex items-center gap-1 font-mono text-[9px] font-bold">
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 3 ? 'bg-blue-600 text-white shadow-2xs' : 'bg-white/8 text-slate-400'"
              >
                <Search :size="9" v-if="stage >= 3" />
                <span>1.검색</span>
              </span>
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 4 ? 'bg-emerald-600 text-white shadow-2xs' : 'bg-white/8 text-slate-400'"
              >
                <Zap :size="9" v-if="stage >= 4" />
                <span>2.증강</span>
              </span>
              <span
                class="px-1.5 py-0.5 rounded transition-all duration-300 flex items-center gap-0.5"
                :class="stage >= 5 ? 'bg-purple-600 text-white shadow-2xs' : 'bg-white/8 text-slate-400'"
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
              <span class="flex items-center gap-1 text-slate-100 truncate">
                <FileText :size="12" class="text-blue-600 shrink-0" />
                <span class="truncate">목포복지관_운영규정.pdf (P.4)</span>
              </span>
            </div>

            <!-- Paragraph with Highlighter at Stage 4+ -->
            <div class="text-[10.5px] text-slate-300 leading-snug font-sans truncate">
              <span>...제4조 </span>
              <span
                class="transition-all duration-700 rounded px-1 py-0.2 font-bold inline-block"
                :class="stage >= 4
                  ? 'bg-amber-300 text-white ring-1 ring-amber-400/80 shadow-xs'
                  : 'bg-white/8 text-slate-400'"
              >
                "방과후 돌봄 아동 특별 지원금은 1인당 연간 32만 원으로 책정한다."
              </span>
            </div>
          </div>
        </div>

        <!-- Answer Output Box with Inline Grounded Citation Badge [규정집 P.4 ↗] (Appears at Stage 5) -->
        <div
          class="rounded-xl border p-2 transition-all duration-500"
          :class="stage >= 5
            ? 'border-emerald-400 bg-white/6 shadow-sm ring-2 ring-emerald-500/20'
            : 'border-white/10 bg-white/5'"
        >
          <div class="flex items-center justify-between mb-0.5">
            <span class="text-[9.5px] font-mono font-bold text-slate-400">답변 출력:</span>
          </div>
          <div class="text-[11.5px] font-bold transition-colors flex items-center gap-1.5 flex-wrap">
            <template v-if="stage >= 5">
              <span class="text-white">
                "취약계층 아동 방과후 특별 지원금은 <strong>연간 32만 원</strong>입니다."
              </span>
              <!-- Grounded Source Citation Pill (Perplexity / Gemini Citation Style) -->
              <span
                class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-md bg-emerald-950 text-emerald-300 border border-emerald-400/80 font-mono text-[10px] font-extrabold shadow-sm hover:bg-emerald-900 cursor-pointer transition-colors"
                title="출처 근거 문서: 목포복지관_운영규정.pdf (4페이지)"
              >
                <FileText :size="9" class="text-emerald-400" />
                <span>규정집 P.4</span>
                <ExternalLink :size="8" class="text-emerald-600" />
              </span>
            </template>
            <span v-else-if="stage === 4" class="text-slate-400 text-xs">
              (팩트 데이터 기반으로 출처 매핑 답변 생성 대기 중...)
            </span>
            <span v-else class="text-slate-400 text-xs">
              (규정집 P.4 검색 완료 ➔ 팩트 추출 대기 중...)
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
      <div class="text-[14.5px] md:text-[16px] font-serif font-extrabold text-slate-100 tracking-tight flex items-center justify-center gap-1.5 flex-wrap">
        <span>“ AI에게 기억만으로 시험 보게 하지 말고, </span>
        <span
          class="inline-block px-2.5 py-0.5 rounded-md text-emerald-300 font-black tracking-tight transition-all duration-700"
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
