<script setup lang="ts">
import AnnotatedComparisonTable, { TableRow } from './AnnotatedComparisonTable.vue'

defineProps<{ stage?: number }>()

const headers = ['구분', '일반 생성형 AI (ChatGPT / Gemini)', 'Gemini Notebook (자료 기반 AI)']
const widths: [string, string, string] = ['20%', '40%', '40%']

const rows: TableRow[] = [
  {
    category: '지식 원천',
    left: '사전 학습된 인터넷 거대 지식 (열린 지식)',
    right: '사용자가 직접 업로드한 기관 문서 (닫힌 지식)',
    markType: 'highlight'
  },
  {
    category: '질의 방식',
    left: '"2026 복지관 사업계획서 예시 써줘" (추상적)',
    right: '"올려둔 2026 운영규정 제4조 기준으로 써줘" (구체적)',
    markType: 'underline'
  },
  {
    category: '출처 보장',
    left: '자체 출처 확인 불가 (기억 및 통계 의존)',
    right: '원문 페이지·문단 단위 클릭형 각주 [1][2] 제공',
    markType: 'circle'
  },
  {
    category: '할루시네이션',
    left: '그럴듯하지만 틀린 사실을 지어낼 위험 존재',
    right: '문서 밖의 내용은 지어내지 않고 100% 팩트 방어',
    markType: 'box'
  },
  {
    category: '실무 활용',
    left: '아이디어 브레인스토밍, 초안 영감 획득',
    right: '기관 내부 결재 문서, 예산 비교표, 최종 보고서 작성',
    markType: 'highlight'
  }
]

const footerQuote = '🎯 <strong>핵심 공식</strong>: 범용 AI가 <strong>"도서관 전체에서 찾아오는 AI"</strong>라면, Gemini Notebook은 <strong>"내가 건넨 우리 기관 서류철만 정독하는 AI"</strong>입니다.'
</script>

<template>
  <AnnotatedComparisonTable
    :headers="headers"
    :rows="rows"
    :widths="widths"
    :stage="stage"
    :footer-quote="footerQuote"
  />
</template>
