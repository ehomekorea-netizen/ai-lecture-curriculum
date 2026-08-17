<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const props = defineProps<{
  stage?: number
}>()

const activeStep = ref(0)

// Sync with Slidev $clicks
watch(
  () => props.stage,
  (val) => {
    if (val === undefined || val === null || val <= 0) {
      activeStep.value = 0
    } else {
      activeStep.value = Math.min(3, Math.max(0, val))
    }
  },
  { immediate: true }
)

function selectStep(idx: number) {
  activeStep.value = idx
}

const steps = [
  {
    step: '01',
    name: '1. 상황 인식 (Sense)',
    shortName: '01. 상황 인식',
    metaphor: '👁️ 눈 (상태 스캔)',
    tag: '환경 & 목표 분석',
    themeColor: 'blue',
    btnActive: 'bg-blue-600 text-white shadow-md border-blue-600 scale-[1.02]',
    cardActive: 'bg-white border-2 border-blue-500 ring-4 ring-blue-500/20 shadow-2xl scale-[1.03] -translate-y-1',
    badgeClass: 'bg-blue-100 text-blue-700 border-blue-200',
    coreDesc: '사용자의 요청 프롬프트와 현재 폴더 구조, 터미널 로그, 브라우저 화면을 꼼꼼히 스캔합니다.',
    actions: [
      { icon: '🎯', title: '사용자 의도 분석', desc: '프롬프트의 핵심 목표와 제약 조건 파악' },
      { icon: '📂', title: '프로젝트 환경 스캔', desc: '현재 파일, 디렉터리, 라이브러리 상태 확인' },
      { icon: '🖥️', title: '실행 콘솔/화면 감지', desc: '이전 단계의 출력 결과 및 오류 감지' }
    ]
  },
  {
    step: '02',
    name: '2. 할 일 계획 (Plan)',
    shortName: '02. 할 일 계획',
    metaphor: '🧠 뇌 (작업 분할)',
    tag: '단계별 순서 수립',
    themeColor: 'amber',
    btnActive: 'bg-amber-500 text-white shadow-md border-amber-500 scale-[1.02]',
    cardActive: 'bg-white border-2 border-amber-500 ring-4 ring-amber-500/20 shadow-2xl scale-[1.03] -translate-y-1',
    badgeClass: 'bg-amber-100 text-amber-800 border-amber-200',
    coreDesc: '복잡한 전체 작업을 한 번에 하지 않고, 3~4개의 구체적 실행 단위로 쪼개어 로드맵을 짭니다.',
    actions: [
      { icon: '✂️', title: '작업 세분화 (Chunking)', desc: '1단계 뼈대 ➔ 2단계 스타일 ➔ 3단계 인터랙션' },
      { icon: '⏱️', title: '의존성 & 우선순위', desc: '파일 생성 전 필수 패키지 설치 순서 결정' },
      { icon: '🛠️', title: '필요 도구 선정', desc: '터미널, 파일 편집기, 웹 브라우저 툴 매핑' }
    ]
  },
  {
    step: '03',
    name: '3. 직접 실행 (Act)',
    shortName: '03. 직접 실행',
    metaphor: '🖐️ 손 (도구 사용)',
    tag: '코드 생성 & 터미널',
    themeColor: 'purple',
    btnActive: 'bg-purple-600 text-white shadow-md border-purple-600 scale-[1.02]',
    cardActive: 'bg-white border-2 border-purple-500 ring-4 ring-purple-500/20 shadow-2xl scale-[1.03] -translate-y-1',
    badgeClass: 'bg-purple-100 text-purple-700 border-purple-200',
    coreDesc: '단순 텍스트 제안에 그치지 않고, 직접 코드를 파일로 저장하고 명령어를 터미널에서 실행합니다.',
    actions: [
      { icon: '💻', title: '파일 자동 생성/수정', desc: 'HTML, CSS, Vue 파일 직접 작성 및 디스크 저장' },
      { icon: '⚡', title: '터미널 명령어 실행', desc: 'npm install, git commit, 빌드 명령어 직접 구동' },
      { icon: '🖱️', title: '브라우저 실제 조작', desc: '실제 웹 화면 띄워 버튼 클릭 및 동작 검증' }
    ]
  },
  {
    step: '04',
    name: '4. 자가 수정 (Feedback)',
    shortName: '04. 자가 수정',
    metaphor: '🔄 반성 (무한 루프)',
    tag: '에러 자체 치유',
    themeColor: 'emerald',
    btnActive: 'bg-emerald-600 text-white shadow-md border-emerald-600 scale-[1.02]',
    cardActive: 'bg-gradient-to-b from-emerald-50/50 to-white border-2 border-emerald-500 ring-4 ring-emerald-500/30 shadow-2xl scale-[1.03] -translate-y-1',
    badgeClass: 'bg-emerald-100 text-emerald-800 border-emerald-300 font-bold',
    coreDesc: '에러가 발생하면 사람에게 묻지 않고, 스스로 버그를 진단하고 수정하여 완제품이 될 때까지 반복합니다.',
    actions: [
      { icon: '🔍', title: '콘솔 에러 자동 포착', desc: '빌드 실패 로그 및 런타임 버그 즉시 감지' },
      { icon: '🔄', title: '자가 치유 (Self-Healing)', desc: '1단계(Sense)로 돌아가 수정 계획 재수립 후 재실행' },
      { icon: '🎉', title: '100% 완제품 납품', desc: '모든 테스트를 통과했을 때만 인간에게 최종 보고' }
    ]
  }
]
</script>

