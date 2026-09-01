<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const isTransformed = computed(() => (props.stage ?? 0) >= 1)
</script>

<template>
  <div class="w-full h-full flex flex-col items-center justify-center select-none py-8 min-h-[420px]">
    <!-- Stage Transition Area -->
    <div class="relative w-full max-w-4xl flex items-center justify-center gap-10 my-auto">
      
      <!-- NotebookLM (Left / Center) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center rounded-3xl bg-white shadow-[0_25px_60px_-15px_rgba(0,0,0,0.7)] p-8 border border-white/20"
        :class="[
          isTransformed
            ? 'w-88 h-48 opacity-90 scale-95 -translate-x-2'
            : 'w-96 h-52 opacity-100 scale-100 translate-x-0'
        ]"
      >
        <img
          src="/images.png"
          alt="NotebookLM"
          class="max-h-24 w-auto object-contain select-none pointer-events-none"
        />
      </div>

      <!-- Minimalist Glowing Arrow (Appears when stage >= 1) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center"
        :class="[
          isTransformed
            ? 'opacity-100 scale-100 translate-x-0 w-16'
            : 'opacity-0 scale-50 -translate-x-6 w-0 overflow-hidden pointer-events-none'
        ]"
      >
        <span class="i-carbon:arrow-right text-4xl text-white/50 font-extralight"></span>
      </div>

      <!-- Gemini Notebook (Appears on Right when stage >= 1) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center rounded-3xl bg-white shadow-[0_25px_60px_-15px_rgba(6,182,212,0.25)] p-8 border border-white/30"
        :class="[
          isTransformed
            ? 'w-88 h-48 opacity-100 scale-100 translate-x-2'
            : 'w-0 h-48 opacity-0 scale-75 translate-x-12 overflow-hidden pointer-events-none p-0 border-0'
        ]"
      >
        <img
          src="/images.jpg"
          alt="Gemini Notebook"
          class="max-h-28 w-auto object-contain select-none pointer-events-none"
        />
      </div>

    </div>
  </div>
</template>
