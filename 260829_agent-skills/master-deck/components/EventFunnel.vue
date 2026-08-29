<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  clicks?: number
}>(), {
  clicks: 0,
})

interface StageStation {
  id: string
  title: string
  subtitle: string
  icon: string
  click: number
  tone: 'cyan' | 'violet' | 'teal' | 'amber'
}

const stations: StageStation[] = [
  { id: 'signals', title: 'Signals & Context', subtitle: 'Chat, Memory, Events', icon: 'i-carbon:chip', click: 1, tone: 'cyan' },
  { id: 'plan', title: 'Attention & Plan', subtitle: 'Context Compression & Prompting', icon: 'i-carbon:idea', click: 2, tone: 'violet' },
  { id: 'execute', title: 'Task Execution', subtitle: 'Tool Dispatch & Output Validation', icon: 'i-carbon:tools', click: 3, tone: 'teal' },
]

const visibleStations = computed(() =>
  stations.filter(s => props.clicks >= s.click),
)
</script>

<template>
  <div class="relative w-full py-4 flex flex-col items-center">
    <div class="grid grid-cols-5 gap-3 items-center w-full max-w-4xl">
      <!-- Station 1 -->
      <article
        class="glass-card p-4 flex flex-col items-center text-center transition duration-500"
        :class="clicks >= 1 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 filter-blur-4'"
      >
        <span class="i-carbon:chip text-3xl text-cyan-400 mb-2" />
        <strong class="text-base text-white">Context Signals</strong>
        <span class="text-xs text-white/60 mt-1">Multi-modal Inputs</span>
      </article>

      <!-- Arrow 1 -->
      <div
        class="flex justify-center transition duration-500"
        :class="clicks >= 2 ? 'opacity-100 scale-100 text-cyan-400' : 'opacity-20 scale-75 text-white/20'"
      >
        <span class="i-carbon:arrow-right text-3xl animate-pulse" />
      </div>

      <!-- Station 2 -->
      <article
        class="glass-card p-4 flex flex-col items-center text-center transition duration-500"
        :class="clicks >= 2 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 filter-blur-4'"
      >
        <span class="i-carbon:idea text-3xl text-violet-400 mb-2" />
        <strong class="text-base text-white">Attention & Plan</strong>
        <span class="text-xs text-white/60 mt-1">Decision Surface</span>
      </article>

      <!-- Arrow 2 -->
      <div
        class="flex justify-center transition duration-500"
        :class="clicks >= 3 ? 'opacity-100 scale-100 text-violet-400' : 'opacity-20 scale-75 text-white/20'"
      >
        <span class="i-carbon:arrow-right text-3xl animate-pulse" />
      </div>

      <!-- Station 3 -->
      <article
        class="glass-card p-4 flex flex-col items-center text-center transition duration-500"
        :class="clicks >= 3 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4 filter-blur-4'"
      >
        <span class="i-carbon:tools text-3xl text-emerald-400 mb-2" />
        <strong class="text-base text-white">Task Executor</strong>
        <span class="text-xs text-white/60 mt-1">Reliable Side-effects</span>
      </article>
    </div>
  </div>
</template>
