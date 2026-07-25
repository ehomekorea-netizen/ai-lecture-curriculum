path = r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 주석 중복 및 삽입 대상 위치 찾기
target_comment = '''            <!-- 3차시 마무리 카드 -->
            <!-- 3차시 마무리 카드 -->
            <!-- 3차시 마무리 카드 -->'''

replacement_block = '''            <!-- [3차시 정리 & 마무리] 내 비서 저장/활용 안내 및 전체 종합 질의응답 (4분 + Q&A 버퍼) -->
            <div class="page-block">
                <div class="page-block-header">
                    <h3>정리 &amp; 안내 : 내 비서 저장 및 내일부터 어떻게 쓸지 안내 &amp; 마무리 질의응답</h3>
                </div>

                <div class="two-column-layout">
                    <!-- 좌측: 내 비서 현장 활용 3단계 가이드 (4분) -->
                    <div class="left-col" style="flex: 1.1;">
                        <div class="instruction-box">
                            <h4><i class="fa-solid fa-mobile-screen-button" style="color:#0284c7;"></i> 📱 내일부터 양식장 현장에서 바로 쓰는 3단계</h4>
                            <p class="big-text">
                                오늘 완성한 나만의 AI 비서는 <strong>스마트폰 앱 및 PC 웹 브라우저</strong>에서 100% 동일하게 연동됩니다.
                            </p>

                            <div style="display:flex; flex-direction:column; gap:10px; margin-top:12px;">
                                <div style="background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:10px; padding:12px 14px;">
                                    <strong style="color:#0369a1; font-size:15px; display:flex; align-items:center; gap:6px;">
                                        <i class="fa-solid fa-download"></i> 1. 스마트폰 Gemini / ChatGPT 앱 실행
                                    </strong>
                                    <p style="font-size:13.5px; color:#334155; margin:4px 0 0 0;">
                                        동일한 구글 계정으로 로그인하면 좌측 메뉴에 방금 만든 <strong class="red-target">[완도 넙치 관제 비서]</strong>가 그대로 떠 있습니다.
                                    </p>
                                </div>

                                <div style="background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:10px; padding:12px 14px;">
                                    <strong style="color:#0369a1; font-size:15px; display:flex; align-items:center; gap:6px;">
                                        <i class="fa-solid fa-microphone"></i> 2. 현장에서 음성 또는 거친 키워드 입력
                                    </strong>
                                    <p style="font-size:13.5px; color:#334155; margin:4px 0 0 0;">
                                        "A-02 수조 오늘 28.5도 산소 4.0 사료 0 폐사 15" 라고 말하거나 텍스트로 찍어 전송합니다.
                                    </p>
                                </div>

                                <div style="background:#f0f9ff; border:1.5px solid #bae6fd; border-radius:10px; padding:12px 14px;">
                                    <strong style="color:#0369a1; font-size:15px; display:flex; align-items:center; gap:6px;">
                                        <i class="fa-solid fa-clipboard-check"></i> 3. 3초 만에 관제표 + 현장 응급 처방 수령
                                    </strong>
                                    <p style="font-size:13.5px; color:#334155; margin:4px 0 0 0;">
                                        AI가 <strong class="red-target">한글 관제 표</strong>와 함께 국립수산과학원 매뉴얼 기준 <strong class="red-target">[절식·산소가동 3줄 처방]</strong>을 즉시 답변합니다.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 우측: 1~3차시 교육 전체 총복습 & 마무리 Q&A 버퍼 (11:50~12:00) -->
                    <div class="right-col" style="flex: 1.1;">
                        <div class="ui-sim-card" style="box-shadow:0 6px 20px rgba(0,0,0,0.1);">
                            <div class="sim-header" style="background:#0f172a; padding:12px 16px;">
                                <span class="sim-title" style="font-size:15px; font-weight:800;"><i class="fa-solid fa-clock-rotate-left" style="color:#38bdf8;"></i> ⏰ 11:50 ~ 12:00 종합 마무리 &amp; 질의응답 (Q&amp;A)</span>
                            </div>
                            <div class="sim-body" style="padding:16px; background:#ffffff;">
                                <div style="background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:10px; padding:14px; margin-bottom:12px;">
                                    <h4 style="color:#0f172a; font-size:15px; font-weight:800; margin-bottom:8px; display:flex; align-items:center; gap:6px;">
                                        <i class="fa-solid fa-graduation-cap" style="color:#0284c7;"></i> 오늘 교육 과정 3대 핵심 요약
                                    </h4>
                                    <ul style="margin:0; padding-left:18px; font-size:13.5px; color:#334155; line-height:1.6;">
                                        <li><strong>1차시:</strong> 포털 검색 대신 <strong class="red-target">3원칙 프롬프트</strong>로 3초 현장 관제표 완성</li>
                                        <li><strong>2차시:</strong> 폐사 수치에 혹하지 않고 <strong class="red-target">사전 위험 신호(수온·DO)</strong> 캐묻기</li>
                                        <li><strong>3차시:</strong> 내 양식장 전담 <strong class="red-target">Gems 맞춤 비서</strong> 구축 및 공유</li>
                                    </ul>
                                </div>

                                <div style="background:#f0fdf4; border:1.5px solid #86efac; border-radius:10px; padding:14px; color:#14532d; font-size:13.5px; line-height:1.55;">
                                    💬 <strong>현장 질의응답 &amp; 진행 지연 버퍼 (10분):</strong><br>
                                    실습 중 궁금했던 점, 스마트폰 연동 장애, 내 양식장 지침 적용 팁 등 자유로운 Q&amp;A 진행 (진행 지연 시 유연한 버퍼 시간으로 활용)
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="brand-footer-line">
                    [3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사
                </div>
            </div>

            <!-- 3차시 마무리 카드 -->'''

if target_comment in content:
    content = content.replace(target_comment, replacement_block)
    print("Successfully replaced repeated comments and inserted Section 6 & 7 summary block!")
else:
    print("Could not find exact comment string, searching fallback location...")
    pos = content.find('<div class="page-block summary-block">\n                <div class="page-block-header">\n                    <h3><i class="fa-solid fa-quote-left"></i> 3차시 핵심 한 줄 정리</h3>')
    if pos != -1:
        # pos 직전 주석들 정리 후 삽입
        lines_before = content[:pos].rstrip()
        # 중복 주석 제거
        while lines_before.endswith('<!-- 3차시 마무리 카드 -->'):
            lines_before = lines_before[:-len('<!-- 3차시 마무리 카드 -->')].rstrip()
        content = lines_before + '\n\n' + replacement_block + '\n' + content[pos:]
        print("Fallback replacement successful!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("File update finished.")
