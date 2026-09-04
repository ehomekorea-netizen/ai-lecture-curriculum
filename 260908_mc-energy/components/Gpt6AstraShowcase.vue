<script setup lang="ts">
import { ref } from 'vue'

const isCopied = ref(false)

const copyLink = () => {
  navigator.clipboard.writeText('https://youtu.be/FlVmJdFjPUA')
  isCopied.value = true
  setTimeout(() => {
    isCopied.value = false
  }, 2000)
}
</script>

<template>
  <div class="w-full my-1">
    <div class="grid grid-cols-[58%_42%] gap-5 items-start">
      
      <!-- Left Column: Large Video Embed -->
      <div class="flex flex-col">
        <!-- Video Container -->
        <div class="w-full aspect-video rounded-2xl overflow-hidden border border-cyan-500/40 bg-black shadow-[0_0_35px_rgba(6,182,212,0.2)] relative">
          <iframe
            class="w-full h-full border-0"
            src="https://www.youtube.com/embed/FlVmJdFjPUA?rel=0&modestbranding=1"
            title="OpenAI GPT-6 Astra Demonstration"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
          ></iframe>
        </div>

        <!-- Video Metadata Bar -->
        <div class="flex items-center justify-between mt-2 px-1 text-xs">
          <div class="flex items-center gap-2">
            <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-red-500/10 border border-red-500/30 text-red-400 font-mono text-[10px] font-bold">
              <span class="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></span>
              YouTube HD
            </span>
            <span class="text-slate-400 text-[11px] font-medium">GPT-6 Astra 현장 시연 데모</span>
          </div>

          <div class="flex items-center gap-2">
            <a
              href="https://youtu.be/FlVmJdFjPUA"
              target="_blank"
              class="text-[11px] font-mono text-cyan-400 hover:text-cyan-300 transition-colors flex items-center gap-1"
            >
              <span>전용창 열기</span>
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Right Column: 3 Core Paradigm Takeaways -->
      <div class="flex flex-col gap-2.5">
        
        <!-- Card 1: 자율 컴퓨터 제어 -->
        <div class="p-3.5 rounded-xl bg-cyan-950/30 border border-cyan-500/30 hover:border-cyan-400/60 transition-all">
          <div class="flex items-center justify-between mb-1.5">
            <div class="flex items-center gap-2">
              <span class="i-carbon:screen text-cyan-400 text-base"></span>
              <span class="font-bold text-white text-[13px]">자율 컴퓨터 제어 (Computer Use)</span>
            </div>
            <span class="px-1.5 py-0.5 rounded text-[9.5px] font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">
              OS 직접 조작
            </span>
          </div>
          <p class="text-[11.5px] text-slate-300 m-0 leading-relaxed">
            단순 텍스트 출력을 넘어 마우스·키보드로 <strong>스프레드시트, 웹 브라우저, 로컬 사내 앱을 인간처럼 직접 탐색 및 조작</strong>
          </p>
        </div>

        <!-- Card 2: 프론티어 복합 추론 -->
        <div class="p-3.5 rounded-xl bg-blue-950/30 border border-blue-500/30 hover:border-blue-400/60 transition-all">
          <div class="flex items-center justify-between mb-1.5">
            <div class="flex items-center gap-2">
              <span class="i-carbon:cognitive text-blue-400 text-base"></span>
              <span class="font-bold text-white text-[13px]">프론티어 복합 추론 (Reasoning)</span>
            </div>
            <span class="px-1.5 py-0.5 rounded text-[9.5px] font-mono font-bold bg-blue-500/20 text-blue-300 border border-blue-500/40">
              최고 벤치마크
            </span>
          </div>
          <p class="text-[11.5px] text-slate-300 m-0 leading-relaxed">
            FrontierMath 97.6% 및 ARC-AGI-3 최고 기록. <strong>단계별 논리 검증과 지능형 자가보정</strong>을 통해 복잡한 기술적 문제 완벽 해결
          </p>
        </div>

        <!-- Card 3: 105만 토큰 & 실무 엔드투엔드 -->
        <div class="p-3.5 rounded-xl bg-emerald-950/30 border border-emerald-500/30 hover:border-emerald-400/60 transition-all">
          <div class="flex items-center justify-between mb-1.5">
            <div class="flex items-center gap-2">
              <span class="i-carbon:document-multiple-01 text-emerald-400 text-base"></span>
              <span class="font-bold text-white text-[13px]">105만 토큰 & 엔드투엔드 완결</span>
            </div>
            <span class="px-1.5 py-0.5 rounded text-[9.5px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
              1.05M Tokens
            </span>
          </div>
          <p class="text-[11.5px] text-slate-300 m-0 leading-relaxed">
            사내 규정집·설비 매뉴얼·방대한 데이터를 통째로 흡수하여 <strong>초안 기획부터 최종 결과 파일 납품까지 단절 없이 자율 완결</strong>
          </p>
        </div>

        <!-- Bottom Takeaway Callout -->
        <div class="p-2.5 rounded-xl bg-white/[0.04] border border-white/15 flex items-center justify-between text-xs">
          <span class="flex items-center gap-1.5 font-bold text-cyan-300 text-[11px] whitespace-nowrap">
            <span class="i-carbon:flash text-amber-400"></span>
            <span>MC에너지 시사점</span>
          </span>
          <span class="text-[11px] text-slate-300 text-right leading-tight">
            "단순 챗봇 질의응답" ➔ <strong>"내 PC에서 업무를 완결하는 실행 파트너"</strong>로 관점 전환
          </span>
        </div>

      </div>

    </div>
  </div>
</template>