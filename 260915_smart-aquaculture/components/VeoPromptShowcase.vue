<script setup lang="ts">
import { ref, onMounted } from 'vue'

const props = withDefaults(
  defineProps<{
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
  }>(),
  {
    aspectRatio: '16/9'
  }
)

const videoRef = ref<HTMLVideoElement | null>(null)
const isMuted = ref(true)
const copied = ref(false)

onMounted(() => {
  if (videoRef.value) {
    videoRef.value.muted = true
    isMuted.value = true
    videoRef.value.play().catch(() => {})
  }
})

const toggleMute = () => {
  if (!videoRef.value) return
  videoRef.value.muted = !videoRef.value.muted
  isMuted.value = videoRef.value.muted
}

const copyPrompt = () => {
  navigator.clipboard.writeText(props.prompt)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<template>
  <div class="w-full my-0.5">
    <!-- 9:16 Vertical Layout (35% : 65%) -->
    <div
      v-if="aspectRatio === '9/16'"
      class="grid grid-cols-[35%_65%] gap-5 items-start"
    >
      <!-- Video Column (Pure Clean Video without internal overlays) -->
      <div class="flex flex-col">
        <div class="h-[310px] w-full flex items-center justify-center bg-black/60 rounded-2xl border border-white/20 overflow-hidden shadow-xl">
          <video
            ref="videoRef"
            :src="videoSrc"
            :poster="poster"
            autoplay
            loop
            muted
            playsinline
            class="w-full h-full object-contain select-none"
          ></video>
        </div>
        <!-- Controls outside video frame -->
        <div class="flex items-center justify-between mt-1.5 px-1">
          <span class="text-[10px] font-mono text-sky-400 font-medium">9:16 Shorts 포맷</span>
          <button
            @click.stop="toggleMute"
            class="px-2 py-0.5 rounded text-[10px] font-mono transition-all cursor-pointer border flex items-center gap-1"
            :class="isMuted ? 'bg-white/5 text-white/60 hover:text-white border-white/15' : 'bg-emerald-500/20 text-emerald-300 border-emerald-400'"
          >
            <span :class="isMuted ? 'i-carbon-volume-mute text-rose-400' : 'i-carbon-volume-up text-emerald-400'"></span>
            <span>{{ isMuted ? '음소거 중' : '소리 켜짐' }}</span>
          </button>
        </div>
      </div>

      <!-- Right Column: Clean Minimalist Breakdown -->
      <div class="flex flex-col gap-2">
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
          <div class="flex items-center gap-2">
            <span class="font-bold text-white text-[13.5px]">{{ title }}</span>
            <span
              v-if="badge"
              class="px-1.5 py-0.5 rounded text-[9.5px] font-mono font-bold bg-sky-500/20 text-sky-300 border border-sky-500/40"
            >
              {{ badge }}
            </span>
          </div>
          <button
            class="px-2 py-0.8 rounded text-[11px] bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 transition-all cursor-pointer border border-white/15"
            @click="copyPrompt"
          >
            <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
            <span>{{ copied ? '복사됨!' : '프롬프트 복사' }}</span>
          </button>
        </div>

        <!-- Official DeepMind Prompt -->
        <div class="p-2 rounded-xl bg-black/50 border border-white/10">
          <div class="text-[9px] font-mono uppercase tracking-wider text-sky-400 font-bold mb-0.5 flex items-center gap-1">
            <span class="i-carbon-terminal"></span>
            <span>Google Veo 3.1 공식 프롬프트</span>
          </div>
          <p class="text-[11px] font-mono text-white/95 leading-relaxed italic m-0">
            "{{ prompt }}"
          </p>
        </div>

        <!-- 4-Point Specs -->
        <div class="grid grid-cols-2 gap-1.5 text-[10.5px]">
          <div v-if="subject" class="p-1.5 bg-white/5 rounded-lg border border-white/10">
            <span class="text-sky-300 font-bold block text-[9.5px] mb-0.5">1. Subject (주체)</span>
            <span class="text-white/85 leading-snug">{{ subject }}</span>
          </div>
          <div v-if="action" class="p-1.5 bg-white/5 rounded-lg border border-white/10">
            <span class="text-indigo-300 font-bold block text-[9.5px] mb-0.5">2. Action (행동)</span>
            <span class="text-white/85 leading-snug">{{ action }}</span>
          </div>
          <div v-if="camera" class="p-1.5 bg-white/5 rounded-lg border border-white/10">
            <span class="text-amber-300 font-bold block text-[9.5px] mb-0.5">3. Camera (카메라)</span>
            <span class="text-white/85 leading-snug">{{ camera }}</span>
          </div>
          <div v-if="environment" class="p-1.5 bg-white/5 rounded-lg border border-white/10">
            <span class="text-emerald-300 font-bold block text-[9.5px] mb-0.5">4. Environment (환경)</span>
            <span class="text-white/85 leading-snug">{{ environment }}</span>
          </div>
        </div>

        <!-- Takeaway Insight Banner -->
        <div
          v-if="takeaway"
          class="px-2.5 py-1.5 bg-sky-950/40 rounded-xl border-l-3 border-l-sky-400 border-t border-r border-b border-sky-500/20 flex items-start gap-1.5"
        >
          <span class="i-carbon-idea text-sky-400 text-xs flex-shrink-0 mt-0.5"></span>
          <p class="text-[10px] text-sky-200 leading-snug m-0">
            <strong>핵심 포인트:</strong> {{ takeaway }}
          </p>
        </div>
      </div>
    </div>

    <!-- 16:9 Landscape Layout (46% : 54%) -->
    <div
      v-else
      class="grid grid-cols-[46%_54%] gap-4.5 items-start"
    >
      <!-- Video Column (Pure Clean Video without internal overlays) -->
      <div class="flex flex-col">
        <div class="h-[245px] w-full rounded-2xl overflow-hidden shadow-xl border border-white/20 bg-black/80 flex items-center justify-center">
          <video
            ref="videoRef"
            :src="videoSrc"
            :poster="poster"
            autoplay
            loop
            muted
            playsinline
            class="w-full h-full object-cover select-none"
          ></video>
        </div>
        <!-- Controls outside video frame -->
        <div class="flex items-center justify-between mt-1.5 px-1">
          <span class="text-[10px] font-mono text-teal-400 font-medium">16:9 와이드 영상</span>
          <button
            @click.stop="toggleMute"
            class="px-2 py-0.5 rounded text-[10px] font-mono transition-all cursor-pointer border flex items-center gap-1"
            :class="isMuted ? 'bg-white/5 text-white/60 hover:text-white border-white/15' : 'bg-emerald-500/20 text-emerald-300 border-emerald-400'"
          >
            <span :class="isMuted ? 'i-carbon-volume-mute text-rose-400' : 'i-carbon-volume-up text-emerald-400'"></span>
            <span>{{ isMuted ? '음소거 중' : '소리 켜짐' }}</span>
          </button>
        </div>
      </div>

      <!-- Right Column: Minimalist Breakdown -->
      <div class="flex flex-col gap-1.5">
        <!-- Header -->
        <div class="flex items-center justify-between border-b border-white/10 pb-1">
          <div class="flex items-center gap-1.5">
            <span class="font-bold text-white text-[12.5px]">{{ title }}</span>
            <span
              v-if="badge"
              class="px-1.5 py-0.5 rounded text-[9px] font-mono font-bold bg-teal-500/20 text-teal-300 border border-teal-500/40"
            >
              {{ badge }}
            </span>
          </div>
          <button
            class="px-2 py-0.5 rounded text-[10.5px] bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 transition-all cursor-pointer border border-white/15"
            @click="copyPrompt"
          >
            <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
            <span>{{ copied ? '복사됨!' : '프롬프트 복사' }}</span>
          </button>
        </div>

        <!-- Official DeepMind Prompt -->
        <div class="p-2 rounded-xl bg-black/50 border border-white/10">
          <div class="text-[9px] font-mono uppercase tracking-wider text-sky-400 font-bold mb-0.5 flex items-center gap-1">
            <span class="i-carbon-terminal"></span>
            <span>Google Veo 3.1 공식 프롬프트</span>
          </div>
          <p class="text-[10px] font-mono text-white/90 leading-relaxed italic m-0 line-clamp-3">
            "{{ prompt }}"
          </p>
        </div>

        <!-- 4-Point Specs -->
        <div class="grid grid-cols-2 gap-1 text-[9.5px]">
          <div v-if="subject" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-sky-300 font-bold block text-[9px]">1. Subject (주체)</span>
            <span class="text-white/85 leading-tight">{{ subject }}</span>
          </div>
          <div v-if="action" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-indigo-300 font-bold block text-[9px]">2. Action (행동)</span>
            <span class="text-white/85 leading-tight">{{ action }}</span>
          </div>
          <div v-if="camera" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-amber-300 font-bold block text-[9px]">3. Camera (카메라)</span>
            <span class="text-white/85 leading-tight">{{ camera }}</span>
          </div>
          <div v-if="environment" class="p-1.5 bg-white/5 rounded border border-white/10">
            <span class="text-emerald-300 font-bold block text-[9px]">4. Env (환경)</span>
            <span class="text-white/85 leading-tight">{{ environment }}</span>
          </div>
        </div>

        <!-- Takeaway Insight Banner -->
        <div
          v-if="takeaway"
          class="px-2 py-1 bg-sky-950/40 rounded-lg border-l-2 border-l-teal-400 border-t border-r border-b border-teal-500/20 flex items-start gap-1.5"
        >
          <span class="i-carbon-idea text-teal-400 text-xs flex-shrink-0 mt-0.5"></span>
          <p class="text-[9.5px] text-teal-200 leading-snug m-0">
            <strong>핵심 포인트:</strong> {{ takeaway }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

