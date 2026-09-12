<script setup lang="ts">
// EdgeAIIntro.vue - 엣지 AI 개념 및 산업용/수산 현장 이점 컴포넌트
</script>

<template>
  <div class="grid grid-cols-[36%_64%] gap-4 my-2 items-center">
    <!-- YouTube Shorts Embed (Left) -->
    <div class="flex flex-col items-center">
      <div class="w-full max-w-[230px] aspect-[9/16] rounded-2xl overflow-hidden border border-white/20 bg-black shadow-2xl relative">
        <iframe
          src="https://www.youtube.com/embed/CAhDyRPQqhw"
          title="엣지 AI (Edge AI)의 특징과 이점 알아보기! - 어드밴텍 웨비나 다시보기 #edgeai #엣지ai #엣지컴퓨팅 #edgecomputing #산업용ai #어드밴텍"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerpolicy="strict-origin-when-cross-origin"
          allowfullscreen
          class="w-full h-full"
        ></iframe>
      </div>
      <div class="flex items-center gap-1.5 text-[11px] text-white/60 font-mono mt-2">
        <span class="i-carbon-video text-sky-400"></span>
        <span>어드밴텍 산업용 엣지 AI 웨비나 요약</span>
      </div>
    </div>

    <!-- Edge AI Core Breakdown (Right) -->
    <div class="flex flex-col gap-2.5">
      <div class="grid grid-cols-2 gap-2.5">
        <!-- Feature 1 -->
        <div class="p-3 rounded-xl border border-sky-500/30 bg-sky-950/25 flex flex-col justify-between backdrop-blur-sm">
          <div>
            <div class="text-sky-300 font-bold text-xs mb-1 flex items-center gap-1.5">
              <span class="i-carbon-flash text-sky-400"></span>
              <span>1. 초저지연 실시간 연산</span>
            </div>
            <p class="text-white/75 text-[11px] leading-relaxed m-0">
              클라우드 전송 지연 없이, 가두리 단말기에서 0.01초 만에 이상 징후를 판독하고 제어합니다.
            </p>
          </div>
          <div class="text-[10px] text-sky-400/90 font-mono mt-2 pt-1.5 border-t border-white/10 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>
            지연 없는 즉각 제어
          </div>
        </div>

        <!-- Feature 2 -->
        <div class="p-3 rounded-xl border border-emerald-500/30 bg-emerald-950/25 flex flex-col justify-between backdrop-blur-sm">
          <div>
            <div class="text-emerald-300 font-bold text-xs mb-1 flex items-center gap-1.5">
              <span class="i-carbon-wifi-off text-emerald-400"></span>
              <span>2. 망 단절 독립 구동</span>
            </div>
            <p class="text-white/75 text-[11px] leading-relaxed m-0">
              해상 폭풍우나 통신 마비 상황에서도 로컬 AI가 중단 없이 24시간 독립 가동됩니다.
            </p>
          </div>
          <div class="text-[10px] text-emerald-400/90 font-mono mt-2 pt-1.5 border-t border-white/10 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            오프라인 자율 방어
          </div>
        </div>

        <!-- Feature 3 -->
        <div class="p-3 rounded-xl border border-purple-500/30 bg-purple-950/25 flex flex-col justify-between backdrop-blur-sm">
          <div>
            <div class="text-purple-300 font-bold text-xs mb-1 flex items-center gap-1.5">
              <span class="i-carbon-data-volume text-purple-400"></span>
              <span>3. 통신 비용 & 대역폭 절감</span>
            </div>
            <p class="text-white/75 text-[11px] leading-relaxed m-0">
              무거운 고화질 CCTV 영상을 다 보내지 않고, 현장에서 판단한 메타데이터만 전송합니다.
            </p>
          </div>
          <div class="text-[10px] text-purple-400/90 font-mono mt-2 pt-1.5 border-t border-white/10 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-purple-400"></span>
            LTE/위성 통신비 90%↓
          </div>
        </div>

        <!-- Feature 4 -->
        <div class="p-3 rounded-xl border border-amber-500/30 bg-amber-950/25 flex flex-col justify-between backdrop-blur-sm">
          <div>
            <div class="text-amber-300 font-bold text-xs mb-1 flex items-center gap-1.5">
              <span class="i-carbon-security text-amber-400"></span>
              <span>4. 현장 데이터 보안 유지</span>
            </div>
            <p class="text-white/75 text-[11px] leading-relaxed m-0">
              양식장의 고유 생육 노하우와 영상이 외부 클라우드로 무단 반출되지 않고 기기에 격리됩니다.
            </p>
          </div>
          <div class="text-[10px] text-amber-400/90 font-mono mt-2 pt-1.5 border-t border-white/10 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
            어장 핵심 자산 보호
          </div>
        </div>
      </div>

      <!-- Bottom Marine Insight Box -->
      <div class="p-2.5 bg-white/5 rounded-xl text-xs text-white/90 border border-white/10 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="i-carbon-idea text-amber-300 text-base flex-shrink-0"></span>
          <span class="text-[11.5px] leading-snug">
            <strong>수산업 현장 시사점:</strong> "통신이 끊겨도 비상 산소 공급기와 사이렌은 스스로 돌아가야 한다"는 현장 자율 방어의 핵심 두뇌가 바로 엣지 AI입니다.
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
