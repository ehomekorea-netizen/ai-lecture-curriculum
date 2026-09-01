<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const slideContext = useSlideContext()
const currentStage = computed(() => {
  const ctxClicks = slideContext?.$clicks?.value ?? slideContext?.$nav?.clicks ?? 0
  return Math.max(props.stage ?? 0, ctxClicks)
})
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top 2-Column: Chat vs Work Practical Prompt Examples -->
    <div class="grid grid-cols-2 gap-5 items-stretch mb-3">
      <!-- Case 1: General Chat Prompt (Standalone Poster) -->
      <div class="p-3.5 rounded-xl bg-white/5 border border-cyan-500/30 flex flex-col justify-between h-58">
        <div>
          <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-2">
            <div class="flex items-center gap-1.5 text-xs font-bold text-cyan-300">
              <span class="i-carbon:chat text-sm"></span>
              <span>Case 1. 일반 Chat 단독 포스터 생성</span>
            </div>
            <span class="text-[9.5px] font-mono text-cyan-300 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20">
              9:16 세로형
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-2.5 rounded-lg bg-black/60 border border-white/10 font-mono text-[10px] text-slate-200 leading-relaxed space-y-1 select-text break-keep">
            <p class="m-0 text-cyan-400 font-bold">"사내 에너지 절감 캠페인 2K 고화질 포스터를 생성해줘.</p>
            <p class="m-0 text-white/80">• <strong class="text-white">배경/구도:</strong> 채광이 좋은 친환경 스마트 오피스 전경 (9:16 세로형)</p>
            <p class="m-0 text-amber-300">• <strong class="text-white">인쇄 문구:</strong> 상단에 <span class="bg-amber-400/20 px-1 rounded text-amber-300">"에너지 절감, 스마트한 실천"</span> 한글 선명 인쇄</p>
            <p class="m-0 text-white/80">• <strong class="text-white">서브카피:</strong> <span class="bg-white/10 px-1 rounded text-white">"MC에너지 지속가능경영본부"</span></p>
            <p class="m-0 text-emerald-400">• <strong class="text-white">스타일:</strong> 과장된 3D가 아닌 자연스러운 자연광 포토리얼리즘"</p>
          </div>
        </div>

        <div class="pt-1.5 text-[9.5px] text-cyan-300/80 font-mono flex items-center justify-between">
          <span>💡 인쇄할 한글은 반드시 큰따옴표("")로 감싸기</span>
          <span class="font-bold">단독 실행</span>
        </div>
      </div>

      <!-- Case 2: ChatGPT Work Prompt (Context-Driven Banner) -->
      <div class="p-3.5 rounded-xl bg-white/5 border border-blue-500/30 flex flex-col justify-between h-58">
        <div>
          <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-2">
            <div class="flex items-center gap-1.5 text-xs font-bold text-blue-300">
              <span class="i-carbon:document-tasks text-sm"></span>
              <span>Case 2. ChatGPT Work 업무 맥락 연계 생성</span>
            </div>
            <span class="text-[9.5px] font-mono text-blue-300 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">
              16:9 가로형
            </span>
          </div>

          <!-- Prompt Box -->
          <div class="p-2.5 rounded-lg bg-black/60 border border-white/10 font-mono text-[10px] text-slate-200 leading-relaxed space-y-1 select-text break-keep">
            <p class="m-0 text-blue-400 font-bold">"방금 작성한 전력 소비 분석 보고서 내용을 바탕으로,</p>
            <p class="m-0 text-white/80">• <strong class="text-white">용도/화면비:</strong> 전사 인트라넷 공지용 16:9 와이드 배너 2K 제작</p>
            <p class="m-0 text-amber-300">• <strong class="text-white">헤드라인:</strong> 중앙에 <span class="bg-amber-400/20 px-1 rounded text-amber-300">"전력 12% 절감 달성! 실천에 감사드립니다"</span></p>
            <p class="m-0 text-white/80">• <strong class="text-white">시각 요소:</strong> 데이터 절감 그래프가 깔끔히 녹아든 클린 테크 그래픽</p>
            <p class="m-0 text-emerald-400">• <strong class="text-white">톤앤매너:</strong> 신뢰감 있는 딥블루/에메랄드 톤, 미니멀 레이아웃"</p>
          </div>
        </div>

        <div class="pt-1.5 text-[9.5px] text-blue-300/80 font-mono flex items-center justify-between">
          <span>💡 앞서 분석한 데이터 맥락을 프롬프트가 자동 계승</span>
          <span class="font-bold">보고서 연계</span>
        </div>
      </div>
    </div>

    <!-- Bottom: 4-Step Universal Prompt Formula (Cheat Sheet) -->
    <div class="p-3 px-4 rounded-xl bg-black/40 border border-white/15 flex items-center justify-between text-xs">
      <div class="flex items-center gap-2 font-mono text-white/90">
        <span class="text-emerald-400 font-bold">📌 교육생 실전 프롬프트 공식:</span>
        <span class="text-cyan-300">[1. 목적/배경]</span>
        <span class="text-white/40">➔</span>
        <span class="text-blue-300">[2. 화면비/2K]</span>
        <span class="text-white/40">➔</span>
        <span class="text-amber-300">[3. "한글 인쇄 문구"]</span>
        <span class="text-white/40">➔</span>
        <span class="text-emerald-300">[4. 포토리얼리즘 스타일]</span>
      </div>
      <span class="text-[10px] font-mono text-white/50">복사하여 단어만 수정해 사용</span>
    </div>
  </div>
</template>
