<script setup lang="ts">
export interface MetricItem {
  value: string | number
  label: string
  sublabel?: string
  prefix?: string
  suffix?: string
  tone?: 'emerald' | 'cyan' | 'violet' | 'amber' | 'rose'
  click?: number
}

withDefaults(defineProps<{
  metrics: MetricItem[]
  clicks?: number
}>(), {
  clicks: 0,
})

const toneColorMap: Record<string, string> = {
  emerald: 'text-emerald-400',
  cyan: 'text-cyan-400',
  violet: 'text-violet-400',
  amber: 'text-amber-400',
  rose: 'text-rose-400',
}
</script>

<template>
  <div class="grid grid-cols-3 gap-6 items-stretch w-full max-w-4xl mx-auto my-6">
    <article
      v-for="(item, idx) in metrics"
      :key="item.label"
      class="metric-card p-6 flex flex-col items-center text-center transition duration-500 ease-out"
      :class="clicks >= (item.click ?? 0) ? 'opacity-100 translate-y-0 filter-none' : 'opacity-0 translate-y-6 filter-blur-4 pointer-events-none'"
      :style="{ transitionDelay: `${idx * 150}ms` }"
    >
      <div class="text-4xl lg:text-5xl font-mono font-bold tracking-tight mb-2" :class="item.tone ? toneColorMap[item.tone] : 'text-white'">
        <span v-if="item.prefix" class="text-2xl mr-1">{{ item.prefix }}</span>
        <span>{{ item.value }}</span>
        <span v-if="item.suffix" class="text-2xl ml-1">{{ item.suffix }}</span>
      </div>

      <div class="text-base font-bold text-white leading-tight">
        {{ item.label }}
      </div>

      <div v-if="item.sublabel" class="text-xs text-white/60 mt-1">
        {{ item.sublabel }}
      </div>
    </article>
  </div>
</template>
