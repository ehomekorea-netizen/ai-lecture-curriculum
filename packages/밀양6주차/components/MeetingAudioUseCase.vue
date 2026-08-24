<script setup lang="ts">
import { ref } from 'vue'
import {
  Mic,
  Package,
  BookOpenCheck,
  Sparkles,
  FileText,
  CheckCircle2,
  Copy,
  Check,
  ShieldCheck,
  ListTodo,
  Volume2,
  ArrowRight
} from 'lucide-vue-next'

const isCopied = ref(false)

function copyStarterPrompt() {
  const prompt = `@Documents, 회의 녹음 파일 [2026_1분기_기관운영위원회_녹음.m4a]를 분석하여:
1. 안건별 핵심 논의 내용과 최종 '의결 결정 사항'을 도출해줘.
2. 기관 표준 서식에 맞춘 '공식 운영위원회 회의록'을 DOCX로 작성해줘.
3. 부서별 '후속 조치 과제(Action Items)'와 담당자·마감기한을 표로 정리해줘.

• 미합의 쟁점이나 추가 확인이 필요한 사항은 [추후 재논의]로 명확히 표시`
  
  navigator.clipboard.writeText(prompt)
  isCopied.value = true
  setTimeout(() => isCopied.value = false, 2000)
}
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[330px] my-auto">
    <!-- ── Top: Skills & Plugins Tag Bar (Matches OpenAI Use Case Header) ── -->
    <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200/90 shadow-2xs mb-2">
      <div class="flex items-center gap-2">
        <span class="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">
          Skills & Plugins
        </span>
        <div class="flex items-center gap-1.5">
          <span class="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-amber-100 text-amber-900 border border-amber-200 flex items-center gap-1">
            <Mic :size="11" />
            <span>@Voice / Whisper (음성 전사)</span>
          </span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-mono font-bold bg-purple-100 text-purple-900 border border-purple-200 flex items-center gap-1">
            <Package :size="11" />
            <span>@Documents (회의록 DOCX)</span>
          </span>
        </div>
      </div>
      <span class="text-[10.5px] text-slate-500 font-medium">
        회의 음성(m4a/mp3) ➔ <strong>표준 회의록(DOCX)</strong> & <strong>실행과제 표</strong> 자동 도출
      </span>
    </div>

    <!-- ── Main 2-Column Grid (Left: Starter Prompt & Intro, Right: Step-by-Step Workflow & Skills) ── -->
    <div class="grid grid-cols-12 gap-3.5 items-stretch h-[270px]">
      <!-- ── Left Column (54% / 7 Cols): Starter Prompt & Introduction ── -->
      <div class="col-span-7 flex flex-col justify-between bg-white rounded-2xl border border-slate-200/90 p-3 shadow-2xs">
        <div>
          <!-- Starter Prompt Header -->
          <div class="flex items-center justify-between pb-1.5 border-b border-slate-100 mb-1.5">
            <span class="text-[11px] font-bold text-slate-900 font-serif flex items-center gap-1">
              <Sparkles :size="13" class="text-purple-600" />
              <span>Starter prompt (실무 시작 지시문)</span>
            </span>
            <button
              type="button"
              @click="copyStarterPrompt"
              class="flex items-center gap-1 px-2 py-0.5 rounded-md bg-purple-50 hover:bg-purple-100 text-purple-700 text-[10px] font-mono font-bold transition-colors cursor-pointer border border-purple-200"
            >
              <Check v-if="isCopied" :size="11" class="text-emerald-600" />
              <Copy v-else :size="11" />
              <span>{{ isCopied ? '복사 완료!' : '프롬프트 복사' }}</span>
            </button>
          </div>

          <!-- Starter Prompt Dark Code Box -->
          <div class="bg-slate-900 text-slate-100 rounded-xl p-2.5 font-mono text-[10px] leading-relaxed border border-slate-800 shadow-inner mb-2 break-keep">
            <span class="text-purple-400 font-bold">@Documents</span>, 회의 녹음 <span class="text-amber-300">[2026_1분기_운영위원회_녹음.m4a]</span>를 분석하여:<br>
            1. 안건별 논의 사항과 <span class="text-emerald-300">'최종 의결 결정 사항'</span>을 도출해줘.<br>
            2. 공공 표준 서식에 맞춘 <span class="text-sky-300">'공식 운영위원회 회의록'</span>을 DOCX로 작성해줘.<br>
            3. 부서별 <span class="text-yellow-300 font-bold">'후속 조치 과제(Action Items)'</span>와 담당자·마감기한을 표로 정리해줘.
          </div>

          <!-- Introduction text -->
          <div class="text-[10.5px] text-slate-600 leading-snug break-keep">
            <strong class="text-slate-900 font-serif block mb-0.5">📌 회의록 타이핑 부담 100% 해소</strong>
            1~2시간 분량의 긴 회의 음성을 일일이 받아 적을 필요 없이, <strong>핵심 결정 사항</strong>과 <strong>부서별 실행 과제(To-Do List)</strong>가 체계화된 완성형 회의록(DOCX)으로 자동 생성합니다.
          </div>
        </div>

        <div class="pt-1.5 border-t border-slate-100 flex items-center justify-between text-[9.5px] text-slate-500 font-mono">
          <span>산출물: 2026_운영위원회_회의록.docx</span>
          <span>화자 분리 & 의결 사항 매핑</span>
        </div>
      </div>

      <!-- ── Right Column (46% / 5 Cols): 3-Step Agent Workflow & Skills to consider ── -->
      <div class="col-span-5 flex flex-col justify-between bg-[#FAF8F4] rounded-2xl border border-slate-200/90 p-3 shadow-2xs">
        <div>
          <span class="text-[11px] font-bold text-slate-900 font-serif block mb-2">
            3-Step 에이전트 실행 흐름
          </span>

          <!-- 3 Steps -->
          <div class="space-y-1.5">
            <div class="p-1.5 px-2.5 rounded-lg bg-white border border-slate-200/90 flex items-start gap-2 shadow-2xs">
              <span class="w-4 h-4 rounded-full bg-amber-100 text-amber-800 text-[9.5px] font-bold font-mono flex items-center justify-center shrink-0 mt-0.5">1</span>
              <div>
                <strong class="text-[10.5px] text-slate-900 block font-serif leading-tight">음성 전사 & 화자 분리 (Whisper)</strong>
                <span class="text-[9.5px] text-slate-500">참여자별 핵심 발언 요약 및 타임스탬프 기록</span>
              </div>
            </div>

            <div class="p-1.5 px-2.5 rounded-lg bg-white border border-slate-200/90 flex items-start gap-2 shadow-2xs">
              <span class="w-4 h-4 rounded-full bg-purple-100 text-purple-800 text-[9.5px] font-bold font-mono flex items-center justify-center shrink-0 mt-0.5">2</span>
              <div>
                <strong class="text-[10.5px] text-slate-900 block font-serif leading-tight">의결 사항 & 쟁점 매트릭스 도출</strong>
                <span class="text-[9.5px] text-slate-500">원안 가결, 수정 합의, 보류 안건 구조화</span>
              </div>
            </div>

            <div class="p-1.5 px-2.5 rounded-lg bg-white border border-slate-200/90 flex items-start gap-2 shadow-2xs">
              <span class="w-4 h-4 rounded-full bg-emerald-100 text-emerald-800 text-[9.5px] font-bold font-mono flex items-center justify-center shrink-0 mt-0.5">3</span>
              <div>
                <strong class="text-[10.5px] text-slate-900 block font-serif leading-tight">공식 DOCX 회의록 & 실행과제표 렌더링</strong>
                <span class="text-[9.5px] text-slate-500">공공 표준 서식 회의록 + 담당자별 To-Do 표 완성</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Skills to consider footer -->
        <div class="pt-2 border-t border-slate-200/80">
          <div class="flex items-center justify-between text-[9.5px]">
            <span class="font-bold text-slate-700">Skills to consider:</span>
            <div class="flex items-center gap-1 font-mono text-purple-700 font-bold">
              <span>$transcribe</span> · <span>$docx</span> · <span>$action-items</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
