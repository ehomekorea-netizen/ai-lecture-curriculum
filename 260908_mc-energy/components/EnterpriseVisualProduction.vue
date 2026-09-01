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

const formats = [
  {
    num: '①',
    name: '사내 공지 & 웹 배너',
    ratio: '16:9 가로',
    desc: '인트라넷 공지, 주간 뉴스레터, 전사 대시보드 헤더용 와이드 비주얼',
    tag: '웹 & 인트라넷',
    color: 'cyan',
  },
  {
    num: '②',
    name: '엘리베이터 사이니지 & 포스터',
    ratio: '9:16 세로',
    desc: '신사옥 엘리베이터 디스플레이, 사내 게시판 인쇄용 고해상도 캠페인 포스터',
    tag: '사이니지 & 인쇄',
    color: 'blue',
  },
  {
    num: '③',
    name: '사내 메신저 & 카드뉴스',
    ratio: '1:1 정방형',
    desc: '사내 메신저 알림, 부서별 주요 업무 소식 및 요약 카드뉴스 이미지',
    tag: '모바일 & 메신저',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top 3-Channel Multi-Format Grid -->
    <div class="grid grid-cols-3 gap-4 items-stretch mb-3">
      <div
        v-for="item in formats"
        :key="item.name"
        class="transition-all duration-500 transform opacity-100 translate-y-0"
      >
        <LiquidGlass
          :glow="item.color === 'cyan' ? 'cyan' : item.color === 'blue' ? 'blue' : 'emerald'"
          :radius="14"
          class="h-full"
        >
          <div class="p-4 flex flex-col justify-between h-46">
            <div>
              <div class="flex items-center justify-between border-b border-white/10 pb-2 mb-2">
                <div class="flex items-center gap-1.5 text-xs font-bold text-white whitespace-nowrap">
                  <span>{{ item.num }} {{ item.name }}</span>
                </div>
                <span
                  class="text-[9.5px] font-mono font-bold px-2 py-0.5 rounded bg-black/40 border border-white/10"
                  :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : 'text-emerald-300'"
                >
                  {{ item.ratio }}
                </span>
              </div>
              <p class="text-[11px] text-white/75 m-0 leading-relaxed break-keep">
                {{ item.desc }}
              </p>
            </div>

            <div
              class="pt-1.5 border-t border-white/10 text-[10px] font-mono whitespace-nowrap font-bold"
              :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : 'text-emerald-300'"
            >
              ✓ {{ item.tag }}
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom: 3-Step Production Pipeline (Click 1 Focus) -->
    <div
      class="transition-all duration-500 transform"
      :class="[currentStage >= 1 ? 'opacity-100 translate-y-0 scale-100' : 'opacity-35 translate-y-1 scale-98']"
    >
      <LiquidGlass glow="neutral" :radius="14">
        <div class="p-3.5 px-5 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-3">
            <span class="i-carbon:workflow text-cyan-400 text-base"></span>
            <span class="break-keep">
              <strong>실무 완결 파이프라인:</strong>
              1. Images 2.0으로 2K 한글 포스터 생성 ➔ 2. @Canva 연동으로 채널별 리사이징 ➔ 3. 인쇄/배포용 원클릭 자산화
            </span>
          </div>
          <span class="text-[10px] font-mono text-emerald-300 font-bold whitespace-nowrap">1 Source Multi-Use</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
