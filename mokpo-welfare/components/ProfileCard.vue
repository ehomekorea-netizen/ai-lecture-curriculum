<script setup lang="ts">
withDefaults(defineProps<{
  name: string
  role: string
  org?: string
  avatar?: string
  github?: string
  twitter?: string
  tags?: string[]
  click?: number
  clicks?: number
}>(), {
  click: 0,
  clicks: 0,
})
</script>

<template>
  <article
    class="glass-card p-6 flex flex-col items-center text-center transition duration-500 ease-out"
    :class="clicks >= click ? 'opacity-100 translate-y-0 filter-none' : 'opacity-0 translate-y-6 filter-blur-4 pointer-events-none'"
  >
    <img
      v-if="avatar"
      :src="avatar"
      :alt="name"
      class="w-28 h-28 mb-4 object-cover rounded-full border-2 border-white/20 shadow-lg"
    />
    <div v-else class="w-28 h-28 mb-4 rounded-full bg-gradient-to-tr from-cyan-500 to-violet-500 flex items-center justify-center text-3xl font-bold text-white shadow-lg">
      {{ name.slice(0, 2) }}
    </div>

    <h2 class="m-0 text-white text-2xl font-bold leading-tight tracking-tight">
      {{ name }}
    </h2>

    <div class="mt-1 text-white/70 text-sm font-medium">
      {{ role }} <span v-if="org" class="opacity-50">· {{ org }}</span>
    </div>

    <div v-if="github" class="mt-3 flex items-center gap-2 text-white/80 text-sm font-mono underline decoration-dashed decoration-white/40 underline-offset-4">
      <span class="i-ri:github-fill text-lg" /> {{ github }}
    </div>

    <div v-if="tags && tags.length" class="mt-4 flex flex-wrap justify-center gap-1.5">
      <span
        v-for="tag in tags"
        :key="tag"
        class="text-xs px-2.5 py-1 rounded-full bg-white/10 text-white/80 border border-white/10"
      >
        {{ tag }}
      </span>
    </div>
  </article>
</template>
