<script setup lang="ts">
/**
 * nekomeowww Seeded Ambient Polygon Glow Base Layer
 *
 * Properties available in slide frontmatter:
 * - glow: 'full' | 'top' | 'bottom' | 'left' | 'right' | 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right' | 'center' | 'topmost'
 * - glowOpacity: number (default: 0.4)
 * - glowHue: number (optional explicit per-slide hue override)
 * - glowSeed: string | false (default: 'default')
 * - theme: 'dark' | 'light' (default: 'dark')
 */
import { useNav } from '@slidev/client'
import seedrandom from 'seedrandom'
import { computed, ref, watch } from 'vue'

const { currentSlideRoute } = useNav()

export type Range = [number, number]
export type Distribution =
  | 'full'
  | 'top'
  | 'bottom'
  | 'left'
  | 'right'
  | 'top-left'
  | 'top-right'
  | 'bottom-left'
  | 'bottom-right'
  | 'center'
  | 'topmost'

const formatter = computed(() => (currentSlideRoute.value.meta?.slide as any)?.frontmatter || {})
const distribution = computed(() => (formatter.value.glow || 'full') as Distribution)
const opacity = computed<number>(() => +(formatter.value.glowOpacity ?? 0.4))

// Section Hue progression: Emerald Green (105deg) -> Warm Amber (0deg) -> Deep Cyan (180deg) -> Agent Violet (270deg)
const hueProgression = {
  from: 105,
  to: 0,
  startSlide: 1,
  endSlide: 20,
} as const

const hue = computed<number>(() => {
  const explicitHue = formatter.value.glowHue
  if (explicitHue !== undefined && explicitHue !== null && explicitHue !== '')
    return +explicitHue

  const { from, to, startSlide, endSlide } = hueProgression
  if (endSlide <= startSlide)
    return to

  const progress = Math.min(1, Math.max(0, (currentSlideRoute.value.no - startSlide) / (endSlide - startSlide)))
  return from + (to - from) * progress
})

const seed = computed<string>(() => (formatter.value.glowSeed === 'false' || formatter.value.glowSeed === false)
  ? Date.now().toString()
  : formatter.value.glowSeed || 'default',
)
const theme = computed(() => (formatter.value.theme || 'dark') as 'light' | 'dark')

const overflow = 0.3
const disturb = 0.3
const disturbChance = 0.3

function distributionToLimits(distribution: Distribution) {
  const min = -0.2
  const max = 1.2
  let x: Range = [min, max]
  let y: Range = [min, max]

  function intersection(a: Range, b: Range): Range {
    return [Math.max(a[0], b[0]), Math.min(a[1], b[1])]
  }

  const limits = distribution.split('-')

  for (const limit of limits) {
    switch (limit) {
      case 'topmost':
        y = intersection(y, [-0.5, 0])
        break
      case 'top':
        y = intersection(y, [min, 0.6])
        break
      case 'bottom':
        y = intersection(y, [0.4, max])
        break
      case 'left':
        x = intersection(x, [min, 0.6])
        break
      case 'right':
        x = intersection(x, [0.4, max])
        break
      case 'center':
        x = intersection(x, [0.25, 0.75])
        y = intersection(y, [0.25, 0.75])
        break
      case 'full':
        x = intersection(x, [0, 1])
        y = intersection(y, [0, 1])
        break
      default:
        break
    }
  }

  return { x, y }
}

function distance2([x1, y1]: Range, [x2, y2]: Range) {
  return (x2 - x1) ** 2 + (y2 - y1) ** 2
}

function usePoly(number = 16) {
  function getPoints(): Range[] {
    const limits = distributionToLimits(distribution.value)
    const rng = seedrandom(`${seed.value}-${currentSlideRoute.value.no}`)
    function randomBetween([a, b]: Range) {
      return rng() * (b - a) + a
    }
    function applyOverflow(random: number, overflow: number) {
      random = random * (1 + overflow * 2) - overflow
      return rng() < disturbChance ? random + (rng() - 0.5) * disturb : random
    }
    return Array.from({ length: number })
      .fill(0)
      .map(() => [
        applyOverflow(randomBetween(limits.x), overflow),
        applyOverflow(randomBetween(limits.y), overflow),
      ])
  }

  const points = ref<Range[]>(getPoints())
  const poly = computed(() => points.value.map(([x, y]) => `${x * 100}% ${y * 100}%`).join(', '))

  function jumpPoints() {
    const newPoints = new Set(getPoints())
    points.value = points.value.map((o) => {
      let minDistance = Number.POSITIVE_INFINITY
      let closest: Range | undefined
      for (const n of newPoints) {
        const d = distance2(o, n)
        if (d < minDistance) {
          minDistance = d
          closest = n
        }
      }
      if (closest)
        newPoints.delete(closest)

      return closest
    }).filter(Boolean) as Range[]
  }

  watch(currentSlideRoute, () => {
    jumpPoints()
  })

  return poly
}

const poly1 = usePoly(10)
const poly2 = usePoly(6)
const poly3 = usePoly(3)
</script>

<template>
  <div>
    <div
      class="bg transform-gpu overflow-hidden pointer-events-none"
      :style="{ filter: `blur(75px) hue-rotate(${hue}deg)` }"
      :class="[
        theme === 'light' ? 'bg-[#f8fafc] scale-120' : 'bg-[#121212]',
      ]"
      aria-hidden="true"
    >
      <div
        class="clip bg-gradient-to-r from-[#10b981] via-[#facc15] to-[#06b6d4]"
        :style="{ 'clip-path': `polygon(${poly1})`, 'opacity': opacity }"
      />
      <div
        class="clip bg-gradient-to-l from-[#8b5cf6] via-[#ec4899] to-[#facc15]"
        :style="{ 'clip-path': `polygon(${poly2})`, 'opacity': opacity * 0.85 }"
      />
      <div
        class="clip bg-gradient-to-t from-[#06b6d4] to-[#10b981]"
        :style="{ 'clip-path': `polygon(${poly3})`, 'opacity': opacity * 0.5 }"
      />
    </div>
  </div>
</template>

<style scoped>
.bg,
.clip {
  transition: all 2.5s ease;
}

.bg {
  position: absolute;
  inset: 0;
  z-index: -10;
}

.clip {
  aspect-ratio: 16 / 9;
  position: absolute;
  inset: 0;
}
</style>
