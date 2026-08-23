<script setup lang="ts">
import {
  BookOpenCheck,
  Package,
  ArrowRight,
  User,
  Users,
  Sparkles,
  ChefHat,
  Boxes
} from 'lucide-vue-next'
</script>

<template>
  <div class="w-full flex flex-col justify-between select-none font-sans text-slate-800 text-left h-[330px] my-auto">
    <!-- ── 2-Column Side-by-Side Metaphor Cards ── -->
    <div class="grid grid-cols-2 gap-6 items-stretch h-[270px]">
      <!-- ── CARD 1: 스킬 (나만의 비법 레시피) ── -->
      <div class="rounded-2xl p-5 border border-blue-200/90 bg-gradient-to-br from-blue-50/70 via-white to-blue-50/30 flex flex-col justify-between shadow-xs hover:shadow-md transition-all">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center shrink-0 shadow-sm">
                <BookOpenCheck :size="20" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-blue-700 uppercase tracking-wider block leading-tight">
                  개인 활용 단계
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

          <!-- Key Metaphor Content -->
          <div class="space-y-2 text-xs">
            <div class="flex items-start gap-2 bg-white/80 p-2 rounded-xl border border-blue-100">
              <User :size="14" class="text-blue-600 shrink-0 mt-0.5" />
              <div>
                <strong class="text-slate-900 block font-serif">사용 대상: 나 혼자 개인적으로 활용</strong>
                <span class="text-slate-600 text-[11px]">내 컴퓨터의 ChatGPT에서 단독으로 테스트하고 작성할 때</span>
              </div>
            </div>

            <div class="flex items-start gap-2 bg-white/80 p-2 rounded-xl border border-blue-100">
              <ChefHat :size="14" class="text-blue-600 shrink-0 mt-0.5" />
              <div>
                <strong class="text-slate-900 block font-serif">역할: 업무 절차 & 품질 지침서</strong>
                <span class="text-slate-600 text-[11px]">주방에서 셰프 혼자 보며 요리하는 5대 목차와 비법 작성 규칙</span>
              </div>
            </div>
          </div>
        </div>

        <div class="pt-2 border-t border-blue-100 flex items-center justify-between text-[10.5px] text-blue-800 font-mono font-semibold">
          <span>작성 파일: SKILL.md 지침서</span>
          <span>개인용 워크플로우</span>
        </div>
      </div>

      <!-- ── CARD 2: 플러그인 (팀이 함께 쓰는 밀키트 패키지) ── -->
      <div class="rounded-2xl p-5 border border-purple-200/90 bg-gradient-to-br from-purple-50/70 via-white to-purple-50/30 flex flex-col justify-between shadow-xs hover:shadow-md transition-all">
        <div>
          <!-- Header -->
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2.5">
              <div class="w-10 h-10 rounded-xl bg-purple-600 text-white flex items-center justify-center shrink-0 shadow-sm">
                <Package :size="20" />
              </div>
              <div>
                <span class="text-[10px] font-mono font-bold text-purple-700 uppercase tracking-wider block leading-tight">
                  조직 배포 단계
                </span>
                <h3 class="text-base font-bold font-serif text-slate-900 leading-tight">
                  플러그인 (Plugin)
                </h3>
              </div>
            </div>
            <span class="px-2.5 py-1 rounded-full text-[10.5px] font-bold bg-purple-100 text-purple-900 border border-purple-200">
              🍱 팀이 함께 쓰는 밀키트
            </span>
          </div>

          <!-- Key Metaphor Content -->
          <div class="space-y-2 text-xs">
            <div class="flex items-start gap-2 bg-white/80 p-2 rounded-xl border border-purple-100">
              <Users :size="14" class="text-purple-600 shrink-0 mt-0.5" />
              <div>
                <strong class="text-slate-900 block font-serif">사용 대상: 팀원 및 기관 전체 배포</strong>
                <span class="text-slate-600 text-[11px]">동료들이 클릭 한 번으로 설치해 전사 동일한 품질로 쓸 때</span>
              </div>
            </div>

            <div class="flex items-start gap-2 bg-white/80 p-2 rounded-xl border border-purple-100">
              <Boxes :size="14" class="text-purple-600 shrink-0 mt-0.5" />
              <div>
                <strong class="text-slate-900 block font-serif">역할: 지침 + 도구(MCP) 결합 패키지</strong>
                <span class="text-slate-600 text-[11px]">누구나 요리해도 똑같은 맛이 나도록 도구와 지침을 묶은 완성형 세트</span>
              </div>
            </div>
          </div>
        </div>

        <div class="pt-2 border-t border-purple-100 flex items-center justify-between text-[10.5px] text-purple-800 font-mono font-semibold">
          <span>패키지: .codex-plugin/ (원클릭 설치)</span>
          <span>조직 표준 배포</span>
        </div>
      </div>
    </div>

    <!-- ── Bottom Golden Takeaway Quote Box ── -->
    <div class="slide-footer quote-box text-xs py-1.5 px-4 font-medium truncate mt-1">
      🎯 <strong>핵심 비유 공식</strong>: 나 혼자 쓸 때는 <strong>스킬(비법 레시피)</strong>로 시작하고, 팀 전체에 전사 표준으로 공유할 때 <strong>플러그인(밀키트 세트)</strong>으로 묶습니다.
    </div>
  </div>
</template>
