<script setup lang="ts">
import { ref } from 'vue'

const scrollEl = ref<HTMLElement | null>(null)
const isDragging = ref(false)
const startY = ref(0)
const scrollTopStart = ref(0)
const hasInteracted = ref(false)

function onMouseDown(e: MouseEvent) {
  isDragging.value = true
  hasInteracted.value = true
  startY.value = e.pageY - (scrollEl.value?.offsetTop || 0)
  scrollTopStart.value = scrollEl.value?.scrollTop || 0
}

function onMouseMove(e: MouseEvent) {
  if (!isDragging.value || !scrollEl.value) return
  e.preventDefault()
  const y = e.pageY - (scrollEl.value.offsetTop || 0)
  const walk = (y - startY.value) * 0.95
  scrollEl.value.scrollTop = scrollTopStart.value - walk
}

function onMouseUp() {
  isDragging.value = false
}

function onWheel(e: WheelEvent) {
  if (!scrollEl.value) return
  hasInteracted.value = true
  e.preventDefault()
  scrollEl.value.scrollTop += e.deltaY * 0.45
}

function onTouchStart(e: TouchEvent) {
  hasInteracted.value = true
  startY.value = e.touches[0].pageY
  scrollTopStart.value = scrollEl.value?.scrollTop || 0
}

function onTouchMove(e: TouchEvent) {
  if (!scrollEl.value) return
  const y = e.touches[0].pageY
  const walk = (y - startY.value) * 0.95
  scrollEl.value.scrollTop = scrollTopStart.value - walk
}
</script>

