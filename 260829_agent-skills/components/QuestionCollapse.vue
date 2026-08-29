<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  question: string
  subQuestion?: string
  answerTitle?: string
  answerBody?: string
  clicks?: number
  threshold?: number
}>(), {
  clicks: 0,
  threshold: 1,
})

const isCollapsed = computed(() => (props.clicks ?? 0) >= props.threshold)
</script>

<template>
  <div class="relative w-full h-full flex flex-col">
    <!-- Question Header / Central Banner -->
    <div
      class="transition-all duration-600 ease-out"
      :class="[
        isCollapsed
          ? 'translate-y-0 opacity-70 scale-90 mb-4 text-left border-b border-white/10 pb-3'
          : 'translate-y-24 text-center scale-100 mb-0'
      ]"
    >
      <div v-if="subQuestion" class="text-sm font-mono text-cyan-400/90 uppercase tracking-widest mb-2">
        {{ subQuestion }}
      </div>
      <h2
        class="m-0 text-white font-bold leading-tight transition-all duration-600"
        :class="isCollapsed ? 'text-2xl' : 'text-4xl lg:text-5xl'"
      >
        {{ question }}
      </h2>
    </div>

    <!-- Collapsed Unfold Content Slot -->
    <div
      class="flex-1 transition-all duration-600 ease-out"
      :class="[
        isCollapsed
          ? 'opacity-100 translate-y-0 filter-none'
          : 'opacity-0 translate-y-6 filter-blur-6 pointer-events-none'
      ]"
    >
      <slot>
        <div v-if="answerTitle || answerBody" class="glass-card p-6 mt-4">
          <h3 v-if="answerTitle" class="text-xl font-bold text-emerald-400 mb-2">
            {{ answerTitle }}
          </h3>
          <p v-if="answerBody" class="text-base text-white/80 leading-relaxed">
            {{ answerBody }}
          </p>
        </div>
      </slot>
    </div>
  </div>
</template>
