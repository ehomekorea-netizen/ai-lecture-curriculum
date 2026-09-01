<script setup lang="ts">
import { ref } from 'vue'

const activePlatform = ref<'youtube' | 'tiktok' | 'instagram'>('youtube')
</script>

<template>
  <div class="glass-card p-4 my-2 text-xs flex flex-col gap-3">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-2.5">
      <div class="flex items-center gap-2">
        <span class="i-carbon-security text-sky-400 text-base"></span>
        <span class="font-bold text-white text-sm">2026 플랫폼별 AI 콘텐츠 라벨링 및 컴플라이언스</span>
      </div>
      <div class="flex items-center gap-1.5">
        <button
          class="px-2.5 py-1 rounded text-[11px] transition-all"
          :class="activePlatform === 'youtube' ? 'bg-red-500/20 text-red-300 font-bold border border-red-500/40' : 'text-white/60 hover:text-white'"
          @click="activePlatform = 'youtube'"
        >
          YouTube (Shorts)
        </button>
        <button
          class="px-2.5 py-1 rounded text-[11px] transition-all"
          :class="activePlatform === 'tiktok' ? 'bg-cyan-500/20 text-cyan-300 font-bold border border-cyan-500/40' : 'text-white/60 hover:text-white'"
          @click="activePlatform = 'tiktok'"
        >
          TikTok
        </button>
        <button
          class="px-2.5 py-1 rounded text-[11px] transition-all"
          :class="activePlatform === 'instagram' ? 'bg-pink-500/20 text-pink-300 font-bold border border-pink-500/40' : 'text-white/60 hover:text-white'"
          @click="activePlatform = 'instagram'"
        >
          Instagram (Reels)
        </button>
      </div>
    </div>

    <!-- YouTube Tab -->
    <div v-if="activePlatform === 'youtube'" class="grid grid-cols-3 gap-2.5">
      <div class="p-3 bg-red-950/20 rounded-xl border border-red-500/30 flex flex-col justify-between">
        <div>
          <div class="text-red-400 font-bold text-xs mb-1">1. 합성/변형 콘텐츠 공개</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            현실적인 인물·시설이 실제 사건처럼 오인될 수 있는 경우 업로드 단계에서 "합성 또는 변형된 콘텐츠" 체크 필수.
          </p>
        </div>
        <div class="text-[10px] text-red-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          표시: 영상 설명란 및 플레이어 배지
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-amber-400 font-bold text-xs mb-1">2. 수익화 & 중복 생성 방지</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            템플릿형 대량 생성이나 단순 프롬프트 영상 나열은 '반복적인 콘텐츠'로 분류되어 수익화 제한 위험.
          </p>
        </div>
        <div class="text-[10px] text-amber-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          핵심: 사람의 내레이션 + 편집 부가가치
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-sky-400 font-bold text-xs mb-1">3. C2PA 메타데이터</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            Google Veo 등 공인 모델이 부여한 SynthID/C2PA 암호화 메타데이터를 제거하거나 훼손하지 않음.
          </p>
        </div>
        <div class="text-[10px] text-sky-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          신뢰도: 자동 인증 마크 연동
        </div>
      </div>
    </div>

    <!-- TikTok Tab -->
    <div v-else-if="activePlatform === 'tiktok'" class="grid grid-cols-3 gap-2.5">
      <div class="p-3 bg-cyan-950/20 rounded-xl border border-cyan-500/30 flex flex-col justify-between">
        <div>
          <div class="text-cyan-400 font-bold text-xs mb-1">1. AI 자동 감지 & 라벨</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            C2PA 기반 자동 감지로 "AI-generated" 라벨이 붙으며, 미표기 적발 시 영상 추천(FYP) 노출 차단.
          </p>
        </div>
        <div class="text-[10px] text-cyan-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          조치: 업로드 시 "AI 생성 콘텐츠" 토글 ON
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-amber-400 font-bold text-xs mb-1">2. 가짜 시설·인물 오해 금지</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            실제 특정 양식장이나 공공기관의 실증 자료인 것처럼 속이는 연출 금지 (교육·홍보용 연출 명시).
          </p>
        </div>
        <div class="text-[10px] text-amber-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          자막: "본 영상은 AI로 재현된 연출 장면입니다"
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-emerald-400 font-bold text-xs mb-1">3. 상표 및 상업 음원 준수</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            영상 내 비인가 브랜드 로고 삽입 금지, 상업용 라이선스가 검증된 음원/효과음만 배경에 매핑.
          </p>
        </div>
        <div class="text-[10px] text-emerald-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          안전: 상업용 무권리 음원 사용
        </div>
      </div>
    </div>

    <!-- Instagram Tab -->
    <div v-else class="grid grid-cols-3 gap-2.5">
      <div class="p-3 bg-pink-950/20 rounded-xl border border-pink-500/30 flex flex-col justify-between">
        <div>
          <div class="text-pink-400 font-bold text-xs mb-1">1. AI 정보 라벨 (Made with AI)</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            Meta 정책에 따라 사실적인 영상·이미지 게시물에 'Made with AI' 라벨 부착 정책 적용.
          </p>
        </div>
        <div class="text-[10px] text-pink-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          위치: 계정명 하단 공식 라벨
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-amber-400 font-bold text-xs mb-1">2. 과장 수치 표기 금지</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            "생존율 100%", "사료비 90% 절감" 등 검증되지 않은 절대 수치 삽입 시 허위 과장 광고 규제 대상.
          </p>
        </div>
        <div class="text-[10px] text-amber-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          기준: FAO 및 공인 학술 자료 범위 내 서술
        </div>
      </div>
      <div class="p-3 bg-white/5 rounded-xl border border-white/10 flex flex-col justify-between">
        <div>
          <div class="text-sky-400 font-bold text-xs mb-1">3. CTA 링크 및 공식 채널</div>
          <p class="text-white/80 text-[11px] leading-relaxed m-0">
            프로필 링크나 공식 접수처 안내 시 기관 담당자의 사전 검수를 마친 공인 URL만 안내.
          </p>
        </div>
        <div class="text-[10px] text-sky-300/80 font-mono mt-2 pt-2 border-t border-white/10">
          안전: 접수 기간 및 주최 기관 대조
        </div>
      </div>
    </div>

    <!-- Bottom Action Checklist -->
    <div class="p-2.5 bg-black/40 rounded-lg border border-white/10 flex items-center justify-between text-[11px]">
      <div class="flex items-center gap-2">
        <span class="i-carbon-checkmark-outline text-emerald-400"></span>
        <span class="text-white/90">
          <strong>수업 핵심 원칙:</strong> "AI 생성 사실을 투명하게 밝히고, 정확한 수산양식 원리와 사람의 역할을 전달할 때 신뢰도가 가장 높습니다."
        </span>
      </div>
      <span class="text-white/50 font-mono text-[10px]">Ethical AI Guardrail</span>
    </div>
  </div>
</template>
