<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue'

function handleGlobalFullscreenKey(e: KeyboardEvent) {
  // Ignore if user is currently typing in an input, textarea, or contenteditable element
  const target = e.target as HTMLElement | null
  const tag = target?.tagName?.toLowerCase()
  if (tag === 'input' || tag === 'textarea' || target?.isContentEditable) {
    return
  }

  // Toggle fullscreen on 'f' or 'F' keypress
  if (e.key === 'f' || e.key === 'F') {
    if (!e.ctrlKey && !e.metaKey && !e.altKey) {
      e.preventDefault()
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {})
      } else {
        document.exitFullscreen().catch(() => {})
      }
    }
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleGlobalFullscreenKey)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleGlobalFullscreenKey)
})
</script>

<template>
  <header
    v-if="$nav.currentPage !== 1 && $nav.currentLayout !== 'center' && $nav.currentLayout !== 'cover'"
    class="global-header"
  >
    <div class="header-right">
      <span class="page-index-badge">{{ $nav.currentPage }}</span>
    </div>
  </header>
</template>

<style scoped>
.global-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  padding: 0.8rem 1.6rem;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  pointer-events: none;
  z-index: 50;
}

.header-right {
  display: flex;
  align-items: center;
}

.page-index-badge {
  font-family: 'Geist Mono', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  color: #64748B;
  background: rgba(248, 250, 252, 0.9);
  border: 1px solid rgba(226, 232, 240, 0.9);
  backdrop-filter: blur(4px);
  padding: 2px 8px;
  border-radius: 6px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}
</style>
