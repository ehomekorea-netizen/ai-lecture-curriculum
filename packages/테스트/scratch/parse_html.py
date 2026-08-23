import re
import html as html_module
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\IN\Desktop\slidev-agent-studio\packages\테스트\ref\3-4차시\work-skill-plugin-map-preview.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Extract inner HTML if srcdoc
idx = raw.find('srcdoc="')
if idx != -1:
    end_idx = raw.rfind('">')
    inner = html_module.unescape(raw[idx+8:end_idx])
    # Extract visible strings
    cleaned = re.sub(r'<style.*?</style>', '', inner, flags=re.DOTALL)
    cleaned = re.sub(r'<script.*?</script>', '', cleaned, flags=re.DOTALL)
    cleaned = re.sub(r'<[^>]+>', '\n', cleaned)
    lines = [l.strip() for l in cleaned.splitlines() if l.strip()]
    print('\n'.join(lines[:80]))
else:
    print('No srcdoc found')
