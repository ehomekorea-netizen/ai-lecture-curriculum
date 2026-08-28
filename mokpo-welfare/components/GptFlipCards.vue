<script setup lang="ts">
import { ref, markRaw } from 'vue'
import { Sparkles, Database, Network, RotateCw, CheckCircle2 } from 'lucide-vue-next'

interface CardItem {
  id: string
  letter: string
  title: string
  sub: string
  color: string
  glowColor: string
  textColor: string
  bgLight: string
  icon: any
  // Back contents
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
    color: '#476BFF',
    glowColor: 'rgba(71, 107, 255, 0.22)',
    textColor: 'text-blue-600',
    bgLight: 'bg-blue-950/40',
    icon: markRaw(Sparkles),
    analogy: '💡 "백지를 채우는 초고속 전문 작가"',
    desc: '저장된 답을 복사하는 것이 아니라, 사용자의 요구 조건과 확률에 따라 새로운 문장과 서식을 직접 합성하여 창작합니다.',
    keyTakeaway: '단순 복사가 아닌 새로운 합성 창작',
  },
  {
    id: 'p',
    letter: 'P',
    title: 'Pre-trained',
    sub: '사전 학습된',
    color: '#10B981',
    glowColor: 'rgba(16, 185, 129, 0.22)',
    textColor: 'text-emerald-600',
    bgLight: 'bg-emerald-950/40',
    icon: markRaw(Database),
    analogy: '💡 "공문서 100만 권을 읽고 온 신입"',
    desc: '수억 건의 공문서와 웹 문서를 미리 학습하여, 별도 코딩이나 문법 교육 없이도 자연스러운 한국어 문맥을 이미 숙지하고 있습니다.',
    keyTakeaway: '방대한 한국어 문맥·격식체 사전 준비',
  },
  {
    id: 't',
    letter: 'T',
    title: 'Transformer',
    sub: '문맥 연결 신경망',
    color: '#8B5CF6',
    glowColor: 'rgba(139, 92, 246, 0.22)',
    textColor: 'text-purple-600',
    bgLight: 'bg-purple-50/70',
    icon: markRaw(Network),
    analogy: '💡 "긴 글의 전후 맥락을 꿰뚫는 기억망"',
    desc: '문장 속 모든 단어 간의 연관성(Attention)을 종합 분석하여, 긴 대화나 복잡한 지침 속에서도 핵심 주제를 놓치지 않습니다.',
    keyTakeaway: '전후 문맥을 잇는 기억 연결망',
  },
]

// Standalone mouse click flip state
const flipped = ref<Record<string, boolean>>({
  g: false,
  p: false,
  t: false,
})

function toggleCard(id: string) {
  flipped.value[id] = !flipped.value[id]
}

// 3D Parallax Tilt Effect on mouse move
const tiltAngles = ref<Record<string, { x: number; y: number }>>({
  g: { x: 0, y: 0 },
  p: { x: 0, y: 0 },
  t: { x: 0, y: 0 },
})

function handleMouseMove(e: MouseEvent, id: string) {
  if (flipped.value[id]) return // Do not tilt while flipped
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
    <!-- 3D Flip Card Grid -->
    <div class="grid grid-cols-3 gap-5 items-stretch">
      <div
        v-for="card in cards"
        :key="card.id"
        class="card-perspective h-[272px] cursor-pointer"
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
              ? `0 12px 28px -4px ${card.glowColor}`
              : `0 8px 22px -6px ${card.glowColor}`,
          }"
        >
          <!-- ── FRONT FACE: Minimal, Clean, Bold ── -->
          <div
            class="card-face card-front absolute inset-0 bg-white/6 rounded-2xl border-2 p-5 flex flex-col justify-between overflow-hidden"
            :style="{ borderColor: card.color + '80' }"
          >
            <!-- Top Icon only -->
            <div class="flex items-center justify-between">
              <div
                class="w-10 h-10 rounded-xl flex items-center justify-center transition-transform group-hover:scale-110"
                :style="{ background: card.color + '15', color: card.color }"
              >
                <component :is="card.icon" :size="24" />
              </div>
            </div>

            <!-- Main Letter & Titles -->
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

            <!-- Bottom: Arrow only -->
            <div class="flex items-center justify-end pt-2 border-t border-slate-100 text-slate-400">
              <span class="text-sm font-bold transition-transform hover:translate-x-1" :style="{ color: card.color }">➔</span>
            </div>
          </div>

          <!-- ── BACK FACE: Clean Layout with No Overflow ── -->
          <div
            class="card-face card-back absolute inset-0 bg-white/6 rounded-2xl border-2 p-4.5 flex flex-col justify-between overflow-hidden"
            :style="{
              borderColor: card.color,
              background: `linear-gradient(180deg, #FFFFFF 0%, ${card.color}08 100%)`
            }"
          >
            <!-- 1. Header -->
            <div>
              <div class="flex items-center justify-between border-b pb-1.5 mb-2" :style="{ borderColor: card.color + '25' }">
                <div class="flex items-center gap-1.5">
                  <span class="w-5 h-5 rounded-full flex items-center justify-center text-xs font-bold text-white font-serif" :style="{ background: card.color }">
                    {{ card.letter }}
                  </span>
                  <span class="text-xs font-bold text-white font-serif">{{ card.title }}</span>
                </div>
                <span class="text-[10px] text-slate-400 font-mono flex items-center gap-0.5">
                  <RotateCw :size="9" /> 뒤집기
                </span>
              </div>

              <!-- 2. Analogy Badge -->
              <div
                class="px-2.5 py-1.5 rounded-lg text-xs font-bold text-slate-100 font-serif leading-snug"
                :style="{ background: card.color + '15' }"
              >
                {{ card.analogy }}
              </div>
            </div>

            <!-- 3. Clean Detailed Description -->
            <div class="my-auto py-1">
              <p class="text-[11.5px] text-slate-300 leading-relaxed font-medium">
                {{ card.desc }}
              </p>
            </div>

            <!-- 4. Key Takeaway Badge (No truncation, safe padding) -->
            <div
              class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-[11px] font-bold mt-1"
              :style="{ background: card.color + '15', color: card.color }"
            >
              <CheckCircle2 :size="12" class="shrink-0" />
              <span class="leading-tight">{{ card.keyTakeaway }}</span>
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
