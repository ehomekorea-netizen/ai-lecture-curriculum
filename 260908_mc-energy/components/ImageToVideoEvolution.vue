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
      <!-- Left: Static Poster (ChatGPT Images 2.0) -->
      <div class="col-span-6 flex flex-col justify-between h-82">
        <LiquidGlass glow="blue" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-blue-500/20 pb-2 mb-2">
                <div class="flex items-center gap-2 text-blue-300 font-bold text-xs">
                  <span class="i-carbon:image text-base"></span>
                  <span>1. 정적 안내문·포스터 (Images 2.0)</span>
                </div>
                <span class="text-[10px] font-mono text-blue-300 font-bold">Static Asset</span>
              </div>

              <div class="p-3 rounded-xl bg-black/40 border border-white/5 space-y-1.5 text-xs text-white/80">
                <div class="flex items-center gap-1.5 text-blue-300 font-bold text-[11px]">
                  <span class="i-carbon:checkmark-filled"></span>
                  <span>사내 인트라넷 공지 및 엘리베이터 사이니지</span>
                </div>
                <p class="text-[10.5px] text-white/70 m-0 break-keep leading-relaxed">
                  2K 초고해상도 한글 타이포그래피로 인쇄물 및 웹 공지용으로 즉시 배포.
                </p>
                <div class="p-1.5 rounded bg-blue-950/60 border border-blue-500/30 text-[10px] font-mono text-blue-200">
                  산출물: 사내_에너지절감_안내문.png
                </div>
              </div>
            </div>

            <div class="text-[10px] font-mono text-blue-300/80 pt-1.5 border-t border-white/10">
              정적 시각 자산 확보
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: 15-Second Motion Video (Canva Video Extension) -->
      <div
        class="col-span-6 flex flex-col justify-between h-82 transition-all duration-500 transform"
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
      >
        <LiquidGlass :glow="currentStage >= 1 ? 'emerald' : 'neutral'" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center justify-between border-b border-emerald-500/20 pb-2 mb-2">
                <div class="flex items-center gap-2 text-emerald-300 font-bold text-xs">
                  <span class="i-carbon:video text-base"></span>
                  <span>2. 15초 홍보 숏폼 영상 (@Canva 연동)</span>
                </div>
                <span class="text-[10px] font-mono text-emerald-300 font-bold">9:16 Motion</span>
              </div>

              <div class="p-3 rounded-xl bg-black/40 border border-emerald-500/20 space-y-1.5 text-xs text-white/80">
                <div class="flex items-center gap-1.5 text-emerald-300 font-bold text-[11px]">
                  <span class="i-carbon:play-filled-alt"></span>
                  <span>사내 릴스 / 메신저 / 유튜브 쇼츠 홍보</span>
                </div>
                <p class="text-[10.5px] text-white/70 m-0 break-keep leading-relaxed">
                  동일한 포스터 기획 소스를 캔바에서 모션 자막, 배경음악, 컷 전환을 더해 생동감 넘치는 15초 영상으로 변환.
                </p>
                <div class="p-1.5 rounded bg-emerald-950/60 border border-emerald-500/30 text-[10px] font-mono text-emerald-200">
                  산출물: 15초_캠페인_홍보영상.mp4
                </div>
              </div>
            </div>

            <div class="text-[10px] font-mono text-emerald-300 font-bold pt-1.5 border-t border-emerald-500/20 flex items-center justify-between">
              <span>✓ 단 1번의 기획으로 포스터와 영상 동시 완결</span>
              <span>1 Source Multi-Use</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
