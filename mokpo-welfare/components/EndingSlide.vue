<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import qrcode from 'qrcode-generator'

const canvasRef = ref<HTMLCanvasElement | null>(null)
let animationId: number | null = null
let gl: WebGLRenderingContext | null = null
let program: WebGLProgram | null = null
let uTimeLoc: WebGLUniformLocation | null = null
let uResLoc: WebGLUniformLocation | null = null
let startTime = Date.now()

// ── 5-Second Delayed Slide-In QR Code Logic ──
const showQr = ref(false)
let qrTimer: ReturnType<typeof setTimeout> | null = null

const QR_URL = 'https://cafe.daangn.com/mogpo-ai-silheo?utm_medium=copy_link'
const QUIET = 2

// High error correction (Level Q 25%) for instant optical camera recognition
const qrObj = computed(() => {
  const c = qrcode(0, 'Q')
  c.addData(QR_URL)
  c.make()
  return c
})

const count = computed(() => qrObj.value.getModuleCount())
const span = computed(() => count.value + QUIET * 2)

// Helper: Check if a coordinate belongs to one of the 3 Corner Finder Patterns (7x7)
function isFinderPattern(r: number, c: number, n: number): boolean {
  if (r < 7 && c < 7) return true
  if (r < 7 && c >= n - 7) return true
  if (r >= n - 7 && c < 7) return true
  return false
}

// Data modules with micro-rounded corners for high optical continuous density
const dataModules = computed(() => {
  const c = qrObj.value
  const n = count.value
  const modules: { x: number; y: number }[] = []

  for (let r = 0; r < n; r++) {
    for (let col = 0; col < n; col++) {
      if (isFinderPattern(r, col, n)) continue

      if (c.isDark(r, col)) {
        modules.push({
          x: col + QUIET,
          y: r + QUIET
        })
      }
    }
  }
  return modules
})

// Exact ISO 1:1:3:1:1 Finder Pattern Positions (Top-Left, Top-Right, Bottom-Left)
const finderOrigins = computed(() => {
  const n = count.value
  return [
    { x: QUIET, y: QUIET },                 // Top-Left
    { x: QUIET + n - 7, y: QUIET },         // Top-Right
    { x: QUIET, y: QUIET + n - 7 }          // Bottom-Left
  ]
})

const vsSource = `
  attribute vec2 position;
  void main() {
    gl_Position = vec4(position, 0.0, 1.0);
  }
`

const fsSource = `
  precision highp float;
  uniform vec2 u_resolution;
  uniform float u_time;

  float hash(vec2 p) {
    return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123);
  }

  float noise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    f = f * f * (3.0 - 2.0 * f);
    return mix(mix(hash(i + vec2(0.0, 0.0)), hash(i + vec2(1.0, 0.0)), f.x),
               mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), f.x), f.y);
  }

  float fbm(vec2 p) {
    float v = 0.0;
    float a = 0.5;
    mat2 rot = mat2(cos(0.55), sin(0.55), -sin(0.55), cos(0.55));
    for (int i = 0; i < 5; ++i) {
      v += a * noise(p);
      p = rot * p * 2.1 + vec2(80.0);
      a *= 0.5;
    }
    return v;
  }

  void main() {
    vec2 uv = gl_FragCoord.xy / u_resolution.xy;
    vec2 p = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / u_resolution.y;

    float t = u_time * 0.32;
    
    vec2 q = vec2(fbm(p + vec2(t * 0.42, t * 0.26)), fbm(p + vec2(t * 0.30, -t * 0.20)));
    vec2 r = vec2(fbm(p + 3.2 * q + vec2(1.7, 9.2) + 0.22 * t), fbm(p + 3.2 * q + vec2(8.3, 2.8) + 0.16 * t));
    float f = fbm(p + 4.2 * r);

    // Silky natural gradient
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.02, 0.04, 0.11);
    vec3 midCobalt = vec3(0.07, 0.22, 0.62);
    vec3 brightCyan = vec3(0.18, 0.58, 0.98);
    vec3 peakGlow = vec3(0.48, 0.85, 1.0);

    vec3 col = mix(calmNavy, midCobalt, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    col = mix(col * 0.72, col * 1.08, lightGrad);

    gl_FragColor = vec4(col, 1.0);
  }
`

function createShader(glCtx: WebGLRenderingContext, type: number, source: string) {
  const shader = glCtx.createShader(type)
  if (!shader) return null
  glCtx.shaderSource(shader, source)
  glCtx.compileShader(shader)
  if (!glCtx.getShaderParameter(shader, glCtx.COMPILE_STATUS)) {
    console.error('Shader compile error:', glCtx.getShaderInfoLog(shader))
    glCtx.deleteShader(shader)
    return null
  }
  return shader
}

function initWebGL() {
  const canvas = canvasRef.value
  if (!canvas) return

  gl = canvas.getContext('webgl', { antialias: true, alpha: false })
  if (!gl) return

  const vertexShader = createShader(gl, gl.VERTEX_SHADER, vsSource)
  const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fsSource)
  if (!vertexShader || !fragmentShader) return

  program = gl.createProgram()
  if (!program) return
  gl.attachShader(program, vertexShader)
  gl.attachShader(program, fragmentShader)
  gl.linkProgram(program)

  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error('Program link error:', gl.getProgramInfoLog(program))
    return
  }

  gl.useProgram(program)

  // Full-quad geometry
  const positionBuffer = gl.createBuffer()
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer)
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
    -1, -1,
     1, -1,
    -1,  1,
    -1,  1,
     1, -1,
     1,  1,
  ]), gl.STATIC_DRAW)

  const posAttrLoc = gl.getAttribLocation(program, 'position')
  gl.enableVertexAttribArray(posAttrLoc)
  gl.vertexAttribPointer(posAttrLoc, 2, gl.FLOAT, false, 0, 0)

  uTimeLoc = gl.getUniformLocation(program, 'u_time')
  uResLoc = gl.getUniformLocation(program, 'u_resolution')

  resize()
  render()
}

