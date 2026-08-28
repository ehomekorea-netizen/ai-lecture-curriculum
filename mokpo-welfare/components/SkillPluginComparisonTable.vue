<script setup lang="ts">
import {
  BookOpenCheck,
  Package
} from 'lucide-vue-next'

const headers = ['구분', '스킬 (Skill)', '플러그인 (Plugin)']
const widths = ['18%', '41%', '41%']

const rows = [
  {
    category: '본질적 역할',
    skill: '"어떻게 일할 것인가?" (세부 작업 규칙)',
    plugin: '"어떤 도구로 일하고, 누구와 공유할 것인가?"'
  },
  {
    category: '실제 형태',
    skill: '마크다운 파일 1개 (SKILL.md)',
    plugin: '스킬 + 외부 도구 + 이름표를 묶은 폴더/패키지'
  },
  {
    category: '사용 대상',
    skill: '나 혼자 내 ChatGPT에서 지침으로 쓸 때',
    plugin: '팀원 전체 / 전사에 배포하여 설치하게 할 때'
  },
  {
    category: '포함 관계',
    skill: '플러그인 안에 들어가는 부품',
    plugin: '여러 스킬들을 담는 상위 바구니'
  },
  {
    category: '강의실 비유',
    skill: '"신입사원 업무 지침서"',
    plugin: '"노트북 + 사내 인트라넷 계정 + 지침서 세트"'
  }
]
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-100 text-left h-[305px] my-auto">
    <!-- ── Crisp Comparison Table (Slide 7 Styling, Static Pure Layout) ── -->
    <table class="w-full border-collapse bg-white/6 rounded-xl overflow-hidden border border-white/10 shadow-xs text-xs table-fixed">
      <thead>
        <tr class="bg-white/6 text-white font-bold border-b border-white/10 h-[36px]">
          <th :style="{ width: widths[0] }" class="p-2 px-3 text-left font-bold text-slate-100">
            {{ headers[0] }}
          </th>
          <th :style="{ width: widths[1] }" class="p-2 px-3 text-left font-bold text-blue-200 bg-blue-950/40 border-l border-white/10">
            <div class="flex items-center gap-1.5">
              <BookOpenCheck :size="14" class="text-blue-600 shrink-0" />
              <span>{{ headers[1] }}</span>
            </div>
          </th>
          <th :style="{ width: widths[2] }" class="p-2 px-3 text-left font-bold text-purple-900 bg-purple-50/50 border-l border-white/10">
            <div class="flex items-center gap-1.5">
              <Package :size="14" class="text-purple-600 shrink-0" />
              <span>{{ headers[2] }}</span>
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, idx) in rows"
          :key="idx"
          class="border-b border-white/10 transition-colors h-[38px]"
          :class="idx % 2 === 1 ? 'bg-white/6' : 'bg-white/6'"
        >
          <!-- Category -->
          <td class="p-2 px-3 font-bold text-white align-middle">
            {{ row.category }}
          </td>

          <!-- Skill Column -->
          <td class="p-2 px-3 text-slate-300 font-medium border-l border-white/10 align-middle leading-tight">
            {{ row.skill }}
          </td>

          <!-- Plugin Column -->
          <td class="p-2 px-3 text-white font-bold border-l border-white/10 align-middle leading-tight bg-purple-50/20">
            {{ row.plugin }}
          </td>
        </tr>
      </tbody>
    </table>

    <!-- ── Bottom Golden Takeaway Quote ── -->
    <div class="slide-footer quote-box text-xs py-1.5 px-3.5 font-medium truncate mt-2">
      💡 <strong>핵심 요약</strong>: <strong>스킬</strong>은 '나만의 고품질 지침서'이고, <strong>플러그인</strong>은 '팀 전체가 원클릭으로 설치하는 완성형 도구 세트'
    </div>
  </div>
</template>