<template>
  <div class="interactive-phone-wrap">
    <!-- iPhone Device Frame -->
    <div class="iphone-frame">
      <!-- Dynamic Island Notch -->
      <div class="iphone-notch">
        <div class="notch-lens"></div>
      </div>

      <!-- Gesture Interaction Tooltip -->
      <transition name="fade">
        <div v-if="!hasInteracted" class="swipe-hint">
          <span>👆 스크롤하여 전체 둘러보기</span>
        </div>
      </transition>

      <!-- Authentic Scrollable Littly Page -->
      <div 
        ref="scrollEl"
        class="iphone-screen-scroll"
        :class="{ grabbing: isDragging }"
        @mousedown="onMouseDown"
        @mousemove="onMouseMove"
        @mouseup="onMouseUp"
        @mouseleave="onMouseUp"
        @wheel="onWheel"
        @touchstart="onTouchStart"
        @touchmove="onTouchMove"
      >
        <div class="screen-content">
          <!-- 1. Profile Header (실제 리틀리 프로필 영역) -->
          <div class="littly-profile-header">
            <div class="profile-avatar-wrap">
              <svg class="profile-avatar-svg" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Warm soft background -->
                <circle cx="40" cy="40" r="40" fill="#E0F2FE" />
                <!-- Hair back -->
                <ellipse cx="40" cy="35" rx="18" ry="18" fill="#1E293B" />
                <!-- Face -->
                <circle cx="40" cy="38" r="14" fill="#FFE4E6" />
                <!-- Hair front fringe -->
                <path d="M25 33C25 24.5 31.5 18 40 18C48.5 18 55 24.5 55 33C50 30 45 31 40 31C34 31 29 29.5 25 33Z" fill="#1E293B" />
                <!-- Eyes & Friendly Smile -->
                <circle cx="35.5" cy="37" r="1.6" fill="#0F172A" />
                <circle cx="44.5" cy="37" r="1.6" fill="#0F172A" />
                <path d="M37.5 42C39 43.5 41 43.5 42.5 42" stroke="#0F172A" stroke-width="1.4" stroke-linecap="round" />
                <!-- Soft blush -->
                <circle cx="32.5" cy="40" r="1.8" fill="#F43F5E" opacity="0.35" />
                <circle cx="47.5" cy="40" r="1.8" fill="#F43F5E" opacity="0.35" />
                <!-- Body / Shirt -->
                <path d="M19 72C19 56.5 30 50 40 50C50 50 61 56.5 61 72H19Z" fill="#2563EB" />
                <!-- Collar -->
                <path d="M34 50L40 58L46 50H34Z" fill="#FFFFFF" />
                <path d="M39 58L40 68L41 58H39Z" fill="#1D4ED8" />
              </svg>
            </div>
            
            <div class="profile-name-row">
              <span class="profile-name">김밀양</span>
              <span class="verified-badge">✓</span>
            </div>
            
            <p class="profile-bio">
              기획·운영·데이터로 가치를 만드는 인재<br/>
              문제 정의부터 실행까지 나만의 경험을 증명합니다.
            </p>

            <!-- Social Links Pill Row (리틀리 소셜 아이콘 바) -->
            <div class="social-icon-row">
              <div class="social-btn" title="Notion">📑</div>
              <div class="social-btn" title="LinkedIn">💼</div>
              <div class="social-btn" title="Email">✉️</div>
              <div class="social-btn" title="Blog">🌐</div>
            </div>
          </div>

          <!-- 2. Featured Large Card Block (리틀리 대표 배너 링크) -->
          <div class="featured-link-card">
            <div class="card-icon-box">
              <span class="card-icon">📂</span>
            </div>
            <div class="card-text-box">
              <div class="card-tag">MAIN PORTFOLIO</div>
              <div class="card-title">[노션] 상세 포트폴리오 &amp; 프로젝트 3선</div>
              <div class="card-desc">기획 프로세스 · 업무 매뉴얼화 · 데이터 분석</div>
            </div>
            <span class="card-chevron">›</span>
          </div>

          <!-- 3. Section Divider Text Block (리틀리 텍스트 구분 블록) -->
          <div class="section-title-block">
            <span class="title-emoji">📷</span>
            <span class="title-text">핵심 경험 &amp; 프로젝트 갤러리</span>
          </div>

          <!-- 4. 2-Column Photo Card Grid Block (리틀리 2열 이미지 카드 블록) -->
          <div class="gallery-grid">
            <!-- Card 1 -->
            <div class="littly-grid-card">
              <div class="grid-card-media">
                <img 
                  src="https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=400&q=80" 
                  alt="기획 및 협업 프로세스" 
                  class="grid-img" 
                />
              </div>
              <div class="grid-card-body">
                <div class="grid-title">기획 &amp; 협업 프로세스</div>
                <div class="grid-sub">일정 20% 단축 매뉴얼 구축</div>
              </div>
            </div>

            <!-- Card 2 -->
            <div class="littly-grid-card">
              <div class="grid-card-media">
                <img 
                  src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=400&q=80" 
                  alt="업무 매뉴얼화 & 데이터 정리" 
                  class="grid-img" 
                />
              </div>
              <div class="grid-card-body">
                <div class="grid-title">업무 매뉴얼 &amp; 데이터 정리</div>
                <div class="grid-sub">반복 업무 표준화 가이드</div>
              </div>
            </div>

            <!-- Card 3 -->
            <div class="littly-grid-card">
              <div class="grid-card-media">
                <img 
                  src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=400&q=80" 
                  alt="현장 운영 & 커뮤니케이션" 
                  class="grid-img" 
                />
              </div>
              <div class="grid-card-body">
                <div class="grid-title">현장 운영 &amp; 고객 소통</div>
                <div class="grid-sub">고객 피드백 즉시 개선</div>
              </div>
            </div>

            <!-- Card 4 -->
            <div class="littly-grid-card">
              <div class="grid-card-media">
                <img 
                  src="https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?auto=format&fit=crop&w=400&q=80" 
                  alt="산출물 기획 & 디자인 제작" 
                  class="grid-img" 
                />
              </div>
              <div class="grid-card-body">
                <div class="grid-title">산출물 기획 &amp; 디자인</div>
                <div class="grid-sub">보고서 가독성 시각화</div>
              </div>
            </div>
          </div>

          <!-- 5. File Download Block (리틀리 첨부파일 다운로드 블록) -->
          <div class="file-download-block">
            <div class="file-icon-wrap">
              <span class="file-icon">📄</span>
            </div>
            <div class="file-text-wrap">
              <div class="file-title">2026 이력서 &amp; 경력기술서 (PDF)</div>
              <div class="file-sub">증빙 서류 사본 포함 · 2.4 MB</div>
            </div>
            <span class="file-download-btn">다운로드</span>
          </div>

          <!-- 6. High-Contrast Primary Contact CTA (리틀리 메인 문의 버튼) -->
          <div class="primary-cta-btn">
            <span>✉️ 직무 제안 및 커피챗 요청하기</span>
          </div>

          <!-- 7. Official Littly Footer Badge (리틀리 공식 푸터) -->
          <div class="littly-branding-footer">
            <div class="littly-badge">
              <span class="lightning">⚡</span>
              <span class="littly-text">litt.ly</span>
              <span class="badge-sub">나만의 페이지 만들기</span>
            </div>
          </div>
        </div>
      </div>

      <!-- iPhone Home Indicator Bar -->
      <div class="iphone-home-bar"></div>
    </div>
  </div>
