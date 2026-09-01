<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const currentStage = computed(() => props.stage ?? 0)

const pipelineSteps = [
  { step: 'Step 1', name: 'Excel 데이터 업로드', tag: '자료 주입', icon: 'i-carbon:upload' },
  { step: 'Step 2', name: '데이터 구조 & 결측치 점검', tag: '무결성 점검', icon: 'i-carbon:search' },
  { step: 'Step 3', name: '증감률 & 원인 분석', tag: '통계 분석', icon: 'i-carbon:analytics' },
  { step: 'Step 4', name: '@visualize 차트 시각화', tag: '시각화', icon: 'i-carbon:chart-line' },
  { step: 'Step 5', name: '@document 1페이지 보고서', tag: '문서화', icon: 'i-carbon:document' },
  { step: 'Step 6', name: '사내 공유용 이미지 생성', tag: '비주얼', icon: 'i-carbon:image' },
  { step: 'Step 7', name: '나만의 Skill로 영구 자산화', tag: '자산화', icon: 'i-carbon:skill-level' },
]

const deliverables = [
  { num: '1', name: '원본 데이터', tag: 'XLSX', desc: '분석에 사용한 엑셀 원천 데이터' },
  { num: '2', name: '지시문 전문', tag: 'RCTF', desc: 'RCTF 구조 단계별 프롬프트' },
  { num: '3', name: '분석 결과표', tag: '표/수식', desc: '증감률 및 핵심 원인 분석표' },
  { num: '4', name: '시각화 차트', tag: '차트', desc: '추세가 한눈에 보이는 그래프' },
  { num: '5', name: '실무 보고서', tag: 'DOCX', desc: '상사 보고용 1페이지 완성본' },
  { num: '6', name: '스킬 지침', tag: 'Skill', desc: '다음 달에도 반복 실행할 지침' },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <div class="grid grid-cols-12 gap-5 items-stretch">
      <!-- Left: 7-Step Pipeline -->
      <div
        class="col-span-6 transition-all duration-500 transform"
        :class="[currentStage >= 0 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="blue" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-82">
            <div>
              <div class="flex items-center gap-2 text-xs font-bold text-blue-300 border-b border-blue-500/20 pb-2 mb-2">
                <span class="i-carbon:pipeline text-base"></span>
                <span>7단계 실행 파이프라인 (35분 실습)</span>
              </div>

              <div class="space-y-1 text-xs">
                <div
                  v-for="s in pipelineSteps"
                  :key="s.step"
                  class="p-1.5 px-2.5 rounded-lg bg-black/40 border border-white/5 flex items-center justify-between"
                >
                  <div class="flex items-center gap-2 text-[11px] text-white/90">
                    <span class="font-mono text-white/40 text-[10px]">{{ s.step }}</span>
                    <span>{{ s.name }}</span>
                  </div>
                  <span class="text-[9px] font-mono text-cyan-300 font-bold">{{ s.tag }}</span>
                </div>
              </div>
            </div>

            <div class="text-[10px] font-mono text-blue-300/80 pt-1.5 border-t border-white/10">
              실무 완결 파이프라인 가동
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: 6 Submission Deliverables -->
      <div
        class="col-span-6 transition-all duration-500 transform"
        :class="[currentStage >= 1 ? 'opacity-100 translate-y-0' : 'opacity-30 translate-y-2']"
      >
        <LiquidGlass glow="emerald" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-82">
            <div>
              <div class="flex items-center gap-2 text-xs font-bold text-emerald-300 border-b border-emerald-500/20 pb-2 mb-2">
                <span class="i-carbon:badge text-base"></span>
                <span>제출 산출물 6종 패키지</span>
              </div>

              <div class="grid grid-cols-2 gap-2 text-[10px]">
                <div
                  v-for="d in deliverables"
                  :key="d.name"
                  class="p-2 rounded-lg bg-black/40 border border-white/5 flex flex-col justify-between h-18"
                >
                  <div>
                    <div class="flex items-center justify-between text-white font-bold text-[11px] mb-0.5">
                      <span>{{ d.num }}. {{ d.name }}</span>
                      <span class="text-[9px] font-mono text-emerald-300 font-bold">{{ d.tag }}</span>
                    </div>
                    <p class="text-[9px] text-white/60 m-0 leading-tight">{{ d.desc }}</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="p-2 rounded-lg bg-black/40 border border-emerald-500/30 text-[10px] text-emerald-200 font-bold flex items-center justify-between">
              <div class="flex items-center gap-1.5">
                <span class="i-carbon:award text-emerald-400 text-sm"></span>
                <span>6종 산출물 완비 시 실무 역량 인증</span>
              </div>
              <span class="font-mono text-emerald-400 font-bold">인증 완료</span>
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