<template>
  <div class="agent-loop-wrapper mt-1">
    <!-- Top 4-Step Clickable Stepper Bar (No Emojis) -->
    <div class="flex items-center justify-between gap-1.5 p-1.5 bg-slate-100 rounded-xl border border-slate-200 mb-3">
      <button
        v-for="(s, idx) in steps"
        :key="s.step"
        class="flex-1 py-1.5 px-2 rounded-lg text-xs font-bold transition-all flex items-center justify-center cursor-pointer border truncate"
        :class="activeStep === idx ? s.btnActive : 'bg-transparent text-slate-500 border-transparent hover:text-slate-800 hover:bg-slate-200/60'"
        @click="selectStep(idx)"
      >
        <span>{{ s.shortName }}</span>
      </button>
    </div>

    <!-- 4 Step Cards Grid with Spotlight Focus -->
    <div class="grid grid-cols-4 gap-2.5 items-stretch">
      <div
        v-for="(s, idx) in steps"
        :key="s.step"
        class="step-card p-3 rounded-2xl border transition-all duration-300 flex flex-col justify-between cursor-pointer"
        :class="activeStep === idx ? `${s.cardActive} z-10` : 'bg-slate-50/80 border-slate-200 opacity-40 grayscale-[40%] scale-[0.97] hover:opacity-80'"
        @click="selectStep(idx)"
      >
        <div>
          <!-- Card Top Pill (No Emoji) -->
          <div class="flex items-center justify-between mb-1.5">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono border" :class="s.badgeClass">
              STEP {{ s.step }}
            </span>
          </div>

          <!-- Title -->
          <h3 class="text-sm font-bold text-slate-900 mb-0.5 leading-tight opacity-100">
            {{ s.name }}
          </h3>
          <p class="text-[10.5px] font-semibold mb-2" :class="activeStep === idx ? 'text-blue-600 font-bold' : 'text-slate-400'">
            {{ s.tag }}
          </p>

          <!-- Action Items -->
          <div class="space-y-1.5">
            <div
              v-for="(act, aIdx) in s.actions"
              :key="aIdx"
              class="p-1.5 rounded-lg bg-slate-50 border border-slate-100/80 text-[10.5px] text-slate-700 leading-snug"
            >
              <div class="font-bold text-slate-800 text-[10.5px] flex items-center gap-1">
                <span>{{ act.icon }}</span>
                <span>{{ act.title }}</span>
              </div>
              <div class="text-[10px] text-slate-500 mt-0.5 pl-3.5">
                {{ act.desc }}
              </div>
            </div>
          </div>
        </div>

        <!-- Footer Metaphor (인간 신체 비유는 유지) -->
        <div class="mt-2.5 pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px]">
          <span class="text-slate-400 font-medium">인간 신체 비유</span>
          <b class="text-slate-700 font-bold">{{ s.metaphor }}</b>
        </div>
      </div>
    </div>

    <!-- Dynamic Bottom Loop Banner -->
    <div class="mt-3 p-2.5 rounded-xl border bg-slate-900 text-white shadow-md flex items-center justify-between transition-all duration-300 border-slate-800">
      <div class="flex items-center gap-2">
        <span class="px-2 py-0.5 rounded text-[10.5px] font-bold font-mono bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 flex items-center gap-1">
          <span class="animate-spin text-xs">🔄</span>
          <span>자율 무한 순환</span>
        </span>
        <span class="text-xs text-slate-200">
          <b class="text-amber-300">{{ steps[activeStep].name }}</b>: {{ steps[activeStep].coreDesc }}
        </span>
      </div>
      <div class="flex-shrink-0 text-[10.5px] text-emerald-400 font-bold bg-white/10 px-2 py-0.5 rounded">
        오류 시 1단계로 회귀 ➔ 자동 완수
      </div>
    </div>
  </div>
</template>

<style scoped>
.step-card {
  min-height: 275px;
}
</style>
