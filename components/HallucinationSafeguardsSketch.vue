<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import rough from 'roughjs'

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

  // Helper for drawing hand-drawn curved arrow with rough.js
  const drawCurvedArrow = (
    x1: number, y1: number,
    cx: number, cy: number,
    x2: number, y2: number,
    color: string
  ) => {
    const pathData = `M ${x1.toFixed(1)} ${y1.toFixed(1)} Q ${cx.toFixed(1)} ${cy.toFixed(1)}, ${x2.toFixed(1)} ${y2.toFixed(1)}`
    svg.appendChild(
      rc.path(pathData, {
        roughness: 1.3,
        bowing: 1.2,
        strokeWidth: 3.5,
        stroke: color,
      })
    )

    // Arrowhead
    const L = 12
    const angle = Math.atan2(y2 - cy, x2 - cx)
    svg.appendChild(
      rc.line(
        x2, y2,
        x2 - L * Math.cos(angle - 0.45),
        y2 - L * Math.sin(angle - 0.45),
        { roughness: 1.0, strokeWidth: 3.5, stroke: color }
      )
    )
    svg.appendChild(
      rc.line(
        x2, y2,
        x2 - L * Math.cos(angle + 0.45),
        y2 - L * Math.sin(angle + 0.45),
        { roughness: 1.0, strokeWidth: 3.5, stroke: color }
      )
    )
  }

  // Arrow 1 -> 2 (Top Left to Top Right): visible from stage >= 2
  if (props.stage >= 2) {
    const x1 = W * 0.46
    const y1 = H * 0.22
    const x2 = W * 0.54
    const y2 = H * 0.22
    const cx = (x1 + x2) / 2
    const cy = y1 - 18
    drawCurvedArrow(x1, y1, cx, cy, x2, y2, '#3B82F6')
  }

  // Arrow 2 -> 3 (Top Right to Bottom Right): visible from stage >= 3
  if (props.stage >= 3) {
    const x1 = W * 0.78
    const y1 = H * 0.45
    const x2 = W * 0.78
    const y2 = H * 0.55
    const cx = x1 + 22
    const cy = (y1 + y2) / 2
    drawCurvedArrow(x1, y1, cx, cy, x2, y2, '#10B981')
  }

  // Arrow 3 -> 4 (Bottom Right to Bottom Left): visible from stage >= 4
  if (props.stage >= 4) {
    const x1 = W * 0.54
    const y1 = H * 0.78
    const x2 = W * 0.46
    const y2 = H * 0.78
    const cx = (x1 + x2) / 2
    const cy = y1 + 18
    drawCurvedArrow(x1, y1, cx, cy, x2, y2, '#A855F7')
  }

  // Loop return arrow 4 -> 1 (Bottom Left to Top Left): visible when stage >= 4
  if (props.stage >= 4) {
    const x1 = W * 0.22
    const y1 = H * 0.55
    const x2 = W * 0.22
    const y2 = H * 0.45
    const cx = x1 - 22
    const cy = (y1 + y2) / 2
    drawCurvedArrow(x1, y1, cx, cy, x2, y2, '#F59E0B')
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
  <div class="w-full flex flex-col items-center select-none my-auto">
    <!-- Clockwise 2x2 Quadrant Framework Container with Rough SVG Overlay -->
    <div ref="wrap" class="relative w-full grid grid-cols-2 gap-x-12 gap-y-4 px-2 py-1">
      <!-- SVG Overlay for Hand-drawn Curved Arrows -->
      <svg ref="overlay" class="absolute inset-0 w-full h-full pointer-events-none z-20" />

      <!-- 1. Top Left: 검색 연동 (Web Search) — Appears on Click 1 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative overflow-hidden bg-white/6 flex items-start gap-3.5 h-[116px] shadow-xs"
        :class="stage >= 1
          ? 'opacity-100 scale-100 translate-y-0 border-blue-500 ring-4 ring-blue-500/15 shadow-md bg-linear-to-br from-white/10 to-blue-50/40'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <!-- Pure Handwritten Number Badge (No 'STEP', No Emojis) -->
        <div class="shrink-0 flex items-center justify-center">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm text-white shadow-xs bg-blue-600"
            style="font-family: 'Kalam', cursive;"
          >
            01
          </div>
        </div>

        <div class="flex-1 min-w-0">
          <div class="flex items-center justify-between mb-1">
            <h4 class="font-bold text-[14px] text-blue-300 leading-tight">
              1. 실시간 검색 연동
            </h4>
            <span class="text-[9.5px] font-mono font-bold px-1.5 py-0.5 rounded bg-blue-100 text-blue-400">
              SEARCH
            </span>
          </div>
          <p class="text-[11.5px] text-slate-400 leading-snug">
            웹 검색을 활성화하여 <strong>최신 사실 데이터·통계·법령</strong>을 AI에 직접 주입합니다.
          </p>
        </div>
      </div>

      <!-- 2. Top Right: RAG 문서 첨부 (Document Retrieval) — Appears on Click 2 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative overflow-hidden bg-white/6 flex items-start gap-3.5 h-[116px] shadow-xs"
        :class="stage >= 2
          ? 'opacity-100 scale-100 translate-y-0 border-emerald-500 ring-4 ring-emerald-500/15 shadow-md bg-linear-to-br from-white/10 to-emerald-50/40'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <!-- Pure Handwritten Number Badge -->
        <div class="shrink-0 flex items-center justify-center">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm text-white shadow-xs bg-emerald-600"
            style="font-family: 'Kalam', cursive;"
          >
            02
          </div>
        </div>

        <div class="flex-1 min-w-0">
          <div class="flex items-center justify-between mb-1">
            <h4 class="font-bold text-[14px] text-emerald-300 leading-tight">
              2. RAG (문서 직접 첨부)
            </h4>
            <span class="text-[9.5px] font-mono font-bold px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-400">
              RAG
            </span>
          </div>
          <p class="text-[11.5px] text-slate-400 leading-snug">
            관련 <strong>규정/지침 PDF 파일</strong>을 업로드하여 답변의 확실한 팩트 근거를 확보합니다.
          </p>
        </div>
      </div>

      <!-- 4. Bottom Left: 인간의 최종 검증 (Human Verification) — Appears on Click 4 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative overflow-hidden bg-white/6 flex items-start gap-3.5 h-[116px] shadow-xs"
        :class="stage >= 4
          ? 'opacity-100 scale-100 translate-y-0 border-amber-500 ring-4 ring-amber-500/15 shadow-md bg-linear-to-br from-white/10 to-amber-50/40'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <!-- Pure Handwritten Number Badge -->
        <div class="shrink-0 flex items-center justify-center">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm text-white shadow-xs bg-amber-600"
            style="font-family: 'Kalam', cursive;"
          >
            04
          </div>
        </div>

        <div class="flex-1 min-w-0">
          <div class="flex items-center justify-between mb-1">
            <h4 class="font-bold text-[14px] text-amber-950 leading-tight">
              4. 인간의 최종 검증
            </h4>
            <span class="text-[9.5px] font-mono font-bold px-1.5 py-0.5 rounded bg-amber-100 text-amber-800">
              VERIFY
            </span>
          </div>
          <p class="text-[11.5px] text-slate-400 leading-snug">
            예산 산출식, 법령 번호, 고유명사는 <strong>실무자(인간)가 최종 크로스체크</strong>합니다.
          </p>
        </div>
      </div>

      <!-- 3. Bottom Right: 프롬프트 제약 (Constraint) — Appears on Click 3 -->
      <div
        class="rounded-2xl border-2 p-3.5 transition-all duration-500 relative overflow-hidden bg-white/6 flex items-start gap-3.5 h-[116px] shadow-xs"
        :class="stage >= 3
          ? 'opacity-100 scale-100 translate-y-0 border-purple-500 ring-4 ring-purple-500/15 shadow-md bg-linear-to-br from-white/10 to-purple-50/40'
          : 'opacity-0 scale-95 translate-y-2 pointer-events-none border-transparent'"
      >
        <!-- Pure Handwritten Number Badge -->
        <div class="shrink-0 flex items-center justify-center">
          <div
            class="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm text-white shadow-xs bg-purple-600"
            style="font-family: 'Kalam', cursive;"
          >
            03
          </div>
        </div>

        <div class="flex-1 min-w-0">
          <div class="flex items-center justify-between mb-1">
            <h4 class="font-bold text-[14px] text-purple-950 leading-tight">
              3. 프롬프트 규칙 제약
            </h4>
            <span class="text-[9.5px] font-mono font-bold px-1.5 py-0.5 rounded bg-purple-100 text-purple-700">
              LOCK
            </span>
          </div>
          <p class="text-[11.5px] text-slate-400 leading-snug">
            <strong>"첨부 문서에 없는 내용은 지어내지 말 것"</strong>이라는 탈출 방지 조건을 명시합니다.
          </p>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Formula: Large Pure Typography (Triggered on Click 5, Zero Jump) -->
    <div
      class="w-full mt-3.5 text-center transition-all duration-500 min-h-[42px] px-2"
      :class="stage >= 5 ? 'opacity-100 translate-y-0' : 'opacity-0 pointer-events-none translate-y-1'"
    >
      <div class="text-[16px] md:text-[17.5px] font-serif font-extrabold text-slate-100 tracking-tight flex items-center justify-center gap-2 flex-wrap">
        <span>생성 AI 실무 역량 = </span>
        <span class="text-blue-600 font-black">생성(Generation)</span>
        <span class="text-slate-400 font-normal">+</span>
        <span class="text-emerald-600 font-black">근거(Grounding)</span>
        <span class="text-slate-400 font-normal">+</span>
        <span class="text-amber-600 font-black">검증(Verification)</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
