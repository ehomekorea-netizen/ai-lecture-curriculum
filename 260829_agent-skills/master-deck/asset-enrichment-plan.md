---
kind: slidev-asset-enrichment-plan
schema_version: 3
status: enrichment-ready
workflow_stage: static-enrichment
mode: research
source_deck: slides.md
deck_brief: ../course-brief.md
draft_approval: user-approved
language: ko
aspect_ratio: 16:9
asset_state: ideas-only
next_stage: user-select-and-materialize
output_root: .
---

# Asset Enrichment Plan: AI 에이전트 마스터코스 (통합 28 슬라이드 Master Deck)

## 1. Handoff summary

`master-deck/slides.md` **총 28개 슬라이드 (1차시 14슬라이드 + 2차시 14슬라이드)** 전체에 대해, **Anthropic/OpenAI 공식 문서, YouTube 튜토리얼 타임코드, 비개발 직무별 실물 산출물 Before/After, 파이썬 연산 도구 실행 캡처, 아키텍처 다이어그램 SVG 등 정밀 리서치 데이터**를 하나로 통합했습니다.

- **시각적 승인 보드:** [`asset-review.html`](./asset-review.html) (28 슬라이드 통합 보드)
- **통합 슬라이드 소스:** [`slides.md`](./slides.md) (1차시 + 2차시 무결점 통합 빌드 통과)

---

## 2. 1차시 & 2차시 통합 에셋 맵

- **1차시 (S01 ~ S14):** SKILL 기초 개념, 점진적 로딩(100토큰), SKILL.md 구조 해부, polishing-emails 실습, 피날레 아키텍처 다이어그램(`agent-skills-architecture.png`)
- **2차시 (S15 ~ S28):** Antigravity & GPTwork 실무 런타임, references/ 20페이지 지식 분리, scripts/ 파이썬 도구 연동, 직무별(기획·마케팅·영업·CS·인사·운영) 실물 사례, 4대 디버깅 매트릭스, 4대 엔터프라이즈 로드맵

---

## 3. Static completion gate

- [x] 1차시 14개 + 2차시 14개 = 총 28개 슬라이드 전체 병합 및 빌드 통과 (`✓ built in 9.17s`)
- [x] 모든 슬라이드에 풍부한 멀티미디어 / 정적 연출 Preferred + Alternative 제안 매핑 완료
- [x] 단독 실행 `asset-review.html` 보드 연동 완료
