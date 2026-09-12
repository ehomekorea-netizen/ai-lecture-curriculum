<script setup lang="ts">
// EdgeAIShorts.vue - 엣지 AI 유튜브 쇼츠 단독 중앙 임베딩 컴포넌트
</script>

<template>
  <div class="flex flex-col items-center justify-center my-1">
    <div class="h-[365px] aspect-[9/16] rounded-2xl overflow-hidden border border-white/20 bg-black shadow-2xl relative">
      <iframe
        width="463"
        height="823"
        src="https://www.youtube.com/embed/CAhDyRPQqhw"
        title="엣지 AI (Edge AI)의 특징과 이점 알아보기! - 어드밴텍 웨비나 다시보기 #edgeai #엣지ai #엣지컴퓨팅 #edgecomputing #산업용ai #어드밴텍"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        class="w-full h-full"
      ></iframe>
    </div>
    <div class="flex items-center gap-2 text-xs text-white/60 font-mono mt-2.5">
      <span class="i-carbon-video text-sky-400"></span>
      <span>어드밴텍 산업용 엣지 AI 웨비나 다시보기 (YouTube Shorts)</span>
    </div>
  </div>
</template>
