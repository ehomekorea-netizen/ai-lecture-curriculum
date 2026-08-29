<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import {
  Layers,
  FileText,
  FileCheck2,
  FileX,
  FileSpreadsheet,
  CheckCircle2,
  AlertTriangle,
  FolderGit2,
  Sparkles,
  ArrowRight
} from 'lucide-vue-next'

const props = withDefaults(defineProps<{ stage?: number }>(), { stage: 0 })

const baseFiles = [
  {
    format: 'DOCX',
    rec: '가장 권장 ★★★',
    badge: '최적',
    badgeColor: 'bg-emerald-100 text-emerald-300 border-emerald-300',
    desc: '문단·표·스타일 등 편집 가능한 구조와 서식 체계를 100% 온전히 유지하기 좋음',
    icon: FileText,
    iconColor: 'text-blue-600'
  },
  {
    format: 'Google Docs',
    rec: '사용 가능 ★★☆',
    badge: '가능',
    badgeColor: 'bg-blue-100 text-blue-300 border-blue-300',
    desc: '클라우드에 연결된 Google 문서의 제목 계층과 스타일을 기준으로 활용',
    icon: FileText,
    iconColor: 'text-sky-600'
  },
  {
    format: 'PDF',
    rec: '보조 자료 ★☆☆',
    badge: '보조',
    badgeColor: 'bg-amber-100 text-amber-800 border-amber-300',
    desc: '시각적 배치 참고에는 유용하나, 편집 가능한 레이아웃 기준으로 삼기에는 제한적',
    icon: FileText,
    iconColor: 'text-amber-600'
  },
  {
    format: 'HWP',
    rec: '직접 사용 불가 ✕',
    badge: '변환 필수',
    badgeColor: 'bg-red-100 text-red-800 border-red-300',
    desc: '반드시 한글 프로그램에서 DOCX로 변환·저장한 뒤 레이아웃을 확인하고 사용',
    icon: FileX,
    iconColor: 'text-red-500'
  }
]

const steps = [
  { num: '01', title: 'DOCX 기준 파일 선정', desc: '기관 표준에 가장 가까운 양식 파일 선택' },
  { num: '02', title: '구조·목적 프롬프트', desc: '필수 유지할 표/목차 및 입력자료 설명' },
  { num: '03', title: '템플릿 서식 검증', desc: '표·제목 계층·여백·문체가 일치하는지 확인' },
  { num: '04', title: '신규 데이터 재사용 시험', desc: '새로운 샘플을 넣어 실제 재사용성 테스트' },
  { num: '05', title: '버전 & 업데이트 기록', desc: '담당자·버전(v1.0)·갱신 조건 명시' }
]
</script>

<template>
  <div class="w-full flex items-stretch gap-4 h-full select-none font-sans text-slate-100 text-left py-1">
    <!-- Left Column (46%): Base File Selection Guide -->
    <div class="w-[46%] flex flex-col justify-between space-y-2">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-mono font-bold text-slate-400 flex items-center gap-1.5">
            <Layers :size="13" class="text-blue-600" />
            <span>템플릿 기준 파일 선택 가이드</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-blue-950/40 text-blue-400 border border-blue-200">
            포맷 우선순위
          </span>
        </div>

        <!-- 4 Format Cards -->
        <div class="space-y-1.5">
          <div
            v-for="file in baseFiles"
            :key="file.format"
            class="p-2 px-2.5 rounded-xl bg-white/6 border border-white/10 shadow-2xs flex items-start gap-2.5"
          >
            <component :is="file.icon" :size="16" :class="file.iconColor" class="shrink-0 mt-0.5" />
            <div class="flex-1 min-w-0">
              <div class="flex items-center justify-between mb-0.5">
                <span class="text-xs font-bold font-mono text-white">{{ file.format }}</span>
                <span class="text-[9.5px] px-1.5 py-0.2 rounded font-bold border" :class="file.badgeColor">
                  {{ file.badge }}
                </span>
              </div>
              <p class="text-[10px] text-slate-400 leading-tight">
                {{ file.desc }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- HWP Warning Note -->
      <div class="bg-red-50/80 rounded-xl p-2 border border-red-200 text-[10px] text-red-900 flex items-center gap-1.5 leading-tight">
        <AlertTriangle :size="13" class="text-red-600 shrink-0" />
        <span><strong>HWP 실무 팁</strong>: [파일] ➔ [다른 이름으로 저장] ➔ [DOCX 선택] 후 사용</span>
      </div>
    </div>

    <!-- Right Column (54%): 5-Step Creation Flow & Asset Philosophy -->
    <div class="w-[54%] flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3.5 shadow-sm">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold text-white font-serif flex items-center gap-1.5">
            <Sparkles :size="14" class="text-emerald-600" />
            <span>5단계 템플릿 자산화 프로세스</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-emerald-100 text-emerald-300">
            Template Creator
          </span>
        </div>

        <!-- 5 Steps List -->
        <div class="space-y-1.5">
          <div
            v-for="st in steps"
            :key="st.num"
            class="p-1.5 px-2.5 rounded-xl bg-white/6 border border-white/10 flex items-center justify-between"
          >
            <div class="flex items-center gap-2">
              <span class="w-5 h-5 rounded-full bg-emerald-600 text-white font-mono font-bold text-[10px] flex items-center justify-center shrink-0">
                {{ st.num }}
              </span>
              <div>
                <span class="text-[11.5px] font-bold text-white block leading-tight font-serif">
                  {{ st.title }}
                </span>
                <span class="text-[9.5px] text-slate-400 leading-tight">
                  {{ st.desc }}
                </span>
              </div>
            </div>
            <CheckCircle2 :size="12" class="text-emerald-600 shrink-0" />
          </div>
        </div>
      </div>

      <!-- Core Philosophy Footer -->
      <div class="mt-2 pt-2 border-t border-slate-100 bg-emerald-950/40 p-2 rounded-xl border border-emerald-100 flex items-start gap-1.5 text-[10px] text-emerald-200 leading-tight">
        <FolderGit2 :size="13" class="text-emerald-400 shrink-0 mt-0.5" />
        <span><strong>업무 자산화</strong>: 개인 템플릿을 시작으로, 검증된 서식은 기관의 표준 보고서로 발전시킵니다.</span>
      </div>
    </div>
  </div>
</template>
