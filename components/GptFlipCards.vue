<script setup lang="ts">
import { ref, markRaw } from 'vue'
import { Sparkles, Database, Network, RotateCw, CheckCircle2, Lightbulb } from 'lucide-vue-next'

interface CardItem {
  id: string
  letter: string
  title: string
  sub: string
  color: string
  glowColor: string
  badgeBg: string
  icon: any
  analogy: string
  desc: string
  keyTakeaway: string
}

const cards: CardItem[] = [
  {
    id: 'g',
    letter: 'G',
    title: 'Generative',
    sub: '생성하는',
    color: '#38BDF8',
    glowColor: 'rgba(56, 189, 248, 0.35)',
    badgeBg: 'bg-sky-950/90 border border-sky-400/70 text-sky-300',
    icon: markRaw(Sparkles),
    analogy: '"백지를 채우는 초고속 전문 작가"',
    desc: '저장된 답을 복사하는 것이 아니라, 사용자의 요구 조건과 확률에 따라 새로운 문장과 서식을 직접 합성하여 창작합니다.',
    keyTakeaway: '단순 복사가 아닌 새로운 합성 창작',
  },
  {
    id: 'p',
    letter: 'P',
    title: 'Pre-trained',
    sub: '사전 학습된',
    color: '#34D399',
    glowColor: 'rgba(52, 211, 153, 0.35)',
    badgeBg: 'bg-emerald-950/90 border border-emerald-400/70 text-emerald-300',
    icon: markRaw(Database),
    analogy: '"공문서 100만 권을 읽고 온 신입"',
    desc: '수억 건의 공문서와 웹 문서를 미리 학습하여, 별도 코딩이나 문법 교육 없이도 자연스러운 한국어 문맥을 이미 숙지하고 있습니다.',
    keyTakeaway: '방대한 한국어 문맥·격식체 사전 준비',
  },
  {
    id: 't',
    letter: 'T',
    title: 'Transformer',
    sub: '문맥 연결 신경망',
    color: '#C084FC',
    glowColor: 'rgba(192, 132, 252, 0.35)',
    badgeBg: 'bg-purple-950/90 border border-purple-400/70 text-purple-300',
    icon: markRaw(Network),
    analogy: '"긴 글의 전후 맥락을 꿰뚫는 기억망"',
    desc: '문장 속 모든 단어 간의 연관성(Attention)을 종합 분석하여, 긴 대화나 복잡한 지침 속에서도 핵심 주제를 놓치지 않습니다.',
    keyTakeaway: '전후 문맥을 잇는 기억 연결망',
  },
]

const flipped = ref<Record<string, boolean>>({
  g: false,
  p: false,
  t: false,
})

function toggleCard(id: string) {
  flipped.value[id] = !flipped.value[id]
}

const tiltAngles = ref<Record<string, { x: number; y: number }>>({
  g: { x: 0, y: 0 },
  p: { x: 0, y: 0 },
  t: { x: 0, y: 0 },
})

function handleMouseMove(e: MouseEvent, id: string) {
  if (flipped.value[id]) return
  const rect = (e.currentTarget as HTMLElement).getBoundingClientRect()
  const x = e.clientX - rect.left - rect.width / 2
  const y = e.clientY - rect.top - rect.height / 2
  tiltAngles.value[id] = {
    x: -(y / (rect.height / 2)) * 8,
    y: (x / (rect.width / 2)) * 8,
  }
}

function handleMouseLeave(id: string) {
  tiltAngles.value[id] = { x: 0, y: 0 }
}
</script>

