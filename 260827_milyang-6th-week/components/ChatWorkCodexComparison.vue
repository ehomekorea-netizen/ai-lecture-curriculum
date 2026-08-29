<script setup lang="ts">
import { computed } from 'vue'
import {
  MessageSquare,
  Briefcase,
  Terminal,
  Zap,
  Lock
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const currentStage = computed(() => props.stage ?? 0)

// When clicks reach 11, unlock Codex smoothly with GPU acceleration (zero reflow lag)
const isCodexVisible = computed(() => currentStage.value >= 11)

export interface ComparisonRow {
  category: string
  chat: string
  work: string
  codex: string
}

const rows: ComparisonRow[] = [
  {
    category: '파일 접근',
    chat: '❌ 로컬 파일 직접 접근 불가 (대화창 전용)',
    work: '⭕ 허용한 로컬 컴퓨터 폴더 파일 직접 읽기·쓰기',
    codex: '⭕ 프로젝트 전체 폴더 및 시스템 코드 직접 제어'
  },
  {
    category: '주요 목적',
    chat: '사고 정리, 브레인스토밍, 프롬프트 질의',
    work: '내 프로젝트 원자료를 종합하여 완성형 포트폴리오 문서 제작',
    codex: '대량 데이터 전처리 및 기술적 파이썬 스크립트 실행'
  },
  {
    category: '최종 산출물',
    chat: '채팅창 텍스트 답변 (수동 복사 필요)',
    work: '편집 가능한 완성형 표준 DOCX · PPTX 파일',
    codex: '터미널 실행 로그, 가공 CSV, 소스코드 파일'
  },
  {
    category: '보안 권한',
    chat: '별도 권한 불필요 (채팅창 안에서만 작동)',
    work: '최소 권한(Least Privilege) 원칙 (지정 폴더만)',
    codex: '로컬 터미널 및 시스템 파일 전체 실행 권한'
  },
  {
    category: '실무 대상',
    chat: '본격 작성 전 취업 아이디어 발상 및 초안 구상',
    work: '취업준비생의 완성형 포트폴리오 & 직무 문서 제작 (수강생 실습 핵심)',
    codex: '데이터 분석가, 개발자 및 엔지니어링 작업'
  }
]

// ── Turn-by-Turn Stage Logic ──
// Phase 1 (Clicks 1 ~ 10): Chat (2*idx + 1) -> Work (2*idx + 2)
function isChatActive(idx: number) {
  return currentStage.value >= 2 * idx + 1
}

function isWorkActive(idx: number) {
  return currentStage.value >= 2 * idx + 2
}

// Phase 2 (Clicks 11 ~ 15): Codex Underlines (11, 12, 13, 14, 15)
function isCodexUnderlineActive(idx: number) {
  return currentStage.value >= 11 + idx
}
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left py-0.5">
    <!-- GPU-Accelerated 4-Column Table Frame (Zero Reflow Lag, 60fps Butter Smooth) -->
    <div class="w-full bg-white rounded-xl overflow-hidden border border-slate-300 shadow-xs mb-2">
      <!-- ── Table Header (Fixed 4-Grid: 16% / 28% / 28% / 28%) ── -->
      <div class="flex items-stretch border-b border-slate-300 h-[40px]">
        <!-- 1. Category Column (16%) -->
        <div class="w-[16%] p-2.5 px-3.5 flex items-center font-bold text-slate-900 bg-[#E8E2D8] shrink-0 border-r border-[#DDD5C7] text-[12.5px] font-serif">
          구분
        </div>

        <!-- 2. Chat Column (28%) -->
        <div class="w-[28%] p-2.5 px-3.5 flex items-center gap-1.5 bg-[#E0F2FE] text-sky-950 font-bold border-r border-sky-200 text-[12.5px] shrink-0">
          <MessageSquare :size="15" class="text-sky-700 shrink-0" />
          <span>Chat (단순 대화 / 탐색)</span>
        </div>

        <!-- 3. ChatGPT Work Column (28%) -->
        <div class="w-[28%] p-2.5 px-3.5 flex items-center gap-1.5 border-r border-blue-300 text-[12.5px] shrink-0 bg-[#BFDBFE] text-blue-950 font-bold border-l border-blue-300">
          <Briefcase :size="15" class="text-blue-700 shrink-0" />
          <span>ChatGPT Work (실무 산출물)</span>
        </div>

        <!-- 4. Codex Column (28% GPU-Accelerated Smooth Reveal) -->
        <div
          class="w-[28%] p-2.5 px-3.5 flex items-center gap-1.5 bg-[#F3E8FF] text-purple-950 font-bold border-l border-purple-300 text-[12.5px] shrink-0 transition-all duration-500 ease-out"
          :class="isCodexVisible ? 'opacity-100 translate-x-0' : 'opacity-20 translate-x-1 grayscale'"
        >
          <Terminal :size="15" :class="isCodexVisible ? 'text-purple-700' : 'text-slate-400'" class="shrink-0" />
          <span>Codex (개발 & 대량 실행)</span>
        </div>
      </div>

      <!-- ── Table Body Rows (4-Column Fixed Grid with Zero Layout Shift) ── -->
      <div class="divide-y divide-slate-200/80 text-[12px]">
        <div
          v-for="(row, idx) in rows"
          :key="row.category"
          class="flex items-stretch h-[44px] transition-colors duration-300"
          :class="[
            (isChatActive(idx) || isWorkActive(idx) || isCodexUnderlineActive(idx))
              ? 'bg-blue-50/15'
              : idx % 2 === 1 ? 'bg-slate-50/40' : 'bg-white'
          ]"
        >
          <!-- Cell 1: Category (16%) -->
          <div class="w-[16%] p-2 px-3.5 font-bold text-slate-900 bg-[#FAF8F4] flex items-center font-serif shrink-0 border-r border-[#E7E0D4]">
            {{ row.category }}
          </div>

          <!-- Cell 2: Chat (28%, Sky Highlighter) -->
          <div class="w-[28%] p-2 px-3 text-slate-700 bg-white/95 font-normal flex items-center leading-snug break-keep shrink-0 border-r border-slate-200/70">
            <div class="inline-flex items-center min-h-[26px]">
              <span
                class="v-mark-highlighter v-mark-sky transition-all duration-400 inline-block"
                :class="{ 'v-mark-active': isChatActive(idx) }"
              >
                {{ row.chat }}
              </span>
            </div>
          </div>

          <!-- Cell 3: ChatGPT Work (28%, Blue Highlighter) -->
          <div class="w-[28%] p-2 px-3 font-medium flex items-center leading-snug break-keep shrink-0 border-r border-slate-200/70 bg-blue-50/35 border-l border-blue-200/80">
            <div class="inline-flex items-center min-h-[26px]">
              <span
                class="v-mark-highlighter v-mark-blue transition-all duration-400 inline-block"
                :class="{ 'v-mark-active': isWorkActive(idx) }"
              >
                {{ row.work }}
              </span>
            </div>
          </div>

          <!-- Cell 4: Codex (28%, GPU Smooth Unlock & Underline) -->
          <div
            class="w-[28%] p-2 px-3 flex items-center leading-snug break-keep shrink-0 bg-purple-50/25 border-l border-purple-200/80 transition-all duration-500 ease-out"
            :class="isCodexVisible ? 'opacity-100 translate-x-0' : 'opacity-25 translate-x-1'"
          >
            <div class="inline-flex items-center min-h-[26px]">
              <span
                class="codex-underline transition-all duration-400 inline-block"
                :class="{ 'codex-underline-active': isCodexUnderlineActive(idx) }"
              >
                {{ row.codex }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Quote Box (Smooth Dynamic Takeaway) -->
    <div class="slide-footer quote-box text-xs mt-1 font-medium relative overflow-hidden min-h-[42px] flex items-center">
      <transition name="quote-fade" mode="out-in">
        <div v-if="!isCodexVisible" key="quote-chat" class="w-full">
          🎯 <strong>핵심 공식</strong>: Chat이 <strong>"생각을 정리하는 대화 상대"</strong>라면, Work는 <strong>"내 컴퓨터의 프로젝트 자료를 직접 읽고 완성형 포트폴리오를 만들어주는 전담 비서"</strong>입니다.
        </div>
        <div v-else key="quote-codex" class="w-full text-purple-950">
          ⚡ <strong>3대 환경 최종 정리</strong>: 일반 대화는 <strong>Chat</strong>, 포트폴리오 문서 제작은 <strong>Work</strong>, 대량 데이터 전처리·코딩 자동화는 <strong>Codex</strong>로 역할이 완벽히 분담됩니다.
        </div>
      </transition>
    </div>
  </div>
</template>

<style scoped>
/* ── Organic v-mark Highlighter Pen Stroke Effects ── */
.v-mark-highlighter {
  position: relative;
  display: inline-block;
  padding: 1px 5px;
  border-radius: 3px;
  background-size: 0% 100%;
  background-repeat: no-repeat;
  background-position: left center;
  transition: background-size 0.45s cubic-bezier(0.22, 1, 0.36, 1), color 0.3s ease, font-weight 0.3s ease;
}

/* 1. Chat Sky Highlighter (v-mark.sky) */
.v-mark-sky {
  background-image: linear-gradient(to right, rgba(56, 189, 248, 0.32), rgba(125, 211, 252, 0.42));
  color: #334155;
}
.v-mark-sky.v-mark-active {
  background-size: 100% 100%;
  color: #0369A1;
  font-weight: 700;
  border-bottom: 2px solid rgba(56, 189, 248, 0.75);
}

/* 2. Work Sapphire Blue Highlighter (v-mark.blue) */
.v-mark-blue {
  background-image: linear-gradient(to right, rgba(59, 130, 246, 0.3), rgba(147, 197, 253, 0.42));
  color: #1E3A8A;
}
.v-mark-blue.v-mark-active {
  background-size: 100% 100%;
  color: #1D4ED8;
  font-weight: 800;
  border-bottom: 2px solid rgba(59, 130, 246, 0.85);
}

/* 3. Codex Underline (Drawn in sequentially on Clicks 11 ~ 15) */
.codex-underline {
  position: relative;
  display: inline-block;
  color: #475569;
  font-weight: 400;
  transition: color 0.35s ease, font-weight 0.35s ease, text-decoration-color 0.4s ease;
}

.codex-underline.codex-underline-active {
  color: #581C87;
  font-weight: 700;
  text-decoration: underline;
  text-decoration-color: #9333EA;
  text-decoration-thickness: 2.5px;
  text-underline-offset: 4px;
}

.quote-fade-enter-active,
.quote-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.quote-fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}

.quote-fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
