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
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Negative / Threatening Tone -->
      <div
        class="col-span-6 transition-all duration-500 transform"
        :class="[showNegative ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
      >
        <LiquidGlass glow="pink" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center justify-between border-b border-rose-500/20 pb-2.5 mb-3">
                <div class="flex items-center gap-2 text-rose-400 font-bold text-sm">
                  <span class="i-carbon:close-filled text-base"></span>
                  <span>부정적 · 위협적 어조</span>
                </div>
                <div class="flex items-baseline gap-1 font-mono text-rose-300 font-black">
                  <span class="text-xs text-rose-400/70 font-normal">정답률</span>
                  <NumberIncreaser :value="56.6" :from="0" :duration="800" class-name="text-2xl font-black text-rose-400" />
                  <span class="text-xs">%</span>
                </div>
              </div>

              <div class="p-3 rounded-xl bg-black/40 border border-rose-500/20 font-mono text-xs text-rose-200/90 leading-relaxed mb-3">
                "틀리면 해고야", "제대로 안 하면 불이익을 준다"<br/>
                <span class="text-[11px] text-white/50">➔ 감정적 압박 및 위협 프롬프트</span>
              </div>

              <p class="text-xs text-white/70 m-0 leading-relaxed">
                AI에게 과도한 감정적 압박을 가할 때 불필요한 방어적 토큰이 생성되며 정답률이 <strong>15% 이상 급락</strong>했습니다.
              </p>
            </div>

            <div class="pt-2 border-t border-rose-500/15 text-[11px] font-mono text-rose-300/60 flex items-center justify-between">
              <span>작동 기제: 노이즈 가중치 증가</span>
              <span class="font-bold text-rose-400">성능 저하</span>
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: Positive / Role-based Tone -->
      <div
        class="col-span-6 transition-all duration-500 transform"
        :class="[showPositive ? 'opacity-100 translate-y-0' : 'opacity-25 translate-y-2']"
      >
        <LiquidGlass glow="emerald" :radius="16" class="h-full">
          <div class="p-5 flex flex-col justify-between h-72">
            <div>
              <div class="flex items-center justify-between border-b border-emerald-500/20 pb-2.5 mb-3">
                <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm">
                  <span class="i-carbon:checkmark-filled text-base"></span>
                  <span>긍정적 · 보상적 어조</span>
                </div>
                <div class="flex items-baseline gap-1 font-mono text-emerald-300 font-black">
                  <span class="text-xs text-emerald-400/70 font-normal">정답률</span>
                  <NumberIncreaser :value="71.9" :from="0" :duration="800" class-name="text-2xl font-black text-emerald-400" />
                  <span class="text-xs">%</span>
                </div>
              </div>

              <div class="p-3 rounded-xl bg-black/40 border border-emerald-500/20 font-mono text-xs text-emerald-200/90 leading-relaxed mb-3">
                "정확하게 답변하면 보너스를 주겠다", "최고의 전문가처럼 답변하라"<br/>
                <span class="text-[11px] text-white/50">➔ 명확한 역할 부여 및 긍정 인센티브</span>
              </div>

              <p class="text-xs text-white/80 m-0 leading-relaxed">
                명확한 역할(Role)과 맥락(Context)을 부여할 때 관련 전문 지식 도메인의 가중치가 활성화되며 <strong>최상의 정답률</strong>을 기록했습니다.
              </p>
            </div>

            <div class="pt-2 border-t border-emerald-500/15 text-[11px] font-mono text-emerald-300/60 flex items-center justify-between">
              <span>작동 기제: 관련 지식 가중치 활성화</span>
              <span class="font-bold text-emerald-400">최적 성능 도출</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom Takeaway -->
    <div
      class="mt-4 transition-all duration-500"
      :class="[showPositive ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <LiquidGlass glow="cyan" :radius="12">
        <div class="p-3 px-4 flex items-center justify-between text-xs text-white/90">
          <div class="flex items-center gap-2.5">
            <span class="i-carbon:information-filled text-base text-cyan-400"></span>
            <span><strong>핵심 결론:</strong> AI는 감정적 압박이 아닌 <strong>명확한 역할 부여(Role)와 구체적 지시 체계(Context)</strong>에 반응합니다.</span>
          </div>
          <span class="text-[11px] font-mono text-cyan-300 font-bold">+15.3%p 성능 격차</span>
        </div>
      </LiquidGlass>
    </div>
  </div>
</template>
