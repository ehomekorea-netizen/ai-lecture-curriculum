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
    title: 'Thinking (추론형 비주얼 생성)',
    desc: '프롬프트를 깊이 생각하고, 웹 검색 및 레이아웃을 스스로 검토·자가 수정(Self-Correction)하여 출력',
    tag: '추론 & 자가 보정',
    color: 'cyan',
  },
  {
    num: '②',
    title: '선명한 다국어·한글 텍스트 인쇄',
    desc: '기존의 외계어/오타 문제를 완벽히 해결하여 사내 포스터와 안내문 속 한글을 인쇄물 수준으로 렌더링',
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
      <!-- Left: Pure Raw Images (No Unnecessary Glass Wrapper) -->
      <div class="col-span-4 flex flex-col justify-between h-82">
        <div class="flex-1 flex flex-col justify-center">
          <img
            src="/gpt image 2.0.jpeg"
            alt="OpenAI GPT Image 2.0 Poster"
            class="rounded-xl w-full max-h-66 object-contain select-none shadow-2xl"
          />
        </div>
        <div class="mt-2">
          <img
            src="/Step-one-select-gpt-image-2-model.avif"
            alt="Select GPT Image 2.0 Model"
            class="rounded-lg w-full max-h-12 object-contain select-none bg-black/40 border border-white/10 p-1"
          />
        </div>
      </div>

      <!-- Right: 4 Core Capabilities Grid -->
      <div class="col-span-8 grid grid-cols-2 gap-3 items-stretch h-82">
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
