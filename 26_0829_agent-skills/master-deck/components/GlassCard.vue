<script setup lang="ts">
import { computed } from 'vue'

export interface CardItem {
  title: string
  subtitle?: string
  description?: string
  icon?: string
  iconUrl?: string
  tone?: 'emerald' | 'cyan' | 'violet' | 'amber' | 'rose' | 'sky' | 'teal'
  click?: number
  delay?: number
}

const props = withDefaults(defineProps<{
  items: CardItem[]
  cols?: number
  clicks?: number
}>(), {
  cols: 3,
  clicks: 0,
})

const toneBorderMap: Record<string, string> = {
  emerald: 'border-emerald-500/40 text-emerald-400',
  cyan: 'border-cyan-500/40 text-cyan-400',
  violet: 'border-violet-500/40 text-violet-400',
  amber: 'border-amber-500/40 text-amber-400',
  rose: 'border-rose-500/40 text-rose-400',
  sky: 'border-sky-500/40 text-sky-400',
  teal: 'border-teal-500/40 text-teal-400',
}

const gridColsClass = computed(() => {
  if (props.cols === 2) return 'grid-cols-2'
  if (props.cols === 4) return 'grid-cols-4'
  return 'grid-cols-3'
})
</script>

<template>
  <div class="grid gap-5 items-stretch" :class="gridColsClass">
    <article
      v-for="(item, idx) in items"
      :key="item.title"
      class="glass-card flex flex-col p-5 transition duration-500 ease-out"
      :class="[
        clicks >= (item.click ?? 0) ? 'opacity-100 translate-y-0 filter-none' : 'opacity-0 translate-y-4 filter-blur-4 pointer-events-none',
        item.tone ? toneBorderMap[item.tone] : '',
      ]"
      :style="{ transitionDelay: `${item.delay ?? idx * 100}ms` }"
    >
      <div class="flex items-center gap-3 mb-3">
        <img v-if="item.iconUrl" :src="item.iconUrl" class="w-8 h-8 object-contain" alt="" />
        <span v-else-if="item.icon" :class="[item.icon, 'text-2xl']" />
        <div v-if="item.subtitle" class="text-xs uppercase tracking-wider opacity-60 font-mono">
          {{ item.subtitle }}
        </div>
      </div>

      <h3 class="m-0 text-lg font-bold text-white leading-tight">
        {{ item.title }}
      </h3>

      <p v-if="item.description" class="mt-2 text-sm text-white/70 leading-relaxed">
        {{ item.description }}
      </p>
    </article>
  </div>
</template>
