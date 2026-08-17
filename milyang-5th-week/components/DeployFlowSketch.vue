<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import rough from 'roughjs'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const root = ref<HTMLElement | null>(null)
const canvasEl = ref<HTMLCanvasElement | null>(null)
const stepCenters = ref<number[]>([100, 300, 500, 700])

const tags = [
  '1. Gemini 캔버스 코딩',
  '2. 단일 HTML 다운로드',
  '3. Netlify 드래그앤드롭',
  '4. 글로벌 Live 배포 (완료)'
]

function draw() {
  const canvas = canvasEl.value
  const container = root.value
  if (!canvas || !container) return

  const W = container.clientWidth || 840
  const H = 270
  canvas.width = W
  canvas.height = H

  const rc = rough.canvas(canvas)
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, W, H)
  const stage = props.stage

  // 완벽한 4등분 동적 좌표 계산 (컨테이너 가로폭에 100% 동기화)
  const pad = 12
  const arrowW = 32
  const bw = Math.max(130, (W - pad * 2 - arrowW * 3) / 4)
  const bh = 125
  const by = 55

  const centers: number[] = []
  for (let i = 0; i < 4; i++) {
    const x = pad + i * (bw + arrowW)
    centers.push(x + bw / 2)
  }
  stepCenters.value = centers

  // 1단계 박스 (Click 0)
  const x0 = pad
  const b1 = { stroke: '#1A73E8', roughness: 1.8, strokeWidth: 2.2, fill: '#E8F0FE', fillStyle: 'solid' }
  rc.rectangle(x0, by, bw, bh, b1)
  ctx.font = 'bold 13.5px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#1A73E8'
  ctx.textAlign = 'center'
  ctx.fillText('✨ Gemini Canvas', centers[0], by + 36)
  ctx.font = '11px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#444'
  ctx.fillText('자연어 바이브 코딩', centers[0], by + 64)
  ctx.fillText('실시간 프리뷰 캔버스', centers[0], by + 86)

  if (stage < 1) return

  // 화살표 1
  const a1_x1 = x0 + bw + 4, a1_x2 = a1_x1 + arrowW - 8
  const cy = by + bh / 2
  rc.line(a1_x1, cy, a1_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1.4 })
  rc.line(a1_x2 - 8, cy - 6, a1_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })
  rc.line(a1_x2 - 8, cy + 6, a1_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })

  // 2단계 박스 (Click 1)
  const x1 = pad + 1 * (bw + arrowW)
  const b2 = { stroke: '#D9930A', roughness: 1.8, strokeWidth: 2.2, fill: '#FFF5E0', fillStyle: 'solid' }
  rc.rectangle(x1, by, bw, bh, b2)
  ctx.font = 'bold 13.5px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#D9930A'
  ctx.fillText('📄 index.html', centers[1], by + 36)
  ctx.font = '11px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#444'
  ctx.fillText('CSS & JS 내장', centers[1], by + 64)
  ctx.fillText('원클릭 파일 다운로드', centers[1], by + 86)

  if (stage < 2) return

  // 화살표 2
  const a2_x1 = x1 + bw + 4, a2_x2 = a2_x1 + arrowW - 8
  rc.line(a2_x1, cy, a2_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1.4 })
  rc.line(a2_x2 - 8, cy - 6, a2_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })
  rc.line(a2_x2 - 8, cy + 6, a2_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })

  // 3단계 박스 (Click 2)
  const x2 = pad + 2 * (bw + arrowW)
  const b3 = { stroke: '#00C7B7', roughness: 1.8, strokeWidth: 2.2, fill: '#E6FAF8', fillStyle: 'solid' }
  rc.rectangle(x2, by, bw, bh, b3)
  ctx.font = 'bold 13.5px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#008B80'
  ctx.fillText('🚀 Netlify Drop', centers[2], by + 36)
  ctx.font = '11px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#333'
  ctx.fillText('브라우저 드래그 앤 드롭', centers[2], by + 64)
  ctx.fillText('무료 글로벌 CDN 호스팅', centers[2], by + 86)

  if (stage < 3) return

  // 화살표 3
  const a3_x1 = x2 + bw + 4, a3_x2 = a3_x1 + arrowW - 8
  rc.line(a3_x1, cy, a3_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1.4 })
  rc.line(a3_x2 - 8, cy - 6, a3_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })
  rc.line(a3_x2 - 8, cy + 6, a3_x2, cy, { stroke: '#2B2620', strokeWidth: 2, roughness: 1 })

  // 4단계 박스 (Click 3+)
  const x3 = pad + 3 * (bw + arrowW)
  const b4 = { stroke: '#1B7A55', roughness: 2, strokeWidth: 2.6, fill: '#EEFFFA', fillStyle: 'solid' }
  rc.rectangle(x3, by - 8, bw, bh + 16, b4)
  ctx.font = 'bold 14px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#1B7A55'
  ctx.fillText('🌐 나만의 Live URL', centers[3], by + 30)
  ctx.font = '10.5px Radio Canada Big, sans-serif'
  ctx.fillStyle = '#1B7A55'
  ctx.fillText('https://my-vibe.netlify.app', centers[3], by + 56)
  ctx.fillText('HTTPS 보안 인증서 기본', centers[3], by + 78)
  ctx.fillText('전 세계 어디서나 접속', centers[3], by + 100)
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
  <div ref="root" class="deploy-sketch-wrap">
    <canvas ref="canvasEl" class="sketch-canvas"></canvas>
    
    <!-- 4개 손그림 박스 중심(centers[i])과 픽셀 단위 1:1 절대 동기화 -->
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
.deploy-sketch-wrap {
  width: 100%;
  background: #FAF8F4;
  border: 1.5px solid #E7E0D4;
  border-radius: 16px;
  padding: 1rem 1rem 0.6rem;
  margin-top: 0.5rem;
  position: relative;
  box-shadow: 0 4px 16px rgba(43, 35, 27, 0.04);
}

.sketch-canvas {
  width: 100%;
  height: 270px;
  display: block;
}

.sketch-legend {
  position: relative;
  width: 100%;
  height: 38px;
  margin-top: 0.4rem;
}

.step-tag {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  background: #ffffff;
  padding: 4px 12px;
  border-radius: 20px;
  border: 1.5px solid #E7E0D4;
  font-size: 0.76rem;
  color: #857B6E;
  font-weight: 700;
  white-space: nowrap;
  transition: all 0.25s ease;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
}

.step-tag.active {
  background: #EEFFFA;
  border-color: #1B7A55;
  color: #1B7A55;
  transform: translateX(-50%) translateY(-2px);
  box-shadow: 0 4px 10px rgba(27, 122, 85, 0.2);
}

.step-tag.dim {
  opacity: 0.35;
  background: #F4EDE2;
}
</style>
