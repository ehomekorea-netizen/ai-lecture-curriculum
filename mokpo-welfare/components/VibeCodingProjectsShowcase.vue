<script setup lang="ts">
import { ExternalLink, Folder, Sparkles } from 'lucide-vue-next'

const projects = [
  {
    id: 'lecture-payment',
    kicker: 'LECTURER FINANCIAL PORTAL',
    title: '출강바이브',
    url: 'https://lecture-payment-dashboard.vercel.app/',
    isHero: true,
    specs: [
      'Vite & Tailwind CSS 기반 초경량 빌드',
      '세율 공제 및 교통비 개별 합산 알고리즘',
      '동적 스크롤 인디케이터 반응형 물리 모션'
    ],
    prd: '여러 기관에 출강하는 프리랜서 강사들을 위해 최적화된 스마트 정산 대시보드입니다. 강의 기관마다 주강사/보조강사 여부, 세율, 교통비 지급 조건 등이 달라 매월 수동으로 복잡하게 정산하던 고충을 해결하기 위해 개발되었습니다. 날짜별 수업 명세만 입력하면 최종 수령액을 자동 산출하고 월별 추이를 차트로 나타냅니다.',
    tags: ['Vite', 'Tailwind CSS', 'Vanilla JS']
  },
  {
    id: 'biblegram',
    kicker: 'DAILY LIFE PWA',
    title: '바이블그램',
    url: 'https://biblegram.vercel.app/',
    isHero: false,
    prd: '바쁜 현대인들이 상쾌한 아침을 성경 말씀과 함께 차분하게 시작할 수 있도록 설계된 아침 푸시 알림 PWA 서비스입니다. 매일 오전 지정된 시간에 영성 카드를 알림으로 전송하며, 마음에 드는 구절 카드를 터치해 이미지 파일로 손쉽게 내려받아 소장 및 소셜 채널로 공유할 수 있도록 기획되었습니다.',
    tags: ['PWA', 'Vercel Cron', 'Web Push API']
  },
  {
    id: 'danggeun',
    kicker: 'COMMUNITY SHARING BOARDS',
    title: 'HEAT Carrot',
    url: 'https://danggeun-dashboard.vercel.app/',
    isHero: false,
    prd: '지역 주민들의 온기 있는 당근 모임과 거래를 통해 쌓인 기부 적립 현황을 실시간으로 게시하는 실시간 현황 모니터입니다. 주민들이 스스로 기부 참여 현황을 투명하게 확인하고 성과를 공유함으로써 지역 기부 문화를 더욱 활성화하기 위해 기획되었습니다. Next.js와 노션 연동을 통해 데이터를 상시 자동 업데이트합니다.',
    tags: ['Next.js', 'Notion SDK', 'Dual Monitor Mod']
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[335px] my-auto py-0.5 space-y-2.5">
    <!-- ── 1. Top Hero Card: 출강바이브 (Full Width) ── -->
    <div class="bg-white rounded-2xl border border-slate-200/90 p-3.5 px-5 shadow-2xs flex flex-col justify-between">
      <div>
        <!-- Card Header -->
        <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-slate-100">
          <div>
            <span class="text-[9px] font-mono font-bold text-slate-400 uppercase tracking-widest block">
              {{ projects[0].kicker }}
            </span>
            <h3 class="text-base md:text-lg font-bold font-serif text-slate-900 leading-tight">
              {{ projects[0].title }}
            </h3>
          </div>

          <div class="flex items-center gap-1.5">
            <span class="p-1 rounded-md bg-slate-50 text-slate-400 border border-slate-200/60">
              <Folder :size="13" />
            </span>
            <a
              :href="projects[0].url"
              target="_blank"
              rel="noopener noreferrer"
              class="p-1 rounded-md bg-blue-50 text-blue-600 hover:bg-blue-600 hover:text-white border border-blue-200 transition-colors flex items-center justify-center cursor-pointer shadow-2xs"
              title="라이브 사이트 바로가기"
            >
              <ExternalLink :size="13" />
            </a>
          </div>
        </div>

        <!-- Card Body: 2-Column Split (Spec vs PRD) -->
        <div class="grid grid-cols-12 gap-4 text-left">
          <!-- Left: App Specification -->
          <div class="col-span-5 space-y-1">
            <span class="text-[9.5px] font-mono font-bold text-slate-400 uppercase tracking-wider block">
              APP SPECIFICATION
            </span>
            <ul class="text-[10.5px] text-slate-600 space-y-0.5 leading-snug pl-3 list-disc">
              <li v-for="spec in projects[0].specs" :key="spec">
                {{ spec }}
              </li>
            </ul>
          </div>

          <!-- Right: PRD -->
          <div class="col-span-7 space-y-1">
            <span class="text-[9.5px] font-mono font-bold text-slate-400 uppercase tracking-wider block">
              기획 의도 (PRD)
            </span>
            <p class="text-[10.5px] text-slate-600 leading-snug break-keep">
              {{ projects[0].prd }}
            </p>
          </div>
        </div>
      </div>

      <!-- Card Footer Tags -->
      <div class="flex items-center gap-1.5 pt-1.5 mt-1 border-t border-slate-100">
        <span
          v-for="tag in projects[0].tags"
          :key="tag"
          class="px-2 py-0.5 rounded-md bg-slate-100/80 text-slate-600 text-[9.5px] font-mono font-medium border border-slate-200/60"
        >
          {{ tag }}
        </span>
      </div>
    </div>

    <!-- ── 2. Bottom 2 Split Cards: 바이블그램 & HEAT Carrot ── -->
    <div class="grid grid-cols-2 gap-3">
      <!-- Card 2: 바이블그램 -->
      <div class="bg-white rounded-2xl border border-slate-200/90 p-3 px-4 shadow-2xs flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-1 pb-1 border-b border-slate-100">
            <div>
              <span class="text-[8.5px] font-mono font-bold text-slate-400 uppercase tracking-widest block">
                {{ projects[1].kicker }}
              </span>
              <h4 class="text-sm font-bold font-serif text-slate-900 leading-tight">
                {{ projects[1].title }}
              </h4>
            </div>

            <div class="flex items-center gap-1">
              <span class="p-0.8 rounded-md bg-slate-50 text-slate-400 border border-slate-200/60">
                <Folder :size="12" />
              </span>
              <a
                :href="projects[1].url"
                target="_blank"
                rel="noopener noreferrer"
                class="p-0.8 rounded-md bg-blue-50 text-blue-600 hover:bg-blue-600 hover:text-white border border-blue-200 transition-colors flex items-center justify-center cursor-pointer shadow-2xs"
                title="라이브 사이트 바로가기"
              >
                <ExternalLink :size="12" />
              </a>
            </div>
          </div>

          <!-- PRD Content -->
          <div class="space-y-0.5 my-1">
            <span class="text-[9px] font-mono font-bold text-slate-400 uppercase tracking-wider block">
              기획 의도 (PRD)
            </span>
            <p class="text-[10px] text-slate-600 leading-snug break-keep line-clamp-3">
              {{ projects[1].prd }}
            </p>
          </div>
        </div>

        <!-- Tags -->
        <div class="flex items-center gap-1 pt-1 border-t border-slate-100">
          <span
            v-for="tag in projects[1].tags"
            :key="tag"
            class="px-1.5 py-0.2 rounded bg-slate-100/80 text-slate-600 text-[9px] font-mono font-medium border border-slate-200/60"
          >
            {{ tag }}
          </span>
        </div>
      </div>

      <!-- Card 3: HEAT Carrot -->
      <div class="bg-white rounded-2xl border border-slate-200/90 p-3 px-4 shadow-2xs flex flex-col justify-between">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-1 pb-1 border-b border-slate-100">
            <div>
              <span class="text-[8.5px] font-mono font-bold text-slate-400 uppercase tracking-widest block">
                {{ projects[2].kicker }}
              </span>
              <h4 class="text-sm font-bold font-serif text-slate-900 leading-tight">
                {{ projects[2].title }}
              </h4>
            </div>

            <div class="flex items-center gap-1">
              <span class="p-0.8 rounded-md bg-slate-50 text-slate-400 border border-slate-200/60">
                <Folder :size="12" />
              </span>
              <a
                :href="projects[2].url"
                target="_blank"
                rel="noopener noreferrer"
                class="p-0.8 rounded-md bg-blue-50 text-blue-600 hover:bg-blue-600 hover:text-white border border-blue-200 transition-colors flex items-center justify-center cursor-pointer shadow-2xs"
                title="라이브 사이트 바로가기"
              >
                <ExternalLink :size="12" />
              </a>
            </div>
          </div>

          <!-- PRD Content -->
          <div class="space-y-0.5 my-1">
            <span class="text-[9px] font-mono font-bold text-slate-400 uppercase tracking-wider block">
              기획 의도 (PRD)
            </span>
            <p class="text-[10px] text-slate-600 leading-snug break-keep line-clamp-3">
              {{ projects[2].prd }}
            </p>
          </div>
        </div>

        <!-- Tags -->
        <div class="flex items-center gap-1 pt-1 border-t border-slate-100">
          <span
            v-for="tag in projects[2].tags"
            :key="tag"
            class="px-1.5 py-0.2 rounded bg-slate-100/80 text-slate-600 text-[9px] font-mono font-medium border border-slate-200/60"
          >
            {{ tag }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
