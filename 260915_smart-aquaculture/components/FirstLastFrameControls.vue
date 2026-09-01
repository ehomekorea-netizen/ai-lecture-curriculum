<script setup lang="ts">
import { ref, onMounted } from 'vue'

const activeStep = ref<'all' | 'first' | 'video' | 'last'>('all')
const videoRef = ref<HTMLVideoElement | null>(null)
const isMuted = ref(true)

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
</script>

<template>
  <div class="w-full my-0.5 flex flex-col gap-2">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
      <div class="flex items-center gap-2">
        <span class="font-bold text-white text-[13.5px]">Veo 3.1 First & Last Frame 고정 생성 제어</span>
        <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
          Temporal Anchor
        </span>
      </div>
      <div class="flex items-center gap-1.5">
        <button
          class="px-2.5 py-1 rounded text-xs transition-all cursor-pointer border border-white/15"
          :class="activeStep === 'all' ? 'bg-white/20 text-white font-bold' : 'text-white/60 hover:text-white bg-white/5'"
          @click="activeStep = 'all'"
        >
          전체 보기
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs transition-all cursor-pointer border"
          :class="activeStep === 'first' ? 'bg-sky-500/20 text-sky-300 font-bold border-sky-400' : 'text-white/60 hover:text-white border-white/10 bg-white/5'"
          @click="activeStep = 'first'"
        >
          1. 시작 프레임
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs transition-all cursor-pointer border"
          :class="activeStep === 'video' ? 'bg-emerald-500/20 text-emerald-300 font-bold border-emerald-400' : 'text-white/60 hover:text-white border-white/10 bg-white/5'"
          @click="activeStep = 'video'"
        >
          2. 비디오 생성
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs transition-all cursor-pointer border"
          :class="activeStep === 'last' ? 'bg-purple-500/20 text-purple-300 font-bold border-purple-400' : 'text-white/60 hover:text-white border-white/10 bg-white/5'"
          @click="activeStep = 'last'"
        >
          3. 끝 프레임
        </button>
      </div>
    </div>

    <!-- 3-Column Visual Flow with Large Hero Media -->
    <div class="grid grid-cols-[1fr_auto_1.5fr_auto_1fr] items-center gap-3.5 my-1">
      <!-- 1. First Frame -->
      <div
        class="flex flex-col gap-1.5 p-2 rounded-2xl border transition-all"
        :class="activeStep === 'first' || activeStep === 'all' ? 'bg-sky-950/40 border-sky-400 shadow-xl' : 'bg-black/30 border-white/5 opacity-40'"
      >
        <div class="flex items-center justify-between text-xs">
          <span class="font-bold text-sky-400">First Frame (시작점)</span>
          <span class="font-mono text-white/50 text-[10px]">0.0s</span>
        </div>
        <div class="relative rounded-xl overflow-hidden border border-white/15 aspect-video bg-black/60 shadow-lg">
          <img src="/veo3/first.webp" alt="First Frame" class="w-full h-full object-cover select-none" />
        </div>
        <p class="text-[10px] text-white/80 m-0 leading-tight">
          인물 위치, 카메라 초기 화각, 조명 앵커 설정
        </p>
      </div>

      <!-- Arrow 1 -->
      <div class="flex flex-col items-center justify-center text-emerald-400">
        <span class="i-carbon-arrow-right text-2xl"></span>
      </div>

      <!-- 2. Video Centerpiece (Hero Asset) -->
      <div
        class="flex flex-col gap-1.5 p-2.5 rounded-2xl border transition-all"
        :class="activeStep === 'video' || activeStep === 'all' ? 'bg-emerald-950/40 border-emerald-400 shadow-2xl ring-1 ring-emerald-400/30' : 'bg-black/30 border-white/5 opacity-40'"
      >
        <div class="flex items-center justify-between text-xs">
          <span class="font-bold text-emerald-300 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
            AI Temporal Interpolation (보간 생성)
          </span>
          <span class="font-mono text-emerald-300 text-[10px] font-bold">Veo 3.1 (5s)</span>
        </div>
        <div class="relative rounded-xl overflow-hidden border border-white/20 aspect-video bg-black/80 shadow-2xl">
          <video
            ref="videoRef"
            src="/veo3/first-last-output.mp4"
            autoplay
            loop
            muted
            playsinline
            class="w-full h-full object-contain select-none"
          ></video>
        </div>
        <!-- Outside Controls -->
        <div class="flex items-center justify-between px-0.5">
          <p class="text-[10.5px] text-emerald-200 m-0 leading-tight">
            시작과 끝을 묶어 중간 움직임의 왜곡 방지
          </p>
          <button
            @click.stop="toggleMute"
            class="px-1.5 py-0.5 rounded text-[9.5px] font-mono transition-all cursor-pointer border flex items-center gap-1"
            :class="isMuted ? 'bg-white/5 text-white/60 hover:text-white border-white/15' : 'bg-emerald-500/20 text-emerald-300 border-emerald-400'"
          >
            <span :class="isMuted ? 'i-carbon-volume-mute text-rose-400' : 'i-carbon-volume-up text-emerald-400'"></span>
            <span>{{ isMuted ? '음소거 중' : '소리 켜짐' }}</span>
          </button>
        </div>
      </div>

      <!-- Arrow 2 -->
      <div class="flex flex-col items-center justify-center text-purple-400">
        <span class="i-carbon-arrow-right text-2xl"></span>
      </div>

      <!-- 3. Last Frame -->
      <div
        class="flex flex-col gap-1.5 p-2 rounded-2xl border transition-all"
        :class="activeStep === 'last' || activeStep === 'all' ? 'bg-purple-950/40 border-purple-400 shadow-xl' : 'bg-black/30 border-white/5 opacity-40'"
      >
        <div class="flex items-center justify-between text-xs">
          <span class="font-bold text-purple-400">Last Frame (도착점)</span>
          <span class="font-mono text-white/50 text-[10px]">5.0s</span>
        </div>
        <div class="relative rounded-xl overflow-hidden border border-white/15 aspect-video bg-black/60 shadow-lg">
          <img src="/veo3/last.webp" alt="Last Frame" class="w-full h-full object-cover select-none" />
        </div>
        <p class="text-[10px] text-white/80 m-0 leading-tight">
          최종 구도 및 다음 쇼트(S02) 연결용 착지점 확정
        </p>
      </div>
    </div>

    <!-- Summary Box -->
    <div class="p-2.5 bg-black/50 rounded-xl border border-white/10 flex items-center justify-between text-xs">
      <div class="flex items-center gap-2">
        <span class="i-carbon-checkmark-filled text-emerald-400 text-base"></span>
        <span class="text-white/90">
          <strong>수산업 쇼트 제작 적용:</strong> 수조 외경(S01) ➔ 센서 근접(S02) 연결 시 끝 프레임을 고정하여 장면 이탈 방지
        </span>
      </div>
      <span class="text-white/50 font-mono text-[10.5px]">Deterministic Transition</span>
    </div>
  </div>
</template>
