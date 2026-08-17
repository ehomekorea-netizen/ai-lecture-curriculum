<script setup lang="ts">
import { ref } from 'vue'

const activeStep = ref<number | null>(null)

const steps = [
  {
    step: '01',
    icon: '📄',
    title: '노션 DB ➔ PDF 추출',
    tag: '4주차 자산 활용',
    borderClass: 'border-blue-500 ring-2 ring-blue-500/20 bg-blue-50/40',
    desc: '4주차에 구축한 노션 경험 DB를 <b>GPT 플러그인과 연동하여 구조화된 PDF 이력서로 다운로드</b>합니다.',
    bullets: ['4주차 노션 경험 DB 연동', 'GPT로 깔끔한 PDF 즉시 추출']
  },
  {
    step: '02',
    icon: '🔑',
    title: '가입 & 데스크탑 설치',
    tag: '로컬 환경 구축',
    borderClass: 'border-indigo-500 ring-2 ring-indigo-500/20 bg-indigo-50/40',
    desc: 'manus.im 가입 후 내 PC의 로컬 폴더를 직접 제어할 수 있는 <b>Manus Desktop 앱을 설치</b>합니다.',
    bullets: ['manus.im 계정 생성', 'Manus Desktop 앱 구동']
  },
  {
    step: '03',
    icon: '📁',
    title: '로컬 에셋 폴더 세팅',
    tag: '데이터 집결',
    borderClass: 'border-amber-500 ring-2 ring-amber-500/20 bg-amber-50/40',
    desc: '다운받은 <b>PDF 이력서와 수료증/자격증 사진, 프로필 이미지</b>를 `my-portfolio` 폴더에 모읍니다.',
    bullets: ['my-portfolio 폴더 생성', 'PDF + 수료증 사진 모두 투입']
  },
  {
    step: '04',
    icon: '🧠',
    title: 'Plan 모드 기획',
    tag: '에셋 자동 분석',
    borderClass: 'border-purple-500 ring-2 ring-purple-500/20 bg-purple-50/40',
    desc: '<b>[Plan Mode]</b>를 켜면 에이전트가 폴더 내 모든 에셋을 스스로 분석하여 웹사이트 구조를 기획합니다.',
    bullets: ['에셋 내용 자체 스캔', '웹사이트 구조(Sitemap) 설계']
  },
  {
    step: '05',
    icon: '🚀',
    title: '한 줄로 완제품 빌드',
    tag: '100% 자율 완성',
    borderClass: 'border-emerald-500 ring-2 ring-emerald-500/20 bg-emerald-50/40',
    desc: '<b>단 한 줄의 자연어 프롬프트</b>를 전송하면, 브라우저 검증까지 마친 반응형 웹 포트폴리오가 완성됩니다.',
    bullets: ['한 줄 프롬프트 전송', '단일 index.html 완제품 출력']
  }
]
</script>

<template>
  <div class="manus-clean-workflow w-full mt-3 select-none">
    <!-- 5 Steps Connected Horizontal Grid Cards (Spacious & Clean) -->
    <div class="grid grid-cols-5 gap-3 items-stretch h-[315px]">
      <div
        v-for="(s, idx) in steps"
        :key="s.step"
        class="p-3.5 bg-white rounded-2xl border transition-all duration-300 shadow-xs flex flex-col justify-between cursor-pointer hover:shadow-md hover:border-slate-400"
        :class="activeStep === idx ? s.borderClass + ' scale-[1.02] shadow-lg' : 'border-slate-200'"
        @mouseenter="activeStep = idx"
        @mouseleave="activeStep = null"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="text-2xl p-1.5 rounded-xl bg-slate-100/90 leading-none">{{ s.icon }}</span>
            <span class="px-2.5 py-0.5 rounded text-[10.5px] font-mono font-extrabold bg-slate-900 text-white">
              STEP {{ s.step }}
            </span>
          </div>

          <!-- Title & Subtitle -->
          <h3 class="text-sm font-bold text-slate-900 mb-0.5 leading-tight opacity-100">
            {{ s.title }}
          </h3>
          <span class="inline-block text-[10px] font-mono font-bold text-blue-600 mb-2">
            {{ s.tag }}
          </span>

          <!-- Description -->
          <p class="text-[10.5px] text-slate-600 leading-snug m-0 mb-2" v-html="s.desc" />
        </div>

        <!-- Bullets -->
        <div class="pt-2 border-t border-slate-100 space-y-1.5 text-[10px] text-slate-500 font-medium">
          <div v-for="(b, bIdx) in s.bullets" :key="bIdx" class="flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-blue-500 flex-shrink-0" />
            <span class="truncate">{{ b }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
