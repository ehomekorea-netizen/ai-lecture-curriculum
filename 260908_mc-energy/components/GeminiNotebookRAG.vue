<script setup lang="ts">
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0,
})
</script>

<template>
  <div class="grid grid-cols-12 gap-8 items-center mt-2">
    <!-- Left: Image Box -->
    <div class="col-span-6 flex justify-center">
      <div class="rounded-2xl overflow-hidden border border-white/20 bg-zinc-950 p-2 shadow-2xl">
        <img
          src="/gemini-notebook-ui.png"
          alt="Gemini Notebook UI"
          class="rounded-xl w-full max-h-76 object-contain"
        />
      </div>
    </div>

    <!-- Right: LiquidGlass Cards -->
    <div class="col-span-6 flex flex-col justify-between h-80">
      <div class="space-y-4">
        <!-- Feature 1: Grounding -->
        <div>
          <LiquidGlass glow="cyan" :radius="14">
            <div class="p-4">
              <div class="flex items-center gap-2 text-cyan-300 font-bold text-xs mb-1.5">
                <span class="i-carbon:catalog"></span>
                <span>Grounding on Your Sources (내 문서 근거 답변)</span>
              </div>
              <p class="text-xs text-white/80 m-0 leading-relaxed">
                인터넷 상의 불확실한 지식이 아니라, <strong class="text-cyan-200">내가 직접 업로드한 PDF, 엑셀, 규정집 안에서만 답변</strong>을 찾아 각주를 달아줍니다.
              </p>
            </div>
          </LiquidGlass>
        </div>

        <!-- Feature 2: RAG Practice (Step 1) -->
        <div
          class="transition-all duration-500"
          :class="[
            (props.stage ?? 0) >= 1
              ? 'opacity-100 translate-y-0'
              : 'opacity-20 translate-y-2'
          ]"
        >
          <LiquidGlass glow="emerald" :radius="14">
            <div class="p-4">
              <div class="flex items-center gap-2 text-emerald-300 font-bold text-xs mb-1.5">
                <span class="i-carbon:locked"></span>
                <span>1차시 RAG 이론의 가장 완벽한 무료 실전 도구</span>
              </div>
              <p class="text-xs text-white/90 m-0 leading-relaxed">
                복잡한 코딩이나 벡터 DB 구축 없이, <strong class="text-emerald-200">파일 드래그 앤 드롭 한 번으로 사내 전용 RAG 시스템</strong>이 즉시 완성됩니다.
              </p>
            </div>
          </LiquidGlass>
        </div>
      </div>
    </div>
  </div>
</template>
