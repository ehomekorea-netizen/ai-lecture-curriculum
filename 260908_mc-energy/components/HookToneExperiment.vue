<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'
import NumberIncreaser from './NumberIncreaser.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showPolite = computed(() => (props.stage ?? 0) >= 1)
const showDirect = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-center">
      <!-- Left: Research Experiment Data Image -->
      <div class="col-span-5 flex items-center justify-center">
        <img
          src="/0002820859_002_20260831071212490.jpg"
          alt="프롬프트 어조별 정답률 실험"
          class="rounded-xl w-full max-h-80 object-contain select-none"
        />
      </div>

      <!-- Right: Research Data Analysis Cards (Matches Image Data 100%) -->
      <div class="col-span-7 flex flex-col justify-between space-y-3">
        <!-- 1. Overly Polite Tone (80.8%) -->
        <div
          class="transition-all duration-500 transform"
          :class="[showPolite ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
        >
          <LiquidGlass glow="pink" :radius="14">
            <div class="p-3.5 px-4 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between border-b border-rose-500/20 pb-2 mb-2">
                  <div class="flex items-center gap-2 text-rose-400 font-bold text-xs">
                    <span class="i-carbon:close-filled text-sm"></span>
                    <span>과도하게 공손한 어조 ("검토해주시겠습니까")</span>
                  </div>
                  <div class="flex items-baseline gap-1 font-mono text-rose-300 font-black">
                    <span class="text-[10px] text-rose-400/70 font-normal">정답률</span>
                    <NumberIncreaser :value="80.8" :from="0" :duration="800" class-name="text-xl font-black text-rose-400" />
                    <span class="text-[10px]">%</span>
                  </div>
                </div>
                <p class="text-xs text-white/70 m-0 leading-relaxed">
                  불필요한 감정적 수식어와 공손 표현이 AI의 <strong>주의(Attention) 토큰을 분산</strong>시켜 정답률이 가장 낮게 나타났습니다.
                </p>
              </div>
            </div>
          </LiquidGlass>
        </div>

        <!-- 2. Direct / Blunt Prompt (84.8%) -->
        <div
          class="transition-all duration-500 transform"
          :class="[showDirect ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
        >
          <LiquidGlass glow="emerald" :radius="14">
            <div class="p-3.5 px-4 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between border-b border-emerald-500/20 pb-2 mb-2">
                  <div class="flex items-center gap-2 text-emerald-400 font-bold text-xs">
                    <span class="i-carbon:checkmark-filled text-sm"></span>
                    <span>단도직입적 · 직설적 지시 ("이것에 답해봐")</span>
                  </div>
                  <div class="flex items-baseline gap-1 font-mono text-emerald-300 font-black">
                    <span class="text-[10px] text-emerald-400/70 font-normal">정답률</span>
                    <NumberIncreaser :value="84.8" :from="0" :duration="800" class-name="text-xl font-black text-emerald-400" />
                    <span class="text-[10px]">%</span>
                  </div>
                </div>
                <p class="text-xs text-white/80 m-0 leading-relaxed">
                  감정적 미사여구 없이 <strong>핵심 요구조건과 맥락만 단도직입적으로 전달</strong>할 때 모델의 추론 집중도가 극대화됩니다.
                </p>
              </div>
            </div>
          </LiquidGlass>
        </div>

        <!-- Bottom Takeaway -->
        <div
          class="transition-all duration-500"
          :class="[showDirect ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
        >
          <LiquidGlass glow="cyan" :radius="12">
            <div class="p-2.5 px-3.5 flex items-center justify-between text-xs text-white/90">
              <div class="flex items-center gap-2">
                <span class="i-carbon:information-filled text-cyan-400"></span>
                <span><strong>핵심 시사점:</strong> AI에게는 예의보다 <strong>군더더기 없는 명확한 지시(Direct Prompting)</strong>가 성능을 결정합니다.</span>
              </div>
              <span class="text-[10px] font-mono text-cyan-300 font-bold">+4.0%p 격차</span>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>
