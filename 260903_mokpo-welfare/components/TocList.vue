<script setup lang="ts">
const items = [
  {
    num: '01',
    title: '생성형 AI와 에이전트의 본질',
    en: 'Principles & Agent'
  },
  {
    num: '02',
    title: '실무 프롬프트 엔지니어링 표준',
    en: 'Prompt Engineering'
  },
  {
    num: '03',
    title: 'ChatGPT Work 도구 및 5대 검토 체계',
    en: 'Work Tools & Review'
  },
  {
    num: '04',
    title: '나만의 스킬 구축과 업무 자산화',
    en: 'Skill & Assetization'
  }
]
</script>

<template>
  <div style="display:flex;flex-direction:column;justify-content:center;width:100%;max-width:780px;margin:0 auto;gap:0;padding-bottom:1.6rem;">
    <div
      v-for="item in items"
      :key="item.num"
      style="display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1.5px solid #e2e8f0;"
    >
      <!-- Number + Title -->
      <div style="display:flex;align-items:center;gap:28px;">
        <span style="font-family:'Geist Mono',monospace;font-size:2rem;font-weight:700;color:#2563eb;line-height:1;min-width:52px;">
          {{ item.num }}
        </span>
        <span style="font-family:'Source Serif 4',Georgia,serif;font-size:1.5rem;font-weight:700;color:#0f172a;line-height:1.2;">
          {{ item.title }}
        </span>
      </div>
      <!-- English Tag -->
      <span style="font-family:'Geist Mono',monospace;font-size:0.7rem;font-weight:600;color:#94a3b8;letter-spacing:0.1em;text-transform:uppercase;white-space:nowrap;padding-left:16px;">
        {{ item.en }}
      </span>
    </div>
  </div>
</template>
