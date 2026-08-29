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
    case 'highlight':
      return 'bg-amber-300/50 text-slate-950 font-bold px-1.5 py-0.5 rounded-sm shadow-2xs'
    case 'circle':
      return 'outline-2 outline-rose-500 text-rose-950 font-bold bg-rose-50/70 shadow-2xs rounded-full px-2.5 py-0.5 outline-offset-2'
    case 'box':
      return 'outline-2 outline-indigo-500 text-indigo-950 font-bold bg-indigo-50/80 shadow-2xs rounded-md px-2 py-0.5 outline-offset-2'
    case 'underline':
      return 'underline decoration-wavy decoration-emerald-500 decoration-2 underline-offset-4 text-emerald-950 font-bold bg-emerald-50/50 px-1 py-0.5 rounded-xs'
    default:
      return 'text-blue-900 font-bold'
  }
}
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800">
    <table class="w-full border-collapse bg-white rounded-xl overflow-hidden border border-slate-200 shadow-xs text-[13px] table-fixed">
      <thead>
        <tr class="bg-[#FFEAD7] text-slate-900 font-bold border-b border-slate-200 h-[38px]">
          <th :style="{ width: widths[0] }" class="p-2.5 px-3.5 text-left font-bold text-slate-800">
            {{ headers[0] }}
          </th>
          <th :style="{ width: widths[1] }" class="p-2.5 px-3.5 text-left font-bold text-slate-700">
            {{ headers[1] }}
          </th>
          <th :style="{ width: widths[2] }" class="p-2.5 px-3.5 text-left font-bold text-blue-900 bg-blue-50/60 border-l border-slate-200/80">
            {{ headers[2] }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, idx) in rows"
          :key="idx"
          class="border-b border-slate-200/80 transition-colors duration-300 h-[44px]"
          :class="currentStage > idx ? 'bg-blue-50/20' : idx % 2 === 1 ? 'bg-slate-50/40' : 'bg-white'"
        >
          <!-- Category Column -->
          <td class="p-2 px-3.5 font-bold text-slate-900 align-middle">
            {{ row.category }}
          </td>

          <!-- Left Column (Standard) -->
          <td class="p-2 px-3.5 text-slate-600 font-normal align-middle leading-snug">
            {{ row.left }}
          </td>

          <!-- Right Column (Zero-CLS Animated Annotations on Clicks) -->
          <td class="p-2 px-3.5 font-medium border-l border-slate-200/70 align-middle leading-snug">
            <div class="inline-flex items-center min-h-[26px]">
              <span
                class="transition-all duration-300 inline-block"
                :class="[
                  currentStage > idx
                    ? getMarkClasses(row.markType)
                    : 'text-slate-800 font-medium px-1 py-0.5'
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
