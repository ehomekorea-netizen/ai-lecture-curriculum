<script setup lang="ts">
import { ref } from 'vue'

const copied = ref(false)
const activeTab = ref<'project1' | 'project2' | 'skills'>('project1')
const showToggleDetail = ref(false)

function copyUrl() {
  navigator.clipboard.writeText('https://milyang-portfolio.notion.site/my-resume').then(() => {
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  })
}
</script>

<template>
  <div class="notion-mockup-wrapper w-full mt-1.5 select-none">
    <!-- Notion Browser Window Mockup -->
    <div class="w-full h-[335px] rounded-2xl bg-white border border-slate-200 shadow-xl flex flex-col overflow-hidden">
      
      <!-- Top Notion Browser Bar -->
      <div class="h-8 bg-slate-100/90 border-b border-slate-200 px-3 flex items-center justify-between flex-shrink-0">
        <!-- Mac Dots -->
        <div class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-400 inline-block" />
          <span class="w-2.5 h-2.5 rounded-full bg-amber-400 inline-block" />
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block" />
        </div>

        <!-- URL Pill with Live Web Publish Badge -->
        <div class="flex items-center gap-2 px-3 py-0.5 rounded-md bg-white border border-slate-200 text-[10.5px] font-mono text-slate-700 shadow-2xs">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
          <span class="text-emerald-700 font-bold">웹에 게시됨</span>
          <span class="text-slate-300">|</span>
          <span class="text-slate-500">https://milyang.notion.site/portfolio</span>
        </div>

        <!-- Copy Link Action -->
        <button
          class="px-2.5 py-0.5 rounded text-[10.5px] font-bold transition-all cursor-pointer border flex items-center gap-1"
          :class="copied ? 'bg-emerald-600 text-white border-emerald-500' : 'bg-white hover:bg-slate-50 text-slate-700 border-slate-300'"
          @click="copyUrl"
        >
          <span>{{ copied ? '✓ 링크 복사됨' : '🔗 공개 링크 복사' }}</span>
        </button>
      </div>

      <!-- Notion Page Content Area (Scrollable Simulation) -->
      <div class="flex-1 overflow-y-auto p-4 bg-white text-slate-800 flex flex-col justify-between">
        
        <!-- 1. Hero Section -->
        <div class="border-b border-slate-100 pb-3">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <!-- Avatar Emoji -->
              <div class="w-10 h-10 rounded-2xl bg-amber-100 border border-amber-200 flex items-center justify-center text-xl shadow-2xs">
                💼
              </div>
              <div>
                <div class="flex items-center gap-2">
                  <h3 class="text-sm font-extrabold text-slate-900 leading-tight m-0">
                    홍길동 | 서비스 기획 &amp; 현장 운영 포트폴리오
                  </h3>
                  <span class="px-1.5 py-0.2 rounded bg-blue-50 text-blue-600 text-[9.5px] font-bold font-mono">
                    4주차 DB 이식 완료
                  </span>
                </div>
                <p class="text-[10.5px] text-slate-500 mt-0.5 m-0">
                  데이터로 문제를 발견하고, 표준 매뉴얼과 디지털 도구로 성과를 만드는 실무자입니다.
                </p>
              </div>
            </div>

            <!-- Contact Badges -->
            <div class="text-right text-[10px] text-slate-400 font-mono space-y-0.5">
              <div>✉️ contact@milyang.kr</div>
              <div>📱 010-1234-5678</div>
            </div>
          </div>
        </div>

        <!-- 2. Interactive STAR Project Cards -->
        <div class="my-2 flex-1">
          <div class="flex items-center justify-between mb-1.5">
            <div class="text-[11px] font-bold text-slate-800 flex items-center gap-1">
              <span>🚀</span>
              <span>핵심 프로젝트 (STAR 문제해결 성과)</span>
            </div>
            <!-- Tab Selector -->
            <div class="flex items-center gap-1">
              <button
                class="px-2 py-0.5 rounded text-[10px] font-bold cursor-pointer transition-colors"
                :class="activeTab === 'project1' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
                @click="activeTab = 'project1'"
              >
                프로젝트 1 (매뉴얼 구축)
              </button>
              <button
                class="px-2 py-0.5 rounded text-[10px] font-bold cursor-pointer transition-colors"
                :class="activeTab === 'project2' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
                @click="activeTab = 'project2'"
              >
                프로젝트 2 (고객 피드백 DB)
              </button>
              <button
                class="px-2 py-0.5 rounded text-[10px] font-bold cursor-pointer transition-colors"
                :class="activeTab === 'skills' ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'"
                @click="activeTab = 'skills'"
              >
                보유 스킬 &amp; 자격
              </button>
            </div>
          </div>

          <!-- Tab 1: Project 1 -->
          <div v-if="activeTab === 'project1'" class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs">
            <div class="flex items-center justify-between mb-1">
              <span class="font-bold text-slate-900 text-[11.5px]">📋 신규 입사자 업무 프로세스 표준 매뉴얼 제작</span>
              <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-bold text-[9.5px]">
                온보딩 소요시간 50% 단축
              </span>
            </div>
            <div class="grid grid-cols-3 gap-2 mt-1.5 text-[10.5px]">
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-rose-600 block text-[9.5px]">Situation &amp; Task</b>
                <span class="text-slate-600">인수인계 문서 부재로 신규 인력 적응에 평균 4주 소요</span>
              </div>
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-blue-600 block text-[9.5px]">Action (해결책)</b>
                <span class="text-slate-600">노션 기반 업무 체크리스트 및 FAQ 30종 표준화 구축</span>
              </div>
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-emerald-600 block text-[9.5px]">Result (정량 성과)</b>
                <span class="text-slate-900 font-bold">적응 기간 4주 ➔ 2주 단축, 업무 오류 0건</span>
              </div>
            </div>

            <!-- Toggle Interaction -->
            <div class="mt-2 pt-1 border-t border-slate-200 flex items-center justify-between text-[10px]">
              <button
                class="text-blue-600 hover:underline cursor-pointer flex items-center gap-1 font-medium"
                @click="showToggleDetail = !showToggleDetail"
              >
                <span>{{ showToggleDetail ? '▼ 상세 프로세스 접기' : '▶ 상세 업무 프로세스 토글 펼치기' }}</span>
              </button>
              <span class="text-slate-400 font-mono">Notion Toggle Block</span>
            </div>
            <div v-if="showToggleDetail" class="mt-1 p-2 rounded bg-white border border-blue-100 text-[10px] text-slate-600">
              1. 1차 부서 인터뷰 ➔ 2. 노션 템플릿 설계 ➔ 3. 현장 실무 피드백 반영 ➔ 4. 전사 배포 완료
            </div>
          </div>

          <!-- Tab 2: Project 2 -->
          <div v-else-if="activeTab === 'project2'" class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs">
            <div class="flex items-center justify-between mb-1">
              <span class="font-bold text-slate-900 text-[11.5px]">📊 고객 VOC 및 피드백 데이터베이스 자동화</span>
              <span class="px-2 py-0.5 rounded-full bg-blue-100 text-blue-800 font-bold text-[9.5px]">
                문의 처리 속도 35% 향상
              </span>
            </div>
            <div class="grid grid-cols-3 gap-2 mt-1.5 text-[10.5px]">
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-rose-600 block text-[9.5px]">Situation &amp; Task</b>
                <span class="text-slate-600">수기 엑셀 기록으로 유형별 불만 원인 분석 지연</span>
              </div>
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-blue-600 block text-[9.5px]">Action (해결책)</b>
                <span class="text-slate-600">노션 관계형 DB로 유형별 태그 및 우선순위 자동 분류</span>
              </div>
              <div class="p-1.5 rounded-lg bg-white border border-slate-200">
                <b class="text-emerald-600 block text-[9.5px]">Result (정량 성과)</b>
                <span class="text-slate-900 font-bold">당일 처리율 92% 달성, 반복 민원 40% 감소</span>
              </div>
            </div>
          </div>

          <!-- Tab 3: Skills -->
          <div v-else class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs">
            <div class="font-bold text-slate-900 text-[11.5px] mb-2">🛠️ 보유 직무 역량 &amp; 툴스택</div>
            <div class="flex flex-wrap gap-1.5">
              <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-[10.5px] font-bold text-slate-800 shadow-2xs">
                📝 Notion (고급 DB 및 웹 퍼블리싱)
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-[10.5px] font-bold text-slate-800 shadow-2xs">
                📊 Excel / 스프레드시트 (피벗테이블, 통계)
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-[10.5px] font-bold text-slate-800 shadow-2xs">
                🎨 Canva / Figma (기획서 &amp; 프로토타입)
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-[10.5px] font-bold text-slate-800 shadow-2xs">
                🤖 생성형 AI 활용 (ChatGPT, Gemini, Manus)
              </span>
            </div>
          </div>
        </div>

        <!-- 3. Bottom Web Publish Info -->
        <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500">
          <span>💡 <b>노션 웹의 핵심</b>: 별도의 코딩 없이 노션 페이지를 링크 하나로 전 세계에 즉시 공유합니다.</span>
          <span class="text-emerald-600 font-bold">No-Code Live Portfolio</span>
        </div>

      </div>

    </div>
  </div>
</template>

<style scoped>
</style>