<template>
  <div class="w-full select-none my-auto">
    <div class="grid grid-cols-3 gap-5 items-stretch">
      <div
        v-for="card in cards"
        :key="card.id"
        class="card-perspective h-[275px] cursor-pointer"
        @click="toggleCard(card.id)"
        @mousemove="handleMouseMove($event, card.id)"
        @mouseleave="handleMouseLeave(card.id)"
      >
        <div
          class="card-inner relative w-full h-full transition-all duration-500 rounded-2xl"
          :class="{ 'is-flipped': flipped[card.id] }"
          :style="{
            transform: flipped[card.id]
              ? 'rotateY(180deg)'
              : `perspective(1000px) rotateX(${tiltAngles[card.id].x}deg) rotateY(${tiltAngles[card.id].y}deg)`,
            boxShadow: flipped[card.id]
              ? `0 16px 36px -4px ${card.glowColor}`
              : `0 8px 24px -6px ${card.glowColor}`,
          }"
        >
          <!-- ── FRONT FACE ── -->
          <div
            class="card-face card-front absolute inset-0 bg-black/80 rounded-2xl border-2 p-5 flex flex-col justify-between overflow-hidden backdrop-blur-xl"
            :style="{ borderColor: card.color + '80' }"
          >
            <div class="flex items-center justify-between">
              <div
                class="w-10 h-10 rounded-xl flex items-center justify-center transition-transform group-hover:scale-110 shadow-md"
                :style="{ background: card.color + '25', color: card.color, border: `1px solid ${card.color}60` }"
              >
                <component :is="card.icon" :size="22" />
              </div>
            </div>

            <div class="my-auto py-1">
              <div class="text-6xl font-black font-serif tracking-tight mb-1" :style="{ color: card.color }">
                {{ card.letter }}
              </div>
              <div class="text-2xl font-bold text-white font-serif leading-tight">
                {{ card.title }}
              </div>
              <div class="text-base font-bold mt-1" :style="{ color: card.color }">
                {{ card.sub }}
              </div>
            </div>

            <div class="flex items-center justify-end pt-2 border-t border-white/10 text-slate-400">
              <span class="text-xs font-mono font-bold flex items-center gap-1" :style="{ color: card.color }">
                클릭하여 뒤집기 ➔
              </span>
            </div>
          </div>

          <!-- ── BACK FACE: 100% High-Contrast Pure Black Stage ── -->
          <div
            class="card-face card-back absolute inset-0 bg-black/95 rounded-2xl border-2 p-4.5 flex flex-col justify-between overflow-hidden backdrop-blur-2xl shadow-2xl"
            :style="{ borderColor: card.color }"
          >
            <!-- 1. Header -->
            <div>
              <div class="flex items-center justify-between border-b pb-1.5 mb-2.5" :style="{ borderColor: card.color + '40' }">
                <div class="flex items-center gap-2">
                  <span class="w-5 h-5 rounded-full flex items-center justify-center text-xs font-black text-black font-serif" :style="{ background: card.color }">
                    {{ card.letter }}
                  </span>
                  <span class="text-sm font-bold text-white font-serif tracking-tight">{{ card.title }}</span>
                </div>
                <span class="text-[10px] text-slate-300 font-mono font-bold flex items-center gap-0.5 bg-white/10 px-2 py-0.5 rounded border border-white/15">
                  <RotateCw :size="9" /> 뒤집기
                </span>
              </div>

              <!-- 2. Analogy Badge -->
              <div
                class="px-2.5 py-1.5 rounded-lg text-xs font-bold font-serif leading-snug shadow-inner"
                :class="card.badgeBg"
              >
                <span class="flex items-center gap-1.5"><Lightbulb :size="13" class="shrink-0 text-amber-300" /><span>{{ card.analogy }}</span></span>
              </div>
            </div>

            <!-- 3. High-Contrast Description -->
            <div class="my-auto py-1">
              <p class="text-xs text-white font-medium leading-relaxed m-0 break-keep">
                {{ card.desc }}
              </p>
            </div>

            <!-- 4. Key Takeaway Badge -->
            <div
              class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-[11px] font-bold shadow-md"
              :style="{ background: card.color + '25', color: '#ffffff', border: `1px solid ${card.color}80` }"
            >
              <CheckCircle2 :size="13" class="shrink-0" :style="{ color: card.color }" />
              <span class="leading-tight text-white">{{ card.keyTakeaway }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-perspective {
  perspective: 1200px;
}
.card-inner {
  transform-style: preserve-3d;
  position: relative;
  transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
}
.card-inner.is-flipped {
  transform: rotateY(180deg) !important;
}
.card-face {
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  box-sizing: border-box;
}
.card-front {
  transform: rotateY(0deg);
}
.card-back {
  transform: rotateY(180deg);
}
</style>
