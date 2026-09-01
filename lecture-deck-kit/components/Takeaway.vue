<script setup lang="ts">
withDefaults(defineProps<{
  kicker?: string
  title: string
  detail?: string
}>(), {
  kicker: 'Takeaway',
  detail: '',
})
</script>

<template>
  <section class="mx-auto max-w-5xl text-center">
    <div class="deck-kicker text-cyan-200/80">{{ kicker }}</div>
    <h1 class="mt-7 text-6xl! leading-tight!">{{ title }}</h1>
    <p v-if="detail" class="mx-auto mt-6 max-w-3xl text-xl deck-muted">
      {{ detail }}
    </p>
    <div class="deck-rule mx-auto" />
  </section>
</template>
