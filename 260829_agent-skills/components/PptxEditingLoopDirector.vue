<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  Presentation,
  FileText,
  RotateCw,
  Eye,
  Sliders,
  CheckCircle2,
  Mic,
  Copy,
  Check,
  ArrowRight,
  Sparkles
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const isCopied = ref(false)

function copyBrief() {
  const text = `[결과물] @Presentations, 지역사회 보고용 PPTX 작성
[소스] 지정한 결과보고서 DOCX와 원자료의 확정 수치
[대상] 기관 내부 회의와 지역사회 보고회
[제약] 10슬라이드 이내, 고딕 계열 글꼴, 기관 로고 사용 권한 확인
[시각화] 만족도·참여율·예산 집행을 시각적 지표로 구성
[검수] 각 슬라이드의 수치·출처·가독성 점검 및 발표자 노트(20초) 작성`
  navigator.clipboard.writeText(text)
  isCopied.value = true
  setTimeout(() => isCopied.value = false, 2000)
}

const loopSteps = [
  { num: '01', title: '초안 생성', desc: '목적·대상·시간·슬라이드 수를 먼저 확정' },
  { num: '02', title: '시각 검토', desc: '제목 줄바꿈, 표·차트 크기, 글꼴 가독성 점검' },
  { num: '03', title: '단일 수정', desc: '한 번에 하나의 명확한 개선 목표만 지시' },
  { num: '04', title: '재편집', desc: '수정된 슬라이드와 전체 스토리라인 동시 검토' },
  { num: '05', title: '최종 검수', desc: '20~30초 발표자 노트(Script) 및 출처 확인' }
]
</script>

<template>
  <div class="w-full flex items-stretch gap-4 h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Left Column (46%): Structured Brief Box -->
    <div class="w-[46%] flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3.5 shadow-sm">
      <div>
        <!-- Header -->
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-1.5">
            <Presentation :size="15" class="text-purple-600" />
            <span class="text-xs font-bold text-white font-serif">
              구조화된 발표 브리프 (Structured Brief)
            </span>
          </div>
          <button
            @click="copyBrief"
            class="flex items-center gap-1 px-2 py-0.5 rounded-md bg-white/8 hover:bg-slate-200 text-slate-300 text-[10px] font-mono font-bold transition-colors cursor-pointer"
          >
            <Check v-if="isCopied" :size="10" class="text-emerald-600" />
            <Copy v-else :size="10" />
            <span>{{ isCopied ? '복사됨' : '브리프 복사' }}</span>
          </button>
        </div>

        <!-- Brief Structure Tags -->
        <div class="space-y-1.5 text-[11px] font-mono">
          <div class="p-1.5 px-2 rounded-lg bg-purple-50/80 border border-purple-100 flex items-start gap-2">
            <span class="font-bold text-purple-700 shrink-0">[결과물]</span>
            <span class="text-slate-100">@Presentations, 지역사회 보고용 PPTX</span>
          </div>
          <div class="p-1.5 px-2 rounded-lg bg-blue-950/40 border border-blue-100 flex items-start gap-2">
            <span class="font-bold text-blue-400 shrink-0">[소 스]</span>
            <span class="text-slate-100">지정한 결과보고서 DOCX + 원자료 확정 수치</span>
          </div>
          <div class="p-1.5 px-2 rounded-lg bg-white/5 border border-white/10 flex items-start gap-2">
            <span class="font-bold text-slate-300 shrink-0">[대 상]</span>
            <span class="text-slate-100">기관 내부 회의 및 지역사회 후원자 보고회</span>
          </div>
          <div class="p-1.5 px-2 rounded-lg bg-amber-50/80 border border-amber-100 flex items-start gap-2">
            <span class="font-bold text-amber-700 shrink-0">[제 약]</span>
            <span class="text-slate-100">10슬라이드 이내, 고딕체, 원자료 없는 주장 금지</span>
          </div>
          <div class="p-1.5 px-2 rounded-lg bg-emerald-950/40 border border-emerald-100 flex items-start gap-2">
            <span class="font-bold text-emerald-400 shrink-0">[노 트]</span>
            <span class="text-slate-100">각 슬라이드 하단에 20~30초 발표 스크립트 작성</span>
          </div>
        </div>
      </div>

      <!-- Core Rule Hint -->
      <div class="bg-white/6 rounded-xl p-2 border border-white/10 text-[10.5px] text-slate-300 font-serif leading-tight">
        💡 <strong>핵심 원칙</strong>: "예쁘게 만들기"보다 <strong>"정확하게 이해시키기"</strong>를 우선합니다.
      </div>
    </div>

    <!-- Right Column (54%): 5-Step Editing Loop -->
    <div class="w-[54%] flex flex-col justify-between space-y-2">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono font-bold text-slate-400 flex items-center gap-1.5">
            <RotateCw :size="13" class="text-purple-600 animate-spin" style="animation-duration: 8s;" />
            <span>반복 개선을 위한 5단계 에디팅 루프</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-purple-100 text-purple-800">
            짧은 수정 주기
          </span>
        </div>

        <!-- 5 Loop Cards -->
        <div class="space-y-1.5">
          <div
            v-for="(step, idx) in loopSteps"
            :key="step.num"
            class="p-2 px-3 rounded-xl bg-white/6 border border-white/10 shadow-2xs flex items-center justify-between hover:border-purple-300 transition-all"
          >
            <div class="flex items-center gap-2.5">
              <span class="w-5 h-5 rounded-full bg-purple-100 text-purple-700 font-mono font-bold text-[10px] flex items-center justify-center shrink-0">
                {{ step.num }}
              </span>
              <div>
                <span class="text-xs font-bold text-white font-serif block leading-tight">
                  {{ step.title }}
                </span>
                <span class="text-[10px] text-slate-400 leading-tight">
                  {{ step.desc }}
                </span>
              </div>
            </div>
            <CheckCircle2 :size="13" class="text-slate-300 shrink-0" />
          </div>
        </div>
      </div>

      <!-- Single Action Prompt Example -->
      <div class="bg-purple-50/90 rounded-xl p-2 border border-purple-200/80 text-[10.5px] text-purple-950 font-mono flex items-start gap-1.5 leading-relaxed">
        <Sparkles :size="13" class="text-purple-600 shrink-0 mt-0.5" />
        <span><strong>수정 지시 예시</strong>: "4번 슬라이드의 만족도 점수를 한눈에 비교할 수 있는 막대 차트로 바꾸고, 표본 수(N=45)를 함께 표시해줘."</span>
      </div>
    </div>
  </div>
</template>
