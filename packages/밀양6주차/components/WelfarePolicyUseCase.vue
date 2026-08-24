<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'
import {
  FileText,
  Presentation
} from 'lucide-vue-next'

const fullPrompt = `@Documents, 첨부된 [목표기업_신입채용공고_및_직무가이드.pdf]를 읽고 내가 제출할 실무 프로젝트 기획서 초안을 DOCX로 작성해줘.
프로젝트 배경, 나의 기여도, 문제 해결 과정(STAR), 기술 스택, 정량적 성과를 5대 목차로 정리하고, 내 경험 DB와 대조해줘.

@Presentations, 같은 기획서 내용을 바탕으로 1차 면접 발표용 5슬라이드 핵심 피치덱 PPTX를 만들어줘.
프로젝트 문제 해결 과정과 성과를 임팩트 있게 정리하고, 기획서의 수치와 데이터를 100% 동일하게 유지해줘.`

const typedText = ref('')
let timer: any = null

onMounted(() => {
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
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})

// Highlight keywords dynamically in typed text
const formattedHtml = computed(() => {
  let text = typedText.value
  // Escape HTML
  text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  
  // Highlight @Documents
  text = text.replace(/@Documents/g, '<span class="text-blue-400 font-bold">@Documents</span>')
  // Highlight @Presentations
  text = text.replace(/@Presentations/g, '<span class="text-purple-400 font-bold">@Presentations</span>')
  // Highlight [목표기업_신입채용공고_및_직무가이드.pdf]
  text = text.replace(/\[목표기업_신입채용공고_및_직무가이드\.pdf\]/g, '<span class="text-amber-300 font-bold">[목표기업_신입채용공고_및_직무가이드.pdf]</span>')
  
  return text
})
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[330px] my-auto">
    <!-- ── Top: Features & Plugins Tag Bar ── -->
    <!-- ── Top: Features & Plugins Tag Bar ── -->
    <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200/90 shadow-2xs mb-2">
      <div class="flex items-center gap-2 shrink-0">
        <span class="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">
          도구 및 플러그인
        </span>
        <div class="flex items-center gap-1.5">
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-blue-100 text-blue-900 border border-blue-200 flex items-center gap-1 whitespace-nowrap">
            <FileText :size="11" class="text-blue-600" />
            <span>@Documents</span>
          </span>
          <span class="px-2.5 py-0.5 rounded-full text-[10.5px] font-mono font-bold bg-purple-100 text-purple-900 border border-purple-200 flex items-center gap-1 whitespace-nowrap">
            <Presentation :size="11" class="text-purple-600" />
            <span>@Presentations</span>
          </span>
        </div>
      </div>
      <span class="text-[10.5px] text-slate-500 font-medium whitespace-nowrap pl-2">
        단일 프롬프트에서 두 플러그인을 지정해 <strong>완성형 포트폴리오 & 발표자료 동시 도출</strong>
      </span>
    </div>

    <!-- ── Main 2-Column Grid (Left: Pure Typewriter Prompt Box, Right: Role Division) ── -->
    <div class="grid grid-cols-12 gap-4 items-stretch h-[275px]">
      <!-- ── Left Column (7 Cols): Pure Typewriter Terminal Box (Zero Clutter) ── -->
      <div class="col-span-7 flex flex-col justify-start bg-slate-950 rounded-2xl border border-slate-800 p-4 shadow-xl relative overflow-hidden">
        <!-- Terminal Header Dot Indicator -->
        <div class="flex items-center gap-1.5 pb-2 border-b border-slate-800/80 mb-2.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-500/80"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500/80"></span>
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500/80"></span>
          <span class="text-[9.5px] font-mono text-slate-500 ml-1.5">job-portfolio-prompt</span>
        </div>

        <!-- Real-time Typewriter Prompt Body with Infinite Blinking Cursor -->
        <div class="font-mono text-[10.5px] leading-relaxed text-slate-200 whitespace-pre-line tracking-tight">
          <span v-html="formattedHtml"></span><span class="cursor-blink"></span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Role Division & Workflow ── -->
      <div class="col-span-5 flex flex-col justify-between bg-white rounded-2xl border border-slate-200/90 p-3.5 shadow-2xs">
        <div>
          <span class="text-[11px] font-bold text-slate-900 font-serif block mb-2.5">
            두 플러그인의 명확한 역할 분담
          </span>

          <div class="space-y-2.5">
            <!-- Role 1: @Documents -->
            <div class="p-2.5 rounded-xl bg-blue-50/50 border border-blue-200/70 shadow-2xs">
              <div class="flex items-center gap-1.5 text-blue-900 font-bold text-[10.5px] mb-1">
                <FileText :size="13" class="text-blue-600 shrink-0" />
                <span>@Documents (문서 작성 플러그인)</span>
              </div>
              <ul class="text-[9.5px] text-slate-600 space-y-0.5 pl-1">
                <li>• 프로젝트 배경·기여도·문제해결(STAR)·성과 5대 체계 기획서 수립</li>
                <li>• 내 경험 DB 원문의 프로젝트 수치 정밀 교차 대조</li>
              </ul>
            </div>

            <!-- Role 2: @Presentations -->
            <div class="p-2.5 rounded-xl bg-purple-50/50 border border-purple-200/70 shadow-2xs">
              <div class="flex items-center gap-1.5 text-purple-900 font-bold text-[10.5px] mb-1">
                <Presentation :size="13" class="text-purple-600 shrink-0" />
                <span>@Presentations (슬라이드 요약 플러그인)</span>
              </div>
              <ul class="text-[9.5px] text-slate-600 space-y-0.5 pl-1">
                <li>• 기획서 핵심 내용을 5단계 면접 피치덱 슬라이드로 요약 변환</li>
                <li>• 기획서와 피치덱의 수치 및 근거를 100% 동일하게 유지</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Footer Takeaway -->
        <div class="pt-1.5 border-t border-slate-100 text-[9.5px] text-slate-600 font-medium">
          💡 <strong>실무 포인트</strong>: 한 프롬프트에서 두 도구를 함께 호출하여 기획서와 면접 피치덱의 수치 오차 0% 달성
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
</style>
