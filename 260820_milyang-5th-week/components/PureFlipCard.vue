<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  beforeTitle: { type: String, default: '❌ Before (수동 방식)' },
  beforeText: { type: String, default: '사람이 직접 확인하고 수동 복구' },
  afterTitle: { type: String, default: '✅ After (AI 자율 자동화)' },
  afterText: { type: String, default: 'AI 에이전트가 24/7 실시간 자동 감지 및 즉시 복구' }
})

const isFlipped = ref(false)
function toggleFlip() {
  isFlipped.value = !isFlipped.value
}
</script>

<template>
  <div class="pure-flip-wrapper" @click="toggleFlip">
    <div class="pure-flip-card" :class="{ flipped: isFlipped }">
      <!-- Front (Before) -->
      <div class="card-face card-front">
        <div class="card-badge before-badge">BEFORE</div>
        <h3 class="card-title opacity-100">{{ beforeTitle }}</h3>
        <p class="card-desc" v-html="beforeText"></p>
        <div class="flip-guide">👇 마우스로 클릭하면 3D로 뒤집힙니다</div>
      </div>
      <!-- Back (After) -->
      <div class="card-face card-back">
        <div class="card-badge after-badge">AFTER</div>
        <h3 class="card-title opacity-100">{{ afterTitle }}</h3>
        <p class="card-desc" v-html="afterText"></p>
        <div class="flip-guide">👇 마우스로 클릭하면 다시 원래대로 돌아옵니다</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pure-flip-wrapper {
  perspective: 1000px;
  width: 100%;
  max-width: 520px;
  height: 220px;
  margin: 1.5rem auto;
  cursor: pointer;
}

.pure-flip-card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}

.pure-flip-card.flipped {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.8rem 2rem;
  text-align: center;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.08);
}

.card-front {
  background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
  border: 2px solid #F87171;
  color: #1E293B;
}

.card-back {
  background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
  border: 2px solid #34D399;
  color: #1E293B;
  transform: rotateY(180deg);
}

.card-badge {
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 3px 12px;
  border-radius: 20px;
  margin-bottom: 0.6rem;
}
.before-badge { background: #DC2626; color: #fff; }
.after-badge { background: #059669; color: #fff; }

h3 {
  font-family: 'Pretendard', -apple-system, sans-serif !important;
  font-size: 1.35rem !important;
  font-weight: 800 !important;
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem !important;
}

.card-front h3 {
  color: #991B1B !important;
}

.card-back h3 {
  color: #065F46 !important;
}

.card-desc {
  font-size: 0.95rem !important;
  color: #1E293B !important;
  font-weight: 500;
  line-height: 1.5 !important;
  opacity: 1 !important;
}

.flip-guide {
  font-size: 0.75rem;
  color: #475569;
  margin-top: 0.8rem;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.8);
  padding: 3px 12px;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}
</style>
