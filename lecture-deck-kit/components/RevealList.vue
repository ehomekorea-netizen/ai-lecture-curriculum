<script setup lang="ts">
interface RevealItem {
  icon?: string
  title: string
  body?: string
}

const props = withDefaults(defineProps<{
  items: RevealItem[]
  stage?: number
}>(), {
  stage: 0,
})

function isVisible(index: number) {
  return props.stage >= index + 1
}
</script>

<template>
  <div class="grid gap-2">
    <article
      v-for="(item, index) in items"
      :key="item.title"
      class="deck-surface deck-reveal-item flex items-center gap-3 px-4 py-2.5"
      :class="{ 'is-visible': isVisible(index) }"
    >
      <div
        v-if="item.icon"
        class="grid h-8 w-8 shrink-0 place-items-center rounded-lg bg-cyan-300/10 text-lg text-cyan-200"
        :class="item.icon"
        aria-hidden="true"
      />
      <div>
        <h3 class="m-0 text-base font-semibold">{{ item.title }}</h3>
        <p v-if="item.body" class="m-0 mt-0.5 text-sm deck-muted">{{ item.body }}</p>
      </div>
    </article>
  </div>
</template>
