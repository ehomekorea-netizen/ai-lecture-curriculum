<script setup lang="ts">
import { ref, onMounted, onUnmounted, nextTick, watch } from 'vue'
import rough from 'roughjs'

const props = withDefaults(
  defineProps<{
    stage?: number
  }>(),
  {
    stage: 0
  }
)

const root = ref<HTMLElement | null>(null)
const canvasEl = ref<HTMLCanvasElement | null>(null)

const layout = ref({
  W: 880,
  H: 295,
  wingW: 230,
  folderW: 270,
  folderX: 305,
  folderY: 30,
  folderH: 220,
  leftX: 16,
  rightX: 634,
  boxH: 95,
  topY: 25,
  botY: 150
})

function drawArrow(rc: any, x1: number, y1: number, x2: number, y2: number, color: string) {
  rc.line(x1, y1, x2, y2, { stroke: color, strokeWidth: 2.2, roughness: 1.4 })
  const angle = Math.atan2(y2 - y1, x2 - x1)
  const headLen = 11
  const a1 = angle - Math.PI / 6
  const a2 = angle + Math.PI / 6
  rc.line(x2, y2, x2 - headLen * Math.cos(a1), y2 - headLen * Math.sin(a1), { stroke: color, strokeWidth: 2.2, roughness: 1.2 })
  rc.line(x2, y2, x2 - headLen * Math.cos(a2), y2 - headLen * Math.sin(a2), { stroke: color, strokeWidth: 2.2, roughness: 1.2 })
}

function updateLayoutAndDraw() {
  const canvas = canvasEl.value
  const container = root.value
  if (!canvas || !container) return

  const W = container.clientWidth || 880
  const H = 295

  // High-DPI Retina resolution setup
  const dpr = Math.max(2, window.devicePixelRatio || 1)
  canvas.width = W * dpr
  canvas.height = H * dpr
  canvas.style.width = `${W}px`
  canvas.style.height = `${H}px`

  const rc = rough.canvas(canvas)
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.scale(dpr, dpr)
  ctx.clearRect(0, 0, W, H)

  // Sizing
  const wingW = Math.min(235, Math.max(200, (W - 320) / 2))
  const folderW = Math.min(280, W - wingW * 2 - 50)
  const folderX = (W - folderW) / 2
  const leftX = 16
  const rightX = W - wingW - 16

  const boxH = 96
  const topY = 22
  const botY = 146
  const folderY = 32
  const folderH = 216

  layout.value = {
    W, H, wingW, folderW, folderX, folderY, folderH, leftX, rightX, boxH, topY, botY
  }

  // ── 1. LEFT WING SKETCH BOXES (항상 먼저 노출) ──
  // Left Top
  rc.rectangle(leftX, topY, wingW, boxH, {
    fill: '#F8FAFC',
    fillStyle: 'solid',
    stroke: '#2563EB',
    strokeWidth: 2.2,
    roughness: 1.6
  })

  // Left Bottom
  rc.rectangle(leftX, botY, wingW, boxH, {
    fill: '#F8FAFC',
    fillStyle: 'solid',
    stroke: '#7C3AED',
    strokeWidth: 2.2,
    roughness: 1.6
  })

  // ── 2. RIGHT WING SKETCH BOXES (항상 먼저 노출) ──
  // Right Top
  rc.rectangle(rightX, topY, wingW, boxH, {
    fill: '#F8FAFC',
    fillStyle: 'solid',
    stroke: '#059669',
    strokeWidth: 2.2,
    roughness: 1.6
  })

  // Right Bottom
  rc.rectangle(rightX, botY, wingW, boxH, {
    fill: '#F8FAFC',
    fillStyle: 'solid',
    stroke: '#E11D48',
    strokeWidth: 2.2,
    roughness: 1.6
  })

  // ── 3. CENTER FOLDER & CONNECTING ARROWS (클릭 시 2단계에서 등장) ──
  if (props.stage >= 1) {
    // Folder Tab
    rc.rectangle(folderX + 12, folderY - 14, 90, 22, {
      fill: '#FEF3C7',
      fillStyle: 'solid',
      stroke: '#D97706',
      strokeWidth: 2.2,
      roughness: 1.6
    })

    // Folder Body
    rc.rectangle(folderX, folderY, folderW, folderH, {
      fill: '#FFFDF5',
      fillStyle: 'solid',
      stroke: '#D97706',
      strokeWidth: 2.5,
      roughness: 1.8
    })

    // Folder Inner Pocket
    rc.rectangle(folderX + 14, folderY + 70, folderW - 28, folderH - 84, {
      fill: '#FEF3C7',
      fillStyle: 'solid',
      stroke: '#B45309',
      strokeWidth: 1.8,
      roughness: 1.4
    })

    // 4 Connecting Hand-Drawn Arrows
    drawArrow(rc, leftX + wingW + 6, topY + boxH / 2, folderX - 8, folderY + 45, '#2563EB')
    drawArrow(rc, leftX + wingW + 6, botY + boxH / 2, folderX - 8, folderY + 145, '#7C3AED')
    drawArrow(rc, rightX - 6, topY + boxH / 2, folderX + folderW + 8, folderY + 45, '#059669')
    drawArrow(rc, rightX - 6, botY + boxH / 2, folderX + folderW + 8, folderY + 145, '#E11D48')
  }
}

