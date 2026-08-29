<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'

const props = withDefaults(defineProps<{
  as?: string
  minFontSize?: number
  maxFontSize?: number
  singleLine?: boolean
  weight?: string | number
  color?: string
  align?: 'left' | 'center' | 'right'
  lineHeight?: number | string
  padding?: string | number
}>(), {
  as: 'div',
  minFontSize: 12,
  maxFontSize: 80,
  singleLine: false,
  weight: 'bold',
  color: '',
  align: 'left',
  lineHeight: 1.15,
  padding: 0
})

const containerRef = ref<HTMLElement | null>(null)
const textRef = ref<HTMLElement | null>(null)
const currentFontSize = ref<number>(props.maxFontSize)

const calculateFit = () => {
  if (!containerRef.value || !textRef.value) return

  const container = containerRef.value
  const text = textRef.value

  const containerWidth = container.clientWidth
  const containerHeight = container.clientHeight

  if (containerWidth === 0 || containerHeight === 0) return

  let low = props.minFontSize
  let high = props.maxFontSize
  let bestSize = props.minFontSize

  // Binary search for optimal font size that fits both width & height
  for (let i = 0; i < 12; i++) {
    const mid = (low + high) / 2
    text.style.fontSize = `${mid}px`

    const isOverflowWidth = text.scrollWidth > containerWidth + 1
    const isOverflowHeight = text.scrollHeight > containerHeight + 1

    if (isOverflowWidth || isOverflowHeight) {
      high = mid
    } else {
      bestSize = mid
      low = mid
    }
  }

  currentFontSize.value = Math.floor(bestSize * 10) / 10
  text.style.fontSize = `${currentFontSize.value}px`
}

let resizeObserver: ResizeObserver | null = null

onMounted(async () => {
  await nextTick()
  calculateFit()

  if (typeof ResizeObserver !== 'undefined' && containerRef.value) {
    resizeObserver = new ResizeObserver(() => {
      calculateFit()
    })
    resizeObserver.observe(containerRef.value)
  }

  window.addEventListener('resize', calculateFit)
})

onUnmounted(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
  }
  window.removeEventListener('resize', calculateFit)
})

watch(() => [props.minFontSize, props.maxFontSize, props.singleLine], () => {
  nextTick(calculateFit)
})
</script>

<template>
  <component
    :is="as"
    ref="containerRef"
    class="autofit-container"
    :style="{
      textAlign: align,
      color: color || 'inherit',
      padding: typeof padding === 'number' ? `${padding}px` : padding
    }"
  >
    <span
      ref="textRef"
      class="autofit-text-inner"
      :style="{
        fontSize: `${currentFontSize}px`,
        fontWeight: weight,
        lineHeight: lineHeight,
        whiteSpace: singleLine ? 'nowrap' : 'normal'
      }"
    >
      <slot />
    </span>
  </component>
</template>

<style scoped>
.autofit-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-sizing: border-box;
}

.autofit-text-inner {
  display: inline-block;
  max-width: 100%;
  word-break: keep-all;
  overflow-wrap: break-word;
  transition: font-size 0.05s ease-out;
}
</style>
