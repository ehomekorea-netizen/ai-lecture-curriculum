<script setup lang="ts">
import { ref, markRaw, watch, computed } from 'vue'
import {
  Bot,
  Brain,
  Layers,
  Sparkles,
  Lightbulb,
  Orbit,
  Sliders,
  Navigation,
  Thermometer,
  Gamepad2,
  MailCheck,
  ShieldAlert,
  LineChart,
  TrendingUp,
  ScanFace,
  AudioWaveform,
  CheckCircle2
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const base = import.meta.env.BASE_URL || '/'
const resolveAsset = (path: string) => {
  if (!path || path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

type LayerKey = 'ai' | 'ml' | 'dl' | 'genai'

const layerKeys: LayerKey[] = ['ai', 'ml', 'dl', 'genai']

// User clicked layer or slide stage
const selectedLayer = ref<LayerKey>('ai')

// If stage changes (from slidev clicks), sync active layer
watch(() => props.stage, (st) => {
  if (st >= 0 && st < layerKeys.length) {
    selectedLayer.value = layerKeys[st]
  } else if (st >= layerKeys.length) {
    selectedLayer.value = 'genai'
  }
}, { immediate: true })

const activeLayer = computed(() => selectedLayer.value)

type TagItem = {
  name: string
  logo?: string
  icon?: any
  iconColor?: string
}

const layerData: Record<LayerKey, {
  title: string
  en: string
  desc: string
  tags: TagItem[]
  color: string
  glowColor: string
  accentBg: string
  icon: any
  tip: string
}> = {
  ai: {
    title: '인공지능 (AI)',
    en: 'Artificial Intelligence — 가장 포괄적인 우주 생태계',
    desc: '기계가 인간의 지적 행동을 모방하는 모든 기술의 총칭입니다. <mark class="hl-ai">데이터 학습 없이</mark> 사람이 직접 설계한 <mark class="hl-ai">논리 규칙(If-Then)과 수학적 탐색 알고리즘</mark>으로 계산하고 판단합니다.',
    tags: [
      { name: '규칙 기반 전문가 시스템 (If-Then)', icon: markRaw(Sliders), iconColor: '#38BDF8' },
      { name: '최단 경로 탐색 (네비게이션)', icon: markRaw(Navigation), iconColor: '#38BDF8' },
      { name: '스마트 센서 자동화 (온도·조명)', icon: markRaw(Thermometer), iconColor: '#38BDF8' },
      { name: '체스·오목 의사결정 알고리즘', icon: markRaw(Gamepad2), iconColor: '#38BDF8' },
    ],
    color: '#38BDF8',
    glowColor: 'rgba(56, 189, 248, 0.55)',
    accentBg: 'rgba(56, 189, 248, 0.08)',
    icon: markRaw(Bot),
    tip: '데이터 학습 여부와 무관하게 <mark class="hl-ai">"사람이 짠 규칙대로 스스로 계산·판단하는"</mark> 가장 거대한 최상위 범주입니다.'
  },
  ml: {
    title: '머신러닝 (기계학습)',
    en: 'Machine Learning — 데이터 기반 통계 학습 방법론',
    desc: '개발자가 규칙을 일일이 코딩하지 않고, <mark class="hl-ml">대량의 데이터를 제공하여 기계가 스스로 최적의 패턴과 통계 규칙을 학습(Learning)</mark>하게 만드는 AI의 핵심 방법론입니다.',
    tags: [
      { name: '스팸 메일 자동 필터링 (분류)', icon: markRaw(MailCheck), iconColor: '#A855F7' },
      { name: '금융 이상거래 탐지 (FDS 이상감지)', icon: markRaw(ShieldAlert), iconColor: '#A855F7' },
      { name: '데이터 기반 시계열 수요 예측', icon: markRaw(LineChart), iconColor: '#A855F7' },
      { name: '개인화 알고리즘 추천 랭킹', icon: markRaw(TrendingUp), iconColor: '#A855F7' },
    ],
    color: '#A855F7',
    glowColor: 'rgba(168, 85, 247, 0.55)',
    accentBg: 'rgba(168, 85, 247, 0.08)',
    icon: markRaw(Brain),
    tip: '사람이 규칙을 짜는 대신, <mark class="hl-ml">"데이터로부터 기계가 통계적 규칙을 스스로 찾아낸다(Learning)"</mark>는 학습 패러다임입니다.'
  },
  dl: {
    title: '딥러닝 (심층학습)',
    en: 'Deep Learning — 뇌 신경망을 모방한 심층 인공신경망',
    desc: '인간 <mark class="hl-dl">뇌 신경망을 모방한 심층 다층 구조(Neural Network)</mark>를 통해, 사람이 규칙을 정의하기 힘든 <mark class="hl-dl">비정형 데이터(이미지·영상·음성)의 특징을 스스로 인지하고 추출</mark>합니다.',
    tags: [
      { name: '알파고 (AlphaGo 심층강화학습)', logo: '/icons/deepmind-color.svg' },
      { name: 'Face ID 생체 안면 인식', logo: '/icons/apple.svg' },
      { name: '자율주행 비전 객체 인식 (CNN)', icon: markRaw(ScanFace), iconColor: '#F59E0B' },
      { name: '실시간 음성 합성 & 변환 (TTS)', icon: markRaw(AudioWaveform), iconColor: '#F59E0B' },
    ],
    color: '#F59E0B',
    glowColor: 'rgba(245, 158, 11, 0.55)',
    accentBg: 'rgba(245, 158, 11, 0.08)',
    icon: markRaw(Layers),
    tip: '복잡한 비정형 데이터(사진 픽셀, 음성 파형)를 <mark class="hl-dl">"심층 인공신경망으로 스스로 해석"</mark>하는 돌파구를 열었습니다.'
  },
  genai: {
    title: '생성형 AI (Generative AI)',
    en: 'Generative AI — 새로운 합성 콘텐츠를 창조하는 중심 핵',
    desc: '기존 데이터를 단순히 분류하거나 판별하는 것을 넘어, <mark class="hl-genai">학습한 확률 문맥을 바탕으로 새로운 글·문서·이미지·코드를 직접 합성(Generation)하고 창조</mark>해내는 최신 AI입니다.',
    tags: [
      { name: 'ChatGPT (OpenAI 자연어 생성)', logo: '/icons/openai.svg' },
      { name: 'Claude (Anthropic 문서·코드 분석)', logo: '/icons/claude-color.svg' },
      { name: 'Gemini (Google 멀티모달 추론)', logo: '/icons/gemini-color.svg' },
      { name: 'Midjourney (고화질 이미지 합성)', logo: '/icons/midjourney.svg' },
    ],
    color: '#10B981',
    glowColor: 'rgba(16, 185, 129, 0.75)',
    accentBg: 'rgba(16, 185, 129, 0.12)',
    icon: markRaw(Sparkles),
    tip: '단순 분석을 넘어 <mark class="hl-genai">"자연어 대화만으로 새로운 실무 콘텐츠를 직접 생성하고 창작"</mark>하는 실전 도구입니다.'
  }
}

// Clean Concentric Cosmic Circle Definitions
const rings = [
  { key: 'ai' as LayerKey, cx: 140, cy: 140, r: 125, color: '#38BDF8', glow: '#0284C7', label: '인공지능 (AI)', icon: markRaw(Bot) },
  { key: 'ml' as LayerKey, cx: 140, cy: 154, r: 96, color: '#A855F7', glow: '#7E22CE', label: '머신러닝 (ML)', icon: markRaw(Brain) },
  { key: 'dl' as LayerKey, cx: 140, cy: 168, r: 68, color: '#F59E0B', glow: '#D97706', label: '딥러닝 (DL)', icon: markRaw(Layers) },
  { key: 'genai' as LayerKey, cx: 140, cy: 182, r: 40, color: '#10B981', glow: '#059669', label: '생성형 AI', icon: markRaw(Sparkles) },
]

function selectLayer(key: LayerKey) {
  selectedLayer.value = key
}
</script>

<template>
  <div class="w-full flex items-center justify-between gap-6 select-none font-sans text-slate-100 my-auto">
    <!-- ── Left: Cosmic Ecosystem Concentric Orbit (280x280) ── -->
    <div class="relative flex flex-col items-center shrink-0">
      <!-- Cosmic Space Glass Sphere Background -->
      <div
        class="relative w-[280px] h-[280px] rounded-full overflow-hidden shadow-2xl flex items-center justify-center border border-slate-700/60 bg-gradient-to-b from-[#0B0F19] via-[#0D1527] to-[#050811]"
      >
        <!-- Background Ambient Nebula Glow -->
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-blue-900/30 via-purple-950/20 to-transparent pointer-events-none" />

        <!-- Floating Micro Stars / Cosmic Stardust -->
        <div class="absolute top-[20px] left-[45px] w-1 h-1 bg-white/70 rounded-full animate-pulse" />
        <div class="absolute top-[80px] right-[35px] w-1 h-1 bg-sky-300/80 rounded-full animate-ping" style="animation-duration: 3s;" />
        <div class="absolute bottom-[40px] left-[50px] w-1.5 h-1.5 bg-purple-300/60 rounded-full animate-pulse" style="animation-duration: 2s;" />
        <div class="absolute top-[130px] left-[20px] w-1 h-1 bg-emerald-300/60 rounded-full" />
        <div class="absolute bottom-[70px] right-[40px] w-1 h-1 bg-amber-200/70 rounded-full animate-pulse" style="animation-duration: 2.5s;" />

        <!-- SVG Concentric Orbital Circles with Glowing Filters -->
        <svg viewBox="0 0 280 280" class="absolute inset-0 w-full h-full">
          <defs>
            <!-- Glowing Filters -->
            <filter id="glow-ai" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="4" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="glow-ml" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="4" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="glow-dl" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="4" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
            <filter id="glow-genai" x="-30%" y="-30%" width="160%" height="160%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>

            <!-- Radial Gradients for Layer Surfaces -->
            <radialGradient id="grad-ai" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.16" />
              <stop offset="100%" stop-color="#0284C7" stop-opacity="0.04" />
            </radialGradient>
            <radialGradient id="grad-ml" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#A855F7" stop-opacity="0.22" />
              <stop offset="100%" stop-color="#7E22CE" stop-opacity="0.06" />
            </radialGradient>
            <radialGradient id="grad-dl" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.26" />
              <stop offset="100%" stop-color="#D97706" stop-opacity="0.08" />
            </radialGradient>
            <radialGradient id="grad-genai" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#34D399" stop-opacity="0.65" />
              <stop offset="60%" stop-color="#10B981" stop-opacity="0.45" />
              <stop offset="100%" stop-color="#059669" stop-opacity="0.2" />
            </radialGradient>
          </defs>

          <!-- 1. AI Orbit (Outermost) -->
          <circle
            cx="140"
            cy="140"
            r="125"
            fill="url(#grad-ai)"
            :stroke="activeLayer === 'ai' ? '#38BDF8' : 'rgba(56, 189, 248, 0.35)'"
            :stroke-width="activeLayer === 'ai' ? 2.5 : 1.2"
            :filter="activeLayer === 'ai' ? 'url(#glow-ai)' : undefined"
            class="transition-all duration-300 cursor-pointer"
            @click="selectLayer('ai')"
          />
          <!-- Orbital Dashed Guide Line -->
          <circle
            cx="140"
            cy="140"
            r="125"
            fill="none"
            stroke="rgba(255,255,255,0.15)"
            stroke-width="1"
            stroke-dasharray="3 6"
            class="pointer-events-none"
          />

          <!-- 2. ML Orbit -->
          <circle
            cx="140"
            cy="154"
            r="96"
            fill="url(#grad-ml)"
            :stroke="activeLayer === 'ml' ? '#C084FC' : 'rgba(168, 85, 247, 0.4)'"
            :stroke-width="activeLayer === 'ml' ? 2.5 : 1.2"
            :filter="activeLayer === 'ml' ? 'url(#glow-ml)' : undefined"
            class="transition-all duration-300 cursor-pointer"
            @click="selectLayer('ml')"
          />
          <circle
            cx="140"
            cy="154"
            r="96"
            fill="none"
            stroke="rgba(255,255,255,0.15)"
            stroke-width="1"
            stroke-dasharray="3 5"
            class="pointer-events-none"
          />

          <!-- 3. DL Orbit -->
          <circle
            cx="140"
            cy="168"
            r="68"
            fill="url(#grad-dl)"
            :stroke="activeLayer === 'dl' ? '#FBBF24' : 'rgba(245, 158, 11, 0.45)'"
            :stroke-width="activeLayer === 'dl' ? 2.5 : 1.2"
            :filter="activeLayer === 'dl' ? 'url(#glow-dl)' : undefined"
            class="transition-all duration-300 cursor-pointer"
            @click="selectLayer('dl')"
          />
          <circle
            cx="140"
            cy="168"
            r="68"
            fill="none"
            stroke="rgba(255,255,255,0.2)"
            stroke-width="1"
            stroke-dasharray="2 4"
            class="pointer-events-none"
          />

          <!-- 4. GenAI Radiant Star Core (Innermost) -->
          <circle
            cx="140"
            cy="182"
            r="40"
            fill="url(#grad-genai)"
            :stroke="activeLayer === 'genai' ? '#6EE7B7' : '#10B981'"
            :stroke-width="activeLayer === 'genai' ? 3 : 1.8"
            :filter="activeLayer === 'genai' ? 'url(#glow-genai)' : undefined"
            class="transition-all duration-300 cursor-pointer"
            @click="selectLayer('genai')"
          />
        </svg>

        <!-- Interactive Futuristic Luminous Tags on the Circles -->
        <!-- Layer 1: AI (Outermost Top) -->
        <button
          @click="selectLayer('ai')"
          class="absolute left-1/2 -translate-x-1/2 top-[24px] flex items-center gap-1.5 px-3 py-0.5 rounded-full text-[10.5px] font-mono font-bold transition-all cursor-pointer shadow-lg z-20 backdrop-blur-md"
          :class="activeLayer === 'ai'
            ? 'bg-sky-500 text-white shadow-[0_0_12px_rgba(56,189,248,0.8)] ring-2 ring-sky-300 scale-105'
            : 'bg-slate-900/80 text-sky-300 border border-sky-500/40 hover:bg-sky-950/90'"
        >
          <Bot :size="12" />
          <span>인공지능 (AI)</span>
        </button>

        <!-- Layer 2: ML -->
        <button
          @click="selectLayer('ml')"
          class="absolute left-1/2 -translate-x-1/2 top-[68px] flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold transition-all cursor-pointer shadow-lg z-20 backdrop-blur-md"
          :class="activeLayer === 'ml'
            ? 'bg-purple-600 text-white shadow-[0_0_12px_rgba(168,85,247,0.8)] ring-2 ring-purple-300 scale-105'
            : 'bg-slate-900/80 text-purple-300 border border-purple-500/40 hover:bg-purple-950/90'"
        >
          <Brain :size="11" />
          <span>머신러닝 (ML)</span>
        </button>

        <!-- Layer 3: DL -->
        <button
          @click="selectLayer('dl')"
          class="absolute left-1/2 -translate-x-1/2 top-[112px] flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[9.5px] font-mono font-bold transition-all cursor-pointer shadow-lg z-20 backdrop-blur-md"
          :class="activeLayer === 'dl'
            ? 'bg-amber-500 text-white font-extrabold shadow-[0_0_12px_rgba(245,158,11,0.8)] ring-2 ring-amber-300 scale-105'
            : 'bg-slate-900/80 text-amber-300 border border-amber-500/40 hover:bg-amber-950/90'"
        >
          <Layers :size="11" />
          <span>딥러닝 (DL)</span>
        </button>

        <!-- Layer 4: GenAI (Innermost Core) -->
        <button
          @click="selectLayer('genai')"
          class="absolute left-1/2 -translate-x-1/2 top-[156px] flex flex-col items-center justify-center w-[54px] h-[54px] rounded-full text-[10px] font-bold transition-all cursor-pointer z-30 shadow-2xl backdrop-blur-md"
          :class="activeLayer === 'genai'
            ? 'bg-emerald-950/400 text-white font-black shadow-[0_0_18px_rgba(16,185,129,0.95)] ring-2 ring-emerald-200 scale-110'
            : 'bg-emerald-950/90 text-emerald-300 border border-emerald-400/60 hover:scale-105'"
        >
          <Sparkles :size="14" class="mb-0.5 animate-bounce" style="animation-duration: 2s;" />
          <span class="leading-tight text-center font-serif text-[10px]">생성형<br>AI</span>
        </button>
      </div>

      <!-- Hint Caption -->
      <div class="flex items-center gap-1 text-[10px] text-slate-400 font-mono mt-1.5">
        <Orbit :size="11" class="text-blue-500" />
        <span>원형 궤도 또는 탭을 클릭해 계층 전환</span>
      </div>
    </div>

    <!-- ── Right: Clean Editorial Detail Card ── -->
    <div class="flex-1 flex flex-col justify-center text-left">
      <!-- Quick Layer Switcher Tabs -->
      <div class="flex items-center gap-2 mb-2.5">
        <button
          v-for="key in layerKeys"
          :key="key"
          @click="selectLayer(key)"
          class="px-3 py-1 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer border shadow-2xs"
          :class="activeLayer === key
            ? 'border-slate-800 text-white bg-white/6 shadow-sm ring-1 ring-slate-800 scale-102'
            : 'border-white/10 text-slate-400 hover:text-white bg-white/70 hover:bg-white/6'"
        >
          <component :is="layerData[key].icon" :size="13" :style="{ color: layerData[key].color }" />
          <span>{{ layerData[key].title.split(' ')[0] }}</span>
        </button>
      </div>

      <!-- Detail Card Container -->
      <div
        class="bg-white/6 rounded-2xl border p-4 shadow-sm transition-all duration-300 relative overflow-hidden"
        :style="{ borderColor: layerData[activeLayer].color + '60' }"
      >
        <!-- Header -->
        <div class="flex items-center justify-between border-b pb-2 mb-2.5" :style="{ borderColor: layerData[activeLayer].color + '25' }">
          <div class="flex items-center gap-2.5">
            <div
              class="w-8 h-8 rounded-xl flex items-center justify-center shadow-inner"
              :style="{ background: layerData[activeLayer].accentBg, color: layerData[activeLayer].color }"
            >
              <component :is="layerData[activeLayer].icon" :size="18" />
            </div>
            <div>
              <h3 class="text-base md:text-[17px] font-bold text-white font-serif leading-tight">
                {{ layerData[activeLayer].title }}
              </h3>
              <div class="text-[10.5px] font-mono text-slate-400">
                {{ layerData[activeLayer].en }}
              </div>
            </div>
          </div>
          <span
            class="px-2.5 py-0.5 rounded-full text-[10.5px] font-bold font-mono uppercase tracking-wider"
            :style="{ background: layerData[activeLayer].accentBg, color: layerData[activeLayer].color }"
          >
            {{ activeLayer }}
          </span>
        </div>

        <!-- Description with Highlighter Markers -->
        <p
          class="text-[12.5px] text-slate-300 font-medium leading-relaxed mb-3 break-keep"
          v-html="layerData[activeLayer].desc"
        />

        <!-- 2x2 Symmetrical Grid: Clean, Zero Line-Break & Perfect Alignment -->
        <div class="grid grid-cols-2 gap-2 mb-3 w-full">
          <div
            v-for="tag in layerData[activeLayer].tags"
            :key="tag.name"
            class="flex items-center gap-2 p-1.5 px-2.5 rounded-xl bg-white/6 text-white text-[11px] font-bold border border-white/10 shadow-2xs hover:border-slate-400 transition-colors whitespace-nowrap overflow-hidden"
          >
            <!-- Brand SVG Logo if available -->
            <img
              v-if="tag.logo"
              :src="resolveAsset(tag.logo)"
              class="w-3.5 h-3.5 object-contain shrink-0"
              :alt="tag.name"
            />
            <!-- Custom Lucide Vector SVG Icon -->
            <component
              v-else-if="tag.icon"
              :is="tag.icon"
              :size="13"
              class="shrink-0"
              :style="{ color: tag.iconColor || layerData[activeLayer].color }"
            />
            <CheckCircle2 v-else :size="11" class="text-slate-400 shrink-0" />
            <span class="truncate">{{ tag.name }}</span>
          </div>
        </div>

        <!-- Tip Box with Highlighter Markers -->
        <div
          class="flex items-start gap-2 p-2.5 rounded-xl text-xs leading-relaxed border border-slate-100"
          :style="{ background: layerData[activeLayer].accentBg }"
        >
          <Lightbulb :size="15" class="text-amber-600 shrink-0 mt-0.5" />
          <span
            class="text-slate-100 font-medium font-serif"
            v-html="layerData[activeLayer].tip"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
:deep(.hl-ai) {
  background: rgba(56, 189, 248, 0.22);
  color: #38BDF8 !important; background: rgba(56, 189, 248, 0.2) !important; border-bottom: 2px solid #38BDF8 !important;
  font-weight: 700;
  padding: 1px 4px;
  border-radius: 4px;
  border-bottom: 2px solid rgba(56, 189, 248, 0.6);
}

:deep(.hl-ml) {
  background: rgba(168, 85, 247, 0.22);
  color: #C084FC !important; background: rgba(192, 132, 252, 0.2) !important; border-bottom: 2px solid #C084FC !important;
  font-weight: 700;
  padding: 1px 4px;
  border-radius: 4px;
  border-bottom: 2px solid rgba(168, 85, 247, 0.6);
}

:deep(.hl-dl) {
  background: rgba(245, 158, 11, 0.24);
  color: #FBBF24 !important; background: rgba(251, 191, 36, 0.2) !important; border-bottom: 2px solid #FBBF24 !important;
  font-weight: 700;
  padding: 1px 4px;
  border-radius: 4px;
  border-bottom: 2px solid rgba(245, 158, 11, 0.6);
}

:deep(.hl-genai) {
  background: rgba(16, 185, 129, 0.25);
  color: #34D399 !important; background: rgba(52, 211, 153, 0.2) !important; border-bottom: 2px solid #34D399 !important;
  font-weight: 700;
  padding: 1px 4px;
  border-radius: 4px;
  border-bottom: 2px solid rgba(16, 185, 129, 0.6);
}
</style>