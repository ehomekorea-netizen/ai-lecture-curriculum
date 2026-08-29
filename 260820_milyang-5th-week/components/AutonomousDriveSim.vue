<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, watch, nextTick } from 'vue'
import rough from 'roughjs'
import { Bot, User } from 'lucide-vue-next'

const scene = ref<HTMLElement | null>(null)
const sceneSvg = ref<SVGSVGElement | null>(null)
const measure = ref<SVGPathElement | null>(null)
const carSvg = ref<SVGSVGElement | null>(null)
const wheelSvg = ref<SVGSVGElement | null>(null)
const wheelEl = ref<HTMLElement | null>(null)

const INK = '#2B2620', SAPPHIRE = '#2563EB', DIM = '#64748B'
const ASPHALT = '#EFEAE1'
const LEAF = ['#3E7D4F', '#4F9160', '#68A874']

const HALF_W = 24          // half the road width, px
const TURN_TO_B = 360      // 360 degrees = 1 full turn to go from A to B (much more responsive!)
const START = 0.02         // sit the car just inside the start line
const N_LIVE = 3           // how many frogs are hopping at once
const MAX_SPLATS = 8
const HOP = 20             // px per hop
const SQUASH_R = 20        // how close the car has to pass

type Player = 'human' | 'llm'
const player = ref<Player | null>(null)
const mode = ref<'idle' | 'manual' | 'arrived' | 'auto' | 'gone'>('idle')
const wheelAngle = ref(0)
const progress = ref(START)
const car = ref({ x: -999, y: -999, a: 0 })

const snap = ref(false)
const carStyle = computed(() => ({
  left: car.value.x + 'px',
  top: car.value.y + 'px',
  transform: `translate(-50%,-50%) rotate(${car.value.a}deg)`,
  transition:
    snap.value ? 'none'
    : mode.value === 'gone' ? 'left 1.3s cubic-bezier(.5,0,1,.6), top 1.3s cubic-bezier(.5,0,1,.6)'
    : mode.value === 'auto' ? 'left .55s ease-in-out, top .55s ease-in-out, transform .55s ease-in-out'
    : 'left .06s linear, top .06s linear, transform .06s linear',
}))
const wheelStyle = computed(() => ({
  transform: `rotate(${wheelAngle.value}deg)`,
  transition:
    mode.value === 'gone' ? 'transform 1.3s cubic-bezier(.5,0,1,.6)'
    : mode.value === 'auto' ? 'transform .55s ease-in-out'
    : 'transform .05s linear',
}))

// ── road geometry ────────────────────────────────────────────────────────
function pathFor(W: number) {
  const y = (f: number) => 30 + f * 160
  return [
    `M ${0.05 * W} ${y(0.72)}`,
    `C ${0.15 * W} ${y(0.72)}, ${0.15 * W} ${y(0.1)}, ${0.29 * W} ${y(0.1)}`,
    `C ${0.43 * W} ${y(0.1)}, ${0.41 * W} ${y(0.92)}, ${0.55 * W} ${y(0.92)}`,
    `C ${0.69 * W} ${y(0.92)}, ${0.67 * W} ${y(0.16)}, ${0.81 * W} ${y(0.16)}`,
    `C ${0.89 * W} ${y(0.16)}, ${0.91 * W} ${y(0.5)}, ${0.95 * W} ${y(0.5)}`,
  ].join(' ')
}
function sample(t: number) {
  const el = measure.value
  if (!el) return null
  const L = el.getTotalLength()
  if (!L) return null
  const d = Math.max(0, Math.min(1, t)) * L
  const p = el.getPointAtLength(d)
  const q = el.getPointAtLength(Math.min(L, d + 1.5))
  const r = el.getPointAtLength(Math.max(0, d - 1.5))
  return { x: p.x, y: p.y, a: Math.atan2(q.y - r.y, q.x - r.x) * 180 / Math.PI }
}

