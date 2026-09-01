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
  <div class="w-full h-full flex flex-col items-center justify-center select-none py-6 min-h-[420px]">
    <!-- Stage Transition Area -->
    <div class="relative w-full max-w-4xl flex items-center justify-center gap-10 my-auto">
      
      <!-- NotebookLM (Left / Center) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center rounded-2xl bg-white shadow-2xl p-6 border border-white/20"
        :class="[
          isTransformed
            ? 'w-84 h-48 opacity-90 scale-95 -translate-x-2'
            : 'w-96 h-52 opacity-100 scale-100 translate-x-0'
        ]"
      >
        <img
          src="/images.png"
          alt="NotebookLM"
          class="max-h-24 w-auto object-contain select-none pointer-events-none"
        />
      </div>

      <!-- Minimalist Arrow (Appears when stage >= 1) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center"
        :class="[
          isTransformed
            ? 'opacity-100 scale-100 translate-x-0 w-16'
            : 'opacity-0 scale-50 -translate-x-6 w-0 overflow-hidden pointer-events-none'
        ]"
      >
        <span class="i-carbon:arrow-right text-4xl text-cyan-400 font-bold"></span>
      </div>

      <!-- Gemini Notebook (Appears on Right when stage >= 1) -->
      <div
        class="transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] flex items-center justify-center rounded-2xl overflow-hidden shadow-2xl border border-cyan-500/30 bg-zinc-950 p-2"
        :class="[
          isTransformed
            ? 'w-88 h-48 opacity-100 scale-100 translate-x-2'
            : 'w-0 h-48 opacity-0 scale-75 translate-x-12 overflow-hidden pointer-events-none p-0 border-0'
        ]"
      >
        <img
          src="/Gemini-notebook-768x432.webp"
          alt="Gemini Notebook"
          class="w-full h-full object-cover select-none pointer-events-none rounded-xl"
        />
      </div>

    </div>
  </div>
</template>
