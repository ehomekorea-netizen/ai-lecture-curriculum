<script setup lang="ts">
import { ref } from 'vue'

interface Shot {
  id: string
  time: string
  role: string
  badgeColor: string
  subject: string
  action: string
  camera: string
  narration: string
  caption: string
  factCaution: string
}

const shots: Shot[] = [
  {
    id: 'S01',
    time: '0~3초',
    role: '시각적 훅 (낯선 질문)',
    badgeColor: 'text-sky-400 bg-sky-950/80 border-sky-400/50',
    subject: '실내 순환여과 양식 수조 + 수질 센서 하우징',
    action: '수조 가장자리에서 센서와 물고기를 향해 천천히 접근',
    camera: 'Medium-Wide Shot, Slow Push-in (안정적 전진 1회)',
    narration: '양식장인데, 물을 계속 바꾸지 않는다고요?',
    caption: '“양식장인데 물을 안 바꾼다?”',
    factCaution: '물고기보다 센서가 먼저 시선을 끌도록 배치'
  },
  {
    id: 'S02',
    time: '3~7초',
    role: '예상 깨기 (오해 ➔ 전환)',
    badgeColor: 'text-indigo-400 bg-indigo-950/80 border-indigo-400/50',
    subject: '투명한 여과 배관과 일정하게 흐르는 정화수',
    action: '수조의 물이 배관을 거쳐 물리적 여과부로 들어가는 흐름',
    camera: 'Lateral Tracking (수평 이동) 또는 Follow Shot',
    narration: '스마트 양식의 핵심은 물을 무작정 버리는 게 아닙니다.',
    caption: '“핵심은 버리는 양이 아닙니다”',
    factCaution: '배관의 시작점과 끝점이 물리적으로 이어져야 함'
  },
  {
    id: 'S03',
    time: '7~12초',
    role: '시스템 작동 (RAS 원리)',
    badgeColor: 'text-amber-400 bg-amber-950/80 border-amber-400/50',
    subject: '기계식 드럼필터 + 생물학적 여과조 + 산소 공급 배관',
    action: '각 정화 장치가 유기적으로 연결되어 돌아가는 시스템 전경',
    camera: 'Stable Medium Shot (흔들림 없는 고정 또는 팬)',
    narration: '기계·생물학적 여과와 산소 관리, 센서 데이터가 함께 물을 살립니다.',
    caption: '“여과 + 산소 + 데이터의 협업”',
    factCaution: '특정 상업 브랜드를 노출하지 않고 원리 중심 묘사'
  },
  {
    id: 'S04',
    time: '12~17초',
    role: '전문인력의 역할 (판단)',
    badgeColor: 'text-emerald-400 bg-emerald-950/80 border-emerald-400/50',
    subject: '스마트폰/태블릿 대시보드를 든 관리자와 실제 수조',
    action: '화면의 DO/수온 수치를 확인한 후 실제 수면을 관찰',
    camera: 'Over-the-Shoulder, Gentle Rack Focus',
    narration: '그리고 숫자와 현장을 함께 판단하는 사람이 있습니다.',
    caption: '“숫자와 현장을 함께 읽는 사람”',
    factCaution: '생성 모델의 글자 깨짐 방지: 화면 글자는 후편집 처리'
  },
  {
    id: 'S05',
    time: '17~20초',
    role: '결론 및 CTA (초대)',
    badgeColor: 'text-purple-400 bg-purple-950/80 border-purple-400/50',
    subject: '밝고 쾌적한 양식장 전경과 전문가의 당당한 뒷모습',
    action: '카메라가 서서히 뒤로 빠지며 전체 시설과 타이틀 영역 확보',
    camera: 'Slow Pull-Back 또는 Static Wide',
    narration: '스마트 수산업의 전문성은 물의 변화에서 시작됩니다.',
    caption: '스마트 수산업 전문인력 양성과정',
    factCaution: '기관명, 접수 기간, 링크는 후편집 자막으로 명확히 삽입'
  }
]

const selectedId = ref<string>('S01')
const selectedShot = computed(() => shots.find(s => s.id === selectedId.value) || shots[0])
</script>

