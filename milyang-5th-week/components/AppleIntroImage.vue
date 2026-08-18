<script setup lang="ts">
import { ref, onMounted } from 'vue'

const base = import.meta.env.BASE_URL || '/'
const isLoaded = ref(false)

onMounted(() => {
  setTimeout(() => {
    isLoaded.value = true
  }, 100)
})
</script>

<template>
  <div class="bright-intro-canvas relative w-full h-full overflow-hidden select-none">
    <!-- 1. Dynamic Animated SVG Ambient Light Background -->
    <div class="ambient-mesh-glow"></div>

    <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Gradients -->
        <linearGradient id="rocketGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#3B82F6" />
          <stop offset="100%" stop-color="#1D4ED8" />
        </linearGradient>
        <linearGradient id="agentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#10B981" />
          <stop offset="100%" stop-color="#059669" />
        </linearGradient>
        <linearGradient id="warmSun" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#F59E0B" />
          <stop offset="100%" stop-color="#EF4444" />
        </linearGradient>
        <linearGradient id="lineGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#60A5FA" stop-opacity="0.2" />
          <stop offset="50%" stop-color="#34D399" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#818CF8" stop-opacity="0.2" />
        </linearGradient>
        <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="8" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
      </defs>

      <!-- Dynamic Curved Energy Flow Paths -->
      <path
        d="M -50,150 Q 250,-20 500,120 T 950,100 T 1100,280"
        fill="none"
        stroke="url(#lineGrad)"
        stroke-width="3"
        stroke-dasharray="8 8"
        class="animated-flow-line-1"
      />
      <path
        d="M 100,550 Q 400,380 700,500 T 1050,420"
        fill="none"
        stroke="url(#lineGrad)"
        stroke-width="2.5"
        stroke-dasharray="6 6"
        class="animated-flow-line-2"
      />

      <!-- Floating Animated Tech Geometric Shapes -->
      <!-- Sparkle Star 1 -->
      <g class="floating-star-1" transform="translate(180, 75)">
        <path d="M0,-12 Q0,0 12,0 Q0,0 0,12 Q0,0 -12,0 Q0,0 0,-12" fill="#F59E0B" opacity="0.85" />
      </g>
      <!-- Sparkle Star 2 -->
      <g class="floating-star-2" transform="translate(480, 50)">
        <path d="M0,-16 Q0,0 16,0 Q0,0 0,16 Q0,0 -16,0 Q0,0 0,-16" fill="#10B981" opacity="0.9" />
      </g>
      <!-- Sparkle Star 3 -->
      <g class="floating-star-3" transform="translate(900, 70)">
        <path d="M0,-14 Q0,0 14,0 Q0,0 0,14 Q0,0 -14,0 Q0,0 0,-14" fill="#3B82F6" opacity="0.85" />
      </g>
      <!-- Sparkle Star 4 -->
      <g class="floating-star-4" transform="translate(540, 480)">
        <path d="M0,-10 Q0,0 10,0 Q0,0 0,10 Q0,0 -10,0 Q0,0 0,-10" fill="#EC4899" opacity="0.75" />
      </g>
      <!-- Floating Circle Dots -->
      <circle cx="80" cy="380" r="6" fill="#38BDF8" opacity="0.6" class="floating-dot-1" />
      <circle cx="420" cy="510" r="8" fill="#FBBF24" opacity="0.7" class="floating-dot-2" />
      <circle cx="940" cy="490" r="5" fill="#34D399" opacity="0.6" class="floating-dot-3" />
    </svg>

    <!-- Top Partner Header Banner -->
    <div class="relative z-10 w-full flex items-center justify-between px-10 pt-6">
      <div class="partner-badge flex items-center gap-2 bg-white/95 backdrop-blur-md px-4 py-1.5 rounded-full border border-slate-200/90 shadow-sm transition-transform hover:scale-105 duration-300">
        <img :src="`${base}img/partner-logos.png`" alt="밀양시 · 밀양소통협력센터 · 에이제이인포텍" class="h-6.5 w-auto object-contain block" />
      </div>

      <div class="flex items-center gap-2">
        <span class="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-bold border border-emerald-200/80 shadow-2xs font-mono">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          2026 청년 취업 특화 과정
        </span>
      </div>
    </div>

    <!-- Main Two-Column Hero Stage -->
    <div class="relative z-10 w-full h-[450px] px-10 flex items-center justify-between">
      
      <!-- Left Column: Energetic Handwritten Typography -->
      <div class="max-w-[560px] flex flex-col items-start justify-center">
        <!-- Kicker Badge -->
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-xl bg-gradient-to-r from-blue-50 to-emerald-50 border border-blue-200/80 text-blue-800 text-xs font-bold tracking-tight mb-3 shadow-2xs">
          <span class="text-sm">🌱</span>
          <span class="font-extrabold font-mono tracking-wide">밀양 청년 취업역량 강화교육 · 5주차</span>
        </div>

        <!-- Handwritten Super Headline -->
        <div class="relative mb-3">
          <h1 class="handwritten-title m-0">
            나만의 디지털
            <span class="highlight-box-blue">
              포트폴리오 빌딩
              <svg class="hand-drawn-line line-blue" viewBox="0 0 260 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M 3,10 Q 70,3 130,8 Q 190,13 255,5" stroke="#2563EB" stroke-width="4.5" stroke-linecap="round" />
              </svg>
            </span>
            <br />
            <span class="text-slate-800">&amp; AI 에이전트 </span>
            <span class="highlight-box-emerald">
              바이브 코딩
              <svg class="hand-drawn-line line-emerald" viewBox="0 0 200 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M 4,8 Q 50,12 100,7 Q 150,2 195,9" stroke="#059669" stroke-width="4.5" stroke-linecap="round" />
              </svg>
            </span>
          </h1>
        </div>

        <!-- Subtitle Description (Crystal Clear & Prominent) -->
        <p class="text-slate-600 text-base leading-relaxed font-medium m-0 max-w-[520px]">
          경험의 <b class="text-slate-900">노션 데이터 자산화</b>부터 <b class="text-blue-600">모바일 마이크로 랜딩</b>, 
          <b class="text-slate-900">제미나이 캔버스 웹 빌딩</b>, <b class="text-emerald-600">마누스 AI 에이전트</b> 자율 완성까지!
        </p>

        <!-- Fresh Decorative Mini Accents -->
        <div class="mt-4 flex items-center gap-3 text-xs text-slate-500 font-medium">
          <span class="flex items-center gap-1">
            <span class="text-emerald-500 font-bold">✓</span> 노코드에서 바이브 코딩으로
          </span>
          <span class="text-slate-300">|</span>
          <span class="flex items-center gap-1">
            <span class="text-blue-500 font-bold">✓</span> 완성형 디지털 포트폴리오
          </span>
        </div>
      </div>

      <!-- Right Column: Rich Animated Dynamic SVG Illustration -->
      <div class="relative w-[360px] h-[360px] flex items-center justify-center">
        <!-- Ambient Orbit Ring -->
        <div class="orbit-glow-disc"></div>

        <svg class="w-full h-full overflow-visible" viewBox="0 0 360 360" fill="none" xmlns="http://www.w3.org/2000/svg">
          
          <!-- Animated Central Laptop / Screen -->
          <g class="laptop-group" transform="translate(60, 100)">
            <!-- Screen Body -->
            <rect x="0" y="0" width="240" height="150" rx="14" fill="#0F172A" stroke="#334155" stroke-width="3" />
            <!-- Inner Webpage Content -->
            <rect x="8" y="8" width="224" height="134" rx="8" fill="#F8FAFC" />
            <!-- Web Header Bar -->
            <rect x="8" y="8" width="224" height="20" rx="8" fill="#F1F5F9" />
            <circle cx="20" cy="18" r="3" fill="#EF4444" />
            <circle cx="29" cy="18" r="3" fill="#F59E0B" />
            <circle cx="38" cy="18" r="3" fill="#10B981" />
            <rect x="52" y="13" width="90" height="10" rx="4" fill="#E2E8F0" />

            <!-- Web Hero Area on Screen -->
            <rect x="20" y="38" width="85" height="14" rx="4" fill="#2563EB" opacity="0.9" />
            <rect x="20" y="58" width="130" height="7" rx="3" fill="#94A3B8" />
            <rect x="20" y="69" width="100" height="7" rx="3" fill="#CBD5E1" />
            
            <!-- Cards on Screen -->
            <rect x="20" y="86" width="60" height="44" rx="6" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1.5" />
            <rect x="26" y="93" width="30" height="6" rx="2" fill="#3B82F6" />
            <rect x="26" y="103" width="45" height="4" rx="2" fill="#93C5FD" />
            <rect x="26" y="111" width="35" height="4" rx="2" fill="#93C5FD" />

            <rect x="88" y="86" width="60" height="44" rx="6" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5" />
            <rect x="94" y="93" width="30" height="6" rx="2" fill="#10B981" />
            <rect x="94" y="103" width="45" height="4" rx="2" fill="#6EE7B7" />
            <rect x="94" y="111" width="35" height="4" rx="2" fill="#6EE7B7" />

            <rect x="156" y="86" width="60" height="44" rx="6" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5" />
            <rect x="162" y="93" width="30" height="6" rx="2" fill="#F59E0B" />
            <rect x="162" y="103" width="45" height="4" rx="2" fill="#FCD34D" />
            <rect x="162" y="111" width="35" height="4" rx="2" fill="#FCD34D" />

            <!-- Laptop Base -->
            <path d="M -25,150 L 265,150 L 250,165 L -10,165 Z" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="2" />
            <rect x="95" y="152" width="50" height="4" rx="2" fill="#94A3B8" />
          </g>

          <!-- Floating Item 1: Notion Asset Badge (Top Left) -->
          <g class="float-badge-1" transform="translate(20, 45)">
            <rect width="84" height="42" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="2" filter="url(#softGlow)" />
            <rect width="84" height="42" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
            <text x="12" y="26" font-size="18">📝</text>
            <text x="36" y="21" font-family="Pretendard, sans-serif" font-size="10" font-weight="bold" fill="#0F172A">Notion DB</text>
            <text x="36" y="32" font-family="Pretendard, sans-serif" font-size="8" font-weight="bold" fill="#10B981">자산화 완료</text>
          </g>

          <!-- Floating Item 2: AI Agent Mascot (Top Right) -->
          <g class="float-badge-2" transform="translate(260, 30)">
            <rect width="90" height="50" rx="14" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="2" />
            <!-- Bot Face -->
            <rect x="8" y="9" width="32" height="32" rx="8" fill="url(#agentGrad)" />
            <!-- Eyes -->
            <circle cx="19" cy="23" r="2.5" fill="#FFFFFF" />
            <circle cx="29" cy="23" r="2.5" fill="#FFFFFF" />
            <!-- Antenna -->
            <line x1="24" y1="9" x2="24" y2="4" stroke="#059669" stroke-width="2" stroke-linecap="round" />
            <circle cx="24" cy="3" r="2" fill="#34D399" />
            <!-- Text -->
            <text x="46" y="24" font-family="Pretendard, sans-serif" font-size="10.5" font-weight="800" fill="#065F46">AI Agent</text>
            <text x="46" y="36" font-family="Pretendard, sans-serif" font-size="8" font-weight="bold" fill="#059669">자율 코딩중 ⚡</text>
          </g>

          <!-- Floating Item 3: Mobile Card (Bottom Right) -->
          <g class="float-badge-3" transform="translate(250, 240)">
            <rect width="80" height="95" rx="12" fill="#FFFFFF" stroke="#BFDBFE" stroke-width="2" />
            <rect x="6" y="6" width="68" height="83" rx="8" fill="#F8FAFC" />
            <circle cx="40" cy="26" r="11" fill="#DBEAFE" />
            <text x="34" y="31" font-size="12">🧑‍💻</text>
            <rect x="18" y="44" width="44" height="6" rx="2" fill="#2563EB" />
            <rect x="14" y="55" width="52" height="5" rx="2" fill="#E2E8F0" />
            <rect x="14" y="64" width="52" height="5" rx="2" fill="#E2E8F0" />
            <rect x="14" y="73" width="52" height="8" rx="3" fill="#10B981" />
            <text x="24" y="79" font-family="Pretendard, sans-serif" font-size="6" font-weight="bold" fill="#FFFFFF">1초 배포</text>
          </g>

          <!-- Floating Rocket Blasting Off (Bottom Left) -->
          <g class="float-rocket" transform="translate(15, 220)">
            <circle cx="35" cy="35" r="30" fill="#FEF3C7" opacity="0.8" />
            <text x="18" y="44" font-size="30">🚀</text>
          </g>
        </svg>
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Bright & Fresh Canvas Base */
.bright-intro-canvas {
  background: linear-gradient(145deg, #FFFFFF 0%, #F8FAFC 45%, #F0FDF4 100%);
  color: #0F172A;
  box-sizing: border-box;
}

/* Ambient Radial Mesh Glow */
.ambient-mesh-glow {
  position: absolute;
  top: -100px;
  right: -80px;
  width: 550px;
  height: 550px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(16, 185, 129, 0.12) 40%, rgba(255, 255, 255, 0) 70%);
  pointer-events: none;
  filter: blur(40px);
  animation: pulseGlow 8s ease-in-out infinite alternate;
}

