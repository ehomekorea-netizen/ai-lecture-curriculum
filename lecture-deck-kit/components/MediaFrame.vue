<script setup lang="ts">
withDefaults(defineProps<{
  src: string
  alt?: string
  kind?: 'image' | 'video'
  caption?: string
  contain?: boolean
  controls?: boolean
  autoplay?: boolean
  muted?: boolean
}>(), {
  alt: '',
  kind: 'image',
  caption: '',
  contain: true,
  controls: false,
  autoplay: false,
  muted: true,
})
</script>

<template>
  <figure class="deck-media">
    <img
      v-if="kind === 'image'"
      :src="src"
      :alt="alt"
      class="block max-h-full w-full"
      :class="contain ? 'object-contain' : 'object-cover'"
    >
    <video
      v-else
      :src="src"
      :controls="controls"
      :autoplay="autoplay"
      :muted="muted"
      playsinline
      class="block max-h-full w-full object-contain"
    />
    <figcaption v-if="caption" class="border-t border-white/10 px-4 py-2 text-xs deck-faint">
      {{ caption }}
    </figcaption>
  </figure>
</template>
