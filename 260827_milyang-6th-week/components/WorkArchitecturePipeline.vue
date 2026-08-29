<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import {
  Package,
  BookOpenCheck,
  Search,
  X
} from 'lucide-vue-next'

type ModalKey = 'plugin' | 'skill' | null

const base = import.meta.env.BASE_URL || '/'
const resolveAsset = (path: string) => {
  if (!path || path.startsWith('http') || path.startsWith('data:')) return path
  const clean = path.startsWith('/') ? path.slice(1) : path
  return `${base}${clean}`
}

const activeModal = ref<ModalKey>(null)

const closeModal = () => {
  activeModal.value = null
}

const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Escape') closeModal()
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})

const data = {
  plugin: {
    title: '플러그인 (Plugin)',
    badge: '상위 번들 패키지',
    subtitle: '스킬과 도구를 묶어 배포하는 상위 컨테이너',
    desc: '특정 업무(@Documents, @Presentations)에 필요한 스킬(지침)과 외부 커넥터·도구를 하나로 묶어 설치 및 활성화합니다.',
    trigger: '@Documents, @Presentations 호출',
    color: '#7C3AED',
    imageSrc: '/플러그인.png'
  },
  skill: {
    title: '스킬 (Skill)',
    badge: '플러그인 내 세부 지침서',
    subtitle: '반복 업무의 표준 절차 및 품질 지침서',
    desc: '플러그인 안에서 작동하며 문서의 5대 목차 서식 규정, 판단 기준, 품질 검수 규칙을 엄격하게 통제합니다.',
    trigger: 'ChatGPT @ / Codex $ 트리거',
    color: '#2563EB',
    imageSrc: '/스킬.png'
  }
}
</script>