<script lang="ts">
import { computed } from 'vue'
</script>

<template>
  <div class="glass-card p-4 my-2 text-xs flex flex-col gap-3">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2.5">
      <div class="flex items-center gap-2">
        <span class="i-carbon-movie text-amber-400 text-base"></span>
        <span class="font-bold text-white text-sm">스마트수산업 15~20초 숏폼 5-쇼트 마스터 스토리보드</span>
      </div>
      <span class="text-[11px] font-mono text-white/60">
        프로젝트: "물고기보다 물을 먼저 읽는 사람"
      </span>
    </div>

    <!-- 5 Shot Stepper Tabs -->
    <div class="grid grid-cols-5 gap-2">
      <button
        v-for="shot in shots"
        :key="shot.id"
        class="p-2 rounded-xl text-left border transition-all flex flex-col justify-between gap-1"
        :class="selectedId === shot.id ? 'bg-white/15 border-white/40 shadow-lg' : 'bg-black/30 border-white/5 hover:border-white/20 opacity-70 hover:opacity-100'"
        @click="selectedId = shot.id"
      >
        <div class="flex items-center justify-between">
          <span class="font-mono font-bold text-xs" :class="selectedId === shot.id ? 'text-white' : 'text-white/60'">
            {{ shot.id }}
          </span>
          <span class="text-[10px] font-mono text-white/50">{{ shot.time }}</span>
        </div>
        <div class="text-[11px] font-medium truncate text-white/90">
          {{ shot.role.split(' ')[0] }}
        </div>
      </button>
    </div>

    <!-- Active Shot Detail Card -->
    <div class="bg-black/50 p-3.5 rounded-xl border border-white/10 grid grid-cols-[1.2fr_1fr] gap-3.5 items-start">
      <!-- Left: Scene & Camera -->
      <div class="flex flex-col gap-2">
        <div class="flex items-center gap-2">
          <span class="px-2 py-0.5 rounded text-[11px] font-bold border font-mono" :class="selectedShot.badgeColor">
            {{ selectedShot.id }} ({{ selectedShot.time }})
          </span>
          <span class="text-white font-bold text-xs">{{ selectedShot.role }}</span>
        </div>

        <div class="space-y-1.5 text-[11px]">
          <div class="p-2 bg-white/5 rounded border border-white/10">
            <span class="text-sky-300 font-bold">주체(Subject):</span>
            <span class="text-white/90 ml-1.5">{{ selectedShot.subject }}</span>
          </div>
          <div class="p-2 bg-white/5 rounded border border-white/10">
            <span class="text-indigo-300 font-bold">핵심 행동(Action):</span>
            <span class="text-white/90 ml-1.5">{{ selectedShot.action }}</span>
          </div>
          <div class="p-2 bg-white/5 rounded border border-white/10">
            <span class="text-amber-300 font-bold">카메라(Camera):</span>
            <span class="text-white/90 ml-1.5 font-mono text-[10.5px]">{{ selectedShot.camera }}</span>
          </div>
        </div>
      </div>

      <!-- Right: Audio, Caption & Caution -->
      <div class="flex flex-col gap-2">
        <div class="p-2.5 bg-emerald-950/40 rounded-lg border border-emerald-500/30">
          <div class="text-[10.5px] text-emerald-300 font-bold flex items-center gap-1 mb-1">
            <span class="i-carbon-microphone"></span>
            <span>내레이션 (45~70자 호흡)</span>
          </div>
          <p class="text-[11px] text-white/95 leading-relaxed font-medium m-0">
            "{{ selectedShot.narration }}"
          </p>
        </div>

        <div class="p-2 bg-black/40 rounded-lg border border-white/10 flex items-center justify-between text-[11px]">
          <span class="text-white/60">후편집 자막:</span>
          <span class="text-amber-300 font-bold">{{ selectedShot.caption }}</span>
        </div>

        <div class="p-2 bg-rose-950/30 rounded-lg border border-rose-500/20 text-[10.5px] text-rose-200">
          <span class="font-bold text-rose-300">검수 주의:</span> {{ selectedShot.factCaution }}
        </div>
      </div>
    </div>
  </div>
</template>