watch(() => props.stage, () => {
  nextTick(() => {
    updateLayoutAndDraw()
  })
})

onMounted(() => {
  nextTick(() => {
    updateLayoutAndDraw()
  })
  window.addEventListener('resize', updateLayoutAndDraw)
})

onUnmounted(() => {
  window.removeEventListener('resize', updateLayoutAndDraw)
})
</script>

<template>
  <div ref="root" class="sketch-folder-container w-full mt-1 select-none">
    <!-- Hand-Drawn Sketch Wrapper -->
    <div class="relative p-2 rounded-2xl bg-[#FCFAF7] border-2 border-dashed border-stone-300 shadow-sm overflow-hidden h-[335px] flex flex-col justify-between">
      
      <!-- Canvas Layer (High-DPI Retina RoughJS Sketch Background) -->
      <canvas ref="canvasEl" class="absolute inset-0 pointer-events-none z-0" />

      <!-- HTML Vector Text Overlay -->
      <div class="relative z-10 w-full h-[295px]">
        
        <!-- ── 1. CENTER FOLDER HTML CONTENT (클릭 시 스테이지 1에서 등장) ── -->
        <transition name="folder-pop">
          <div
            v-if="props.stage >= 1"
            class="absolute flex flex-col items-center justify-between text-center p-3"
            :style="{
              left: `${layout.folderX}px`,
              top: `${layout.folderY}px`,
              width: `${layout.folderW}px`,
              height: `${layout.folderH}px`
            }"
          >
            <!-- Top Header -->
            <div>
              <div class="text-sm font-extrabold text-amber-900 font-mono tracking-tight flex items-center justify-center gap-1.5">
                <span class="text-base">📂</span>
                <span>my-portfolio /</span>
              </div>
              <div class="text-[10.5px] font-bold text-amber-700 mt-0.5">
                ✨ Manus 에셋 집결 폴더
              </div>
            </div>

            <!-- Center Pocket (Clean & Direct without double glass box) -->
            <div class="w-full flex flex-col items-center justify-center mt-2 py-1">
              <div class="text-[12px] font-extrabold text-amber-950">
                📥 모든 에셋을 한곳에 투입
              </div>
              <div class="text-[13px] font-black text-emerald-700 mt-1.5 flex items-center justify-center gap-1">
                <span>🧠 Manus Plan 모드</span>
              </div>
              <p class="text-[11px] text-stone-600 font-medium m-0 mt-1 leading-snug">
                에이전트가 알아서 파싱 & 기획
              </p>
            </div>

            <!-- Bottom Spacer -->
            <div class="h-2" />
          </div>
        </transition>

        <!-- ── 2. LEFT TOP: 📄 노션 경험 DB (항상 노출) ── -->
        <div
          class="absolute p-2.5 flex flex-col justify-between"
          :style="{
            left: `${layout.leftX}px`,
            top: `${layout.topY}px`,
            width: `${layout.wingW}px`,
            height: `${layout.boxH}px`
          }"
        >
          <div>
            <div class="text-xs font-extrabold text-blue-700 flex items-center gap-1">
              <span>📄</span>
              <span>1. 노션 경험 DB</span>
            </div>
            <div class="text-[10px] font-mono text-blue-500 font-bold mt-0.5">
              notion_backup.md / .csv
            </div>
          </div>
          <div class="text-[10.5px] text-slate-600 leading-snug font-medium">
            • 4주차에 구축한 경력/프로젝트 DB
          </div>
        </div>

        <!-- ── 3. LEFT BOTTOM: 📑 포트폴리오 PDF (항상 노출) ── -->
        <div
          class="absolute p-2.5 flex flex-col justify-between"
          :style="{
            left: `${layout.leftX}px`,
            top: `${layout.botY}px`,
            width: `${layout.wingW}px`,
            height: `${layout.boxH}px`
          }"
        >
          <div>
            <div class="text-xs font-extrabold text-purple-700 flex items-center gap-1">
              <span>📑</span>
              <span>2. 포트폴리오 PDF</span>
            </div>
            <div class="text-[10px] font-mono text-purple-500 font-bold mt-0.5">
              resume_2026.pdf
            </div>
          </div>
          <div class="text-[10.5px] text-slate-600 leading-snug font-medium">
            • 기존 이력서 & 경력 기술 문서
          </div>
        </div>

        <!-- ── 4. RIGHT TOP: 🖼️ 프로필 증명사진 (항상 노출) ── -->
        <div
          class="absolute p-2.5 flex flex-col justify-between"
          :style="{
            left: `${layout.rightX}px`,
            top: `${layout.topY}px`,
            width: `${layout.wingW}px`,
            height: `${layout.boxH}px`
          }"
        >
          <div>
            <div class="text-xs font-extrabold text-emerald-700 flex items-center gap-1">
              <span>🖼️</span>
              <span>3. 프로필 증명사진</span>
            </div>
            <div class="text-[10px] font-mono text-emerald-500 font-bold mt-0.5">
              profile.jpg / photo.png
            </div>
          </div>
          <div class="text-[10.5px] text-slate-600 leading-snug font-medium">
            • 웹사이트 Hero 메인 프로필 사진
          </div>
        </div>

        <!-- ── 5. RIGHT BOTTOM: 📜 수료증 & 자격증 (항상 노출) ── -->
        <div
          class="absolute p-2.5 flex flex-col justify-between"
          :style="{
            left: `${layout.rightX}px`,
            top: `${layout.botY}px`,
            width: `${layout.wingW}px`,
            height: `${layout.boxH}px`
          }"
        >
          <div>
            <div class="text-xs font-extrabold text-rose-700 flex items-center gap-1">
              <span>📜</span>
              <span>4. 수료증 & 자격증 사본</span>
            </div>
            <div class="text-[10px] font-mono text-rose-500 font-bold mt-0.5">
              certificate_ai.png
            </div>
          </div>
          <div class="text-[10.5px] text-slate-600 leading-snug font-medium">
            • 자격증 및 교육 이수 증빙 이미지
          </div>
        </div>

      </div>

      <!-- Bottom Hand-drawn Note Bar -->
      <div class="relative z-10 pt-1.5 border-t border-stone-200 flex items-center justify-center text-[11px] text-stone-600 px-2 font-sans">
        <div class="flex items-center gap-1.5">
          <span class="font-bold text-amber-700 font-mono">✏️ 핵심:</span>
          <span>어떤 형식이든 <b>이 폴더 하나에 다 넣어두기만 하면</b>, Manus가 스스로 내용을 읽고 기획(Plan)합니다!</span>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.folder-pop-enter-active,
.folder-pop-leave-active {
  transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.folder-pop-enter-from {
  opacity: 0;
  transform: scale(0.85);
}
</style>
