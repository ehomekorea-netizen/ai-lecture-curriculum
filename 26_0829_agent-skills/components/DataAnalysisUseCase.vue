<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import {
  FileText,
  BarChart3
} from 'lucide-vue-next'

const rootRef = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | null = null

const fullPrompt = `업로드한 [2026_만족도설문.xlsx]를 분석해줘.

1. 60대, 70대, 80대 이상 어르신의 만족도를 비교해줘.
2. 가장 많이 나온 불만 3가지를 찾아줘.
3. 비교 막대그래프와 요약표를 만들어줘.
4. 사회복지사가 이해하기 쉬운 말로 핵심 결과를 정리해줘.

@Documents, 지금 분석한 결과를 1쪽짜리 요약 보고서 DOCX로 만들어줘.

보고서에는 제목, 핵심 결과 3개, 현장에서 참고할 점 2개를 넣어줘.`

const typedText = ref('')
let timer: any = null

function startTyping() {
  if (timer) clearInterval(timer)
  let charIdx = 0
  typedText.value = ''
  timer = setInterval(() => {
    if (charIdx < fullPrompt.length) {
      typedText.value += fullPrompt[charIdx]
      charIdx++
    } else {
      clearInterval(timer)
      timer = null
    }
  }, 14)
}

function stopTyping() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

onMounted(() => {
  if (rootRef.value) {
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          startTyping()
        } else {
          stopTyping()
        }
      })
    }, { threshold: 0.15 })
    observer.observe(rootRef.value)
  }
})

onUnmounted(() => {
  stopTyping()
  if (observer) observer.disconnect()
})

// Highlight keywords dynamically in typed text
const formattedHtml = computed(() => {
  let text = typedText.value
  // Escape HTML
  text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  
  // Highlight [2026_만족도설문.xlsx] (Amber)
  text = text.replace(/\[2026_만족도설문\.xlsx\]/g, '<span class="text-amber-300 font-bold">[2026_만족도설문.xlsx]</span>')
  // Highlight only the actual plugin @Documents (Blue)
  text = text.replace(/@Documents/g, '<span class="text-sky-300 font-bold">@Documents</span>')
  
  return text
})
</script>

<template>
  <div ref="rootRef" class="w-full flex flex-col justify-between select-none font-sans text-slate-100 text-left h-[330px] my-auto">
    <!-- ── Top: Features & Plugins Tag Bar ── -->
    <div class="flex items-center justify-between bg-white/5 px-3 py-1.5 rounded-xl border border-white/10 shadow-2xs mb-2">
      <div class="flex items-center gap-2">
        <span class="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">
          도구 및 플러그인
        </span>
        <div class="flex items-center gap-1.5">
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-emerald-950/80 text-emerald-300 border border-emerald-400/60 flex items-center gap-1.5 shadow-sm">
            <BarChart3 :size="12" class="text-emerald-400" />
            <span>데이터 분석 기능</span>
          </span>
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-sky-950/80 text-sky-300 border border-sky-400/60 flex items-center gap-1.5 shadow-sm">
            <FileText :size="12" class="text-sky-400" />
            <span>@Documents</span>
          </span>
        </div>
      </div>
      <span class="text-[11px] text-slate-200 font-medium">
        데이터 분석 연산 ➔ <strong class="text-white">@Documents 1쪽 요약 보고서(DOCX)</strong> 자동 렌더링
      </span>
    </div>

    <!-- ── Main 2-Column Grid (Left: Pure Typewriter Prompt, Right: Role Division) ── -->
    <div class="grid grid-cols-12 gap-4 items-stretch h-[275px]">
      <!-- ── Left Column (7 Cols): Pure Typewriter Terminal Box ── -->
      <div class="col-span-7 flex flex-col justify-start bg-slate-950 rounded-2xl border border-slate-800 p-4 shadow-xl relative overflow-hidden">
        <!-- Terminal Header Dot Indicator -->
        <div class="flex items-center gap-1.5 pb-2 border-b border-slate-800/80 mb-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-950/40 border border-rose-500/50"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500/80 border border-amber-400/50"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-950/40 border border-emerald-500/50"></span>
          <span class="text-[9.5px] font-mono text-slate-400 ml-1.5">survey-analysis-prompt</span>
        </div>

        <!-- Real-time Typewriter Prompt Body with Infinite Blinking Cursor -->
        <div class="font-mono text-[10px] leading-relaxed text-slate-200 whitespace-pre-line tracking-tight">
          <span v-html="formattedHtml"></span><span class="cursor-blink"></span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Role Division & Workflow (Apple Dark Glass) ── -->
      <div class="col-span-5 flex flex-col justify-between bg-white/5 rounded-2xl border border-white/12 p-3.5 shadow-xl backdrop-blur-sm">
        <div>
          <span class="text-[12px] font-bold text-white font-serif block mb-2.5">
            기본 분석 기능과 @Documents의 역할 분담
          </span>

          <div class="space-y-2.5">
            <!-- Role 1: 내장 데이터 분석 기능 -->
            <div class="p-2.5 rounded-xl bg-emerald-950/50 border border-emerald-400/50 shadow-xs">
              <div class="flex items-center gap-1.5 text-emerald-300 font-bold text-[11.5px] mb-1">
                <BarChart3 :size="13" class="text-emerald-400 shrink-0" />
                <span>기본 데이터 분석 (통계 & 시각화)</span>
              </div>
              <ul class="text-[10.5px] text-white space-y-1 pl-1 font-medium">
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0 mt-1"></span>
                  <span class="text-white">60·70·80대 이상 어르신 만족도 교차 비교</span>
                </li>
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0 mt-1"></span>
                  <span class="text-white">상위 3대 불만 요소 추출 및 막대그래프 생성</span>
                </li>
              </ul>
            </div>

            <!-- Role 2: @Documents -->
            <div class="p-2.5 rounded-xl bg-sky-950/50 border border-sky-400/50 shadow-xs">
              <div class="flex items-center gap-1.5 text-sky-300 font-bold text-[11.5px] mb-1">
                <FileText :size="13" class="text-sky-400 shrink-0" />
                <span>@Documents (1쪽 요약 보고서)</span>
              </div>
              <ul class="text-[10.5px] text-white space-y-1 pl-1 font-medium">
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0 mt-1"></span>
                  <span class="text-white">제목, 핵심 결과 3개, 실무 제언 2개 체계화</span>
                </li>
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0 mt-1"></span>
                  <span class="text-white">인쇄 및 즉시 결재 가능한 1쪽 DOCX 파일 렌더링</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Footer Takeaway -->
        <div class="pt-2 border-t border-white/10 flex items-start gap-1.5 text-[10.5px] text-slate-100 font-medium">
          <span class="text-amber-400 shrink-0"><span class="i-carbon:idea text-amber-300"></span></span>
          <span><strong>실무 포인트</strong>: 데이터 분석 연산 후 @Documents를 연속 호출해 1쪽 DOCX 요약 보고서 자동 렌더링</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* ── Terminal Blinking Cursor (Infinite) ── */
@keyframes cursor-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.cursor-blink {
  display: inline-block;
  width: 2px;
  height: 1.15em;
  background-color: #38bdf8;
  margin-left: 2px;
  vertical-align: text-bottom;
  animation: cursor-blink 0.9s infinite;
}
</style>
