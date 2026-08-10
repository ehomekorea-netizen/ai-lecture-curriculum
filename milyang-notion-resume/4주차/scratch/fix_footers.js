const fs = require('fs');
let html = fs.readFileSync('presentation.html', 'utf8');

// Replace all legacy <span>Slide XX / 60</span> or <span>Slide XX / 63</span> with dynamic badge class
html = html.replace(/<span>Slide \d+ \/ \d+<\/span>/g, '<span class="slide-dynamic-badge"></span>');

fs.writeFileSync('presentation.html', html, 'utf8');
console.log('✅ 모든 슬라이드 푸터의 하드코딩 Slide XX / XX 표시를 slide-dynamic-badge 로 일괄 전환 완료!');
