<script setup lang="ts">
defineProps<{
  number?: string
  label?: string
}>()
</script>

<template>
  <div class="apple-fact-box flex flex-col items-center justify-center p-8 text-center bg-gray-950 text-white rounded-xl border border-gray-800 shadow-xl min-h-[180px]">
    <div class="my-auto space-y-2">
      <div v-if="number" class="text-5xl font-black tracking-tight text-white font-mono">
        {{ number }}
      </div>
      <div v-if="label" class="text-sm font-medium text-gray-400 tracking-wide uppercase">
        {{ label }}
      </div>
      <slot />
    </div>
  </div>
</template>
