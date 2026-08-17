<script setup lang="ts">
import { TOOL_ECOSYSTEM } from '../data'

const props = withDefaults(defineProps<{
  category?: string
  limit?: number
}>(), {
  category: 'all',
  limit: 6
})

const tools = TOOL_ECOSYSTEM
</script>

<template>
  <div class="tech-grid">
    <div
      v-for="tool in tools"
      :key="tool.name"
      class="tool-card"
      :style="{ '--brand': tool.color }"
    >
      <div class="tool-top">
        <span class="tool-icon">{{ tool.icon }}</span>
        <span class="tool-badge">{{ tool.badge }}</span>
      </div>

      <h3 class="tool-name">{{ tool.name }}</h3>
      <p class="tool-desc">{{ tool.description }}</p>

      <div class="tool-pros">
        <span v-for="(pro, i) in tool.pros" :key="i" class="pro-chip">✓ {{ pro }}</span>
      </div>

      <div class="tool-rec">
        <span class="rec-label">추천 용도:</span>
        <span class="rec-text">{{ tool.recommendedFor }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tech-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  width: 100%;
  margin-top: 0.8rem;
}

@media (max-width: 900px) {
  .tech-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.tool-card {
  background: #ffffff;
  border: 1.5px solid #E7E0D4;
  border-radius: 14px;
  padding: 1rem 1.1rem;
  box-shadow: 0 4px 12px rgba(43, 35, 27, 0.05);
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
  text-align: left;
}

.tool-card:hover {
  transform: translateY(-3px);
  border-color: #476BFF;
  box-shadow: 0 10px 24px rgba(71, 107, 255, 0.12);
}

.tool-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.tool-icon {
  font-size: 1.4rem;
}

.tool-badge {
  font-size: 0.68rem;
  font-weight: 800;
  background: #E8EEFF;
  color: #476BFF;
  padding: 2px 8px;
  border-radius: 10px;
}

.tool-name {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: #2B2620;
  margin: 0.1rem 0;
}

.tool-desc {
  font-size: 0.76rem;
  color: #666;
  line-height: 1.35;
}

.tool-pros {
  display: flex;
  flex-direction: column;
  gap: 3px;
  margin: 0.3rem 0;
}

.pro-chip {
  font-size: 0.7rem;
  color: #1B7A55;
  font-weight: 600;
  background: #EEFFFA;
  padding: 1px 6px;
  border-radius: 4px;
}

.tool-rec {
  margin-top: auto;
  padding-top: 0.4rem;
  border-top: 1px dashed #E7E0D4;
  font-size: 0.7rem;
  color: #857B6E;
  display: flex;
  gap: 4px;
}

.rec-label {
  font-weight: 700;
  color: #476BFF;
  flex-shrink: 0;
}

.rec-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
