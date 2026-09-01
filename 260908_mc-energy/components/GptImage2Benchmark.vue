<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

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

const capabilities = [
  {
    num: '①',
    title: 'Thinking (추론형 생성)',
    desc: '프롬프트를 깊이 생각하고, 웹 검색 및 레이아웃을 스스로 자가 수정(Self-Correction)하여 출력',
    tag: '추론 & 자가 보정',
    color: 'cyan',
  },
  {
    num: '②',
    title: '선명한 한글 텍스트 렌더링',
    desc: '기존 모델의 외계어/오타 문제를 완벽히 해결하여 사내 포스터와 안내문 한글을 인쇄물 수준으로 렌더링',
    tag: '한글 오타 제로',
    color: 'blue',
  },
  {
    num: '③',
    title: '3:1 ~ 1:3 자유 화면비 & 2K',
    desc: '가로 현수막(3:1)부터 인스타 릴스·유튜브 쇼츠(1:3 / 9:16)까지 2K 초고해상도로 자유 지원',
    tag: '2K 규격 제한 해제',
    color: 'violet',
  },
  {
    num: '④',
    title: '스타일 일관성 유지 (Multi-Image)',
    desc: '1번의 프롬프트로 동일한 브랜드 콘셉트와 캐릭터 화풍을 유지하며 최대 8장 연속 컷 생성',
    tag: '동일 톤앤매너 유지',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-5 items-stretch">
      <!-- Left: Benchmark Leaderboard & Model Selection Badge -->
      <div class="col-span-5 flex flex-col justify-between h-82">
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/20 pb-2 mb-2">
                <div class="flex items-center gap-2">
                  <span class="i-carbon:trophy text-cyan-400 text-base"></span>
                  <span class="text-xs font-bold text-cyan-300">비주얼 벤치마크 압도적 1위</span>
                </div>
                <span class="text-[10px] font-mono text-cyan-300 font-bold px-2 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/30">1,512 pts</span>
              </div>

              <!-- Leaderboard Image -->
              <div class="rounded-xl overflow-hidden bg-black/40 border border-white/10 p-1 mb-2">
                <img
                  src="/ChatGPT-Images-2.0-1.webp"
                  alt="ChatGPT Images 2.0 Leaderboard Benchmark"
                  class="w-full h-36 object-contain rounded-lg select-none"
                />
              </div>
            </div>

            <!-- Model Badge -->
            <div class="p-2 rounded-xl bg-black/40 border border-white/10 flex items-center justify-between text-xs">
              <div class="flex items-center gap-2">
                <span class="i-simple-icons:openai text-white text-base"></span>
                <span class="font-mono font-bold text-white text-xs">ChatGPT Images 2.0</span>
              </div>
              <span class="text-[10px] font-mono text-emerald-300 font-bold">gpt-image-2</span>
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: 4 Core Capabilities Grid -->
      <div class="col-span-7 grid grid-cols-2 gap-3 items-stretch h-82">
        <div
          v-for="(item, idx) in capabilities"
          :key="item.num"
          class="transition-all duration-500 transform"
          :class="[
            currentStage >= Math.floor(idx / 2) ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98',
          ]"
        >
          <LiquidGlass
            :glow="currentStage >= Math.floor(idx / 2) ? (item.color === 'cyan' ? 'cyan' : item.color === 'blue' ? 'blue' : item.color === 'violet' ? 'violet' : 'emerald') : 'neutral'"
            :radius="12"
            class="h-full"
          >
            <div class="p-3.5 flex flex-col justify-between h-38">
              <div>
                <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-1.5 whitespace-nowrap">
                  <span class="text-xs font-bold text-white">{{ item.num }} {{ item.title }}</span>
                </div>
                <p class="text-[10.5px] text-white/75 m-0 leading-relaxed break-keep">
                  {{ item.desc }}
                </p>
              </div>

              <div class="pt-1.5 border-t border-white/10 text-[9.5px] font-mono whitespace-nowrap font-bold" :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'">
                ✓ {{ item.tag }}
              </div>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>
