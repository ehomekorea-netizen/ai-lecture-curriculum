<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  title: string
  tool: string
  subtitle?: string
  steps?: string[]
  url?: string
  link?: string
}>(), {
  subtitle: '슬라이드에서 강사의 라이브 화면으로 시선을 전환합니다.',
  steps: () => [
    '강사의 실시간 시연 관찰 및 핵심 조작 포인트 체크',
    '제공된 프롬프트 및 템플릿 복제하여 개인 환경에 적용',
    '막히는 구간 발생 시 즉시 질문 및 실시간 트러블슈팅'
  ]
})

const targetUrl = computed(() => props.url || props.link)

function handleLinkClick(e: MouseEvent) {
  e.stopPropagation()
  if (targetUrl.value) {
    window.open(targetUrl.value, '_blank', 'noopener,noreferrer')
  }
}
</script>

<template>
  <div class="live-demo-card">
    <div class="live-header">
      <div class="live-pulse-badge">
        <span class="pulse-dot"></span>
        <span class="live-tag">LIVE ACTION STAGE</span>
      </div>
      <div class="tool-duration-tags">
        <a
          v-if="targetUrl"
          :href="targetUrl"
          target="_blank"
          rel="noopener noreferrer"
          class="tool-tag tool-tag-link"
          title="실습 사이트로 이동하기 (새 창)"
          @click.stop="handleLinkClick"
        >
          <span>🛠️ {{ tool }}</span>
          <span class="link-arrow">↗</span>
        </a>
        <span v-else class="tool-tag">🛠️ {{ tool }}</span>
      </div>
    </div>

    <div class="live-body">
      <h2 class="live-title">{{ title }}</h2>
      <p class="live-subtitle">{{ subtitle }}</p>

      <div class="steps-box">
        <div class="steps-label">실습 진행 체크포인트</div>
        <ul class="steps-list">
          <li v-for="(step, idx) in steps" :key="idx" class="step-item">
            <span class="step-num">{{ idx + 1 }}</span>
            <span class="step-desc">{{ step }}</span>
          </li>
        </ul>
      </div>
    </div>

    <div class="live-footer">
      <span class="focus-alert">💡 화면을 전환하고 강사 라이브 시연에 집중해 주세요!</span>
    </div>
  </div>
</template>

<style scoped>
.live-demo-card {
  width: 100%;
  max-width: 760px;
  margin: 1.2rem auto 0;
  background: linear-gradient(145deg, #181920 0%, #1e2029 100%);
  border: 2px solid #383b4b;
  border-radius: 18px;
  padding: 1.6rem 2.2rem;
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.25), 0 0 25px rgba(71, 107, 255, 0.15);
  color: #fff;
  position: relative;
  overflow: hidden;
  pointer-events: auto !important;
  z-index: 20;
}

.live-demo-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #FF5F56, #FFBD2E, #53DFA9, #476BFF);
}

.live-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  position: relative;
  z-index: 30;
}

.live-pulse-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 95, 86, 0.15);
  border: 1px solid rgba(255, 95, 86, 0.4);
  padding: 4px 12px;
  border-radius: 20px;
}

.pulse-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #FF5F56;
  box-shadow: 0 0 10px #FF5F56;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 95, 86, 0.7); }
  70% { transform: scale(1.15); box-shadow: 0 0 0 8px rgba(255, 95, 86, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 95, 86, 0); }
}

.live-tag {
  font-family: 'Geist Mono', monospace;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #FF8E88;
}

.tool-duration-tags {
  display: flex;
  gap: 8px;
  position: relative;
  z-index: 40;
}

.tool-tag {
  background: rgba(71, 107, 255, 0.2);
  border: 1px solid rgba(71, 107, 255, 0.4);
  color: #8CA4FF;
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  text-decoration: none;
}

.tool-tag-link {
  cursor: pointer !important;
  pointer-events: auto !important;
  background: rgba(71, 107, 255, 0.28);
  border: 1.5px solid rgba(140, 164, 255, 0.7);
  color: #c2d1ff;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 0 14px rgba(71, 107, 255, 0.25);
  position: relative;
  z-index: 50;
  user-select: none;
}

.tool-tag-link:hover {
  background: rgba(71, 107, 255, 0.55);
  border-color: #ffffff;
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 4px 18px rgba(71, 107, 255, 0.5), 0 0 10px rgba(83, 223, 169, 0.3);
}

.tool-tag-link:active {
  transform: translateY(0);
}

.link-arrow {
  font-size: 0.82rem;
  font-weight: 900;
  color: #53DFA9;
  transition: transform 0.2s ease, color 0.2s ease;
}

.tool-tag-link:hover .link-arrow {
  transform: translate(2px, -2px);
  color: #ffffff;
}

.live-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 1.65rem;
  font-weight: 700;
  color: #fff;
  margin: 0 0 0.35rem 0;
  line-height: 1.25;
}

.live-subtitle {
  font-size: 0.88rem;
  color: #a6adc8;
  margin-bottom: 1.2rem;
}

.steps-box {
  background: rgba(0, 0, 0, 0.25);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  padding: 0.9rem 1.1rem;
  margin-bottom: 1rem;
}

.steps-label {
  font-size: 0.72rem;
  font-weight: 700;
  color: #8CA4FF;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 0.5rem;
}

.steps-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}

.step-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.82rem;
  color: #d9e0ee;
}

.step-num {
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: #476BFF;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 800;
  flex-shrink: 0;
}

.live-footer {
  text-align: center;
  padding-top: 0.7rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.focus-alert {
  font-size: 0.8rem;
  font-weight: 700;
  color: #53DFA9;
}
</style>
