<script setup lang="ts">
import { ref, computed } from 'vue'

const props = withDefaults(defineProps<{
  code?: string
  lines?: string[]
  currentStep?: number
  lang?: string
}>(), {
  lang: 'markdown',
  currentStep: 0,
  lines: () => [
    '// 1단계: 분위기(Vibe) 정의',
    'const vibe = { persona: "Junior Planner", style: "Minimalism", color: "#1A2B4C" };',
    '// 2단계: 핵심 섹션 지시',
    'const sections = ["Hero (Typing)", "About (Lift Card)", "Projects", "Contact"];',
    '// 3단계: 제약사항 및 단일 HTML 번들링',
    'const constraints = { responsive: true, bundle: "single-html" };'
  ]
})

const activeIndex = ref(0)

const displayLines = computed(() => {
  if (props.code) {
    return props.code.split('\n')
  }
  return props.lines
})

function nextStep() {
  activeIndex.value = (activeIndex.value + 1) % displayLines.value.length
}
function prevStep() {
  activeIndex.value = (activeIndex.value - 1 + displayLines.value.length) % displayLines.value.length
}
</script>

<template>
  <div class="stepcode-container">
    <div class="stepcode-topbar">
      <span class="lang-tag">{{ lang }}</span>
      <div class="step-nav">
        <button class="step-btn" @click="prevStep">◀</button>
        <span class="step-counter">Line {{ activeIndex + 1 }} / {{ displayLines.length }}</span>
        <button class="step-btn" @click="nextStep">▶</button>
      </div>
    </div>

    <div class="stepcode-body">
      <div
        v-for="(line, idx) in displayLines"
        :key="idx"
        class="code-line-item"
        :class="{ active: idx === activeIndex }"
        @click="activeIndex = idx"
      >
        <span class="line-num">{{ idx + 1 }}</span>
        <span class="line-text">{{ line }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stepcode-container {
  width: 100%;
  max-width: 650px;
  background: #181824;
  border: 1.5px solid #2f3142;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
  margin: 0.8rem auto 0;
}

.stepcode-topbar {
  background: #202130;
  padding: 6px 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #2e3040;
}

.lang-tag {
  font-family: 'Geist Mono', monospace;
  font-size: 0.68rem;
  font-weight: 700;
  color: #8CA4FF;
  text-transform: uppercase;
}

.step-nav {
  display: flex;
  align-items: center;
  gap: 8px;
}

.step-counter {
  font-family: 'Geist Mono', monospace;
  font-size: 0.68rem;
  color: #a6adc8;
}

.step-btn {
  background: #2b2d42;
  color: #fff;
  border: 1px solid #3d405b;
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 0.65rem;
  cursor: pointer;
}

.step-btn:hover {
  background: #476BFF;
}

.stepcode-body {
  padding: 0.75rem 0.5rem;
  font-family: 'Geist Mono', monospace;
  font-size: 0.75rem;
  line-height: 1.6;
}

.code-line-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 2px 8px;
  border-radius: 6px;
  cursor: pointer;
  color: #a6adc8;
  transition: all 0.15s;
}

.code-line-item:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
}

.code-line-item.active {
  background: rgba(71, 107, 255, 0.22);
  color: #53DFA9;
  font-weight: 700;
  box-shadow: inset 3px 0 0 #476BFF;
}

.line-num {
  font-size: 0.68rem;
  color: #585b70;
  width: 20px;
  text-align: right;
  user-select: none;
}

.line-text {
  white-space: pre-wrap;
  word-break: break-all;
}
</style>
