// Single source of truth for levels & tool matrices

export interface Level {
  key: string
  short: string
  name: string
  color: string
  ink: string
  aspirational?: boolean
}

export const LEVELS: Level[] = [
  { key: 'manual',      short: 'L0', name: 'Manual',                  color: '#B0A79B', ink: '#2B2620' },
  { key: 'assisted',    short: 'L1', name: 'Assisted (템플릿 복제)',   color: '#859EFF', ink: '#0A1B4D' },
  { key: 'linear',      short: 'L2', name: 'Linear (노션 DB 연동)',   color: '#476BFF', ink: '#FFFFFF' },
  { key: 'conditional', short: 'L3', name: 'Web Deploy (웹 호스팅)',  color: '#53DFA9', ink: '#06281E' },
  { key: 'high',        short: 'L4', name: 'Vibe Coding (AI 생성)',   color: '#A6E05A', ink: '#2B3A08' },
  { key: 'autonomy',    short: 'L5', name: 'Full Agent (자율 완성)',   color: '#CDE519', ink: '#3A3D08', aspirational: true },
]

export interface ToolItem {
  name: string
  category: string
  tag: string
  badge: string
  color: string
  description: string
  pros: string[]
  recommendedFor: string
  icon: string
}

export const TOOL_ECOSYSTEM: ToolItem[] = [
  {
    name: 'Notion Database',
    category: '경험 자산화',
    tag: 'No-Code DB',
    badge: '정리 & 아카이빙',
    color: '#2B2620',
    description: '프로젝트, 역량, 성과 수치를 구조화된 관계형 데이터베이스로 영구 자산화',
    pros: ['갤러리/보드 다각도 뷰', 'ChatGPT @Notion 쉬운 연동', '모바일/데스크톱 완벽 동기화'],
    recommendedFor: '정밀한 이력 관리 및 다수 프로젝트 아카이빙',
    icon: '📊'
  },
  {
    name: 'Littly (리틀리)',
    category: '마이크로 랜딩',
    tag: 'Link-in-Bio',
    badge: '3초 요약 퍼널',
    color: '#FF5A5F',
    description: '채용 담당자의 시선을 3초 만에 사로잡는 모바일 퍼스트 원페이지 브랜딩',
    pros: ['모바일 최적화 UX', '클릭 유도형 CTA 버튼', 'SNS/이력서 프로필 링크 최적화'],
    recommendedFor: 'SNS 유입 및 이력서 상단 퀵 프로필 링크',
    icon: '🔗'
  },
  {
    name: 'Gemini Canvas',
    category: '바이브 웹 빌딩',
    tag: 'Interactive Code',
    badge: '실시간 프리뷰',
    color: '#1A73E8',
    description: '자연어로 HTML/CSS/JS 단일 웹 문서를 만들고 실시간 우측 캔버스에서 확인',
    pros: ['즉각적인 코드 & 렌더링 피드백', '대화형 자연어 디자인 수정', '단일 파일 다운로드 용이'],
    recommendedFor: '나만의 커스텀 1페이지 웹 포트폴리오 초고속 제작',
    icon: '✨'
  },
  {
    name: 'Netlify',
    category: '글로벌 호스팅',
    tag: '1분 드롭 배포',
    badge: 'Live URL 배포',
    color: '#00C7B7',
    description: 'index.html 파일을 브라우저로 드래그 앤 드롭하면 즉시 전 세계 접속 가능한 URL 생성',
    pros: ['무료 글로벌 CDN 호스팅', '무료 HTTPS 보안 인증서', '커스텀 서브도메인 지원'],
    recommendedFor: '웹 제작 직후 1분 만에 라이브 배포 완료',
    icon: '🚀'
  },
  {
    name: 'Manus.ai',
    category: '자율 AI 에이전트',
    tag: 'General Agent',
    badge: '자율 브라우징 & 코딩',
    color: '#7C3AED',
    description: '목표 지시 한 번으로 기획-코딩-배포-검증을 스스로 완수하는 자율 실행 에이전트',
    pros: ['Sense-Plan-Act 피드백 루프', '자체 브라우저 환경에서 코딩/테스트', '완제품 레포트 및 사이트 생성'],
    recommendedFor: '바이브 코딩의 정석 및 복합 결과물 일괄 제작',
    icon: '🤖'
  },
  {
    name: 'Meta.ai & 대안 에이전트',
    category: '멀티 에이전트',
    tag: 'Multi-Agent Flow',
    badge: '도구 조합 시너지',
    color: '#0668E1',
    description: '아이디어 브레인스토밍부터 코드 블록 집중 생성까지 목적별 도구 다각화',
    pros: ['고속 Llama 3 기반 추론', '다양한 모델별 강점 활용', '환각 최소화 및 스티어링 훈련'],
    recommendedFor: 'AI 협업 감각 체화 및 교차 검증',
    icon: '🧭'
  }
]
