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
    <div class="grid grid-cols-12 gap-5 items-stretch">
      <!-- Left: Traditional Forward Method (Slow & Frustrating) -->
      <div class="col-span-5 flex flex-col justify-between h-82">
        <LiquidGlass glow="neutral" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-2.5">
                <div class="flex items-center gap-2 text-white/70 font-bold text-xs">
                  <span class="i-carbon:close-outline text-rose-400 text-base"></span>
                  <span>기존 정방향 방식 (비효율)</span>
                </div>
                <span class="text-[10px] font-mono text-white/40">수작업 탐색</span>
              </div>

              <div class="space-y-2 text-xs text-white/75">
                <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center gap-2">
                  <span class="text-rose-400 font-mono text-[10px]">1.</span>
                  <span class="break-keep">캔바 사이트에 직접 접속하여 백지 오픈</span>
                </div>
                <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center gap-2">
                  <span class="text-rose-400 font-mono text-[10px]">2.</span>
                  <span class="break-keep">수만 개 템플릿 검색창에서 시간 소모</span>
                </div>
                <div class="p-2 rounded bg-black/40 border border-white/5 flex items-center gap-2">
                  <span class="text-rose-400 font-mono text-[10px]">3.</span>
                  <span class="break-keep">기획 내용과 템플릿 레이아웃 불일치 발생</span>
                </div>
              </div>
            </div>

            <div class="text-[10.5px] font-mono text-rose-400/80 pt-1.5 border-t border-white/10">
              기획과 디자인이 따로 놀아 재작업 반복
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: 2026 Reverse Workflow (ChatGPT -> @Canva Instant Generation) -->
      <div
        class="col-span-7 flex flex-col justify-between h-82 transition-all duration-500 transform"
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="currentStage >= 1 ? 'cyan' : 'neutral'" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/20 pb-2 mb-2.5">
                <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs">
                  <span class="i-carbon:flash text-cyan-400 text-base"></span>
                  <span>2026 역방향 파이프라인 (대화창 @Canva)</span>
                </div>
                <span class="text-[10px] font-mono text-cyan-300 font-bold px-2 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/30">1초 템플릿</span>
              </div>

              <div class="space-y-2 text-xs">
                <div class="p-2 rounded-lg bg-black/40 border border-cyan-500/20 flex items-center justify-between">
                  <div class="flex items-center gap-2 text-white">
                    <span class="text-cyan-400 font-mono font-bold text-[10px]">Step 1</span>
                    <span class="break-keep">ChatGPT에서 기획서·카피라이팅 완성</span>
                  </div>
                  <span class="text-[10px] font-mono text-cyan-300">기획 완료</span>
                </div>
                <div class="p-2 rounded-lg bg-black/40 border border-cyan-500/20 flex items-center justify-between">
                  <div class="flex items-center gap-2 text-white">
                    <span class="text-blue-400 font-mono font-bold text-[10px]">Step 2</span>
                    <span class="break-keep">대화창에서 <strong>@Canva</strong> 호출 ➔ 맞춤형 템플릿 생성</span>
                  </div>
                  <span class="text-[10px] font-mono text-blue-300">다이렉트 생성</span>
                </div>
                <div class="p-2 rounded-lg bg-black/40 border border-emerald-500/20 flex items-center justify-between">
                  <div class="flex items-center gap-2 text-white">
                    <span class="text-emerald-400 font-mono font-bold text-[10px]">Step 3</span>
                    <span class="break-keep">생성된 링크 클릭 ➔ 캔바에서 폰트/로고만 1분 컷 피니시</span>
                  </div>
                  <span class="text-[10px] font-mono text-emerald-300 font-bold">원클릭 완성</span>
                </div>
              </div>
            </div>

            <div class="text-[10.5px] font-mono text-cyan-300 font-bold pt-1.5 border-t border-cyan-500/20 flex items-center justify-between">
              <span>✓ 기획 내용에 100% 맞춰진 완성형 디자인 직행</span>
              <span>Fast Track</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