type Spine = { x: number; y: number; nx: number; ny: number }
let spine: Spine[] = []
const pond = ref({ x: 0, y: 0, rx: 32, ry: 21 })

function nearest(x: number, y: number) {
  let best: Spine | null = null, bd = Infinity
  for (const s of spine) {
    const d = Math.hypot(s.x - x, s.y - y)
    if (d < bd) { bd = d; best = s }
  }
  return { s: best, d: bd }
}
function sideOf(x: number, y: number) {
  const { s } = nearest(x, y)
  if (!s) return 0
  return Math.sign((x - s.x) * s.nx + (y - s.y) * s.ny)
}

// ── frogs ────────────────────────────────────────────────────────────────
type Frog = { id: number; x: number; y: number; a: number; dead: boolean }
const frogs = ref<Frog[]>([])
let frogId = 0

function spawnFrog(): Frog | null {
  const cont = scene.value
  if (!cont || !spine.length) return null
  const W = cont.clientWidth
  const pondSide = sideOf(pond.value.x, pond.value.y)
  for (let i = 0; i < 250; i++) {
    const x = 20 + Math.random() * (W - 40)
    const y = 16 + Math.random() * 200
    if (nearest(x, y).d < HALF_W + 16) continue
    if (sideOf(x, y) === pondSide) continue
    if (Math.hypot(x - pond.value.x, y - pond.value.y) < 170) continue
    return { id: ++frogId, x, y, a: 0, dead: false }
  }
  return null
}

const DOOMED: { t: number; at: number }[] = [
  { t: 0.16, at: 700 }, { t: 0.31, at: 1350 }, { t: 0.45, at: 1950 }, { t: 0.58, at: 2520 },
]
function seedDoomedFrogs() {
  for (const m of DOOMED) {
    const s = sample(m.t)
    if (!s) continue
    const dx = pond.value.x - s.x, dy = pond.value.y - s.y
    const d = Math.hypot(dx, dy) || 1
    const back = (m.at / 520) * HOP
    frogs.value.push({
      id: ++frogId,
      x: s.x - (dx / d) * back,
      y: s.y - (dy / d) * back,
      a: Math.atan2(dy, dx) * 180 / Math.PI + 90,
      dead: false,
    })
  }
}

function refillFrogs() {
  let guard = 0
  while (frogs.value.filter(f => !f.dead).length < N_LIVE && guard++ < 10) {
    const f = spawnFrog()
    if (!f) break
    frogs.value.push(f)
  }
}
function hopFrogs() {
  const arrived: number[] = []
  for (const f of frogs.value) {
    if (f.dead) continue
    const dx = pond.value.x - f.x, dy = pond.value.y - f.y
    const d = Math.hypot(dx, dy) || 1
    f.a = Math.atan2(dy, dx) * 180 / Math.PI + 90
    if (d < 26) { arrived.push(f.id); continue }
    const step = Math.min(HOP, d)
    f.x += (dx / d) * step
    f.y += (dy / d) * step
  }
  if (arrived.length) frogs.value = frogs.value.filter(f => !arrived.includes(f.id))
  const splats = frogs.value.filter(f => f.dead)
  if (splats.length > MAX_SPLATS) {
    const drop = new Set(splats.slice(0, splats.length - MAX_SPLATS).map(f => f.id))
    frogs.value = frogs.value.filter(f => !drop.has(f.id))
  }
  refillFrogs()
}

function distToSeg(px: number, py: number, x1: number, y1: number, x2: number, y2: number) {
  const vx = x2 - x1, vy = y2 - y1
  const len2 = vx * vx + vy * vy
  if (!len2) return Math.hypot(px - x1, py - y1)
  let t = ((px - x1) * vx + (py - y1) * vy) / len2
  t = Math.max(0, Math.min(1, t))
  return Math.hypot(px - (x1 + t * vx), py - (y1 + t * vy))
}
function squash(from: { x: number; y: number }, to: { x: number; y: number }) {
  const dir = Math.atan2(to.y - from.y, to.x - from.x) * 180 / Math.PI
  for (const f of frogs.value) {
    if (!f.dead && distToSeg(f.x, f.y, from.x, from.y, to.x, to.y) < SQUASH_R) {
      f.dead = true
      f.a = dir
    }
  }
}

