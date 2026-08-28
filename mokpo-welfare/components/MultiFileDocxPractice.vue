<script setup lang="ts">
import { ref } from 'vue'
import {
  FolderPlus,
  FolderOpen,
  FileText,
  FileSpreadsheet,
  FileCheck,
  Sparkles,
  ArrowRight,
  ShieldCheck,
  CheckCircle2,
  Copy,
  Check,
  Upload,
  Files
} from 'lucide-vue-next'

const isCopied = ref(false)

function copyPrompt() {
  const text = `@Documents, 폴더 안의 관련 파일들을 근거로 '2026 고령층 스마트 라이프 지원사업 기획서' 초안을 DOCX로 작성해줘. 목차는 [1. 추진 배경 및 필요성, 2. 사업 목적 및 대상, 3. 세부 프로그램 운영안, 4. 예산 산출 근거, 5. 기대 효과]로 구성하고, 통계 수치는 원자료와 일치시켜줘.`
  navigator.clipboard.writeText(text)
  isCopied.value = true
  setTimeout(() => isCopied.value = false, 2000)
}

const sampleFiles = [
  {
    name: '2026_복지부_정책지침.pdf',
    type: '정부 가이드라인',
    desc: '국정과제 및 시니어 디지털 복지 기준',
    icon: FileText,
    color: '#0284C7'
  },
  {
    name: '타기관_우수사례_노트.docx',
    type: '벤치마킹 리서치',
    desc: '타 지자체 우수 프로그램 운영 사례',
    icon: FileText,
    color: '#2563EB'
  },
  {
    name: '통계청_정보격차_데이터.xlsx',
    type: '공공 실태 통계',
    desc: '고령층 디지털 소외율 통계 데이터',
    icon: FileSpreadsheet,
    color: '#059669'
  }
]
</script>

