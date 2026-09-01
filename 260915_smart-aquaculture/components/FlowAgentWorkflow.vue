<script setup lang="ts">
import { ref } from 'vue'

interface WorkflowStep {
  id: number
  title: string
  badge: string
  color: string
  intent: string
  prompt: string
  rules: string[]
}

const steps: WorkflowStep[] = [
  {
    id: 1,
    title: '1. 계획 먼저 받기 (승인 전 생성 금지)',
    badge: 'Plan First',
    color: 'text-sky-400 border-sky-400/50 bg-sky-950/40',
    intent: '크레딧 낭비 방지: 영상을 바로 뽑지 않고 훅 3안과 쇼트 리스트 계획부터 검토',
    prompt: `지금은 영상을 생성하지 말고 계획만 작성해줘.

다음 순서로 답해줘:
1. 한 문장 핵심 주장
2. 첫 3초 훅 3안
3. 15~20초 전체 내레이션 초안
4. 3~5개 쇼트 리스트
5. 각 쇼트의 subject/action/camera/environment/style
6. 장면 간 연속성 규칙
7. 검증이 필요한 사실과 출처
8. 생성 모델이 실패할 가능성이 높은 요소
9. 후편집으로 처리할 요소

외부 자료의 확인되지 않은 내용에는 [검증 필요]를 붙여줘.
계획 마지막에 "승인 후 생성"이라고 적고 기다려줘.`,
    rules: [
      '크레딧 소모 없이 기획 정합성 먼저 확보',
      '외부 미확인 수치에 [검증 필요] 태깅 강제',
      '사용자 승인 전 임의 생성 원천 차단'
    ]
  },
  {
    id: 2,
    title: '2. 승인된 첫 쇼트(S01) 초안 생성',
    badge: 'Draft S01',
    color: 'text-emerald-400 border-emerald-400/50 bg-emerald-950/40',
    intent: '360p 초안으로 시작: 5대 필드를 명시하고 스스로 왜곡 점검 지시',
    prompt: `승인된 S01만 생성해줘.

목적: 스마트 양식장의 낯선 구조를 보여주고 다음 질문이 궁금해지게 만든다.
포맷: 9:16 vertical, 4 seconds, draft quality first

장면:
- subject: clean indoor recirculating aquaculture tank, water-quality sensor, several healthy fish
- action: the camera slowly pushes in from the tank edge toward the sensor and fish
- camera: medium-wide shot, one slow push-in, stable movement
- environment: plausible modern aquaculture facility, visible pipes and filtration area
- lighting: soft cool daylight, realistic reflections on water
- style: documentary realism, premium educational short-form, natural motion

연속성:
- keep the same blue-and-silver facility palette for later shots
- keep the same sensor housing and tank geometry
- no new people, no brand logos, no readable generated text

생성 후 스스로 fish anatomy, pipe logic, camera stability를 점검해줘.`,
    rules: [
      '초안(Draft)으로 속도와 크레딧 절약',
      '한 쇼트 1개 핵심 행동(Slow push-in) 엄수',
      '후속 쇼트 연결용 색상 팔레트 고정'
    ]
  },
  {
    id: 3,
    title: '3. 구체적 오류 수정 (정밀 피드백)',
    badge: 'Refine Error',
    color: 'text-amber-400 border-amber-400/50 bg-amber-950/40',
    intent: '"더 자연스럽게"라는 모호한 말 대신 문제점과 수정 행동을 1:1 특정',
    prompt: `이 쇼트의 구도와 스타일은 유지하고 다음 문제만 수정해줘.

문제:
- 센서 케이블이 수조 벽을 통과하는 위치가 불분명하다.
- 물고기의 크기가 쇼트 중간에 급격히 바뀐다.
- 카메라가 너무 빠르게 이동한다.

수정:
- 케이블을 센서 하우징에서 수조 외부 제어함 방향으로 자연스럽게 연결
- 같은 종과 비슷한 크기의 물고기로 유지
- 한 번의 느린 push-in만 사용
- 새 장비, 새 인물, 새 로고는 추가하지 않음`,
    rules: [
      '구도와 색감은 고정하고 특정 오류만 교정',
      '물리적 연결(배관·케이블) 현실성 보정',
      '불필요한 새 객체 추가 금지'
    ]
  },
  {
    id: 4,
    title: '4. 4가지 변형안(Variations) 비교',
    badge: '4 Variations',
    color: 'text-purple-400 border-purple-400/50 bg-purple-950/40',
    intent: '같은 핵심 구조를 유지하면서 카메라 각도와 전경 요소를 다변화하여 최적안 선택',
    prompt: `S01의 핵심 내용과 연속성은 유지하면서 변형안 4개를 만들어줘.

변경 가능한 요소:
1. 카메라를 낮은 수면 높이로 변경
2. 센서 데이터를 확인하는 손을 전경에 추가
3. 필터와 흐르는 물을 더 넓은 화면으로 보여주기
4. 수조 표면 반사와 물의 움직임을 강조

변경하지 말 것:
- 9:16 세로형 포맷
- 같은 파란색·은색 시설 팔레트
- 같은 센서와 수조 구조
- 한 쇼트 한 행동
- 읽을 수 있는 글자나 로고 추가 금지

각 변형안의 장점과 실패 가능성도 한 줄씩 설명해줘.`,
    rules: [
      '최대 4개까지만 비교하여 의사결정 지연 방지',
      '장점뿐 아니라 실패 가능성(실패율) 함께 분석',
      '최종안 선정 후 SceneBuilder로 조립'
    ]
  }
]

