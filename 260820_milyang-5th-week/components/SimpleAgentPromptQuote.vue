<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'

const props = withDefaults(
  defineProps<{
    stage?: number
  }>(),
  {
    stage: 0
  }
)

const copied = ref(false)
const fullTextLine1 = "폴더에 있는 나의 경험 DB와 PDF를 분석해"
const fullTextLine2 = "전문적인 포트폴리오를 만들어줘."
const simplePrompt = `${fullTextLine1} ${fullTextLine2}`

const typedLine1 = ref('')
const typedLine2 = ref('')
const isTyping = ref(false)
let typingTimeout: any = null

function startTypingAnimation() {
  typedLine1.value = ''
  typedLine2.value = ''
  isTyping.value = true
  clearTimeout(typingTimeout)

  let idx1 = 0
  let idx2 = 0

  function typeFirst() {
    if (idx1 < fullTextLine1.length) {
      typedLine1.value += fullTextLine1[idx1]
      idx1++
      typingTimeout = setTimeout(typeFirst, 40)
    } else {
      typingTimeout = setTimeout(typeSecond, 180)
    }
  }

  function typeSecond() {
    if (idx2 < fullTextLine2.length) {
      typedLine2.value += fullTextLine2[idx2]
      idx2++
      typingTimeout = setTimeout(typeSecond, 40)
    } else {
      isTyping.value = false
    }
  }

  typeFirst()
}

function resetState() {
  clearTimeout(typingTimeout)
  typedLine1.value = ''
  typedLine2.value = ''
  isTyping.value = false
}

watch(
  () => props.stage,
  (newStage) => {
    if (newStage >= 1) {
      startTypingAnimation()
    } else {
      resetState()
    }
  }
)

function copyPrompt() {
  navigator.clipboard.writeText(simplePrompt).then(() => {
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  })
}

onMounted(() => {
  if (props.stage >= 1) {
    startTypingAnimation()
  } else {
    resetState()
  }
})

onUnmounted(() => {
  clearTimeout(typingTimeout)
})
</script>

<template>
  <div class="apple-typewriter-container w-full h-[335px] flex items-center justify-center select-none mt-1">
    <!-- Monolithic Apple Keynote Card -->
    <div class="relative w-full h-full rounded-3xl bg-[#08090C] text-white p-7 flex flex-col justify-between items-center text-center overflow-hidden border border-slate-800 shadow-2xl">
      
      <!-- Subtle Apple Ambient Radial Glow -->
      <div class="absolute -top-16 left-1/2 -translate-x-1/2 w-[550px] h-[240px] bg-gradient-to-b from-blue-600/20 via-indigo-600/10 to-transparent blur-3xl pointer-events-none" />

      <!-- Center Headline: Initial Blank with Cursor -> Click to Pure Text Typing (No Cursor) -->
      <div class="z-10 max-w-3xl my-auto px-4 min-h-[90px] flex flex-col justify-center items-center">
        <!-- Typed Prompt Headline -->
        <h2 class="text-2xl md:text-[28px] font-black tracking-tight text-white leading-snug m-0 drop-shadow-md min-h-[64px] flex flex-col justify-center items-center">
          <!-- Post-click: Clean text typing with NO cursor -->
          <template v-if="props.stage >= 1">
            <span class="text-white font-black">{{ typedLine1 }}</span>
            <span v-if="typedLine2.length > 0" class="text-emerald-300 font-black mt-0.5">
              {{ typedLine2 }}
            </span>
          </template>

          <!-- Pre-click Initial State: Pure Blinking Cursor Only -->
          <template v-else>
            <span class="typewriter-cursor text-emerald-400 text-3xl font-light">|</span>
          </template>
        </h2>

        <!-- Bottom Explanation: Always Mapped & Visible -->
        <p class="text-xs md:text-sm text-slate-300 mt-3 font-medium tracking-normal max-w-lg mx-auto leading-relaxed m-0">
          문법 암기도, 복잡한 프롬프트 엔지니어링도 필요 없습니다.<br />
          인간은 <b class="text-white font-bold">의도(Vibe)</b>만 던지고, 완제품은 <b class="text-emerald-400 font-bold">에이전트</b>가 만듭니다.
        </p>
      </div>

      <!-- Bottom Apple Frosted Glass Pill Button -->
      <div class="z-10">
        <button
          class="px-6 py-2.5 rounded-full text-xs font-bold tracking-tight transition-all duration-300 cursor-pointer flex items-center gap-2 border backdrop-blur-xl shadow-lg"
          :class="copied ? 'bg-emerald-500 text-white border-emerald-400 scale-105 shadow-emerald-500/25' : 'bg-white/15 hover:bg-white/25 text-white border-white/30 hover:border-white/50'"
          @click="copyPrompt"
        >
          <span>{{ copied ? '✓ 복사되었습니다' : '📋 프롬프트 복사하기' }}</span>
        </button>
      </div>

    </div>
  </div>
</template>

<style scoped>
.apple-typewriter-container {
  letter-spacing: -0.02em;
}

@keyframes blinkCursor {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.typewriter-cursor {
  display: inline-block;
  margin-left: 2px;
  font-weight: 300;
  animation: blinkCursor 0.8s infinite;
}
</style>
