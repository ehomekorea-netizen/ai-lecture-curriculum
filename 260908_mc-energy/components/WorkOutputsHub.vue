<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const showOutputs = computed(() => (props.stage ?? 0) >= 1)
const showBottom = computed(() => (props.stage ?? 0) >= 2)
</script>

<template>
  <div class="w-full flex flex-col justify-between py-2 select-none">
    
    <div class="grid grid-cols-12 gap-6 items-stretch">
      
      <!-- Left: Request Card -->
      <div class="col-span-4 p-6 rounded-2xl border border-white/10 bg-white/5 backdrop-blur-md shadow-lg flex flex-col justify-between h-76">
        <div>
          <div class="text-xs font-mono text-white/50 uppercase font-bold mb-3">단일 업무 요청</div>
          <div class="p-4 rounded-xl bg-black/40 font-mono text-xs text-white/90 border border-white/10 leading-relaxed mb-2">
            "실적 데이터를 분석하고,<br/>
            표와 차트를 포함한<br/>
            임원 보고서를 작성하라."
          </div>
        </div>
        <div class="pt-3 border-t border-white/10 text-xs font-mono text-white/50 flex items-center justify-between">
          <span>작업 위임</span>
          <span class="i-carbon:arrow-right text-base text-blue-400"></span>
        </div>
      </div>

      <!-- Right: 5 Output Artifacts -->
      <div
        class="col-span-8 grid grid-cols-2 gap-3 transition-all duration-500"
        :class="[showOutputs ? 'opacity-100 translate-x-0' : 'opacity-20 translate-x-2']"
      >
        <div class="p-3.5 rounded-xl bg-black/30 border border-white/10 flex items-center gap-3">
          <span class="text-xl">📊</span>
          <div>
            <div class="text-xs font-bold text-white">Spreadsheet</div>
            <div class="text-[11px] text-white/50">표, 수식, 데이터 시트 (.xlsx)</div>
          </div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/30 border border-white/10 flex items-center gap-3">
          <span class="text-xl">📄</span>
          <div>
            <div class="text-xs font-bold text-white">Document</div>
            <div class="text-[11px] text-white/50">정식 기획서, 실무 보고서 (.docx)</div>
          </div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/30 border border-white/10 flex items-center gap-3">
          <span class="text-xl">📑</span>
          <div>
            <div class="text-xs font-bold text-white">Presentation</div>
            <div class="text-[11px] text-white/50">발표 슬라이드 구조 (.pptx)</div>
          </div>
        </div>

        <div class="p-3.5 rounded-xl bg-black/30 border border-white/10 flex items-center gap-3">
          <span class="text-xl">📈</span>
          <div>
            <div class="text-xs font-bold text-white">Analysis & Chart</div>
            <div class="text-[11px] text-white/50">통계 분석 & 시각화 그래프</div>
          </div>
        </div>

        <div class="col-span-2 p-3.5 rounded-xl bg-black/30 border border-white/10 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <span class="text-xl">🖼</span>
            <div>
              <div class="text-xs font-bold text-white">Image Assets</div>
              <div class="text-[11px] text-white/50">사내 공지, 홍보 카드뉴스, 시각 포스터</div>
            </div>
          </div>
          <span class="text-[10px] font-mono text-white/40">DALL-E 3</span>
        </div>
      </div>

    </div>

    <!-- Bottom Callout -->
    <div
      class="mt-4 p-3.5 rounded-xl border border-white/10 bg-white/5 flex items-center justify-between text-xs text-white/90 transition-all duration-500"
      :class="[showBottom ? 'opacity-100' : 'opacity-20']"
    >
      <div class="flex items-center gap-2">
        <span class="i-carbon:checkmark-filled text-base text-blue-400"></span>
        <span>단순한 대화창 텍스트가 아니라, <strong>실무에서 즉시 활용 가능한 '완성형 파일'</strong>을 만들어냅니다.</span>
      </div>
      <span class="text-[11px] font-mono text-white/40">Output Centric</span>
    </div>

  </div>
</template>
