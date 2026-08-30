<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  title?: string
  badPrompt?: string
  role?: string
  goal?: string
  context?: string
  inputData?: string
  condition?: string
  outputFormat?: string
  validation?: string
}>()

const activeTab = ref<'good' | 'bad'>('good')
const copied = ref(false)

const getFullGoodPrompt = () => {
  return `[역할] ${props.role || '수산양식 관리 전문 비서'}
[목표] ${props.goal || '보고서 초안 작성'}
[배경] ${props.context || '해상가두리 양식 현장 정기 점검'}
[입력] ${props.inputData || '원문 데이터 첨부'}
[조건] ${props.condition || '추정 금지, 미확인 항목 별도 표기'}
[출력] ${props.outputFormat || '표 및 핵심 행동 목록'}
[검증] ${props.validation || '수치 누락 및 사실관계 교차 점검'}`
}

const copyPrompt = () => {
  navigator.clipboard.writeText(getFullGoodPrompt())
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<template>
  <div class="glass-card flex flex-col gap-2.5 my-2 p-4 text-xs">
    <div class="flex items-center justify-between border-b border-white/10 pb-2">
      <div class="flex items-center gap-2 font-bold text-white text-sm">
        <span class="i-carbon-chat-bot text-emerald-400 text-base"></span>
        <span>{{ title || '실무 프롬프트 7단계 공식 쇼케이스' }}</span>
      </div>
      <div class="flex items-center gap-2">
        <button
          class="px-2.5 py-1 rounded text-xs transition-colors"
          :class="activeTab === 'bad' ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activeTab = 'bad'"
        >
          ❌ 아쉬운 요청
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs transition-colors"
          :class="activeTab === 'good' ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activeTab = 'good'"
        >
          ✨ 실무 7단계 지시
        </button>
        <button
          v-if="activeTab === 'good'"
          class="px-2.5 py-1 rounded text-xs bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 transition-all"
          @click="copyPrompt"
        >
          <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
          <span>{{ copied ? '복사됨!' : '프롬프트 복사' }}</span>
        </button>
      </div>
    </div>

    <!-- Bad Prompt Tab -->
    <div v-if="activeTab === 'bad'" class="p-3 bg-rose-950/30 border border-rose-500/20 rounded-lg">
      <div class="text-xs text-rose-400 font-bold mb-1">검색창처럼 쓴 한 줄 프롬프트</div>
      <div class="text-white/90 text-xs font-mono bg-black/40 p-2.5 rounded border border-rose-500/10">
        "{{ badPrompt || '가두리 일지 정리해줘.' }}"
      </div>
      <div class="mt-2 text-[11px] text-white/60 flex items-center gap-1.5">
        <span class="i-carbon-warning-filled text-rose-400"></span>
        <span>문제점: AI가 맥락과 목적을 몰라 일반적이고 두루뭉술한 답변을 내놓게 됩니다.</span>
      </div>
    </div>

    <!-- Good Prompt Tab (7 Structure) -->
    <div v-else class="grid grid-cols-2 gap-2 text-[11px]">
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-emerald-400 font-bold">1. 역할 (Role)</span>
        <p class="text-white/80 mt-0.5">{{ role || '수산양식 현장 관리 및 행정 비서' }}</p>
      </div>
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-emerald-400 font-bold">2. 목표 (Goal)</span>
        <p class="text-white/80 mt-0.5">{{ goal || '핵심 점검사항, 수온 이상, 후속조치 추출' }}</p>
      </div>
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-emerald-400 font-bold">3. 배경/맥락 (Context)</span>
        <p class="text-white/80 mt-0.5">{{ context || '고수온 특보 대비 해상가두리 8개 동 일일 점검' }}</p>
      </div>
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-emerald-400 font-bold">4. 입력자료 (Input)</span>
        <p class="text-white/80 mt-0.5">{{ inputData || '가두리 수온/DO 로그 및 현장 메모 전문' }}</p>
      </div>
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-sky-400 font-bold">5. 조건/제약 (Condition)</span>
        <p class="text-white/80 mt-0.5">{{ condition || '확인되지 않은 내용은 추정 금지, [미확인] 명시' }}</p>
      </div>
      <div class="p-2 bg-white/5 rounded border border-white/10">
        <span class="text-sky-400 font-bold">6. 출력형식 (Output)</span>
        <p class="text-white/80 mt-0.5">{{ outputFormat || '주의 가두리 최상단 요약 + 마크다운 표' }}</p>
      </div>
      <div class="col-span-2 p-2 bg-amber-500/10 rounded border border-amber-500/20">
        <span class="text-amber-300 font-bold">7. 검증기준 (Validation)</span>
        <span class="text-white/90 ml-2">{{ validation || '수치/단위 오류 확인, 수과원 기준 대조' }}</span>
      </div>
    </div>
  </div>
</template>
