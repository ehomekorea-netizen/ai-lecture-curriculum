<script setup lang="ts">
defineProps<{
  title?: string
  beforeTitle?: string
  beforeSteps: string[]
  beforeTime?: string
  afterTitle?: string
  afterSteps: string[]
  afterTime?: string
}>()
</script>

<template>
  <div class="my-2 text-xs">
    <div v-if="title" class="text-center font-bold text-sm text-white mb-2">
      {{ title }}
    </div>
    <div class="grid grid-cols-2 gap-3">
      <!-- Before (Traditional Workflow) -->
      <div class="glass-card border-rose-500/20 bg-rose-950/15 p-3.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between border-b border-rose-500/20 pb-1.5 mb-2.5">
            <div class="flex items-center gap-1.5 text-rose-300 font-bold">
              <span class="i-carbon-time text-sm"></span>
              <span>{{ beforeTitle || '기존 수작업 방식' }}</span>
            </div>
            <span v-if="beforeTime" class="text-[10px] px-2 py-0.5 rounded bg-rose-500/20 text-rose-200 font-mono">
              {{ beforeTime }}
            </span>
          </div>
          <ol class="space-y-1.5 text-[11px] text-white/80">
            <li
              v-for="(step, idx) in beforeSteps"
              :key="idx"
              class="flex items-start gap-1.5"
            >
              <span class="flex-shrink-0 w-3.5 h-3.5 rounded-full bg-rose-500/20 text-rose-300 flex items-center justify-center text-[9px] font-bold mt-0.5">
                {{ idx + 1 }}
              </span>
              <span class="leading-relaxed">{{ step }}</span>
            </li>
          </ol>
        </div>
        <div class="mt-2.5 pt-1.5 border-t border-rose-500/10 text-[10px] text-rose-300/80 flex items-center gap-1">
          <span class="i-carbon-close-filled text-rose-400 flex-shrink-0"></span>
          <span>단순 반복 타이핑으로 인한 피로 및 오탈자/누락 위험</span>
        </div>
      </div>

      <!-- After (AI Partner Workflow) -->
      <div class="glass-card border-emerald-500/30 bg-emerald-950/20 p-3.5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between border-b border-emerald-500/20 pb-1.5 mb-2.5">
            <div class="flex items-center gap-1.5 text-emerald-300 font-bold">
              <span class="i-carbon-flash text-sm"></span>
              <span>{{ afterTitle || 'AI 파트너 협업 방식' }}</span>
            </div>
            <span v-if="afterTime" class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-200 font-mono font-bold">
              {{ afterTime }}
            </span>
          </div>
          <ol class="space-y-1.5 text-[11px] text-white/90">
            <li
              v-for="(step, idx) in afterSteps"
              :key="idx"
              class="flex items-start gap-1.5"
            >
              <span class="flex-shrink-0 w-3.5 h-3.5 rounded-full bg-emerald-500/30 text-emerald-300 flex items-center justify-center text-[9px] font-bold mt-0.5">
                {{ idx + 1 }}
              </span>
              <span class="leading-relaxed">{{ step }}</span>
            </li>
          </ol>
        </div>
        <div class="mt-2.5 pt-1.5 border-t border-emerald-500/20 text-[10px] text-emerald-300 flex items-center gap-1 font-medium">
          <span class="i-carbon-checkmark-filled text-emerald-400 flex-shrink-0"></span>
          <span>사람은 [목표 지시]와 [현장 실측 검증]에만 집중</span>
        </div>
      </div>
    </div>
  </div>
</template>
