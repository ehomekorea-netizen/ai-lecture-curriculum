<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import rough from 'roughjs'
import { Search, Bot, Sparkles } from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const wrap = ref<HTMLElement | null>(null)
const overlay = ref<SVGSVGElement | null>(null)

function draw() {
  const svg = overlay.value, cont = wrap.value
  if (!svg || !cont) return
  const W = cont.clientWidth, H = cont.clientHeight
  if (!W || !H) return

  svg.setAttribute('viewBox', `0 0 ${W} ${H}`)
  while (svg.firstChild) svg.removeChild(svg.firstChild)
  const rc = rough.svg(svg)

  // Stage 2 (우측 슬라이드 넘김 2회차): 검색 카드에 큰 빨간 X 및 우측 팝업 LLM으로 이어지는 커브 화살표
  if (props.stage >= 2) {
    // 1. Search Box boundary dimensions (Left 46% of width)
    const leftW = W * 0.46
    const padX = W * 0.04
    const padY = H * 0.15

    const x1 = padX
    const y1 = padY
    const x2 = leftW - padX
    const y2 = H - padY

    // Draw Big Red X with rough.js
    svg.appendChild(
      rc.line(x1, y1, x2, y2, {
        roughness: 1.8,
        bowing: 1.3,
        strokeWidth: 4.5,
        stroke: '#EF4444',
      })
    )
    svg.appendChild(
      rc.line(x2, y1, x1, y2, {
        roughness: 1.8,
        bowing: 1.3,
        strokeWidth: 4.5,
        stroke: '#EF4444',
      })
    )

    // 2. Curved Bold Rough Arrow from Search card to LLM card
    const startX = leftW + W * 0.015
    const startY = H * 0.48
    const endX = W * 0.54 - W * 0.01
    const endY = H * 0.48

    // Center bridge curved arrow
    const midX = (startX + endX) / 2
    const pathData = `M ${startX.toFixed(1)} ${startY.toFixed(1)} Q ${midX.toFixed(1)} ${(startY - 18).toFixed(1)}, ${endX.toFixed(1)} ${endY.toFixed(1)}`
    
    svg.appendChild(
      rc.path(pathData, {
        roughness: 1.3,
        bowing: 1.2,
        strokeWidth: 3.5,
        stroke: '#476BFF',
      })
    )

    // Arrowhead pointing right towards the newly popped-up LLM card
    const L = 12
    const angle = Math.atan2(endY - (startY - 18), endX - midX)
    svg.appendChild(
      rc.line(
        endX, endY,
        endX - L * Math.cos(angle - 0.42),
        endY - L * Math.sin(angle - 0.42),
        { roughness: 1.0, strokeWidth: 3.5, stroke: '#476BFF' }
      )
    )
    svg.appendChild(
      rc.line(
        endX, endY,
        endX - L * Math.cos(angle + 0.42),
        endY - L * Math.sin(angle + 0.42),
        { roughness: 1.0, strokeWidth: 3.5, stroke: '#476BFF' }
      )
    )
  }
}

let ro: ResizeObserver
onMounted(() => {
  draw()
  ro = new ResizeObserver(() => draw())
  if (wrap.value) ro.observe(wrap.value)
})
onUnmounted(() => ro?.disconnect())
watch(() => props.stage, () => nextTick(draw))
</script>

