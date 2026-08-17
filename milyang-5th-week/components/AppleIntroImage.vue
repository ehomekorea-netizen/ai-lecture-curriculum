<script setup lang="ts">
withDefaults(defineProps<{
  image?: string
  overlay?: string
}>(), {
  image: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
  overlay: 'linear-gradient(180deg, rgba(15, 23, 42, 0.45) 0%, rgba(15, 23, 42, 0.92) 100%)'
})
</script>

<template>
  <div 
    class="apple-intro-container"
    :style="{
      backgroundImage: `${overlay}, url('${image}')`
    }"
  >
    <!-- Top Partner Logos Banner -->
    <div class="top-logo-bar">
      <div class="logo-badge-wrapper">
        <img src="/img/partner-logos.png" alt="밀양시 · 밀양소통협력센터 · 에이제이인포텍" class="partner-logos-img" />
      </div>
    </div>

    <!-- Bottom Anchored Typography -->
    <div class="intro-content">
      <div class="intro-slot">
        <slot>
          <div class="kicker-tag">밀양 청년 취업역량 강화교육 · 5주차</div>
          <h1 class="intro-title">
            나만의 디지털 포트폴리오 빌딩<br>
            <span class="highlight-cyan">&amp; AI 에이전트 바이브 코딩</span>
          </h1>
          <p class="intro-desc">
            경험의 노션 데이터 자산화부터 모바일 링크인바이오, 제미나이 캔버스 웹 빌딩, 마누스 AI 에이전트 실무
          </p>
          <div class="meta-row">
            <span class="meta-pill">🗓️ 수/목 6시간 마스터</span>
            <span class="meta-pill">✨ 인터랙티브 웹 교안</span>
            <span class="meta-pill">⚡ No-Code to Vibe Coding</span>
          </div>
        </slot>
      </div>
    </div>
  </div>
</template>

<style scoped>
.apple-intro-container {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 2.2rem 3.5rem;
  box-sizing: border-box;
  color: #ffffff;
}

.top-logo-bar {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  z-index: 10;
}

.logo-badge-wrapper {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  padding: 6px 18px;
  border-radius: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.8);
  display: inline-flex;
  align-items: center;
}

.partner-logos-img {
  height: 28px;
  width: auto;
  object-fit: contain;
  display: block;
}

.intro-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  z-index: 10;
  margin-bottom: 0.5rem;
}

.kicker-tag {
  display: inline-block;
  font-family: 'Radio Canada Big', sans-serif;
  font-size: 0.85rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #53DFA9;
  margin-bottom: 0.7rem;
}

.intro-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 2.85rem;
  font-weight: 800;
  line-height: 1.16;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin: 0 0 0.9rem 0;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.4);
}

.highlight-cyan {
  color: #53DFA9;
  background: linear-gradient(135deg, #53DFA9 0%, #38BDF8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.intro-desc {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.82);
  line-height: 1.45;
  max-width: 680px;
  margin: 0 0 1.4rem 0;
}

.meta-row {
  display: flex;
  gap: 0.8rem;
}

.meta-pill {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 4px 14px;
  border-radius: 20px;
}
</style>
