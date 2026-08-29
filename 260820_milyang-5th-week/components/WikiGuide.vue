<template>
  <div class="wiki-guide-box">
    <h2>🛠️ 새로운 컴포넌트 발견 시 3초 만에 위키에 추가하는 방법</h2>
    
    <div class="steps-grid">
      <div class="step-card">
        <div class="step-num">Step 1</div>
        <h3>.vue 파일 복사</h3>
        <p>새로 발견한 컴포넌트 파일(예: <code>MyNewEffect.vue</code>)을 <code>components/</code> 폴더에 쏙 복사해 넣습니다.</p>
      </div>

      <div class="step-card">
        <div class="step-num">Step 2</div>
        <h3>wikiData.ts 메타데이터 등록</h3>
        <p><code>wikiData.ts</code> 파일의 배열 맨 아래에 신규 컴포넌트 정보(이름, 연출 효과, 용도, 마크다운 태그)를 1줄 추가합니다.</p>
      </div>

      <div class="step-card">
        <div class="step-num">Step 3</div>
        <h3>실시간 4x4 타일 갱신 완료!</h3>
        <p>브라우저로 돌아오면 4x4 도감 타일에 새 컴포넌트 정보와 태그가 즉시 짠 하고 자동 갱신됩니다!</p>
      </div>
    </div>

    <div class="code-example mt-4">
      <div class="code-title">📄 <code>wikiData.ts</code> 등록 코드 예시:</div>
      <pre><code>{
  id: 17,
  title: '새로운 3D 차트 컴포넌트',
  category: '시각화',
  effect: '마우스 호버 시 3D 회전하는 파이 차트',
  useCase: '매출 성과 및 비율 시각화',
  tag: '&lt;MyNewChart :data="[10, 20, 30]" /&gt;',
  icon: '📊',
  componentName: 'MyNewChart'
}</code></pre>
    </div>
  </div>
</template>

<style scoped>
.wiki-guide-box {
  background: #ffffff;
  border: 1px solid #E7E0D4;
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}
.wiki-guide-box h2 {
  font-family: 'Source Serif 4', serif;
  font-size: 1.4rem;
  color: #2B2620;
  margin-bottom: 1.2rem;
}
.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
.step-card {
  background: #FAF8F4;
  border: 1px solid #EAE3D9;
  border-radius: 10px;
  padding: 1rem;
}
.step-num {
  display: inline-block;
  background: #476BFF;
  color: white;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 12px;
  margin-bottom: 0.5rem;
}
.step-card h3 {
  font-size: 1rem;
  font-weight: 700;
  color: #2B2620;
  margin-bottom: 0.4rem;
}
.step-card p {
  font-size: 0.82rem;
  color: #666;
  line-height: 1.4;
}
.code-example {
  background: #2B2620;
  color: #53DFA9;
  padding: 0.8rem 1rem;
  border-radius: 8px;
  font-family: 'Geist Mono', monospace;
  font-size: 0.78rem;
}
.code-title {
  color: #FAF8F4;
  font-weight: 700;
  margin-bottom: 0.3rem;
}
</style>