function place(t: number) {
  const s = sample(t)
  if (s) car.value = s
}

const carEl = ref<HTMLElement | null>(null)
let raf = 0
let lastFrame: { x: number; y: number } | null = null
let settle = 0

function trackCar() {
  raf = requestAnimationFrame(trackCar)
  const el = carEl.value, cont = scene.value
  if (!el || !cont || !player.value) { lastFrame = null; return }
  const r = el.getBoundingClientRect()
  if (!r.width) { lastFrame = null; return }
  const base = cont.getBoundingClientRect()
  const s = base.width / cont.clientWidth || 1
  const now = {
    x: (r.left + r.width / 2 - base.left) / s,
    y: (r.top + r.height / 2 - base.top) / s,
  }
  if (settle > 0) settle--
  else if (lastFrame) squash(lastFrame, now)
  lastFrame = now
}

// ── the crash ────────────────────────────────────────────────────────────
const boom = ref<{ x: number; y: number } | null>(null)
const boomSvg = ref<SVGSVGElement | null>(null)
let boomAt: { x: number; y: number } | null = null
let boomTimer: ReturnType<typeof setTimeout> | undefined

function exitPoint(x: number, y: number, a: number) {
  const cont = scene.value
  if (!cont) return null
  const W = cont.clientWidth, H = cont.clientHeight
  const dx = Math.cos(a), dy = Math.sin(a)
  let best = Infinity
  for (const t of [dx > 0 ? (W - x) / dx : dx < 0 ? -x / dx : Infinity,
                   dy > 0 ? (H - y) / dy : dy < 0 ? -y / dy : Infinity]) {
    if (t > 0 && t < best) best = t
  }
  if (!isFinite(best)) return null
  const inset = Math.max(0, best - 84)
  return { x: x + dx * inset, y: y + dy * inset }
}

// ── choosing a player ────────────────────────────────────────────────────
let timer: ReturnType<typeof setInterval> | undefined
function pick(p: Player) {
  clearInterval(timer)
  clearTimeout(boomTimer)
  boom.value = null
  boomAt = null
  player.value = p
  progress.value = START
  wheelAngle.value = 0
  frogs.value = []
  clearInterval(hop)
  hop = setInterval(hopFrogs, 520)
  if (p === 'llm') seedDoomedFrogs()
  refillFrogs()
  snap.value = true
  settle = 8
  lastFrame = null
  place(START)
  nextTick(() => requestAnimationFrame(() => { snap.value = false }))
  if (p === 'human') { mode.value = 'manual'; return }
  mode.value = 'auto'
  let step = 0
  timer = setInterval(() => {
    step++
    if (step <= 4) {
      progress.value = START + (0.62 - START) * (step / 4)
      wheelAngle.value += 75
      place(progress.value)
    } else {
      clearInterval(timer)
      mode.value = 'gone'
      const a = car.value.a * Math.PI / 180
      const edge = exitPoint(car.value.x, car.value.y, a)
      const run = edge ? Math.hypot(edge.x - car.value.x, edge.y - car.value.y) + 150 : 1800
      car.value = { x: car.value.x + Math.cos(a) * run, y: car.value.y + Math.sin(a) * run, a: car.value.a }
      wheelAngle.value += 1080
      if (edge) boomAt = edge
      boomTimer = setTimeout(() => { if (boomAt) boom.value = boomAt }, 1120)
    }
  }, 620)
}

// ── Manual Steering (Highly Responsive Polar & Drag Tracking) ────────────
let isDraggingWheel = false
let lastPointerPos = { x: 0, y: 0 }
let lastPolarAngle: number | null = null

