<script setup lang="ts">
import {
  Folder,
  FolderOpen,
  FileText,
  Sparkles,
  CheckCircle2
} from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[310px] my-auto py-1">
    <!-- ── Main 2-Column Grid (Full Canvas Height, Zero Footer Clutter) ── -->
    <div class="grid grid-cols-12 gap-4.5 items-stretch h-full">
      <!-- ── Left Column (7 Cols): Light-Canvas Directory Tree ── -->
      <div class="col-span-7 flex flex-col justify-between bg-white rounded-3xl border border-slate-200/90 p-5 shadow-2xs font-mono">
        <div>
          <!-- Root Folder -->
          <div class="flex items-center gap-2 text-slate-900 font-bold text-sm mb-3 pb-2.5 border-b border-slate-100">
            <FolderOpen :size="16" class="text-amber-500 shrink-0" />
            <span>my-skill/</span>
            <span class="text-[10px] font-sans font-normal text-slate-400 ml-auto">표준 스킬 패키지 구조</span>
          </div>

          <!-- Tree Items List -->
          <div class="pl-3.5 space-y-2 border-l-2 border-slate-200 ml-2">
            <!-- 1. SKILL.md (REQUIRED - BLUE HIGHLIGHT) -->
            <div class="flex items-center justify-between bg-blue-50/90 border border-blue-200 rounded-xl px-3.5 py-2 text-blue-900 shadow-2xs">
              <div class="flex items-center gap-2">
                <span class="text-slate-400 font-bold">├──</span>
                <FileText :size="15" class="text-blue-600 shrink-0" />
                <strong class="text-blue-900 text-xs font-bold font-mono">SKILL.md</strong>
              </div>
              <div class="flex items-center gap-2 font-sans">
                <span class="text-[9.5px] font-bold bg-blue-600 text-white px-2 py-0.5 rounded-full">필수</span>
                <span class="text-[11.5px] text-blue-900 font-semibold">이름 · 설명 · 업무 지침</span>
              </div>
            </div>

            <!-- 2. scripts/ (Optional - Gray) -->
            <div class="flex items-center justify-between px-3.5 py-0.5 text-slate-400 font-sans">
              <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-300">├──</span>
                <Folder :size="13" class="text-slate-400 shrink-0" />
                <span class="text-slate-500 text-xs">scripts/</span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[9px] bg-slate-100 text-slate-500 px-1.5 py-0.2 rounded">선택</span>
                <span class="text-[11px] text-slate-400">실행 코드</span>
              </div>
            </div>

            <!-- 3. references/ (Optional - Gray) -->
            <div class="flex items-center justify-between px-3.5 py-0.5 text-slate-400 font-sans">
              <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-300">├──</span>
                <Folder :size="13" class="text-slate-400 shrink-0" />
                <span class="text-slate-500 text-xs">references/</span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[9px] bg-slate-100 text-slate-500 px-1.5 py-0.2 rounded">선택</span>
                <span class="text-[11px] text-slate-400">참고 문서·가이드</span>
              </div>
            </div>

            <!-- 4. assets/ (Optional - Gray) -->
            <div class="flex items-center justify-between px-3.5 py-0.5 text-slate-400 font-sans">
              <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-300">├──</span>
                <Folder :size="13" class="text-slate-400 shrink-0" />
                <span class="text-slate-500 text-xs">assets/</span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[9px] bg-slate-100 text-slate-500 px-1.5 py-0.2 rounded">선택</span>
                <span class="text-[11px] text-slate-400">템플릿·서식</span>
              </div>
            </div>

            <!-- 5. agents/openai.yaml (Optional - Gray) -->
            <div class="flex items-center justify-between px-3.5 py-0.5 text-slate-400 font-sans">
              <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-300">└──</span>
                <Folder :size="13" class="text-slate-400 shrink-0" />
                <span class="text-slate-500 text-xs">agents/openai.yaml</span>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[9px] bg-slate-100 text-slate-500 px-1.5 py-0.2 rounded">선택</span>
                <span class="text-[11px] text-slate-400">UI 표시 설정</span>
              </div>
            </div>
          </div>
        </div>

        <div class="pt-2.5 border-t border-slate-100 text-[10.5px] text-blue-700 font-sans font-medium flex items-center gap-1.5">
          <CheckCircle2 :size="13" class="text-blue-600" />
          <span>SKILL.md 파일 1개만 있어도 모든 스킬이 100% 동작합니다.</span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Clean Keynote Principle ── -->
      <div class="col-span-5 flex flex-col justify-between bg-[#FAF8F4] rounded-3xl border border-slate-200/90 p-5 shadow-2xs">
        <div>
          <span class="text-[10px] font-mono font-bold text-blue-600 uppercase tracking-wider block mb-1.5">
            Core Practice Rule
          </span>

          <h3 class="text-base md:text-lg font-bold font-serif text-slate-900 leading-tight mb-2.5">
            복잡한 폴더 대신,<br>
            <span class="text-blue-600">SKILL.md 1개에 집중</span>
          </h3>

          <p class="text-xs text-slate-600 leading-relaxed break-keep mb-3.5">
            실무에서는 복잡한 프로그래밍 폴더 없이, <strong>오직 마크다운(SKILL.md) 1장에 업무 지침을 작성</strong>하는 것만으로 충분합니다.
          </p>

          <div class="p-3.5 rounded-2xl bg-white border border-slate-200/90 text-xs text-slate-700 space-y-1.5 shadow-2xs">
            <div class="flex items-center gap-1.5 font-bold text-slate-900 font-serif text-xs">
              <Sparkles :size="13" class="text-blue-600" />
              <span>SKILL.md 필수 3대 내용</span>
            </div>
            <ul class="text-[11.5px] text-slate-500 space-y-1 pl-4 list-disc">
              <li>스킬 목적 및 호출 기준 (@스킬명)</li>
              <li>단계별 업무 수행 절차 (5대 목차 등)</li>
              <li>원자료 수치 대조 및 완성형 서식</li>
            </ul>
          </div>
        </div>

        <div class="pt-2.5 border-t border-slate-200/80 text-[10.5px] text-slate-400 font-medium">
          OpenAI 공식 Build Skills 규격 준수
        </div>
      </div>
    </div>
  </div>
</template>
