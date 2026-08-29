<script setup lang="ts">
import { ref, onMounted, onUnmounted, markRaw, watch, nextTick } from 'vue'
import rough from 'roughjs'
import { FileText, Image, Mic, Code2, Sparkles, MessageSquare, Database } from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const base = import.meta.env.BASE_URL || '/'
const resolveAsset = (path: string) => {
  if (!path || path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

const wrap = ref<HTMLElement | null>(null)
const overlay = ref<SVGSVGElement | null>(null)

type Kind = 'input' | 'model' | 'output'
type Box = {
  id: string
  l: number
  t: number
  w: number
  h: number
  label: string
  sub?: string
  kind: Kind
  color?: string
  icon?: any
  stage: number // The stage at which this box appears
}

const boxes: Box[] = [
  // ── Central Model — Appears FIRST at stage 2 ──
  { id: 'model', l: 36, t: 18, w: 26, h: 62, label: '생성형 AI 엔진', sub: 'Generative AI Engine', kind: 'model', icon: markRaw(Sparkles), stage: 2 },

  // ── Left Inputs — Sequential stages 3, 4, 5 ──
  { id: 'in-prompt', l: 1, t: 4, w: 23, h: 25, label: '프롬프트 (지시)', sub: 'Role, Goal, Constraint', kind: 'input', icon: markRaw(MessageSquare), stage: 3 },
  { id: 'in-context', l: 1, t: 37, w: 23, h: 25, label: '업무 맥락 (Context)', sub: '규정 · 공문 · 참고 자료', kind: 'input', icon: markRaw(FileText), stage: 4 },
  { id: 'in-pattern', l: 1, t: 70, w: 23, h: 25, label: '사전학습 패턴', sub: '수억 개 언어 통계 구조', kind: 'input', icon: markRaw(Database), stage: 5 },

  // ── Right Multimodal Outputs — Sequential stages 6, 7, 8, 9 ──
  { id: 'out-txt', l: 73, t: 2, w: 26, h: 20, label: '텍스트 (Text)', sub: '보고서 · 기획서 · 공문', kind: 'output', icon: markRaw(FileText), color: '#476BFF', stage: 6 },
  { id: 'out-img', l: 73, t: 26, w: 26, h: 20, label: '이미지 (Image)', sub: '홍보 포스터 · 카드뉴스', kind: 'output', icon: markRaw(Image), color: '#8b5cf6', stage: 7 },
  { id: 'out-aud', l: 73, t: 50, w: 26, h: 20, label: '음성 (Audio)', sub: '안내 방송 · 나레이션', kind: 'output', icon: markRaw(Mic), color: '#10B981', stage: 8 },
  { id: 'out-code', l: 73, t: 74, w: 26, h: 20, label: '코드 · 데이터 (Code)', sub: '엑셀 수식 · 분석 자동화', kind: 'output', icon: markRaw(Code2), color: '#F5512E', stage: 9 },
]

const INK = '#2B2620', SAPPHIRE = '#476BFF', AMBER = '#D9930A'

function draw() {
  const svg = overlay.value, cont = wrap.value
  if (!svg || !cont) return
  const W = cont.clientWidth, H = cont.clientHeight
  if (!W || !H) return

  svg.setAttribute('viewBox', `0 0 ${W} ${H}`)
  while (svg.firstChild) svg.removeChild(svg.firstChild)
  const rc = rough.svg(svg)

  const px = (b: Box) => ({
    x: (b.l / 100) * W,
    y: (b.t / 100) * H,
    w: (b.w / 100) * W,
    h: (b.h / 100) * H,
  })
  const at = (id: string) => px(boxes.find(b => b.id === id)!)

  // Draw Box borders for visible boxes
  boxes.forEach(b => {
    if (props.stage < b.stage) return
    const p = px(b)
    const stroke = b.kind === 'model'
      ? SAPPHIRE
      : b.kind === 'input'
        ? AMBER
        : b.color || INK
    const sw = b.kind === 'model' ? 2.4 : 1.8
    const roughness = b.kind === 'model' ? 1.8 : 1.3

    svg.appendChild(
      rc.rectangle(p.x, p.y, p.w, p.h, {
        roughness,
        bowing: 1.2,
        strokeWidth: sw,
        stroke,
        fill: b.kind === 'model' ? 'rgba(71, 107, 255, 0.05)' : undefined,
      })
    )
  })

  // Helper for drawing curved rough arrow
  const drawCurvedArrow = (
    x1: number, y1: number,
    cx1: number, cy1: number,
    cx2: number, cy2: number,
    x2: number, y2: number,
    color: string
  ) => {
    const pathData = `M ${x1.toFixed(1)} ${y1.toFixed(1)} C ${cx1.toFixed(1)} ${cy1.toFixed(1)}, ${cx2.toFixed(1)} ${cy2.toFixed(1)}, ${x2.toFixed(1)} ${y2.toFixed(1)}`
    svg.appendChild(
      rc.path(pathData, {
        roughness: 1.2,
        bowing: 1.1,
        strokeWidth: 2.2,
        stroke: color,
      })
    )

    const dx = x2 - cx2
    const dy = y2 - cy2
    const angle = Math.atan2(dy, dx)
    const L = 10

    svg.appendChild(
      rc.line(
        x2, y2,
        x2 - L * Math.cos(angle - 0.42),
        y2 - L * Math.sin(angle - 0.42),
        { roughness: 1.0, strokeWidth: 2.2, stroke: color }
      )
    )
    svg.appendChild(
      rc.line(
        x2, y2,
        x2 - L * Math.cos(angle + 0.42),
        y2 - L * Math.sin(angle + 0.42),
        { roughness: 1.0, strokeWidth: 2.2, stroke: color }
      )
    )
  }

  // 1. Left inputs -> Central Model curves (Sequential stages 3, 4, 5)
  if (props.stage >= 2) {
    const model = at('model')
    const inputConfigs = [
      { id: 'in-prompt', targetRatio: 0.22, stage: 3 },
      { id: 'in-context', targetRatio: 0.50, stage: 4 },
      { id: 'in-pattern', targetRatio: 0.78, stage: 5 },
    ]

    inputConfigs.forEach(inpConf => {
      if (props.stage < inpConf.stage) return
      const inp = at(inpConf.id)
      const x1 = inp.x + inp.w
      const y1 = inp.y + inp.h / 2
      const x2 = model.x
      const y2 = model.y + model.h * inpConf.targetRatio
      const dx = x2 - x1
      const cx1 = x1 + dx * 0.52
      const cy1 = y1
      const cx2 = x1 + dx * 0.48
      const cy2 = y2

      drawCurvedArrow(x1, y1, cx1, cy1, cx2, cy2, x2, y2, AMBER)
    })
  }

  // 2. Central Model -> Right Multimodal Outputs curves (Sequential stages 6, 7, 8, 9)
  if (props.stage >= 2) {
    const model = at('model')
    const outputConfigs = [
      { id: 'out-txt', startRatio: 0.18, color: '#476BFF', stage: 6 },
      { id: 'out-img', startRatio: 0.38, color: '#8b5cf6', stage: 7 },
      { id: 'out-aud', startRatio: 0.62, color: '#10B981', stage: 8 },
      { id: 'out-code', startRatio: 0.82, color: '#F5512E', stage: 9 },
    ]

    outputConfigs.forEach(out => {
      if (props.stage < out.stage) return
      const outBox = at(out.id)
      const x1 = model.x + model.w
      const y1 = model.y + model.h * out.startRatio
      const x2 = outBox.x
      const y2 = outBox.y + outBox.h / 2
      const dx = x2 - x1
      const cx1 = x1 + dx * 0.50
      const cy1 = y1
      const cx2 = x1 + dx * 0.50
      const cy2 = y2

      drawCurvedArrow(x1, y1, cx1, cy1, cx2, cy2, x2, y2, out.color)
    })
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

const styleOf = (b: Box) => ({
  left: b.l + '%',
  top: b.t + '%',
  width: b.w + '%',
  height: b.h + '%',
})
</script>

<template>
  <div class="w-full flex flex-col items-center select-none">
    <!-- Top Claim Statement with Stage-based Red Strikethrough (Stage 0 -> 1) -->
    <div class="w-full mb-1 flex items-center justify-start gap-3 flex-wrap min-h-[30px] px-1">
      <div class="relative inline-block">
        <span
          class="text-base font-bold transition-all duration-300"
          :class="stage >= 1 ? 'text-slate-400 line-through decoration-rose-500 decoration-3' : 'text-slate-100'"
          style="font-family: 'Kalam', 'Source Serif 4', cursive;"
        >
          AI는 저장된 문장을 복사해서 꺼내온다
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
        다음에 올 확률이 가장 높은 단어를 계속 예측하여 조립한다
      </span>
    </div>

    <!-- Hand-drawn Architecture Canvas (Fixed Height) -->
    <div ref="wrap" class="sketch-wrap">
      <svg ref="overlay" class="sketch-overlay" />

      <!-- Boxes -->
      <div
        v-for="b in boxes"
        v-show="stage >= b.stage"
        :key="b.id"
        class="sketch-box"
        :class="b.kind"
        :style="styleOf(b)"
      >
        <div class="flex items-center gap-1.5 justify-center">
          <component
            :is="b.icon"
            v-if="b.icon"
            class="sketch-icon"
            :size="b.kind === 'model' ? 26 : 16"
            :style="{ color: b.color || 'inherit' }"
          />
          <span class="box-title" :style="{ color: b.color || 'inherit' }">{{ b.label }}</span>
        </div>
        <span v-if="b.sub" class="box-sub">{{ b.sub }}</span>
      </div>
    </div>

    <!-- NIST Standard Definition - Fixed Reserved Space with Zero Layout Shift -->
    <div
      class="w-full mt-2 transition-all duration-500"
      :class="stage >= 10 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2 pointer-events-none'"
    >
      <div class="flex items-center gap-5 bg-amber-50/70 rounded-xl px-5 py-2.5 border-l-4 border-emerald-500 shadow-xs">
        <img
          :src="resolveAsset('/nist-logo.png')"
          class="h-13 w-auto object-contain shrink-0"
          alt="NIST 미국 국립표준기술연구소"
        />
        <div class="flex-1">
          <div class="text-[11px] font-bold font-mono text-emerald-300 uppercase tracking-wider mb-0.5">
            NIST 공식 표준 정의 (미국 국립표준기술연구소 AI Risk Management Framework)
          </div>
          <div class="text-[14.5px] text-slate-100 font-serif leading-relaxed italic font-medium">
            “학습 데이터의 구조와 특성을 분석하여, 이를 바탕으로 <strong>새롭고 독창적인 합성 콘텐츠(Synthetic Content)</strong>를 생성해내는 인공지능 기술”
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sketch-wrap {
  position: relative;
  width: 100%;
  height: 220px;
  margin-top: 0.1rem;
}

.sketch-overlay {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.sketch-box {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Kalam', cursive;
  font-weight: 700;
  text-align: center;
  padding: 0.15rem 0.35rem;
  line-height: 1.15;
  box-sizing: border-box;
}

.sketch-box.input {
  color: #8C5800;
  font-size: 0.84rem;
}

.sketch-box.model {
  color: #1E3A8A;
  font-size: 1.25rem;
  gap: 0.35rem;
}

.sketch-box.output {
  font-size: 0.84rem;
  align-items: flex-start;
  padding-left: 0.65rem;
}

.box-title {
  font-weight: 700;
  letter-spacing: -0.01em;
}

.box-sub {
  font-family: 'Radio Canada Big', sans-serif;
  font-size: 0.68rem;
  font-weight: 600;
  color: #716657;
  margin-top: 0.15rem;
}

.sketch-icon {
  flex-shrink: 0;
}
</style>
