<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  ShieldAlert,
  FolderLock,
  FileSearch,
  UserCheck,
  Share2,
  CheckCircle2,
  Lock,
  AlertTriangle
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const stages = [
  {
    step: '01',
    title: '입력 전 (Input)',
    q: '실제 개인정보(실명·연락처·주민번호)가 완벽히 비식별화되었는가?',
    rule: '민감 데이터 사전 차단',
    icon: ShieldAlert,
    color: '#3B82F6'
  },
  {
    step: '02',
    title: '권한 설정 (Permission)',
    q: '전체 폴더가 아니라 실습 전용 폴더만 최소 권한으로 허용했는가?',
    rule: '최소 권한(Least Privilege)',
    icon: FolderLock,
    color: '#8B5CF6'
  },
  {
    step: '03',
    title: '생성 중 (Generation)',
    q: '원자료에 없는 수치를 임의 창작하지 않도록 제약 조건을 명시했는가?',
    rule: '원자료 100% 근거 엄수',
    icon: FileSearch,
    color: '#F59E0B'
  },
  {
    step: '04',
    title: '출력 후 (Review)',
    q: '표와 본문 수치, 페이지 나눔, 출처를 담당자가 직접 대조·검토했는가?',
    rule: '사람의 최종 승인 필수',
    icon: UserCheck,
    color: '#10B981'
  },
  {
    step: '05',
    title: '공유 전 (Share)',
    q: '기관의 보안·보존 정책에 맞는 안전한 내부 위치와 파일명으로 저장했는가?',
    rule: '공식 보존 규정 준수',
    icon: Share2,
    color: '#EC4899'
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Top: 5-Stage Step Flow Cards -->
    <div class="grid grid-cols-5 gap-2.5 mb-2.5">
      <div
        v-for="s in stages"
        :key="s.step"
        class="bg-white/6 rounded-2xl border border-white/10 p-3 shadow-2xs hover:shadow-sm transition-all flex flex-col justify-between"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-mono font-bold" :style="{ color: s.color }">
              STAGE {{ s.step }}
            </span>
            <div
              class="w-6 h-6 rounded-lg flex items-center justify-center shadow-2xs"
              :style="{ background: s.color + '15', color: s.color }"
            >
              <component :is="s.icon" :size="13" />
            </div>
          </div>

          <h4 class="text-xs font-bold text-white font-serif leading-tight mb-1.5">
            {{ s.title }}
          </h4>

          <p class="text-[10px] text-slate-400 leading-relaxed break-keep mb-2">
            {{ s.q }}
          </p>
        </div>

        <div class="pt-2 border-t border-slate-100 flex items-center gap-1 text-[9.5px] font-bold text-slate-300">
          <CheckCircle2 :size="11" :style="{ color: s.color }" class="shrink-0" />
          <span class="truncate">{{ s.rule }}</span>
        </div>
      </div>
    </div>

    <!-- Bottom: Security Rule Banner -->
    <div class="bg-gradient-to-r from-red-50/90 via-orange-50/70 to-amber-50/80 rounded-2xl border border-red-200/90 p-3 flex items-center justify-between gap-4 shadow-xs">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-xl bg-red-600 text-white flex items-center justify-center shrink-0 shadow-xs">
          <Lock :size="18" />
        </div>
        <div>
          <h4 class="text-xs md:text-sm font-bold text-white flex items-center gap-2">
            <span>실무 보안 대원칙: <strong class="text-red-700">최소 권한 부여와 비식별화</strong></span>
            <span class="px-2 py-0.5 rounded-md bg-red-600 text-white text-[10px] font-mono font-bold">보안 지침</span>
          </h4>
          <p class="text-[11.5px] text-slate-300 leading-relaxed mt-0.5">
            편의상 '전체 드라이브'를 허용하지 않으며, 클라이언트 실명·사례 정보는 사전에 가명 처리 후 작업합니다.
          </p>
        </div>
      </div>

      <div class="px-3 py-1.5 rounded-xl bg-white/6 border border-red-300 text-[11px] font-bold text-red-800 shadow-2xs shrink-0 flex items-center gap-1.5">
        <AlertTriangle :size="13" class="text-red-600" />
        <span>내부 보안 규정 준수</span>
      </div>
    </div>
  </div>
</template>
