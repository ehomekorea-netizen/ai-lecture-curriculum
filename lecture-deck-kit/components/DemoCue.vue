<script setup lang="ts">
const props = withDefaults(defineProps<{
  title: string
  steps: string[]
  duration?: string
  stage?: number
}>(), {
  duration: '',
  stage: 0,
})

function isVisible(index: number) {
  return props.stage >= index + 1
}
</script>

<template>
  <section class="demo-cue deck-surface">
    <header class="flex items-start justify-between gap-8 border-b border-white/10 px-7 py-6">
      <div>
        <div class="deck-kicker flex items-center gap-2 text-rose-200/80">
          <span class="h-2 w-2 rounded-full bg-rose-400 shadow-[0_0_1rem_rgba(251,113,133,0.8)]" />
          Live demo
        </div>
        <h3 class="mt-3 text-2xl">{{ title }}</h3>
      </div>
      <div v-if="duration" class="shrink-0 font-mono text-sm deck-faint">
        {{ duration }}
      </div>
    </header>

    <ol class="m-0 grid list-none gap-3 px-7 py-6">
      <li
        v-for="(step, index) in steps"
        :key="step"
        class="deck-reveal-item flex items-center gap-4"
        :class="{ 'is-visible': isVisible(index) }"
      >
        <span class="grid h-8 w-8 shrink-0 place-items-center rounded-full border border-cyan-300/30 text-sm text-cyan-200">
          {{ index + 1 }}
        </span>
        <span class="text-lg">{{ step }}</span>
      </li>
    </ol>
  </section>
</template>

<style scoped>
.demo-cue h3 {
  margin: 0;
  max-width: 42rem;
  font-weight: 600;
}
</style>
