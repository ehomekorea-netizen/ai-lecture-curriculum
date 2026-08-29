<script setup lang="ts">
import {
  BookOpenCheck,
  Package,
  Sparkles,
  ArrowRight,
  FileCode2,
  Boxes,
  ChefHat,
  Utensils
} from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[330px] my-auto">
    <!-- ── 2-Column Culinary Analogy Grid (Direct from Screenshot) ── -->
    <div class="grid grid-cols-2 gap-5 items-stretch h-[275px]">
      <!-- ── Left Column: 📘 스킬 (Skill) - 나만의 비법 레시피 ── -->
      <div class="rounded-2xl p-4.5 border border-blue-200/90 bg-gradient-to-br from-blue-50/60 via-white to-blue-50/20 flex flex-col justify-between shadow-2xs hover:shadow-md transition-all">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-2.5 border-b border-blue-100 mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-blue-600 text-white flex items-center justify-center shrink-0 shadow-2xs">
                <BookOpenCheck :size="18" />
              </div>
              <div>
                <span class="text-[9.5px] font-mono font-bold text-blue-600 uppercase tracking-wider block leading-tight">
                  단일 지침서 · SKILL.MD
                </span>
                <h3 class="text-base font-bold font-serif text-slate-900 leading-tight">
                  스킬 (Skill)
                </h3>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10.5px] font-bold bg-blue-100 text-blue-900 border border-blue-200">
              📜 나만의 비법 레시피
            </span>
          </div>

          <!-- Culinary Recipe Bullets -->
          <div class="space-y-2 text-xs">
            <div class="bg-white/85 p-2.5 rounded-xl border border-blue-100/80 shadow-2xs">
              <div class="text-[11px] font-bold text-blue-900 mb-1.5 flex items-center gap-1.5">
                <ChefHat :size="13" class="text-blue-600" />
                <span>요리책에 적어둔 세부 지침:</span>
              </div>
              <ul class="space-y-1 text-[11px] text-slate-700 pl-1">
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-blue-500 shrink-0"></span>
                  <span><strong>작업 순서:</strong> 고기는 3cm로 자를 것 (5대 목차 규정)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-blue-500 shrink-0"></span>
                  <span><strong>품질 기준:</strong> 양념장 비율은 3:2:1 (수치 검수 규칙)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-blue-500 shrink-0"></span>
                  <span><strong>마무리:</strong> 마지막엔 참기름 1스푼 (최종 서식 렌더링)</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bottom Goal -->
        <div class="pt-2 border-t border-blue-100 flex items-center justify-between text-[11px]">
          <span class="font-serif font-bold text-blue-950">👉 핵심 목적: <strong>"어떤 맛(품질)을 낼 것인가?"</strong></span>
          <span class="font-mono text-[10px] text-blue-700 font-bold bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">품질 통제</span>
        </div>
      </div>

      <!-- ── Right Column: 📦 플러그인 (Plugin) - 팀 전용 밀키트 세트 ── -->
      <div class="rounded-2xl p-4.5 border border-purple-200/90 bg-gradient-to-br from-purple-50/60 via-white to-purple-50/20 flex flex-col justify-between shadow-2xs hover:shadow-md transition-all">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-2.5 border-b border-purple-100 mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-purple-600 text-white flex items-center justify-center shrink-0 shadow-2xs">
                <Package :size="18" />
              </div>
              <div>
                <span class="text-[9.5px] font-mono font-bold text-purple-600 uppercase tracking-wider block leading-tight">
                  상위 번들 패키지 · PLUGIN.JSON
                </span>
                <h3 class="text-base font-bold font-serif text-slate-900 leading-tight">
                  플러그인 (Plugin)
                </h3>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10.5px] font-bold bg-purple-100 text-purple-900 border border-purple-200">
              🍱 팀 전용 밀키트 세트
            </span>
          </div>

          <!-- Meal-kit Package Bullets -->
          <div class="space-y-2 text-xs">
            <div class="bg-white/85 p-2.5 rounded-xl border border-purple-100/80 shadow-2xs">
              <div class="text-[11px] font-bold text-purple-900 mb-1.5 flex items-center gap-1.5">
                <Boxes :size="13" class="text-purple-600" />
                <span>레시피 + 조리도구 + 재료를 묶은 패키지:</span>
              </div>
              <ul class="space-y-1 text-[11px] text-slate-700 pl-1">
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-500 shrink-0"></span>
                  <span><strong>조리 도구:</strong> 전용 냄비와 칼 (<code>@Documents</code>, <code>@Presentations</code>)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-500 shrink-0"></span>
                  <span><strong>손질된 재료:</strong> 양념과 원자료 (<code>@GoogleDrive</code>, <code>@Slack</code>)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-500 shrink-0"></span>
                  <span><strong>비법 지침:</strong> 박스에 동봉된 레시피 (스킬 <code>SKILL.md</code>)</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bottom Goal -->
        <div class="pt-2 border-t border-purple-100 flex items-center justify-between text-[11px]">
          <span class="font-serif font-bold text-purple-950">👉 핵심 목적: <strong>"누구에게 어떻게 배포할 것인가?"</strong></span>
          <span class="font-mono text-[10px] text-purple-700 font-bold bg-purple-50 px-2 py-0.5 rounded-md border border-purple-200">조직 배포·표준화</span>
        </div>
      </div>
    </div>

    <!-- ── Bottom Golden Takeaway Quote ── -->
    <div class="slide-footer quote-box text-xs py-1.5 px-3.5 font-medium truncate mt-1">
      🎯 <strong>핵심 요약</strong>: <strong>스킬(레시피)</strong>이 고품질 결과물을 만드는 '품질 지침'이라면, <strong>플러그인(밀키트)</strong>은 팀 전체가 설치해 쓰는 '완성형 업무 도구 상자'
    </div>
  </div>
</template>
