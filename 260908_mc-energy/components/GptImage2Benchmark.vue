<script setup lang="ts">
const insights = [
  {
    title: '1. 리더보드 압도적 1위 (1,512 pts)',
    desc: 'Image Arena 글로벌 평가에서 2위 모델(1,271점) 대비 240+ 점의 압도적 격차 기록',
    tag: 'SOTA 1위 달성',
    color: 'cyan',
  },
  {
    title: '2. 99% 수준의 텍스트 렌더링 정확도',
    desc: '기존 모델의 최대 난제였던 다국어·한글 텍스트 및 곡면/라벨 타이포그래피를 완벽하게 인쇄',
    tag: '오타·깨짐 완전 극복',
    color: 'blue',
  },
  {
    title: '3. 자기회귀(Autoregressive) 추론 도입',
    desc: '단순 노이즈 제거(Diffusion)가 아닌 프롬프트의 복합 제약조건을 사전에 추론하고 자가 보정',
    tag: '추론형 생성 엔진',
    color: 'violet',
  },
  {
    title: '4. 인위적인 AI 색감(AI Tint) 제거',
    desc: '과장된 광택과 누런 톤을 걷어내고 실무 포스터·홍보물에 바로 쓰는 고화질 포토리얼리즘 완성',
    tag: '실무 인쇄급 화질',
    color: 'emerald',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-6 items-stretch">
      <!-- Left: Benchmark Leaderboard Image -->
      <div class="col-span-5 flex flex-col justify-center items-center h-82">
        <img
          src="/ChatGPT-Images-2.0-1.webp"
          alt="ChatGPT Images 2.0 Leaderboard Benchmark"
          class="rounded-2xl w-full max-h-78 object-contain select-none shadow-2xl"
        />
      </div>

      <!-- Right: Structured Analytics Vidhya Insights Grid -->
      <div class="col-span-7 grid grid-cols-2 gap-3.5 items-stretch h-82">
        <div
          v-for="item in insights"
          :key="item.title"
          class="p-3.5 rounded-xl bg-white/5 border border-white/10 flex flex-col justify-between h-39"
        >
          <div>
            <div class="border-b border-white/10 pb-1 mb-1.5 whitespace-nowrap">
              <strong class="text-xs text-white">{{ item.title }}</strong>
            </div>
            <p class="text-[10.5px] text-white/80 m-0 leading-relaxed break-keep">
              {{ item.desc }}
            </p>
          </div>

          <div
            class="pt-1 border-t border-white/10 text-[9.5px] font-mono whitespace-nowrap font-bold"
            :class="item.color === 'cyan' ? 'text-cyan-300' : item.color === 'blue' ? 'text-blue-300' : item.color === 'violet' ? 'text-purple-300' : 'text-emerald-300'"
          >
            ✓ {{ item.tag }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
