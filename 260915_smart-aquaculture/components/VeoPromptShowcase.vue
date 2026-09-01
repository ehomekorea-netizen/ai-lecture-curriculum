<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  videoSrc: string
  poster?: string
  aspectRatio?: '16/9' | '9/16'
  title: string
  badge?: string
  prompt: string
  subject?: string
  action?: string
  camera?: string
  environment?: string
  style?: string
  takeaway?: string
}>()

const copied = ref(false)

const copyPrompt = () => {
  navigator.clipboard.writeText(props.prompt)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<template>
  <div class="glass-card p-4 my-2 text-xs flex flex-col gap-3">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2.5">
      <div class="flex items-center gap-2">
        <span class="i-carbon-video-filled text-sky-400 text-base"></span>
        <span class="font-bold text-white text-sm">{{ title }}</span>
        <span v-if="badge" class="px-2 py-0.5 rounded text-[10.5px] font-mono font-bold bg-sky-500/20 text-sky-300 border border-sky-500/40">
          {{ badge }}
        </span>
      </div>
      <button
        class="px-2.5 py-1 rounded text-xs bg-white/10 hover:bg-white/20 text-white flex items-center gap-1.5 transition-all"
        @click="copyPrompt"
      >
        <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
        <span>{{ copied ? '복사됨!' : '공식 프롬프트 복사' }}</span>
      </button>
    </div>

    <!-- Main Grid: Video + Prompt Breakdown -->
    <div class="grid gap-4 items-start" :class="aspectRatio === '9/16' ? 'grid-cols-[200px_1fr]' : 'grid-cols-[1.1fr_1fr]'">
      <!-- Video Column -->
      <div class="relative rounded-xl overflow-hidden bg-black/60 border border-white/10 shadow-2xl flex items-center justify-center">
        <video
          :src="videoSrc"
          :poster="poster"
          autoplay
          loop
          muted
          playsinline
          class="w-full h-auto max-h-[300px] object-contain rounded-xl select-none"
        ></video>
      </div>

      <!-- Prompt Analysis Column -->
      <div class="flex flex-col gap-2.5">
        <!-- Raw Prompt Box -->
        <div class="bg-black/50 p-2.5 rounded-lg border border-white/10">
          <div class="text-[10px] font-mono uppercase tracking-wider text-sky-400 font-bold mb-1 flex items-center gap-1">
            <span class="i-carbon-terminal"></span>
            <span>Official DeepMind Prompt</span>
          </div>
          <p class="text-[11px] font-mono text-white/90 leading-relaxed italic m-0 line-clamp-3 hover:line-clamp-none transition-all">
            "{{ prompt }}"
          </p>
        </div>

        <!-- 5 Key Pillars -->
        <div class="grid grid-cols-2 gap-1.5 text-[10.5px]">
          <div v-if="subject" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-sky-300 font-bold">1. Subject (주체):</span>
            <p class="text-white/80 m-0 mt-0.5">{{ subject }}</p>
          </div>
          <div v-if="action" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-indigo-300 font-bold">2. Action (행동):</span>
            <p class="text-white/80 m-0 mt-0.5">{{ action }}</p>
          </div>
          <div v-if="camera" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-amber-300 font-bold">3. Camera (카메라):</span>
            <p class="text-white/80 m-0 mt-0.5">{{ camera }}</p>
          </div>
          <div v-if="environment" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-emerald-300 font-bold">4. Env (환경):</span>
            <p class="text-white/80 m-0 mt-0.5">{{ environment }}</p>
          </div>
        </div>

        <!-- Takeaway Insight Box -->
        <div v-if="takeaway" class="p-2 bg-sky-950/40 rounded-lg border border-sky-500/30 flex items-start gap-2">
          <span class="i-carbon-idea text-sky-400 text-sm flex-shrink-0 mt-0.5"></span>
          <p class="text-[11px] text-sky-200 leading-snug m-0">
            <strong>핵심 인사이트:</strong> {{ takeaway }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