<template>
  <div class="w-full flex flex-col items-center select-none">
    <!-- Top Claim Statement with Stage-based Red Strikethrough (Stage 0 -> 1) -->
    <div class="w-full mb-2 flex items-center justify-start gap-3 flex-wrap min-h-[30px] px-1">
      <div class="relative inline-block">
        <span
          class="text-base font-bold transition-all duration-300"
          :class="stage >= 1 ? 'text-slate-400 line-through decoration-rose-500 decoration-3' : 'text-slate-800'"
          style="font-family: 'Kalam', 'Source Serif 4', cursive;"
        >
          GPT = 똑똑한 네이버 / 구글 검색창
        </span>
      </div>

      <span
        v-if="stage >= 1"
        class="text-xs text-slate-400 italic font-mono transition-all duration-300"
      >
        is really
      </span>

      <span
        v-if="stage >= 1"
        class="text-base font-extrabold text-blue-600 transition-all duration-500"
        style="font-family: 'Kalam', cursive;"
      >
        문맥에서 다음 토큰(단어)을 확률적으로 예측하는 생성기
      </span>
    </div>

    <!-- Comparison Cards Container with Rough SVG Overlay -->
    <div ref="wrap" class="relative w-full grid grid-cols-2 gap-7 mt-1">
      <!-- SVG Overlay for Big Red X and Arrow -->
      <svg ref="overlay" class="absolute inset-0 w-full h-full pointer-events-none z-20" />

      <!-- Left Card: 검색 시스템 (Search Engine) — Shown initially -->
      <div
        class="rounded-2xl border p-4.5 transition-all duration-500 relative overflow-hidden bg-white shadow-xs flex flex-col justify-between h-[210px]"
        :class="stage >= 2 ? 'opacity-40 grayscale-40 border-slate-300 bg-slate-50/70' : 'border-slate-300'"
      >
        <div>
          <!-- Tag Header -->
          <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-2.5">
            <div class="flex items-center gap-1.5 font-bold text-slate-700 text-xs font-serif">
              <Search :size="15" class="text-slate-500" />
              <span>검색 시스템 (Search Engine)</span>
            </div>
            <span class="text-[10px] font-mono text-slate-400 px-2 py-0.5 rounded-full bg-slate-100">
              EXISTING DB
            </span>
          </div>

          <!-- Feature List -->
          <div class="space-y-2 text-xs text-slate-700 leading-relaxed">
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-slate-900 shrink-0">• 동작:</span>
              <span>웹이나 DB의 문서를 <strong>찾아서 링크/원본을 제공</strong></span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-slate-900 shrink-0">• 출처:</span>
              <span>가져온 웹페이지의 <strong>원문 URL 출처가 명확함</strong></span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-slate-900 shrink-0">• 특징:</span>
              <span>실시간 최신 사실, 통계, 지자체 조례 번호 확인에 강함</span>
            </div>
          </div>
        </div>

        <div class="text-[10.5px] font-bold text-slate-400 font-mono pt-1.5 border-t border-slate-100">
          🔍 "존재하는 것을 찾아주는 검색기"
        </div>
      </div>

      <!-- Right Card: 언어 모델 (LLM) — Pops Up ONLY at Stage 2 with zero layout jump -->
      <div
        class="rounded-2xl border-2 p-4.5 transition-all duration-600 relative overflow-hidden bg-white flex flex-col justify-between h-[210px]"
        :class="stage >= 2
          ? 'opacity-100 scale-100 translate-x-0 border-blue-600 ring-4 ring-blue-500/20 shadow-xl bg-linear-to-b from-white to-blue-50/40'
          : 'opacity-0 scale-95 translate-x-3 pointer-events-none border-blue-200'"
      >
        <div>
          <!-- Tag Header -->
          <div class="flex items-center justify-between pb-2 border-b border-blue-100 mb-2.5">
            <div class="flex items-center gap-1.5 font-bold text-blue-700 text-xs font-serif">
              <Bot :size="16" class="text-blue-600" />
              <span>언어 모델 (LLM / Generative AI)</span>
            </div>
            <span
              class="text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-blue-600 text-white shadow-xs animate-pulse"
            >
              PROBABILISTIC AI
            </span>
          </div>

          <!-- Feature List -->
          <div class="space-y-2 text-xs text-slate-800 leading-relaxed">
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-blue-900 shrink-0">• 동작:</span>
              <span>입력된 질문의 맥락을 보고 <strong>다음 말을 확률적으로 조립</strong></span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-blue-900 shrink-0">• 출처:</span>
              <span>기억(패턴)에 기반하므로 원문 출처 자동 보장 불가</span>
            </div>
            <div class="flex items-start gap-1.5">
              <span class="font-bold text-blue-900 shrink-0">• 특징:</span>
              <span><strong>요약, 서식 변환, 초안 작성, 번역</strong>에 압도적 강점</span>
            </div>
          </div>
        </div>

        <div class="text-[11px] font-bold text-blue-700 font-serif pt-1.5 border-t border-blue-100 flex items-center justify-between">
          <span>✨ "맥락에 맞춰 새로 써주는 작가"</span>
          <span class="text-[10px] font-mono text-blue-600 font-bold">★ FOCUS</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
