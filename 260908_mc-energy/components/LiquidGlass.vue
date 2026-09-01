<script setup lang="ts">
withDefaults(defineProps<{
  as?: string
  glow?: 'pink' | 'cyan' | 'amber' | 'blue' | 'emerald' | 'violet' | 'neutral'
  radius?: number
}>(), {
  as: 'div',
  glow: 'neutral',
  radius: 18,
})
</script>

<template>
  <component
    :is="as"
    class="liquid-glass"
    :class="`liquid-glass-${glow}`"
    :style="{
      borderRadius: `${radius}px`,
    }"
  >
    <slot />
  </component>
</template>

<style scoped>
.liquid-glass {
  position: relative;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px) saturate(160%);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  border: 1px solid rgba(255, 255, 255, 0.12);
  transform: translateZ(0);
  backface-visibility: hidden;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(255, 255, 255, 0.12),
    0 16px 40px rgba(0, 0, 0, 0.28);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
}

.liquid-glass::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.18), transparent 42%),
    radial-gradient(circle at 18% 8%, rgba(255, 255, 255, 0.25), transparent 34%);
  opacity: 0.75;
}

.liquid-glass::after {
  content: '';
  position: absolute;
  left: 10%;
  right: 10%;
  bottom: 0;
  height: 44%;
  pointer-events: none;
  border-radius: 999px 999px 0 0;
  background:
    radial-gradient(85% 115% at 50% 100%, rgba(255, 255, 255, 0.35), transparent 62%),
    linear-gradient(180deg, transparent, rgba(255, 255, 255, 0.18));
  filter: blur(6px);
  opacity: 0.8;
  transform: translateY(40%);
}

.liquid-glass-pink {
  border-color: rgba(244, 114, 182, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(244, 114, 182, 0.18),
    0 16px 40px rgba(236, 72, 153, 0.16);
}

.liquid-glass-cyan {
  border-color: rgba(34, 211, 238, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(34, 211, 238, 0.18),
    0 16px 40px rgba(34, 211, 238, 0.16);
}

.liquid-glass-amber {
  border-color: rgba(251, 191, 36, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(251, 191, 36, 0.18),
    0 16px 40px rgba(245, 158, 11, 0.16);
}

.liquid-glass-blue {
  border-color: rgba(96, 165, 250, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(96, 165, 250, 0.18),
    0 16px 40px rgba(59, 130, 246, 0.2);
}

.liquid-glass-emerald {
  border-color: rgba(52, 211, 153, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(52, 211, 153, 0.18),
    0 16px 40px rgba(16, 185, 129, 0.2);
}

.liquid-glass-violet {
  border-color: rgba(167, 139, 250, 0.3);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.28),
    inset 0 -1px 0 rgba(167, 139, 250, 0.18),
    0 16px 40px rgba(139, 92, 246, 0.2);
}
</style>
