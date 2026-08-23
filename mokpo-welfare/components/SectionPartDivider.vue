<script setup lang="ts">
import AnimatedBrushUnderline from './AnimatedBrushUnderline.vue'

const props = withDefaults(defineProps<{
  part?: string
  title?: string
  subtitle?: string
  image?: string
  video?: string
}>(), {
  part: '',
  title: '생성형 AI의 본질에서 AI 에이전트까지',
  subtitle: '규칙 기반 소프트웨어에서 확률적 생성, 그리고 스스로 일하는 에이전트로의 진화',
  image: '/adobestock-556454258_1920-1080.avif'
})
</script>

<template>
  <div class="w-full h-full flex items-center justify-between gap-8 select-none font-sans text-left my-auto" style="min-height: 380px;">
    <!-- Left Column: Title, Animated Underlines, Subtitle -->
    <div class="w-[54%] flex flex-col justify-center space-y-4">
      <!-- Part Tag (Optional) -->
      <div v-if="part">
        <span class="text-xs md:text-[13px] font-mono font-bold tracking-[0.25em] text-blue-600 uppercase">
          {{ part }}
        </span>
      </div>

      <!-- Main Serif Title -->
      <div class="relative inline-block">
        <h1 class="text-4xl md:text-[46px] font-serif font-bold text-slate-900 leading-[1.15] tracking-tight mb-2 break-keep">
          {{ title }}
        </h1>

        <!-- Animated Hand-drawn Style Double Underlines (Smooth Brushstroke) -->
        <AnimatedBrushUnderline width="max-w-[480px]" />
      </div>

      <!-- Subtitle & Quote Box -->
      <div v-if="subtitle" class="quote-box text-sm md:text-base font-serif text-slate-700 leading-relaxed max-w-xl mt-3">
        {{ subtitle }}
      </div>
    </div>

    <!-- Right Column: Pure Media Frame (No Borders, Clean Rounded Shape) -->
    <div class="w-[46%] flex items-center justify-center">
      <div class="w-full max-w-[460px] aspect-[16/10] rounded-2xl overflow-hidden flex items-center justify-center bg-transparent">
        <!-- Looping Video Support -->
        <video
          v-if="video || (image && image.endsWith('.mp4'))"
          :src="video || image"
          autoplay
          loop
          muted
          playsinline
          class="w-full h-full object-cover rounded-2xl select-none"
        />
        <!-- Image Fallback -->
        <img
          v-else
          :src="image"
          :alt="title"
          class="w-full h-full object-cover rounded-2xl select-none"
        />
      </div>
    </div>
  </div>
</template>
