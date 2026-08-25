<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'
import {
  Clock,
  Search,
  FileCode,
  Terminal,
  CheckCircle2,
  Sparkles,
  ChevronRight,
  ChevronDown,
  Loader2,
  Zap,
  ArrowUp,
  Plus,
  Copy,
  ThumbsUp,
  ThumbsDown,
  FileSpreadsheet
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const rootRef = ref<HTMLElement | null>(null)
let observer: IntersectionObserver | null = null

const fullPrompt = '2026년 목포종합사회복지관 취약계층 아동 방과후 특별돌봄 사업계획서 작성 및 세출 예산안 비교 분석해줘.'

// Live execution progression state (0 to 5)
const streamStep = ref(0)
const liveAdditions = ref(0)
const liveTimerSec = ref(1)
const workingDots = ref('...')

// Interactive A4 artifact modal state
const isModalOpen = ref(false)

let timerInterval: any = null
let dotsInterval: any = null
let stepTimers: any[] = []

function clearAllTimers() {
  clearInterval(timerInterval)
  clearInterval(dotsInterval)
  stepTimers.forEach(t => clearTimeout(t))
  stepTimers = []
}

function startAgentExecution() {
  clearAllTimers()
  streamStep.value = 1
  liveAdditions.value = 0
  liveTimerSec.value = 1
  isModalOpen.value = false

  // Timer counts up while active
  timerInterval = setInterval(() => {
    liveTimerSec.value++
  }, 1000)

  dotsInterval = setInterval(() => {
    if (workingDots.value === '...') workingDots.value = '.'
    else if (workingDots.value === '.') workingDots.value = '..'
    else workingDots.value = '...'
  }, 350)

  // Step 2: Deep Thought & Planning (Starts at 1.8s)
  stepTimers.push(setTimeout(() => {
    streamStep.value = 2
  }, 1800))

  // Step 3: Run Command & Tool Call (Starts at 3.6s)
  stepTimers.push(setTimeout(() => {
    streamStep.value = 3
  }, 3600))

  // Step 4: File Edit with smooth progressive line diff counting (Starts at 5.4s)
  stepTimers.push(setTimeout(() => {
    streamStep.value = 4
    let diff = 0
    const diffTimer = setInterval(() => {
      diff += 24
      if (diff >= 248) {
        liveAdditions.value = 248
        clearInterval(diffTimer)
      } else {
        liveAdditions.value = diff
      }
    }, 45)
  }, 5400))

  // Step 5: Artifact Created & Timer STOPS! (Starts at 7.2s)
  stepTimers.push(setTimeout(() => {
    streamStep.value = 5
    clearInterval(timerInterval)
    clearInterval(dotsInterval)
  }, 7200))
}

function showCompletedState() {
  clearAllTimers()
  streamStep.value = 5
  liveAdditions.value = 248
  liveTimerSec.value = 8
}

onMounted(() => {
  if (rootRef.value) {
    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          if (props.stage === 0) {
            startAgentExecution()
          } else if (props.stage === 1) {
            showCompletedState()
          }
        } else {
          clearAllTimers()
        }
      })
    }, { threshold: 0.15 })
    observer.observe(rootRef.value)
  }
})

onUnmounted(() => {
  clearAllTimers()
  if (observer) observer.disconnect()
})

watch(() => props.stage, (newStage) => {
  if (newStage === 0) {
    startAgentExecution()
    isModalOpen.value = false
  } else if (newStage === 1) {
    // Stage 1: Ensure completed state is shown
    showCompletedState()
    isModalOpen.value = false
  } else if (newStage >= 2) {
    // Stage 2: Artifact Modal Opens directly!
    showCompletedState()
    isModalOpen.value = true
  }
})
</script>

