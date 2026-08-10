import os

html_path = r'c:\Users\IN\Desktop\꼬리치레\presentation.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix HTML input tags in Slide 12 to match correct function names
content = content.replace('oninput="doBulletInstant(this)" onkeyup="doBulletInstant(this)"', 'oninput="handleBulletInline()" onkeyup="handleBulletInline()"')
content = content.replace('oninput="doTodoInstant(this)" onkeyup="doTodoInstant(this)"', 'oninput="handleTodoInline()" onkeyup="handleTodoInline()"')

# 2. Re-write the Slide 12 JS functions entirely to ensure 100% Instant Transform Behavior
old_js_start_marker = "// --- SLIDE 12"
idx_start = content.find(old_js_start_marker)

if idx_start != -1:
    idx_end = content.find("</script>", idx_start)
    if idx_end != -1:
        perfect_js = """// --- SLIDE 12 100% INSTANT INLINE TRANSFORM FUNCTIONS ---
    function handleBulletInline() {
      try {
        const input = document.getElementById('bulletInputText');
        const display = document.getElementById('bulletTransformedBlock');
        const textSpan = document.getElementById('bulletTransformedText');
        if (!input || !display || !textSpan) return;

        let val = input.value;
        // 빈칸 1개라도 치거나, '-' 가 들어가면 100% 무조건 발동
        if (val.includes('-') || val.length > 0) {
          let clean = val.replace(/^-[\s]*/, '').trim();
          if (!clean || clean.length === 0) clean = "01. 카페 아르바이트 (고객 응대)";
          textSpan.innerText = clean;
          
          input.style.display = 'none'; // 인풋 박스는 숨기고
          display.style.display = 'flex'; // 완성된 불릿 카드를 짠! 보여줌
        }
      } catch (e) { console.log(e); }
    }

    function handleTodoInline() {
      try {
        const input = document.getElementById('todoInputText');
        const display = document.getElementById('todoTransformedBlock');
        const textSpan = document.getElementById('todoTransformedText');
        if (!input || !display || !textSpan) return;

        let val = input.value;
        // 빈칸 1개라도 치거나, '[]' 관련 문자 치면 100% 무조건 발동
        if (val.includes('[') || val.includes(']') || val.length > 0) {
          let clean = val.replace(/^\[\][\s]*/, '').replace(/^\[[\s]*/, '').trim();
          if (!clean || clean.length === 0) clean = "01. 개인 이력 메인 페이지 생성";
          textSpan.innerText = clean;
          textSpan.style.textDecoration = 'none';
          textSpan.style.color = '#fff';
          
          input.style.display = 'none'; // 인풋 박스는 숨기고
          display.style.display = 'flex'; // 완성된 미완료 체크박스 카드를 짠! 보여줌
        }
      } catch (e) { console.log(e); }
    }

    function toggleTodoState(icon) {
      try {
        icon.classList.toggle('checked');
        const tText = document.getElementById('todoTransformedText');
        const badge = document.getElementById('todoStateBadge');
        // 체크박스 클릭 시 스타일 토글
        if (icon.classList.contains('checked')) {
          if (tText) {
            tText.style.textDecoration = 'line-through';
            tText.style.color = 'var(--text-sub)';
          }
          if (badge) {
            badge.innerText = '☑ 완수 완료!';
            badge.style.background = 'rgba(16,185,129,0.3)';
            badge.style.color = 'var(--emerald)';
          }
        } else {
          if (tText) {
            tText.style.textDecoration = 'none';
            tText.style.color = '#fff';
          }
          if (badge) {
            badge.innerText = '☐ 미완료 (클릭 시 체크)';
            badge.style.background = 'rgba(245,158,11,0.25)';
            badge.style.color = 'var(--amber)';
          }
        }
      } catch (e) { console.log(e); }
    }
"""
        content = content[:idx_start] + perfect_js + content[idx_end:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Slide 12 HTML input tags and JS functions perfectly aligned and fixed!")
