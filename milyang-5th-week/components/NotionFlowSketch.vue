<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import rough from 'roughjs'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const root = ref<HTMLElement | null>(null)
const canvasEl = ref<HTMLCanvasElement | null>(null)

const stepBoxes = ref([
  { x: 12, y: 35, w: 180, h: 135 },
  { x: 220, y: 35, w: 180, h: 135 },
  { x: 428, y: 35, w: 180, h: 135 },
  { x: 636, y: 30, w: 180, h: 145 }
])

const stepCenters = ref<number[]>([102, 310, 518, 726])

const tags = [
  '1. 템플릿 탐색',
  '2. 구조 해체',
  '3. 템플릿 복제 & 튜닝',
  '4. 웹으로 게시 (완료)'
]

function draw() {
  const canvas = canvasEl.value
  const container = root.value
  if (!canvas || !container) return

  const W = container.clientWidth || 840
  const H = 210

  // High-DPI Retina resolution setup
  const dpr = Math.max(2, window.devicePixelRatio || 1)
  canvas.width = W * dpr
  canvas.height = H * dpr
  canvas.style.width = `${W}px`
  canvas.style.height = `${H}px`

  const rc = rough.canvas(canvas)
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.scale(dpr, dpr)
  ctx.clearRect(0, 0, W, H)
  const stage = props.stage

  // 4등분 동적 좌표 계산
  const pad = 12
  const arrowW = 28
  const bw = Math.max(140, (W - pad * 2 - arrowW * 3) / 4)
  const bh = 135
  const by = 35

  const boxes = []
  const centers: number[] = []
  for (let i = 0; i < 4; i++) {
    const x = pad + i * (bw + arrowW)
    const isStep4 = i === 3
    boxes.push({
      x,
      y: isStep4 ? by - 5 : by,
      w: bw,
      h: isStep4 ? bh + 10 : bh
    })
    centers.push(x + bw / 2)
  }
  stepBoxes.value = boxes
  stepCenters.value = centers

  const cy = by + bh / 2

  // 1단계 박스
  rc.rectangle(boxes[0].x, boxes[0].y, boxes[0].w, boxes[0].h, {
    stroke: '#2563EB',
    roughness: 1.6,
    strokeWidth: 2.2,
    fill: '#EFF6FF',
    fillStyle: 'solid'
  })

  if (stage < 1) return

  // 화살표 1
  const a1_x1 = boxes[0].x + bw + 4
  const a1_x2 = a1_x1 + arrowW - 8
  rc.line(a1_x1, cy, a1_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1.2 })
  rc.line(a1_x2 - 7, cy - 5, a1_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })
  rc.line(a1_x2 - 7, cy + 5, a1_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })

  // 2단계 박스
  rc.rectangle(boxes[1].x, boxes[1].y, boxes[1].w, boxes[1].h, {
    stroke: '#D97706',
    roughness: 1.6,
    strokeWidth: 2.2,
    fill: '#FFFBEB',
    fillStyle: 'solid'
  })

  if (stage < 2) return

  // 화살표 2
  const a2_x1 = boxes[1].x + bw + 4
  const a2_x2 = a2_x1 + arrowW - 8
  rc.line(a2_x1, cy, a2_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1.2 })
  rc.line(a2_x2 - 7, cy - 5, a2_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })
  rc.line(a2_x2 - 7, cy + 5, a2_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })

  // 3단계 박스
  rc.rectangle(boxes[2].x, boxes[2].y, boxes[2].w, boxes[2].h, {
    stroke: '#7C3AED',
    roughness: 1.6,
    strokeWidth: 2.2,
    fill: '#F5F3FF',
    fillStyle: 'solid'
  })

  if (stage < 3) return

  // 화살표 3
  const a3_x1 = boxes[2].x + bw + 4
  const a3_x2 = a3_x1 + arrowW - 8
  rc.line(a3_x1, cy, a3_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1.2 })
  rc.line(a3_x2 - 7, cy - 5, a3_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })
  rc.line(a3_x2 - 7, cy + 5, a3_x2, cy, { stroke: '#475569', strokeWidth: 2.2, roughness: 1 })

  // 4단계 박스 (완료 하이라이트)
  rc.rectangle(boxes[3].x, boxes[3].y, boxes[3].w, boxes[3].h, {
    stroke: '#059669',
    roughness: 1.8,
    strokeWidth: 2.6,
    fill: '#ECFDF5',
    fillStyle: 'solid'
  })
}

let ro: ResizeObserver
onMounted(() => {
  nextTick(draw)
  ro = new ResizeObserver(() => draw())
  if (root.value) ro.observe(root.value)
})
onUnmounted(() => ro?.disconnect())
watch(() => props.stage, () => nextTick(draw))
</script>

