<script setup lang="ts">
const props = withDefaults(defineProps<{
  stage?: number
  items?: Array<{
    narrow: string
    arrow?: string
    broad: string
  }>
}>(), {
  stage: 0,
  items: () => []
})
</script>

<template>
  <div class="claims-stack">
    <div
      v-for="(item, idx) in items"
      :key="idx"
      class="claim-card"
      :class="{
        'is-active': stage > idx,
        'is-pending': stage <= idx
      }"
    >
      <!-- Before (기존의 방식/한계) -->
      <div class="claim-before">
        <span class="status-icon before-icon">❌</span>
        <span class="text-before">
          {{ item.narrow }}
          <span class="strike-line" :class="{ 'draw-strike': stage > idx }"></span>
        </span>
      </div>

      <!-- Arrow Divider -->
      <div class="claim-divider">
        <span class="divider-line"></span>
        <span class="divider-arrow">➔</span>
        <span class="divider-line"></span>
      </div>

      <!-- After (새로운 솔루션/핵심 가치) -->
      <div class="claim-after">
        <span class="status-icon after-icon">✨</span>
        <span class="text-after">{{ item.broad }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.claims-stack {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  width: 100%;
  max-width: 100%;
}

.claim-card {
  display: flex;
  flex-direction: column;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 14px;
  padding: 0.75rem 0.9rem;
  box-shadow: 0 2px 6px rgba(15, 23, 42, 0.03);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  box-sizing: border-box;
}

.claim-card.is-active {
  border-color: #93C5FD;
  background: #FFFFFF;
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.07);
}

/* Before Row */
.claim-before {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: #475569;
  line-height: 1.35;
}

.status-icon {
  font-size: 0.8rem;
  flex-shrink: 0;
}

.text-before {
  position: relative;
  font-weight: 500;
  color: #475569;
  transition: color 0.3s ease;
  word-break: keep-all;
}

.claim-card.is-active .text-before {
  color: #94A3B8;
}

.strike-line {
  position: absolute;
  top: 50%;
  left: -2px;
  right: -2px;
  height: 2px;
  background: #EF4444;
  border-radius: 2px;
  transform: translateY(-50%) scaleX(0);
  transform-origin: left center;
  transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
  pointer-events: none;
}

.strike-line.draw-strike {
  transform: translateY(-50%) scaleX(1);
}

/* Subtle Divider */
.claim-divider {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0.3rem 0;
  opacity: 0.4;
  transition: opacity 0.3s ease;
}

.claim-card.is-active .claim-divider {
  opacity: 0.9;
}

.divider-line {
  flex: 1;
  height: 1px;
  background: #E2E8F0;
}

.divider-arrow {
  font-size: 0.75rem;
  color: #94A3B8;
  font-weight: 700;
}

.claim-card.is-active .divider-arrow {
  color: #2563EB;
}

/* After Row */
.claim-after {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.92rem;
  font-weight: 700;
  color: #334155;
  transition: all 0.3s ease;
  line-height: 1.35;
}

.text-after {
  word-break: keep-all;
  flex: 1;
  min-width: 0;
}

.claim-card.is-active .claim-after {
  color: #1D4ED8;
}
</style>