<template>
  <div class="w-full flex items-stretch gap-3.5 select-none font-sans text-slate-100 text-left h-[325px] my-auto">
    <!-- ── Left Column (46%): STEP 1. 프로젝트 폴더 생성 & 다중 파일 적재 ── -->
    <div class="w-[46%] flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3 shadow-2xs">
      <div>
        <div class="flex items-center justify-between pb-1.5 border-b border-slate-100 mb-2">
          <div class="flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse" />
            <strong class="text-xs font-bold text-white font-serif">
              STEP 1. 프로젝트 폴더 생성 & 다중 파일 적재
            </strong>
          </div>
          <span class="text-[9.5px] px-2 py-0.2 rounded-full bg-blue-950/40 text-blue-400 font-mono font-bold border border-blue-200">
            사전 준비
          </span>
        </div>

        <!-- 1-1. 폴더 생성 액션 -->
        <div class="p-2 rounded-xl bg-blue-950/40 border border-blue-200/80 mb-2 flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center shrink-0 shadow-2xs">
              <FolderPlus :size="13" />
            </div>
            <div>
              <span class="text-[11px] font-bold text-blue-300 block leading-tight">
                1. ChatGPT Work에서 새 프로젝트 폴더 지정
              </span>
              <span class="text-[10px] text-blue-300 font-mono font-semibold">
                📁 실습폴더: <code class="bg-white/80 px-1 rounded">26_신규사업기획/</code>
              </span>
            </div>
          </div>
          <span class="text-[9px] px-1.5 py-0.5 rounded bg-blue-100 text-blue-200 font-bold shrink-0">
            폴더 격리
          </span>
        </div>

        <!-- 1-2. 다중 파일 적재 예시 -->
        <div class="space-y-1.5">
          <div class="text-[10px] font-mono text-slate-400 font-bold flex items-center justify-between">
            <span class="flex items-center gap-1">
              <Upload :size="11" />
              <span>2. 기획 관련 다중 파일들(PDF·DOCX·XLSX 등) 넣기</span>
            </span>
            <span class="text-[9px] text-blue-600 font-normal">N개 파일 지원</span>
          </div>

          <div
            v-for="file in sampleFiles"
            :key="file.name"
            class="p-1.5 px-2.5 rounded-lg bg-white/6 border border-white/10 flex items-center justify-between hover:bg-white/5 transition-colors"
          >
            <div class="flex items-center gap-2 min-w-0">
              <div
                class="w-5 h-5 rounded-md flex items-center justify-center shrink-0 shadow-2xs"
                :style="{ background: file.color + '15', color: file.color }"
              >
                <component :is="file.icon" :size="12" />
              </div>
              <span class="text-[11px] font-mono font-bold text-white truncate">
                {{ file.name }}
              </span>
            </div>
            <span class="text-[9.5px] text-slate-400 truncate ml-2">
              {{ file.desc }}
            </span>
          </div>
        </div>
      </div>

      <!-- Security / Least Privilege Note -->
      <div class="pt-1.5 border-t border-slate-100 flex items-center gap-1.5 text-[10px] text-slate-400">
        <ShieldCheck :size="13" class="text-emerald-600 shrink-0" />
        <span class="truncate">최소 권한 원칙: Work는 지정된 <strong class="text-slate-100">이 폴더 안의 파일들만</strong> 안전하게 조합합니다.</span>
      </div>
    </div>

    <!-- ── Right Column (54%): STEP 2 & STEP 3. @Documents 지시 & 기획서 DOCX 생성 ── -->
    <div class="w-[54%] flex flex-col justify-between bg-white/6 rounded-2xl border border-white/10 p-3 shadow-2xs">
      <!-- Step 2: @Documents 지시문 -->
      <div>
        <div class="flex items-center justify-between pb-1.5 border-b border-slate-100 mb-1.5">
          <div class="flex items-center gap-1.5">
            <Sparkles :size="14" class="text-purple-600" />
            <strong class="text-xs font-bold text-white font-serif">
              STEP 2. @Documents 플러그인 호출 & 기획서 작성 지시
            </strong>
          </div>
          <button
            type="button"
            @click="copyPrompt"
            class="flex items-center gap-1 px-2 py-0.5 rounded-md bg-purple-50 hover:bg-purple-100 text-purple-700 text-[10px] font-mono font-bold transition-colors cursor-pointer border border-purple-200"
          >
            <Check v-if="isCopied" :size="11" class="text-emerald-600" />
            <Copy v-else :size="11" />
            <span>{{ isCopied ? '복사 완료!' : '프롬프트 복사' }}</span>
          </button>
        </div>

        <!-- Prompt Snippet Box -->
        <div class="bg-slate-900 text-slate-100 rounded-xl p-2.5 font-mono text-[10.5px] leading-relaxed border border-slate-800 shadow-inner mb-2 break-keep">
          <span class="text-purple-400 font-bold">@Documents</span>, 폴더 안의 관련 파일들을 근거로 <span class="text-amber-300">고령층 스마트 라이프 지원사업 기획서</span> 초안을 DOCX로 작성해줘.<br>
          목차는 <span class="text-emerald-300">[1.배경·필요성 2.목적·대상 3.세부프로그램 4.예산산출 5.기대효과]</span>로 구성하고, <span class="text-rose-300 font-bold">통계 수치는 원자료와 일치시켜줘.</span>
        </div>
      </div>

      <!-- Step 3: 사업기획서 DOCX 산출물 완성 -->
      <div>
        <div class="p-2 px-3 rounded-xl bg-emerald-950/40 border border-emerald-300/80 flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <div class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-2xs">
              <FileCheck :size="14" />
            </div>
            <div>
              <span class="text-[11.5px] font-bold text-emerald-300 font-serif block leading-tight">
                STEP 3. 2026_신규_사업기획서_초안.docx 완성
              </span>
              <span class="text-[10px] text-emerald-300 font-mono">
                정부 지침 + 우수사례 + 통계자료 등 다중 파일이 결합된 고품질 기획서
              </span>
            </div>
          </div>
          <span class="px-2 py-0.5 rounded-full text-[9.5px] font-bold bg-emerald-600 text-white shadow-2xs shrink-0 font-mono">
            DOCX 완성
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