<template>
  <div ref="root" class="sketch-wrap relative select-none">
    <!-- Rough Canvas for Crisp Hand-drawn Outlines -->
    <canvas ref="canvasEl" class="sketch-canvas"></canvas>

    <!-- Crystal Clear HTML Overlay Elements (Slide 42 Style) -->
    <div class="absolute inset-0 pointer-events-none">
      <!-- Step 1 Overlay -->
      <div
        v-if="stage >= 0 && stepBoxes[0]"
        class="absolute p-3 flex flex-col justify-between text-center box-border"
        :style="{
          left: `${stepBoxes[0].x}px`,
          top: `${stepBoxes[0].y}px`,
          width: `${stepBoxes[0].w}px`,
          height: `${stepBoxes[0].h}px`
        }"
      >
        <div>
          <div class="text-xs font-black text-blue-700 tracking-tight flex items-center justify-center gap-1">
            <span>📑</span>
            <span>공식 템플릿 탐색</span>
          </div>
          <div class="mt-1.5 inline-block text-[9.5px] font-mono font-bold text-blue-600 bg-blue-100/90 px-2 py-0.5 rounded-md">
            notion.com/ko/templates
          </div>
        </div>
        <div class="text-[11px] text-slate-600 font-medium leading-snug">
          합격자 이력서 레퍼런스 발굴
        </div>
      </div>

      <!-- Step 2 Overlay -->
      <div
        v-if="stage >= 1 && stepBoxes[1]"
        class="absolute p-3 flex flex-col justify-between text-center box-border"
        :style="{
          left: `${stepBoxes[1].x}px`,
          top: `${stepBoxes[1].y}px`,
          width: `${stepBoxes[1].w}px`,
          height: `${stepBoxes[1].h}px`
        }"
      >
        <div>
          <div class="text-xs font-black text-amber-700 tracking-tight flex items-center justify-center gap-1">
            <span>🔍</span>
            <span>레이아웃 해체</span>
          </div>
          <div class="mt-1.5 inline-block text-[9.5px] font-mono font-bold text-amber-800 bg-amber-100/90 px-2 py-0.5 rounded-md">
            Hero + About + Project
          </div>
        </div>
        <div class="text-[11px] text-slate-600 font-medium leading-snug">
          우수 구성 요소 벤치마킹
        </div>
      </div>

      <!-- Step 3 Overlay -->
      <div
        v-if="stage >= 2 && stepBoxes[2]"
        class="absolute p-3 flex flex-col justify-between text-center box-border"
        :style="{
          left: `${stepBoxes[2].x}px`,
          top: `${stepBoxes[2].y}px`,
          width: `${stepBoxes[2].w}px`,
          height: `${stepBoxes[2].h}px`
        }"
      >
        <div>
          <div class="text-xs font-black text-purple-700 tracking-tight flex items-center justify-center gap-1">
            <span>✏️</span>
            <span>템플릿 복제 & 튜닝</span>
          </div>
          <div class="mt-1.5 inline-block text-[9.5px] font-mono font-bold text-purple-700 bg-purple-100/90 px-2 py-0.5 rounded-md">
            우측 상단 [복제] 클릭
          </div>
        </div>
        <div class="text-[11px] text-slate-600 font-medium leading-snug">
          내 프로젝트 & 성과 DB 이식
        </div>
      </div>

      <!-- Step 4 Overlay -->
      <div
        v-if="stage >= 3 && stepBoxes[3]"
        class="absolute p-3 flex flex-col justify-between text-center box-border"
        :style="{
          left: `${stepBoxes[3].x}px`,
          top: `${stepBoxes[3].y}px`,
          width: `${stepBoxes[3].w}px`,
          height: `${stepBoxes[3].h}px`
        }"
      >
        <div>
          <div class="text-xs font-black text-emerald-800 tracking-tight flex items-center justify-center gap-1">
            <span>🌐</span>
            <span>웹으로 게시 (Publish)</span>
          </div>
          <div class="mt-1.5 inline-block text-[9.5px] font-mono font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded-md">
            [공유] ➔ [웹으로 게시]
          </div>
        </div>
        <div class="text-[11px] text-slate-700 font-bold leading-snug">
          나만의 노션 웹 포폴 링크 완성 ✨
        </div>
      </div>
    </div>

    <!-- Step Indicator Bottom Legends -->
    <div class="sketch-legend">
      <div 
        v-for="(tag, i) in tags" 
        :key="i"
        class="step-tag" 
        :style="{ left: stepCenters[i] + 'px' }" 
        :class="{ active: stage >= i, dim: stage < i }"
      >
        {{ tag }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.sketch-wrap {
  width: 100%;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 18px;
  padding: 0.8rem 1rem 0.6rem;
  margin-top: 0.5rem;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
}

.sketch-canvas {
  width: 100%;
  height: 210px;
  display: block;
}

.sketch-legend {
  position: relative;
  width: 100%;
  height: 34px;
  margin-top: 0.3rem;
}

.step-tag {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  background: #FFFFFF;
  padding: 3.5px 12px;
  border-radius: 20px;
  border: 1.5px solid #E2E8F0;
  font-size: 0.75rem;
  color: #64748B;
  font-weight: 700;
  font-family: 'Pretendard', 'Inter', sans-serif;
  white-space: nowrap;
  transition: all 0.25s ease;
  box-shadow: 0 2px 5px rgba(0,0,0,0.03);
}

.step-tag.active {
  background: #EFF6FF;
  border-color: #2563EB;
  color: #1D4ED8;
  transform: translateX(-50%) translateY(-2px);
  box-shadow: 0 4px 10px rgba(37, 99, 235, 0.15);
}

.step-tag.dim {
  opacity: 0.35;
  background: #F8FAFC;
}
</style>
