path = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_s1 = '''            <!-- 1차시 마무리 카드 -->
            <div class="page-block summary-block">
                <div class="page-block-header">
                    <h3><i class="fa-solid fa-quote-left"></i> 1차시 핵심 한 줄 정리</h3>
                </div>
                <div class="summary-card-box" style="padding:24px; background:linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border:2.5px solid #4ade80; border-radius:16px; box-shadow:0 6px 20px rgba(22, 101, 52, 0.12);">
                    <div style="text-align:center; margin-bottom:14px;">
                        <span style="display:inline-block; background:linear-gradient(90deg, #15803d, #16a34a); color:#fff; font-size:14px; font-weight:900; padding:5px 18px; border-radius:20px; letter-spacing:0.5px;">
                            ★ 1차시 핵심 정수 (Key Insight)
                        </span>
                    </div>
                    <p style="color:#14532d; font-size:22px; text-align:center; font-weight:900; margin:0 0 18px 0; line-height:1.55;">
                        "포털 검색에 더 이상 시간을 빼앗기지 말고!<br>
                        AI에게 <strong class="red-target">3원칙([역할]+[맥락]+[형식])</strong>으로 제대로 물어<br>
                        <strong class="red-target">3초 현장 관제표</strong>를 완성합니다!"
                    </p>
                    <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:4px;">
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">🔑 포털 검색 시간 단축</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">🎯 3원칙 프롬프트 설계</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#15803d; border:1.5px solid #15803d; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#ffffff; white-space:nowrap;">⚡ 3초 현장 맞춤 관제표</span>
                    </div>
                </div>
                <div class="brand-footer-line">
                    [1차시] AI 리터러시 - 골라 쓰고, 제대로 묻기 | 오진실 강사
                </div>
            </div>
'''

new_s2 = '''            <!-- 2차시 마무리 카드 -->
            <div class="page-block summary-block">
                <div class="page-block-header">
                    <h3><i class="fa-solid fa-quote-left"></i> 2차시 핵심 한 줄 정리</h3>
                </div>
                <div class="summary-card-box" style="padding:24px; background:linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border:2.5px solid #4ade80; border-radius:16px; box-shadow:0 6px 20px rgba(22, 101, 52, 0.12);">
                    <div style="text-align:center; margin-bottom:14px;">
                        <span style="display:inline-block; background:linear-gradient(90deg, #15803d, #16a34a); color:#fff; font-size:14px; font-weight:900; padding:5px 18px; border-radius:20px; letter-spacing:0.5px;">
                            ★ 2차시 핵심 정수 (Key Insight)
                        </span>
                    </div>
                    <p style="color:#14532d; font-size:22px; text-align:center; font-weight:900; margin:0 0 18px 0; line-height:1.55;">
                        "아무리 AI가 데이터로 위험과 원인을 훌륭히 추론해 줄지라도,<br>
                        최종 완성은 어민의 <strong class="red-target">30년 현장 경험</strong>과 <strong class="red-target">도메인 데이터</strong>가<br>
                        협력해서 검증할 때 비로소 완성됩니다!"
                    </p>
                    <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:4px;">
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">🧠 AI 데이터 패턴 추론</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">🌿 어민 현장 노하우 검증</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#15803d; border:1.5px solid #15803d; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#ffffff; white-space:nowrap;">🏆 완벽한 스마트양식 관제</span>
                    </div>
                </div>
                <div class="brand-footer-line">
                    [2차시] 데이터 깊이 읽기 - 한 번 묻고 끝내지 않는다 | 오진실 강사
                </div>
            </div>
'''

new_s3 = '''            <!-- 3차시 마무리 카드 -->
            <div class="page-block summary-block">
                <div class="page-block-header">
                    <h3><i class="fa-solid fa-quote-left"></i> 3차시 핵심 한 줄 정리</h3>
                </div>
                <div class="summary-card-box" style="padding:24px; background:linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border:2.5px solid #4ade80; border-radius:16px; box-shadow:0 6px 20px rgba(22, 101, 52, 0.12);">
                    <div style="text-align:center; margin-bottom:14px;">
                        <span style="display:inline-block; background:linear-gradient(90deg, #15803d, #16a34a); color:#fff; font-size:14px; font-weight:900; padding:5px 18px; border-radius:20px; letter-spacing:0.5px;">
                            ★ 3차시 핵심 정수 (Key Insight)
                        </span>
                    </div>
                    <p style="color:#14532d; font-size:22px; text-align:center; font-weight:900; margin:0 0 18px 0; line-height:1.55;">
                        "매번 길게 설명할 필요 없이!<br>
                        내 양식장의 수조·어종 특성을 기억하는 <strong class="red-target">어민 전담 AI 비서</strong>로<br>
                        <strong class="red-target">수질 경보부터 일지까지 자동화</strong>합니다!"
                    </p>
                    <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; margin-top:4px;">
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">⚙️ 어민 맞춤 지침 등록</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#ffffff; border:1.5px solid #4ade80; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#14532d; white-space:nowrap;">🧠 전용 AI 맞춤 비서 구축</span>
                        <span style="color:#15803d; font-size:22px; font-weight:900;">→</span>
                        <span style="background:#15803d; border:1.5px solid #15803d; border-radius:10px; padding:8px 14px; font-size:14px; font-weight:800; color:#ffffff; white-space:nowrap;">🚀 스마트 양식장 칼퇴근 완수</span>
                    </div>
                </div>
                <div class="brand-footer-line">
                    [3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사
                </div>
            </div>
'''

positions = []
for i, line in enumerate(lines):
    if 'page-block summary-block' in line:
        positions.append(i)

def find_block_end(lines, start):
    count = 0
    for i in range(start, len(lines)):
        count += lines[i].count('<div') - lines[i].count('</div>')
        if count <= 0 and i > start:
            return i
    return start + 15

new_blocks = [new_s1, new_s2, new_s3]
for idx in reversed(range(len(positions))):
    start = positions[idx]
    end = find_block_end(lines, start)
    new_block_lines = new_blocks[idx].splitlines(keepends=True)
    lines = lines[:start] + new_block_lines + lines[end+1:]

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Updated summary blocks successfully!")