</template>

<style scoped>
.interactive-phone-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

/* Realistic iPhone Device Shell */
.iphone-frame {
  width: 258px;
  height: 382px;
  background: #F8FAFC;
  border-radius: 38px;
  border: 4.5px solid #1E293B;
  box-shadow: 0 16px 36px rgba(15, 23, 42, 0.18), 0 0 0 1px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* Dynamic Island Notch */
.iphone-notch {
  position: absolute;
  top: 7px;
  left: 50%;
  transform: translateX(-50%);
  width: 72px;
  height: 16px;
  background: #0F172A;
  border-radius: 10px;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 7px;
  pointer-events: none;
}

.notch-lens {
  width: 5.5px;
  height: 5.5px;
  background: #1E293B;
  border-radius: 50%;
}

/* Gesture Interaction Tooltip */
.swipe-hint {
  position: absolute;
  top: 32px;
  left: 50%;
  transform: translateX(-50%);
  background: #0F172A;
  color: #FFFFFF;
  font-size: 0.62rem;
  font-weight: 700;
  padding: 3px 9px;
  border-radius: 10px;
  z-index: 25;
  white-space: nowrap;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  animation: bounce 1.8s infinite;
  pointer-events: none;
}

@keyframes bounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50% { transform: translateX(-50%) translateY(-3px); }
}

.fade-leave-active {
  transition: opacity 0.4s;
}
.fade-leave-to {
  opacity: 0;
}

/* Scrollable Screen (Clean Littly Canvas) */
.iphone-screen-scroll {
  flex: 1;
  width: 100%;
  background: #F8FAFC;
  overflow-y: auto;
  overflow-x: hidden;
  cursor: grab;
  user-select: none;
  scrollbar-width: none;
  -ms-overflow-style: none;
  padding: 30px 11px 22px;
}

.iphone-screen-scroll::-webkit-scrollbar {
  display: none;
}

.iphone-screen-scroll.grabbing {
  cursor: grabbing;
}

.screen-content {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

/* 1. Profile Header */
.littly-profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding-top: 4px;
}

.profile-avatar-wrap {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.1);
  border: 2px solid #FFFFFF;
  margin-bottom: 5px;
  background: #E0F2FE;
}

.profile-avatar-svg {
  width: 100%;
  height: 100%;
  display: block;
}

.profile-name-row {
  display: flex;
  align-items: center;
  gap: 4px;
}

.profile-name {
  font-size: 0.84rem;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.2;
}

.verified-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 13px;
  height: 13px;
  background: #2563EB;
  color: #FFFFFF;
  font-size: 0.5rem;
  font-weight: 900;
  border-radius: 50%;
}

.profile-bio {
  font-size: 0.58rem;
  color: #64748B;
  line-height: 1.35;
  margin: 3px 0 6px;
  max-width: 90%;
}

.social-icon-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.social-btn {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  transition: transform 0.15s ease;
}

