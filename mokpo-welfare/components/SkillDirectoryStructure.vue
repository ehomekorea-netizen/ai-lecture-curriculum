<script setup lang="ts">
import { ref } from 'vue'
import {
  Folder,
  FolderOpen,
  FileText,
  FileCode,
  FileSpreadsheet,
  FileCheck,
  ChevronRight,
  ChevronDown,
  Sparkles,
  CheckCircle2
} from 'lucide-vue-next'

interface FolderNode {
  id: string
  name: string
  tag: string
  desc: string
  isOpen: boolean
  files: { name: string; desc: string; type: 'code' | 'doc' | 'sheet' | 'yaml' }[]
}

const folders = ref<FolderNode[]>([
  {
    id: 'scripts',
    name: 'scripts/',
    tag: '선택',
    desc: '실행 코드 및 자동화 스크립트',
    isOpen: false,
    files: [
      { name: 'run_report.py', desc: '보고서 자동 추출 파이썬 스크립트', type: 'code' },
      { name: 'data_filter.py', desc: '이상치 검증 및 데이터 필터링', type: 'code' }
    ]
  },
  {
    id: 'references',
    name: 'references/',
    tag: '선택',
    desc: '업무 지침서 및 참고 규정집',
    isOpen: false,
    files: [
      { name: 'welfare_guideline_2026.pdf', desc: '2026 복지사업 표준 운영지침', type: 'doc' },
      { name: 'report_rules.md', desc: '공문서 작성 및 표기 규칙', type: 'doc' }
    ]
  },
  {
    id: 'assets',
    name: 'assets/',
    tag: '선택',
    desc: '표준 템플릿 및 공문 서식 파일',
    isOpen: false,
    files: [
      { name: 'report_template.docx', desc: '기관 표준 결과보고서 양식', type: 'doc' },
      { name: 'summary_form.xlsx', desc: '통계 요약 엑셀 시트 템플릿', type: 'sheet' }
    ]
  },
  {
    id: 'agents',
    name: 'agents/',
    tag: '선택',
    desc: 'UI 연동 및 에이전트 설정',
    isOpen: false,
    files: [
      { name: 'openai.yaml', desc: 'ChatGPT UI 표시 및 파라미터 정의', type: 'yaml' }
    ]
  }
])

function toggleFolder(id: string) {
  const f = folders.value.find(item => item.id === id)
  if (f) f.isOpen = !f.isOpen
}

