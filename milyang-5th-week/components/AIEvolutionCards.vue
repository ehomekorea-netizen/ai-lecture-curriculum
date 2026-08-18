<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const base = import.meta.env.BASE_URL || '/'

const props = defineProps<{
  stage?: number
}>()

// Internal active level (0: LLM, 1: Workflow, 2: Agent)
const activeIndex = ref(0)

// Sync with Slidev $clicks
watch(
  () => props.stage,
  (val) => {
    if (val === undefined || val === null || val <= 0) {
      activeIndex.value = 0
    } else if (val === 1) {
      activeIndex.value = 1
    } else {
      activeIndex.value = 2
    }
  },
  { immediate: true }
)

function selectLevel(idx: number) {
  activeIndex.value = idx
}

const summaryText = computed(() => {
  if (activeIndex.value === 0) {
    return {
      badge: 'LEVEL 1 · 수동 반응형',
      badgeColor: 'bg-blue-100 text-blue-700 border-blue-300',
      icon: '💬',
      desc: '인간이 먼저 질문하지 않으면 아무것도 하지 못하는 "수동형 텍스트 생성기"',
      color: 'text-blue-600'
    }
  } else if (activeIndex.value === 1) {
    return {
      badge: 'LEVEL 2 · 반자동 파이프라인',
      badgeColor: 'bg-amber-100 text-amber-800 border-amber-300',
      icon: '⚙️',
      desc: '인간이 설계한 고정 경로(구글 캘린더 등)로만 달리는 "정해진 철로 위의 기차"',
      color: 'text-amber-700'
    }
  } else {
    return {
      badge: 'LEVEL 3 · 완전 자율 완제품 제작',
      badgeColor: 'bg-emerald-100 text-emerald-800 border-emerald-400 font-bold',
      icon: '🚀',
      desc: '목표만 주면 스스로 길을 찾고 오류를 고쳐 완제품을 납품하는 "자율주행차"',
      color: 'text-emerald-700'
    }
  }
})
</script>

