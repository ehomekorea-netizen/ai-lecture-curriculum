import re

with open('presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

headers = re.findall(r'<h2>(.*?)</h2>', content)
for i, h in enumerate(headers):
    print(f"Slide {i+1:02d}: {h}")
