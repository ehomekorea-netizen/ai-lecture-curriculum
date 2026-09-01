<script setup lang="ts">
const guidelines = [
  {
    num: '①',
    title: '비즈니스 목적 & 사용 맥락 정의',
    desc: '단순한 그림 묘사가 아닌 "사내 에너지 절감 캠페인용 포스터"처럼 사용처와 목적을 명시하면 모델이 Thinking(추론)을 통해 최적의 배경과 구도를 설계합니다.',
    tag: 'Thinking 유도',
    color: 'cyan',
  },
  {
    num: '②',
    title: '큰따옴표("")로 인쇄할 한글 문구 엄격 지정',
    desc: '포스터에 들어갈 문구를 큰따옴표로 정확히 감싸주면 ("스마트한 실천, 에너지 절감의 시작"), 99% 정확도로 오타나 글자 깨짐 없이 선명하게 인쇄됩니다.',
    tag: '한글 오타 제로',
    color: 'blue',
  },
  {
    num: '③',
    title: '규격(화면비) & 2K 실무 해상도 제약',
    desc: '사내 게시판/사이니지용 "9:16 세로형", 인트라넷 배너용 "16:9 가로형", 그리고 "2K 초고해상도, 자연스러운 포토리얼리즘"을 명시하여 실무 인쇄 퀄리티를 확보합니다.',
    tag: '2K 규격 통제',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Pure Korean Typography Showcase Image -->
      <div class="col-span-5 flex items-center justify-center h-82">
        <img
          src="/image.inblog.webp"
          alt="ChatGPT Images 2.0 Korean Typography Showcase"
          class="rounded-2xl w-full h-82 object-cover select-none shadow-2xl"
        />
      </div>

      <!-- Right: 3 Core Prompting Principles for Reasoning Models -->
      <div class="col-span-7 flex flex-col justify-between h-82 py-1">
        <div class="space-y-3 flex-1 flex flex-col justify-between">
          <div
            v-for="item in guidelines"
            :key="item.num"
            class="p-3 rounded-xl bg-white/5 border border-white/10 flex flex-col justify-between"
          >
            <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-1.5">
              <strong class="text-xs text-white font-bold">{{ item.num }} {{ item.title }}</strong>
              <span
                class="text-[9.5px] font-mono font-bold px-2 py-0.5 rounded bg-black/40 border border-white/10 whitespace-nowrap"
                :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : 'text-emerald-300'"
              >
                ✓ {{ item.tag }}
              </span>
            </div>
            <p class="text-[11px] text-white/80 m-0 leading-relaxed break-keep">
              {{ item.desc }}
            </p>
          </div>
        </div>

        <!-- Footer Guideline Summary -->
        <div class="pt-2 text-[10px] font-mono text-white/40 flex items-center justify-between">
          <span>Rule: [목적 정의] ➔ [따옴표 한글 텍스트] ➔ [2K 화면비 & 스타일]</span>
          <span class="text-emerald-300/90 font-bold">ChatGPT Images 2.0 Standard</span>
        </div>
      </div>
    </div>
  </div>
</template>
