<script setup lang="ts">
import {
  Smartphone,
  ArrowUpRight
} from 'lucide-vue-next'

interface ProjectItem {
  id: string
  title: string
  kicker: string
  url: string
  badge: string
  badgeType: 'mobile' | 'desktop'
  desc: string
  tags: string[]
}

const projects: ProjectItem[] = [
  {
    id: 'lecture-payment',
    title: '출강바이브',
    kicker: 'LECTURER FINANCIAL PORTAL',
    url: 'https://lecture-payment-dashboard.vercel.app/',
    badge: 'PWA App',
    badgeType: 'mobile',
    desc: '프리랜서 강사를 위한 스마트 정산 PWA 대시보드',
    tags: ['Vite', 'Tailwind CSS', 'PWA']
  },
  {
    id: 'biblegram',
    title: '바이블그램',
    kicker: 'DAILY LIFE DEVOTIONAL PWA',
    url: 'https://biblegram.vercel.app/',
    badge: 'Push Web',
    badgeType: 'mobile',
    desc: '매일 아침 성경 구절 푸시 알림 및 영성 카드 PWA',
    tags: ['Next.js', 'Vercel Cron', 'Web Push']
  },
  {
    id: 'danggeun',
    title: 'HEAT Carrot',
    kicker: 'COMMUNITY SHARING BOARDS',
    url: 'https://danggeun-dashboard.vercel.app/',
    badge: 'Live Monitor',
    badgeType: 'desktop',
    desc: '당근 모임 기부 적립 현황 실시간 모니터 대시보드',
    tags: ['Next.js', 'Notion SDK', 'Live Monitor']
  }
]
</script>

