<script setup lang="ts">
import { computed } from 'vue'
import AnimatedBrushUnderline from './AnimatedBrushUnderline.vue'

const props = withDefaults(defineProps<{
  part?: string
  title?: string
  subtitle?: string
  image?: string
  video?: string
}>(), {
  part: '1차시',
  title: '생성형 AI를 통한 실무능력 향상',
  subtitle: 'AI의 기본 작동 구조를 이해하고, 사실에 기반한 업무 결과물을 얻기 위한 프롬프트 작성법과 결과 검증 체계 확립',
  image: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop'
})

const base = import.meta.env.BASE_URL || '/'
const resolveMedia = (path?: string) => {
  if (!path) return ''
  if (path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

const resolvedVideo = computed(() => {
  const target = props.video || (props.image && props.image.endsWith('.mp4') ? props.image : '')
  return resolveMedia(target)
})

const resolvedImage = computed(() => resolveMedia(props.image))
</script>

<template>
  <div class="w-full h-full flex items-center justify-between gap-8 select-none font-sans text-left my-auto px-6 py-4" style="min-height: 380px;">
    <!-- Left Column: Title, Animated Underlines, Subtitle -->
    <div class="w-[54%] flex flex-col justify-center space-y-4">
      <!-- Part Tag (Optional) -->
      <div v-if="part">
        <span class="text-xs md:text-[13px] font-mono font-bold tracking-[0.25em] text-cyan-400 uppercase bg-cyan-500/10 border border-cyan-500/30 px-3 py-1 rounded-full">
          {{ part }}
        </span>
      </div>

      <!-- Main Title -->
      <div class="relative inline-block mt-2">
        <h1 class="text-4xl md:text-[44px] font-serif font-bold text-white leading-[1.18] tracking-tight mb-2 break-keep">
          {{ title }}
        </h1>

        <!-- Animated Hand-drawn Style Double Underlines -->
        <AnimatedBrushUnderline width="max-w-[480px]" />
      </div>

      <!-- Subtitle & Quote Box -->
      <div v-if="subtitle" class="p-4 rounded-xl border border-white/15 bg-white/5 backdrop-blur-md text-sm md:text-[15px] font-serif text-slate-300 leading-relaxed max-w-xl mt-4">
        {{ subtitle }}
      </div>
    </div>

    <!-- Right Column: Pure Media Frame -->
    <div class="w-[46%] flex items-center justify-center">
      <div class="w-full max-w-[460px] aspect-[16/10] rounded-2xl overflow-hidden flex items-center justify-center bg-black/40 border border-white/15 shadow-2xl">
        <!-- Looping Video Support -->
        <video
          v-if="video || (image && image.endsWith('.mp4'))"
          :src="resolvedVideo"
          autoplay
          loop
          muted
          playsinline
          class="w-full h-full object-cover rounded-2xl select-none"
        />
        <!-- Image Fallback -->
        <img
          v-else
          :src="resolvedImage"
          :alt="title"
          class="w-full h-full object-cover rounded-2xl select-none"
        />
      </div>
    </div>
  </div>
</template>
