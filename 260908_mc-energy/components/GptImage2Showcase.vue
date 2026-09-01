<script setup lang="ts">
const formulaSteps = [
  {
    num: '1',
    title: '용도 & 비즈니스 상황 정의',
    desc: '사내 에너지 절감 캠페인 안내문, 안전 수칙 표지판 등 구체적 사용 목적과 상황을 명시',
    tag: '목적 & 맥락',
    color: 'cyan',
  },
  {
    num: '2',
    title: '정확한 한글 인쇄 텍스트 지정',
    desc: '포스터나 라벨에 들어갈 한글 문구를 큰따옴표로 지정 ("에너지 절감, 스마트한 실천")',
    tag: '한글 텍스트 명시',
    color: 'blue',
  },
  {
    num: '3',
    title: '비주얼 톤 & 규격 제약 통제',
    desc: '2K 고화질, 미니멀 클린 레이아웃, 세로형 9:16 또는 가로형 16:9 규격 지정',
    tag: '2K 화질 & 화면비',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Direct Pure Korean Typography Image -->
      <div class="col-span-5 flex flex-col justify-center items-center h-82">
        <img
          src="/image.inblog.webp"
          alt="ChatGPT Images 2.0 Korean Typography Showcase"
          class="rounded-2xl w-full h-82 object-cover select-none shadow-2xl"
        />
      </div>

      <!-- Right: Clean 1, 2, 3 Formula List (No Bottom Overlapping Section) -->
      <div class="col-span-7 flex flex-col justify-between h-82">
        <div
          v-for="item in formulaSteps"
          :key="item.num"
          class="p-3.5 rounded-xl bg-white/5 border border-white/10 flex flex-col justify-between h-25"
        >
          <div class="flex items-center justify-between border-b border-white/10 pb-1 mb-1">
            <strong class="text-xs text-white">{{ item.num }}. {{ item.title }}</strong>
            <span
              class="text-[9.5px] font-mono font-bold"
              :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : 'text-emerald-300'"
            >
              {{ item.tag }}
            </span>
          </div>
          <p class="text-[11px] text-white/80 m-0 leading-relaxed break-keep">
            {{ item.desc }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
