<script setup lang="ts">
const capabilities = [
  {
    num: '①',
    title: 'Thinking (추론형 비주얼 생성)',
    desc: '단순 확산(Diffusion)을 넘어 자기회귀적 추론을 통해 프롬프트와 레이아웃을 스스로 검토·보정',
    tag: '자기회귀 추론 엔진',
    color: 'cyan',
  },
  {
    num: '②',
    title: '선명한 다국어·한글 텍스트 인쇄',
    desc: '텍스트 렌더링 정확도 99% 달성. 사내 포스터, 라벨, 표지판 속 한글을 오타·깨짐 없이 인쇄',
    tag: '한글 오타 제로',
    color: 'blue',
  },
  {
    num: '③',
    title: '3:1 ~ 1:3 자유 화면비 & 2K',
    desc: '가로 현수막(3:1)부터 인스타 릴스·유튜브 쇼츠(1:3 / 9:16)까지 2K 초고해상도로 자유 지원',
    tag: '2K 규격 제한 해제',
    color: 'violet',
  },
  {
    num: '④',
    title: '스타일 일관성 유지 (Multi-Image)',
    desc: '1번의 지시로 동일한 브랜드 콘셉트와 캐릭터 화풍을 유지하며 최대 8장 연속 컷 생성',
    tag: '동일 톤앤매너 유지',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Clean Full-Height Poster Image (No Small Badge Below) -->
      <div class="col-span-4 flex items-center justify-center h-82">
        <img
          src="/gpt image 2.0.jpeg"
          alt="OpenAI GPT Image 2.0 Poster"
          class="rounded-2xl w-full h-82 object-cover select-none shadow-2xl"
        />
      </div>

      <!-- Right: 4 Core Capabilities Grid -->
      <div class="col-span-8 grid grid-cols-2 gap-3.5 items-stretch h-82">
        <div
          v-for="item in capabilities"
          :key="item.num"
          class="p-4 rounded-xl bg-white/5 border border-white/10 flex flex-col justify-between h-39"
        >
          <div>
            <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-2 whitespace-nowrap">
              <span class="text-xs font-bold text-white">{{ item.num }} {{ item.title }}</span>
            </div>
            <p class="text-[11px] text-white/80 m-0 leading-relaxed break-keep">
              {{ item.desc }}
            </p>
          </div>

          <div
            class="pt-1.5 border-t border-white/10 text-[10px] font-mono whitespace-nowrap font-bold"
            :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'"
          >
            ✓ {{ item.tag }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
