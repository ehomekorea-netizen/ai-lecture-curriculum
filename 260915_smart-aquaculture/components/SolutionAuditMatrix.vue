<script setup lang="ts">
import { ref } from 'vue'

const activeTab = ref<'trap' | 'checklist'>('trap')

const checklistItems = [
  { id: 1, cat: '데이터', q: '우리 어종·해역 데이터로 재학습(Fine-tuning)이 가능한가?', checked: true },
  { id: 2, cat: '데이터', q: '우리가 수집한 양식장 데이터의 소유권이 우리에게 있는가?', checked: true },
  { id: 3, cat: '성능', q: '단순 정확도가 아닌 [재현율·정밀도] 지표를 명확히 제시하는가?', checked: true },
  { id: 4, cat: '성능', q: '학습 데이터와 검증 데이터가 철저히 분리되어 검증되었는가?', checked: true },
  { id: 5, cat: '성능', q: '유사 해역·유사 어종에서의 실증(PoC) 사례가 존재하는가?', checked: false },
  { id: 6, cat: '운영', q: '해상 통신 장애나 인터넷 두절 시에도 로컬 최소 기능이 동작하는가?', checked: true },
  { id: 7, cat: '운영', q: '오경보 누적 시 경보 임계 기준을 관리자가 직접 조정할 수 있는가?', checked: true },
  { id: 8, cat: '운영', q: '예측 근거(수온, DO, 기상 등)를 사람이 이해할 수 있게 시각화하는가?', checked: true },
  { id: 9, cat: '비용', q: '구축비 외 연간 유지보수비 및 모델 재학습 비용이 명시되어 있는가?', checked: true },
  { id: 10, cat: '책임', q: 'AI 오작동·오예측으로 인한 사고 시 책임 한계가 계약서에 명시되어 있는가?', checked: false },
]
</script>

<template>
  <div class="glass-card p-3.5 my-2 text-xs flex flex-col gap-2">
    <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
      <div class="flex items-center gap-2 font-bold text-white text-sm">
        <span class="i-carbon-certificate-check text-emerald-400 text-base"></span>
        <span>AI 성능 평가의 진실 & 솔루션 도입 체크리스트</span>
      </div>
      <div class="flex items-center gap-2">
        <button
          class="px-2.5 py-1 rounded text-xs transition-all"
          :class="activeTab === 'trap' ? 'bg-rose-500/20 text-rose-300 border border-rose-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activeTab = 'trap'"
        >
          정확도 97%의 함정
        </button>
        <button
          class="px-2.5 py-1 rounded text-xs transition-all"
          :class="activeTab === 'checklist' ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold' : 'text-white/60 hover:text-white'"
          @click="activeTab = 'checklist'"
        >
          도입 검토 10대 체크리스트 (전체보기)
        </button>
      </div>
    </div>

    <!-- Tab 1: Accuracy Trap -->
    <div v-if="activeTab === 'trap'" class="space-y-2">
      <div class="p-2.5 bg-rose-950/30 border border-rose-500/20 rounded-lg">
        <div class="text-rose-400 font-bold text-xs mb-1">
          🚨 "공급업체: 저희 AI는 폐사 예측 정확도가 97%입니다!" 믿어도 될까요?
        </div>
        <p class="text-white/80 text-[11px] leading-relaxed">
          100일 중 실제 폐사 위험일이 단 3일뿐인 해역이라면, <strong>"1년 365일 무조건 안전함"</strong>이라고만 답하는 모델도 정확도는 <strong>97%</strong>가 나옵니다! (단 1번의 위험도 못 잡음)
        </p>
      </div>

      <div class="grid grid-cols-2 gap-2.5 text-xs">
        <div class="p-2.5 bg-emerald-950/20 border border-emerald-500/30 rounded-lg">
          <div class="text-emerald-300 font-bold text-xs mb-1">재현율 (Recall) ⭐ 수산양식 최우선!</div>
          <p class="text-white/70 text-[10px] mb-1.5">실제 위험 발생일 중 AI가 찾아낸 비율</p>
          <div class="p-1.5 bg-black/40 rounded text-emerald-200 text-[10px]">
            • 낮으면: <strong>위험을 놓침 → 대량 폐사 직격타!</strong><br>
            • 폐사·질병 예방에서는 무조건 재현율을 최우선 확인해야 함
          </div>
        </div>

        <div class="p-2.5 bg-sky-950/20 border border-sky-500/30 rounded-lg">
          <div class="text-sky-300 font-bold text-xs mb-1">정밀도 (Precision)</div>
          <p class="text-white/70 text-[10px] mb-1.5">AI가 울린 경보 중 진짜 위험이었던 비율</p>
          <div class="p-1.5 bg-black/40 rounded text-sky-200 text-[10px]">
            • 낮으면: <strong>헛경보 누적 → 양식장 인력 피로 및 불신</strong><br>
            • 비용이 많이 드는 조기 출하 결정 등에서 중시
          </div>
        </div>
      </div>
    </div>

    <!-- Tab 2: 10 Checklist (2-Column Grid, Zero-Scroll) -->
    <div v-else class="space-y-1.5">
      <div class="grid grid-cols-2 gap-1.5">
        <div
          v-for="item in checklistItems"
          :key="item.id"
          class="p-1.5 rounded bg-white/5 border border-white/10 flex items-center justify-between text-[10px]"
        >
          <div class="flex items-center gap-1.5 pr-1">
            <span class="px-1 py-0.2 rounded bg-white/10 text-white/50 text-[9px] font-bold flex-shrink-0">{{ item.cat }}</span>
            <span class="text-white/90 truncate">{{ item.id }}. {{ item.q }}</span>
          </div>
          <span class="px-1.5 py-0.5 rounded text-[9px] font-bold flex-shrink-0" :class="item.checked ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'">
            {{ item.checked ? '필수 확인' : '계약 특약' }}
          </span>
        </div>
      </div>
      <div class="p-1.5 bg-amber-500/10 rounded border border-amber-500/20 text-[10px] text-amber-300 text-center font-bold">
        💡 10개 문항 중 "예"가 7개 미만이면 도입을 전면 재검토해야 합니다.
      </div>
    </div>
  </div>
</template>
