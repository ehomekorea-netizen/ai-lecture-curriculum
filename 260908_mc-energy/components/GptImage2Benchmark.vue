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
          src="/ChatGPT-Images-2.0-1.webp"
          alt="ChatGPT Images 2.0 Leaderboard Benchmark"
          class="rounded-2xl w-full max-h-76 object-contain select-none shadow-2xl"
        />
      </div>

      <!-- Right: Benchmark Takeaways & Insights -->
      <div class="col-span-6 flex flex-col justify-between h-82">
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-5 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/20 pb-2 mb-3">
                <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs">
                  <span class="i-carbon:trophy text-cyan-400 text-base"></span>
                  <span>비주얼 벤치마크 평가 분석</span>
                </div>
                <span class="text-[10px] font-mono text-cyan-300 font-bold px-2 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/30">Rank #1 (1,512 pts)</span>
              </div>

              <div class="space-y-2.5 text-xs">
                <div class="p-2.5 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-white text-[11px]">1. 2위 모델 대비 240+ 점 압도적 격차:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">단순 확산 모델(Diffusion)을 넘어선 추론형(Thinking) 비주얼 엔진의 압도적 정밀도</p>
                </div>
                <div class="p-2.5 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-blue-300 text-[11px]">2. 복잡한 다단계 지시어 이행력:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">인물 구도, 조명, 텍스트 배치, 서식 규칙 등 복합 요구조건을 왜곡 없이 정확하게 반영</p>
                </div>
                <div class="p-2.5 rounded-lg bg-black/40 border border-white/5">
                  <strong class="text-emerald-300 text-[11px]">3. 비즈니스 실무 투입 수준 달성:</strong>
                  <p class="text-[10.5px] text-white/75 m-0 mt-0.5 break-keep">사내 포스터, 홍보물, 소셜 카드뉴스 등 실무 인쇄 및 배포가 가능한 완성도</p>
                </div>
              </div>
            </div>

            <div
              class="pt-2 border-t border-cyan-500/20 text-[10.5px] font-mono text-cyan-200 transition-all duration-500 flex items-center justify-between"
              :class="[currentStage >= 1 ? 'opacity-100' : 'opacity-40']"
            >
              <span>✓ 글로벌 AI 이미지 생성 모델 1위 공인</span>
              <span class="font-bold">SOTA Verified</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