function getPolarAngle(e: PointerEvent) {
  if (!wheelEl.value) return 0
  const r = wheelEl.value.getBoundingClientRect()
  const cx = r.left + r.width / 2
  const cy = r.top + r.height / 2
  return Math.atan2(e.clientY - cy, e.clientX - cx) * 180 / Math.PI
}

function wheelDown(e: PointerEvent) {
  if (mode.value !== 'manual') return
  isDraggingWheel = true
  lastPointerPos = { x: e.clientX, y: e.clientY }
  lastPolarAngle = getPolarAngle(e)
  ;(e.target as HTMLElement).setPointerCapture?.(e.pointerId)
}

function wheelMove(e: PointerEvent) {
  if (!isDraggingWheel || mode.value !== 'manual') return

  // Calculate circular angle delta
  const currentPolar = getPolarAngle(e)
  let angleDelta = 0
  if (lastPolarAngle !== null) {
    angleDelta = currentPolar - lastPolarAngle
    while (angleDelta > 180) angleDelta -= 360
    while (angleDelta < -180) angleDelta += 360
  }
  lastPolarAngle = currentPolar

  // Also calculate linear drag delta for maximum responsiveness
  const dx = e.clientX - lastPointerPos.x
  const dy = e.clientY - lastPointerPos.y
  lastPointerPos = { x: e.clientX, y: e.clientY }
  const dragDelta = (dx - dy * 0.5) * 1.5

  // Combine deltas for smooth, instantaneous feel
  const appliedDelta = Math.abs(angleDelta) > 1 ? angleDelta : dragDelta

  wheelAngle.value = Math.max(0, Math.min(TURN_TO_B, wheelAngle.value + appliedDelta))
  progress.value = Math.max(START, Math.min(0.995, START + (wheelAngle.value / TURN_TO_B) * (0.995 - START)))
  place(progress.value)

  if (progress.value >= 0.985) {
    mode.value = 'arrived'
    isDraggingWheel = false
  }
}

function wheelUp(e: PointerEvent) {
  isDraggingWheel = false
  lastPolarAngle = null
}

function onWheelScroll(e: WheelEvent) {
  if (mode.value !== 'manual') return
  const delta = (e.deltaY || e.deltaX) * 0.8
  wheelAngle.value = Math.max(0, Math.min(TURN_TO_B, wheelAngle.value + delta))
  progress.value = Math.max(START, Math.min(0.995, START + (wheelAngle.value / TURN_TO_B) * (0.995 - START)))
  place(progress.value)
  if (progress.value >= 0.985) {
    mode.value = 'arrived'
  }
}

