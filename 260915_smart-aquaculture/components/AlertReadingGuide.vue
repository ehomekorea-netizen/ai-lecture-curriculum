<script setup lang="ts">
</script>

<template>
  <div class="my-2 grid grid-cols-2 gap-3 text-xs">
    <!-- Wrong Actions / Misunderstandings -->
    <div class="glass-card border-rose-500/30 bg-rose-950/15 p-3.5 flex flex-col justify-between">
      <div>
        <div class="flex items-center gap-1.5 text-rose-300 font-bold text-xs border-b border-rose-500/20 pb-1.5 mb-2">
          <span class="i-carbon-close-filled text-rose-400 text-sm"></span>
          <span>❌ 잘못된 해석 & 절대 금지 행동</span>
        </div>
        <ul class="space-y-2 text-white/80">
          <li class="p-2 bg-black/40 rounded border border-rose-500/15">
            <strong class="text-rose-300 text-[11px]">"위험도 82% 경보가 왔으니 100% 확실하다"</strong>
            <p class="text-white/60 text-[10px] mt-0.5">→ AI 예측은 확률적 신호일 뿐이며 오류 가능성이 상존함</p>
          </li>
          <li class="p-2 bg-black/40 rounded border border-rose-500/15">
            <strong class="text-rose-300 text-[11px]">"경보 오자마자 약품 투여/조기 출하 즉시 실행"</strong>
            <p class="text-white/60 text-[10px] mt-0.5">→ 되돌릴 수 없는 사육 조치는 실측 확인 없이 즉시 시행 금지!</p>
          </li>
          <li class="p-2 bg-black/40 rounded border border-rose-500/15">
            <strong class="text-rose-300 text-[11px]">"어제 오경보 떴으니 앞으로 경보 다 무시한다"</strong>
            <p class="text-white/60 text-[10px] mt-0.5">→ 오경보 기록을 남겨야 개발사에 모델 재보정/튜닝을 요구할 수 있음</p>
          </li>
        </ul>
      </div>
      <div class="mt-2 pt-1 border-t border-rose-500/20 text-[10px] text-rose-300/80">
        위험: 맹목적 과신 또는 성급한 조작으로 인한 2차 폐사 위험
      </div>
    </div>

    <!-- Correct Actions / Best Practices -->
    <div class="glass-card border-emerald-500/30 bg-emerald-950/15 p-3.5 flex flex-col justify-between">
      <div>
        <div class="flex items-center gap-1.5 text-emerald-300 font-bold text-xs border-b border-emerald-500/20 pb-1.5 mb-2">
          <span class="i-carbon-checkmark-filled text-emerald-400 text-sm"></span>
          <span>⭕ 올바른 해석 & 현장 실무 3원칙</span>
        </div>
        <ul class="space-y-2 text-white/90">
          <li class="p-2 bg-black/40 rounded border border-emerald-500/20">
            <strong class="text-emerald-300 text-[11px]">1. 예측값은 '구간(범위)'으로 해석</strong>
            <p class="text-white/70 text-[10px] mt-0.5">"3일 후 27.2℃"는 ±1.5℃ 구간의 상승 가능성을 의미</p>
          </li>
          <li class="p-2 bg-black/40 rounded border border-emerald-500/20">
            <strong class="text-emerald-300 text-[11px]">2. 조치의 최종 근거는 '현장 실측값'</strong>
            <p class="text-white/70 text-[10px] mt-0.5">AI 경보는 준비를 앞당기는 용도, 조치는 육안 점검 및 실측 후 결정</p>
          </li>
          <li class="p-2 bg-black/40 rounded border border-emerald-500/20">
            <strong class="text-emerald-300 text-[11px]">3. 이례적 사건(과거에 없던 냉수대/태풍) 주의</strong>
            <p class="text-white/70 text-[10px] mt-0.5">과거 학습 데이터에 없던 극한 상황은 예측력이 급락함을 인지</p>
          </li>
        </ul>
      </div>
      <div class="mt-2 pt-1 border-t border-emerald-500/20 text-[10px] text-emerald-300 font-medium">
        핵심: AI는 "조기 경보 알람", 최종 판단과 책임은 "현장 관리자"
      </div>
    </div>
  </div>
</template>
