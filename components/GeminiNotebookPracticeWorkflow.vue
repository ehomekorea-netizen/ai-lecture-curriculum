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
    desc: '자료가 전혀 없는 상태에서 2026년 고령층 디지털 격차 관련 최신 정책, 통계, 학술 연구, 복지 현장 사례를 AI가 자동으로 광범위하게 수집합니다.',
    rule: '단순 검색이 아닌 [조사 목표 · 범위 · 출력 기준]을 명시하여 AI가 체계적인 조사 계획을 수립하도록 유도',
    type: 'prompt',
    promptTitle: 'Deep Research Prompt (심층 조사 설계 프롬프트)',
    promptText: `[조사 목표] 2026년 고령층 디지털 격차 해소를 위한 복지관 신규 사업계획서 수립
[조사 범위]
1. 2024~2026 보건복지부·NIA 정책 및 지자체 지원 방향
2. 고령층 스마트폰·키오스크·모바일 뱅킹 이용 실태 통계
3. 타 복지관 및 지역사회 디지털 역량 강화 성공/한계 사례
[출력 기준]
- 자료명, 발행기관, 발행연도, 핵심 시사점, 복지관 적용 포인트를 표로 정리
- 단순 기기 교육을 넘어 '생활 밀착형 지속 활용 모델' 위주 조사`
  },
  {
    id: 2,
    step: 'STEP 02',
    badge: 'STEP 02. 자료 선별 및 분류 (Source Curation)',
    icon: Filter,
    color: 'indigo',
    title: 'AI 수집 자료에서 알짜만 골라 담기',
    desc: 'AI가 찾아준 자료를 그대로 사용하지 않고, 공신력과 최신성을 기준으로 필요한 자료만 꼼꼼하게 선별하여 주제별로 체계화합니다.',
    rule: 'AI는 자료를 추천할 뿐, 우리 복지관 사업에 적합한지는 사람이 직접 필터링',
    type: 'curation',
    criteria: [
      { tag: '신뢰성 & 최신성', desc: '공공기관(복지부·NIA 등) 최근 3개년 자료' },
      { tag: '현장 관련성', desc: '고령층 실제 이용 격차 및 사업 실행 가능성' },
      { tag: '구체성 & 중복제거', desc: '수치·근거 명확한 자료 남기고 중복 배제' }
    ],
    labels: [
      { name: 'POLICY', label: '정책·제도' },
      { name: 'STATISTICS', label: '통계·현황' },
      { name: 'RESEARCH', label: '연구·논문' },
      { name: 'CASE', label: '현장사례' },
      { name: 'INTERNAL', label: '기관자료' }
    ]
  },
  {
    id: 3,
    step: 'STEP 03',
    badge: 'STEP 03. 자료 분석 (Chat 심층 질의)',
    icon: MessageSquare,
    color: 'purple',
    title: '단순 요약을 넘어 비교·교차검증하기',
    desc: '수집된 문서들을 교차 대조하여 정책 지원 방향과 현장의 실제 문제점 간의 괴리를 분석하고 차별화된 사업 명분을 발굴합니다.',
    rule: '질문할 때마다 원문 출처 각주 [1][2]를 클릭해 팩트를 직접 검증',
    type: 'chat_multi',
    prompts: [
      { num: 'Q1', q: '현재 자료를 종합해서 고령층 디지털 격차 문제가 왜 중요한지 설명해줘.' },
      { num: 'Q2', q: '정부 정책의 방향과 현장 연구에서 나타난 문제를 비교해줘.' },
      { num: 'Q3', q: '현재 자료에서 반복적으로 등장하는 핵심 문제를 정리해줘.' },
      { num: 'Q4', q: '자료에서 공통적으로 확인되는 내용과 서로 다른 주장을 구분해줘.' }
    ]
  },
  {
    id: 4,
    step: 'STEP 04',
    badge: 'STEP 04. 정리 메모를 새 자료로 등록 (Note ➔ Source)',
    icon: Sparkles,
    color: 'amber',
    title: 'AI로 정리한 메모가 다음 작업의 새로운 원본 자료가 됩니다',
    desc: 'Chat으로 분석하고 정제한 핵심 내용을 메모(Note)로 남기고, 이 메모를 다시 AI의 원본 자료(Source)로 추가하여 문서 작성을 이어갑니다.',
    rule: '외부 자료 분석 ➔ 핵심 메모 정리 ➔ 새 원본 자료로 추가하여 완성도 높이기',
    type: 'knowledge_loop',
    notes: [
      { title: '사업 필요성', text: '단순 기기 보급을 넘어 실생활 서비스(키오스크·뱅킹) 활용 격차 심각' },
      { title: '정책 방향', text: '단발성 교육 지양, 일상생활 밀착형 1:1 맞춤 디지털 역량 강화 추진' },
      { title: '현장 시사점', text: '교육 후 반복 실습과 복지관-지역사회 연계 지지체계 필수' }
    ]
  },
  {
    id: 5,
    step: 'STEP 05',
    badge: 'STEP 05. 사업계획서 초안 작성 (Drafting)',
    icon: FileText,
    color: 'emerald',
    title: '표준 행정 목차 기반 팩트 중심 초안 도출',
    desc: 'Notebook에 축적된 100% 근거 자료만을 바탕으로 종합사회복지관 표준 12개 목차에 맞춘 행정 공문서 초안을 완성합니다.',
    rule: '자료에 없는 내용은 추측하지 않고 [확인 필요]로 명시하여 신뢰도 확보',
    type: 'prompt',
    promptTitle: 'Drafting Prompt (초안 작성 프롬프트)',
    promptText: `현재 Notebook의 자료만을 근거로
[고령층 디지털 역량 강화 프로그램] 사업계획서 초안을 작성해줘.

1. 자료에 없는 내용은 추측하지 말고 [확인 필요]로 표시
2. 수치와 통계는 원문을 유지하고 관련 Source 각주 표시
3. 종합사회복지관 내부 사업계획서 행정문체 사용

목차: 사업배경, 지역사회 욕구, 사업목적·목표, 대상, 세부프로그램, 예산, 성과지표`
  },
  {
    id: 6,
    step: 'STEP 06',
    badge: 'STEP 06. AI 검토 및 인간의 책임 (Review)',
    icon: ShieldCheck,
    color: 'rose',
    title: 'AI 검토 리포트와 사회복지사의 최종 결정',
    desc: '작성된 초안의 논리적 비약과 근거 부족을 AI로 1차 스크리닝한 뒤, 사회복지사의 전문적 판단과 기관 현실을 반영해 최종 확정합니다.',
    rule: 'AI는 초안과 검토를 도울 뿐, 최종 의사결정과 문서 책임은 사람에게 있습니다.',
    type: 'review_roles',
    aiRoles: ['논리적 비약 & 누락 항목 점검', '출처 미확인 수치 필터링', '목표-성과지표 연결성 검토', '행정 문체 다듬기 및 요약'],
    humanRoles: ['복지관 현장 예산·인력 적합성 판단', '민감 사례 & 개인정보 보호 점검', '사회복지사 전문 가치 반영', '최종 승인 및 문서 책임']
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
  <div class="w-full h-[280px] flex items-center justify-center select-none font-sans relative">
    <Transition name="practice-fade" mode="out-in">
      <div
        :key="currentScene.id"
        class="w-full h-full flex items-center justify-between gap-7 text-left"
      >
        <!-- ── Left Column: Statement, Concept & Key Rule (Matching Slide 16 Scale) ── -->
        <div class="w-[44%] flex flex-col justify-between h-[270px] py-0.5">
          <div>
            <!-- Badge -->
            <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11.5px] font-bold mb-2.5 shadow-2xs"
              :class="{
                'bg-blue-950/40 text-blue-400 border border-blue-200': currentScene.color === 'blue',
                'bg-indigo-50 text-indigo-300 border border-indigo-200': currentScene.color === 'indigo',
                'bg-purple-50 text-purple-700 border border-purple-200': currentScene.color === 'purple',
                'bg-amber-50 text-amber-800 border border-amber-200': currentScene.color === 'amber',
                'bg-emerald-950/40 text-emerald-300 border border-emerald-300': currentScene.color === 'emerald',
                'bg-rose-950/40 text-rose-300 border border-rose-200': currentScene.color === 'rose'
              }"
            >
              <component :is="currentScene.icon" :size="13" />
              <span>{{ currentScene.badge }}</span>
            </div>

            <!-- Main Title -->
            <h2 class="text-[22px] md:text-[24px] font-serif font-bold text-white leading-snug tracking-tight mb-2.5 break-keep">
              {{ currentScene.title }}
            </h2>

            <!-- Description -->
            <p class="text-[13.5px] md:text-[14px] text-slate-100 font-sans font-medium leading-relaxed break-keep">
              {{ currentScene.desc }}
            </p>
          </div>

          <!-- Bottom Key Rule Tag -->
          <div class="p-2 px-3 rounded-xl bg-white/5 border border-white/10 text-[10.5px] text-slate-200 leading-snug flex items-start gap-2 shadow-2xs mt-2">
            <Lightbulb :size="14" class="text-amber-500 shrink-0 mt-0.5" />
            <span><strong class="text-indigo-300 font-bold">핵심 포인트: </strong>{{ currentScene.rule }}</span>
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
            class="w-full h-full rounded-2xl bg-white/6 p-3.5 px-4 flex flex-col justify-between text-left border border-white/10 shadow-xl"
          >
            <div>
              <div class="text-[11.5px] font-mono font-bold text-indigo-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <Filter :size="13" />
                <span>자료 선별 기준 4원칙</span>
              </div>
              <div class="space-y-1.5 mb-2.5">
                <div
                  v-for="(crit, idx) in currentScene.criteria"
                  :key="idx"
                  class="flex items-center justify-between p-1.5 px-3 rounded-lg bg-white/5 border border-white/10 text-[12px]"
                >
                  <span class="font-bold text-indigo-300 flex items-center gap-1.5">
                    <CheckCircle2 :size="13" class="text-indigo-400" />
                    <span>{{ crit.tag }}</span>
                  </span>
                  <span class="text-[11.5px] text-white font-medium">{{ crit.desc }}</span>
                </div>
              </div>
            </div>

            <div>
              <div class="text-[11px] font-mono font-bold text-slate-400 uppercase tracking-wider mb-1.5">
                5대 카테고리 자동 라벨링
              </div>
              <div class="flex flex-wrap gap-1.5">
                <span
                  v-for="(l, idx) in currentScene.labels"
                  :key="idx"
                  class="px-2 py-0.5 rounded text-[11px] font-bold bg-white/8 text-slate-100 border border-white/10"
                >
                  <strong class="text-blue-400 font-mono">{{ l.name }}</strong> {{ l.label }}
                </span>
              </div>
            </div>
          </div>

          <!-- 3. Multi-Prompt Chat Questions (Step 3: Exact 270px matching left column baseline) -->
          <div
            v-else-if="currentScene.type === 'chat_multi'"
            class="w-full h-[270px] rounded-2xl bg-white/4 p-3 px-3.5 flex flex-col justify-between text-left border border-white/10 shadow-lg"
          >
            <!-- Header (Height: 22px) -->
            <div class="text-[11px] font-mono font-bold text-purple-300 uppercase tracking-wider flex items-center justify-between pb-1 border-b border-white/10 shrink-0">
              <span class="flex items-center gap-1.5">
                <MessageSquare :size="13" class="text-purple-400" />
                <span>Chat 심층 비교 질의 프롬프트 예시 4종</span>
              </span>
              <span class="text-[9.5px] text-slate-400 font-normal">교안 원문</span>
            </div>

            <!-- 4 Clean Rows (Height ~165px) -->
            <div class="flex flex-col justify-between my-auto py-0.5 space-y-1">
              <div
                v-for="p in currentScene.prompts"
                :key="p.num"
                class="flex items-center gap-2 py-0.5"
              >
                <span class="w-4.5 h-4.5 rounded bg-purple-500/30 text-purple-300 border border-purple-400/40 font-mono text-[9.5px] font-extrabold flex items-center justify-center shrink-0">
                  {{ p.num }}
                </span>
                <p class="text-[11px] md:text-[11.5px] font-normal text-slate-100 leading-tight break-keep">
                  "{{ p.q }}"
                </p>
              </div>
            </div>

            <!-- Bottom Tip (Height: 30px, aligns perfectly with the left column's bottom tip baseline) -->
            <div class="text-[10px] text-purple-200 font-medium bg-purple-950/60 py-1 px-2 rounded-lg text-center flex items-center justify-center gap-1.5 border border-purple-500/30 shrink-0 h-[30px]">
              <Lightbulb :size="11" class="text-amber-400 shrink-0" />
              <span>단순 요약 대신 "비교해줘", "차이점을 구분해줘"로 질문하는 것이 핵심</span>
            </div>
          </div>

          <!-- 4. Knowledge Loop Note -> Source (Step 4) -->
          <div
            v-else-if="currentScene.type === 'knowledge_loop'"
            class="w-full h-full rounded-2xl bg-white/4 p-3 px-3.5 flex flex-col justify-between text-left border border-white/10 shadow-lg"
          >
            <div class="text-[11px] font-mono font-bold text-amber-300 uppercase tracking-wider flex items-center justify-between pb-1 border-b border-white/10">
              <span class="flex items-center gap-1.5">
                <Sparkles :size="13" class="text-amber-400" />
                <span>정리 메모(Note) 예시 ➔ 새 원본(Source)으로 추가</span>
              </span>
              <span class="text-[9.5px] text-amber-400 font-bold">자료 축적</span>
            </div>

            <div class="flex flex-col gap-1.5 my-auto">
              <div
                v-for="(n, idx) in currentScene.notes"
                :key="idx"
                class="p-1.5 px-3 rounded-lg bg-white/5 border border-white/8 text-[11.5px] leading-snug"
              >
                <div class="font-bold text-amber-300 mb-0.5 flex items-center gap-1.5">
                  <Bookmark :size="12" class="text-amber-400" />
                  <span>{{ n.title }}</span>
                </div>
                <div class="text-slate-200 text-[11px] pl-4">{{ n.text }}</div>
              </div>
            </div>

            <!-- Loop Diagram Banner -->
            <div class="p-1.5 px-3 rounded-lg bg-white/6 text-slate-200 text-[10.5px] font-mono flex items-center justify-between border border-white/10">
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
            class="w-full h-full rounded-2xl bg-white/6 p-3.5 px-4 flex flex-col justify-between text-left border border-white/10 shadow-xl"
          >
            <div class="text-[11.5px] font-mono font-bold text-rose-300 uppercase tracking-wider flex items-center justify-between pb-1.5 border-b border-slate-100">
              <span class="flex items-center gap-1.5">
                <ShieldCheck :size="13" />
                <span>AI와 사람의 명확한 역할 분담 원칙</span>
              </span>
              <span class="text-[10px] text-rose-400 font-bold">최종 책임 = 사람</span>
            </div>

            <div class="grid grid-cols-2 gap-2.5 my-auto">
              <!-- AI Role Box -->
              <div class="p-2 rounded-xl bg-white/5 border border-white/10">
                <div class="flex items-center gap-1.5 text-[11px] font-bold text-slate-100 mb-1 pb-1 border-b border-white/10">
                  <Bot :size="13" class="text-blue-600" />
                  <span>AI가 잘하는 일</span>
                </div>
                <ul class="space-y-0.5 text-[10px] text-slate-400 leading-tight">
                  <li v-for="(r, idx) in currentScene.aiRoles" :key="idx" class="flex items-start gap-1">
                    <span class="text-blue-500 font-bold">•</span>
                    <span>{{ r }}</span>
                  </li>
                </ul>
              </div>

              <!-- Human Role Box -->
              <div class="p-2 rounded-xl bg-rose-950/40 border border-rose-200">
                <div class="flex items-center gap-1.5 text-[11px] font-bold text-rose-300 mb-1 pb-1 border-b border-rose-200">
                  <UserCheck :size="13" class="text-rose-600" />
                  <span>사람이 해야 할 일</span>
                </div>
                <ul class="space-y-0.5 text-[10px] text-rose-300 font-medium leading-tight">
                  <li v-for="(r, idx) in currentScene.humanRoles" :key="idx" class="flex items-start gap-1">
                    <Check :size="10" class="text-rose-600 shrink-0 mt-0.5" />
                    <span>{{ r }}</span>
                  </li>
                </ul>
              </div>
            </div>

            <div class="text-[9.5px] text-slate-100 font-bold bg-white/8 py-1 px-2 rounded-md text-center">
              "AI는 초안을 만들 수 있지만, 사회복지사의 전문적 판단과 최종 책임은 사람이 집니다."
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
