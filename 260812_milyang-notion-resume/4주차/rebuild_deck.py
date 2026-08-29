import re, os

html_path = r'c:\Users\IN\Desktop\꼬리치레\presentation.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Header: everything before <div class="deck-container" id="deckContainer"> + 1 line
header_end = content.find('<div class="deck-container" id="deckContainer">')
header = content[:header_end + len('<div class="deck-container" id="deckContainer">')]

# Footer: everything from <!-- UI Controls -->
footer_start = content.find('<!-- UI Controls -->')
footer = content[footer_start:]

# Extract slides by splitting on <div class="slide
raw_chunks = content[header_end:footer_start].split('<div class="slide')

slide_blocks = []
for chunk in raw_chunks:
    chunk = chunk.strip()
    if not chunk:
        continue
    # Re-attach <div class="slide
    if chunk.startswith('active'):
        full_slide = '<div class="slide ' + chunk
    else:
        full_slide = '<div class="slide' + chunk
    
    # Remove trailing </div> of deck-container if attached
    full_slide = re.sub(r'\s*</div>\s*$', '', full_slide)
    slide_blocks.append(full_slide)

print(f"Total raw slides found: {len(slide_blocks)}")

# Deduplicate slides by their unique title or header
unique_slides = []
seen_titles = set()

for s in slide_blocks:
    title_match = re.search(r'<h2>(.*?)</h2>', s, re.DOTALL)
    title = title_match.group(1).strip() if title_match else s[:80]
    if title not in seen_titles:
        seen_titles.add(title)
        unique_slides.append(s)

print(f"Unique slides count: {len(unique_slides)}")

# Locate Timetable slide and Video slide
video_slide = None
timetable_idx = -1

for idx, s in enumerate(unique_slides):
    if 'Notion이란?' in s or 'YOUTUBE VIDEO' in s:
        video_slide = s
    if '3시간(180분) 실습 타임테이블' in s:
        timetable_idx = idx

if video_slide and timetable_idx != -1:
    unique_slides = [s for s in unique_slides if s != video_slide]
    for idx, s in enumerate(unique_slides):
        if '3시간(180분) 실습 타임테이블' in s:
            timetable_idx = idx
            break
    # Insert video slide right after timetable slide (Slide 06)
    unique_slides.insert(timetable_idx + 1, video_slide)
    print(f"Placed Video Slide right after Timetable Slide (at Slide 6)!")

# Rebuild final presentation HTML with proper numbers
total_n = len(unique_slides)
rebuilt_slides = []

for idx, s in enumerate(unique_slides, start=1):
    # Set first slide active, others non-active
    if idx == 1:
        s = re.sub(r'<div class="slide[^"]*">', '<div class="slide active">', s, count=1)
    else:
        s = re.sub(r'<div class="slide[^"]*">', '<div class="slide">', s, count=1)
        
    # Update badge
    s = re.sub(r'<div class="slide-number-badge">\d+</div>', f'<div class="slide-number-badge">{idx:02d}</div>', s)
    # Update footer slide count
    s = re.sub(r'<span>Slide \d+ / \d+</span>', f'<span>Slide {idx} / {total_n}</span>', s)
    
    rebuilt_slides.append(s)

deck_body = "\n\n".join(rebuilt_slides)

# Update page indicator in footer
footer_clean = re.sub(r'<div class="page-indicator" id="pageIndicator">1 / \d+</div>', f'<div class="page-indicator" id="pageIndicator">1 / {total_n}</div>', footer)

final_html = header + "\n\n" + deck_body + "\n\n  </div>\n\n  " + footer_clean

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

try:
    os.remove('dedup_and_move.py')
except:
    pass

print(f"Successfully rebuilt presentation.html with {total_n} slides!")
