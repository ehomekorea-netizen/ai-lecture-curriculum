<script setup lang="ts">
withDefaults(defineProps<{
  src: string
  title: string
  subtitle?: string
  tag?: string
  poster?: string
  autoplay?: boolean
  loop?: boolean
  muted?: boolean
}>(), {
  autoplay: true,
  loop: true,
  muted: true,
})
</script>

<template>
  <div class="fade-video-slide">
    <video
      :src="src"
      :poster="poster"
      :autoplay="autoplay"
      :loop="loop"
      :muted="muted"
      playsinline
    />

    <div class="fade-heading">
      <div v-if="tag" class="text-xs font-mono text-cyan-300 uppercase tracking-widest mb-1.5">
        {{ tag }}
      </div>
      <h2 class="m-0 text-white text-3xl font-bold leading-tight drop-shadow-md">
        {{ title }}
      </h2>
      <p v-if="subtitle" class="mt-2 text-white/80 text-base leading-snug drop-shadow">
        {{ subtitle }}
      </p>
    </div>
  </div>
</template>
