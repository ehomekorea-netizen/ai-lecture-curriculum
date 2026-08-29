<script setup lang="ts">
import { ArrowUpRight } from 'lucide-vue-next'
import lectureImg from '../public/showcase-lecture-vibe.png'
import biblegramImg from '../public/showcase-biblegram.png'
import danggeunImg from '../public/showcase-danggeun.png'

const projects = [
  {
    id: '01',
    title: '출강바이브',
    url: 'https://lecture-payment-dashboard.vercel.app/',
    img: lectureImg,
    desc: '강사용 실시간 정산 및 3.3% 세액 자동 계산',
  },
  {
    id: '02',
    title: '바이블그램',
    url: 'https://biblegram.vercel.app/',
    img: biblegramImg,
    desc: '바쁜 일상 속 아침 7시 성경 말씀 푸시 알림',
  },
  {
    id: '03',
    title: 'HEAT Carrot',
    url: 'https://danggeun-dashboard.vercel.app/',
    img: danggeunImg,
    desc: '당근 이웃 나눔 챌린지 기부 적립 실시간 모니터',
  },
]
</script>

<template>
  <div class="w-full grid grid-cols-3 gap-6 items-center justify-items-center select-none my-auto">
    <a
      v-for="p in projects"
      :key="p.id"
      :href="p.url"
      target="_blank"
      rel="noopener noreferrer"
      class="group flex flex-col items-center text-center no-underline cursor-pointer transition-transform duration-300 hover:scale-103"
    >
      <!-- Pure Raw Image with Direct Vite Asset Bundle -->
      <img
        :src="p.img"
        :alt="p.title"
        class="w-auto h-[290px] max-w-full object-contain rounded-2xl shadow-2xl transition-all duration-300 group-hover:shadow-[0_0_30px_rgba(56,189,248,0.45)]"
      />

      <!-- Simple Title & 1-Line Target Description Under Image -->
      <div class="mt-2.5 flex flex-col items-center gap-0.5">
        <div class="flex items-center gap-1 text-sm font-bold text-white group-hover:text-cyan-300 transition-colors">
          <span>{{ p.title }}</span>
          <ArrowUpRight :size="14" class="text-slate-400 group-hover:text-cyan-300 group-hover:translate-x-0.5 transition-all" />
        </div>
        <p class="text-xs text-slate-300 font-medium m-0 tracking-tight">
          {{ p.desc }}
        </p>
      </div>
    </a>
  </div>
</template>
