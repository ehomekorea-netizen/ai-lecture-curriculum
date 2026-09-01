<script setup lang="ts">
const props = withDefaults(defineProps<{
  leftTitle: string
  leftBody: string
  rightTitle: string
  rightBody: string
  takeaway?: string
  stage?: number
}>(), {
  takeaway: '',
  stage: 0,
})

const showRight = () => props.stage >= 1
const showTakeaway = () => props.stage >= 2
</script>

<template>
  <div class="comparison-grid">
    <article class="deck-surface comparison-panel comparison-panel--muted">
      <div class="deck-kicker">Before</div>
      <h3>{{ leftTitle }}</h3>
      <p>{{ leftBody }}</p>
    </article>

    <div class="comparison-arrow i-carbon:arrow-right" aria-hidden="true" />

    <article
      class="deck-surface comparison-panel comparison-panel--accent deck-reveal-item"
      :class="{ 'is-visible': showRight() }"
    >
      <div class="deck-kicker text-cyan-200/80">After</div>
      <h3>{{ rightTitle }}</h3>
      <p>{{ rightBody }}</p>
    </article>

    <div
      v-if="takeaway"
      class="comparison-takeaway deck-reveal-item"
      :class="{ 'is-visible': showTakeaway() }"
    >
      <span class="i-carbon:checkmark-filled text-cyan-300" aria-hidden="true" />
      <span>{{ takeaway }}</span>
    </div>
  </div>
</template>

<style scoped>
.comparison-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 4rem minmax(0, 1fr);
  gap: 1.25rem;
  align-items: center;
}

.comparison-panel {
  min-height: 15rem;
  padding: 1.75rem;
}

.comparison-panel h3 {
  margin: 2rem 0 0;
  font-size: 1.6rem;
}

.comparison-panel p {
  margin: 0.75rem 0 0;
  color: var(--deck-muted);
}

.comparison-panel--muted {
  opacity: 0.72;
}

.comparison-panel--accent {
  border-color: rgb(103 232 249 / 34%);
  background: rgb(34 211 238 / 8%);
}

.comparison-arrow {
  justify-self: center;
  color: rgb(255 255 255 / 28%);
  font-size: 2rem;
}

.comparison-takeaway {
  grid-column: 1 / -1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  padding-top: 0.75rem;
  color: var(--deck-muted);
  text-align: center;
}
</style>