const allExpanded = ref(false)
function toggleAll() {
  allExpanded.value = !allExpanded.value
  folders.value.forEach(f => {
    f.isOpen = allExpanded.value
  })
}
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[325px] my-auto py-0.5">
    <!-- ── Main 2-Column Grid ── -->
    <div class="grid grid-cols-12 gap-4.5 items-stretch h-full">
      <!-- ── Left Column (7 Cols): Interactive Tree Explorer with Toggle Accordion ── -->
      <div class="col-span-7 flex flex-col justify-between bg-white rounded-3xl border border-slate-200/90 p-4 px-5 shadow-2xs font-mono overflow-hidden">
        <div>
          <!-- Root Folder Header + Quick Toggle Button -->
          <div class="flex items-center justify-between text-slate-900 font-bold text-xs md:text-sm mb-2.5 pb-2 border-b border-slate-100">
            <div class="flex items-center gap-2">
              <FolderOpen :size="16" class="text-amber-500 shrink-0" />
              <span>my-skill/</span>
              <span class="text-[10px] font-sans font-normal text-slate-400">스킬 패키지 트리</span>
            </div>
            <!-- Expand / Collapse All Button -->
            <button
              class="text-[10px] font-sans font-medium px-2 py-0.8 rounded-lg bg-slate-100 hover:bg-blue-50 text-slate-600 hover:text-blue-600 border border-slate-200 transition-colors flex items-center gap-1 cursor-pointer"
              @click="toggleAll"
            >
              <span>{{ allExpanded ? '모두 접기' : '모두 펼치기' }}</span>
            </button>
          </div>

          <!-- Tree Items List (Scrollable if expanded) -->
          <div class="pl-2 space-y-1.5 border-l-2 border-slate-200 ml-2 max-h-[200px] overflow-y-auto pr-1">
            <!-- 1. SKILL.md (REQUIRED - BLUE HIGHLIGHT) -->
            <div class="flex items-center justify-between bg-blue-50/90 border border-blue-200 rounded-xl px-3 py-1.5 text-blue-900 shadow-2xs">
              <div class="flex items-center gap-2">
                <span class="text-slate-400 font-bold text-xs">├──</span>
                <FileText :size="14" class="text-blue-600 shrink-0" />
                <strong class="text-blue-900 text-xs font-bold font-mono">SKILL.md</strong>
              </div>
              <div class="flex items-center gap-2 font-sans">
                <span class="text-[9px] font-bold bg-blue-600 text-white px-2 py-0.5 rounded-full">필수</span>
                <span class="text-[11px] text-blue-900 font-semibold">이름 · 설명 · 업무 지침</span>
              </div>
            </div>

            <!-- 2~5. Toggleable Folder Nodes -->
            <div
              v-for="(folder, fIdx) in folders"
              :key="folder.id"
              class="space-y-1"
            >
              <!-- Folder Header Row (Clickable Toggle) -->
              <div
                class="flex items-center justify-between px-2.5 py-1 rounded-lg text-slate-600 font-sans hover:bg-slate-50 cursor-pointer transition-colors border border-transparent hover:border-slate-200/80"
                @click="toggleFolder(folder.id)"
              >
                <div class="flex items-center gap-1.5 font-mono">
                  <span class="text-slate-300 text-xs">{{ fIdx === folders.length - 1 && !folder.isOpen ? '└──' : '├──' }}</span>
                  <!-- Chevron Icon -->
                  <component
                    :is="folder.isOpen ? ChevronDown : ChevronRight"
                    :size="12"
                    class="text-slate-400 shrink-0 transition-transform"
                  />
                  <!-- Folder Icon -->
                  <component
                    :is="folder.isOpen ? FolderOpen : Folder"
                    :size="14"
                    :class="folder.isOpen ? 'text-amber-500' : 'text-slate-400'"
                    class="shrink-0"
                  />
                  <span class="text-xs font-bold text-slate-700">{{ folder.name }}</span>
                </div>

                <div class="flex items-center gap-1.5 text-slate-400">
                  <span class="text-[9px] bg-slate-100 text-slate-500 px-1.5 py-0.2 rounded font-sans">{{ folder.tag }}</span>
                  <span class="text-[10.5px] font-sans text-slate-400">{{ folder.desc }}</span>
                </div>
              </div>

              <!-- Nested Subfiles (Smooth Expand Transition) -->
              <div
                v-if="folder.isOpen"
                class="pl-6 space-y-1 py-0.5 border-l-2 border-dashed border-slate-200 ml-4 font-mono"
              >
                <div
                  v-for="(file, fileIdx) in folder.files"
                  :key="file.name"
                  class="flex items-center justify-between px-2 py-0.5 rounded bg-slate-50/80 border border-slate-200/50 text-slate-700 text-xs"
                >
                  <div class="flex items-center gap-1.5">
                    <span class="text-slate-300 text-[10px]">{{ fileIdx === folder.files.length - 1 ? '└──' : '├──' }}</span>
                    <FileCode v-if="file.type === 'code'" :size="12" class="text-emerald-500" />
                    <FileSpreadsheet v-else-if="file.type === 'sheet'" :size="12" class="text-green-600" />
                    <FileText v-else-if="file.type === 'doc'" :size="12" class="text-blue-500" />
                    <FileCheck v-else :size="12" class="text-purple-500" />
                    <span class="text-[11px] font-mono text-slate-800">{{ file.name }}</span>
                  </div>
                  <span class="text-[10px] font-sans text-slate-400">{{ file.desc }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Note -->
        <div class="pt-2 border-t border-slate-100 text-[10.5px] text-blue-700 font-sans font-medium flex items-center gap-1.5">
          <CheckCircle2 :size="13" class="text-blue-600 shrink-0" />
          <span>폴더를 클릭하면 하위 상세 파일 구조를 토글하여 확인할 수 있습니다.</span>
        </div>
      </div>

      <!-- ── Right Column (5 Cols): Clean Keynote Core Principle ── -->
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
            실무에서는 복잡한 하위 폴더 없이, <strong>오직 마크다운(SKILL.md) 1장에 업무 지침을 작성</strong>하는 것만으로 완성도 높은 스킬이 동작합니다.
          </p>

          <div class="p-3 rounded-2xl bg-white border border-slate-200/90 text-xs text-slate-700 space-y-1.5 shadow-2xs">
            <div class="flex items-center gap-1.5 font-bold text-slate-900 font-serif text-xs">
              <Sparkles :size="13" class="text-blue-600" />
              <span>SKILL.md 필수 3대 내용</span>
            </div>
            <ul class="text-[11px] text-slate-500 space-y-1 pl-4 list-disc">
              <li>스킬 목적 및 호출 기준 (@스킬명)</li>
              <li>단계별 업무 수행 절차 (5대 목차)</li>
              <li>원자료 수치 대조 및 완성형 서식</li>
            </ul>
          </div>
        </div>

        <div class="pt-2 border-t border-slate-200/80 text-[10px] text-slate-400 font-medium">
          OpenAI 공식 Build Skills 아키텍처 규격 준수
        </div>
      </div>
    </div>
  </div>
</template>
