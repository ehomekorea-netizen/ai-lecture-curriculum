<script setup lang="ts">
import { ref, computed, onUnmounted } from 'vue'
import { X } from 'lucide-vue-next'

const cases = [
  {
    id: 0,
    title: '포트폴리오 피치덱을 만드세요',
    description: 'ChatGPT Work를 사용하여 내 프로젝트 경험 기록과 기술 스택을 면접 발표용 8슬라이드 피치덱으로 변환하세요.',
    promptTitle: '면접 피치덱 프레젠테이션 작성 실무 프롬프트',
    glowColor: 'rgba(59, 130, 246, 0.45)',
    borderColor: 'border-blue-500/80',
    prompt: `첨부된 [내_프로젝트_경험기록_및_성과.md]를 검토하여 [기업 면접관 및 심사위원]을 위한 8슬라이드 포트폴리오 피치덱을 작성해줘. 주요 문제 해결 과정(STAR)과 정량적 성과 지표를 포함하고, 보완이 필요한 부분은 [확인 필요]로 표시한 초안을 작성해줘.`
  },
  {
    id: 1,
    title: '채용공고 비교 시트를 만드세요',
    description: 'ChatGPT Work를 사용하여 지원 희망 기업별 채용 공고와 우대조건을 스프레드시트로 변환하고 나만의 지원 전략을 세우세요.',
    promptTitle: '채용공고 비교 스프레드시트 실무 프롬프트',
    glowColor: 'rgba(168, 85, 247, 0.45)',
    borderColor: 'border-purple-500/80',
    prompt: `[지원 희망 3대 IT 기업의 신입 채용 공고]를 비교하는 스프레드시트를 작성해줘. 연봉, 요구 기술, 우대사항, 성장성 기준 점수를 매기고, 내 프로젝트 역량과의 갭(Gap)을 표시하며 맞춤형 지원 전략을 포함하는 요약 탭을 추가해줘.`
  },
  {
    id: 2,
    title: '채용 공고 정기 업데이트를 설정하세요',
    description: '관심 기업의 채용 공고나 실무 프로젝트 진행 상황을 주기적으로 모니터링하고 새로고침할 때 예약된 작업을 활용하세요.',
    promptTitle: '주간 채용 모니터링 실무 프롬프트',
    glowColor: 'rgba(16, 185, 129, 0.45)',
    borderColor: 'border-emerald-500/80',
    prompt: `매주 월요일 아침, [원티드 및 사람인 주요 채용 사이트]의 신규 신입 구직 공고 업데이트를 확인해줘. 지원 자격, 마감일, 필수 스킬을 포함하여 주간 취업 활동 캘린더를 갱신하고 나에게 알림을 보내줘.`
  }
]

const currentIndex = ref(0)
const isModalOpen = ref(false)
const typedText = ref('')
let typingTimer: any = null

const activeCase = computed(() => cases[currentIndex.value] || cases[0])

function setCase(idx: number) {
  currentIndex.value = idx
  closeModal()
}

function openPromptModal() {
  isModalOpen.value = true
  
  if (typingTimer) clearInterval(typingTimer)
  typedText.value = ''
  
  const fullText = activeCase.value.prompt
  let charIdx = 0
  
  typingTimer = setInterval(() => {
    if (charIdx < fullText.length) {
      typedText.value += fullText[charIdx]
      charIdx++
    } else {
      clearInterval(typingTimer)
      typingTimer = null
    }
  }, 20)
}

function closeModal() {
  if (typingTimer) clearInterval(typingTimer)
  isModalOpen.value = false
}

onUnmounted(() => {
  if (typingTimer) clearInterval(typingTimer)
})
</script>

