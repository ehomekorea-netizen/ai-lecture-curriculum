<script setup lang="ts">
import { ref, onMounted } from 'vue'

const videoEl = ref<HTMLVideoElement | null>(null)

onMounted(() => {
  if (videoEl.value) {
    // 최초 도달 시: 정지 상태 & 음소거 OFF(소리 켜짐 대기)
    videoEl.value.pause()
    videoEl.value.muted = false
    videoEl.value.volume = 1.0
  }
})
</script>

<template>
  <div class="manus-video-clean-wrapper w-full flex items-center justify-center mt-1 select-none">
    <!-- Clean Minimal Video Screen Container (Zero Overlay) -->
    <div class="relative w-full max-w-[780px] h-[360px] rounded-2xl overflow-hidden bg-black shadow-2xl border border-slate-800 flex items-center justify-center">
      <video
        ref="videoEl"
        src="/video/Manus_web_intro.mp4"
        class="w-full h-full object-contain"
        preload="auto"
        controls
        playsinline
      />
    </div>
  </div>
</template>

<style scoped>
.manus-video-clean-wrapper video {
  outline: none;
}
</style>
