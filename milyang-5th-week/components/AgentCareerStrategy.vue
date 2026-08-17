<script setup lang="ts">
const skills = [
  {
    num: '01',
    title: '업무 프로세스 설계 능력',
    eng: 'Process Design',
    icon: '📐',
    desc: '단순 프롬프트 작성을 넘어, 업무의 <b>전체 단계와 데이터 흐름을 논리적으로 쪼개고 구조화</b>하는 능력'
  },
  {
    num: '02',
    title: '비판적 검증 & 조향 능력',
    eng: 'Critical Evaluation',
    icon: '🔍',
    desc: 'Agent가 생성한 결과물과 데이터의 정확성을 팩트체크하고, <b>환각(Hallucination)을 감지하여 올바른 방향으로 핸들을 트는 능력</b>'
  },
  {
    num: '03',
    title: '에이전트 툴 활용 & 적응력',
    eng: 'Tool Adoption',
    icon: '🛠️',
    desc: '<b>Codex, Claude Code, Manus, Gemini</b> 등 최신 AI 에이전트 도구를 내 직무 목적에 맞게 빠르게 습득하고 활용하는 능력'
  }
]
</script>

<template>
  <div class="career-strategy mt-1">
    <!-- 3 Core Competency Cards Grid -->
    <div class="grid grid-cols-3 gap-3.5 items-stretch">
      <div
        v-for="s in skills"
        :key="s.num"
        class="p-3.5 bg-white rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between hover:border-blue-500 hover:shadow-md transition-all"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-50 text-blue-600 text-[10px] font-bold font-mono">
              COMPETENCY {{ s.num }}
            </span>
            <span class="text-sm">{{ s.icon }}</span>
          </div>

          <!-- Title -->
          <h3 class="text-sm font-bold text-slate-900 mb-0.5 leading-tight opacity-100">
            {{ s.title }}
          </h3>
          <p class="text-[10px] font-mono text-slate-400 font-semibold mb-2">
            {{ s.eng }}
          </p>

          <!-- Description -->
          <p class="text-xs text-slate-600 leading-relaxed m-0" v-html="s.desc" />
        </div>

        <!-- Footer Tag -->
        <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-[10px]">
          <span class="text-slate-400">요구 수준</span>
          <b class="text-blue-600 font-bold">신입 필수 핵심 역량</b>
        </div>
      </div>
    </div>

    <!-- Bottom Session 1 Summary Banner -->
    <div class="mt-3 p-3 rounded-2xl bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 text-white shadow-md border border-slate-700 flex items-center justify-between">
      <div class="space-y-0.5">
        <div class="text-[10px] font-bold font-mono text-emerald-400 uppercase tracking-wide">
          DAY 2 · SESSION 1 KEY TAKEAWAY
        </div>
        <div class="text-xs text-slate-200">
          "미래 취업 시장의 핵심은 AI 사용자가 아니라, <b>AI 에이전트에게 일을 어떻게 나누어 맡길 것인가(위임 & 설계)</b>입니다."
        </div>
      </div>
      <div class="flex-shrink-0 px-3 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow-sm">
        Next ➔ Session 2 실전 바이브 코딩
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
