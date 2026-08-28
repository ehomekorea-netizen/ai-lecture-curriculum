<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  FileSearch,
  Calculator,
  ShieldCheck,
  LayoutTemplate,
  FolderSync,
  UserCheck,
  AlertTriangle,
  CheckCircle2
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const checkItems = [
  {
    num: '01',
    category: '내용 정합성',
    en: 'Content Integrity',
    desc: '원자료에 없는 사실·수치가 임의로 추가되지 않았고, 불확실한 내용은 [확인 필요]로 명시되었는가?',
    icon: FileSearch,
    color: '#3B82F6',
    passCriteria: '원자료 100% 근거 엄수'
  },
  {
    num: '02',
    category: '수치 일치성',
    en: 'Numerical Accuracy',
    desc: '본문 요약 수치와 상세 표의 합계·단위(명, 원, %, 회차)가 서로 모순 없이 일치하는가?',
    icon: Calculator,
    color: '#8B5CF6',
    passCriteria: '표 vs 본문 합계 완벽 일치'
  },
  {
    num: '03',
    category: '개인정보 보호',
    en: 'Privacy & Security',
    desc: '참여자 실명, 연락처, 주민번호, 민감한 사례관리 기록이 완전히 제거·가명화되었는가?',
    icon: ShieldCheck,
    color: '#10B981',
    passCriteria: '민감정보 0% 비식별화'
  },
  {
    num: '04',
    category: '문서 서식 품질',
    en: 'Formatting & Layout',
    desc: '제목 계층(H1/H2), 표 너비 잘림 방지, 페이지 넘김 위치, 기관 지정 글꼴이 바르게 적용되었는가?',
    icon: LayoutTemplate,
    color: '#F59E0B',
    passCriteria: '인쇄/공유 즉시 가독성 확보'
  },
  {
    num: '05',
    category: '파일 버전 관리',
    en: 'File Versioning',
    desc: '출력 폴더 위치, 명확한 파일명(`결과보고서_v1.0.docx`), 작성일, 기준 원자료가 기록되었는가?',
    icon: FolderSync,
    color: '#EC4899',
    passCriteria: '추적 가능한 버전 기록'
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Top: 5-Item Audit Grid -->
    <div class="grid grid-cols-5 gap-2.5 mb-2.5">
      <div
        v-for="(item, idx) in checkItems"
        :key="item.num"
        class="bg-white/6 rounded-2xl border border-white/10 p-3 shadow-2xs hover:shadow-sm transition-all flex flex-col justify-between"
      >
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-mono font-bold" :style="{ color: item.color }">
              CHECK {{ item.num }}
            </span>
            <div
              class="w-6 h-6 rounded-lg flex items-center justify-center shadow-2xs"
              :style="{ background: item.color + '15', color: item.color }"
            >
              <component :is="item.icon" :size="13" />
            </div>
          </div>

          <h4 class="text-xs font-bold text-white font-serif leading-tight mb-1">
            {{ item.category }}
          </h4>
          <span class="text-[9.5px] font-mono text-slate-400 block mb-2">
            {{ item.en }}
          </span>

          <p class="text-[10px] text-slate-400 leading-relaxed break-keep">
            {{ item.desc }}
          </p>
        </div>

        <div class="mt-2.5 pt-2 border-t border-slate-100 flex items-center gap-1 text-[9.5px] font-bold text-slate-300">
          <CheckCircle2 :size="11" :style="{ color: item.color }" class="shrink-0" />
          <span class="truncate">{{ item.passCriteria }}</span>
        </div>
      </div>
    </div>

    <!-- Bottom: Human-in-the-loop Final Approval Banner -->
    <div class="bg-gradient-to-r from-amber-50/90 via-orange-50/70 to-yellow-50/80 rounded-2xl border border-amber-200/90 p-3 flex items-center justify-between gap-4 shadow-xs">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-xl bg-amber-600 text-white flex items-center justify-center shrink-0 shadow-xs">
          <UserCheck :size="18" />
        </div>
        <div>
          <h4 class="text-xs md:text-sm font-bold text-white flex items-center gap-2">
            <span>사람의 최종 승인 원칙: <strong class="text-amber-800">Human-in-the-Loop</strong></span>
            <span class="px-2 py-0.5 rounded-md bg-amber-600 text-white text-[10px] font-mono font-bold">책임 소재</span>
          </h4>
          <p class="text-[11.5px] text-slate-300 leading-relaxed mt-0.5">
            AI가 생성한 결과물은 언제나 <strong>'초안(Draft)'</strong>입니다. 수치 대조, 사실 확인, 기관 공식 표현의 최종 검토 및 책임은 <strong class="text-white">업무 담당자</strong>에게 있습니다.
          </p>
        </div>
      </div>

      <div class="px-3 py-1.5 rounded-xl bg-white/6 border border-amber-300 text-[11px] font-bold text-amber-900 shadow-2xs shrink-0 flex items-center gap-1.5">
        <AlertTriangle :size="13" class="text-amber-600" />
        <span>무검수 제출 절대 금지</span>
      </div>
    </div>
  </div>
</template>
