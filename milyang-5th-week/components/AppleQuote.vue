<script setup lang="ts">
defineProps<{
  quote?: string
  author?: string
}>()
</script>

<template>
  <div class="apple-quote-box flex flex-col justify-center p-8 bg-gray-950 text-white rounded-xl border border-gray-800 shadow-xl min-h-[180px]">
    <blockquote class="my-auto space-y-4">
      <p class="text-xl italic font-serif leading-relaxed text-gray-100">
        "{{ quote || '수많은 훌륭한 아이디어도 단순하고 명확하게 전달될 때 비로소 혁신이 된다.' }}"
      </p>
      <footer v-if="author" class="text-sm font-semibold text-gray-400">
        — {{ author }}
      </footer>
      <slot />
    </blockquote>
  </div>
</template>
