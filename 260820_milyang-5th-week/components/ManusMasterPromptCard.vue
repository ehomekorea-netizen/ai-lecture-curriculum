<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref(0)
const copied = ref(false)

const prompts = [
  {
    id: 'master',
    tag: '추천 · 만능 통합형',
    title: '🌟 노션 DB + PDF + 수료증 사진 통합 완제품 프롬프트',
    subtitle: '폴더 내 모든 이종(異種) 에셋을 에이전트가 알아서 파싱하여 모던 인터랙티브 웹을 제작하는 마스터 공식',
    promptText: `[목표]: 현재 작업 폴더에 들어있는 모든 에셋(노션 백업 문서, 포트폴리오 PDF, 자격증/수료증 이미지, 프로필 사진)을 스스로 분석하여, 나를 기업 담당자에게 가장 매력적으로 어필할 수 있는 모던 인터랙티브 원페이지 웹 포트폴리오(index.html)를 제작해줘.

[작업 절차 (Plan Mode)]:
1. 폴더 내 모든 텍스트(노션 .md/.csv) 및 PDF 문서를 읽어 나의 핵심 직무 강점, 경력 타임라인, 프로젝트별 정량적 성과(숫자/지표)를 구조화해줘.
2. 폴더 내 이미지 에셋(profile.jpg, 수료증 사진 등)의 파일명을 확인하고, About 섹션 및 Certificate 자격 증빙 카드에 정확히 연동해줘.
3. 디자인: 세련된 다크/라이트 듀얼 톤, 모던 타이포그래피, 부드러운 스크롤 애니메이션, 프로젝트 클릭 시 팝업되는 모달(Modal)창을 구현해줘.
4. 산출물: 외부 의존성 없이 단독 실행 가능한 단일 'index.html' 완제품으로 생성하고 가상 브라우저로 렌더링을 검증해줘.`
  },
  {
    id: 'notion',
    tag: '노션 사용자용',
    title: '📄 노션 데이터베이스(DB) & 경력 정리 기반 프롬프트',
    subtitle: '노션에서 내보낸 Markdown/CSV 파일의 테이블 구조를 웹 카드로 완벽 변환',
    promptText: `[목표]: 폴더에 저장된 노션(Notion) 내보내기 데이터(.md, .csv)를 기반으로, 나의 업무 역량과 프로젝트 히스토리가 한눈에 들어오는 인터랙티브 커리어 대시보드 웹페이지(index.html)를 만들어줘.

[세부 지시사항]:
1. 노션 데이터의 태그(스킬셋), 진행 기간, 핵심 기여도를 파싱하여 필터링 가능한 프로젝트 카드 그리드를 구성해줘.
2. 각 프로젝트 카드 호버 시 하이라이트 애니메이션 및 상세 내용 보기 모달창을 탑재해줘.
3. 상단에는 나를 소개하는 강력한 한 줄 헤드라인과 핵심 역량 칩(Badge)을 배치해줘.
4. 모바일 및 PC 브라우저에 모두 최적화된 반응형 단일 HTML 파일로 완성해줘.`
  },
  {
    id: 'assets',
    tag: 'PDF & 수료증 보유자용',
    title: '📜 PDF 이력서 & 수료증/자격증 이미지 갤러리형 프롬프트',
    subtitle: '스캔된 수료증 사진과 PDF 포트폴리오를 웹 갤러리 형태로 시각화',
    promptText: `[목표]: 현재 폴더의 포트폴리오 PDF 문서와 수료증/자격증 이미지 파일들을 분석하여, 나의 신뢰도를 극대화하는 '증빙 갤러리형' 반응형 포트폴리오 웹사이트를 구축해줘.

[세부 지시사항]:
1. PDF 문서를 스캔하여 나의 학력, 교육 이수 내역, 수상 경력을 시간순 타임라인으로 정리해줘.
2. 폴더의 수료증/자격증 이미지들을 라이트박스(Lightbox) 확대 기능이 있는 신뢰도 증빙 갤러리 섹션으로 구성해줘.
3. 프로필 이미지를 상단 Hero 섹션에 깔끔한 원형 프레임으로 배치하고 연락처(이메일/깃허브/링크드인) 버튼을 만들어줘.
4. 가상 브라우저에서 이미지 로딩과 레이아웃을 자체 검증한 뒤 단일 index.html 파일로 출력해줘.`
  }
]

function copyCurrentPrompt() {
  const text = prompts[activeTab.value].promptText
  navigator.clipboard.writeText(text).then(() => {
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  })
}
</script>

<template>
  <div class="manus-prompt-card-wrapper w-full mt-1">
    <!-- Top Preset Tabs & Copy Button -->
    <div class="flex items-center justify-between gap-2 mb-2">
      <!-- Tabs -->
      <div class="flex items-center gap-1.5 p-1 bg-slate-100/90 rounded-xl border border-slate-200">
        <button
          v-for="(p, idx) in prompts"
          :key="p.id"
          class="px-2.5 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer border select-none"
          :class="activeTab === idx ? 'bg-slate-900 text-white border-slate-800 shadow-xs' : 'bg-transparent text-slate-600 border-transparent hover:bg-white hover:text-slate-900'"
          @click="activeTab = idx"
        >
          <span>{{ p.tag }}</span>
        </button>
      </div>

      <!-- Copy Action Button -->
      <button
        class="px-3.5 py-1.5 rounded-xl font-bold text-xs transition-all cursor-pointer flex items-center gap-1.5 shadow-sm border"
        :class="copied ? 'bg-emerald-600 text-white border-emerald-500 scale-105' : 'bg-blue-600 hover:bg-blue-700 text-white border-blue-500'"
        @click="copyCurrentPrompt"
      >
        <span>{{ copied ? '✅ 프롬프트 복사 완료!' : '📋 실습 프롬프트 전체 복사' }}</span>
      </button>
    </div>

    <!-- Main Prompt Display Area -->
    <div class="p-3.5 bg-slate-950 rounded-2xl border border-slate-800 shadow-xl text-white font-mono flex flex-col justify-between h-[285px]">
      <div>
        <!-- Prompt Header -->
        <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-2">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
            <span class="text-xs font-bold text-slate-200 font-sans">{{ prompts[activeTab].title }}</span>
          </div>
          <span class="text-[10px] text-slate-500 font-sans">Manus Plan Mode 최적화</span>
        </div>

        <!-- Prompt Content Box -->
        <div class="overflow-y-auto max-h-[190px] pr-1.5 text-xs text-slate-300 leading-relaxed space-y-1.5 select-text font-mono">
          <pre class="whitespace-pre-wrap font-mono text-[11px] text-slate-200 bg-slate-900/80 p-2.5 rounded-xl border border-slate-800/80 leading-snug">{{ prompts[activeTab].promptText }}</pre>
        </div>
      </div>

      <!-- Bottom Insight Pill -->
      <div class="pt-2 border-t border-slate-800 flex items-center justify-between text-[10.5px] text-slate-400 font-sans">
        <div class="flex items-center gap-1.5">
          <span class="text-amber-400 font-bold">💡 강사 팁:</span>
          <span>수강생들에게 폴더에 에셋을 넣은 후, <b>위 프롬프트를 그대로 복사해 Manus에 전송</b>하도록 안내하세요.</span>
        </div>
        <span class="text-emerald-400 font-mono font-bold">100% Zero Manual Coding</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
