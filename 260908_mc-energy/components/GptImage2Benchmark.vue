<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const slideContext = useSlideContext()
const currentStage = computed(() => {
  const ctxClicks = slideContext?.$clicks?.value ?? slideContext?.$nav?.clicks ?? 0
  return Math.max(props.stage ?? 0, ctxClicks)
})

const isExpanded = computed(() => currentStage.value >= 1)

const coreInsights = [
  {
    title: '1. Text-to-Image Arena 글로벌 1위 (1,512 pts)',
    desc: '2위 Nano Banana 2(1,271점), 3위 Nano Banana Pro(1,244점) 대비 240+ 점의 압도적 격차 기록',
    tag: 'SOTA 1위 달성',
    color: 'cyan',
  },
  {
    title: '2. 99% 수준의 텍스트 렌더링 정확도',
    desc: '기존 확산 모델의 최대 난제였던 다국어·한글 텍스트 및 곡면/라벨 타이포그래피를 완벽 인쇄',
    tag: '오타·깨짐 완전 극복',
    color: 'blue',
  },
  {
    title: '3. 자기회귀(Autoregressive) 추론 엔진',
    desc: '단순 노이즈 제거(Diffusion)가 아닌 프롬프트의 복합 제약조건을 사전 추론하고 자가 보정',
    tag: '추론형 생성 엔진',
    color: 'violet',
  },
  {
    title: '4. 인위적 AI 틴트(AI Tint/Look) 제거',
    desc: '누런 색조와 과장된 플라스틱 광택을 걷어내고 실무 포스터에 바로 쓰는 고화질 포토리얼리즘 완성',
    tag: '실무 인쇄급 화질',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Interactive Image Switch (Click 0: Top 5 -> Click 1: Full 15 Leaderboard) -->
      <div class="col-span-5 flex flex-col justify-center items-center h-82 relative">
        <!-- Top 5 Image (Click 0) -->
        <transition name="fade">
          <div v-if="!isExpanded" class="w-full h-full flex flex-col justify-center items-center">
            <img
              src="/ChatGPT-Images-2.0-1.webp"
              alt="ChatGPT Images 2.0 Leaderboard Top 5"
              class="rounded-2xl w-full max-h-78 object-contain select-none shadow-2xl transition-all duration-500"
            />
            <div class="text-[10px] font-mono text-cyan-300/70 mt-1">
              Top 5 리더보드 요약 (클릭 시 1~15위 전체 랭킹 확장)
            </div>
          </div>
        </transition>

        <!-- Full 15 Leaderboard Image (Click 1) -->
        <transition name="fade">
          <div v-if="isExpanded" class="w-full h-full flex flex-col justify-center items-center">
            <img
              src="/GPT-image-2.webp"
              alt="Text-to-Image Arena Full Leaderboard #1"
              class="rounded-2xl w-full max-h-78 object-contain select-none shadow-2xl transition-all duration-500"
            />
            <div class="text-[10px] font-mono text-emerald-300 font-bold mt-1">
              Arena.ai 공식 Text-to-Image 전체 15대 모델 비교
            </div>
          </div>
        </transition>
      </div>

      <!-- Right: Structured Analytics Vidhya Insights Grid -->
      <div class="col-span-7 flex flex-col justify-between h-82">
        <div class="grid grid-cols-2 gap-3.5 items-stretch flex-1 mb-2">
          <div
            v-for="item in coreInsights"
            :key="item.title"
            class="p-3.5 rounded-xl bg-white/5 border border-white/10 flex flex-col justify-between h-34"
          >
            <div>
              <div class="border-b border-white/10 pb-1 mb-1.5 whitespace-nowrap">
                <strong class="text-xs text-white">{{ item.title }}</strong>
              </div>
              <p class="text-[10.5px] text-white/80 m-0 leading-relaxed break-keep">
                {{ item.desc }}
              </p>
            </div>

            <div
              class="pt-1 border-t border-white/10 text-[9.5px] font-mono whitespace-nowrap font-bold"
              :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'"
            >
              ✓ {{ item.tag }}
            </div>
          </div>
        </div>

        <!-- Bottom Source Bar -->
        <div class="p-2 rounded-lg bg-black/40 border border-white/10 flex items-center justify-between text-[10px] text-white/60">
          <span class="font-mono">Source: Arena.ai & Analytics Vidhya (2026.04)</span>
          <span class="font-mono text-cyan-300 font-bold">Autoregressive vs Diffusion</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scale(0.97);
}
</style>
