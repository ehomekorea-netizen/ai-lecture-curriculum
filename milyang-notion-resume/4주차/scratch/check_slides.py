import re

with open('c:/Users/IN/Desktop/밀양 디지털실무/4주차/presentation.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split by slide start
slides_raw = re.split(r'(<div\s+(?:[^>]*?\s+)?class=["\']slide(?:\s+[^"\']*)?["\'])', html, flags=re.IGNORECASE)

print(f"Total parts: {len(slides_raw)}")
# slides_raw[0] is header/css
# odd indices are the `<div class="slide..."` tags, even indices are the contents up to next slide

slide_num = 0
for i in range(1, len(slides_raw), 2):
    slide_num += 1
    tag = slides_raw[i]
    body = slides_raw[i+1]
    
    # We want to check how many <div> are inside this slide.
    # The slide starts with 1 open div (the tag itself).
    # To find where the slide ends, we track depth.
    depth = 1
    tokens = re.findall(r'</?div[\s>]', body, flags=re.IGNORECASE)
    for tok in tokens:
        if tok.lower().startswith('</div'):
            depth -= 1
        else:
            depth += 1
        if depth == 0:
            break
    
    if depth != 0:
        # Title extraction
        t_match = re.search(r'<h[12][^>]*>(.*?)</h[12]>', body, re.DOTALL | re.IGNORECASE)
        title = t_match.group(1).strip() if t_match else "No Title"
        print(f"❌ Slide #{slide_num} (Line around start) UNBALANCED! Depth remaining: {depth}, Title: {title[:40]}")
