<script setup lang="ts">
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const { currentSlideRoute } = useNav()

const frontmatter = computed(() => (currentSlideRoute.value.meta?.slide as any)?.frontmatter || {})
const glow = computed(() => String(frontmatter.value.glow || 'bottom'))
const opacity = computed(() => Number(frontmatter.value.glowOpacity ?? 0.32))
const hue = computed(() => Number(frontmatter.value.glowHue ?? 170))

const style = computed(() => ({
  '--kit-glow-opacity': opacity.value,
  '--kit-glow-hue': String(hue.value) + 'deg',
}))
</script>

<template>
  <div class="kit-ambient" :class="'kit-ambient--' + glow" :style="style" aria-hidden="true">
    <div class="kit-ambient__orb kit-ambient__orb--one" />
    <div class="kit-ambient__orb kit-ambient__orb--two" />
  </div>
</template>

<style scoped>
.kit-ambient {
  position: absolute;
  z-index: -1;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  opacity: var(--kit-glow-opacity);
  filter: blur(42px) saturate(1.1);
}

.kit-ambient__orb {
  position: absolute;
  width: 58%;
  height: 62%;
  border-radius: 50%;
  background: hsl(var(--kit-glow-hue) 80% 42% / 0.24);
  transform: translateZ(0);
}

.kit-ambient__orb--one {
  right: -18%;
  bottom: -36%;
}

.kit-ambient__orb--two {
  left: -25%;
  bottom: -48%;
  width: 44%;
  height: 48%;
  background: hsl(calc(var(--kit-glow-hue) + 42deg) 78% 50% / 0.12);
}

.kit-ambient--top .kit-ambient__orb--one {
  top: -34%;
  bottom: auto;
}

.kit-ambient--left .kit-ambient__orb--one {
  right: auto;
  left: -20%;
}

.kit-ambient--right .kit-ambient__orb--one {
  right: -20%;
}

.kit-ambient--center .kit-ambient__orb--one {
  right: 18%;
  bottom: -30%;
}

.kit-ambient--full .kit-ambient__orb--one {
  right: 14%;
  bottom: -24%;
  width: 72%;
  height: 72%;
}
</style>
