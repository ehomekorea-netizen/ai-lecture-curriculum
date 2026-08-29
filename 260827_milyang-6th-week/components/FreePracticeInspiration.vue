<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed } from 'vue'

const scenes = [
  {
    main: '이제, 여러분의 방식대로 해보세요',
    sub: '오늘 배운 플러그인을 자유롭게 조합해 업무의 작은 불편 하나를 해결해봅니다.'
  },
  {
    main: '궁금한 것 하나',
    sub: '불편한 것 하나 · 만들고 싶은 것 하나'
  },
  {
    main: '플러그인은 자유롭게 호출하세요',
    sub: '화면에 보이는 도구를 @ 로 하나 이상 선택해보세요'
  },
  {
    main: '결과물도 자유롭게 정해보세요',
    sub: '보고서 · 표 · 발표자료 · 아이디어 초안'
  },
  {
    main: '첫 결과에서 멈추지 마세요',
    sub: '더 쉽게 · 더 짧게 · 더 창의적으로'
  },
  {
    main: '정답보다, 내 업무에 필요한 결과',
    sub: '이제 시작하세요'
  }
]

const currentIndex = ref(0)
let loopTimer: any = null

onMounted(() => {
  loopTimer = setInterval(() => {
    currentIndex.value = (currentIndex.value + 1) % scenes.length
  }, 1500)
})

onUnmounted(() => {
  if (loopTimer) clearInterval(loopTimer)
})

const activeScene = computed(() => scenes[currentIndex.value])
</script>

<template>
  <div class="w-full flex flex-col justify-between items-center select-none font-sans text-slate-800 text-center h-[330px] my-auto">
    <!-- ── Center Stage (Ultra-Large Statement Typography with 1.5s Auto Loop) ── -->
    <div class="w-full max-w-4xl flex-1 flex flex-col items-center justify-center relative overflow-hidden py-2">
      <Transition name="statement-fade" mode="out-in">
        <div :key="currentIndex" class="flex flex-col items-center justify-center space-y-3 px-4">
          <!-- Statement Big Heading (Apple Keynote Statement Style) -->
          <h2 class="text-3xl md:text-5xl lg:text-[46px] font-bold font-serif text-slate-900 tracking-tight leading-tight break-keep">
            {{ activeScene.main }}
          </h2>

          <!-- Subtitle / Descriptive Message -->
          <p class="text-lg md:text-2xl text-slate-500 font-sans font-medium max-w-2xl leading-relaxed break-keep">
            <template v-if="currentIndex === 2">
              화면에 보이는 도구를 <span class="text-blue-600 font-mono font-bold px-2 py-0.5 rounded-lg bg-blue-50 border border-blue-200">@</span> 로 하나 이상 선택해보세요
            </template>
            <template v-else-if="currentIndex === 5">
              <span class="text-blue-600 font-bold text-2xl font-serif">이제 시작하세요</span>
            </template>
            <template v-else>
              {{ activeScene.sub }}
            </template>
          </p>
        </div>
      </Transition>
    </div>

    <!-- ── Bottom Inspiration Bar ── -->
    <div class="w-full max-w-xl pt-3 pb-1 border-t border-slate-200/90 flex items-center justify-center">
      <p class="text-xs md:text-sm font-serif font-bold text-blue-600 tracking-wide">
        아이디어 하나를 플러그인으로 결과물로 바꿔보세요
      </p>
    </div>
  </div>
</template>

<style scoped>
/* ── Statement Smooth Crossfade & Rise ── */
.statement-fade-enter-active,
.statement-fade-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.statement-fade-enter-from {
  opacity: 0;
  transform: translateY(16px) scale(0.97);
}

.statement-fade-leave-to {
  opacity: 0;
  transform: translateY(-16px) scale(0.97);
}
</style>