<template>
  <div ref="rootRef" class="w-full flex flex-col items-center justify-center select-none my-auto h-[415px] relative font-sans">
    <!-- Antigravity Native Dark Chat Interface (Expanded Zero-Clipping Layout: ~400px) -->
    <div class="w-full h-[400px] rounded-2xl bg-[#0D0E12] border border-[#232733] shadow-2xl p-3.5 px-4.5 flex flex-col justify-between z-10 text-[#C5C9D5] relative overflow-hidden">
      <!-- 1. Top Trajectory Header -->
      <div class="flex items-center justify-between pb-1.5 border-b border-[#1E222D] shrink-0 text-xs font-mono transition-all duration-500 h-[26px]">
        <div class="flex items-center gap-2">
          <div class="flex items-center gap-1.5 text-slate-400 hover:text-slate-200 cursor-pointer">
            <Clock :size="12" class="text-indigo-400" />
            <!-- Exact logic: Working for during execution -> Worked for upon completion! -->
            <span class="font-bold text-[#E2E5EE] text-[11px]">
              {{ streamStep < 5 ? 'Working for' : 'Worked for' }} {{ Math.floor(liveTimerSec / 60) }}m {{ liveTimerSec % 60 }}s
            </span>
            <ChevronDown :size="11" class="text-slate-500" />
          </div>
          <span class="text-slate-600 text-[10px]">|</span>
          <span class="text-indigo-400 font-bold flex items-center gap-1.5 text-[11px]">
            <span class="w-1.5 h-1.5 rounded-full" :class="streamStep < 5 ? 'bg-indigo-400 animate-ping' : 'bg-emerald-400'"></span>
            <span>{{ streamStep < 5 ? 'AUTONOMOUS EXECUTION' : 'COMPLETED (5 STAGES)' }}</span>
          </span>
        </div>

        <div class="flex items-center gap-1.5 text-[10px]">
          <span class="px-2 py-0.2 rounded-md bg-[#181B24] border border-[#2A2E3D] text-slate-300 font-bold flex items-center gap-1">
            <Zap :size="10" class="text-amber-400" />
            <span>Agent Engine</span>
          </span>
        </div>
      </div>

      <!-- 2. Chat Feed Area (Comfortable spacing, zero clipping guaranteed) -->
      <div class="flex-1 py-1.5 space-y-1.5 overflow-hidden text-xs flex flex-col justify-start">
        <!-- User Prompt Message Card (Always visible) -->
        <div class="p-1.5 px-3 rounded-lg bg-[#141720] border border-[#232838] flex items-start gap-2 shadow-xs animate-in fade-in duration-300 shrink-0">
          <div class="w-4 h-4 rounded bg-blue-600 flex items-center justify-center text-white text-[9px] font-bold shrink-0 mt-0.5">
            Q
          </div>
          <div class="text-[11.5px] font-sans font-medium text-slate-100 leading-snug">
            {{ fullPrompt }}
          </div>
        </div>

        <!-- Trajectory Log 1: Search & Exploration -->
        <div
          v-if="streamStep >= 1"
          class="flex items-center justify-between px-2.5 py-0.5 rounded-md border text-[10.5px] font-mono transition-all duration-300 bg-[#141720]/80 border-[#232838] text-slate-200 shrink-0"
        >
          <div class="flex items-center gap-2">
            <CheckCircle2 v-if="streamStep >= 2" :size="11" class="text-emerald-400 shrink-0" />
            <Loader2 v-else :size="11" class="text-blue-400 animate-spin shrink-0" />
            <span class="font-bold">Explored 2 files, 3 searches</span>
            <span class="text-slate-400 font-sans text-[10px] truncate max-w-[420px]">➔ view_file("목포복지관_운영규정.pdf")</span>
          </div>
          <span v-if="streamStep >= 2" class="text-[9px] text-emerald-400 font-bold">Done</span>
          <ChevronRight v-else :size="11" class="text-slate-500" />
        </div>

        <!-- Trajectory Log 2: Thought Log -->
        <div
          v-if="streamStep >= 2"
          class="flex items-center justify-between px-2.5 py-0.5 rounded-md border text-[10.5px] font-mono transition-all duration-300 bg-[#141720]/80 border-[#232838] text-slate-200 shrink-0"
        >
          <div class="flex items-center gap-2">
            <CheckCircle2 v-if="streamStep >= 3" :size="11" class="text-emerald-400 shrink-0" />
            <Loader2 v-else :size="11" class="text-amber-400 animate-spin shrink-0" />
            <span class="text-amber-300 font-bold">Thought for 12s</span>
            <span class="text-slate-300 font-sans text-[10px] truncate max-w-[420px]">➔ 제4조 4.2억 조항 확인, 2025 실적 3.5억과 대조 완료</span>
          </div>
          <span v-if="streamStep >= 3" class="text-[9px] text-emerald-400 font-bold">Planned</span>
          <ChevronRight v-else :size="11" class="text-slate-500" />
        </div>

        <!-- Trajectory Log 3: Command Execution Log -->
        <div
          v-if="streamStep >= 3"
          class="flex items-center justify-between px-2.5 py-0.5 rounded-md border text-[10.5px] font-mono transition-all duration-300 bg-[#141720]/90 border-purple-500/30 text-slate-200 shrink-0"
        >
          <div class="flex items-center gap-2">
            <CheckCircle2 v-if="streamStep >= 4" :size="11" class="text-emerald-400 shrink-0" />
            <Loader2 v-else :size="11" class="text-purple-400 animate-spin shrink-0" />
            <span class="text-purple-300">Ran command:</span>
            <span class="text-slate-300 font-mono text-[9.5px] truncate max-w-[390px]">python calc_growth.py --y2026 420000000 --y2025 350000000</span>
          </div>
          <span v-if="streamStep >= 4" class="text-[9px] text-emerald-400 font-bold font-mono">+20.0% (OK)</span>
          <ChevronRight v-else :size="11" class="text-slate-500" />
        </div>

        <!-- Trajectory Log 4: File Edit with Proper Font Kerning -->
        <div
          v-if="streamStep >= 4"
          class="flex items-center justify-between px-2.5 py-0.5 rounded-md border text-[10.5px] transition-all duration-300 bg-[#141720] border-indigo-500/40 text-slate-200 shrink-0"
        >
          <div class="flex items-center gap-2 font-sans">
            <CheckCircle2 v-if="streamStep >= 5" :size="11" class="text-emerald-400 shrink-0" />
            <Loader2 v-else :size="11" class="text-indigo-400 animate-spin shrink-0" />
            <span class="text-slate-400 text-[10px]">Edited</span>
            <span class="font-bold text-slate-100 tracking-tight">2026_아동돌봄_사업계획서_최종.md</span>
            <!-- Live diffs incrementing -->
            <span class="text-emerald-400 font-bold font-mono text-[9.5px] bg-emerald-950/60 px-1 rounded border border-emerald-500/30">
              +{{ liveAdditions }}
            </span>
            <span class="text-rose-400 font-bold font-mono text-[9.5px] bg-rose-950/60 px-1 rounded border border-rose-500/30">
              -12
            </span>
          </div>
          <span class="text-[9px] font-mono text-indigo-400 bg-indigo-950/80 px-1.5 py-0.2 rounded border border-indigo-500/30">
            {{ streamStep >= 5 ? 'SAVED' : 'WRITING...' }}
          </span>
        </div>

        <!-- Active Working... Pill (Shown right beneath the active step) -->
        <div
          v-if="streamStep > 0 && streamStep < 5"
          class="p-1 px-3 rounded-lg bg-indigo-950/60 border border-indigo-500/50 shadow-xs flex items-center justify-between text-xs animate-pulse shrink-0"
        >
          <div class="flex items-center gap-2">
            <Loader2 :size="12" class="animate-spin text-indigo-400 shrink-0" />
            <span class="font-bold text-indigo-300 font-mono text-[11px]">Working{{ workingDots }}</span>
            <span class="text-slate-300 text-[10px] font-sans">
              {{
                streamStep === 1 ? '지침서 및 규정 PDF 문서 색인 탐색 중...' :
                streamStep === 2 ? '다단계 실행 계획 수립 및 팩트 대조 중...' :
                streamStep === 3 ? '파이썬 연산 도구 호출 및 예산 증감률 계산 중...' :
                '2026 사업계획서 최종본 마크다운 생성 및 저장 중...'
              }}
            </span>
          </div>
          <span class="px-1.5 py-0.2 rounded bg-indigo-600 text-white text-[8.5px] font-mono font-bold">
            AGENT
          </span>
        </div>

        <!-- ── ASSISTANT COMPLETION MESSAGE & REALISTIC FOOTER BAR (When streamStep === 5) ── -->
        <div
          v-if="streamStep >= 5"
          class="space-y-1 pt-1 animate-in fade-in duration-500 shrink-0 mb-1"
        >
          <!-- Assistant Completion Response Box with Review Button on the EXACT RIGHT of the line -->
          <div class="flex items-center justify-between gap-3 pr-1">
            <div class="text-[11.5px] font-sans text-slate-100 font-medium leading-snug">
              목포종합사회복지관 2026년도 아동 방과후 특별돌봄 사업계획서 작성을 완료하였습니다! 🚀
            </div>

            <!-- Review / Open Document Button placed ON THE RIGHT of the completion line -->
            <button
              @click="isModalOpen = true"
              class="flex items-center gap-1.5 text-[10.5px] font-bold text-white bg-indigo-600 hover:bg-indigo-500 border border-indigo-400 px-3 py-0.5 rounded-lg shadow-md cursor-pointer transition-all duration-300 shrink-0 mr-1"
              title="클릭하여 실물 사업계획서 열람"
            >
              <FileSpreadsheet :size="12" />
              <span>Review (문서 열람 ↗)</span>
            </button>
          </div>

          <!-- Diff Row (1 file changed +248 -12) -->
          <div class="flex items-center gap-1.5 text-[10.5px] font-mono text-slate-400 py-0.5">
            <span>1 file changed</span>
            <span class="text-emerald-400 font-bold">+248</span>
            <span class="text-rose-400 font-bold">-12</span>
            <ChevronRight :size="11" class="text-slate-500" />
          </div>

          <!-- Timestamp & Action Icons: Copy, Thumbs Up, Thumbs Down (Clear vertical height, zero clipping) -->
          <div class="h-[18px] flex items-center justify-between text-[10.5px] text-slate-500 pt-0.5 pb-0.5 pr-2 mb-0.5">
            <span>오후 11:43</span>
            <div class="flex items-center gap-3 text-slate-400 mr-1">
              <Copy :size="13" class="hover:text-slate-200 cursor-pointer transition-colors" title="복사" />
              <ThumbsUp :size="13" class="hover:text-slate-200 cursor-pointer transition-colors" title="좋아요" />
              <ThumbsDown :size="13" class="hover:text-slate-200 cursor-pointer transition-colors" title="싫어요" />
            </div>
          </div>
        </div>
      </div>

      <!-- 3. Bottom Native Antigravity Prompt Input Bar (Click to replay anytime) -->
      <div
        @click="startAgentExecution"
        class="pt-1.5 border-t border-[#1E222D] shrink-0 mt-0.5 cursor-pointer"
        title="클릭하여 작업 시뮬레이션 다시 실행"
      >
        <div class="rounded-xl bg-[#14161E] border border-[#2B2F3D] p-2 flex flex-col justify-between shadow-inner">
          <div class="text-[11.5px] font-sans font-medium text-slate-100 min-h-[20px] flex items-center">
            <span class="text-slate-500 select-none text-[11px]">Ask anything, @ to mention, / for actions</span>
          </div>

          <!-- Bottom Control Bar: Model Tag + Send Button -->
          <div class="flex items-center justify-between pt-1 text-[10px] text-slate-400 font-mono">
            <div class="flex items-center gap-1.5">
              <span class="flex items-center gap-1 px-2 py-0.2 rounded-md bg-[#1C1F2B] border border-[#2B2F3E] text-slate-300 font-bold hover:bg-[#252938] cursor-pointer text-[9.5px]">
                <Plus :size="10" />
                <span>Gemini 3.7 Flash High</span>
                <ChevronDown :size="10" />
              </span>
            </div>

            <!-- Send Button -->
            <div class="w-5.5 h-5.5 rounded-full flex items-center justify-center bg-blue-600 text-white shadow-xs">
              <ArrowUp :size="12" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ── FULL-SCREEN BLURRED BACKDROP WITH CENTERED 9:14 ZERO-SCROLL PROPOSAL DOCUMENT ── -->
    <div
      v-if="isModalOpen"
      @click.self="isModalOpen = false"
      class="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-3 animate-in fade-in zoom-in-95 duration-700 ease-out cursor-pointer"
    >
      <!-- Official Crisp A4 Proposal Document (Aspect Ratio ~9:13, Perfectly fitted without any clipping or scroll) -->
      <div
        @click.stop
        class="w-[390px] h-[420px] bg-white rounded-lg shadow-2xl border-2 border-slate-300 p-3.5 px-4.5 flex flex-col justify-between text-slate-900 select-none overflow-hidden ring-4 ring-black/30 cursor-default"
      >
        <!-- Top Official Document Header -->
        <div class="text-center pb-1.5 border-b-2 border-slate-900 shrink-0">
          <div class="flex items-center justify-between text-[8.5px] font-mono text-slate-500 mb-0.5">
            <span>[문서번호: 2026-기획-042]</span>
            <span class="text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.2 rounded border border-emerald-300">
              ✓ AI 에이전트 자율 완성본
            </span>
          </div>
          <h2 class="text-sm md:text-[14.5px] font-serif font-black text-slate-900 tracking-tight leading-tight">
            2026년도 취약계층 아동 방과후 특별돌봄 사업계획서
          </h2>
          <div class="text-[9px] font-sans text-slate-600 mt-0.5">
            목포종합사회복지관 아동복지기획팀
          </div>
        </div>

        <!-- Document Body Sections (Zero-Scroll Formatted Layout) -->
        <div class="flex-1 py-1.5 space-y-1.5 text-[10px] font-sans flex flex-col justify-between">
          <!-- Section 1: Summary Table -->
          <div class="space-y-0.5">
            <div class="font-bold text-slate-800 flex items-center gap-1 text-[10.5px]">
              <span class="w-1 h-1 bg-indigo-600 rounded-full inline-block"></span>
              <span>1. 사업 개요</span>
            </div>
            <table class="w-full text-[9px] border-collapse border border-slate-300">
              <tbody>
                <tr>
                  <td class="bg-slate-100 p-0.5 px-1 font-bold border border-slate-300 w-16 text-slate-700">사 업 명</td>
                  <td class="p-0.5 px-1 border border-slate-300 text-slate-800 font-medium">2026년 목포 꿈자람 아동 방과후 돌봄 교실</td>
                </tr>
                <tr>
                  <td class="bg-slate-100 p-0.5 px-1 font-bold border border-slate-300 text-slate-700">사업기간</td>
                  <td class="p-0.5 px-1 border border-slate-300 text-slate-800">2026. 03. 01 ~ 2026. 12. 31 (10개월)</td>
                </tr>
                <tr>
                  <td class="bg-slate-100 p-0.5 px-1 font-bold border border-slate-300 text-slate-700">지원대상</td>
                  <td class="p-0.5 px-1 border border-slate-300 text-slate-800">목포시 관내 돌봄 취약계층 아동 20명</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Section 2: Grounded Regulation -->
          <div class="space-y-0.5">
            <div class="font-bold text-slate-800 flex items-center gap-1 text-[10.5px]">
              <span class="w-1 h-1 bg-indigo-600 rounded-full inline-block"></span>
              <span>2. 추진 근거 및 규정</span>
            </div>
            <div class="p-1 rounded bg-slate-50 border border-slate-200 text-[9px] text-slate-700 leading-snug">
              • <strong>목포종합사회복지관 운영규정 제4조 (특별지원사업)</strong> 제2항 규정 명시 준수
            </div>
          </div>

          <!-- Section 3: Budget Analysis (Computed by Agent) -->
          <div class="space-y-0.5">
            <div class="font-bold text-slate-800 flex items-center justify-between text-[10.5px]">
              <div class="flex items-center gap-1">
                <span class="w-1 h-1 bg-indigo-600 rounded-full inline-block"></span>
                <span>3. 세출 예산 비교 분석 (Tool 연산)</span>
              </div>
              <span class="text-[8.5px] font-mono text-indigo-600 font-bold">자율 연산 완료</span>
            </div>
            <table class="w-full text-[9px] text-center border-collapse border border-slate-300">
              <thead>
                <tr class="bg-slate-100 text-slate-700 font-bold">
                  <th class="p-0.5 border border-slate-300">구분</th>
                  <th class="p-0.5 border border-slate-300">2025년 실적</th>
                  <th class="p-0.5 border border-slate-300">2026년 확정</th>
                  <th class="p-0.5 border border-slate-300 text-indigo-700">증감률</th>
                </tr>
              </thead>
              <tbody class="text-slate-800 font-medium">
                <tr>
                  <td class="p-0.5 border border-slate-300 font-bold">방과후 돌봄</td>
                  <td class="p-0.5 border border-slate-300">350,000,000원</td>
                  <td class="p-0.5 border border-slate-300 font-bold text-slate-900">420,000,000원</td>
                  <td class="p-0.5 border border-slate-300 font-bold text-indigo-700 bg-indigo-50">+20.0% 증액</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Official Bottom Footer & Official Center Seal -->
        <div class="pt-1.5 border-t-2 border-slate-900 flex items-center justify-between shrink-0">
          <div class="text-[9px] font-serif font-bold text-slate-700">
            2026년 2월 22일
          </div>

          <!-- Official Center Signature with Seal -->
          <div class="flex items-center gap-1.5 relative">
            <span class="font-serif font-black text-xs text-slate-900 tracking-wider">
              목포종합사회복지관장
            </span>
            <!-- Red Official Seal Stamp (직인) -->
            <div class="w-6 h-6 rounded-full border-2 border-rose-600 flex items-center justify-center text-rose-600 font-serif font-black text-[8px] rotate-12 shadow-xs">
              직인
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
