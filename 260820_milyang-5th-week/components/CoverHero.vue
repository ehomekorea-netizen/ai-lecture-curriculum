<script setup lang="ts">
// Apple Keynote Style Hero Cover Component
</script>

<template>
  <div class="cover-hero-container">
    <!-- Top Kicker Pill Badge -->
    <div class="kicker-badge">
      <span class="pulse-icon">⚡</span>
      <span>2026 밀양 청년 취업역량 강화교육 · 5주차 마스터 클래스</span>
    </div>

    <!-- Main Hero Headline -->
    <h1 class="hero-title">
      나만의 디지털 포트폴리오 빌딩<br>
      <span class="gradient-text">&amp; AI 에이전트 바이브 코딩</span>
    </h1>

    <!-- Subtitle Description -->
    <p class="hero-sub">
      경험의 노션 데이터 자산화부터 모바일 링크트리, 제미나이 캔버스 웹 빌딩, 마누스 AI 에이전트 실무까지
    </p>

    <!-- Two Day Summary Feature Cards -->
    <div class="curriculum-cards">
      <div class="c-card day1-card">
        <div class="card-head">
          <span class="day-badge day1">DAY 1 · 수요일</span>
          <span class="time-text">14:00 ~ 17:00 (3h)</span>
        </div>
        <h3 class="card-title">디지털 포트폴리오 &amp; 글로벌 배포</h3>
        <p class="card-desc">Notion 템플릿 커스텀 · Littly 마이크로 허브 · Gemini Canvas &amp; Netlify 1분 배포</p>
      </div>

      <div class="c-card day2-card">
        <div class="card-head">
          <span class="day-badge day2">DAY 2 · 목요일</span>
          <span class="time-text">14:00 ~ 17:00 (3h)</span>
        </div>
        <h3 class="card-title">생성형 AI 에이전트 &amp; 바이브 코딩</h3>
        <p class="card-desc">LLM vs 자율 Agent 패러다임 · V-I-B-E 4단계 공식 · Manus.ai 완제품 제작</p>
      </div>
    </div>

    <!-- Bottom Metadata -->
    <div class="hero-footer">
      <span class="meta-tag">🎓 6시간 마스터 커리큘럼</span>
      <span class="meta-tag">✨ 100% 인터랙티브 웹 교안</span>
      <span class="meta-tag">🚀 No-Code to Vibe Coding</span>
    </div>
  </div>
</template>

<style scoped>
.cover-hero-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 100%;
  width: 100%;
  padding: 1.5rem 2rem 1rem;
  box-sizing: border-box;
}

.kicker-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 1.5px solid #E7E0D4;
  border-radius: 24px;
  padding: 5px 16px;
  font-family: 'Radio Canada Big', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  color: #476BFF;
  box-shadow: 0 2px 8px rgba(71, 107, 255, 0.08);
  margin-bottom: 1.2rem;
}

.pulse-icon {
  font-size: 0.9rem;
}

.hero-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 2.75rem;
  font-weight: 800;
  line-height: 1.18;
  letter-spacing: -0.03em;
  color: #1D1D1F;
  margin: 0 0 0.8rem 0;
}

.gradient-text {
  color: #476BFF;
  background: linear-gradient(135deg, #3B63DB 0%, #7C3AED 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-sub {
  font-size: 0.95rem;
  color: #6E6E73;
  max-width: 650px;
  line-height: 1.45;
  margin: 0 auto 1.6rem;
}

.curriculum-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.2rem;
  width: 100%;
  max-width: 820px;
  margin-bottom: 1.6rem;
}

.c-card {
  background: #ffffff;
  border: 1.5px solid #E7E0D4;
  border-radius: 16px;
  padding: 1.1rem 1.3rem;
  text-align: left;
  box-shadow: 0 6px 16px rgba(43, 35, 27, 0.05);
  transition: transform 0.2s, box-shadow 0.2s;
}

.c-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(43, 35, 27, 0.09);
}

.card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.45rem;
}

.day-badge {
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 8px;
  letter-spacing: 0.04em;
}

.day-badge.day1 {
  background: #E8EEFF;
  color: #476BFF;
  border: 1px solid rgba(71, 107, 255, 0.3);
}

.day-badge.day2 {
  background: #F3E8FF;
  color: #7C3AED;
  border: 1px solid rgba(124, 58, 237, 0.3);
}

.time-text {
  font-family: 'Geist Mono', monospace;
  font-size: 0.7rem;
  color: #857B6E;
}

.card-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: #1D1D1F;
  margin: 0 0 0.3rem 0;
}

.card-desc {
  font-size: 0.78rem;
  color: #666666;
  line-height: 1.35;
  margin: 0;
}

.hero-footer {
  display: flex;
  gap: 0.8rem;
  justify-content: center;
}

.meta-tag {
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid #E7E0D4;
  padding: 3px 12px;
  border-radius: 20px;
  font-size: 0.72rem;
  font-weight: 600;
  color: #6E6E73;
}
</style>
