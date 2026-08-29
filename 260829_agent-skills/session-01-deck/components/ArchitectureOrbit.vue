<script setup lang="ts">
export interface SatelliteNode {
  id: string
  title: string
  subtitle?: string
  icon?: string
  iconUrl?: string
  tone?: string
  click?: number
}

withDefaults(defineProps<{
  centerTitle: string
  centerSubtitle?: string
  centerIcon?: string
  nodes: SatelliteNode[]
  clicks?: number
}>(), {
  clicks: 0,
})
</script>

<template>
  <div class="relative w-full max-w-4xl mx-auto h-72 flex items-center justify-center my-4">
    <!-- Orbit circle path -->
    <div class="absolute w-64 h-64 rounded-full border border-white/15 border-dashed animate-spin animate-duration-30s pointer-events-none" />

    <!-- Center Core Node -->
    <div class="glass-card z-10 px-6 py-4 flex flex-col items-center text-center border-cyan-500/50 shadow-cyan-500/20 shadow-xl">
      <span v-if="centerIcon" :class="[centerIcon, 'text-3xl text-cyan-400 mb-1']" />
      <strong class="text-lg text-white font-bold">{{ centerTitle }}</strong>
      <span v-if="centerSubtitle" class="text-xs text-cyan-300/80 font-mono">{{ centerSubtitle }}</span>
    </div>

    <!-- Satellites around center -->
    <div class="absolute inset-0 flex items-center justify-between pointer-events-none">
      <div
        v-for="(node, idx) in nodes"
        :key="node.id"
        class="glass-card px-4 py-3 pointer-events-auto transition duration-500 flex items-center gap-3"
        :class="clicks >= (node.click ?? 0) ? 'opacity-100 translate-y-0 filter-none' : 'opacity-0 translate-y-4 filter-blur-4'"
      >
        <img v-if="node.iconUrl" :src="node.iconUrl" class="w-6 h-6 object-contain" alt="" />
        <span v-else-if="node.icon" :class="[node.icon, 'text-xl text-violet-400']" />
        <div class="flex flex-col text-left">
          <strong class="text-sm text-white">{{ node.title }}</strong>
          <span v-if="node.subtitle" class="text-xs text-white/60">{{ node.subtitle }}</span>
        </div>
      </div>
    </div>
  </div>
</template>
