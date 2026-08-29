<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import {
  FileText,
  Presentation
} from 'lucide-vue-next'

const rootRef = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | null = null

const fullPrompt = `@Documents, 개정된 [2026_복지부_디지털돌봄_정책지침.pdf]를 읽고 우리 기관에 적용할 신규 사업기획서 초안을 DOCX로 작성해줘.
사업 배경, 목적, 대상, 주요 프로그램, 예산, 기대효과를 5대 목차로 정리하고, 정책 원문 수치는 원자료와 대조해줘.

@Presentations, 같은 정책자료와 @Documents가 만든 기획서 내용을 바탕으로 이사회 보고용 핵심 요약 PPTX를 만들어줘.
핵심 내용을 5단계로 쉽게 정리하고, 기획서와 정책자료의 숫자와 근거를 동일하게 유지해줘.`

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
  }, 16)
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
  
  // Highlight @Documents
  text = text.replace(/@Documents/g, '<span class="text-sky-300 font-bold">@Documents</span>')
  // Highlight @Presentations
  text = text.replace(/@Presentations/g, '<span class="text-purple-300 font-bold">@Presentations</span>')
  // Highlight [2026_복지부_디지털돌봄_정책지침.pdf]
  text = text.replace(/\[2026_복지부_디지털돌봄_정책지침\.pdf\]/g, '<span class="text-amber-300 font-bold">[2026_복지부_디지털돌봄_정책지침.pdf]</span>')
  
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
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-sky-950/80 text-sky-300 border border-sky-400/60 flex items-center gap-1.5 shadow-sm">
            <FileText :size="12" class="text-sky-400" />
            <span>@Documents</span>
          </span>
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-purple-950/80 text-purple-300 border border-purple-400/60 flex items-center gap-1.5 shadow-sm">
            <Presentation :size="12" class="text-purple-400" />
            <span>@Presentations</span>
          </span>
        </div>
      </div>
      <span class="text-[11px] text-slate-200 font-medium">
        단일 프롬프트에서 두 플러그인을 지정해 <strong class="text-white">완성형 파일 2종 동시 연계 도출</strong>
      </span>
    </div>

    <!-- ── Main 2-Column Grid (Left: Typewriter Prompt Box, Right: Role Division) ── -->
    <div class="grid grid-cols-12 gap-4 items-stretch h-[275px]">
      <!-- ── Left Column (7 Cols): Pure Typewriter Terminal Box ── -->
      <div class="col-span-7 flex flex-col justify-start bg-slate-950 rounded-2xl border border-slate-800 p-4 shadow-xl relative overflow-hidden">
        <!-- Terminal Header Dot Indicator -->
        <div class="flex items-center gap-1.5 pb-2 border-b border-slate-800/80 mb-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-950/40 border border-rose-500/50"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500/80 border border-amber-400/50"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-950/40 border border-emerald-500/50"></span>
          <span class="text-[9.5px] font-mono text-slate-400 ml-1.5">chatgpt-work-prompt</span>
        </div>

        <!-- Real-time Typewriter Prompt Body with Infinite Blinking Cursor -->
        <div class="font-mono text-[10.5px] leading-relaxed text-slate-200 whitespace-pre-line tracking-tight">
          <span v-html="formattedHtml"></span><span class="cursor-blink"></span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Role Division & Workflow (Apple Dark Glass) ── -->
      <div class="col-span-5 flex flex-col justify-between bg-white/5 rounded-2xl border border-white/12 p-3.5 shadow-xl backdrop-blur-sm">
        <div>
          <span class="text-[12px] font-bold text-white font-serif block mb-2.5">
            두 플러그인의 명확한 역할 분담
          </span>

          <div class="space-y-2.5">
            <!-- Role 1: @Documents -->
            <div class="p-2.5 rounded-xl bg-sky-950/50 border border-sky-400/50 shadow-xs">
              <div class="flex items-center gap-1.5 text-sky-300 font-bold text-[11.5px] mb-1">
                <FileText :size="13" class="text-sky-400 shrink-0" />
                <span>@Documents (문서 작성 플러그인)</span>
              </div>
              <ul class="text-[10.5px] text-white space-y-1 pl-1 font-medium">
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0 mt-1"></span>
                  <span class="text-white">사업 배경·목적·프로그램·예산 5대 체계 기획서 수립</span>
                </li>
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0 mt-1"></span>
                  <span class="text-white">지침서 원문의 통계·단가 수치 정밀 교차 대조</span>
                </li>
              </ul>
            </div>

            <!-- Role 2: @Presentations -->
            <div class="p-2.5 rounded-xl bg-purple-950/50 border border-purple-400/50 shadow-xs">
              <div class="flex items-center gap-1.5 text-purple-300 font-bold text-[11.5px] mb-1">
                <Presentation :size="13" class="text-purple-400 shrink-0" />
                <span>@Presentations (슬라이드 요약 플러그인)</span>
              </div>
              <ul class="text-[10.5px] text-white space-y-1 pl-1 font-medium">
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 shrink-0 mt-1"></span>
                  <span class="text-white">기획서 핵심 내용을 5단계 슬라이드로 요약 변환</span>
                </li>
                <li class="flex items-start gap-1.5 leading-snug">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 shrink-0 mt-1"></span>
                  <span class="text-white">기획서와 정책자료의 숫자 및 근거를 동일하게 유지</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Footer Takeaway -->
        <div class="pt-2 border-t border-white/10 flex items-start gap-1.5 text-[10.5px] text-slate-100 font-medium">
          <span class="text-amber-400 shrink-0"><span class="i-carbon:idea text-amber-300"></span></span>
          <span><strong>실무 포인트</strong>: 한 프롬프트에서 두 도구를 함께 호출하여 기획서와 보고 슬라이드의 수치 오차 0% 달성</span>
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
  animation: cursor-blink 0.9s infinite;
}
</style>
