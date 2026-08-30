<script setup lang="ts">
import { ref } from 'vue'

const activePreset = ref<'typhoon' | 'checklist'>('typhoon')
const copied = ref(false)

const presets = {
  typhoon: {
    title: '태풍 대비 시설점검 안내문 (어촌계 공지)',
    r: '당신은 어촌계 사무장입니다.',
    c: '가두리 30가구 회원 대상, 다음 주 태풍 북상 대비 시설 점검 긴급 SMS 발송 예정입니다.',
    t: '태풍 대비 필수 점검 안내문을 작성하시오.',
    f: '150자 이내, 공손한 어조, 핵심 3대 조치를 번호 목록으로 제시하시오.',
    output: `[어촌계 긴급 공지: 태풍 대비 안내]
어촌계원 여러분, 다음 주 태풍 북상에 대비해 아래 점검을 오늘 중 완료해 주십시오.
1. 가두리 닻줄 및 계류 로프 장력 보강
2. 그물망 훼손 부위 봉합 및 침하 방지
3. 비상 발전기 및 산소 공급기 가동 점검
피해 없는 안전한 어장을 위해 협조 바랍니다.`,
  },
  checklist: {
    title: '고수온 대비 주간 점검 체크리스트 초안',
    r: '당신은 해상가두리 양식장 사육 및 시설 총괄 책임자입니다.',
    c: '가두리 8개 동 운영 중, 이번 주 28℃ 고수온 특보 대비 점검 계획입니다.',
    t: '고수온 집중 대비 주간 점검 체크리스트 초안을 작성하시오.',
    f: '마크다운 표 [점검 항목 | 점검 시점 | 담당 직책 | 확인 방법]',
    output: `| 점검 항목 | 점검 시점 | 담당 직책 | 확인 방법 |
|---|---|---|---|
| 표층/중층 수온·DO 측정 | 매일 06:00, 14:00 | 사육관리자 | 고정 센서 및 휴대용 측정기 대조 |
| 차광막 5m 하강 준비 | 특보 발령 전일 | 시설담당자 | 권양기 작동 및 로프 결속 확인 |
| 급이량 50% 감량 / 절식 | 수온 27℃ 도달 시 | 어장관리사 | 섭이 행동 관찰 및 급이기 제어 |
| 비상 액화산소 라인 점검 | 매일 08:00 | 총괄책임자 | 배관 압력 게이지 및 밸브 확인 |`,
  },
}

const copyPrompt = () => {
  const p = presets[activePreset.value]
  const text = `[Role] ${p.r}\n[Context] ${p.c}\n[Task] ${p.t}\n[Format] ${p.f}`
  navigator.clipboard.writeText(text)
  copied.value = true
  setTimeout(() => copied.value = false, 2000)
}
</script>

<template>
  <div class="glass-card p-4 mb-4 flex flex-col gap-3">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2">
      <div class="flex items-center gap-2 font-bold text-white text-sm">
        <span class="i-carbon-script text-amber-400 text-base"></span>
        <span>수산양식 실무 RCTF 프롬프트 랩</span>
      </div>
      <div class="flex items-center gap-2">
        <button
          class="px-3 py-1 rounded text-xs transition-all"
          :class="activePreset === 'typhoon' ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activePreset = 'typhoon'"
        >
          태풍 공지문
        </button>
        <button
          class="px-3 py-1 rounded text-xs transition-all"
          :class="activePreset === 'checklist' ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activePreset = 'checklist'"
        >
          고수온 체크리스트
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 font-mono transition-all"
          @click="copyPrompt"
        >
          <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
          <span>{{ copied ? '복사됨!' : 'RCTF 복사' }}</span>
        </button>
      </div>
    </div>

    <!-- 4 RCTF Cards -->
    <div class="grid grid-cols-4 gap-2.5">
      <div class="p-2.5 bg-white/5 rounded-lg border border-white/10">
        <span class="text-amber-400 font-bold text-xs">R (Role)</span>
        <p class="text-white/90 mt-1 leading-snug text-xs line-clamp-3">{{ presets[activePreset].r }}</p>
      </div>
      <div class="p-2.5 bg-white/5 rounded-lg border border-white/10">
        <span class="text-sky-400 font-bold text-xs">C (Context)</span>
        <p class="text-white/90 mt-1 leading-snug text-xs line-clamp-3">{{ presets[activePreset].c }}</p>
      </div>
      <div class="p-2.5 bg-white/5 rounded-lg border border-white/10">
        <span class="text-emerald-400 font-bold text-xs">T (Task)</span>
        <p class="text-white/90 mt-1 leading-snug text-xs line-clamp-3">{{ presets[activePreset].t }}</p>
      </div>
      <div class="p-2.5 bg-white/5 rounded-lg border border-white/10">
        <span class="text-purple-400 font-bold text-xs">F (Format)</span>
        <p class="text-white/90 mt-1 leading-snug text-xs line-clamp-3">{{ presets[activePreset].f }}</p>
      </div>
    </div>

    <!-- Output Preview -->
    <div class="p-3 bg-black/60 rounded-lg border border-emerald-500/30">
      <div class="text-xs text-emerald-400 font-bold mb-1.5 flex items-center gap-1.5">
        <span class="i-carbon-checkmark-filled text-sm"></span>
        <span>AI 생성 결과물 (현장 즉시 투입)</span>
      </div>
      <pre class="font-sans whitespace-pre-wrap text-white/95 text-xs leading-relaxed">{{ presets[activePreset].output }}</pre>
    </div>
  </div>
</template>
