<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

interface RowState {
  label: string
  tag: string
  examples: string[]
  displayText: string
  exampleIdx: number
  isDeleting: boolean
  initialDelay: number
  typeSpeed: number
  delSpeed: number
  pauseTime: number
}

const rows = ref<RowState[]>([
  {
    label: '내가 반복하는 업무',
    tag: 'Focus',
    examples: [
      '월간 프로그램 운영보고서 작성',
      '분기별 취약계층 안부확인 일지',
      '신규 후원자 예우 및 사업평가서'
    ],
    displayText: '',
    exampleIdx: 0,
    isDeleting: false,
    initialDelay: 0,
    typeSpeed: 65,
    delSpeed: 35,
    pauseTime: 1800
  },
  {
    label: '입력 자료',
    tag: 'Input',
    examples: [
      '출석부 및 만족도 설문(XLSX)',
      '상담 기록 일지 및 활동 사진',
      '현장 모니터링 체크리스트'
    ],
    displayText: '',
    exampleIdx: 0,
    isDeleting: false,
    initialDelay: 400,
    typeSpeed: 75,
    delSpeed: 40,
    pauseTime: 1600
  },
  {
    label: '항상 지킬 기준',
    tag: 'Rules',
    examples: [
      '5대 필수 목차 및 기관 표준 양식',
      '원자료 수치 100% 무결성 유지',
      '공문서 규정 준수 및 중립적 문체'
    ],
    displayText: '',
    exampleIdx: 0,
    isDeleting: false,
    initialDelay: 850,
    typeSpeed: 55,
    delSpeed: 30,
    pauseTime: 2000
  },
  {
    label: '원하는 결과 형식',
    tag: 'Output',
    examples: [
      '표준 서식 적용 완성형 DOCX',
      '보고용 핵심 요약 PPTX 슬라이드',
      '공식 결재용 한글/PDF 공문 초안'
    ],
    displayText: '',
    exampleIdx: 0,
    isDeleting: false,
    initialDelay: 250,
    typeSpeed: 70,
    delSpeed: 35,
    pauseTime: 1700
  }
])

const timeouts: any[] = []

function runTypewriterForRow(idx: number) {
  const row = rows.value[idx]
  if (!row) return

  const currentFull = row.examples[row.exampleIdx]

  if (!row.isDeleting) {
    // Typing forward
    if (row.displayText.length < currentFull.length) {
      row.displayText = currentFull.slice(0, row.displayText.length + 1)
      const t = setTimeout(() => runTypewriterForRow(idx), row.typeSpeed + Math.random() * 20)
      timeouts.push(t)
    } else {
      // Completed typing full string -> Pause before deleting
      const t = setTimeout(() => {
        row.isDeleting = true
        runTypewriterForRow(idx)
      }, row.pauseTime)
      timeouts.push(t)
    }
  } else {
    // Backspacing / Deleting
    if (row.displayText.length > 0) {
      row.displayText = currentFull.slice(0, row.displayText.length - 1)
      const t = setTimeout(() => runTypewriterForRow(idx), row.delSpeed)
      timeouts.push(t)
    } else {
      // Completed deleting -> Switch to next example
      row.isDeleting = false
      row.exampleIdx = (row.exampleIdx + 1) % row.examples.length
      const t = setTimeout(() => runTypewriterForRow(idx), 300)
      timeouts.push(t)
    }
  }
}

onMounted(() => {
  rows.value.forEach((row, idx) => {
    const t = setTimeout(() => {
      runTypewriterForRow(idx)
    }, row.initialDelay)
    timeouts.push(t)
  })
})

onUnmounted(() => {
  timeouts.forEach(t => clearTimeout(t))
})
</script>

<template>
  <div class="w-full flex flex-col justify-between items-center select-none font-sans text-slate-800 text-center h-[335px] my-auto py-0.5">
    <!-- ── Center Stage: Grand Keynote Scale 4-Row Fill-in Card ── -->
    <div class="w-full max-w-4xl bg-white rounded-3xl border border-slate-200/90 p-5 px-8 shadow-sm flex flex-col justify-between h-[270px] text-left">
      <div class="space-y-2.5 my-auto">
        <div
          v-for="(item, idx) in rows"
          :key="item.label"
          class="flex items-center justify-between py-2 px-4 rounded-2xl bg-slate-50/70 border border-slate-200/60 transition-all hover:bg-blue-50/60 hover:border-blue-200/80 shadow-2xs"
        >
          <!-- Left Label + Number Badge (Large Scale) -->
          <div class="flex items-center gap-3 min-w-[175px] shrink-0">
            <span class="w-7 h-7 rounded-xl font-mono font-bold text-xs flex items-center justify-center bg-blue-50 text-blue-600 border border-blue-200 shadow-2xs">
              0{{ idx + 1 }}
            </span>
            <span class="text-base md:text-lg font-bold font-serif text-slate-900 tracking-tight">
              {{ item.label }}
            </span>
            <span class="text-slate-400 font-mono text-sm">:</span>
          </div>

          <!-- Blank Underline & Live Asynchronous Typewriter (Large Scale) -->
          <div class="flex-1 border-b-2 border-dashed border-slate-300 ml-4 pb-1 flex items-center justify-between overflow-hidden">
            <div class="flex items-center">
              <span class="text-sm md:text-base font-bold text-blue-600 tracking-tight whitespace-nowrap">
                {{ item.displayText }}
              </span>
              <span class="cursor-blink text-blue-500 font-mono font-bold text-sm ml-0.5 leading-none">
                _
              </span>
            </div>
            <span class="text-[10.5px] font-mono font-bold text-slate-400 uppercase tracking-wider shrink-0 pl-3 bg-white/80 px-2 py-0.5 rounded-md border border-slate-100 shadow-2xs">
              {{ item.tag }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- ── Bottom Inspiration Bar (Large Scale) ── -->
    <div class="w-full max-w-2xl pt-2.5 pb-0.5 border-t border-slate-200/90 flex items-center justify-center">
      <p class="text-sm md:text-base font-serif font-bold text-blue-600 tracking-wide">
        반복되는 나의 업무를, 다시 쓸 수 있는 방식으로 바꿔보세요.
      </p>
    </div>
  </div>
</template>

<style scoped>
/* ── Infinite Cursor Blink ── */
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.cursor-blink {
  animation: blink 0.75s infinite;
}
</style>
