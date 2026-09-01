<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top 3-Pane Layout Grid -->
    <div class="grid grid-cols-12 gap-4 items-stretch mb-3">
      <!-- Pane 1: Left - Sources -->
      <div
        class="col-span-4 transition-all duration-500 transform"
        :class="[currentStage >= 0 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="cyan" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center gap-2 text-sm font-bold text-cyan-300 border-b border-cyan-500/20 pb-2 mb-2.5">
                <span class="i-carbon:folder-shared text-base"></span>
                <span>소스 패널 (Source)</span>
              </div>
              <div class="space-y-1.5 text-xs text-white/80">
                <div class="p-2 rounded-lg bg-black/40 border border-white/5 flex items-center justify-between">
                  <div class="flex items-center gap-1.5">
                    <span class="i-carbon:document text-cyan-400"></span>
                    <span>사내 규정집.pdf</span>
                  </div>
                  <span class="text-[10px] text-cyan-400 font-mono">선택됨 ✓</span>
                </div>
                <div class="p-2 rounded-lg bg-black/40 border border-white/5 flex items-center justify-between">
                  <div class="flex items-center gap-1.5">
                    <span class="i-carbon:chart-line text-cyan-400"></span>
                    <span>2026 전력동향.xlsx</span>
                  </div>
                  <span class="text-[10px] text-cyan-400 font-mono">선택됨 ✓</span>
                </div>
              </div>
            </div>
            <div class="text-[11px] font-mono text-cyan-300/80 pt-1.5 border-t border-white/10">
              필요한 사내 문서만 체크하여 범위 한정
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Pane 2: Center - Chat & Citations -->
      <div
        class="col-span-4 transition-all duration-500 transform"
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="blue" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center gap-2 text-sm font-bold text-blue-300 border-b border-blue-500/20 pb-2 mb-2.5">
                <span class="i-carbon:chat text-base"></span>
                <span>근거 채팅 & 각주 (Chat)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-black/40 border border-blue-500/20 font-mono text-[11px] text-blue-100 leading-relaxed mb-2">
                "취업규칙 제15조<span class="text-cyan-400 font-bold bg-cyan-950/80 px-1 rounded ml-0.5">[1]</span>에 따라 3년 근속 시 16일의 연차가 부여됩니다."
              </div>
            </div>
            <div class="text-[11px] font-mono text-blue-300/80 pt-1.5 border-t border-white/10">
              각주 번호 클릭 시 원본 조항 즉시 대조
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Pane 3: Right - Studio Outputs -->
      <div
        class="col-span-4 transition-all duration-500 transform"
        :class="[currentStage >= 2 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="emerald" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center gap-2 text-sm font-bold text-emerald-300 border-b border-emerald-500/20 pb-2 mb-2.5">
                <span class="i-carbon:template text-base"></span>
                <span>스튜디오 변환 (Studio)</span>
              </div>
              <div class="grid grid-cols-2 gap-1.5 text-xs text-white/80">
                <div class="p-1.5 rounded-lg bg-black/30 border border-white/5 flex items-center gap-1.5">
                  <span class="i-carbon:microphone text-emerald-400"></span>
                  <span>오디오 팟캐스트</span>
                </div>
                <div class="p-1.5 rounded-lg bg-black/30 border border-white/5 flex items-center gap-1.5">
                  <span class="i-carbon:report text-emerald-400"></span>
                  <span>브리핑 문서</span>
                </div>
                <div class="p-1.5 rounded-lg bg-black/30 border border-white/5 flex items-center gap-1.5">
                  <span class="i-carbon:help text-emerald-400"></span>
                  <span>FAQ 가이드</span>
                </div>
                <div class="p-1.5 rounded-lg bg-black/30 border border-white/5 flex items-center gap-1.5">
                  <span class="i-carbon:time text-emerald-400"></span>
                  <span>타임라인 표</span>
                </div>
              </div>
            </div>
            <div class="text-[11px] font-mono text-emerald-300/80 pt-1.5 border-t border-white/10">
              업로드 문서 기반 실무 초안 원클릭 변환
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom: 3 Golden Rules -->
    <div
      class="grid grid-cols-3 gap-4 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-1']"
    >
      <div class="p-3 rounded-xl bg-white/5 border border-white/10 text-xs">
        <div class="flex items-center gap-1.5 font-bold text-cyan-300 mb-1">
          <span class="i-carbon:checkmark-filled"></span>
          <span>원칙 1: 소스 품질이 결과 품질</span>
        </div>
        <p class="text-[11px] text-white/70 m-0 leading-relaxed">정제된 사내 PDF와 데이터만 골라 업로드합니다.</p>
      </div>
      <div class="p-3 rounded-xl bg-white/5 border border-white/10 text-xs">
        <div class="flex items-center gap-1.5 font-bold text-blue-300 mb-1">
          <span class="i-carbon:checkmark-filled"></span>
          <span>원칙 2: 각주 번호 교차 대조</span>
        </div>
        <p class="text-[11px] text-white/70 m-0 leading-relaxed">답변 각주를 클릭해 원본 원문과 수치를 직접 확인합니다.</p>
      </div>
      <div class="p-3 rounded-xl bg-white/5 border border-white/10 text-xs">
        <div class="flex items-center gap-1.5 font-bold text-emerald-300 mb-1">
          <span class="i-carbon:checkmark-filled"></span>
          <span>원칙 3: 초안 베이스캠프로 활용</span>
        </div>
        <p class="text-[11px] text-white/70 m-0 leading-relaxed">스튜디오 산출물을 출발점으로 삼아 최종 검토를 진행합니다.</p>
      </div>
    </div>
  </div>
</template>
