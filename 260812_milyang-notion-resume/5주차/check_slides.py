import re

with open('presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Only count slide container divs
slides = re.findall(r'<div class="slide[\s"]', content)
print(f"Exact Slide Container count: {len(slides)}")
