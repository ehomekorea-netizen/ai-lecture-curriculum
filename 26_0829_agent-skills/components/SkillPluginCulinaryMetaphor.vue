<script setup lang="ts">
import {
  BookOpenCheck,
  Package,
  Boxes,
  ChefHat,
  Scroll,
  Sparkles,
  Target,
  CheckCircle2,
  ArrowRight,
  Lightbulb
} from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-100 text-left h-[330px] my-auto">
    <!-- ── 2-Column Culinary Analogy Grid ── -->
    <div class="grid grid-cols-2 gap-5 items-stretch h-[275px]">
      <!-- ── Left Column: 📘 스킬 (Skill) - 나만의 비법 레시피 ── -->
      <div class="rounded-2xl p-4.5 border border-sky-400/30 bg-white/5 flex flex-col justify-between shadow-xl backdrop-blur-sm">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-2.5 border-b border-white/10 mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-sky-600 text-white flex items-center justify-center shrink-0 shadow-md">
                <BookOpenCheck :size="18" />
              </div>
              <div>
                <span class="text-[9.5px] font-mono font-bold text-sky-400 uppercase tracking-wider block leading-tight">
                  단일 지침서 · SKILL.MD
                </span>
                <h3 class="text-base font-bold font-serif text-white leading-tight">
                  스킬 (Skill)
                </h3>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10.5px] font-bold bg-sky-950/70 text-sky-300 border border-sky-400/50">
              <span class="inline-flex items-center gap-1.5"><Scroll :size="12" class="text-sky-400" /><span>나만의 비법 레시피</span></span>
            </span>
          </div>

          <!-- Culinary Recipe Bullets -->
          <div class="space-y-2 text-xs">
            <div class="bg-white/4 p-2.5 rounded-xl border border-white/10 shadow-xs">
              <div class="text-[11px] font-bold text-sky-300 mb-1.5 flex items-center gap-1.5">
                <ChefHat :size="13" class="text-sky-400" />
                <span>요리책에 적어둔 세부 지침:</span>
              </div>
              <ul class="space-y-1 text-[11px] text-slate-200 pl-1">
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0"></span>
                  <span><strong class="text-white">작업 순서:</strong> 고기는 3cm로 자를 것 (5대 목차 규정)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0"></span>
                  <span><strong class="text-white">품질 기준:</strong> 양념장 비율은 3:2:1 (수치 검수 규칙)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-sky-400 shrink-0"></span>
                  <span><strong class="text-white">마무리:</strong> 마지막엔 참기름 1스푼 (최종 서식 렌더링)</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bottom Goal -->
        <div class="pt-2 border-t border-white/10 flex items-center justify-between text-[11px]">
          <span class="font-serif font-bold text-sky-300"><ArrowRight :size="12" class="inline text-amber-400 mr-1" />핵심 목적: <strong class="text-white">"어떤 맛(품질)을 낼 것인가?"</strong></span>
          <span class="font-mono text-[10px] text-sky-300 font-bold bg-sky-950/70 px-2 py-0.5 rounded-md border border-sky-400/50">품질 통제</span>
        </div>
      </div>

      <!-- ── Right Column: 📦 플러그인 (Plugin) - 팀 전용 밀키트 세트 ── -->
      <div class="rounded-2xl p-4.5 border border-purple-400/30 bg-white/5 flex flex-col justify-between shadow-xl backdrop-blur-sm">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between pb-2.5 border-b border-white/10 mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-purple-600 text-white flex items-center justify-center shrink-0 shadow-md">
                <Package :size="18" />
              </div>
              <div>
                <span class="text-[9.5px] font-mono font-bold text-purple-400 uppercase tracking-wider block leading-tight">
                  상위 번들 패키지 · PLUGIN.JSON
                </span>
                <h3 class="text-base font-bold font-serif text-white leading-tight">
                  플러그인 (Plugin)
                </h3>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10.5px] font-bold bg-purple-950/70 text-purple-300 border border-purple-400/50">
              <span class="inline-flex items-center gap-1.5"><Package :size="12" class="text-purple-400" /><span>팀 전용 밀키트 세트</span></span>
            </span>
          </div>

          <!-- Meal-kit Package Bullets -->
          <div class="space-y-2 text-xs">
            <div class="bg-white/4 p-2.5 rounded-xl border border-white/10 shadow-xs">
              <div class="text-[11px] font-bold text-purple-300 mb-1.5 flex items-center gap-1.5">
                <Boxes :size="13" class="text-purple-400" />
                <span>레시피 + 조리도구 + 재료를 묶은 패키지:</span>
              </div>
              <ul class="space-y-1 text-[11px] text-slate-200 pl-1">
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 shrink-0"></span>
                  <span><strong class="text-white">조리 도구:</strong> 전용 냄비와 칼 (<code class="text-sky-300 bg-sky-950/60 px-1 rounded">@Documents</code>, <code class="text-purple-300 bg-purple-950/60 px-1 rounded">@Presentations</code>)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 shrink-0"></span>
                  <span><strong class="text-white">손질된 재료:</strong> 양념과 원자료 (<code class="text-amber-300 bg-amber-950/60 px-1 rounded">@GoogleDrive</code>, <code class="text-emerald-300 bg-emerald-950/60 px-1 rounded">@Slack</code>)</span>
                </li>
                <li class="flex items-center gap-1.5">
                  <span class="w-1.5 h-1.5 rounded-full bg-purple-400 shrink-0"></span>
                  <span><strong class="text-white">비법 지침:</strong> 박스에 동봉된 레시피 (스킬 <code class="text-indigo-300 bg-indigo-950/60 px-1 rounded">SKILL.md</code>)</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bottom Goal -->
        <div class="pt-2 border-t border-white/10 flex items-center justify-between text-[11px]">
          <span class="font-serif font-bold text-purple-300"><ArrowRight :size="12" class="inline text-amber-400 mr-1" />핵심 목적: <strong class="text-white">"누구에게 어떻게 배포할 것인가?"</strong></span>
          <span class="font-mono text-[10px] text-purple-300 font-bold bg-purple-950/70 px-2 py-0.5 rounded-md border border-purple-400/50">조직 배포·표준화</span>
        </div>
      </div>
    </div>

    <!-- ── Bottom Single Takeaway Bar ── -->
    <div class="p-2 px-3.5 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-200 flex items-center gap-2 shadow-xs">
      <span class="text-rose-400 font-bold"><Target :size="13" class="inline text-rose-400 mr-1" />핵심 요약:</span>
      <span>
        <strong>스킬(레시피)</strong>이 고품질 결과물을 만드는 '품질 지침'이라면,
        <strong>플러그인(밀키트)</strong>은 팀 전체가 설치해 쓰는 '완성형 업무 도구 상자'
      </span>
    </div>
  </div>
</template>
