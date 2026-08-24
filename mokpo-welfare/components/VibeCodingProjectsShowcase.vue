<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import {
  ExternalLink,
  X,
  Smartphone,
  Monitor,
  Sparkles,
  HelpCircle,
  Heart,
  MessageSquare,
  Send,
  Bookmark,
  Share2,
  CheckCircle2,
  Flame,
  ArrowRight
} from 'lucide-vue-next'

interface ProjectItem {
  id: 'lecture-payment' | 'biblegram' | 'danggeun'
  title: string
  kicker: string
  url: string
  type: 'mobile' | 'desktop'
  desc: string
  tags: string[]
}

const projects: ProjectItem[] = [
  {
    id: 'lecture-payment',
    title: '출강바이브',
    kicker: 'LECTURER FINANCIAL PORTAL',
    url: 'https://lecture-payment-dashboard.vercel.app/',
    type: 'mobile',
    desc: '프리랜서 강사를 위한 스마트 정산 PWA 대시보드',
    tags: ['Vite', 'Tailwind CSS', 'PWA']
  },
  {
    id: 'biblegram',
    title: '바이블그램',
    kicker: 'DAILY LIFE DEVOTIONAL PWA',
    url: 'https://biblegram.vercel.app/',
    type: 'mobile',
    desc: '매일 아침 성경 구절 푸시 알림 및 영성 카드 PWA',
    tags: ['Next.js', 'Vercel Cron', 'Web Push']
  },
  {
    id: 'danggeun',
    title: 'HEAT Carrot',
    kicker: 'COMMUNITY SHARING BOARDS',
    url: 'https://danggeun-dashboard.vercel.app/',
    type: 'desktop',
    desc: '당근 모임 기부 적립 현황 실시간 모니터 대시보드',
    tags: ['Next.js', 'Notion SDK', 'Live Monitor']
  }
]

const activeDrawer = ref<ProjectItem | null>(null)

function openDrawer(item: ProjectItem) {
  activeDrawer.value = item
}

function closeDrawer() {
  activeDrawer.value = null
}

function handleKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape' && activeDrawer.value) {
    closeDrawer()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onBeforeUnmount(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<template>
  <div class="relative w-full h-[335px] my-auto select-none font-sans overflow-hidden flex flex-col justify-between py-1">
    <!-- ── 3 Interactive Live Preview Cards (3-Column Grid) ── -->
    <div class="grid grid-cols-3 gap-3.5 h-full items-stretch">
      <!-- ── 1. 출강바이브 Card (PWA Install & Coin Visual) ── -->
      <div
        class="group relative bg-gradient-to-b from-slate-50/90 to-white rounded-2xl border border-slate-200/90 p-3.5 px-4 shadow-2xs hover:shadow-md hover:border-blue-300 transition-all cursor-pointer flex flex-col justify-between text-left"
        @click="openDrawer(projects[0])"
      >
        <div>
          <!-- Top Badge & Device Tag -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-slate-100">
            <span class="text-[8.5px] font-mono font-bold text-blue-600 uppercase tracking-wider">
              01 · LECTURER PORTAL
            </span>
            <span class="flex items-center gap-1 text-[9px] font-mono bg-blue-50 text-blue-600 px-1.5 py-0.5 rounded-md font-semibold">
              <Smartphone :size="10" /> PWA App
            </span>
          </div>

          <!-- Visual App Identity Box -->
          <div class="p-3 rounded-xl bg-white border border-slate-200/70 shadow-2xs text-center space-y-1.5 mb-2">
            <!-- Animated 3D Coin Badge -->
            <div class="w-10 h-10 mx-auto rounded-full bg-gradient-to-tr from-amber-400 to-yellow-300 flex items-center justify-center text-white text-lg font-black shadow-md ring-4 ring-amber-100 group-hover:scale-110 transition-transform">
              ₩
            </div>
            <h4 class="text-sm font-bold font-serif text-slate-900 m-0">출강바이브</h4>
            <p class="text-[9.5px] text-slate-500 leading-tight m-0 break-keep">
              홈 화면에 추가하고 매일 편리하게 정산 현황을 관리하세요.
            </p>
          </div>

          <!-- Micro Guide Pill -->
          <div class="p-2 rounded-lg bg-blue-50/70 border border-blue-100 text-[9.5px] text-blue-800 space-y-0.5">
            <div class="font-bold flex items-center gap-1">
              <span>📥 [홈화면에 추가]</span>
              <span class="text-blue-500 font-normal">누르면 끝!</span>
            </div>
            <p class="text-[8.5px] text-blue-600/80 leading-tight m-0">
              세율 공제 및 교통비 자동 정산 알고리즘
            </p>
          </div>
        </div>

        <!-- Open Drawer Trigger Button -->
        <div class="pt-2 border-t border-slate-100 flex items-center justify-between">
          <span class="text-[10.5px] font-bold text-blue-600 flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
            <span>실전 앱 열어보기</span>
            <ArrowRight :size="11" />
          </span>
          <span class="text-[9px] text-slate-400 font-mono">Drawer ➔</span>
        </div>
      </div>

      <!-- ── 2. 바이블그램 Card (Visual Devotional Sanctuary) ── -->
      <div
        class="group relative bg-gradient-to-b from-[#0F172A] to-[#1E293B] text-slate-100 rounded-2xl border border-slate-700/80 p-3.5 px-4 shadow-2xs hover:shadow-md hover:border-amber-400/50 transition-all cursor-pointer flex flex-col justify-between text-left"
        @click="openDrawer(projects[1])"
      >
        <div>
          <!-- Top Badge -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-slate-800">
            <span class="text-[8.5px] font-mono font-bold text-amber-400 uppercase tracking-wider">
              02 · DAILY LIFE PWA
            </span>
            <span class="flex items-center gap-1 text-[9px] font-mono bg-amber-400/10 text-amber-300 px-1.5 py-0.5 rounded-md font-semibold">
              <Smartphone :size="10" /> Push Web
            </span>
          </div>

          <!-- Sanctum Visual Card -->
          <div class="relative p-2.5 rounded-xl bg-slate-950/80 border border-slate-800/90 shadow-inner overflow-hidden mb-2">
            <div class="text-[8px] font-mono font-bold text-amber-300/80 tracking-widest text-center uppercase mb-1">
              LIGHT OF WORD
            </div>
            <p class="text-[10px] text-slate-200 font-serif leading-relaxed text-center break-keep m-0 px-1 font-medium">
              "나의 반석이시요 나의 구속자이신 여호와여, 내 입의 말과 마음의 묵상이 주의 앞에 열납되기를..."
            </p>
            <div class="text-[8.5px] text-amber-400/90 text-center font-serif mt-1">
              (시편 19:14)
            </div>

            <!-- Floating Micro Icons -->
            <div class="flex items-center justify-center gap-3 pt-1.5 mt-1 border-t border-slate-800/80 text-slate-400 text-[8.5px]">
              <span class="flex items-center gap-0.5"><Sparkles :size="9" class="text-amber-400" /> AI 묵상</span>
              <span class="flex items-center gap-0.5"><Heart :size="9" /> 0</span>
              <span class="flex items-center gap-0.5"><Share2 :size="9" /> 공유</span>
            </div>
          </div>

          <!-- Sub Feature -->
          <div class="p-1.5 px-2 rounded-lg bg-slate-800/60 text-[9px] text-slate-300">
            <span class="text-amber-300 font-semibold">⏰ 매일 아침 푸시</span> · 영성 카드 이미지 원클릭 다운로드
          </div>
        </div>

        <!-- Open Drawer Trigger -->
        <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
          <span class="text-[10.5px] font-bold text-amber-300 flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
            <span>실전 앱 열어보기</span>
            <ArrowRight :size="11" />
          </span>
          <span class="text-[9px] text-slate-500 font-mono">Drawer ➔</span>
        </div>
      </div>

      <!-- ── 3. HEAT Carrot Card (Dark Dashboard & Rabbit Mascot) ── -->
      <div
        class="group relative bg-[#121212] text-white rounded-2xl border border-neutral-800 p-3.5 px-4 shadow-2xs hover:shadow-md hover:border-orange-500/50 transition-all cursor-pointer flex flex-col justify-between text-left"
        @click="openDrawer(projects[2])"
      >
        <div>
          <!-- Top Badge -->
          <div class="flex items-center justify-between mb-2 pb-1.5 border-b border-neutral-800">
            <span class="text-[8.5px] font-mono font-bold text-orange-400 uppercase tracking-wider">
              03 · SHARING BOARDS
            </span>
            <span class="flex items-center gap-1 text-[9px] font-mono bg-orange-500/10 text-orange-400 px-1.5 py-0.5 rounded-md font-semibold">
              <Monitor :size="10" /> Monitor
            </span>
          </div>

          <!-- Header with Cute Rabbit Mascot Graphic -->
          <div class="p-2.5 rounded-xl bg-neutral-900 border border-neutral-800 mb-2 flex items-center gap-2.5">
            <!-- Cute SVG Rabbit Mascot -->
            <div class="w-9 h-9 shrink-0 flex items-end justify-center">
              <svg viewBox="0 0 64 64" class="w-full h-full drop-shadow">
                <!-- Rabbit Ears -->
                <ellipse cx="24" cy="18" rx="5" ry="16" fill="#FFFFFF" />
                <ellipse cx="24" cy="18" rx="2.5" ry="11" fill="#FFB6C1" />
                <ellipse cx="40" cy="18" rx="5" ry="16" fill="#FFFFFF" />
                <ellipse cx="40" cy="18" rx="2.5" ry="11" fill="#FFB6C1" />
                <!-- Head -->
                <ellipse cx="32" cy="42" rx="20" ry="18" fill="#FFFFFF" />
                <!-- Eyes -->
                <circle cx="26" cy="38" r="2.2" fill="#1E293B" />
                <circle cx="38" cy="38" r="2.2" fill="#1E293B" />
                <!-- Cheeks -->
                <circle cx="21" cy="43" r="2.2" fill="#FFB6C1" opacity="0.8" />
                <circle cx="43" cy="43" r="2.2" fill="#FFB6C1" opacity="0.8" />
                <!-- Nose -->
                <polygon points="32,42 30,45 34,45" fill="#FF9494" />
              </svg>
            </div>
            <div>
              <div class="flex items-center gap-1">
                <span class="text-xs font-black tracking-tight bg-gradient-to-r from-red-500 via-orange-400 to-emerald-400 bg-clip-text text-transparent">
                  HEAT Carrot
                </span>
                <span class="text-[10px] font-bold text-white">프로젝트</span>
              </div>
              <p class="text-[9px] text-neutral-400 leading-snug m-0 break-keep">
                당근의 온기로 근처 이웃에게 따뜻함을 전합니다.
              </p>
            </div>
          </div>

          <!-- Feature Specs -->
          <div class="p-2 rounded-lg bg-neutral-900/90 border border-neutral-800 text-[9.5px] text-neutral-300 space-y-1">
            <div class="flex items-center justify-between">
              <span class="text-neutral-400">연동 시스템</span>
              <span class="text-orange-400 font-mono font-bold">Next.js + Notion SDK</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-neutral-400">데이터 갱신</span>
              <span class="text-emerald-400 font-mono font-bold">실시간 자동 동기화</span>
            </div>
          </div>
        </div>

        <!-- Open Drawer Trigger -->
        <div class="pt-2 border-t border-neutral-800 flex items-center justify-between">
          <span class="text-[10.5px] font-bold text-orange-400 flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
            <span>실전 대시보드 열기</span>
            <ArrowRight :size="11" />
          </span>
          <span class="text-[9px] text-neutral-500 font-mono">Drawer ➔</span>
        </div>
      </div>
    </div>

    <!-- ── Interactive Slide Drawer (In-Deck Left Drawer with Device Frame) ── -->
    <Transition name="drawer">
      <div
        v-if="activeDrawer"
        class="absolute inset-0 z-50 flex bg-slate-900/60 backdrop-blur-xs select-none"
        @click.self="closeDrawer"
      >
        <!-- Drawer Panel: Slides from Left -->
        <div class="relative w-[480px] max-w-[85%] h-full bg-white shadow-2xl flex flex-col justify-between border-r border-slate-200 overflow-hidden text-left">
          <!-- Drawer Header -->
          <div class="flex items-center justify-between px-4 py-2.5 bg-slate-50 border-b border-slate-200">
            <div class="flex items-center gap-2">
              <span
                class="w-2.5 h-2.5 rounded-full"
                :class="activeDrawer.id === 'lecture-payment' ? 'bg-blue-600' : activeDrawer.id === 'biblegram' ? 'bg-amber-500' : 'bg-orange-500'"
              />
              <span class="font-bold text-xs font-serif text-slate-900">{{ activeDrawer.title }}</span>
              <span class="text-[9.5px] font-mono text-slate-400 uppercase tracking-wider">{{ activeDrawer.kicker }}</span>
            </div>

            <div class="flex items-center gap-2">
              <!-- Live External Link -->
              <a
                :href="activeDrawer.url"
                target="_blank"
                rel="noopener noreferrer"
                class="flex items-center gap-1 text-[10px] text-blue-600 hover:text-blue-800 bg-blue-50 px-2 py-0.8 rounded-md font-medium border border-blue-200 transition-colors"
                title="새 탭에서 열기"
              >
                <span>새 창</span>
                <ExternalLink :size="10" />
              </a>

              <!-- Close Button -->
              <button
                class="flex items-center gap-1 text-[10px] font-bold text-slate-600 hover:text-red-600 bg-slate-200/70 hover:bg-red-50 px-2.5 py-0.8 rounded-md transition-colors cursor-pointer border border-slate-300/80"
                @click="closeDrawer"
              >
                <span>취소 ✕</span>
              </button>
            </div>
          </div>

          <!-- Drawer Body: Device Screen (Iframe / Live App Viewer) -->
          <div class="flex-1 bg-slate-900 flex items-center justify-center p-2 overflow-hidden relative">
            <!-- Mobile Frame -->
            <div
              v-if="activeDrawer.type === 'mobile'"
              class="w-[260px] h-[260px] rounded-2xl bg-black border-2 border-slate-700 shadow-xl overflow-hidden relative flex flex-col"
            >
              <!-- Dynamic Island / Speaker Bar -->
              <div class="w-full h-3 bg-black flex items-center justify-center shrink-0">
                <div class="w-10 h-1 bg-slate-700 rounded-full" />
              </div>
              <iframe
                :src="activeDrawer.url"
                class="w-full flex-1 border-none bg-white"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              />
            </div>

            <!-- Desktop Frame -->
            <div
              v-else
              class="w-full h-[260px] rounded-xl bg-slate-950 border border-slate-800 shadow-xl overflow-hidden flex flex-col"
            >
              <!-- Browser Chrome Bar -->
              <div class="w-full h-5 bg-slate-900 border-b border-slate-800 flex items-center px-2.5 gap-1.5 shrink-0">
                <div class="w-2 h-2 rounded-full bg-red-500/80" />
                <div class="w-2 h-2 rounded-full bg-amber-500/80" />
                <div class="w-2 h-2 rounded-full bg-emerald-500/80" />
                <div class="flex-1 mx-2 h-3 rounded bg-slate-800 text-[8px] font-mono text-slate-400 flex items-center px-2 truncate">
                  {{ activeDrawer.url }}
                </div>
              </div>
              <iframe
                :src="activeDrawer.url"
                class="w-full flex-1 border-none bg-slate-900"
              />
            </div>
          </div>

          <!-- Drawer Footer -->
          <div class="px-4 py-1.5 bg-white border-t border-slate-100 flex items-center justify-between text-[10px] text-slate-500">
            <span class="truncate max-w-[280px]">{{ activeDrawer.desc }}</span>
            <button
              class="text-blue-600 font-bold hover:underline cursor-pointer"
              @click="closeDrawer"
            >
              닫기
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
/* ── Left Drawer Smooth Slide Transition ── */
.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.25s ease;
}

.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
}

.drawer-enter-active > div,
.drawer-leave-active > div {
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.drawer-enter-from > div {
  transform: translateX(-100%);
}

.drawer-leave-to > div {
  transform: translateX(-100%);
}
</style>