<template>
  <div class="relative w-full h-[335px] my-auto select-none font-sans overflow-hidden flex flex-col justify-between py-1">
    <!-- ── 3 Direct New-Tab Link Cards (3-Column Grid) ── -->
    <div class="grid grid-cols-3 gap-3.5 h-full items-stretch">
      <!-- ── 1. 출강바이브 Card (High Contrast Apple Dark Glass) ── -->
      <a
        :href="projects[0].url"
        target="_blank"
        rel="noopener noreferrer"
        class="group relative bg-white/5 rounded-2xl border border-white/12 p-3.5 px-4 shadow-xl hover:shadow-2xl hover:border-amber-400/80 hover:-translate-y-1 transition-all cursor-pointer flex flex-col justify-between text-left no-underline block backdrop-blur-sm"
      >
        <div>
          <!-- Top Badge & Device Tag -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
            <span class="text-[9px] font-mono font-bold text-amber-400 uppercase tracking-wider">
              01 · LECTURER PORTAL
            </span>
            <span class="flex items-center gap-1 text-[9.5px] font-mono bg-amber-950/70 text-amber-300 border border-amber-400/50 px-2 py-0.5 rounded-md font-bold">
              <Smartphone :size="10" /> PWA App
            </span>
          </div>

          <!-- Visual App Identity Box -->
          <div class="p-3 rounded-xl bg-black/60 border border-white/10 shadow-inner text-center space-y-1.5 mb-2">
            <!-- Coin Badge -->
            <div class="w-10 h-10 mx-auto rounded-full bg-gradient-to-tr from-amber-400 to-yellow-300 flex items-center justify-center text-slate-950 text-lg font-black shadow-md ring-2 ring-amber-400/60 group-hover:scale-110 transition-transform">
              ₩
            </div>
            <h4 class="text-base font-bold font-serif text-white m-0 tracking-tight">출강바이브</h4>
            <p class="text-[10px] text-slate-200 leading-snug m-0 break-keep font-medium">
              홈 화면에 추가하고 매일 편리하게 정산 현황을 관리하세요.
            </p>
          </div>

          <!-- Micro Guide Pill -->
          <div class="p-2 rounded-lg bg-amber-950/40 border border-amber-400/40 text-[10px] text-amber-200 space-y-0.5">
            <div class="font-bold flex items-center gap-1">
              <span class="inline-flex items-center gap-1"><Download :size="11" class="text-amber-300" /><span>[홈화면에 추가]</span></span>
              <span class="text-amber-300 font-normal">누르면 끝!</span>
            </div>
            <p class="text-[9px] text-slate-300 leading-tight m-0">
              세율 공제 및 교통비 자동 정산 알고리즘
            </p>
          </div>
        </div>

        <!-- Open New Tab Button -->
        <div class="pt-2 border-t border-white/10 flex items-center justify-between">
          <span class="text-[11px] font-bold text-amber-300 flex items-center gap-1 group-hover:text-amber-200">
            <span>라이브 서비스 바로가기</span>
            <ArrowUpRight :size="13" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </span>
          <span class="text-[9.5px] text-slate-400 font-mono">새 탭 ↗</span>
        </div>
      </a>

      <!-- ── 2. 바이블그램 Card ── -->
      <a
        :href="projects[1].url"
        target="_blank"
        rel="noopener noreferrer"
        class="group relative bg-white/5 rounded-2xl border border-white/12 p-3.5 px-4 shadow-xl hover:shadow-2xl hover:border-indigo-400/80 hover:-translate-y-1 transition-all cursor-pointer flex flex-col justify-between text-left no-underline block backdrop-blur-sm"
      >
        <div>
          <!-- Top Badge -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
            <span class="text-[9px] font-mono font-bold text-indigo-400 uppercase tracking-wider">
              02 · DAILY LIFE PWA
            </span>
            <span class="flex items-center gap-1 text-[9.5px] font-mono bg-indigo-950/70 text-indigo-300 border border-indigo-400/50 px-2 py-0.5 rounded-md font-bold">
              <Smartphone :size="10" /> Push Web
            </span>
          </div>

          <!-- Sanctum Visual Card -->
          <div class="relative p-2.5 rounded-xl bg-black/60 border border-white/10 shadow-inner overflow-hidden mb-2">
            <div class="text-[8.5px] font-mono font-bold text-indigo-300 tracking-widest text-center uppercase mb-1">
              LIGHT OF WORD
            </div>
            <p class="text-[10.5px] text-slate-100 font-serif leading-relaxed text-center break-keep m-0 px-1 font-medium">
              "나의 반석이시요 나의 구속자이신 여호와여, 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를..."
            </p>
            <div class="text-[9px] text-indigo-300 text-center font-serif mt-1 font-bold">
              (시편 19:14)
            </div>
          </div>

          <!-- Feature Tag List -->
          <div class="p-2 rounded-lg bg-indigo-950/40 border border-indigo-400/40 text-[10px] text-indigo-200 space-y-0.5">
            <div class="font-bold text-indigo-300">
              <Bell :size="12" class="inline text-indigo-300 mr-1" />매일 아침 7시 성경 말씀 푸시
            </div>
            <p class="text-[9px] text-slate-300 leading-tight m-0">
              바쁜 현대인을 위한 영성 묵상 카드 PWA
            </p>
          </div>
        </div>

        <!-- Open New Tab Button -->
        <div class="pt-2 border-t border-white/10 flex items-center justify-between">
          <span class="text-[11px] font-bold text-indigo-300 flex items-center gap-1 group-hover:text-indigo-200">
            <span>라이브 서비스 바로가기</span>
            <ArrowUpRight :size="13" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </span>
          <span class="text-[9.5px] text-slate-400 font-mono">새 탭 ↗</span>
        </div>
      </a>

      <!-- ── 3. HEAT Carrot Card ── -->
      <a
        :href="projects[2].url"
        target="_blank"
        rel="noopener noreferrer"
        class="group relative bg-white/5 rounded-2xl border border-white/12 p-3.5 px-4 shadow-xl hover:shadow-2xl hover:border-orange-400/80 hover:-translate-y-1 transition-all cursor-pointer flex flex-col justify-between text-left no-underline block backdrop-blur-sm"
      >
        <div>
          <!-- Top Badge -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-white/10">
            <span class="text-[9px] font-mono font-bold text-orange-400 uppercase tracking-wider">
              03 · LIVE MONITOR
            </span>
            <span class="flex items-center gap-1 text-[9.5px] font-mono bg-orange-950/70 text-orange-300 border border-orange-400/50 px-2 py-0.5 rounded-md font-bold">
              <span>⚡ Live Monitor</span>
            </span>
          </div>

          <!-- Heat Thermometer Visual Box -->
          <div class="p-3 rounded-xl bg-black/60 border border-white/10 shadow-inner text-center space-y-1.5 mb-2">
            <div class="w-10 h-10 mx-auto rounded-full bg-gradient-to-tr from-orange-500 to-amber-400 flex items-center justify-center text-white text-lg font-black shadow-md ring-2 ring-orange-400/60 group-hover:scale-110 transition-transform">
              <span class="text-sm font-bold text-orange-400">🥕</span>
            </div>
            <h4 class="text-base font-bold font-serif text-white m-0 tracking-tight">HEAT Carrot</h4>
            <p class="text-[10px] text-slate-200 leading-snug m-0 break-keep font-medium">
              당근 모임 기부 적립 현황 실시간 모니터 대시보드
            </p>
          </div>

          <!-- Real-time Live Badge -->
          <div class="p-2 rounded-lg bg-orange-950/40 border border-orange-400/40 text-[10px] text-orange-200 space-y-0.5">
            <div class="font-bold text-orange-300 flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-orange-400 animate-ping"></span>
              <span>노션 DB 실시간 자동 동기화</span>
            </div>
            <p class="text-[9px] text-slate-300 leading-tight m-0">
              커뮤니티 나눔 목표치 달성률 시각화
            </p>
          </div>
        </div>

        <!-- Open New Tab Button -->
        <div class="pt-2 border-t border-white/10 flex items-center justify-between">
          <span class="text-[11px] font-bold text-orange-300 flex items-center gap-1 group-hover:text-orange-200">
            <span>라이브 서비스 바로가기</span>
            <ArrowUpRight :size="13" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </span>
          <span class="text-[9.5px] text-slate-400 font-mono">새 탭 ↗</span>
        </div>
      </a>
    </div>
  </div>
</template>