<template>
  <div class="evolution-wrapper mt-0.5">
    <!-- Top Interactive Progress Stepper -->
    <div class="flex items-center justify-between gap-2 p-1.5 bg-slate-100 rounded-xl border border-slate-200 mb-3">
      <button
        class="flex-1 py-1.5 px-3 rounded-lg text-xs font-bold transition-all flex items-center justify-center gap-1.5 cursor-pointer border"
        :class="activeIndex === 0 ? 'bg-blue-600 text-white shadow-md border-blue-600 scale-[1.02]' : 'bg-transparent text-slate-500 border-transparent hover:text-slate-800'"
        @click="selectLevel(0)"
      >
        <span>01</span>
        <span>LLM (대형 언어 모델)</span>
      </button>

      <span class="text-slate-300 font-bold">➔</span>

      <button
        class="flex-1 py-1.5 px-3 rounded-lg text-xs font-bold transition-all flex items-center justify-center gap-1.5 cursor-pointer border"
        :class="activeIndex === 1 ? 'bg-amber-500 text-white shadow-md border-amber-500 scale-[1.02]' : 'bg-transparent text-slate-500 border-transparent hover:text-slate-800'"
        @click="selectLevel(1)"
      >
        <span>02</span>
        <span>AI 워크플로우 (Workflow)</span>
      </button>

      <span class="text-slate-300 font-bold">➔</span>

      <button
        class="flex-1 py-1.5 px-3 rounded-lg text-xs font-bold transition-all flex items-center justify-center gap-1.5 cursor-pointer border"
        :class="activeIndex === 2 ? 'bg-emerald-600 text-white shadow-md border-emerald-600 scale-[1.02]' : 'bg-transparent text-slate-500 border-transparent hover:text-slate-800'"
        @click="selectLevel(2)"
      >
        <span>03</span>
        <span>AI 자율 에이전트 (Agent)</span>
      </button>
    </div>

    <!-- 3 Cards Grid with Spotlight Effect & Tightly-Fitted Logos -->
    <div class="grid grid-cols-3 gap-3.5 items-stretch">
      <!-- 1. LLM -->
      <div
        class="card-box p-3.5 rounded-2xl border transition-all duration-300 flex flex-col justify-between cursor-pointer"
        :class="activeIndex === 0
          ? 'active-card bg-white border-blue-500 ring-4 ring-blue-500/20 shadow-xl scale-[1.03] -translate-y-1'
          : 'dim-card bg-slate-50/80 border-slate-200 opacity-40 grayscale-[40%] scale-[0.97] hover:opacity-75'"
        @click="selectLevel(0)"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono" :class="activeIndex === 0 ? 'bg-blue-100 text-blue-700' : 'bg-slate-200 text-slate-600'">LEVEL 01</span>
            <span class="text-[10.5px] font-semibold" :class="activeIndex === 0 ? 'text-blue-600 font-bold' : 'text-slate-400'">자율도 20%</span>
          </div>
          <h3 class="text-sm font-bold text-slate-900 mb-0.5 opacity-100">1. 대형 언어 모델 (LLM)</h3>
          <p class="text-[11px] text-slate-500 mb-2">방대한 데이터 기반의 텍스트 예측</p>
          
          <div class="space-y-1.5 text-xs text-slate-600">
            <div class="p-2 bg-slate-50 rounded-xl border border-slate-100">
              <b class="text-slate-800 block text-[10.5px] mb-0.5">💬 작동 방식</b>
              <span class="text-[11px] text-slate-600 leading-snug">사용자 입력(프롬프트)에 따라서만 수동적으로 응답</span>
            </div>
            <div class="p-2 bg-red-50 rounded-xl border border-red-100">
              <b class="text-red-600 block text-[10.5px] mb-0.5">⚠️ 핵심 한계</b>
              <span class="text-[11px] text-red-700 leading-snug">인간의 추가 질문 없이는 스스로 아무것도 할 수 없음</span>
            </div>
          </div>
        </div>

        <!-- Level 1 Official Logos (Tightly Cropped, Margin-Free) -->
        <div class="mt-2.5 pt-2 border-t border-slate-100">
          <div class="text-[9px] font-bold font-mono text-slate-400 mb-1.5">REPRESENTATIVE TOOLS</div>
          <div class="grid grid-cols-2 gap-2">
            <!-- ChatGPT -->
            <div class="flex items-center justify-center px-2 py-1 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5">
              <img :src="`${base}img/logos/logo-chatgpt.png`" class="h-6 w-auto object-contain" alt="ChatGPT" />
            </div>

            <!-- Gemini -->
            <div class="flex items-center justify-center px-2 py-1 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5">
              <img :src="`${base}img/logos/logo-gemini.png`" class="h-5.5 w-auto object-contain" alt="Gemini" />
            </div>
          </div>
        </div>
      </div>

      <!-- 2. AI Workflow -->
      <div
        class="card-box p-3.5 rounded-2xl border transition-all duration-300 flex flex-col justify-between cursor-pointer"
        :class="activeIndex === 1
          ? 'active-card bg-white border-amber-500 ring-4 ring-amber-500/20 shadow-xl scale-[1.03] -translate-y-1'
          : 'dim-card bg-slate-50/80 border-slate-200 opacity-40 grayscale-[40%] scale-[0.97] hover:opacity-75'"
        @click="selectLevel(1)"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono" :class="activeIndex === 1 ? 'bg-amber-100 text-amber-800' : 'bg-slate-200 text-slate-600'">LEVEL 02</span>
            <span class="text-[10.5px] font-semibold" :class="activeIndex === 1 ? 'text-amber-600 font-bold' : 'text-slate-400'">자율도 60%</span>
          </div>
          <h3 class="text-sm font-bold text-slate-900 mb-0.5 opacity-100">2. AI 워크플로우 (Workflow)</h3>
          <p class="text-[11px] text-amber-600 font-medium mb-2">LLM + 외부 데이터/도구 연동</p>
          
          <div class="space-y-1.5 text-xs text-slate-600">
            <div class="p-2 bg-slate-50 rounded-xl border border-slate-100">
              <b class="text-slate-800 block text-[10.5px] mb-0.5">⚙️ 작동 방식</b>
              <span class="text-[11px] text-slate-600 leading-snug">설정된 경로(구글 캘린더 등)에서 정보 수집 및 정확한 답변 도출</span>
            </div>
            <div class="p-2 bg-amber-50 rounded-xl border border-amber-100">
              <b class="text-amber-700 block text-[10.5px] mb-0.5">⚠️ 핵심 한계</b>
              <span class="text-[11px] text-amber-800 leading-snug">사전에 정의된 고정 경로만 따르며, 자율적 경로 변경 불가</span>
            </div>
          </div>
        </div>

        <!-- Level 2 Official Logos (Tightly Cropped, Margin-Free) -->
        <div class="mt-2.5 pt-2 border-t border-slate-100">
          <div class="text-[9px] font-bold font-mono text-slate-400 mb-1.5">REPRESENTATIVE TOOLS</div>
          <div class="grid grid-cols-3 gap-1.5">
            <!-- Zapier -->
            <div class="flex items-center justify-center px-1.5 py-1 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5">
              <img :src="`${base}img/logos/logo-zapier.png`" class="h-5 w-auto object-contain" alt="Zapier" />
            </div>

            <!-- n8n -->
            <div class="flex items-center justify-center px-1.5 py-1 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5">
              <img :src="`${base}img/logos/logo-n8n.png`" class="h-5.5 w-auto object-contain" alt="n8n" />
            </div>

            <!-- Dify -->
            <div class="flex items-center justify-center px-1.5 py-1 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5">
              <img :src="`${base}img/logos/logo-dify.png`" class="h-5.5 w-auto object-contain" alt="Dify" />
            </div>
          </div>
        </div>
      </div>

      <!-- 3. AI Agent (Claude Code, Codex, Manus, Meta AI) -->
      <div
        class="card-box p-3.5 rounded-2xl border transition-all duration-300 flex flex-col justify-between cursor-pointer"
        :class="activeIndex === 2
          ? 'active-card bg-gradient-to-b from-emerald-50/50 to-white border-2 border-emerald-500 ring-4 ring-emerald-500/30 shadow-2xl scale-[1.03] -translate-y-1'
          : 'dim-card bg-slate-50/80 border-slate-200 opacity-40 grayscale-[40%] scale-[0.97] hover:opacity-75'"
        @click="selectLevel(2)"
      >
        <div>
          <div class="flex items-center justify-between mb-1.5">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono" :class="activeIndex === 2 ? 'bg-emerald-500 text-white' : 'bg-slate-200 text-slate-600'">LEVEL 03</span>
            <span class="text-[10.5px] font-bold" :class="activeIndex === 2 ? 'text-emerald-600' : 'text-slate-400'">완전 자율 100%</span>
          </div>
          <h3 class="text-sm font-bold text-emerald-950 mb-0.5 opacity-100">3. AI 자율 에이전트 (Agent)</h3>
          <p class="text-[11px] text-emerald-600 font-semibold mb-2">스스로 계획하고 실행하는 완제품 제작자</p>
          
          <div class="space-y-1.5 text-xs text-slate-600">
            <div class="p-2 bg-emerald-50/80 rounded-xl border border-emerald-100">
              <b class="text-emerald-800 block text-[10.5px] mb-0.5">🎯 작동 방식</b>
              <span class="text-[11px] text-emerald-900 leading-snug">목표만 주면 최적의 접근법을 <b>스스로 계획·관찰·수정·완수</b></span>
            </div>
            <div class="p-2 bg-emerald-50/80 rounded-xl border border-emerald-100">
              <b class="text-emerald-800 block text-[10.5px] mb-0.5">✨ 결정적 차이</b>
              <span class="text-[11px] text-emerald-900 leading-snug">오류 발생 시 스스로 셀프 피드백하여 버그 해결 후 납품</span>
            </div>
          </div>
        </div>

        <!-- Level 3 Official Logos (4 Logos, Tightly Cropped, Margin-Free) -->
        <div class="mt-2.5 pt-2 border-t border-emerald-100">
          <div class="text-[9px] font-bold font-mono text-emerald-700 mb-1.5">REPRESENTATIVE AGENTS</div>
          <div class="grid grid-cols-2 gap-1.5">
            <!-- 1. Claude Code -->
            <div class="flex items-center justify-center px-1.5 py-0.5 bg-black rounded-lg border border-zinc-800 shadow-2xs h-8.5 overflow-hidden">
              <img :src="`${base}img/logos/logo-claude-code.png`" class="h-6.5 w-auto object-contain" alt="Claude Code" />
            </div>

            <!-- 2. Codex -->
            <div class="flex items-center justify-center px-1.5 py-0.5 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5 overflow-hidden">
              <img :src="`${base}img/logos/logo-codex.png`" class="h-5.5 w-auto object-contain" alt="Codex" />
            </div>

            <!-- 3. Manus -->
            <div class="flex items-center justify-center px-1.5 py-0.5 bg-white rounded-lg border border-slate-200 shadow-2xs h-8.5 overflow-hidden">
              <img :src="`${base}img/logos/logo-manus.png`" class="h-5.5 w-auto object-contain" alt="Manus" />
            </div>

            <!-- 4. Meta AI -->
            <div class="flex items-center justify-center px-1.5 py-0.5 bg-black rounded-lg border border-zinc-800 shadow-2xs h-8.5 overflow-hidden">
              <img :src="`${base}img/logos/logo-meta-ai.png`" class="h-5 w-auto object-contain" alt="Meta AI" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Dynamic Bottom Callout Banner -->
    <div class="mt-3 p-2.5 rounded-xl border bg-white shadow-sm flex items-center transition-all duration-300 border-slate-200">
      <div class="flex items-center gap-2">
        <span class="text-base">{{ summaryText.icon }}</span>
        <span class="px-2 py-0.5 rounded text-[10px] font-bold border" :class="summaryText.badgeColor">
          {{ summaryText.badge }}
        </span>
        <span class="text-xs text-slate-700 font-medium">
          {{ summaryText.desc }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-box {
  min-height: 280px;
}
.active-card {
  z-index: 10;
}
.dim-card {
  filter: blur(0.2px);
}
</style>
