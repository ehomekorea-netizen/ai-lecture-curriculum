<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, computed } from 'vue'
import { onSlideEnter } from '@slidev/client'
import rough from 'roughjs'

const props = defineProps<{ kicker?: string; title: string; art?: string }>()

const svgEl = ref<SVGSVGElement | null>(null)
const titleEl = ref<HTMLElement | null>(null)

const SAPPHIRE = '#2563EB', MINT = '#10B981'
const RULE_H = 20

const isImage = computed(() => {
  if (!props.art) return false
  return props.art.startsWith('/') || props.art.startsWith('http') || props.art.includes('.svg') || props.art.includes('.png') || props.art.includes('.jpg') || props.art.includes('.jpeg') || props.art.includes('.webp')
})

const isLogo = computed(() => {
  if (!props.art) return false
  return props.art.toLowerCase().includes('logo')
})

const base = import.meta.env.BASE_URL || '/'
const resolvedArt = computed(() => {
  if (!props.art) return ''
  if (!isImage.value || props.art.startsWith('http') || props.art.startsWith('data:')) return props.art
  let clean = props.art.startsWith('/') ? props.art.slice(1) : props.art
  if (!clean.startsWith('img/')) {
    clean = `img/${clean}`
  }
  return `${base}${clean}`
})

function draw() {
  const svg = svgEl.value, t = titleEl.value
  if (!svg || !t) return
  const w = t.offsetWidth
  if (!w) return
  svg.setAttribute('viewBox', `0 0 ${w} ${RULE_H}`)
  svg.style.width = w + 'px'
  while (svg.firstChild) svg.removeChild(svg.firstChild)

  const rc = rough.svg(svg)
  const line1 = rc.line(3, 7, w - 4, 6, {
    roughness: 1.5, bowing: 1.5, strokeWidth: 3.5, stroke: SAPPHIRE,
  })
  const line2 = rc.line(10, 14, Math.min(w * 0.72, w - 10), 13, {
    roughness: 1.8, bowing: 2.2, strokeWidth: 2.5, stroke: MINT,
  })

  const paths1 = Array.from(line1.querySelectorAll('path'))
  const paths2 = Array.from(line2.querySelectorAll('path'))

  paths1.forEach(p => {
    const len = Math.ceil(p.getTotalLength?.() || w * 1.2)
    p.style.strokeDasharray = `${len}`
    p.style.strokeDashoffset = `${len}`
    p.style.transition = 'stroke-dashoffset 0.65s cubic-bezier(0.2, 0.8, 0.2, 1) 0.15s'
  })

  paths2.forEach(p => {
    const len = Math.ceil(p.getTotalLength?.() || w * 0.9)
    p.style.strokeDasharray = `${len}`
    p.style.strokeDashoffset = `${len}`
    p.style.transition = 'stroke-dashoffset 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) 0.45s'
  })

  svg.appendChild(line1)
  svg.appendChild(line2)

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      paths1.forEach(p => { p.style.strokeDashoffset = '0' })
      paths2.forEach(p => { p.style.strokeDashoffset = '0' })
    })
  })
}

let ro: ResizeObserver
onMounted(() => {
  nextTick(draw)
  ro = new ResizeObserver(() => draw())
  if (titleEl.value) ro.observe(titleEl.value)
})

onSlideEnter(() => {
  setTimeout(draw, 100)
})

onUnmounted(() => ro?.disconnect())
</script>

<template>
  <div class="sc">
    <div class="sc-body">
      <div v-if="kicker" class="sc-kicker">{{ kicker }}</div>
      <div class="sc-title-wrap">
        <h1 ref="titleEl" class="sc-title">{{ title }}</h1>
        <svg ref="svgEl" class="sc-rule" :height="RULE_H" />
      </div>
      <div v-if="$slots.default" class="sc-teaser"><slot /></div>
    </div>
    <div v-if="art" class="sc-art-wrap">
      <img
        v-if="isImage"
        :src="resolvedArt"
        class="sc-art-img"
        :class="{ 'is-logo': isLogo }"
        :alt="title"
      />
      <div v-else class="sc-art-emoji">{{ art }}</div>
    </div>
  </div>
</template>

<style scoped>
.sc {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2.5rem;
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 28px;
  padding: 2.2rem 2.8rem;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.06), 0 2px 6px rgba(15, 23, 42, 0.03);
}

.sc-body {
  text-align: left;
  flex: 1;
  min-width: 0;
}

.sc-kicker {
  display: inline-flex;
  align-items: center;
  font-family: 'Geist Mono', monospace;
  font-size: 0.76rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2563EB;
  background: #EFF6FF;
  border: 1px solid #DBEAFE;
  padding: 4px 12px;
  border-radius: 20px;
  margin-bottom: 0.8rem;
}

.sc-title-wrap {
  display: inline-block;
  max-width: 100%;
}

.sc-title {
  display: block;
  font-family: 'Pretendard', 'Inter', -apple-system, sans-serif !important;
  font-size: 2.1rem;
  font-weight: 800;
  line-height: 1.25;
  letter-spacing: -0.035em;
  color: #0F172A;
  margin: 0;
  word-break: keep-all;
  text-wrap: balance;
  background: linear-gradient(135deg, #0F172A 0%, #334155 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.sc-rule {
  display: block;
  margin-top: 0.35rem;
  overflow: visible;
}

.sc-teaser {
  margin-top: 1.2rem;
}

.sc-teaser:empty {
  display: none;
}

.sc-art-wrap {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 250px;
}

.sc-art-img {
  width: 250px;
  height: auto;
  max-height: 175px;
  object-fit: contain;
  border-radius: 18px;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.12);
  border: 1.5px solid #E2E8F0;
  background: #0B0F19;
  display: block;
}

.sc-art-img.is-logo {
  width: 170px;
  height: 170px;
  object-fit: contain;
  background: #FFFFFF;
  padding: 16px;
}

.sc-art-emoji {
  font-size: 5rem;
  line-height: 1;
  background: #F8FAFC;
  border: 1.5px solid #E2E8F0;
  border-radius: 24px;
  padding: 1.4rem 1.6rem;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
