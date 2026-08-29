banner = """
                <!-- 💡 [검증 통합 배너] 어민이 꼭 기억해야 할 엑셀 데이터 3단계 판독 기준 -->
                <div style="margin-top:20px; background:linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border:2px solid #38bdf8; border-radius:14px; padding:18px 22px; box-shadow:0 6px 16px rgba(3,105,161,0.08);">
                    <h4 style="color:#0369a1; font-size:18px; font-weight:900; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
                        <i class="fa-solid fa-lightbulb" style="color:#0284c7; font-size:22px;"></i> 💡 현장에서 꼭 기억해야 할 엑셀 관제 데이터 3단계 판독 기준
                    </h4>

                    <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:12px;">
                        <!-- 1. 사전 위험 신호 -->
                        <div style="background:#ffffff; border:1.5px solid #38bdf8; border-radius:10px; padding:12px 14px;">
                            <span style="background:#0284c7; color:#fff; font-size:12px; font-weight:800; padding:2px 8px; border-radius:10px; display:inline-block; margin-bottom:6px;">1단계: 원인 경보</span>
                            <strong style="display:block; color:#0369a1; font-size:16px; margin-bottom:4px;">🌊 사전 위험 신호 (Pre)</strong>
                            <p style="font-size:13.5px; color:#334155; margin:0; line-height:1.45;">
                                <strong>수온 28.2℃↑ &amp; DO 4.1mg/L↓</strong><br>
                                어류가 숨 막혀 죽기 전 물이 미리 알려주는 골든타임 경고 신호
                            </p>
                        </div>
                        <!-- 2. 결과 신호 -->
                        <div style="background:#ffffff; border:1.5px solid #fecdd3; border-radius:10px; padding:12px 14px;">
                            <span style="background:#e11d48; color:#fff; font-size:12px; font-weight:800; padding:2px 8px; border-radius:10px; display:inline-block; margin-bottom:6px;">2단계: 어체 피해</span>
                            <strong style="display:block; color:#9f1239; font-size:16px; margin-bottom:4px;">🐟 결과 신호 (Post)</strong>
                            <p style="font-size:13.5px; color:#334155; margin:0; line-height:1.45;">
                                <strong>신규 폐사 12마리 발생</strong><br>
                                이미 발생한 어체 피해 결과일 뿐 원인이 아니므로 숫자에 매몰되지 말 것
                            </p>
                        </div>
                        <!-- 3. 현장 응급 조치 -->
                        <div style="background:#ffffff; border:1.5px solid #86efac; border-radius:10px; padding:12px 14px;">
                            <span style="background:#15803d; color:#fff; font-size:12px; font-weight:800; padding:2px 8px; border-radius:10px; display:inline-block; margin-bottom:6px;">3단계: 어민 대응</span>
                            <strong style="display:block; color:#14532d; font-size:16px; margin-bottom:4px;">⚙️ 현장 응급 조치 (Action)</strong>
                            <p style="font-size:13.5px; color:#334155; margin:0; line-height:1.45;">
                                <strong>사료 전면 절식 + 산소 가동</strong><br>
                                고수온에 사료로 죽이지 않고 숨 쉬게 살려내는 필수 응급 대응 행동
                            </p>
                        </div>
                    </div>
                </div>
"""

path = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 라인 914 (0-indexed: 913) = '                </div>\n'  이후 빈줄(914)
# 라인 916 (0-indexed: 915) = '                <div class="brand-footer-line">\n'
# 배너를 915번 줄 앞에 삽입 (0-indexed: 914 위치 = 빈줄 이후)
insert_at = 915  # 0-indexed: brand-footer-line 이전 빈줄 다음에 삽입

lines.insert(insert_at, banner)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Banner inserted at line", insert_at + 1, "successfully!")
