<script setup lang="ts">
import { onMounted, nextTick } from 'vue'

declare global {
  interface Window {
    instgrm?: {
      Embeds: {
        process: () => void
      }
    }
  }
}

const props = withDefaults(
  defineProps<{
    postId?: string
    url?: string
  }>(),
  {
    postId: 'DYlyHEAFLR7',
    url: 'https://www.instagram.com/p/DYlyHEAFLR7/'
  }
)

const embedUrl = `https://www.instagram.com/p/${props.postId}/embed/`

onMounted(() => {
  if (!window.instgrm) {
    const s = document.createElement('script')
    s.src = '//www.instagram.com/embed.js'
    s.async = true
    s.onload = () => {
      window.instgrm?.Embeds.process()
    }
    document.head.appendChild(s)
  } else {
    nextTick(() => {
      window.instgrm?.Embeds.process()
    })
  }
})
</script>

<template>
  <div class="insta-exact-wrapper w-full h-[330px] flex items-center justify-center select-none">
    <!-- Outer Card Frame: Exact 3:4 Aspect Ratio of the Instagram Media Card -->
    <div class="insta-window rounded-2xl overflow-hidden border-0 bg-transparent shadow-2xl">
      <!-- Scaler Layer: Offsets 48px header and matches 440px media height perfectly -->
      <div class="insta-scaler">
        <iframe
          :src="embedUrl"
          class="insta-live-frame"
          frameborder="0"
          scrolling="no"
          allowtransparency="true"
          allow="encrypted-media"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.insta-exact-wrapper {
  width: 100%;
  height: 330px;
}

/* 3:4 Aspect Ratio Box (250px x 330px) */
.insta-window {
  width: 255px;
  height: 330px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 12px 28px -4px rgba(0, 0, 0, 0.12), 0 4px 10px -2px rgba(0, 0, 0, 0.05);
}

.insta-scaler {
  width: 330px;
  height: 520px;
  transform: scale(0.77);
  transform-origin: top left;
  margin-top: -48px; /* 인스타그램 상단 48px 프로필 헤더만 정밀하게 숨김 */
}

.insta-live-frame {
  width: 330px;
  height: 520px;
  border: none;
  display: block;
}
</style>