const currentStepId = ref(1)
const currentStep = computed(() => steps.find(s => s.id === currentStepId.value) || steps[0])

const copied = ref(false)
const copyPrompt = () => {
  navigator.clipboard.writeText(currentStep.value.prompt)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<script lang="ts">
import { computed } from 'vue'
</script>

<template>
  <div class="glass-card p-4 my-2 text-xs flex flex-col gap-3">
    <!-- Top Step Buttons -->
    <div class="grid grid-cols-4 gap-2">
      <button
        v-for="step in steps"
        :key="step.id"
        class="p-2.5 rounded-xl text-left border transition-all flex flex-col justify-between gap-1"
        :class="currentStepId === step.id ? 'bg-white/15 border-white/40 shadow-lg' : 'bg-black/30 border-white/5 hover:border-white/20 opacity-70 hover:opacity-100'"
        @click="currentStepId = step.id"
      >
        <div class="flex items-center justify-between">
          <span class="font-bold text-xs" :class="currentStepId === step.id ? 'text-white' : 'text-white/60'">
            Step 0{{ step.id }}
          </span>
          <span class="px-1.5 py-0.2 rounded text-[9.5px] font-mono border" :class="step.color">
            {{ step.badge }}
          </span>
        </div>
        <div class="text-[10.5px] font-medium truncate text-white/90">
          {{ step.title.split(' ')[1] }}
        </div>
      </button>
    </div>

    <!-- Active Step Content Area -->
    <div class="bg-black/50 p-3.5 rounded-xl border border-white/10 grid grid-cols-[1.3fr_1fr] gap-4 items-start">
      <!-- Left: Copyable Prompt Box -->
      <div class="flex flex-col gap-2">
        <div class="flex items-center justify-between">
          <span class="text-white font-bold text-xs flex items-center gap-1.5">
            <span class="i-carbon-terminal text-sky-400"></span>
            <span>{{ currentStep.title }}</span>
          </span>
          <button
            class="px-2.5 py-1 rounded text-xs bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 transition-all"
            @click="copyPrompt"
          >
            <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
            <span>{{ copied ? '복사 완료!' : '프롬프트 복사' }}</span>
          </button>
        </div>

        <div class="p-2.5 bg-black/60 rounded-lg border border-white/10 max-h-[190px] overflow-y-auto font-mono text-[11px] text-white/90 leading-relaxed whitespace-pre-wrap select-all">
{{ currentStep.prompt }}
        </div>
      </div>

      <!-- Right: Intent & Strict Rules -->
      <div class="flex flex-col gap-2.5">
        <div class="p-2.5 bg-sky-950/30 rounded-lg border border-sky-500/30">
          <div class="text-[10.5px] text-sky-300 font-bold mb-1 flex items-center gap-1">
            <span class="i-carbon-bullseye"></span>
            <span>단계별 지시 목적</span>
          </div>
          <p class="text-[11px] text-sky-100 leading-snug m-0">
            {{ currentStep.intent }}
          </p>
        </div>

        <div class="p-2.5 bg-white/5 rounded-lg border border-white/10">
          <div class="text-[10.5px] text-amber-300 font-bold mb-1.5 flex items-center gap-1">
            <span class="i-carbon-rule"></span>
            <span>반드시 지켜야 할 가드레일</span>
          </div>
          <ul class="space-y-1 text-[10.5px] text-white/80 pl-4 list-disc m-0">
            <li v-for="(rule, idx) in currentStep.rules" :key="idx">{{ rule }}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
