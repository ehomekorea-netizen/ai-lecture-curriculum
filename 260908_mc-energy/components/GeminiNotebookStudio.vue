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
          <div class="p-3.5 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center justify-between border-b border-cyan-500/20 pb-1.5 mb-2">
                <div class="flex items-center gap-1.5 text-xs font-bold text-cyan-300">
                  <span class="i-carbon:folder-shared"></span>
                  <span>① 좌측: 소스 패널</span>
                </div>
                <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-200">다중 파일 주입</span>
              </div>
              <div class="space-y-1.5 text-[11px] text-white/80">
                <div class="p-1.5 rounded bg-black/40 border border-white/5 flex items-center justify-between">
                  <span>📄 사내 규정집.pdf</span>
                  <span class="text-[10px] text-cyan-400 font-mono">선택됨 ✓</span>
                </div>
                <div class="p-1.5 rounded bg-black/40 border border-white/5 flex items-center justify-between">
                  <span>📊 2026 전력동향.xlsx</span>
                  <span class="text-[10px] text-cyan-400 font-mono">선택됨 ✓</span>
                </div>
              </div>
              <p class="text-[10px] text-white/60 m-0 mt-1.5 leading-tight">
                체크박스로 필요한 문서만 선택하여 질문 범위 지정
              </p>
            </div>
            <div class="text-[10px] font-mono text-cyan-300/70 pt-1 border-t border-white/10">
              최대 수십 개 문서 통합 RAG
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
          <div class="p-3.5 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center justify-between border-b border-blue-500/20 pb-1.5 mb-2">
                <div class="flex items-center gap-1.5 text-xs font-bold text-blue-300">
                  <span class="i-carbon:chat"></span>
                  <span>② 중앙: 근거 채팅</span>
                </div>
                <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-200">인라인 각주</span>
              </div>
              <div class="p-2 rounded bg-black/40 border border-blue-500/20 font-mono text-[10px] text-blue-100 leading-relaxed mb-1.5">
                "취업규칙 제15조<span class="text-cyan-400 font-bold bg-cyan-950/60 px-1 rounded">[1]</span>에 따라 3년 근속 시 16일의 연차가 발생합니다."
              </div>
              <p class="text-[10px] text-white/60 m-0 leading-tight">
                답변 내 번호 클릭 시 원본 문서의 정확한 문맥 하이라이트 대조
              </p>
            </div>
            <div class="text-[10px] font-mono text-blue-300/70 pt-1 border-t border-white/10">
              오픈북 팩트체크 보장
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Pane 3: Right - Studio 9 Outputs -->
      <div
        class="col-span-4 transition-all duration-500 transform"
        :class="[currentStage >= 2 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="emerald" :radius="14" class="h-full">
          <div class="p-3.5 flex flex-col justify-between h-54">
            <div>
              <div class="flex items-center justify-between border-b border-emerald-500/20 pb-1.5 mb-2">
                <div class="flex items-center gap-1.5 text-xs font-bold text-emerald-300">
                  <span class="i-carbon:template"></span>
                  <span>③ 우측: Studio 산출물</span>
                </div>
                <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-200">9대 맞춤 변환</span>
              </div>
              <div class="grid grid-cols-2 gap-1 text-[10px] text-white/80">
                <div class="p-1 rounded bg-black/30 border border-white/5">🎙️ 오디오(팟캐스트)</div>
                <div class="p-1 rounded bg-black/30 border border-white/5">📋 브리핑 문서</div>
                <div class="p-1 rounded bg-black/30 border border-white/5">❓ FAQ 가이드</div>
                <div class="p-1 rounded bg-black/30 border border-white/5">⏳ 타임라인 표</div>
              </div>
            </div>
            <div class="text-[10px] font-mono text-emerald-300/70 pt-1 border-t border-white/10">
              원클릭 1차 초안 생성
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom: 3 Golden Rules -->
    <div
      class="grid grid-cols-3 gap-3 transition-all duration-500"
      :class="[currentStage >= 3 ? 'opacity-100 translate-y-0' : 'opacity-40 translate-y-1']"
    >
      <div class="p-2.5 rounded-xl bg-black/40 border border-white/10 text-xs">
        <strong class="text-cyan-300">원칙 ① 소스가 80%:</strong>
        <p class="text-[10px] text-white/60 m-0 mt-0.5">정제된 고품질 PDF/데이터를 업로드할수록 결과물의 정확도 상승</p>
      </div>
      <div class="p-2.5 rounded-xl bg-black/40 border border-white/10 text-xs">
        <strong class="text-blue-300">원칙 ② 출처를 물어라:</strong>
        <p class="text-[10px] text-white/60 m-0 mt-0.5">답변 각주 번호를 직접 클릭하여 원본 문서의 조항을 직접 대조 검증</p>
      </div>
      <div class="p-2.5 rounded-xl bg-black/40 border border-white/10 text-xs">
        <strong class="text-emerald-300">원칙 ③ 초안으로 활용:</strong>
        <p class="text-[10px] text-white/60 m-0 mt-0.5">Studio 결과물은 최종본이 아닌 실무 검토용 고품질 베이스캠프로 활용</p>
      </div>
    </div>
  </div>
</template>
