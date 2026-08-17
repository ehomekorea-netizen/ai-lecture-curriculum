<script setup lang="ts">
import { ref, onMounted } from 'vue'
import rough from 'roughjs'

const svgEl = ref<SVGSVGElement | null>(null)
const INK = '#2B2620'
const SAPPHIRE = '#476BFF'

const B = { x: 20, y: 15, w: 380, h: 180, r: 24 }

function bubblePath() {
  const { x, y, w, h, r } = B
  return [
    `M ${x + r} ${y}`,
    `H ${x + w - r}`,
    `A ${r} ${r} 0 0 1 ${x + w} ${y + r}`,
    `V ${y + h - r}`,
    `A ${r} ${r} 0 0 1 ${x + w - r} ${y + h}`,
    `H ${x + r}`,
    `A ${r} ${r} 0 0 1 ${x} ${y + h - r}`,
    `V ${y + r}`,
    `A ${r} ${r} 0 0 1 ${x + r} ${y}`,
    'Z',
  ].join(' ')
}

onMounted(() => {
  const svg = svgEl.value
  if (!svg) return
  const rc = rough.svg(svg)
  svg.appendChild(rc.path(bubblePath(), {
    roughness: 1.6, bowing: 1.2, strokeWidth: 2.5, stroke: SAPPHIRE,
    fill: '#FFFFFF', fillStyle: 'solid',
  }))
})
</script>

<template>
  <div class="closing-wrap">
    <div class="bubble-area">
      <svg ref="svgEl" class="closing-svg" viewBox="0 0 420 210" />
      <div class="closing-text">
        <slot>
          5주간 수고 많으셨습니다!<br>
          여러분의 멋진 취업과 도전을<br>
          진심으로 응원합니다! 🚀
        </slot>
      </div>
    </div>
    <div class="cheer-icons">
      <span class="icon-item">🎓</span>
      <span class="icon-item">💼</span>
      <span class="icon-item">✨</span>
      <span class="icon-item">🚀</span>
    </div>
  </div>
</template>

<style scoped>
.closing-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  width: 420px;
}

.bubble-area {
  position: relative;
  width: 420px;
  height: 210px;
}

.closing-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.closing-text {
  position: absolute;
  inset: 15px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 1.8rem;
  text-align: center;
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.45;
  color: var(--ink);
}

.cheer-icons {
  display: flex;
  gap: 1.2rem;
  font-size: 2.4rem;
}

.icon-item {
  background: #fff;
  border: 1.5px solid var(--border);
  border-radius: 18px;
  padding: 0.5rem 0.8rem;
  box-shadow: 0 4px 12px rgba(43, 35, 27, 0.06);
  animation: float 3s ease-in-out infinite alternate;
}

.icon-item:nth-child(2) { animation-delay: 0.5s; }
.icon-item:nth-child(3) { animation-delay: 1s; }
.icon-item:nth-child(4) { animation-delay: 1.5s; }

@keyframes float {
  0% { transform: translateY(0px); }
  100% { transform: translateY(-8px); }
}
</style>