.social-btn:hover {
  transform: translateY(-1px);
}

/* 2. Featured Large Card Block */
.featured-link-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 8px 10px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.featured-link-card:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 10px rgba(15, 23, 42, 0.08);
}

.card-icon-box {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: #EFF6FF;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.card-icon {
  font-size: 1.05rem;
}

.card-text-box {
  flex: 1;
  min-width: 0;
}

.card-tag {
  font-size: 0.46rem;
  font-weight: 800;
  color: #2563EB;
  letter-spacing: 0.03em;
}

.card-title {
  font-size: 0.64rem;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-desc {
  font-size: 0.52rem;
  color: #64748B;
  margin-top: 1px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-chevron {
  font-size: 0.85rem;
  font-weight: 700;
  color: #94A3B8;
}

/* 3. Section Title Block */
.section-title-block {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 2px 2px 0;
}

.title-emoji {
  font-size: 0.72rem;
}

.title-text {
  font-size: 0.62rem;
  font-weight: 800;
  color: #334155;
  letter-spacing: -0.01em;
}

/* 4. 2-Column Photo Card Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.littly-grid-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(15, 23, 42, 0.04);
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease;
}

.littly-grid-card:hover {
  transform: translateY(-1px);
}

.grid-card-media {
  position: relative;
  height: 64px;
  overflow: hidden;
  background: #E2E8F0;
}

.grid-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.littly-grid-card:hover .grid-img {
  transform: scale(1.06);
}

.grid-card-body {
  padding: 5px 6px;
}

.grid-title {
  font-size: 0.58rem;
  font-weight: 800;
  color: #0F172A;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.grid-sub {
  font-size: 0.48rem;
  color: #64748B;
  margin-top: 1px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 5. File Download Block */
.file-download-block {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 10px;
  padding: 6px 8px;
  display: flex;
  align-items: center;
  gap: 7px;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.03);
}

.file-icon-wrap {
  width: 26px;
  height: 26px;
  border-radius: 6px;
  background: #FEF2F2;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.file-icon {
  font-size: 0.85rem;
}

.file-text-wrap {
  flex: 1;
  min-width: 0;
}

.file-title {
  font-size: 0.58rem;
  font-weight: 700;
  color: #0F172A;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.file-sub {
  font-size: 0.48rem;
  color: #94A3B8;
}

.file-download-btn {
  font-size: 0.5rem;
  font-weight: 700;
  color: #2563EB;
  background: #EFF6FF;
  padding: 2.5px 6px;
  border-radius: 6px;
  flex-shrink: 0;
}

/* 6. Primary Action Button */
.primary-cta-btn {
  background: #0F172A;
  color: #FFFFFF;
  border-radius: 10px;
  padding: 7px 10px;
  text-align: center;
  font-size: 0.6rem;
  font-weight: 700;
  box-shadow: 0 4px 10px rgba(15, 23, 42, 0.15);
  cursor: pointer;
  transition: transform 0.15s ease, background 0.15s ease;
}

.primary-cta-btn:hover {
  background: #1E293B;
  transform: translateY(-1px);
}

/* 7. Littly Branding Footer */
.littly-branding-footer {
  display: flex;
  justify-content: center;
  padding-top: 4px;
  padding-bottom: 2px;
}

.littly-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  padding: 2.5px 8px;
  border-radius: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.lightning {
  font-size: 0.55rem;
  color: #F59E0B;
}

.littly-text {
  font-size: 0.54rem;
  font-weight: 900;
  color: #0F172A;
  letter-spacing: -0.02em;
}

.badge-sub {
  font-size: 0.46rem;
  color: #94A3B8;
}

/* iPhone Home Bar */
.iphone-home-bar {
  position: absolute;
  bottom: 4px;
  left: 50%;
  transform: translateX(-50%);
  width: 75px;
  height: 3px;
  background: #0F172A;
  opacity: 0.35;
  border-radius: 2px;
  z-index: 30;
  pointer-events: none;
}
</style>
