<script setup lang="ts">
import { computed } from 'vue'

const base = import.meta.env.BASE_URL || '/'
const coverImageUrl = computed(() => `${base}img/cover-teamwork.jpg`)
</script>

<template>
  <div 
    class="keynote-cover-container absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden"
    :style="{
      backgroundImage: `linear-gradient(135deg, rgba(15, 23, 42, 0.88) 0%, rgba(15, 23, 42, 0.62) 55%, rgba(15, 23, 42, 0.30) 100%), url('${coverImageUrl}')`
    }"
  >
    <!-- Top Partner Header -->
    <div class="relative z-10 w-full flex items-center justify-between px-12 pt-8">
      <div class="partner-glass-badge flex items-center bg-white/95 backdrop-blur-md px-4.5 py-1.5 rounded-full border border-white/60 shadow-lg">
        <img :src="`${base}img/partner-logos.png`" alt="밀양시 · 밀양소통협력센터 · 에이제이인포텍" class="h-6.5 w-auto object-contain block" />
      </div>

      <div class="px-3.5 py-1 rounded-full bg-slate-900/60 backdrop-blur-md border border-white/15 text-slate-300 text-xs font-semibold font-mono tracking-wide shadow-sm">
        2026 청년 취업역량 강화 특화 과정
      </div>
    </div>

    <!-- Main Typography Content (Anchored Bottom-Left for Apple Keynote Feel) -->
    <div class="relative z-10 w-full px-12 pb-12">
      <div class="max-w-[720px]">
        <!-- Kicker -->
        <div class="inline-block text-xs font-extrabold uppercase tracking-widest text-emerald-400 font-mono mb-2.5">
          밀양 청년 취업역량 강화교육 · 5주차
        </div>

        <!-- Main Headline (Polished, Ultra-High Legibility) -->
        <h1 class="intro-title">
          나만의 디지털 포트폴리오 빌딩<br />
          <span class="intro-accent">&amp; AI 에이전트 바이브 코딩</span>
        </h1>

        <!-- Subtitle Description -->
        <p class="intro-desc">
          경험의 노션 데이터 자산화부터 모바일 마이크로 랜딩, 제미나이 캔버스 웹 빌딩, 마누스 AI 에이전트 실무
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.keynote-cover-container {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: #FFFFFF;
  box-sizing: border-box;
}

.intro-title {
  font-family: 'Pretendard', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  font-size: 3.1rem !important;
  font-weight: 800 !important;
  line-height: 1.18 !important;
  letter-spacing: -0.035em !important;
  color: #FFFFFF !important;
  margin: 0 0 1rem 0 !important;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.45);
  word-break: keep-all;
}

.intro-accent {
  background: linear-gradient(135deg, #38BDF8 0%, #34D399 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.intro-desc {
  font-family: 'Pretendard', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 1.05rem;
  font-weight: 500;
  line-height: 1.6;
  color: rgba(241, 245, 249, 0.92);
  margin: 0;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.4);
  word-break: keep-all;
}
</style>
