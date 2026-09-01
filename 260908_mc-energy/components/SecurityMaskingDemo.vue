<script setup lang="ts">
import { computed } from 'vue'
import LiquidGlass from './LiquidGlass.vue'

const props = withDefaults(defineProps<{
  stage?: number
}>(), {
  stage: 0
})

const isMasked = computed(() => (props.stage ?? 0) >= 1)
const showChecklist = computed(() => (props.stage ?? 0) >= 2)

const securityRules = [
  {
    icon: 'i-carbon:locked',
    title: '사내 비공개 기밀',
    target: '미공개 사업계획, 독점 알고리즘, 파트너십 협약',
    solution: '가명칭(프로젝트 A) 및 일반화된 기술 용어로 치환',
    badge: '기밀 보호',
    color: 'blue',
  },
  {
    icon: 'i-carbon:user-avatar-filled-alt',
    title: '고객 개인정보 (PII)',
    target: '주민등록번호, 전화번호, 이메일, 계좌번호',
    solution: '필수 마스킹 [고객A], [010-XXXX-XXXX] 처리',
    badge: '법적 의무',
    color: 'pink',
  },
  {
    icon: 'i-carbon:money',
    title: '민감 재무 · 견적가',
    target: '원가 산출표, 고객사별 특별 할인 단가, 마진율',
    solution: '비율(%) 또는 배수 단위 가상 수치로 변환',
    badge: '영업 비밀',
    color: 'amber',
  },
]
</script>

<template>
  <div class="w-full flex flex-col justify-between py-1 select-none">
    <!-- Top: Live Masking Sandbox Comparison -->
    <div class="grid grid-cols-12 gap-5 items-stretch mb-3.5">
      <!-- Left: Raw Input (Before Masking) -->
      <div class="col-span-6">
        <LiquidGlass glow="pink" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-42">
            <div>
              <div class="flex items-center justify-between border-b border-rose-500/20 pb-1.5 mb-2">
                <div class="flex items-center gap-2 text-rose-400 font-bold text-xs">
                  <span class="i-carbon:warning-filled"></span>
                  <span>위험 원본 데이터 (Before)</span>
                </div>
                <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold">외부 유출 위험</span>
              </div>
              <div class="p-2.5 rounded-lg bg-black/40 font-mono text-[11px] text-rose-200/90 leading-relaxed border border-rose-500/20">
                "MC에너지 <span class="bg-rose-500/30 text-rose-300 px-1 rounded">홍길동 차장(010-1234-5678)</span>이 <span class="bg-rose-500/30 text-rose-300 px-1 rounded">(주)한국전력과 15.4억원</span> 규모 전력 직거래 계약을 체결함."
              </div>
            </div>
            <div class="text-[10px] font-mono text-rose-400/60 pt-1">
              개인정보 및 거래단가 노출 상태
            </div>
          </div>
        </LiquidGlass>
      </div>

      <!-- Right: Masked Input (After Masking) -->
      <div class="col-span-6">
        <LiquidGlass glow="emerald" :radius="14" class="h-full">
          <div class="p-4 flex flex-col justify-between h-42">
            <div>
              <div class="flex items-center justify-between border-b border-emerald-500/20 pb-1.5 mb-2">
                <div class="flex items-center gap-2 text-emerald-400 font-bold text-xs">
                  <span class="i-carbon:security"></span>
                  <span>안전 마스킹 데이터 (After)</span>
                </div>
                <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">보안 준수 완료</span>
              </div>
              <div class="p-2.5 rounded-lg bg-black/40 font-mono text-[11px] text-emerald-200/90 leading-relaxed border border-emerald-500/20">
                "MC에너지 <span class="bg-emerald-500/30 text-emerald-300 px-1 rounded font-bold">[담당자A]</span>가 <span class="bg-emerald-500/30 text-emerald-300 px-1 rounded font-bold">[고객사B]와 [OO억원]</span> 규모 전력 직거래 계약을 체결함."
              </div>
            </div>
            <div class="text-[10px] font-mono text-emerald-300/80 pt-1">
              가명화 처리로 안전한 AI 분석 가능
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>

    <!-- Bottom: 3 Core Security Rules -->
    <div class="grid grid-cols-3 gap-4">
      <div
        v-for="rule in securityRules"
        :key="rule.title"
        class="transition-all duration-500"
        :class="[showChecklist ? 'opacity-100 translate-y-0' : 'opacity-80 translate-y-0']"
      >
        <LiquidGlass :glow="rule.color === 'blue' ? 'blue' : rule.color === 'pink' ? 'pink' : 'amber'" :radius="14">
          <div class="p-3.5 flex flex-col justify-between h-34">
            <div>
              <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-white/10">
                <div class="flex items-center gap-1.5 text-xs font-bold text-white">
                  <span :class="[rule.icon, 'text-sm']"></span>
                  <span>{{ rule.title }}</span>
                </div>
                <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white/10 text-white/70">{{ rule.badge }}</span>
              </div>
              <p class="text-[11px] text-white/60 m-0 leading-relaxed">
                <strong class="text-white/80">대상:</strong> {{ rule.target }}
              </p>
            </div>
            <div class="pt-1.5 border-t border-white/10 text-[10px] font-mono text-cyan-300">
              💡 {{ rule.solution }}
            </div>
          </div>
        </LiquidGlass>
      </div>
    </div>
  </div>
</template>
