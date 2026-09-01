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
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Direct Pure Image (No Unnecessary Glass Wrapper) -->
      <div class="col-span-6 flex flex-col justify-center items-center h-82">
        <img
          src="/image.inblog.webp"
          alt="ChatGPT Images 2.0 Korean Typography Showcase"
          class="rounded-2xl w-full max-h-76 object-cover select-none shadow-2xl"
        />
      </div>

      <!-- Right: Enterprise Poster Prompt Formula -->
      <div class="col-span-6 flex flex-col justify-between h-82">
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-5 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/20 pb-2 mb-2.5">
                <div class="flex items-center gap-2">
                  <span class="i-carbon:terminal text-cyan-400 text-base"></span>
                  <span class="text-xs font-bold text-white">사내 안내문 & 포스터 프롬프트 3요소</span>
                </div>
                <span class="text-[10px] font-mono text-cyan-300 font-bold">Prompt Formula</span>
              </div>

              <div class="space-y-2 text-xs">
                <div class="p-2 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-cyan-300 text-[11px]">1. 용도 & 상황 정의:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">사내 에너지 절감 캠페인 안내문, 안전 수칙 표지판 등 목적 명시</p>
                </div>
                <div class="p-2 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-blue-300 text-[11px]">2. 정확한 한글 텍스트 지정:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">포스터 상단에 "에너지 절감, 스마트한 실천" 문구를 명확히 인쇄</p>
                </div>
                <div class="p-2 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-emerald-300 text-[11px]">3. 비주얼 톤 & 규격 제약:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">2K 고화질, 미니멀 클린 인포그래픽 스타일, 세로형 9:16 비율</p>
                </div>
              </div>
            </div>

            <!-- Bottom Example Output Card -->
            <div
              class="pt-2 border-t border-cyan-500/20 text-[10.5px] font-mono text-cyan-200 transition-all duration-500 flex items-center justify-between"
              :class="[currentStage >= 1 ? 'opacity-100' : 'opacity-40']"
            >
              <span>✓ 사내 인트라넷 공지 및 엘리베이터 사이니지 즉시 배포</span>
              <span class="font-bold">Ready to Print</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