@keyframes pulseGlow {
  0% { transform: scale(0.95) translate(0, 0); opacity: 0.7; }
  100% { transform: scale(1.1) translate(-20px, 20px); opacity: 1; }
}

/* Handwritten Main Headline Styling */
.handwritten-title {
  font-family: 'Gaegu', 'Pretendard', cursive, sans-serif;
  font-size: 3.25rem;
  font-weight: 700;
  line-height: 1.18;
  letter-spacing: -0.02em;
  color: #0F172A;
  word-break: keep-all;
}

/* Highlight boxes with dynamic hand-drawn styling */
.highlight-box-blue {
  position: relative;
  display: inline-block;
  color: #1D4ED8;
}

.highlight-box-emerald {
  position: relative;
  display: inline-block;
  color: #047857;
}

.hand-drawn-line {
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 100%;
  height: 14px;
  pointer-events: none;
}

.line-blue path {
  stroke-dasharray: 300;
  stroke-dashoffset: 300;
  animation: drawLine 1.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.3s;
}

.line-emerald path {
  stroke-dasharray: 250;
  stroke-dashoffset: 250;
  animation: drawLine 1.2s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.6s;
}

@keyframes drawLine {
  to { stroke-dashoffset: 0; }
}

/* Flow line animations */
.animated-flow-line-1 {
  animation: flowDash 20s linear infinite;
}
.animated-flow-line-2 {
  animation: flowDash 25s linear infinite reverse;
}

