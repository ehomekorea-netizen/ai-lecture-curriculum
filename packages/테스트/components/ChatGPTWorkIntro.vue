<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })
const currentStage = computed(() => props.stage ?? 0)
</script>

<template>
  <div class="w-full flex flex-col justify-center select-none font-sans text-slate-800 text-left h-[330px] my-auto px-4">
    <!-- ── Pure Plain Text Editorial Layout (Highlight ONLY Chat & ChatGPT Work on Clicks) ── -->
    <div class="space-y-4 text-xs md:text-[14px] leading-relaxed max-w-4xl font-normal">
      <!-- Paragraph 1: Main Definition -->
      <p class="text-sm md:text-[16px] font-bold text-slate-900 font-serif leading-snug">
        ChatGPT Work는 ChatGPT에게
        <span class="text-blue-600 underline underline-offset-4 decoration-blue-300 font-bold">실제 업무를 위임하는 방식</span>입니다.
      </p>

      <!-- Paragraph 2: Chat vs Work Core Contrast (ONLY these two get highlighter pen animation) -->
      <p class="text-slate-700 leading-relaxed break-keep">
        단순한 답변, 개념 설명, 아이디어 브레인스토밍, 짧은 초안 작성이 필요할 때는
        <span
          class="hl-brush font-bold text-slate-900"
          :class="{ active: currentStage >= 1 }"
        >Chat</span>을 사용합니다. 반면, 기획서, 발표 슬라이드, 데이터 분석, 정기 업데이트처럼
        <strong>내가 직접 검토하고 즉시 활용할 수 있는 명확한 결과물(파일)</strong>이 필요할 때는
        <span
          class="hl-brush text-blue-600 font-black"
          :class="{ active: currentStage >= 2 }"
        >ChatGPT Work</span>를 사용합니다.
      </p>

      <!-- Paragraph 3: File/Tool Orchestration & Human Approval -->
      <p class="text-slate-700 leading-relaxed break-keep">
        ChatGPT Work는 내 컴퓨터의 파일, 플러그인, 승인된 도구를 직접 활용해 정보를 찾고, 완성된 파일을 생성하며,
        <strong>검토 준비가 완료된 상태로 업무를 완수</strong>합니다. 작업이 진행되는 동안 실시간 진행 상황을 확인하고, 질문에 답하거나 방향을 전환하며,
        <strong>중요한 결정과 행동을 사람이 직접 승인</strong>할 수 있습니다.
      </p>

      <!-- Paragraph 4: Desktop Local Files -->
      <p class="text-slate-600 leading-relaxed break-keep text-[12.5px] pt-3 border-t border-slate-200/80">
        데스크톱 앱에서는 내 컴퓨터의
        <strong>지정된 로컬 파일과 앱</strong>을 직접 연결하여, 복잡한 실무를 일상적인 업무 경험으로 손쉽게 해결할 수 있습니다.
      </p>
    </div>
  </div>
</template>

<style scoped>
/* ── Clean & Subtle Blue/Sky Highlighter Pen Brush Animation for Chat & ChatGPT Work ── */
.hl-brush {
  background-image: linear-gradient(120deg, rgba(59, 130, 246, 0.22) 0%, rgba(37, 99, 235, 0.3) 100%);
  background-repeat: no-repeat;
  background-position: 0 88%;
  background-size: 0% 45%;
  transition: background-size 0.45s cubic-bezier(0.16, 1, 0.3, 1);
  padding: 0 4px;
  border-radius: 3px;
}

.hl-brush.active {
  background-size: 100% 45%;
}
</style>
