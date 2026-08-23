<script setup lang="ts">
import { useNav } from '@slidev/client'
const { currentPage, total } = useNav()
</script>

<template>
  <footer v-if="currentPage > 1" class="absolute bottom-3 right-5 select-none pointer-events-none z-50">
    <span class="font-mono text-[11px] font-bold text-slate-400 tracking-wider">
      {{ currentPage }} / {{ total }}
    </span>
  </footer>
</template>