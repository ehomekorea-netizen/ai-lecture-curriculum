<script setup lang="ts">
defineProps<{
  videoId?: string
}>()
</script>

<template>
  <div class="news-video-clean-wrapper w-full flex items-center justify-center mt-1 select-none">
    <!-- Clean Minimal Video Screen Container (Zero Overlay) -->
    <div class="relative w-full max-w-[780px] h-[360px] rounded-2xl overflow-hidden bg-black shadow-2xl border border-slate-800 flex items-center justify-center">
      <iframe
        :src="`https://www.youtube.com/embed/${videoId || 'Mq_zBMB8tN0'}?rel=0&modestbranding=1`"
        class="w-full h-full border-0"
        title="SBS News AI Job Market Report"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      />
    </div>
  </div>
</template>

<style scoped>
.news-video-clean-wrapper iframe {
  outline: none;
}
</style>
