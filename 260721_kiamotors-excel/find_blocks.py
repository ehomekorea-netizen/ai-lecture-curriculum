path = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 현재 라인 찾기 (0-indexed)
def find_block(lines, start_hint, end_hint, search_from=0):
    """summary-block 시작 라인과 끝 라인을 찾기"""
    start = None
    for i in range(search_from, len(lines)):
        if 'page-block summary-block' in lines[i]:
            start = i
            break
    if start is None:
        return None, None
    # 블록 끝 찾기 (</div>\n 이후 </section> 또는 다음 <!-- 이전)
    end = None
    depth = 0
    for i in range(start, len(lines)):
        if '<div' in lines[i] and not '/div' in lines[i]:
            depth += lines[i].count('<div') - lines[i].count('</div')
        elif '</div>' in lines[i]:
            depth -= lines[i].count('</div>') - lines[i].count('<div')
        if depth <= 0 and i > start:
            end = i
            break
    return start, end

# 1차시 마무리 블록 (첫 번째 summary-block)
s1_start, s1_end = find_block(lines, 0, 0, search_from=0)
print(f"1차시 summary-block: lines {s1_start+1}~{s1_end+1}")
for i in range(s1_start, s1_end+1):
    print(f"  {i+1}: {lines[i]}", end='')