@keyframes flowDash {
  to { stroke-dashoffset: -1000; }
}

/* Floating Stars & Dots Animations */
.floating-star-1 {
  animation: floatStar 4s ease-in-out infinite;
}
.floating-star-2 {
  animation: floatStar 5s ease-in-out infinite 0.8s;
}
.floating-star-3 {
  animation: floatStar 4.5s ease-in-out infinite 1.5s;
}
.floating-star-4 {
  animation: floatStar 6s ease-in-out infinite 2s;
}

@keyframes floatStar {
  0%, 100% { transform: translate(var(--tx, 0), var(--ty, 0)) scale(1) rotate(0deg); }
  50% { transform: translate(var(--tx, 0), calc(var(--ty, 0) - 8px)) scale(1.15) rotate(15deg); }
}

.floating-dot-1 { animation: floatDot 5s ease-in-out infinite; }
.floating-dot-2 { animation: floatDot 6s ease-in-out infinite 1s; }
.floating-dot-3 { animation: floatDot 4s ease-in-out infinite 2s; }

@keyframes floatDot {
  0%, 100% { transform: translateY(0); opacity: 0.6; }
  50% { transform: translateY(-10px); opacity: 0.9; }
}

/* Right Illustration Floating Components */
.orbit-glow-disc {
  position: absolute;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(219, 234, 254, 0.6) 0%, rgba(209, 250, 229, 0.4) 50%, transparent 70%);
  filter: blur(20px);
}