function resize() {
  if (!canvasRef.value || !gl) return
  const width = canvasRef.value.clientWidth || 980
  const height = canvasRef.value.clientHeight || 552
  const dpr = Math.min(window.devicePixelRatio || 1, 2)
  canvasRef.value.width = width * dpr
  canvasRef.value.height = height * dpr
  gl.viewport(0, 0, canvasRef.value.width, canvasRef.value.height)
}

function render() {
  if (!gl || !program) return
  const elapsed = (Date.now() - startTime) / 1000.0

  if (uTimeLoc) gl.uniform1f(uTimeLoc, elapsed)
  if (uResLoc && canvasRef.value) {
    gl.uniform2f(uResLoc, canvasRef.value.width, canvasRef.value.height)
  }

  gl.drawArrays(gl.TRIANGLES, 0, 6)
  animationId = requestAnimationFrame(render)
}

onMounted(() => {
  initWebGL()
  window.addEventListener('resize', resize)
  // Trigger smooth QR slide-in exactly after 5 seconds
  qrTimer = setTimeout(() => {
    showQr.value = true
  }, 5000)
})

onBeforeUnmount(() => {
  if (animationId) cancelAnimationFrame(animationId)
  if (qrTimer) clearTimeout(qrTimer)
  window.removeEventListener('resize', resize)
})
</script>

<template>
  <div class="absolute inset-0 w-full h-full flex flex-col justify-center items-center select-none overflow-hidden bg-slate-950 p-10 px-12 text-center font-['Nanum_Gothic',sans-serif]">
    <!-- ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── -->
    <canvas
      ref="canvasRef"
      class="absolute inset-0 w-full h-full block pointer-events-none"
    />

    <!-- ── Center: Elegant 1.5x Statement Layout ── -->
    <div class="relative z-10 my-auto w-full max-w-4xl space-y-6 px-4">
      <div class="pure-white-title break-keep">
        AI는 초안을 쓰고,<br>
        가치는 여러분이 담습니다.
      </div>

      <div class="pure-white-sub">
        경청해 주셔서 감사합니다.
      </div>
    </div>

    <!-- ── 5s Delayed Slide-in: 100% Completely Free-Floating Pure White QR (Zero Glass, Zero Border) ── -->
    <div
      class="absolute bottom-6 left-8 z-20 transition-all duration-800 ease-out"
      :class="showQr ? 'opacity-100 translate-y-0 scale-100 pointer-events-auto' : 'opacity-0 translate-y-8 scale-90 pointer-events-none'"
    >
      <!-- Pure Vector SVG Floating Directly Over Fluid Canvas with Subtle Cinema Shadow -->
      <svg
        :viewBox="`0 0 ${span} ${span}`"
        width="164"
        height="164"
        shape-rendering="geometricPrecision"
        class="block drop-shadow-[0_4px_24px_rgba(0,0,0,0.95)]"
      >
        <!-- 1. Three ISO 1:1:3:1:1 Finder Patterns (Instant Camera Lock Standard) -->
        <g v-for="(origin, idx) in finderOrigins" :key="idx">
          <!-- Outer 7x7 Square Ring (Radius 1.4) -->
          <rect
            :x="origin.x"
            :y="origin.y"
            width="7"
            height="7"
            rx="1.4"
            ry="1.4"
            fill="#FFFFFF"
          />
          <!-- Inner 5x5 Transparent Gap (Shows Fluid Canvas) -->
          <rect
            :x="origin.x + 1"
            :y="origin.y + 1"
            width="5"
            height="5"
            rx="0.7"
            ry="0.7"
            fill="#050811"
          />
          <!-- Center 3x3 Solid Core -->
          <rect
            :x="origin.x + 2"
            :y="origin.y + 2"
            width="3"
            height="3"
            rx="0.6"
            ry="0.6"
            fill="#FFFFFF"
          />
        </g>

        <!-- 2. Pure White Micro-Rounded Data Modules (Continuous Optical Density) -->
        <rect
          v-for="(mod, mIdx) in dataModules"
          :key="mIdx"
          :x="mod.x + 0.04"
          :y="mod.y + 0.04"
          width="0.92"
          height="0.92"
          rx="0.25"
          ry="0.25"
          fill="#FFFFFF"
        />
      </svg>
    </div>
  </div>
</template>

<style scoped>
/* ── Exactly 1.5x Scaled Pure White Statement (33.6px -> 52px) ── */
.pure-white-title {
  color: #FFFFFF !important;
  font-size: 52px !important;
  line-height: 1.28 !important;
  font-weight: 800 !important;
  letter-spacing: -0.015em !important;
  text-shadow: 0 4px 30px rgba(0, 0, 0, 0.92), 0 2px 6px rgba(0, 0, 0, 0.85) !important;
  font-family: 'Nanum Gothic', sans-serif !important;
  margin: 0 !important;
}

.pure-white-sub {
  color: rgba(255, 255, 255, 0.9) !important;
  font-size: 22px !important;
  font-weight: 400 !important;
  letter-spacing: 0.04em !important;
  text-shadow: 0 2px 18px rgba(0, 0, 0, 0.9), 0 1px 4px rgba(0, 0, 0, 0.8) !important;
  font-family: 'Nanum Gothic', sans-serif !important;
  padding-top: 6px !important;
}
</style>
