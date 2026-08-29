<script setup lang="ts">
import { computed } from 'vue'

export interface TableRow {
  category: string
  left: string
  right: string
  markType?: 'underline' | 'circle' | 'highlight' | 'box'
  markColor?: 'amber' | 'rose' | 'indigo' | 'emerald' | 'blue' | 'purple'
}

const props = withDefaults(
  defineProps<{
    headers: string[]
    rows: TableRow[]
    stage?: number
    widths?: [string, string, string]
    footerQuote?: string
  }>(),
  {
    stage: 0,
    widths: () => ['20%', '40%', '40%'],
    footerQuote: ''
  }
)

const currentStage = computed(() => props.stage ?? 0)

function getMarkClasses(type?: string) {
  switch (type) {
    case 'highlight': return 'bg-amber-500/25 text-amber-200 border border-amber-400/50 font-bold px-2 py-0.5 rounded shadow-sm'
    case 'circle': return 'bg-rose-500/25 text-rose-200 border border-rose-400/60 font-bold rounded-full px-2.5 py-0.5 shadow-sm'
    case 'box': return 'bg-indigo-500/25 text-indigo-200 border border-indigo-400/60 font-bold rounded-md px-2.5 py-0.5 shadow-sm'
    case 'underline': return 'bg-emerald-500/25 text-emerald-200 border-b-2 border-emerald-400 font-bold px-2 py-0.5 rounded-sm shadow-sm'
    default:
      return 'text-blue-200 font-bold'
  }
}
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-100">
    <table class="w-full border-collapse bg-white/6 rounded-xl overflow-hidden border border-white/10 shadow-xs text-[13px] table-fixed">
      <thead>
        <tr class="bg-white/8 text-white font-bold border-b border-white/10 h-[38px]">
          <th :style="{ width: widths[0] }" class="p-2.5 px-3.5 text-left font-bold text-slate-100">
            {{ headers[0] }}
          </th>
          <th :style="{ width: widths[1] }" class="p-2.5 px-3.5 text-left font-bold text-slate-300">
            {{ headers[1] }}
          </th>
          <th :style="{ width: widths[2] }" class="p-2.5 px-3.5 text-left font-bold text-blue-200 bg-blue-950/40 border-l border-white/10">
            {{ headers[2] }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, idx) in rows"
          :key="idx"
          class="border-b border-white/10 transition-colors duration-300 h-[44px]"
          :class="currentStage > idx ? 'bg-blue-950/40' : idx % 2 === 1 ? 'bg-white/6' : 'bg-white/6'"
        >
          <!-- Category Column -->
          <td class="p-2 px-3.5 font-bold text-white align-middle">
            {{ row.category }}
          </td>

          <!-- Left Column (Standard) -->
          <td class="p-2 px-3.5 text-slate-400 font-normal align-middle leading-snug">
            {{ row.left }}
          </td>

          <!-- Right Column (Zero-CLS Animated Annotations on Clicks) -->
          <td class="p-2 px-3.5 font-medium border-l border-white/10 align-middle leading-snug">
            <div class="inline-flex items-center min-h-[26px]">
              <span
                class="transition-all duration-300 inline-block"
                :class="[
                  currentStage > idx
                    ? getMarkClasses(row.markType)
                    : 'text-slate-100 font-medium px-1 py-0.5'
                ]"
              >
                {{ row.right }}
              </span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Footer Quote Box -->
    <div v-if="footerQuote" class="slide-footer quote-box text-xs mt-2 font-medium">
      <span v-html="footerQuote"></span>
    </div>
  </div>
</template>

<style scoped>
table {
  table-layout: fixed;
}
table td, table th {
  vertical-align: middle;
  box-sizing: border-box;
}
</style>
