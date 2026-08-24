<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'
import { X } from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const base = import.meta.env.BASE_URL || '/'
const resolveAsset = (path: string) => {
  if (!path || path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

interface VideoSegment {
  id: number
  name: string
  title: string
  desc: string
  start: number
  end: number
}

const segments: Record<number, VideoSegment> = {
  1: {
    id: 1,
    name: '출처 (Sources)',
    title: '📁 1. Sources: 자료 등록 및 맞춤 소스 관리',
    desc: 'PDF, 웹문서, 구글 드라이브 파일을 업로드하고 분석할 문서를 체크박스로 선택합니다.',
    start: 0.0,
    end: 15.0
  },
  2: {
    id: 2,
    name: '채팅 (Chat)',
    title: '💬 2. Chat: 자료 기반 심층 질의 & 출처 각주',
    desc: '문서 내용에 대해 질문하고, 답변 속 번호 각주 [1][2]를 클릭해 원문 해당 단락을 즉시 검증합니다.',
    start: 16.0,
    end: 25.0
  },
  3: {
    id: 3,
    name: '스튜디오 (Studio)',
    title: '✨ 3. Studio: 오디오 팟캐스트 & 브리핑 제작',
    desc: 'Deep Dive 오디오 팟캐스트, 스터디 가이드, 브리핑 문서를 원클릭으로 자동 생성합니다.',
    start: 26.0,
    end: 51.0
  }
}

const activeZone = ref<number | null>(null)
const videoRef = ref<HTMLVideoElement | null>(null)

// Sync with Slidev clicks ($clicks)
watch(() => props.stage, (newStage) => {
  if (typeof newStage === 'number') {
    if (newStage === 0) {
      closeVideo()
    } else if (newStage === 1) {
      playSegment(1)
    } else if (newStage === 2) {
      playSegment(2)
    } else if (newStage >= 3) {
      playSegment(3)
    }
  }
})

function playSegment(zoneId: number) {
  activeZone.value = zoneId
  const seg = segments[zoneId]
  if (!seg) return

  nextTick(() => {
    if (videoRef.value) {
      videoRef.value.currentTime = seg.start
      videoRef.value.play().catch(() => {})
    }
  })
}

function closeVideo() {
  if (videoRef.value) {
    videoRef.value.pause()
  }
  activeZone.value = null
}

function onTimeUpdate() {
  if (!videoRef.value || !activeZone.value) return
  const seg = segments[activeZone.value]
  if (!seg) return

  const cur = videoRef.value.currentTime
  // Loop precisely within the segment
  if (cur >= seg.end || cur < seg.start) {
    videoRef.value.currentTime = seg.start
    videoRef.value.play().catch(() => {})
  }
}
</script>

<template>
  <div class="w-full flex flex-col items-center justify-center h-[335px] select-none font-sans relative">
    <!-- ── 1. STATIC 3-SPLIT BASE VIEW ── -->
    <div
      class="h-[315px] rounded-xl overflow-hidden shadow-2xl relative bg-black flex items-center justify-center"
      style="aspect-ratio: 1910 / 912;"
    >
      <!-- Real UI Image -->
      <img
        :src="resolveAsset('/notebooklm-ui-3split.png')"
        alt="Gemini Notebook UI"
        class="w-full h-full object-fill block select-none"
      />

      <!-- Red Vertical Line 1 (Exact 25.63%) -->
      <div
        class="absolute top-0 bottom-0 left-[25.63%] w-[2.5px] bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.95)] z-10 pointer-events-none"
      />

      <!-- Red Vertical Line 2 (Exact 73.95%) -->
      <div
        class="absolute top-0 bottom-0 left-[73.95%] w-[2.5px] bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.95)] z-10 pointer-events-none"
      />

      <!-- Clickable Zone 1: 출처 (0% ~ 25.63%) -->
      <div
        @click="playSegment(1)"
        class="absolute top-0 bottom-0 left-0 w-[25.63%] cursor-pointer transition-colors duration-150 hover:bg-rose-500/15"
        title="1. 출처 (Sources) 시연 영상 재생 (0~15초)"
      />

      <!-- Clickable Zone 2: 채팅 (25.63% ~ 73.95%) -->
      <div
        @click="playSegment(2)"
        class="absolute top-0 bottom-0 left-[25.63%] w-[48.32%] cursor-pointer transition-colors duration-150 hover:bg-rose-500/15"
        title="2. 채팅 (Chat) 시연 영상 재생 (16~25초)"
      />

      <!-- Clickable Zone 3: 스튜디오 (73.95% ~ 100%) -->
      <div
        @click="playSegment(3)"
        class="absolute top-0 bottom-0 left-[73.95%] w-[26.05%] cursor-pointer transition-colors duration-150 hover:bg-rose-500/15"
        title="3. 스튜디오 (Studio) 시연 영상 재생 (26~51초)"
      />
    </div>

    <!-- ── 2. 85% FULL-SCREEN POPUP VIDEO MODAL ── -->
    <Teleport to="body">
      <Transition name="modal-pop">
        <div
          v-if="activeZone"
          @click.self="closeVideo"
          class="fixed inset-0 z-[999] bg-slate-950/85 backdrop-blur-md flex flex-col items-center justify-center p-4 cursor-pointer select-none font-sans"
        >
          <!-- Video Frame (85% Width, Pure Video Edge-to-Edge) -->
          <div
            @click.stop
            class="w-[880px] max-w-[92vw] aspect-video bg-black relative shadow-2xl overflow-hidden cursor-default flex items-center justify-center"
          >
            <!-- HTML5 Video Player (Zero Crop, Pure 16:9 Edge-to-Edge) -->
            <video
              ref="videoRef"
              :src="resolveAsset('/notebooklm-demo.mp4')"
              class="w-full h-full object-cover block select-none"
              @timeupdate="onTimeUpdate"
              playsinline
              muted
              autoplay
            />

            <!-- Top-Right Close Button (Pure X Circle) -->
            <button
              @click="closeVideo"
              class="absolute top-3 right-3 w-8 h-8 rounded-full bg-black/75 hover:bg-black text-white flex items-center justify-center cursor-pointer transition-transform hover:scale-110 shadow-lg z-30 border border-white/20"
              title="닫기"
            >
              <X :size="18" />
            </button>
          </div>

          <!-- Description Bar (Clean, Big & Highly Legible Text Outside Video at Bottom) -->
          <div
            @click.stop
            class="w-[880px] max-w-[92vw] mt-4 text-center text-white space-y-1.5 cursor-default"
          >
            <h3 class="text-2xl md:text-[26px] font-serif font-bold text-white tracking-tight leading-snug">
              {{ segments[activeZone]?.title }}
            </h3>
            <p class="text-base md:text-[17.5px] text-slate-200 font-sans font-medium leading-relaxed">
              {{ segments[activeZone]?.desc }}
            </p>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<style scoped>
video {
  outline: none;
  border: none;
}

.modal-pop-enter-active,
.modal-pop-leave-active {
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-pop-enter-from,
.modal-pop-leave-to {
  opacity: 0;
  transform: scale(0.97);
}
</style>
