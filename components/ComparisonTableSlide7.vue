<script setup lang="ts">
import AnnotatedComparisonTable, { TableRow } from './AnnotatedComparisonTable.vue'

defineProps<{ stage?: number }>()

const headers = ['구분', '검색 (Search Engine)', '생성 (Generative AI)']
const widths: [string, string, string] = ['22%', '39%', '39%']

const rows: TableRow[] = [
  {
    category: '기본 동작',
    left: '존재하는 정보를 찾아서 보여준다',
    right: '문맥에 맞는 응답을 새롭게 조립한다',
    markType: 'highlight'
  },
  {
    category: '데이터 접근',
    left: '원문 웹문서에 직접 접근',
    right: '학습된 신경망 패턴을 활용',
    markType: 'box'
  },
  {
    category: '출처 보장',
    left: '원문 출처 링크 명확 (URL)',
    right: '자체 출처 보장 불가 (기억 의존)',
    markType: 'circle'
  },
  {
    category: '최대 강점',
    left: '정확한 사실, 최신 통계, 법령 번호',
    right: '논리적 요약, 기획서 초안, 표 변환, 번역',
    markType: 'underline'
  }
]

const footerQuote = '<span class="i-carbon:rocket text-cyan-400 inline-block mr-1"></span> <strong>스마트 워크플로우</strong>: <code>[1. 최신 검색] ➔ [2. 근거 문서 확보] ➔ [3. AI 생성 요청] ➔ [4. 출처 기반 최종 검증]</code>'
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
