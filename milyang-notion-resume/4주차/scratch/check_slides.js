const fs = require('fs');
const html = fs.readFileSync('presentation.html', 'utf8');

const matches = html.match(/<div class="slide["\s]/g);
console.log('✅ 탑레벨 .slide 디브 수:', matches ? matches.length : 0);

// 슬라이드 46~48 구간의 하드코딩 푸터 텍스트 확인
const lines = html.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('Slide ') && line.includes('/ 60')) {
    console.log(`L${idx + 1}: ${line.trim()}`);
  }
});
