<script setup lang="ts">
import { ref } from 'vue'
import { WIKI_COMPONENTS, WikiItem } from '../wikiData'

const activeItem = ref<WikiItem | null>(null)

function selectItem(item: WikiItem) {
  activeItem.value = item
}
</script>

<template>
  <div class="wiki-grid-container">
    <div class="grid-layout">
      <div 
        v-for="item in WIKI_COMPONENTS" 
        :key="item.id"
        class="wiki-card"
        :class="{ active: activeItem?.id === item.id }"
        @click="selectItem(item)"
      >
        <div class="card-top">
          <span class="card-icon">{{ item.icon }}</span>
          <span class="badge">{{ item.category }}</span>
        </div>
        <div class="card-title">{{ item.title }}</div>
        <div class="card-effect">✨ {{ item.effect }}</div>
        <div class="card-usecase">🎯 {{ item.useCase }}</div>
        <div class="card-tag"><code>{{ item.tag }}</code></div>
      </div>
    </div>

    <!-- Active Details Modal / Banner -->
    <div v-if="activeItem" class="active-detail-banner">
      <div class="detail-content">
        <h3>Selected: {{ activeItem.icon }} {{ activeItem.title }} ({{ activeItem.category }})</h3>
        <p><b>연출 효과:</b> {{ activeItem.effect }}</p>
        <p><b>주요 용도:</b> {{ activeItem.useCase }}</p>
        <p><b>사용 태그:</b> <code>{{ activeItem.tag }}</code></p>
      </div>
      <button class="close-btn" @click="activeItem = null">✕ 닫기</button>
    </div>
  </div>
</template>

<style scoped>
.wiki-grid-container {
  width: 100%;
  max-width: 1100px;
  margin: 0 auto;
}
.grid-layout {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.75rem;
}
.wiki-card {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #E7E0D4;
  border-radius: 10px;
  padding: 0.75rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.03);
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.wiki-card:hover {
  transform: translateY(-3px);
  border-color: #476BFF;
  box-shadow: 0 6px 12px rgba(71, 107, 255, 0.12);
}
.wiki-card.active {
  border-color: #476BFF;
  background: #F4F7FF;
}
.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.3rem;
}
.card-icon {
  font-size: 1.2rem;
}
.badge {
  font-size: 0.65rem;
  font-weight: 700;
  padding: 2px 6px;
  background: #E8EEFF;
  color: #476BFF;
  border-radius: 6px;
  text-transform: uppercase;
}
.card-title {
  font-family: 'Source Serif 4', serif;
  font-size: 0.88rem;
  font-weight: 700;
  color: #2B2620;
  margin-bottom: 0.25rem;
  line-height: 1.25;
}
.card-effect {
  font-size: 0.72rem;
  color: #555;
  margin-bottom: 0.2rem;
  line-height: 1.2;
}
.card-usecase {
  font-size: 0.7rem;
  color: #476BFF;
  margin-bottom: 0.38rem;
  line-height: 1.2;
}
.card-tag {
  background: #FAF8F4;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.62rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border: 1px solid #EAE3D9;
}
.card-tag code {
  color: #D9930A;
}
.active-detail-banner {
  margin-top: 0.8rem;
  padding: 0.8rem 1.2rem;
  background: #476BFF;
  color: #ffffff;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 12px rgba(71, 107, 255, 0.3);
}
.active-detail-banner p {
  margin: 0.15rem 0;
  font-size: 0.85rem;
}
.active-detail-banner code {
  background: rgba(255,255,255,0.2);
  padding: 2px 6px;
  border-radius: 4px;
  color: #fff;
}
.close-btn {
  background: rgba(255,255,255,0.2);
  border: none;
  color: white;
  padding: 4px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 700;
}
</style>