.laptop-group {
  animation: floatLaptop 6s ease-in-out infinite;
  transform-origin: center;
}

@keyframes floatLaptop {
  0%, 100% { transform: translate(60px, 100px) rotate(0deg); }
  50% { transform: translate(60px, 92px) rotate(1deg); }
}

.float-badge-1 {
  animation: floatBadge1 5s ease-in-out infinite;
}
@keyframes floatBadge1 {
  0%, 100% { transform: translate(20px, 45px) rotate(-3deg); }
  50% { transform: translate(20px, 35px) rotate(0deg); }
}

.float-badge-2 {
  animation: floatBadge2 5.5s ease-in-out infinite 0.5s;
}
@keyframes floatBadge2 {
  0%, 100% { transform: translate(260px, 30px) rotate(3deg); }
  50% { transform: translate(260px, 20px) rotate(-1deg); }
}

.float-badge-3 {
  animation: floatBadge3 6s ease-in-out infinite 1s;
}
@keyframes floatBadge3 {
  0%, 100% { transform: translate(250px, 240px) rotate(-2deg); }
  50% { transform: translate(250px, 230px) rotate(1deg); }
}

.float-rocket {
  animation: floatRocket 4.5s ease-in-out infinite 0.7s;
}
@keyframes floatRocket {
  0%, 100% { transform: translate(15px, 220px) rotate(0deg); }
  50% { transform: translate(18px, 208px) rotate(-6deg); }
}
</style>
