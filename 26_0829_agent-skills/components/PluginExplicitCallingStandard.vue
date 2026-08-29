<script setup lang="ts">
import {
  computed } from 'vue'
import {
  XCircle,
  CheckCircle2,
  AlertTriangle,
  Target,
  Pin
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
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-100 text-left h-[325px] my-auto">
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
          <div class="rounded-2xl border border-rose-500/30 bg-white/5 p-5 flex flex-col justify-between shadow-xl">
            <!-- Header -->
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-xl bg-rose-950/80 text-rose-400 border border-rose-500/40 flex items-center justify-center shrink-0">
                <XCircle :size="18" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-rose-400 uppercase tracking-wider block leading-tight">
                  자연어 지시 방식
                </span>
                <h3 class="text-sm md:text-base font-bold font-serif text-white leading-tight">
                  모호한 자연어 지시
                </h3>
              </div>
            </div>

            <!-- Input Prompt Box -->
            <div class="bg-black/60 rounded-xl p-3 border border-white/10 shadow-inner">
              <span class="text-[10px] font-mono font-bold text-slate-400 block mb-1">입력 프롬프트</span>
              <p class="text-xs md:text-[12.5px] font-mono text-slate-100 leading-relaxed font-medium">
                "이번 지침서 분석해서 기획서 좀 깔끔하게 정리해줘"
              </p>
            </div>

            <!-- AI Result Box -->
            <div class="bg-rose-950/50 rounded-xl p-3 border border-rose-500/40 text-xs text-rose-200 leading-relaxed">
              <span class="text-[10px] font-mono font-bold text-rose-400 block mb-0.5">실제 AI 동작 결과</span>
              <AlertTriangle :size="13" class="inline text-rose-400 mr-1" /><strong>AI의 오판:</strong> 문서 파일(DOCX)을 생성하지 않고, 채팅창에 짧은 텍스트 요약만 남기고 종료됨.
            </div>
          </div>

          <!-- ✅ Right: @도구이름 명시적 호출 -->
          <div class="rounded-2xl border border-emerald-500/30 bg-white/5 p-5 flex flex-col justify-between shadow-xl">
            <!-- Header -->
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-xl bg-emerald-950/80 text-emerald-400 border border-emerald-500/40 flex items-center justify-center shrink-0">
                <CheckCircle2 :size="18" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-emerald-400 uppercase tracking-wider block leading-tight">
                  명시적 호출 방식
                </span>
                <h3 class="text-sm md:text-base font-bold font-serif text-white leading-tight">
                  @도구이름 명시적 호출
                </h3>
              </div>
            </div>

            <!-- Input Prompt Box -->
            <div class="bg-black/60 rounded-xl p-3 border border-white/10 shadow-inner">
              <span class="text-[10px] font-mono font-bold text-slate-400 block mb-1">입력 프롬프트</span>
              <p class="text-xs md:text-[12.5px] font-mono text-white leading-relaxed font-medium">
                "<strong class="text-sky-300 font-bold bg-sky-950/80 px-1.5 py-0.5 rounded border border-sky-400/50">@Documents</strong>, 이번 지침서를 분석해 표준 기획서(DOCX)로 작성해줘"
              </p>
            </div>

            <!-- AI Result Box -->
            <div class="bg-emerald-950/50 rounded-xl p-3 border border-emerald-500/40 text-xs text-emerald-200 leading-relaxed">
              <span class="text-[10px] font-mono font-bold text-emerald-400 block mb-0.5">실제 AI 동작 결과</span>
              <Target :size="13" class="inline text-emerald-400 mr-1" /><strong>100% 확정:</strong> AI가 문서 제작 플러그인을 즉시 가동하여 실무 검토가 가능한 완성형 파일 렌더링.
            </div>
          </div>
        </div>

        <!-- ── STAGE 1 ($clicks >= 1): 0.5초 간격으로 우아하게 순차 등장 ── -->
        <div
          v-else
          key="stage-benefits"
          class="grid grid-cols-3 gap-5 h-full items-stretch"
        >
          <!-- Benefit 1 -->
          <div class="cascade-card-1 rounded-2xl border border-white/12 bg-white/5 p-4.5 flex flex-col justify-between shadow-xl">
            <div>
              <div class="w-8 h-8 rounded-xl bg-blue-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-md mb-2.5">
                01
              </div>
              <h4 class="text-sm font-bold font-serif text-white leading-snug mb-1.5">
                단순 텍스트 응답 방지<br>
                <span class="text-sky-400 text-xs font-sans font-semibold">(의도 100% 고정)</span>
              </h4>
              <p class="text-[11.5px] text-slate-200 leading-relaxed break-keep">
                자연어가 모호해도 <code class="text-sky-300 bg-sky-950/60 px-1 rounded">@Documents</code>를 명시하면 <strong class="text-white">"채팅 대신 파일로 제작하라"</strong>는 의도가 확실하게 고정됩니다.
              </p>
            </div>
            <div class="pt-2 border-t border-white/10 text-[10.5px] font-mono font-bold text-sky-300">
              ✓ 산출물 형태 확정
            </div>
          </div>

          <!-- Benefit 2 -->
          <div class="cascade-card-2 rounded-2xl border border-white/12 bg-white/5 p-4.5 flex flex-col justify-between shadow-xl">
            <div>
              <div class="w-8 h-8 rounded-xl bg-purple-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-md mb-2.5">
                02
              </div>
              <h4 class="text-sm font-bold font-serif text-white leading-snug mb-1.5">
                다중 데이터 소스 간<br>
                <span class="text-purple-400 text-xs font-sans font-semibold">혼선 원천 차단</span>
              </h4>
              <p class="text-[11.5px] text-slate-200 leading-relaxed break-keep">
                구글 드라이브, 슬랙이 동시 연결되어 있어도 <code class="text-purple-300 bg-purple-950/60 px-1 rounded">@Google Drive</code>로 <strong class="text-white">지정 사내 문서만 정확히 탐색</strong>합니다.
              </p>
            </div>
            <div class="pt-2 border-t border-white/10 text-[10.5px] font-mono font-bold text-purple-300">
              ✓ 데이터 경계선 고정
            </div>
          </div>

          <!-- Benefit 3 -->
          <div class="cascade-card-3 rounded-2xl border border-white/12 bg-white/5 p-4.5 flex flex-col justify-between shadow-xl">
            <div>
              <div class="w-8 h-8 rounded-xl bg-emerald-600 text-white font-mono font-bold text-xs flex items-center justify-center shadow-md mb-2.5">
                03
              </div>
              <h4 class="text-sm font-bold font-serif text-white leading-snug mb-1.5">
                실행 속도 및<br>
                <span class="text-emerald-400 text-xs font-sans font-semibold">작업 성공률 극대화</span>
              </h4>
              <p class="text-[11.5px] text-slate-200 leading-relaxed break-keep">
                AI의 도구 선택 탐색 단계를 생략하고 <strong class="text-white">지정된 전용 플러그인을 즉시 가동</strong>하여 지연 시간을 줄입니다.
              </p>
            </div>
            <div class="pt-2 border-t border-white/10 text-[10.5px] font-mono font-bold text-emerald-300">
              ✓ 실행 파이프라인 직결
            </div>
          </div>
        </div>
      </Transition>
    </div>

    <!-- ── Bottom Single Takeaway Bar ── -->
    <div class="p-2 px-3.5 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 flex items-center gap-2 shadow-xs">
      <span class="text-amber-400 font-bold flex items-center gap-1"><Pin :size="12" class="text-amber-400" /><span>실무 표준 원칙:</span></span>
      <span>
        "자연어로도 알아듣지만, 의도 왜곡과 오차를 없애려면
        <strong class="text-sky-300">@도구이름</strong>을 통한 명시적 호출이 가장 확실한 실무 표준입니다."
      </span>
    </div>
  </div>
</template>

<style scoped>
.cascade-card-1 {
  animation: cascadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both;
}
.cascade-card-2 {
  animation: cascadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.6s both;
}
.cascade-card-3 {
  animation: cascadeIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 1.1s both;
}

@keyframes cascadeIn {
  0% {
    opacity: 0;
    transform: translateY(12px) scale(0.97);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
</style>
