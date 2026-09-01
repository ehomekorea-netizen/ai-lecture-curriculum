<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showTop = computed(() => true)
const showBottom = computed(() => (props.stage ?? 0) >= 1)
const showConclusion = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-center select-none py-1">
    
    <!-- Top Track: 1차시 RAG 이론 구조 (Theory Track) -->
    <div class="p-4 rounded-2xl border border-blue-500/30 bg-blue-950/20 backdrop-blur-md shadow-lg">
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-blue-400 animate-pulse"></span>
          <span class="text-xs font-mono font-bold text-blue-400 uppercase tracking-wider">1차시 RAG 이론 아키텍처</span>
        </div>
        <span class="text-[11px] font-mono text-white/50">Retrieval-Augmented Generation</span>
      </div>

      <div class="grid grid-cols-4 gap-3 relative">
        <!-- Step 1 -->
        <div class="p-3 rounded-xl bg-black/50 border border-blue-500/20 flex flex-col justify-between text-center relative group">
          <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:user text-base"></span>
          </div>
          <span class="text-xs font-bold text-white mb-0.5">사용자 질문</span>
          <span class="text-[10px] text-white/60">자연어 질의 입력</span>
          <!-- Arrow -->
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-blue-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Step 2 -->
        <div class="p-3 rounded-xl bg-black/50 border border-blue-500/20 flex flex-col justify-between text-center relative">
          <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:search text-base"></span>
          </div>
          <span class="text-xs font-bold text-blue-300 mb-0.5">1. Retrieval</span>
          <span class="text-[10px] text-white/60">사내 규정 DB 검색</span>
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-blue-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Step 3 -->
        <div class="p-3 rounded-xl bg-black/50 border border-blue-500/20 flex flex-col justify-between text-center relative">
          <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:data-enrichment text-base"></span>
          </div>
          <span class="text-xs font-bold text-blue-300 mb-0.5">2. Augmentation</span>
          <span class="text-[10px] text-white/60">프롬프트에 원문 주입</span>
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-blue-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Step 4 -->
        <div class="p-3 rounded-xl bg-black/50 border border-blue-500/20 flex flex-col justify-between text-center">
          <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:document-view text-base"></span>
          </div>
          <span class="text-xs font-bold text-blue-300 mb-0.5">3. Generation</span>
          <span class="text-[10px] text-white/60">근거 기반 답변 생성</span>
        </div>
      </div>
    </div>

    <!-- Vertical Bridge Connectors (Animated when stage >= 1) -->
    <div
      class="flex items-center justify-around py-2 transition-all duration-500"
      :class="[showBottom ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-1.5 text-cyan-300 text-xs font-mono">
        <span class="i-carbon:arrow-down text-base animate-bounce"></span>
        <span>복잡한 코딩 없이 도구로 1:1 완벽 자동화</span>
        <span class="i-carbon:arrow-down text-base animate-bounce"></span>
      </div>
    </div>

    <!-- Bottom Track: 2차시 Gemini Notebook 실무 도구 구현 (Practice Track) -->
    <div
      class="p-4 rounded-2xl border border-cyan-500/40 border-t-4 border-t-cyan-400 bg-cyan-950/25 backdrop-blur-md shadow-xl transition-all duration-700"
      :class="[showBottom ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
    >
      <div class="flex items-center justify-between mb-3 border-b border-white/10 pb-2">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
          <span class="text-xs font-mono font-bold text-cyan-300 uppercase tracking-wider">2차시 Gemini Notebook 실제 구현</span>
        </div>
        <span class="text-[11px] font-mono text-cyan-200">클릭만으로 완성하는 노코드 RAG</span>
      </div>

      <div class="grid grid-cols-4 gap-3">
        <!-- Notebook Step 1 -->
        <div class="p-3 rounded-xl bg-black/60 border border-cyan-500/30 flex flex-col justify-between text-center relative">
          <div class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:document-add text-base"></span>
          </div>
          <span class="text-xs font-bold text-white mb-0.5">Source (자료 등록)</span>
          <span class="text-[10px] text-cyan-200/80">PDF · 웹 · 유튜브 업로드</span>
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-cyan-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Notebook Step 2 -->
        <div class="p-3 rounded-xl bg-black/60 border border-cyan-500/30 flex flex-col justify-between text-center relative">
          <div class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:data-structured text-base"></span>
          </div>
          <span class="text-xs font-bold text-cyan-300 mb-0.5">자동 색인 (Index)</span>
          <span class="text-[10px] text-cyan-200/80">Gemini 1.5 Pro 벡터화</span>
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-cyan-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Notebook Step 3 -->
        <div class="p-3 rounded-xl bg-black/60 border border-cyan-500/30 flex flex-col justify-between text-center relative">
          <div class="w-7 h-7 rounded-lg bg-cyan-500/20 text-cyan-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:chat text-base"></span>
          </div>
          <span class="text-xs font-bold text-cyan-300 mb-0.5">Chat (자료 질문)</span>
          <span class="text-[10px] text-cyan-200/80">S-A-F 공식 질의</span>
          <span class="absolute -right-2 top-1/2 -translate-y-1/2 text-cyan-400 text-sm hidden md:block">➔</span>
        </div>

        <!-- Notebook Step 4 -->
        <div class="p-3 rounded-xl bg-black/60 border border-emerald-500/40 border-t-3 border-t-emerald-400 flex flex-col justify-between text-center shadow-lg">
          <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-300 flex items-center justify-center mx-auto mb-1.5">
            <span class="i-carbon:checkmark-outline text-base font-bold"></span>
          </div>
          <span class="text-xs font-bold text-emerald-300 mb-0.5">Citation (인용 대조)</span>
          <span class="text-[10px] text-emerald-200">클릭 시 원문 위치 이동</span>
        </div>
      </div>
    </div>

    <!-- Bottom Conclusion Banner -->
    <div
      class="mt-3.5 p-3 rounded-xl border border-emerald-500/30 bg-emerald-950/25 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showConclusion ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-emerald-400"></span>
        <span><strong>핵심 결론:</strong> RAG를 개발하지 않아도, 사용자는 <strong>'근거자료를 넣고 질문한다'</strong>는 방식으로 완벽히 체감할 수 있습니다.</span>
      </div>
      <span class="text-[11px] font-mono text-emerald-300 font-bold">노코드 RAG 완성</span>
    </div>

  </div>
</template>
