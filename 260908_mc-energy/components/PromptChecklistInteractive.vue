<script setup lang="ts">
import { ref, computed } from 'vue'

interface ChecklistItem {
  id: number
  key: string
  title: string
  sub: string
  tag: string
  activeBorder: string
  activeBg: string
  activeText: string
  activeTag: string
}

const items: ChecklistItem[] = [
  {
    id: 0,
    key: '1. Role',
    title: '누가 하는 일인가?',
    sub: '담당자 역할과 관점을 명시했는가?',
    tag: '고객 지원 담당자',
    activeBorder: 'border-blue-500/50',
    activeBg: 'bg-blue-950/30',
    activeText: 'text-blue-400',
    activeTag: 'text-blue-300 bg-blue-500/15 border-blue-500/30'
  },
  {
    id: 1,
    key: '2. Context',
    title: '어떤 상황인가?',
    sub: '사내 규정과 마스킹된 배경 정보를 넣었는가?',
    tag: '규정 및 마스킹 데이터',
    activeBorder: 'border-cyan-500/50',
    activeBg: 'bg-cyan-950/30',
    activeText: 'text-cyan-300',
    activeTag: 'text-cyan-300 bg-cyan-500/15 border-cyan-500/30'
  },
  {
    id: 2,
    key: '3. Task',
    title: '무엇을 해야 하는가?',
    sub: '구체적인 작업 지시를 명시했는가?',
    tag: '단계별 안내문 작성',
    activeBorder: 'border-sky-500/50',
    activeBg: 'bg-sky-950/30',
    activeText: 'text-sky-400',
    activeTag: 'text-sky-300 bg-sky-500/15 border-sky-500/30'
  },
  {
    id: 3,
    key: '4. Format',
    title: '어떤 형태로 받는가?',
    sub: '원하는 표 구조와 예시 1행을 주었는가?',
    tag: '표 헤더 및 Few-shot',
    activeBorder: 'border-indigo-500/50',
    activeBg: 'bg-indigo-950/30',
    activeText: 'text-indigo-300',
    activeTag: 'text-indigo-300 bg-indigo-500/15 border-indigo-500/30'
  },
  {
    id: 4,
    key: '5. Constraint',
    title: '모르는 것은 어떻게?',
    sub: '불확실 정보에 대한 예외 처리 기준을 넣었는가?',
    tag: "'확인 필요' 표기",
    activeBorder: 'border-amber-500/50',
    activeBg: 'bg-amber-950/30',
    activeText: 'text-amber-400',
    activeTag: 'text-amber-300 bg-amber-500/15 border-amber-500/30'
  }
]

const checkedList = ref<boolean[]>([false, false, false, false, false])

const toggleItem = (index: number) => {
  checkedList.value[index] = !checkedList.value[index]
}

const checkedCount = computed(() => checkedList.value.filter(Boolean).length)
const allChecked = computed(() => checkedCount.value === 5)

const resetAll = () => {
  checkedList.value = [false, false, false, false, false]
}

const selectAll = () => {
  checkedList.value = [true, true, true, true, true]
}
</script>

<template>
  <div class="flex flex-col gap-4 w-full select-none">
    <!-- Top Minimal Control Bar -->
    <div class="flex items-center justify-between px-1">
      <div class="flex items-center gap-2 text-xs font-mono text-white/60">
        <span>점검 진행률:</span>
        <span class="font-bold" :class="allChecked ? 'text-emerald-400' : 'text-cyan-300'">
          {{ checkedCount }} / 5
        </span>
      </div>
      <div class="flex items-center gap-2">
        <button
          @click="resetAll"
          class="text-[11px] font-mono px-2 py-0.5 rounded bg-white/5 border border-white/10 text-white/50 hover:text-white transition-colors"
        >
          초기화
        </button>
        <button
          @click="selectAll"
          class="text-[11px] font-mono px-2 py-0.5 rounded bg-white/10 border border-white/15 text-white/80 hover:text-white transition-colors"
        >
          전체 선택
        </button>
      </div>
    </div>

    <!-- 5 Checklist Cards -->
    <div class="grid grid-cols-5 gap-3.5">
      <div
        v-for="(item, index) in items"
        :key="item.id"
        @click="toggleItem(index)"
        class="rounded-xl p-4 flex flex-col justify-between h-48 cursor-pointer transition-all duration-200"
        :class="[
          checkedList[index]
            ? [item.activeBg, item.activeBorder, 'border opacity-100 shadow-md']
            : 'bg-black/50 border border-white/10 opacity-40 hover:opacity-75'
        ]"
      >
        <div>
          <!-- Header (Key + Checkbox) -->
          <div class="flex items-center justify-between mb-2">
            <span
              class="text-xs font-mono font-bold"
              :class="checkedList[index] ? item.activeText : 'text-white/40'"
            >
              {{ item.key }}
            </span>
            <span
              class="text-base"
              :class="[
                checkedList[index]
                  ? ['i-carbon:checkbox-checked', item.activeText]
                  : 'i-carbon:checkbox text-white/30'
              ]"
            ></span>
          </div>

          <!-- Title -->
          <div
            class="text-xs font-bold mb-1.5"
            :class="checkedList[index] ? 'text-white/95' : 'text-white/60'"
          >
            {{ item.title }}
          </div>

          <!-- Subtext -->
          <p
            class="text-[11px] m-0 leading-relaxed"
            :class="checkedList[index] ? 'text-white/80' : 'text-white/40'"
          >
            {{ item.sub }}
          </p>
        </div>

        <!-- Bottom Tag -->
        <div class="pt-2.5 border-t" :class="checkedList[index] ? 'border-white/10' : 'border-white/5'">
          <span
            class="text-[10px] font-mono px-2 py-0.5 rounded border inline-block"
            :class="[
              checkedList[index]
                ? item.activeTag
                : 'text-white/40 bg-white/5 border-white/5'
            ]"
          >
            {{ item.tag }}
          </span>
        </div>
      </div>
    </div>

    <!-- Bottom Status Area (Clean and Minimal) -->
    <div class="mt-1">
      <div
        v-if="allChecked"
        class="p-3.5 rounded-xl border border-emerald-500/40 bg-emerald-950/25 flex items-center justify-between text-xs text-white/90 transition-all duration-300"
      >
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          <span><strong>5개 점검 완료:</strong> 역할(R) · 맥락(C) · 작업(T) · 형식(F) · 제약조건이 충족되었습니다. 실습을 시작합니다.</span>
        </div>
        <span class="font-mono text-[11px] font-bold text-emerald-300">19번 실습으로 진행</span>
      </div>

      <div
        v-else
        class="p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/60"
      >
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-white/30"></span>
          <span>카드를 클릭하여 5가지 실무 점검 항목을 확인하세요.</span>
        </div>
        <span class="font-mono text-[11px] text-white/40">{{ checkedCount }} / 5 항목 확인</span>
      </div>
    </div>
  </div>
</template>
