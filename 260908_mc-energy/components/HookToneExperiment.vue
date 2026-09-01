<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'
import NumberIncreaser from './NumberIncreaser.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showNegative = computed(() => (props.stage ?? 0) >= 1)
const showPositive = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-center">
      <!-- Left: Direct Research Experiment Image (No Wrapper Shell) -->
      <div class="col-span-5 flex items-center justify-center">
        <img
          src="/0002820859_002_20260831071212490.jpg"
          alt="프롬프트 어조별 정답률 실험"
          class="rounded-xl w-full max-h-80 object-contain select-none"
        />
      </div>

      <!-- Right: Tone Comparison Cards (Clicks) -->
      <div class="col-span-7 flex flex-col justify-between space-y-3">
        <!-- Negative Tone -->
        <div
          class="transition-all duration-500 transform"
          :class="[showNegative ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
        >
          <LiquidGlass glow="pink" :radius="14">
            <div class="p-3.5 px-4 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between border-b border-rose-500/20 pb-2 mb-2">
                  <div class="flex items-center gap-2 text-rose-400 font-bold text-xs">
                    <span class="i-carbon:close-filled text-sm"></span>
                    <span>부정적 · 위협적 어조 ("틀리면 해고야")</span>
                  </div>
                  <div class="flex items-baseline gap-1 font-mono text-rose-300 font-black">
                    <span class="text-[10px] text-rose-400/70 font-normal">정답률</span>
                    <NumberIncreaser :value="56.6" :from="0" :duration="800" class-name="text-xl font-black text-rose-400" />
                    <span class="text-[10px]">%</span>
                  </div>
                </div>
                <p class="text-xs text-white/70 m-0 leading-relaxed">
                  과도한 감정 압박 시 방어적 토큰이 생성되며 정답률이 <strong>15% 이상 급락</strong>합니다.
                </p>
              </div>
            </div>
          </LiquidGlass>
        </div>

        <!-- Positive Tone -->
        <div
          class="transition-all duration-500 transform"
          :class="[showPositive ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
        >
          <LiquidGlass glow="emerald" :radius="14">
            <div class="p-3.5 px-4 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between border-b border-emerald-500/20 pb-2 mb-2">
                  <div class="flex items-center gap-2 text-emerald-400 font-bold text-xs">
                    <span class="i-carbon:checkmark-filled text-sm"></span>
                    <span>긍정적 · 역할 중심 어조 ("전문가처럼 답변하라")</span>
                  </div>
                  <div class="flex items-baseline gap-1 font-mono text-emerald-300 font-black">
                    <span class="text-[10px] text-emerald-400/70 font-normal">정답률</span>
                    <NumberIncreaser :value="71.9" :from="0" :duration="800" class-name="text-xl font-black text-emerald-400" />
                    <span class="text-[10px]">%</span>
                  </div>
                </div>
                <p class="text-xs text-white/80 m-0 leading-relaxed">
                  명확한 역할(Role) 부여 시 전문 도메인 가중치가 활성화되어 <strong>최상의 성능</strong>을 기록합니다.
                </p>
              </div>
            </div>
          </LiquidGlass>
        </div>

        <!-- Bottom Takeaway -->
        <div
          class="transition-all duration-500"
          :class="[showPositive ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
        >
          <LiquidGlass glow="cyan" :radius="12">
            <div class="p-2.5 px-3.5 flex items-center justify-between text-xs text-white/90">
              <div class="flex items-center gap-2">
                <span class="i-carbon:information-filled text-cyan-400"></span>
                <span><strong>핵심 결론:</strong> AI는 감정적 압박이 아닌 <strong>명확한 역할(Role)과 맥락(Context)</strong>에 반응합니다.</span>
              </div>
              <span class="text-[10px] font-mono text-cyan-300 font-bold">+15.3%p 격차</span>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>