<template>
  <div class="w-full flex flex-col justify-center items-center select-none font-sans text-slate-800 text-left h-[330px] my-auto">
    <!-- ── Apple-Style Minimal Indicator (Dots/Bars) + Center Card ── -->
    <div class="w-full max-w-2xl flex flex-col items-center">
      <!-- Ultra-Minimal Dot/Bar Indicator -->
      <div class="flex items-center justify-center gap-2 mb-4">
        <button
          v-for="(_, idx) in cases"
          :key="idx"
          type="button"
          @click="setCase(idx)"
          class="h-1.5 rounded-full transition-all duration-300 cursor-pointer p-0 border-0"
          :class="[
            currentIndex === idx
              ? 'w-7 bg-blue-600'
              : 'w-2 bg-slate-200 hover:bg-slate-300'
          ]"
        />
      </div>

      <!-- Pure White Card: Physical Mouse Click Trigger ONLY -->
      <div
        @click="openPromptModal"
        class="w-full bg-white rounded-3xl border border-slate-200/90 p-10 shadow-sm hover:shadow-xl hover:border-blue-400 transition-all cursor-pointer text-center flex flex-col items-center justify-center space-y-3 group"
      >
        <!-- Large Title -->
        <h2 class="text-2xl md:text-3xl font-bold font-serif text-slate-900 tracking-tight leading-snug group-hover:text-blue-600 transition-colors">
          {{ activeCase.title }}
        </h2>

        <!-- Subtitle Description -->
        <p class="text-sm md:text-base text-slate-500 max-w-xl leading-relaxed break-keep font-normal">
          {{ activeCase.description }}
        </p>
      </div>
    </div>

    <!-- ── Theatrical Ultra-Large Glowing Modal (Giant Typography for Lecture Hall) ── -->
    <Teleport to="body">
      <Transition name="keynote-modal">
        <div
          v-if="isModalOpen"
          class="fixed inset-0 z-50 flex items-center justify-center p-6 md:p-10 bg-black/80 backdrop-blur-2xl select-none font-sans"
          @click.self="closeModal"
        >
          <!-- Giant Glowing Aura Container (max-w-5xl) -->
          <div
            class="relative w-full max-w-5xl bg-slate-950 border-2 rounded-3xl p-8 md:p-12 shadow-2xl transition-all"
            :class="activeCase.borderColor"
            :style="{
              boxShadow: `0 0 90px ${activeCase.glowColor}, 0 30px 70px rgba(0, 0, 0, 0.95)`
            }"
          >
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-4 border-b border-slate-800/90 mb-6">
              <span class="text-sm md:text-base font-mono font-bold text-slate-300 tracking-wider">
                {{ activeCase.promptTitle }}
              </span>
              <button
                type="button"
                @click="closeModal"
                class="w-10 h-10 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center transition-colors cursor-pointer"
              >
                <X :size="20" />
              </button>
            </div>

            <!-- Typing Prompt Body with Gigantic High-Visibility Text -->
            <div class="bg-slate-900/95 rounded-2xl p-6 md:p-10 border border-slate-800 min-h-[180px] flex items-center shadow-inner">
              <p class="font-sans text-xl md:text-2xl lg:text-[26px] font-semibold text-white leading-relaxed break-keep tracking-tight">
                {{ typedText }}<span class="cursor-blink"></span>
              </p>
            </div>

            <!-- Footer Hint -->
            <div class="mt-4 flex items-center justify-between text-xs md:text-sm text-slate-400 font-mono">
              <span>바깥을 클릭하거나 ESC 키를 누르면 닫힙니다.</span>
              <span class="text-blue-400 font-bold">수강생 실습용 프롬프트</span>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<style scoped>
/* ── Keynote Smooth Scale & Fade ── */
.keynote-modal-enter-active,
.keynote-modal-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.keynote-modal-enter-from,
.keynote-modal-leave-to {
  opacity: 0;
  transform: scale(0.96);
}

/* ── Authentic Terminal Blinking Cursor (High-Visibility) ── */
@keyframes cursor-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.cursor-blink {
  display: inline-block;
  width: 3px;
  height: 1.15em;
  background-color: #60a5fa;
  margin-left: 4px;
  vertical-align: text-bottom;
  animation: cursor-blink 0.85s infinite;
}
</style>
