<script setup lang="ts">
import { ref } from 'vue'

const copied = ref(false)

const promptText = `# 역할: 웹 퍼블리셔 및 UI 디자이너
아래 나의 경험 DB를 바탕으로 깔끔하고 반응형인 1페이지 웹 포트폴리오를 만들어줘.

[포트폴리오 필수 구성]
1. Hero: 이름, 희망 직무, 한 줄 슬로건, 연락처(이메일, 전화번호)
2. About: 나의 일하는 태도와 직무 핵심 강점 3가지 요약
3. Projects: 노션 DB의 문제해결 과정(STAR)과 정량 성과 카드 레이아웃
4. Skills: 활용 가능한 툴 및 자격증 뱃지 목록

[나의 노션 경험 DB]
(여기에 1교시 노션 포트폴리오의 텍스트를 그대로 붙여넣기)`

async function copyPrompt(e: Event) {
  e.stopPropagation()
  try {
    await navigator.clipboard.writeText(promptText)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy: ', err)
  }
}
</script>

<template>
  <div class="prompt-card bg-slate-950 text-slate-100 rounded-2xl border border-slate-700/80 shadow-2xl p-3.5 select-text">
    <!-- Header with Copy Button -->
    <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span class="text-xs font-black text-emerald-400 font-mono tracking-wide">1-Shot 마스터 프롬프트</span>
      </div>
      
      <!-- Instructor Copy Button -->
      <button
        @click="copyPrompt"
        class="flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold font-mono transition-all cursor-pointer select-none"
        :class="copied ? 'bg-emerald-600 text-white shadow-lg scale-105' : 'bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600/80 hover:border-emerald-400'"
      >
        <span>{{ copied ? '✅' : '📋' }}</span>
        <span>{{ copied ? '복사 완료!' : '프롬프트 복사' }}</span>
      </button>
    </div>

    <!-- Crystal Clear Prompt Content (No Scrollbar Needed) -->
    <div class="font-mono text-[11px] leading-[1.45] space-y-1 text-slate-200">
      <div class="text-cyan-300 font-bold">
        # 역할: 웹 퍼블리셔 및 UI 디자이너
      </div>
      <div class="text-slate-100 font-medium">
        아래 나의 경험 DB를 바탕으로 깔끔하고 반응형인 1페이지 웹 포트폴리오를 만들어줘.
      </div>

      <div class="pt-1 text-amber-300 font-bold">
        [포트폴리오 필수 구성]
      </div>
      <div class="grid grid-cols-2 gap-x-2 gap-y-0.5 text-[10.5px] text-slate-300 bg-slate-900/90 p-1.5 rounded-lg border border-slate-800">
        <div>1. <b class="text-white">Hero</b>: 슬로건 &amp; 연락처</div>
        <div>2. <b class="text-white">About</b>: 핵심 직무 역량</div>
        <div>3. <b class="text-white">Projects</b>: STAR 성과 카드</div>
        <div>4. <b class="text-white">Skills</b>: 툴 &amp; 자격증 뱃지</div>
      </div>

      <div class="pt-1 text-emerald-400 font-bold">
        [나의 노션 경험 DB]
      </div>
      <div class="text-[10px] text-slate-400 bg-slate-900/60 px-2 py-1 rounded border border-dashed border-slate-700 italic">
        👉 (1교시 노션 포트폴리오의 텍스트를 그대로 복사하여 여기에 붙여넣기)
      </div>
    </div>
  </div>
</template>

<style scoped>
.prompt-card {
  box-sizing: border-box;
}
</style>