// ── hand-drawn rendering ─────────────────────────────────────────────────
function rng(seed: number) {
  return () => {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

function drawScene() {
  const svg = sceneSvg.value, cont = scene.value, mp = measure.value
  if (!svg || !cont || !mp) return
  const W = cont.clientWidth, H = cont.clientHeight
  if (!W || !H) return
  svg.setAttribute('viewBox', `0 0 ${W} ${H}`)
  mp.setAttribute('d', pathFor(W))
  pond.value = { x: 0.10 * W, y: 48, rx: 32, ry: 21 }

  Array.from(svg.querySelectorAll('.gen')).forEach(n => n.remove())
  const rc = rough.svg(svg)
  const add = (n: SVGGElement) => { n.classList.add('gen'); svg.appendChild(n) }

  const L = mp.getTotalLength()
  const N = 150
  spine = []
  for (let i = 0; i <= N; i++) {
    const d = (i / N) * L
    const p = mp.getPointAtLength(d)
    const q = mp.getPointAtLength(Math.min(L, d + 1.5))
    const r = mp.getPointAtLength(Math.max(0, d - 1.5))
    const tx = q.x - r.x, ty = q.y - r.y
    const m = Math.hypot(tx, ty) || 1
    spine.push({ x: p.x, y: p.y, nx: -ty / m, ny: tx / m })
  }

  const rand = rng(1337)
  const trees: { x: number; y: number; r: number }[] = []
  for (let tries = 0; tries < 700 && trees.length < 14; tries++) {
    const x = rand() * W, y = 10 + rand() * 190
    if (nearest(x, y).d < HALF_W + 32) continue
    if (Math.hypot(x - pond.value.x, y - pond.value.y) < 78) continue
    if (trees.some(t => Math.hypot(t.x - x, t.y - y) < 70)) continue
    trees.push({ x, y, r: 12 + rand() * 7 })
  }
  trees.forEach((t, i) => {
    const c = LEAF[i % LEAF.length]
    add(rc.circle(t.x, t.y, t.r * 2, {
      roughness: 2, bowing: 1.4, strokeWidth: 1.6, stroke: '#2F5E3C', fill: c, fillStyle: 'solid',
    }))
    add(rc.circle(t.x + t.r * 0.35, t.y - t.r * 0.3, t.r * 1.1, {
      roughness: 2.2, strokeWidth: 1.2, stroke: '#2F5E3C', fill: c, fillStyle: 'solid',
    }))
  })

  add(rc.ellipse(pond.value.x, pond.value.y, pond.value.rx * 2, pond.value.ry * 2, {
    roughness: 1.9, bowing: 1.3, strokeWidth: 2, stroke: '#2F6D8F', fill: '#BFE3F2', fillStyle: 'solid',
  }))
  add(rc.line(pond.value.x - 12, pond.value.y + 4, pond.value.x + 4, pond.value.y + 4,
    { roughness: 1.6, strokeWidth: 1.3, stroke: '#5FA3C4' }))

  const left = spine.map(s => [s.x + s.nx * HALF_W, s.y + s.ny * HALF_W] as [number, number])
  const right = spine.map(s => [s.x - s.nx * HALF_W, s.y - s.ny * HALF_W] as [number, number])
  add(rc.polygon([...left, ...right.reverse()], {
    roughness: 1.5, bowing: 0.8, strokeWidth: 2.2, stroke: INK, fill: ASPHALT, fillStyle: 'solid',
  }))
  for (let i = 0; i < N; i += 6) {
    const p = spine[i], q = spine[Math.min(N, i + 3)]
    add(rc.line(p.x, p.y, q.x, q.y, { roughness: 1.2, strokeWidth: 1.6, stroke: DIM }))
  }
}

function drawCar() {
  const el = carSvg.value
  if (!el) return
  while (el.firstChild) el.removeChild(el.firstChild)
  const rc = rough.svg(el)
  const o = { roughness: 1.5, bowing: 1.1, strokeWidth: 2, stroke: INK }
  ;[[11, 1], [11, 23], [33, 1], [33, 23]].forEach(([x, y]) => {
    el.appendChild(rc.rectangle(x, y, 9, 4, { ...o, strokeWidth: 1.4, fill: INK, fillStyle: 'solid' }))
  })
  el.appendChild(rc.rectangle(5, 4, 44, 20, {
    ...o,
    fill: player.value === 'llm' ? '#3B82F6' : '#10B981',
    fillStyle: 'solid',
  }))
  el.appendChild(rc.rectangle(33, 7, 11, 14, { ...o, strokeWidth: 1.5, fill: '#DBF9EE', fillStyle: 'solid' }))
}

function drawBoom() {
  const el = boomSvg.value
  if (!el) return
  while (el.firstChild) el.removeChild(el.firstChild)
  const rc = rough.svg(el)
  const star = (spikes: number, rOut: number, rIn: number, rot: number) => {
    const pts: [number, number][] = []
    for (let i = 0; i < spikes * 2; i++) {
      const r = i % 2 ? rIn : rOut
      const t = rot + (i * Math.PI) / spikes
      pts.push([70 + Math.cos(t) * r, 70 + Math.sin(t) * r])
    }
    return pts
  }
  el.appendChild(rc.polygon(star(11, 66, 34, 0.15), {
    roughness: 2.1, bowing: 1.4, strokeWidth: 2.4, stroke: '#B3400F',
    fill: '#F5A524', fillStyle: 'solid',
  }))
  el.appendChild(rc.polygon(star(9, 40, 19, 0.5), {
    roughness: 2.2, bowing: 1.3, strokeWidth: 2, stroke: '#B3400F',
    fill: '#F5512E', fillStyle: 'solid',
  }))
}

function drawWheel() {
  const el = wheelSvg.value
  if (!el) return
  while (el.firstChild) el.removeChild(el.firstChild)
  const rc = rough.svg(el)
  const o = { roughness: 1.7, bowing: 1.3, strokeWidth: 3.5, stroke: INK }
  el.appendChild(rc.circle(60, 60, 100, o))
  el.appendChild(rc.circle(60, 60, 26, { ...o, strokeWidth: 2.8, fill: '#E2E8F0', fillStyle: 'solid' }))
  ;[[10, 60], [110, 60], [60, 110]].forEach(([x, y]) => {
    el.appendChild(rc.line(60, 60, x, y, { ...o, strokeWidth: 2.8 }))
  })
}

const marks = ref<{ a: { x: number; y: number }; b: { x: number; y: number } } | null>(null)
const splatCount = computed(() => frogs.value.filter(f => f.dead).length)

let ro: ResizeObserver
let hop: ReturnType<typeof setInterval> | undefined
function relayout() {
  drawScene()
  place(progress.value)
  const s0 = sample(0), s1 = sample(1)
  if (s0 && s1) marks.value = { a: { x: s0.x - 6, y: s0.y + 44 }, b: { x: s1.x + 8, y: s1.y - 42 } }
  refillFrogs()
}
onMounted(() => {
  relayout(); drawCar(); drawWheel()
  ro = new ResizeObserver(relayout)
  if (scene.value) ro.observe(scene.value)
  hop = setInterval(hopFrogs, 520)
  raf = requestAnimationFrame(trackCar)
})
onUnmounted(() => {
  ro?.disconnect(); clearInterval(timer); clearInterval(hop); clearTimeout(boomTimer)
  cancelAnimationFrame(raf)
})
watch(boom, v => { if (v) nextTick(drawBoom) })
</script>

<template>
  <div ref="scene" class="scene">
    <svg ref="sceneSvg" class="scenery">
      <path ref="measure" fill="none" stroke="none" />
    </svg>

    <template v-if="marks">
      <span class="marker marker-a" :style="{ left: marks.a.x + 'px', top: marks.a.y + 'px' }">A (출발)</span>
      <span class="marker marker-b" :style="{ left: marks.b.x + 'px', top: marks.b.y + 'px' }">B (도착)</span>
    </template>

    <!-- Frogs -->
    <div
      v-for="f in frogs"
      :key="f.id"
      class="frog"
      :class="{ dead: f.dead }"
      :style="{ left: f.x + 'px', top: f.y + 'px', transform: `translate(-50%,-50%) rotate(${f.a}deg)` }"
    >
      <svg v-if="!f.dead" viewBox="0 0 18 16" width="27">
        <ellipse cx="9" cy="9" rx="6" ry="5" fill="#5FB45F" stroke="#2F5E3C" stroke-width="1.2" />
        <circle cx="6.4" cy="4.2" r="2.1" fill="#5FB45F" stroke="#2F5E3C" stroke-width="1.1" />
        <circle cx="11.6" cy="4.2" r="2.1" fill="#5FB45F" stroke="#2F5E3C" stroke-width="1.1" />
        <circle cx="6.4" cy="4.2" r="0.8" fill="#1D3B26" />
        <circle cx="11.6" cy="4.2" r="0.8" fill="#1D3B26" />
        <path d="M2.5 12.5 L0.8 15 M15.5 12.5 L17.2 15" stroke="#2F5E3C" stroke-width="1.2" fill="none" />
      </svg>
      <!-- squashed -->
      <svg v-else viewBox="0 0 22 16" width="33">
        <ellipse cx="11" cy="8" rx="10" ry="3.2" fill="#98A375" stroke="#5A6340" stroke-width="1.1" />
        <path d="M2 8 L0.2 6.2 M20 8 L21.8 6.2 M5 10.6 L3.6 12.8 M17 10.6 L18.4 12.8"
              stroke="#5A6340" stroke-width="1.1" fill="none" />
        <path d="M7 6.4 L9 9 M9 6.4 L7 9 M13 6.4 L15 9 M15 6.4 L13 9"
              stroke="#3A2F22" stroke-width="1.2" fill="none" />
      </svg>
    </div>

    <!-- Boom explosion -->
    <div v-if="boom" class="boom" :style="{ left: boom.x + 'px', top: boom.y + 'px' }">
      <svg ref="boomSvg" viewBox="0 0 140 140" width="140" />
      <span class="boom-word">💥 탈선 폭발!</span>
    </div>

    <div v-show="player && !boom" ref="carEl" class="car" :style="carStyle">
      <svg ref="carSvg" viewBox="0 0 54 28" width="54" />
    </div>

    <!-- Player Picker in Korean -->
    <div class="picker">
      <div class="picker-title">🕹️ 운전자(모드)를 선택하세요</div>
      <div class="cards">
        <button class="card" :class="{ on: player === 'human' }" @click="pick('human')">
          <User :size="20" /><span>👨‍💼 사람 직접 운전 (핸들 조작)</span>
        </button>
        <button class="card" :class="{ on: player === 'llm' }" @click="pick('llm')">
          <Bot :size="20" /><span>🤖 LLM 자율 주행 (환각 시뮬레이션)</span>
        </button>
      </div>
    </div>

    <!-- Wheel with direct drag, polar circle and mousewheel support -->
    <div
      ref="wheelEl"
      class="wheel"
      :class="{ live: mode !== 'manual' }"
      @pointerdown="wheelDown"
      @pointermove="wheelMove"
      @pointerup="wheelUp"
      @wheel.prevent="onWheelScroll"
      title="마우스로 드래그하거나 휠을 굴려 운전하세요"
    >
      <svg ref="wheelSvg" class="wheel-svg" viewBox="0 0 120 120" width="115" :style="wheelStyle" />
      <User v-if="player === 'human'" class="wheel-driver text-emerald-600" :size="26" />
      <Bot v-else-if="player === 'llm'" class="wheel-driver bot text-blue-600" :size="26" />
    </div>

    <!-- Captions in Clean Korean -->
    <div class="caption">
      <span v-if="mode === 'idle'" class="dim font-medium">
        💡 왼쪽 아래에서 운전자를 선택해 <b>A(출발)</b>에서 시뮬레이션을 시작하세요.
      </span>
      <span v-else-if="mode === 'manual'" class="dim font-medium text-emerald-800">
        ✋ 오른쪽 핸들을 <b>마우스로 드래그하거나 휠을 굴려</b> <b>A</b>에서 <b>B</b>까지 안전하게 운전하세요!
      </span>
      <span v-else-if="mode === 'arrived'" class="punch text-emerald-600">
        🎉 <b>목적지 B 완벽 도착!</b> 사람의 능동적 상황 인식 & 조향(Sense-Plan-Act) 성공!
      </span>
      <span v-else-if="mode === 'auto' || !boom" class="dim font-medium text-blue-700">
        🤖 <b>LLM 자율 주행 중:</b> 초기 커브는 그럴듯하게 주행하고 있습니다...
      </span>
      <span v-else class="punch apology text-red-600">
        💥 <b>"죄송합니다. 도로 밖으로 나가면 안 되는 거였군요."</b> (피드백 루프 없는 LLM의 환각/탈선)
      </span>
      <span v-if="splatCount" class="toll font-bold">🐸 개구리 충돌: {{ splatCount }}마리</span>
    </div>
  </div>
</template>

<style scoped>
.scene {
  position: relative; width: 100%; height: 380px;
  overflow: hidden; touch-action: none; user-select: none;
  background: white; border-radius: 1rem; border: 1px solid #E2E8F0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}
.scenery { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }

.marker {
  position: absolute; transform: translate(-50%, -50%);
  font-family: 'Pretendard', sans-serif; font-weight: 800; font-size: 0.95rem;
}
.marker-a { color: #059669; }
.marker-b { color: #2563EB; }

.frog { position: absolute; pointer-events: none; transition: left .42s ease-out, top .42s ease-out; }
.frog.dead { transition: none; }
.frog svg { display: block; height: auto; }

.boom {
  position: absolute; transform: translate(-50%, -50%);
  pointer-events: none; z-index: 10;
  display: grid; place-items: center;
  animation: pop .32s cubic-bezier(.2,1.5,.4,1) both;
}
.boom svg { display: block; height: auto; grid-area: 1 / 1; }
.boom-word {
  grid-area: 1 / 1;
  font-family: 'Pretendard', sans-serif; font-weight: 900; font-size: 1.1rem;
  color: #FFF6E5; text-shadow: 0 2px 4px rgba(179, 64, 15, 0.8);
  transform: rotate(-6deg);
}
@keyframes pop {
  from { opacity: 0; transform: translate(-50%, -50%) scale(.25); }
  to   { opacity: 1; transform: translate(-50%, -50%) scale(1); }
}

.car { position: absolute; will-change: left, top, transform; z-index: 5; }
.car svg { display: block; height: auto; }

.picker { position: absolute; left: 1.2rem; bottom: 55px; z-index: 10; }
.picker-title {
  font-family: 'Pretendard', sans-serif; font-size: 0.8rem; font-weight: 700; color: #64748B; margin-bottom: 0.35rem;
}
.cards { display: flex; gap: 0.6rem; }
.card {
  display: flex; align-items: center; gap: 0.45rem;
  padding: 0.45rem 0.9rem; border-radius: 10px; cursor: pointer;
  border: 1.5px solid #CBD5E1; background: white; color: #1E293B;
  font-family: 'Pretendard', sans-serif; font-weight: 700; font-size: 0.82rem;
  transition: all .15s ease; box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.card:hover { transform: translateY(-1px); border-color: #94A3B8; }
.card.on { border-color: #2563EB; background: #EFF6FF; color: #1D4ED8; box-shadow: 0 2px 4px rgba(37,99,235,0.15); }

.wheel {
  position: absolute; right: 28px; bottom: 20px;
  width: 115px; height: 115px; cursor: grab; touch-action: none; z-index: 10;
}
.wheel:active { cursor: grabbing; }
.wheel.live { cursor: default; }
.wheel-svg { display: block; will-change: transform; }
.wheel-driver { position: absolute; inset: 0; margin: auto; pointer-events: none; }
.wheel-driver.bot { color: #2563EB; }

.caption {
  position: absolute; left: 1.2rem; bottom: 12px; right: 160px;
  display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap;
  font-size: 0.85rem; font-family: 'Pretendard', sans-serif; z-index: 10;
}
.caption b { color: #2563EB; font-weight: 800; }
.dim { color: #475569; }
.punch { font-size: 0.92rem; font-weight: 700; }
.punch.apology { font-size: 0.88rem; font-weight: 600; color: #DC2626; }
.toll { font-size: 0.8rem; color: #B91C1C; background: #FEE2E2; padding: 2px 6px; border-radius: 4px; }
</style>
