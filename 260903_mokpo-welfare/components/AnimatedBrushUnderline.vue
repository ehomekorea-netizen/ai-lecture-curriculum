<script setup lang="ts">
withDefaults(defineProps<{
  width?: string
  duration?: number
  delay?: number
}>(), {
  width: 'max-w-[480px]',
  duration: 1.4,
  delay: 0.2
})
</script>

<template>
  <div class="w-full relative mt-1 select-none overflow-visible" :class="width">
    <svg class="w-full h-4 overflow-visible" viewBox="0 0 450 14" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Blue Primary Brush Line (Smooth Hand-Drawn Stroke Animation) -->
      <path
        class="brush-stroke-blue"
        d="M 2 4 Q 120 1, 240 5 T 448 3"
        stroke="#3B82F6"
        stroke-width="3.2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <!-- Mint Green Accent Line (Layered Secondary Stroke Animation) -->
      <path
        class="brush-stroke-mint"
        d="M 12 10 Q 140 12, 260 8 T 420 11"
        stroke="#10B981"
        stroke-width="2.6"
        stroke-linecap="round"
        stroke-linejoin="round"
        opacity="0.9"
      />
    </svg>
  </div>
</template>

<style scoped>
.brush-stroke-blue {
  stroke-dasharray: 480;
  stroke-dashoffset: 480;
  animation: drawStroke 1.5s cubic-bezier(0.22, 1, 0.36, 1) 0.25s forwards;
}

.brush-stroke-mint {
  stroke-dasharray: 480;
  stroke-dashoffset: 480;
  animation: drawStroke 1.4s cubic-bezier(0.22, 1, 0.36, 1) 0.65s forwards;
}

@keyframes drawStroke {
  0% {
    stroke-dashoffset: 480;
  }
  100% {
    stroke-dashoffset: 0;
  }
}
</style>
