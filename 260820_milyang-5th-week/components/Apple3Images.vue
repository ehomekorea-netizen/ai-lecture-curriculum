<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  imageLeft?: string
  imageTopRight?: string
  imageBottomRight?: string
}>()

const leftStyle = computed(() => props.imageLeft ? { backgroundImage: `url(${props.imageLeft})`, backgroundSize: 'cover', backgroundPosition: 'center' } : { backgroundColor: '#1f2937' })
const topRightStyle = computed(() => props.imageTopRight ? { backgroundImage: `url(${props.imageTopRight})`, backgroundSize: 'cover', backgroundPosition: 'center' } : { backgroundColor: '#374151' })
const bottomRightStyle = computed(() => props.imageBottomRight ? { backgroundImage: `url(${props.imageBottomRight})`, backgroundSize: 'cover', backgroundPosition: 'center' } : { backgroundColor: '#4b5563' })
</script>

<template>
  <div class="apple-3images-grid grid grid-cols-2 gap-4 w-full h-full min-h-[220px] rounded-xl overflow-hidden bg-gray-950 p-4">
    <div class="rounded-lg border border-gray-800 shadow-md" :style="leftStyle" />
    <div class="grid grid-rows-2 gap-4 h-full">
      <div class="rounded-lg border border-gray-800 shadow-md" :style="topRightStyle" />
      <div class="rounded-lg border border-gray-800 shadow-md" :style="bottomRightStyle" />
    </div>
  </div>
</template>