<template>
  <div class="w-full flex flex-col justify-center items-center select-none font-sans text-slate-800 text-left h-[300px] my-auto px-2">
    <!-- ── Main 2-Card Balanced Presentation Layout (Airy & Centered) ── -->
    <div class="grid grid-cols-2 gap-6 w-full max-w-4xl h-full items-stretch">
      <!-- ── CARD 1: 플러그인 (Plugin) ── -->
      <div
        @click="activeModal = 'plugin'"
        class="rounded-2xl p-5 px-6 border border-[#E7E0D4] bg-[#FAF8F4] hover:bg-white hover:border-purple-400 hover:shadow-xl hover:scale-[1.02] transition-all duration-300 cursor-pointer flex flex-col justify-between group shadow-xs"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2.5">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center shrink-0 shadow-2xs group-hover:bg-purple-600 group-hover:text-white transition-colors duration-300">
                <Package :size="18" />
              </div>
              <div>
                <h3 class="text-sm md:text-base font-bold font-serif text-slate-900 leading-tight">
                  플러그인 (Plugin)
                </h3>
                <span class="text-[10.5px] font-mono text-purple-700 font-bold">
                  {{ data.plugin.trigger }}
                </span>
              </div>
            </div>
            <span class="text-[9.5px] px-2.5 py-0.5 rounded-full font-mono font-bold bg-purple-100/80 text-purple-900 border border-purple-200">
              {{ data.plugin.badge }}
            </span>
          </div>

          <h4 class="text-xs font-bold text-purple-950 mb-1">
            {{ data.plugin.subtitle }}
          </h4>
          <p class="text-[11px] text-slate-600 leading-relaxed break-keep">
            {{ data.plugin.desc }}
          </p>
        </div>

        <!-- Card Footer (Click to inspect screenshot preview) -->
        <div class="pt-3 border-t border-slate-200/80 flex items-center justify-between text-[11px] text-purple-700 font-medium">
          <span class="flex items-center gap-1 group-hover:underline">
            <Search :size="13" />
            <span>실무 화면 팝업 보기</span>
          </span>
          <span class="text-[10px] font-mono text-slate-400 group-hover:text-purple-600 transition-colors">
            CLICK TO VIEW
          </span>
        </div>
      </div>

      <!-- ── CARD 2: 스킬 (Skill) ── -->
      <div
        @click="activeModal = 'skill'"
        class="rounded-2xl p-5 px-6 border border-[#E7E0D4] bg-[#FAF8F4] hover:bg-white hover:border-blue-400 hover:shadow-xl hover:scale-[1.02] transition-all duration-300 cursor-pointer flex flex-col justify-between group shadow-xs"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2.5">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center shrink-0 shadow-2xs group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300">
                <BookOpenCheck :size="18" />
              </div>
              <div>
                <h3 class="text-sm md:text-base font-bold font-serif text-slate-900 leading-tight">
                  스킬 (Skill)
                </h3>
                <span class="text-[10.5px] font-mono text-blue-700 font-bold">
                  {{ data.skill.trigger }}
                </span>
              </div>
            </div>
            <span class="text-[9.5px] px-2.5 py-0.5 rounded-full font-mono font-bold bg-blue-100/80 text-blue-900 border border-blue-200">
              {{ data.skill.badge }}
            </span>
          </div>

          <h4 class="text-xs font-bold text-blue-950 mb-1">
            {{ data.skill.subtitle }}
          </h4>
          <p class="text-[11px] text-slate-600 leading-relaxed break-keep">
            {{ data.skill.desc }}
          </p>
        </div>

        <!-- Card Footer (Click to inspect screenshot preview) -->
        <div class="pt-3 border-t border-slate-200/80 flex items-center justify-between text-[11px] text-blue-700 font-medium">
          <span class="flex items-center gap-1 group-hover:underline">
            <Search :size="13" />
            <span>실무 화면 팝업 보기</span>
          </span>
          <span class="text-[10px] font-mono text-slate-400 group-hover:text-blue-600 transition-colors">
            CLICK TO VIEW
          </span>
        </div>
      </div>
    </div>

    <!-- ── APPLE KEYNOTE STYLE LIGHTBOX MODAL (Pure Centered Image + Backdrop Blur) ── -->
    <Teleport to="body">
      <transition name="modal-pop">
        <div
          v-if="activeModal !== null"
          @click="closeModal"
          class="fixed inset-0 z-[9999] bg-black/75 backdrop-blur-md flex flex-col items-center justify-center p-4 md:p-8 cursor-pointer select-none"
        >
          <!-- Modal Card Container (Clicks inside image don't bubble, or clicking anywhere closes) -->
          <div
            @click.stop
            class="relative max-w-4xl max-h-[82vh] flex flex-col items-center justify-center"
          >
            <!-- Pure Image Itself (High-Res, Rounded, Floating Shadow) -->
            <img
              :src="resolveAsset(data[activeModal].imageSrc)"
              :alt="data[activeModal].title"
              class="max-w-full max-h-[78vh] object-contain rounded-2xl shadow-2xl border border-white/20 select-none"
            />

            <!-- Dismiss Hint Bar -->
            <div class="mt-2.5 flex items-center gap-3 text-white/80 text-xs font-medium">
              <span class="px-2.5 py-0.5 rounded-full bg-white/20 backdrop-blur-xs text-[11px] font-mono">
                ESC 또는 바깥 영역을 클릭하여 닫기
              </span>
              <button
                type="button"
                @click="closeModal"
                class="w-6 h-6 rounded-full bg-white/20 hover:bg-white/40 text-white flex items-center justify-center transition-colors cursor-pointer"
              >
                <X :size="14" />
              </button>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>
  </div>
</template>

<style scoped>
/* ── Apple Keynote Lightbox Modal Ultra-Smooth Zoom & Blur ── */
.modal-pop-enter-active,
.modal-pop-leave-active {
  transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1), transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.modal-pop-enter-from {
  opacity: 0;
  transform: scale(0.92);
}

.modal-pop-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>
