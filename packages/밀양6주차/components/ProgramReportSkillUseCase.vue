<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { ShieldCheck } from 'lucide-vue-next'

const fullPrompt = `@skill-creator

내가 교육과정에서 실습한 프로젝트 활동 기록과 커밋 로그를
채용 제출용 [STAR 기반 프로젝트 경험 포트폴리오]로 정리하는 스킬을 만들어줘.

항상 포함할 내용:
문제 상황(S), 내가 맡은 과제(T), AI 협업 및 문제 해결 행동(A), 정량적 성과(R)

내 경험 DB에 없는 내용은 절대 지어내지 말고,
면접관이 신뢰하는 전문적이고 구체적인 비즈니스 문체를 사용해줘.`

const typedText = ref('')
const isTypingFinished = ref(false)
let timer: any = null

onMounted(() => {
  let charIdx = 0
  typedText.value = ''
  isTypingFinished.value = false
  timer = setInterval(() => {
    if (charIdx < fullPrompt.length) {
      typedText.value += fullPrompt[charIdx]
      charIdx++
    } else {
      clearInterval(timer)
      timer = null
      isTypingFinished.value = true // 타이핑 완료 즉시 화살표 드로잉 트리거
    }
  }, 14)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

// Highlight keywords dynamically in typed text
const formattedHtml = computed(() => {
  let text = typedText.value
  // Escape HTML
  text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  
  // Highlight @skill-creator (Blue)
  text = text.replace(/@skill-creator/g, '<span class="text-blue-400 font-bold underline underline-offset-2">@skill-creator</span>')
  // Highlight STAR 기반 프로젝트 경험 포트폴리오 (Amber)
  text = text.replace(/\[STAR 기반 프로젝트 경험 포트폴리오\]/g, '<span class="text-amber-300 font-bold">[STAR 기반 프로젝트 경험 포트폴리오]</span>')
  // Highlight 항상 포함할 내용: (Emerald)
  text = text.replace(/항상 포함할 내용:/g, '<span class="text-emerald-300 font-bold">항상 포함할 내용:</span>')
  
  return text
})
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[310px] my-auto py-1">
    <!-- ── Main 2-Column Grid (Left: 100% Preserved Terminal, Right: Vertical 3-Card Timeline) ── -->
    <div class="grid grid-cols-12 gap-4.5 items-stretch h-full">
      <!-- ── Left Column (7 Cols): Pure Typewriter Terminal Box (100% Preserved) ── -->
      <div class="col-span-7 flex flex-col justify-start bg-slate-950 rounded-3xl border border-slate-800 p-5 shadow-xl relative overflow-hidden">
        <!-- Terminal Header Dot Indicator -->
        <div class="flex items-center gap-1.5 pb-2.5 border-b border-slate-800/80 mb-3">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-500/80"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500/80"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500/80"></span>
          <span class="text-[10px] font-mono text-slate-500 ml-1.5">skill-creator-prompt</span>
        </div>

        <!-- Real-time Typewriter Prompt Body with Infinite Blinking Cursor -->
        <div class="font-mono text-[10.5px] leading-relaxed text-slate-200 whitespace-pre-line tracking-tight">
          <span v-html="formattedHtml"></span><span class="cursor-blink"></span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Vertical 3-Step Flow with Sequential 1.0s Slow-Drawn Arrows ── -->
      <div class="col-span-5 flex flex-col justify-between h-full py-0.5">
        <!-- Top Area: 3 Vertical Independent Cards with Arrows Triggered on Typing Finish -->
        <div class="flex flex-col justify-center flex-1">
          <!-- Card 1: 프로젝트 활동 기록 -->
          <div class="w-full h-[52px] bg-white rounded-2xl border border-slate-300 shadow-2xs px-4 flex items-center gap-3">
            <span class="w-6 h-6 rounded-lg bg-blue-50 text-blue-600 font-mono font-bold text-xs flex items-center justify-center border border-blue-200 shrink-0">
              01
            </span>
            <span class="text-sm font-serif font-bold text-slate-800 tracking-tight whitespace-nowrap">
              프로젝트 활동 기록
            </span>
          </div>

          <!-- Rough Hand-drawn Arrow 1 (Draws for 1.0s immediately after typing completes) -->
          <div class="flex items-center justify-center h-4.5 my-0.5">
            <svg
              class="w-4 h-4.5 overflow-visible transition-opacity duration-300"
              :class="isTypingFinished ? 'opacity-100' : 'opacity-0'"
              viewBox="0 0 16 18"
              fill="none"
            >
              <!-- Hand-drawn wavy vertical shaft -->
              <path
                d="M 8 1.5 Q 6.8 8, 8 14.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-1-shaft' : ''"
              />
              <!-- Hand-drawn left head -->
              <path
                d="M 3.5 10 Q 6 13, 8 15.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-1-head' : ''"
              />
              <!-- Hand-drawn right head -->
              <path
                d="M 12.5 10 Q 10 13, 8 15.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-1-head' : ''"
              />
            </svg>
          </div>

          <!-- Card 2: @skill-creator -->
          <div class="w-full h-[52px] bg-white rounded-2xl border border-slate-300 shadow-2xs px-4 flex items-center gap-3">
            <span class="w-6 h-6 rounded-lg bg-blue-50 text-blue-600 font-mono font-bold text-xs flex items-center justify-center border border-blue-200 shrink-0">
              02
            </span>
            <span class="text-sm font-mono font-bold text-blue-600 tracking-tight whitespace-nowrap">
              @skill-creator
            </span>
          </div>

          <!-- Rough Hand-drawn Arrow 2 (Draws for 1.0s starting 1.0s after Arrow 1) -->
          <div class="flex items-center justify-center h-4.5 my-0.5">
            <svg
              class="w-4 h-4.5 overflow-visible transition-opacity duration-300"
              :class="isTypingFinished ? 'opacity-100' : 'opacity-0'"
              viewBox="0 0 16 18"
              fill="none"
            >
              <!-- Hand-drawn wavy vertical shaft -->
              <path
                d="M 8 1.5 Q 6.8 8, 8 14.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-2-shaft' : ''"
              />
              <!-- Hand-drawn left head -->
              <path
                d="M 3.5 10 Q 6 13, 8 15.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-2-head' : ''"
              />
              <!-- Hand-drawn right head -->
              <path
                d="M 12.5 10 Q 10 13, 8 15.5"
                stroke="#2563eb"
                stroke-width="2.4"
                stroke-linecap="round"
                :class="isTypingFinished ? 'rough-arrow-2-head' : ''"
              />
            </svg>
          </div>

          <!-- Card 3: STAR 경험 포트폴리오 -->
          <div class="w-full h-[52px] bg-white rounded-2xl border border-slate-300 shadow-2xs px-4 flex items-center gap-3">
            <span class="w-6 h-6 rounded-lg bg-blue-50 text-blue-600 font-mono font-bold text-xs flex items-center justify-center border border-blue-200 shrink-0">
              03
            </span>
            <span class="text-sm font-serif font-bold text-slate-800 tracking-tight whitespace-nowrap">
              STAR 경험 포트폴리오
            </span>
          </div>
        </div>

        <!-- Bottom Info: Single Line Criteria + Privacy Tip -->
        <div class="pt-2 border-t border-slate-200/90 space-y-1 mt-1">
          <div class="text-[11px] text-slate-600 font-medium tracking-tight">
            스킬 지침: <strong class="text-slate-800 font-semibold">필수 항목(STAR)</strong> · <strong class="text-slate-800 font-semibold">수치 무결성</strong> · <strong class="text-slate-800 font-semibold">비즈니스 문체</strong>
          </div>
          <div class="text-[10px] text-slate-400 font-medium flex items-center gap-1.5">
            <ShieldCheck :size="12" class="text-emerald-600 shrink-0" />
            <span>개인정보 및 프로젝트 보안을 위해 비식별화 가상 자료 활용</span>
          </div>
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
  background-color: #60a5fa;
  margin-left: 2px;
  vertical-align: text-bottom;
  animation: cursor-blink 0.85s infinite;
}

/* ── Arrow 1 Animation (Starts immediately upon typing completion, draws for 1.0s) ── */
@keyframes draw-shaft-smooth {
  0% {
    stroke-dashoffset: 30;
    opacity: 0;
  }
  15% {
    opacity: 1;
  }
  100% {
    stroke-dashoffset: 0;
    opacity: 1;
  }
}

@keyframes draw-head-smooth {
  0% {
    stroke-dashoffset: 20;
    opacity: 0;
  }
  100% {
    stroke-dashoffset: 0;
    opacity: 1;
  }
}

.rough-arrow-1-shaft {
  stroke-dasharray: 30;
  stroke-dashoffset: 30;
  animation: draw-shaft-smooth 1.0s cubic-bezier(0.25, 1, 0.5, 1) 0.1s both;
}

.rough-arrow-1-head {
  stroke-dasharray: 20;
  stroke-dashoffset: 20;
  animation: draw-head-smooth 0.6s cubic-bezier(0.25, 1, 0.5, 1) 0.75s both;
}

/* ── Arrow 2 Animation (Starts 1.0s later, draws for 1.0s) ── */
.rough-arrow-2-shaft {
  stroke-dasharray: 30;
  stroke-dashoffset: 30;
  animation: draw-shaft-smooth 1.0s cubic-bezier(0.25, 1, 0.5, 1) 1.1s both;
}

.rough-arrow-2-head {
  stroke-dasharray: 20;
  stroke-dashoffset: 20;
  animation: draw-head-smooth 0.6s cubic-bezier(0.25, 1, 0.5, 1) 1.75s both;
}
</style>
