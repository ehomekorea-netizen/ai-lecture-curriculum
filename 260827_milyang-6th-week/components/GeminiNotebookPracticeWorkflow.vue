<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import {
  Search,
  Filter,
  MessageSquare,
  Sparkles,
  FileText,
  ShieldCheck,
  Terminal,
  ArrowRight,
  CheckCircle2,
  Bookmark,
  UserCheck,
  Bot,
  Lightbulb,
  Check
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const scenes = [
  {
    id: 1,
    step: 'STEP 01',
    badge: 'STEP 01. 자료 조사 (Deep Research)',
    icon: Search,
    color: 'blue',
    title: '맨땅에서 시작하는 AI 심층 자료 탐색',
    desc: '자료가 전혀 없는 상태에서 목표 기업/직무의 최신 채용 트렌드, 요구 스킬셋, 합격자 우수 포트폴리오 구조를 AI가 자동으로 광범위하게 수집합니다.',
    rule: '단순 검색이 아닌 [조사 목표 · 범위 · 출력 기준]을 명시하여 AI가 체계적인 조사 계획을 수립하도록 유도',
    type: 'prompt',
    promptTitle: 'Deep Research Prompt (심층 조사 설계 프롬프트)',
    promptText: `[조사 목표] 밀양 취업역량 교육 수강생으로서 지원할 목표 기업/직무 맞춤형 포트폴리오 기획서 수립
[조사 범위]
1. 2026년 IT/스타트업 신입 서비스기획 채용 트렌드 및 우대사항
2. 서류 합격자들의 우수 실무 포트폴리오 구조 및 문제해결 방식
3. 기업 면접관이 주목하는 생성형 AI 활용 실무 역량 기준
[출력 기준]
- 자료명, 출처, 핵심 요구역량, 내 포트폴리오 차별화 포인트를 표로 정리
- 단순 이론을 넘어 '실무 문제해결 및 산출물 포트폴리오 모델' 위주 조사`
  },
  {
    id: 2,
    step: 'STEP 02',
    badge: 'STEP 02. 자료 선별 및 분류 (Source Curation)',
    icon: Filter,
    color: 'indigo',
    title: 'AI 수집 자료에서 알짜만 골라 담기',
    desc: 'AI가 찾아준 자료를 그대로 사용하지 않고, 공신력과 최신성을 기준으로 필요한 자료만 꼼꼼하게 선별하여 주제별로 체계화합니다.',
    rule: 'AI가 추천한 수많은 정보 중, 내가 실제 지원할 직무와 내 경험에 맞는 알짜 자료만 수강생이 직접 필터링',
    type: 'curation',
    criteria: [
      { tag: '신뢰성 & 최신성', desc: '기업 공식 채용공고 및 최근 3개년 업계 리포트' },
      { tag: '직무 관련성', desc: '채용 시장 실제 요구 스킬 및 내 프로젝트 매칭도' },
      { tag: '구체성 & 중복제거', desc: '실제 채용 우대사항 명확한 자료 남기고 중복 배제' }
    ],
    labels: [
      { name: 'TREND', label: '채용동향' },
      { name: 'JOB_DESC', label: '직무공고' },
      { name: 'PORTFOLIO', label: '우수사례' },
      { name: 'MY_EXP', label: '경험DB' },
      { name: 'FEEDBACK', label: '피드백' }
    ]
  },
  {
    id: 3,
    step: 'STEP 03',
    badge: 'STEP 03. 자료 분석 (Chat 심층 질의)',
    icon: MessageSquare,
    color: 'purple',
    title: '단순 요약을 넘어 비교·교차검증하기',
    desc: '수집된 채용 정보와 내 경험 자료를 교차 대조하여 기업 요구역량과 내 프로젝트 강점을 분석하고 차별화된 합격 포인트를 발굴합니다.',
    rule: '질문할 때마다 원문 출처 각주 [1][2]를 클릭해 팩트를 직접 검증',
    type: 'chat_multi',
    prompts: [
      { num: 'Q1', q: '현재 자료를 종합해서 목표 기업이 신입 지원자에게 가장 바라는 핵심 역량이 무엇인지 분석해줘.' },
      { num: 'Q2', q: '목표 기업의 채용 공고 우대사항과 내가 정리한 프로젝트 경험 DB를 비교해줘.' },
      { num: 'Q3', q: '내 경험에서 기업의 요구역량과 일치하는 강점 3가지를 도출해줘.' },
      { num: 'Q4', q: '경쟁 지원자들과 차별화할 수 있는 나만의 프로젝트 문제해결 포인트를 찾아줘.' }
    ]
  },
  {
    id: 4,
    step: 'STEP 04',
    badge: 'STEP 04. 지식 축적 및 환류 (Note ➔ Source)',
    icon: Sparkles,
    color: 'amber',
    title: '정리한 메모가 다시 AI의 지식이 되는 선순환',
    desc: 'Chat으로 분석한 핵심 인사이트를 Note 메모로 저장하고, 이 Note를 다시 새로운 공식 Source로 승격시켜 지식을 연속 발전시킵니다.',
    rule: 'Notebook은 단순 파일 보관함이 아닌, 지식이 계속 진화하는 작업 공간',
    type: 'knowledge_loop',
    notes: [
      { title: '직무 강점', text: '비전공자이지만 AI 에이전트 협업으로 실제 웹 산출물 제작 경험 보유' },
      { title: '포트폴리오 전략', text: '단순 결과 나열 지양, 트러블슈팅과 Before/After 데이터 지표 강조' },
      { title: '면접 대비', text: 'AI가 작성한 초안에 얽매이지 않고 실제 내가 겪은 고민과 배운 점 정리' }
    ]
  },
  {
    id: 5,
    step: 'STEP 05',
    badge: 'STEP 05. 실무 프로젝트 기획서 초안 작성 (Drafting)',
    icon: FileText,
    color: 'emerald',
    title: '표준 프로젝트 목차 기반 팩트 중심 초안 도출',
    desc: 'Notebook에 축적된 100% 근거 자료만을 바탕으로 밀양 청소년 취업역량 프로젝트 표준 기획서 초안을 완성합니다.',
    rule: '자료에 없는 내용은 추측하지 않고 [확인 필요]로 명시하여 신뢰도 확보',
    type: 'prompt',
    promptTitle: 'Drafting Prompt (초안 작성 프롬프트)',
    promptText: `현재 Notebook의 내 경험 자료만을 근거로
[신입 서비스기획 실무 포트폴리오] 기획서 초안을 작성해줘.

1. 내 경험 DB에 없는 내용은 추측하지 말고 [확인 필요]로 표시
2. 수치와 프로젝트 성과는 원문을 유지하고 관련 Source 각주 표시
3. 채용담당자가 신뢰하는 STAR 구조 기반 비즈니스 기획 문체 사용

목차: 프로젝트 개요, 문제 정의 및 타깃, 나의 기여도(STAR), 트러블슈팅, 정량 성과`
  },
  {
    id: 6,
    step: 'STEP 06',
    badge: 'STEP 06. AI 검토 및 인간의 책임 (Review)',
    icon: ShieldCheck,
    color: 'rose',
    title: 'AI 검토 리포트와 수강생(취업준비생)의 최종 결정',
    desc: '작성된 초안의 논리적 비약과 근거 부족을 AI로 1차 스크리닝한 뒤, 취업준비생의 실제 경험과 진실성에 맞춰 최종 확정합니다.',
    rule: 'AI는 초안과 검토를 도울 뿐, 최종 의사결정과 문서 책임은 사람에게 있습니다.',
    type: 'review_roles',
    aiRoles: ['논리적 비약 & 누락 항목 점검', '출처 미확인 수치 필터링', '직무 목표-성과지표 연결성 검토', '비즈니스 문체 다듬기 및 요약'],
    humanRoles: ['실제 내 경험과의 진실성 일치 여부 확인', '과장되거나 날조된 표현 수정', '나만의 고유한 동기와 스토리 반영', '최종 입사지원서 제출 및 면접 답변 책임']
  }
]

const currentIdx = ref(0)

watch(() => props.stage, (newStage) => {
  if (typeof newStage === 'number') {
    currentIdx.value = Math.min(Math.max(newStage, 0), scenes.length - 1)
  }
}, { immediate: true })

const currentScene = computed(() => scenes[currentIdx.value] || scenes[0])
</script>

<template>
  <div class="w-full h-[290px] flex items-center justify-center select-none font-sans relative overflow-hidden">
    <Transition name="practice-fade" mode="out-in">
      <div
        :key="currentScene.id"
        class="w-full h-full flex items-center justify-between gap-7 text-left"
      >
        <!-- ── Left Column: Statement, Concept & Key Rule (Matching Slide 16 Scale) ── -->
        <div class="w-[44%] flex flex-col justify-between h-full py-1">
          <div>
            <!-- Badge -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11.5px] font-bold mb-2.5 shadow-2xs"
              :class="{
                'bg-blue-50 text-blue-700 border border-blue-200': currentScene.color === 'blue',
                'bg-indigo-50 text-indigo-700 border border-indigo-200': currentScene.color === 'indigo',
                'bg-purple-50 text-purple-700 border border-purple-200': currentScene.color === 'purple',
                'bg-amber-50 text-amber-800 border border-amber-200': currentScene.color === 'amber',
                'bg-emerald-50 text-emerald-800 border border-emerald-300': currentScene.color === 'emerald',
                'bg-rose-50 text-rose-800 border border-rose-200': currentScene.color === 'rose'
              }"
            >
              <component :is="currentScene.icon" :size="13" />
              <span>{{ currentScene.badge }}</span>
            </div>

            <!-- Main Title -->
            <h2 class="text-[22px] md:text-[24px] font-serif font-bold text-slate-900 leading-snug tracking-tight mb-2.5 break-keep">
              {{ currentScene.title }}
            </h2>

            <!-- Description -->
            <p class="text-[13.5px] md:text-[14px] text-slate-800 font-sans font-medium leading-relaxed break-keep">
              {{ currentScene.desc }}
            </p>
          </div>

          <!-- Bottom Key Rule Tag -->
          <div class="p-2 px-3 rounded-xl bg-slate-50 border border-slate-200/90 text-[11px] text-indigo-950 leading-normal flex items-start gap-2 shadow-2xs">
            <Lightbulb :size="14" class="text-amber-500 shrink-0 mt-0.5" />
            <span><strong class="text-indigo-900 font-bold">핵심 포인트: </strong>{{ currentScene.rule }}</span>
          </div>
        </div>

        <!-- ── Right Column: High-Impact Spacious Visual Panels ── -->
        <div class="w-[56%] h-full flex items-center justify-center">
          <!-- 1. Single Prompt Terminal (Step 1 & Step 5) -->
          <div
            v-if="currentScene.type === 'prompt'"
            class="w-full h-full rounded-2xl bg-slate-900 p-3.5 px-4 flex flex-col justify-between text-left border border-slate-800 shadow-xl"
          >
            <div class="flex items-center justify-between text-[10.5px] font-mono text-slate-400 border-b border-slate-800 pb-1.5 mb-1.5">
              <div class="flex items-center gap-1.5">
                <Terminal :size="13" class="text-emerald-400" />
                <span class="font-bold text-slate-200">{{ currentScene.promptTitle }}</span>
              </div>
              <span class="text-[10px] text-amber-400 font-bold">Gemini Deep Research</span>
            </div>
            <pre class="text-[11px] md:text-[11.5px] font-mono text-emerald-300 whitespace-pre-wrap leading-relaxed overflow-hidden my-auto">{{ currentScene.promptText }}</pre>
            <div class="text-[10px] text-slate-400 flex items-center justify-between pt-1.5 border-t border-slate-800/90">
              <span class="text-slate-400">조사 목표 · 범위 · 출력 형태 명시</span>
              <span class="text-emerald-400 font-mono font-bold">자동 조사 계획 수립 & 실행</span>
            </div>
          </div>

          <!-- 2. Source Curation & Labeling (Step 2) -->
          <div
            v-else-if="currentScene.type === 'curation'"
            class="w-full h-full rounded-2xl bg-white p-3.5 px-4 flex flex-col justify-between text-left border border-slate-200/90 shadow-xl"
          >
            <div>
              <div class="text-[11.5px] font-mono font-bold text-indigo-700 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <Filter :size="13" />
                <span>자료 선별 기준 4원칙</span>
              </div>
              <div class="space-y-1.5 mb-2.5">
                <div
                  v-for="(crit, idx) in currentScene.criteria"
                  :key="idx"
                  class="flex items-center justify-between p-1.5 px-3 rounded-lg bg-indigo-50/50 border border-indigo-100 text-[12px]"
                >
                  <span class="font-bold text-indigo-950 flex items-center gap-1.5">
                    <CheckCircle2 :size="13" class="text-indigo-600" />
                    <span>{{ crit.tag }}</span>
                  </span>
                  <span class="text-[11.5px] text-slate-600 font-medium">{{ crit.desc }}</span>
                </div>
              </div>
            </div>

            <div>
              <div class="text-[11px] font-mono font-bold text-slate-500 uppercase tracking-wider mb-1.5">
                5대 카테고리 자동 라벨링
              </div>
              <div class="flex flex-wrap gap-1.5">
                <span
                  v-for="(l, idx) in currentScene.labels"
                  :key="idx"
                  class="px-2 py-0.5 rounded text-[11px] font-bold bg-slate-100 text-slate-800 border border-slate-200"
                >
                  <strong class="text-blue-700 font-mono">{{ l.name }}</strong> {{ l.label }}
                </span>
              </div>
            </div>
          </div>

          <!-- 3. Multi-Prompt Chat Questions (Step 3: Large, Crisp, 100% Fully Visible Questions) -->
          <div
            v-else-if="currentScene.type === 'chat_multi'"
            class="w-full h-full rounded-2xl bg-white p-3.5 px-4 flex flex-col justify-between text-left border border-slate-200/90 shadow-xl"
          >
            <div class="text-[11.5px] font-mono font-bold text-purple-700 uppercase tracking-wider flex items-center justify-between pb-1.5 border-b border-slate-100">
              <span class="flex items-center gap-1.5">
                <MessageSquare :size="13" />
                <span>Chat 심층 비교 질의 프롬프트 예시 4종</span>
              </span>
              <span class="text-[10px] text-slate-400 font-normal">교안 원문</span>
            </div>

            <!-- 4 Distinct Spacious Question Cards -->
            <div class="space-y-1.5 my-auto">
              <div
                v-for="p in currentScene.prompts"
                :key="p.num"
                class="p-2 px-3 rounded-xl bg-purple-50/80 border border-purple-200/90 flex items-center gap-2.5 shadow-2xs hover:border-purple-300 transition-colors"
              >
                <span class="w-5 h-5 rounded-md bg-purple-600 text-white font-mono text-[10px] font-bold flex items-center justify-center shrink-0">
                  {{ p.num }}
                </span>
                <p class="text-[12px] md:text-[12.5px] font-medium text-slate-900 leading-snug break-keep">
                  "{{ p.q }}"
                </p>
              </div>
            </div>

            <div class="text-[10.5px] text-purple-900 font-bold bg-purple-50 py-1 px-2.5 rounded-lg text-center flex items-center justify-center gap-1.5">
              <Lightbulb :size="12" class="text-amber-500 shrink-0" />
              <span>단순 요약 대신 "비교해줘", "차이점을 구분해줘"로 질문하는 것이 핵심</span>
            </div>
          </div>

          <!-- 4. Knowledge Loop Note -> Source (Step 4) -->
          <div
            v-else-if="currentScene.type === 'knowledge_loop'"
            class="w-full h-full rounded-2xl bg-white p-3.5 px-4 flex flex-col justify-between text-left border border-slate-200/90 shadow-xl"
          >
            <div class="text-[11.5px] font-mono font-bold text-amber-800 uppercase tracking-wider flex items-center justify-between pb-1.5 border-b border-slate-100">
              <span class="flex items-center gap-1.5">
                <Sparkles :size="13" />
                <span>Note 작성 예시 ➔ 새 Source로 승격</span>
              </span>
              <span class="text-[10px] text-amber-700 font-bold">지식 선순환</span>
            </div>

            <div class="space-y-1.5 my-auto">
              <div
                v-for="(n, idx) in currentScene.notes"
                :key="idx"
                class="p-1.5 px-3 rounded-lg bg-amber-50/50 border border-amber-200/80 text-[11.5px] leading-snug"
              >
                <div class="font-bold text-amber-950 mb-0.5 flex items-center gap-1.5">
                  <Bookmark :size="12" class="text-amber-600" />
                  <span>{{ n.title }}</span>
                </div>
                <div class="text-slate-700 text-[11px] pl-4">{{ n.text }}</div>
              </div>
            </div>

            <!-- Loop Diagram Banner -->
            <div class="p-2 px-3 rounded-lg bg-slate-900 text-white text-[10.5px] font-mono flex items-center justify-between shadow-sm">
              <span>외부자료</span>
              <ArrowRight :size="11" class="text-amber-400" />
              <span>AI분석</span>
              <ArrowRight :size="11" class="text-amber-400" />
              <span class="text-amber-300 font-bold">Note작성</span>
              <ArrowRight :size="11" class="text-amber-400" />
              <span class="text-emerald-300 font-bold">새 Source등록</span>
            </div>
          </div>

          <!-- 5. Review & Human vs AI Roles (Step 6) -->
          <div
            v-else-if="currentScene.type === 'review_roles'"
            class="w-full h-full rounded-2xl bg-white p-3.5 px-4 flex flex-col justify-between text-left border border-slate-200/90 shadow-xl"
          >
            <div class="text-[11.5px] font-mono font-bold text-rose-800 uppercase tracking-wider flex items-center justify-between pb-1.5 border-b border-slate-100">
              <span class="flex items-center gap-1.5">
                <ShieldCheck :size="13" />
                <span>AI와 사람의 명확한 역할 분담 원칙</span>
              </span>
              <span class="text-[10px] text-rose-700 font-bold">최종 책임 = 사람</span>
            </div>

            <div class="grid grid-cols-2 gap-2.5 my-auto">
              <!-- AI Role Box -->
              <div class="p-2 rounded-xl bg-slate-50 border border-slate-200">
                <div class="flex items-center gap-1.5 text-[11px] font-bold text-slate-800 mb-1 pb-1 border-b border-slate-200">
                  <Bot :size="13" class="text-blue-600" />
                  <span>AI가 잘하는 일</span>
                </div>
                <ul class="space-y-0.5 text-[10px] text-slate-600 leading-tight">
                  <li v-for="(r, idx) in currentScene.aiRoles" :key="idx" class="flex items-start gap-1">
                    <span class="text-blue-500 font-bold">•</span>
                    <span>{{ r }}</span>
                  </li>
                </ul>
              </div>

              <!-- Human Role Box -->
              <div class="p-2 rounded-xl bg-rose-50/70 border border-rose-200">
                <div class="flex items-center gap-1.5 text-[11px] font-bold text-rose-950 mb-1 pb-1 border-b border-rose-200">
                  <UserCheck :size="13" class="text-rose-600" />
                  <span>사람이 해야 할 일</span>
                </div>
                <ul class="space-y-0.5 text-[10px] text-rose-900 font-medium leading-tight">
                  <li v-for="(r, idx) in currentScene.humanRoles" :key="idx" class="flex items-start gap-1">
                    <Check :size="10" class="text-rose-600 shrink-0 mt-0.5" />
                    <span>{{ r }}</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="text-[9.5px] text-slate-800 font-bold bg-slate-100 py-1 px-2 rounded-md text-center">
              "AI는 초안을 만들 수 있지만, 취업준비생의 차별화된 경험과 최종 책임은 사람이 집니다."
            </div>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.practice-fade-enter-active,
.practice-fade-leave-active {
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.practice-fade-enter-from {
  opacity: 0;
  transform: translateY(10px) scale(0.985);
}

.practice-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.985);
}
</style>
