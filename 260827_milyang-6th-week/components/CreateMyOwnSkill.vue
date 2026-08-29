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
    label: '내가 반복하는 취업 준비',
    tag: 'Focus',
    examples: [
      '프로젝트 경험을 STAR 포트폴리오로 정리',
      '기업별 채용공고 맞춤 자기소개서 초안',
      '면접 대비 1분 자기소개 및 예상질문'
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
      '내 프로젝트 활동 기록 및 노션 DB(MD)',
      '깃허브 커밋 기록 및 문제해결 메모',
      '목표 기업 채용공고 및 인재상(PDF)'
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
      'STAR(상황-과제-행동-성과) 구조화 준수',
      '내 경험 데이터 100% 진실성 유지',
      '면접관의 눈높이에 맞는 비즈니스 문체'
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
      '제출용 완성형 포트폴리오 DOCX',
      '면접 발표용 5슬라이드 피치덱 PPTX',
      '노션/이력서 이식용 마크다운 산출물'
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
    <!-- ── Center Stage: Grand Keynote Scale 4-Row Fill-in Card (Fixed Zero-Shift Grid) ── -->
    <div class="w-full max-w-4xl bg-white rounded-3xl border border-slate-200/90 p-5 px-8 shadow-sm flex flex-col justify-between h-[270px] text-left">
      <div class="space-y-2.5 my-auto">
        <div
          v-for="(item, idx) in rows"
          :key="item.label"
          class="flex items-center justify-between h-[46px] px-4 rounded-2xl bg-slate-50/70 border border-slate-200/60 transition-colors duration-200 hover:bg-blue-50/60 hover:border-blue-200/80 shadow-2xs relative"
        >
          <!-- 1. Left Label + Number Badge (Fixed Width: 205px, Zero Layout Shift) -->
          <div class="flex items-center gap-2.5 w-[205px] shrink-0">
            <span class="w-7 h-7 rounded-xl font-mono font-bold text-xs flex items-center justify-center bg-blue-50 text-blue-600 border border-blue-200 shadow-2xs shrink-0">
              0{{ idx + 1 }}
            </span>
            <span class="text-[15px] font-bold font-serif text-slate-900 tracking-tight whitespace-nowrap">
              {{ item.label }}
            </span>
            <span class="text-slate-400 font-mono text-sm ml-auto pr-1">:</span>
          </div>

          <!-- 2. Center: Fixed-Height Typewriter Track with Stable Dashed Line (Zero Reflow) -->
          <div class="relative flex-1 h-full flex items-center mx-3 overflow-hidden">
            <!-- Absolute Fixed Dashed Underline -->
            <div class="absolute bottom-2 inset-x-0 border-b-2 border-dashed border-slate-300 pointer-events-none"></div>

            <!-- Typing Text with Infinite Blinking Cursor -->
            <div class="relative z-10 flex items-center h-full max-w-full pb-1 overflow-hidden">
              <span class="text-[14.5px] font-bold text-blue-600 tracking-tight whitespace-nowrap overflow-hidden text-ellipsis">
                {{ item.displayText }}
              </span>
              <span class="cursor-blink text-blue-500 font-mono font-bold text-sm ml-0.5 leading-none shrink-0">
                _
              </span>
            </div>
          </div>

          <!-- 3. Right Fixed Tag (Fixed Width: 64px, Zero Shift) -->
          <div class="w-[64px] shrink-0 flex justify-end">
            <span class="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider bg-white/90 px-2 py-0.5 rounded-md border border-slate-200/80 shadow-2xs text-center w-full block">
              {{ item.tag }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- ── Bottom Inspiration Bar (Large Scale) ── -->
    <div class="w-full max-w-2xl pt-2.5 pb-0.5 border-t border-slate-200/90 flex items-center justify-center">
      <p class="text-sm md:text-base font-serif font-bold text-blue-600 tracking-wide">
        취업을 위한 나의 경험 정리를, 평생 쓰는 강력한 직무 자산으로 바꿔보세요.
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
