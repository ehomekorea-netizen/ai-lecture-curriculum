<script setup lang="ts">
import { computed } from 'vue'
import {
  XCircle,
  CheckCircle2
} from 'lucide-vue-next'

const props = withDefaults(
  defineProps<{
    stage?: number
  }>(),
  {
    stage: 0
  }
)

const currentStage = computed(() => Number(props.stage ?? 0))
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[325px] my-auto">
    <!-- ── Main Stage Area (h-[255px], Zero Clipping) ── -->
    <div class="relative w-full h-[255px]">
      <!-- ── STAGE 0 ($clicks === 0): 프롬프트 방식 차이 (1:1 대칭 카드) ── -->
      <Transition name="keynote-fade" mode="out-in">
        <div
          v-if="currentStage === 0"
          key="stage-0"
          class="grid grid-cols-2 gap-5 h-full items-stretch"
        >
          <!-- ❌ Left: 모호한 자연어 지시 -->
          <div class="rounded-3xl border border-rose-200/80 bg-gradient-to-b from-rose-50/40 via-white to-rose-50/10 p-5 flex flex-col justify-between shadow-2xs">
            <!-- Header -->
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center shrink-0">
                <XCircle :size="18" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-rose-500 uppercase tracking-wider block leading-tight">
                  자연어 지시 방식
                </span>
                <h3 class="text-sm md:text-base font-bold font-serif text-slate-900 leading-tight">
                  모호한 자연어 지시
                </h3>
              </div>
            </div>

            <!-- Input Prompt Box -->
            <div class="bg-white rounded-2xl p-3.5 border border-rose-200/70 shadow-2xs">
              <span class="text-[10px] font-mono font-bold text-slate-400 block mb-1">입력 프롬프트</span>
              <p class="text-xs md:text-[12.5px] font-mono text-slate-800 leading-relaxed font-medium">
                "이번 지침서 분석해서 기획서 좀 깔끔하게 정리해줘"
              </p>
            </div>

            <!-- AI Result Box -->
            <div class="bg-rose-50/80 rounded-2xl p-3 border border-rose-200/60 text-xs text-rose-900 leading-relaxed">
              <span class="text-[10px] font-mono font-bold text-rose-600 block mb-0.5">실제 AI 동작 결과</span>
              <strong>⚠️ AI의 오판:</strong> 문서 파일(DOCX)을 생성하지 않고, 채팅창에 짧은 텍스트 요약만 남기고 종료됨.
            </div>
          </div>

          <!-- ✅ Right: @도구이름 명시적 호출 -->
          <div class="rounded-3xl border border-emerald-200/80 bg-gradient-to-b from-emerald-50/40 via-white to-emerald-50/10 p-5 flex flex-col justify-between shadow-2xs">
            <!-- Header -->
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                <CheckCircle2 :size="18" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-emerald-600 uppercase tracking-wider block leading-tight">
                  명시적 호출 방식
                </span>
                <h3 class="text-sm md:text-base font-bold font-serif text-slate-900 leading-tight">
                  @도구이름 명시적 호출
                </h3>
              </div>
            </div>

            <!-- Input Prompt Box -->
            <div class="bg-white rounded-2xl p-3.5 border border-emerald-200/70 shadow-2xs">
              <span class="text-[10px] font-mono font-bold text-slate-400 block mb-1">입력 프롬프트</span>
              <p class="text-xs md:text-[12.5px] font-mono text-slate-900 leading-relaxed font-medium">
                "<strong class="text-blue-600 font-bold bg-blue-50 px-1.5 py-0.5 rounded border border-blue-200">@Documents</strong>, 이번 지침서를 분석해 표준 기획서(DOCX)로 작성해줘"
              </p>
            </div>

            <!-- AI Result Box -->
            <div class="bg-emerald-50/80 rounded-2xl p-3 border border-emerald-200/60 text-xs text-emerald-900 leading-relaxed">
              <span class="text-[10px] font-mono font-bold text-emerald-700 block mb-0.5">실제 AI 동작 결과</span>
              <strong>🎯 100% 확정:</strong> AI가 문서 제작 플러그인을 즉시 가동하여 실무 검토가 가능한 완성형 파일 렌더링.
            </div>
          </div>
        </div>

        <!-- ── STAGE 1 ($clicks >= 1): 0.5초 간격으로 우아하게 순차 등장 (Cascade) ── -->
        <div
          v-else
          key="stage-benefits"
          class="grid grid-cols-3 gap-5 h-full items-stretch"
        >
          <!-- Benefit 1 (0.1s Delay) -->
          <div class="cascade-card-1 rounded-3xl border border-blue-200/80 bg-gradient-to-b from-blue-50/50 via-white to-blue-50/20 p-4.5 flex flex-col justify-between shadow-2xs">
            <div>
              <div class="w-8 h-8 rounded-xl bg-blue-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-2xs mb-2.5">
                01
              </div>
              <h4 class="text-sm font-bold font-serif text-slate-900 leading-snug mb-1.5">
                단순 텍스트 응답 방지<br>
                <span class="text-blue-600 text-xs font-sans font-semibold">(의도 100% 고정)</span>
              </h4>
              <p class="text-[11.5px] text-slate-600 leading-relaxed break-keep">
                자연어가 모호해도 <code>@Documents</code>를 명시하면 <strong>"채팅 대신 파일로 제작하라"</strong>는 의도가 확실하게 고정됩니다.
              </p>
            </div>
            <div class="pt-2 border-t border-blue-100 text-[10px] font-mono font-bold text-blue-700">
              ✓ 산출물 형태 확정
            </div>
          </div>

          <!-- Benefit 2 (0.6s Delay: 0.5s 간격) -->
          <div class="cascade-card-2 rounded-3xl border border-purple-200/80 bg-gradient-to-b from-purple-50/50 via-white to-purple-50/20 p-4.5 flex flex-col justify-between shadow-2xs">
            <div>
              <div class="w-8 h-8 rounded-xl bg-purple-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-2xs mb-2.5">
                02
              </div>
              <h4 class="text-sm font-bold font-serif text-slate-900 leading-snug mb-1.5">
                다중 데이터 소스 간<br>
                <span class="text-purple-600 text-xs font-sans font-semibold">혼선 원천 차단</span>
              </h4>
              <p class="text-[11.5px] text-slate-600 leading-relaxed break-keep">
                구글 드라이브, 슬랙이 동시 연결되어 있어도 <code>@Google Drive</code>로 <strong>지정 사내 문서만 정확히 탐색</strong>합니다.
              </p>
            </div>
            <div class="pt-2 border-t border-purple-100 text-[10px] font-mono font-bold text-purple-700">
              ✓ 데이터 경계선 고정
            </div>
          </div>

          <!-- Benefit 3 (1.1s Delay: 0.5s 간격) -->
          <div class="cascade-card-3 rounded-3xl border border-emerald-200/80 bg-gradient-to-b from-emerald-50/50 via-white to-emerald-50/20 p-4.5 flex flex-col justify-between shadow-2xs">
            <div>
              <div class="w-8 h-8 rounded-xl bg-emerald-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-2xs mb-2.5">
                03
              </div>
              <h4 class="text-sm font-bold font-serif text-slate-900 leading-snug mb-1.5">
                크레딧 낭비 없는<br>
                <span class="text-emerald-700 text-xs font-sans font-semibold">원샷(One-Shot) 성공</span>
              </h4>
              <p class="text-[11.5px] text-slate-600 leading-relaxed break-keep">
                AI의 도구 추측 오판을 없애 재작업 없이 <strong>단 1번의 지시로 원하는 완성형 결과물을 도출</strong>합니다.
              </p>
            </div>
            <div class="pt-2 border-t border-emerald-100 text-[10px] font-mono font-bold text-emerald-800">
              ✓ 재작업 비용 0%
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <!-- ── Dynamic Bottom Quote Box (Stage 0: Principle / Stage 1: Formula) ── -->
    <div class="slide-footer quote-box text-xs py-1.5 px-4 font-medium truncate mt-1">
      <template v-if="currentStage === 0">
        📌 <strong>실무 표준 원칙</strong>: "자연어로도 알아듣지만, 의도 왜곡과 오차를 없애려면 <code>@도구이름</code>을 통한 명시적 호출이 가장 확실한 실무 표준입니다."
      </template>
      <template v-else>
        💡 <strong>실무 작성 공식</strong>: <code>[@도구이름]</code> + <code>[참조할 원자료 파일명]</code> + <code>[원하는 최종 산출물 서식]</code>
      </template>
    </div>
  </div>
</template>

<style scoped>
.keynote-fade-enter-active,
.keynote-fade-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.keynote-fade-enter-from {
  opacity: 0;
  transform: scale(0.98);
}

.keynote-fade-leave-to {
  opacity: 0;
  transform: scale(0.98);
}

/* ── 0.5s Interval Smooth Keynote Cascade Animations ── */
@keyframes cascade-smooth {
  0% {
    opacity: 0;
    transform: translateY(22px) scale(0.96);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.cascade-card-1 {
  animation: cascade-smooth 0.65s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both;
}

.cascade-card-2 {
  animation: cascade-smooth 0.65s cubic-bezier(0.16, 1, 0.3, 1) 0.6s both;
}

.cascade-card-3 {
  animation: cascade-smooth 0.65s cubic-bezier(0.16, 1, 0.3, 1) 1.1s both;
}
</style>
