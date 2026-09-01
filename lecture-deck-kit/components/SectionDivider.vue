<script setup lang="ts">
withDefaults(defineProps<{
  section?: string
  eyebrow?: string
  title: string
  subtitle?: string
}>(), {
  section: '01',
  eyebrow: 'Section',
  subtitle: '',
})
</script>

<template>
  <section class="section-divider">
    <div class="deck-kicker flex items-center gap-3">
      <span class="text-cyan-300/80">{{ section }}</span>
      <span class="h-px w-10 bg-white/20" />
      <span>{{ eyebrow }}</span>
    </div>
    <h1 class="mt-7 max-w-4xl">{{ title }}</h1>
    <p v-if="subtitle" class="mt-6 max-w-2xl text-xl deck-muted">
      {{ subtitle }}
    </p>
    <div class="deck-rule" />
  </section>
</template>

<style scoped>
.section-divider {
  max-width: 70rem;
}
</style>
