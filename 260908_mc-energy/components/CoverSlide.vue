<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue'

const canvasRef = ref<HTMLCanvasElement | null>(null)
let animationId: number | null = null
let gl: WebGLRenderingContext | null = null
let program: WebGLProgram | null = null
let uTimeLoc: WebGLUniformLocation | null = null
let uResLoc: WebGLUniformLocation | null = null
let startTime = Date.now()

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

    // Smooth dynamic fluid motion
    float t = u_time * 0.32;
    
    // Dynamic multi-layer turbulent organic fluid flow
    vec2 q = vec2(fbm(p + vec2(t * 0.42, t * 0.26)), fbm(p + vec2(t * 0.30, -t * 0.20)));
    vec2 r = vec2(fbm(p + 3.2 * q + vec2(1.7, 9.2) + 0.22 * t), fbm(p + 3.2 * q + vec2(8.3, 2.8) + 0.16 * t));
    float f = fbm(p + 4.2 * r);

    // ── Silky Smooth MC Energy Gradient (Deep Navy -> Cobalt Blue -> Electric Cyan Glow) ──
    float lightGrad = smoothstep(0.02, 0.95, uv.x);

    vec3 calmNavy = vec3(0.01, 0.03, 0.12);
    vec3 midBlue = vec3(0.00, 0.20, 0.65);
    vec3 brightCyan = vec3(0.08, 0.55, 0.88);
    vec3 peakGlow = vec3(0.35, 0.85, 0.98);

    vec3 col = mix(calmNavy, midBlue, clamp((f * f) * 3.4, 0.0, 1.0));
    col = mix(col, brightCyan, clamp(length(q) * (0.35 + 0.65 * lightGrad), 0.0, 1.0));
    col = mix(col, peakGlow, clamp(length(r.x) * lightGrad * 0.55, 0.0, 1.0));

    // Eye-friendly natural lighting transition
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

  const posBuffer = gl.createBuffer()
  gl.bindBuffer(gl.ARRAY_BUFFER, posBuffer)
  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array([
      -1.0, -1.0,
       1.0, -1.0,
      -1.0,  1.0,
      -1.0,  1.0,
       1.0, -1.0,
       1.0,  1.0,
    ]),
    gl.STATIC_DRAW,
  )

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
})

onBeforeUnmount(() => {
  if (animationId) cancelAnimationFrame(animationId)
  window.removeEventListener('resize', resize)
})
</script>

<template>
  <div class="absolute inset-0 w-full h-full flex flex-col justify-between select-none overflow-hidden bg-black p-12 px-14 text-left font-['Pretendard',sans-serif]">
    <!-- ── Continuous Moving WebGL Fluid Canvas with Silky Smooth Natural Gradient ── -->
    <canvas
      ref="canvasRef"
      class="absolute inset-0 w-full h-full block pointer-events-none"
    />

    <!-- ── Top Tag ── -->
    <div class="relative z-10">
      <span class="inline-block text-xs md:text-sm font-bold tracking-widest text-white uppercase pure-white-text">
        2026년 MC에너지 AI 실무역량 강화과정
      </span>
    </div>

    <!-- ── Center: Apple Keynote Statement Layout (100% Pure White Floating Title) ── -->
    <div class="relative z-10 my-auto max-w-4xl space-y-4 pt-2">
      <h1 class="text-3xl md:text-[46px] font-extrabold leading-[1.2] tracking-tight pure-white-title whitespace-nowrap">
        생성형 AI를 통한 실무능력 향상
      </h1>

      <p class="text-sm md:text-base font-normal leading-relaxed max-w-2xl pure-white-sub break-keep">
        AI의 본질과 팩트 검증부터 업무 위임(Work), 그리고 실무 시각화(Images 2.0 & Canva) 완성까지
      </p>
    </div>

    <!-- ── Bottom Bar: Logos & Presenter Text ── -->
    <div class="relative z-10 flex items-center justify-between border-t border-white/20 pt-4">
      <div class="flex items-center gap-2.5">
        <img
          src="/mc-energy-logo.jpg"
          alt="MC Energy"
          class="h-6.5 rounded px-2.5 py-1 bg-white object-contain shadow-sm"
        />
        <img
          src="/smhrd-logo.png"
          alt="스마트인재개발원"
          class="h-6.5 rounded px-2.5 py-1 bg-white object-contain shadow-sm"
        />
      </div>
      <span class="text-sm md:text-base font-bold text-white tracking-wide flex items-center gap-2 pure-white-text">
        <span class="text-white/60 font-normal text-xs uppercase tracking-widest">Presenter</span>
        오진실 강사
      </span>
    </div>
  </div>
</template>

<style scoped>
/* ── Absolute 100% Pure White Text & High-End Drop Shadows ── */
.pure-white-title {
  color: #FFFFFF !important;
  text-shadow: 0 4px 30px rgba(0, 0, 0, 0.9), 0 2px 6px rgba(0, 0, 0, 0.85);
  font-family: 'Pretendard', sans-serif !important;
}

.pure-white-sub {
  color: #FFFFFF !important;
  text-shadow: 0 2px 18px rgba(0, 0, 0, 0.85), 0 1px 4px rgba(0, 0, 0, 0.8);
  font-family: 'Pretendard', sans-serif !important;
}

.pure-white-text {
  color: #FFFFFF !important;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.85);
  font-family: 'Pretendard', sans-serif !important;
}
</style>
