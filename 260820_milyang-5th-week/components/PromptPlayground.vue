<script setup lang="ts">
import { ref } from 'vue'

const copied = ref(false)

const promptText = `[1단계: 나의 목표 직무 및 분위기(Vibe)]
"나는 [희망 직무: 사무행정 / 마케팅 / 매장관리 등] 취업을 준비 중인 [이름]이야.
나의 알바 경험과 역량을 신뢰감 있게 보여주는 깔끔한 1페이지 포트폴리오 웹사이트를 만들어줘.
메인 컬러는 차분한 네이비(#1A2B4C)와 활력 있는 포인트 오렌지(#FF6B35)를 사용해줘."

[2단계: 핵심 섹션 구성]
"반드시 포함해야 할 섹션은 아래 4개야:
1. Hero: '성실함과 책임감으로 기여하는 인재 [이름]' 타이핑 소개
2. About: 내 핵심 강점 3가지 (꼼꼼한 문서 정리, 친절한 고객 응대, 원활한 협업)
3. Experience: 2개의 알바/활동 경험 (카페 알바 매뉴얼 제작, 학과 축제 기획 성과)
4. Contact: 이메일 복사 버튼 및 내 노션/리틀리 링크 버튼"

[3단계: 기술적 제약사항]
"- 스마트폰 화면에서도 완벽하게 작동하는 모바일 반응형 웹으로 작성해줘.
- 별도 설치 없이 브라우저에서 바로 열리는 단일 HTML 파일로 완성해줘."`

function copyPrompt() {
  navigator.clipboard.writeText(promptText).then(() => {
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  })
}
</script>

<template>
  <div class="prompt-playground">
    <div class="pp-header">
      <div class="pp-title-box">
        <span class="pp-badge">VIBE CODING PROMPT</span>
        <span class="pp-sub">수강생 원클릭 복사용 마스터 프롬프트</span>
      </div>
      <button class="copy-btn" :class="{ copied }" @click="copyPrompt">
        <span v-if="copied">✅ 복사 완료!</span>
        <span v-else>📋 프롬프트 전체 복사</span>
      </button>
    </div>

    <div class="pp-content">
      <div class="prompt-section">
        <div class="section-tag vibe-tag">1. Vision & Vibe (목표 직무 & 무드)</div>
        <div class="code-line quote">"나는 [사무행정/마케팅/매장관리] 취업 준비생 [이름]이야. 알바 경험과 역량을 신뢰감 있게 보여주는 깔끔한 1페이지 웹을 만들어줘."</div>
      </div>

      <div class="prompt-section">
        <div class="section-tag inputs-tag">2. Inputs & Structure (4대 필수 섹션)</div>
        <div class="code-line list">
          <div>• <b>Hero</b>: 성실함과 강점을 어필하는 한 줄 타이핑 애니메이션</div>
          <div>• <b>About</b>: 꼼꼼함, 소통력 등 3대 핵심 역량 카드</div>
          <div>• <b>Experience</b>: 알바/동아리 경험 (역할 및 "매뉴얼 제작", "비용 절감" 성과)</div>
          <div>• <b>Contact</b>: 원클릭 이메일 복사 + 노션/리틀리 링크</div>
        </div>
      </div>

      <div class="prompt-section">
        <div class="section-tag bound-tag">3. Boundaries (제약사항)</div>
        <div class="code-line constraint">
          <div>• 모바일 화면에서도 깨지지 않는 반응형 웹(Responsive)</div>
          <div>• 별도 서버 설정 없이 즉시 열리는 <b>단일 HTML 파일</b>(Single File)</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.prompt-playground {
  width: 100%;
  max-width: 780px;
  margin: 1rem auto 0;
  background: #181824;
  border: 1.5px solid #2f3142;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.22);
}

.pp-header {
  background: #202130;
  padding: 0.75rem 1.2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #2e3040;
}

.pp-title-box {
  display: flex;
  align-items: center;
  gap: 10px;
}

.pp-badge {
  background: #476BFF;
  color: #fff;
  font-family: 'Geist Mono', monospace;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 6px;
  letter-spacing: 0.08em;
}

.pp-sub {
  font-size: 0.8rem;
  color: #a6adc8;
  font-weight: 600;
}

.copy-btn {
  background: #27C93F;
  color: #0b2b11;
  border: none;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 5px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.copy-btn:hover {
  background: #34e74f;
  transform: translateY(-1px);
}

.copy-btn.copied {
  background: #53DFA9;
  color: #05261b;
}

.pp-content {
  padding: 1.1rem 1.4rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.prompt-section {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.section-tag {
  font-family: 'Geist Mono', monospace;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  padding: 2px 6px;
  border-radius: 4px;
  display: inline-block;
  width: fit-content;
}

.vibe-tag { background: rgba(71, 107, 255, 0.2); color: #8CA4FF; }
.inputs-tag { background: rgba(255, 189, 46, 0.2); color: #FFD269; }
.bound-tag { background: rgba(83, 223, 169, 0.2); color: #72F3C0; }

.code-line {
  background: #0f1016;
  border: 1px solid #232533;
  border-radius: 8px;
  padding: 0.55rem 0.8rem;
  font-family: 'Geist Mono', monospace;
  font-size: 0.75rem;
  line-height: 1.5;
  color: #cdd6f4;
}

.code-line b {
  color: #53DFA9;
}
</style>
