const fs = require('fs');
const path = 'c:/Users/IN/Desktop/밀양 디지털실무/4주차/presentation.html';
const content = fs.readFileSync(path, 'utf8');

// Match all <div class="slide"...> blocks and check their internal balance
const slideRegex = /<div\s+class=["']slide[^"']*["'][\s\S]*?<\/div>\s*<\/div>/g;
// Let's do a strict parse of all slides
const slides = content.split(/<div\s+class=["']slide/i);

console.log(`Total slide blocks found: ${slides.length - 1}`);

for (let i = 1; i < slides.length; i++) {
  const slideChunk = '<div class="slide' + slides[i];
  // extract up to the closing of this slide or next slide start
  const open = (slideChunk.match(/<div[\s>]/gi) || []).length;
  const close = (slideChunk.match(/<\/div>/gi) || []).length;
  if (open !== close) {
    // find slide ID or title for easy identification
    const idMatch = slideChunk.match(/id=["']([^"']+)["']/);
    const titleMatch = slideChunk.match(/<h[12][^>]*>([\s\S]*?)<\/h[12]>/i);
    console.log(`Slide #${i} (ID: ${idMatch ? idMatch[1] : 'none'}) is UNBALANCED: Open=${open}, Close=${close}`);
    console.log(`Title: ${titleMatch ? titleMatch[1].replace(/\s+/g, ' ').trim() : 'Unknown'}`);
  }
}
