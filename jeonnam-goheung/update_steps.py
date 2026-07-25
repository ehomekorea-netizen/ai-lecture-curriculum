with open(r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html', 'rb') as f:
    content_bytes = f.read()

# utf-8 ignore 혹은 latin1 디코딩 후 변환
content = content_bytes.decode('utf-8', errors='ignore')

pos_step3 = content.find('Step 3 :')
pos_step3_footer = content.find('[3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사', pos_step3)
pos_step3_div1 = content.find('</div>', pos_step3_footer)
pos_step3_block_end = content.find('</div>', pos_step3_div1 + 6) + 6

pos_old_order = content.find('<!-- 순서 1 & 2')

new_blocks = """
            <!-- [Step 4] 시스템 지침(Instructions) 설계 4대 축 & 완성형 템플릿 입력 (단독 독립 블록) -->
            <div class="page-block">
                <div class="page-block-header">
                    <h3>Step 4 : ★ 시스템 지침(System Instructions) 설계 4대 축 & 템플릿 입력하기</h3>
                </div>

                <div class="two-column-layout">
                    <!-- 좌측: 지시사항 4대 축 & 템플릿 복사 -->
                    <div class="left-col" style="flex: 1.1;">
                        <div class="instruction-box">
                            <h4><i class="fa-solid fa-cubes" style="color:#0284c7;"></i> 지시사항(Instructions) 잘 작성하기 4대 핵심 축</h4>
                            <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:8px;">
                                <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:10px;">
                                    <strong style="color:#0369a1; font-size:15px;">1. 페르소나 (Persona)</strong>
                                    <p style="font-size:13px; color:#334155; margin:2px 0 0 0;">30년 경력 스마트양식 수질 전문가 및 일지 관리자 지위 부여</p>
                                </div>
                                <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:10px;">
                                    <strong style="color:#0369a1; font-size:15px;">2. 작업 (Task)</strong>
                                    <p style="font-size:13px; color:#334155; margin:2px 0 0 0;">수치 입력 시 관제 표 정리 및 고수온 응급 조치 처방 수행</p>
                                </div>
                                <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:10px;">
                                    <strong style="color:#0369a1; font-size:15px;">3. 관련 정보 (Context)</strong>
                                    <p style="font-size:13px; color:#334155; margin:2px 0 0 0;">고수온 특보(28.2℃↑), DO(4.1mg/L↓) 시 사료 절식/산소 가동 수칙</p>
                                </div>
                                <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:8px; padding:10px;">
                                    <strong style="color:#0369a1; font-size:15px;">4. 형식 (Format)</strong>
                                    <p style="font-size:13px; color:#334155; margin:2px 0 0 0;">엑셀형 한글 표 + 현장 실행 3대 체크리스트 고정 출력</p>
                                </div>
                            </div>

                            <!-- 템플릿 복사 박스 -->
                            <div class="prompt-copy-widget" style="margin-top:14px;">
                                <div class="widget-head">
                                    <span class="w-label"><i class="fa-solid fa-scroll"></i> 어민 전담 Gems 지시사항 완성형 템플릿</span>
                                    <button class="copy-btn" data-copy="[Gems 수산 관제 비서 시스템 지침서]
- 역할: 너는 30년 경력 전남 완도 넙치 육상양식장 전담 '일지 정리 및 수질 안전 비서 Gems'야.
- 임무: 어민이 거칠게 입력한 수온, 용존산소, 사료량, 폐사 수 키워드를 읽고 스마트양식 한글 관제 표 보고서를 즉시 작성해 줘.
- 현장 응급 조치 처방: 수온 28도 이상 또는 용존산소 4.5 이하 감지 시 어민이 당장 실행할 3단계 활동 수칙(사료 전면 절식, 액성산소 100% 가동, 취수량 150% 증대)을 처방해 줘.
- 작성 스타일: 어조는 어민 어르신께 친근하고 정중하며 객관적인 문체(~하심. ~을 필요로 함)로 서술해 줘.
- 출력 고정: 답변의 맨 마지막 줄에는 현장 점검용 [어민 현장 조치 3줄 요약] 단락을 반드시 고정 출력해 줘.">
                                        <i class="fa-regular fa-copy"></i> 지침 템플릿 복사
                                    </button>
                                </div>
                                <div class="widget-body" style="font-size:14.5px; line-height:1.5;">
[Gems 수산 관제 비서 시스템 지침서]<br>
- 역할: 너는 30년 경력 전남 완도 넙치 육상양식장 전담 '일지 정리 및 수질 안전 비서 Gems'야.<br>
- 임무: 어민이 거칠게 입력한 수온, 용존산소, 사료량, 폐사 수 키워드를 읽고 스마트양식 한글 관제 표 보고서를 즉시 작성해 줘.<br>
- 현장 응급 조치 처방: 수온 28도 이상 또는 용존산소 4.5 이하 감지 시 어민이 당장 실행할 3단계 활동 수칙(사료 전면 절식, 액성산소 100% 가동, 취수량 150% 증대)을 처방해 줘.<br>
- 작성 스타일: 어조는 어민 어르신께 친근하고 정중하며 객관적인 문체(~하심. ~을 필요로 함)로 서술해 줘.<br>
- 출력 고정: 답변의 맨 마지막 줄에는 현장 점검용 [어민 현장 조치 3줄 요약] 단락을 반드시 고정 출력해 줘.
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 우측: 전달받은 요청 사항(Instructions) 실물 캡처 이미지 -->
                    <div class="right-col" style="flex: 1.1;">
                        <div class="ui-sim-card" style="box-shadow:0 6px 20px rgba(0,0,0,0.1);">
                            <div class="sim-header" style="background:#0f172a; padding:12px 16px;">
                                <span class="sim-title" style="font-size:15px; font-weight:800;"><i class="fa-solid fa-image" style="color:#38bdf8;"></i> Step 4: [요청 사항 (Instructions)] 입력 상자 파란 박스 가이드</span>
                            </div>
                            <div class="sim-body center-img-body" style="padding:8px; background:#ffffff;">
                                <img src="images/step4_instructions.png" alt="요청 사항 입력 상자 캡처 이미지" class="expand-fill-img" style="border-radius:8px;">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="brand-footer-line">
                    [3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사
                </div>
            </div>

            <!-- [Step 5] Gems에 현장 양식 매뉴얼 지식(Knowledge) 파일 탑재 (단독 독립 블록) -->
            <div class="page-block">
                <div class="page-block-header">
                    <h3>Step 5 : ★ Gems에 현장 양식 매뉴얼 지식(Knowledge) 파일 탑재하기</h3>
                </div>

                <div class="two-column-layout">
                    <!-- 좌측: 지식 추가 조작 설명 및 실물 PDF 다운로드 -->
                    <div class="left-col" style="flex: 1;">
                        <div class="instruction-box">
                            <h4><i class="fa-solid fa-file-pdf" style="color:#f43f5e;"></i> 국립수산과학원 표준 매뉴얼 지식 이식하기</h4>
                            <p class="big-text">
                                AI 비서가 단순 작문기가 아닌, <strong>국립수산과학원 표준 매뉴얼에 입각해 전문 조치</strong>를 내리도록 근거 자료를 이식합니다.
                            </p>

                            <!-- 실물 PDF 다운로드 박스 -->
                            <div style="background:#fff1f2; border:2px solid #fda4af; border-radius:12px; padding:14px; margin-top:10px; box-shadow:0 3px 10px rgba(225,29,72,0.08);">
                                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:6px;">
                                    <span style="color:#9f1239; font-size:15px; font-weight:800; display:flex; align-items:center; gap:6px;">
                                        <i class="fa-solid fa-file-pdf" style="color:#e11d48; font-size:18px;"></i> 실습용 표준 지식 문서 준비
                                    </span>
                                    <button class="copy-btn download-pdf-btn" style="background:#e11d48; font-size:13.5px; padding:6px 14px; font-weight:800;">
                                        <i class="fa-solid fa-file-pdf"></i> 📄 NIFS 표준 수질관리 매뉴얼(.pdf) 다운로드
                                    </button>
                                </div>
                                <p class="big-text" style="color:#881337; font-size:13.5px; margin:0; line-height:1.4; font-weight:700;">
                                    <i class="fa-solid fa-paperclip red-target"></i> 버튼을 눌러 저장한 문서를 Gems 지식<strong class="red-target">[+]</strong> 버튼으로 업로드해 보세요!
                                </p>
                            </div>

                            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:12px; margin-top:12px;">
                                <strong>1. 지식 영역 [+] 클릭:</strong><br>
                                빌더 화면 좌측 하단의 <strong class="red-target">[지식 (Knowledge)]</strong> 영역의 <strong>[+]</strong> 버튼 클릭
                            </div>
                            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:12px; margin-top:8px;">
                                <strong>2. 수질/양식 매뉴얼 문서 선택:</strong><br>
                                내 컴퓨터에 다운로드된 <strong class="red-target">[NIFS_넙치_스마트양식_수질관리_매뉴얼.pdf]</strong> 파일 선택 업로드
                            </div>

                            <!-- 보안 수칙 알림 -->
                            <div style="background:#fff1f2; border:1.5px solid #fecdd3; border-radius:8px; padding:10px; margin-top:12px; color:#be123c; font-size:13px; font-weight:700;">
                                🔒 <strong>지식 파일 업로드 보안 수칙:</strong><br>
                                올리려는 파일 내에 실제 어민 성함, 어선/양식장 고유 인정번호나 비밀번호가 적혀 있다면 반드시 사전에 해당 글자를 삭제하고 가명화한 후 탑재하십시오.
                            </div>
                        </div>
                    </div>

                    <!-- 우측: 전달받은 지식(Knowledge) 파일 탑재 실물 캡처 이미지 -->
                    <div class="right-col" style="flex: 1.1;">
                        <div class="ui-sim-card" style="box-shadow:0 6px 20px rgba(0,0,0,0.1);">
                            <div class="sim-header" style="background:#0f172a; padding:12px 16px;">
                                <span class="sim-title" style="font-size:15px; font-weight:800;"><i class="fa-solid fa-image" style="color:#38bdf8;"></i> Step 5: Gems 지식 (Knowledge) 업로드 완료 실물 캡처</span>
                            </div>
                            <div class="sim-body center-img-body" style="padding:8px; background:#ffffff;">
                                <img src="images/step5_knowledge.png" alt="Gems 지식 업로드 완료 캡처 이미지" class="expand-fill-img" style="border-radius:8px;">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="brand-footer-line">
                    [3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사
                </div>
            </div>

            <!-- [Step 6 & Step 7] 실시간 미리보기 테스트, 튜닝 및 동료 공유하기 -->
            <div class="page-block">
                <div class="page-block-header">
                    <h3>Step 6 & 7 : 실시간 미리보기 테스트, 지시사항 튜닝 및 동료 공유하기</h3>
                </div>

                <div class="two-column-layout">
                    <div class="left-col">
                        <div class="instruction-box">
                            <h4><i class="fa-solid fa-vial-circle-check" style="color:#059669;"></i> Step 6: 실시간 테스트 창에서 수조 데이터 검증</h4>
                            <div class="test-chat-box">
                                <div class="user-msg">
                                    <i class="fa-solid fa-comment-dots"></i> 어민 미리보기 테스트 입력:<br>
                                    "수급자 완도 A-03 수조, 7월 26일 16:30 수온 28.2도, 산소 4.1, 사료 절식했음, 폐사 12마리 발생"
                                </div>
                                <div class="ai-msg">
                                    <i class="fa-solid fa-robot red-target"></i> Gems 비서 실시간 자동 응답:<br>
                                    <strong>[7월 26일 A-03 수조 관제 보고서]</strong><br>
                                    • 수온: 28.2℃ (고수온 경보) | DO: 4.1 mg/L (저산소 특보) | 사료: 0kg (절식) | 폐사: 12마리<br>
                                    ➔ <em>[현장 조치 3줄 요약] 사장님! 수온 28도 초과 고수온 경보입니다. 액성산소 100% 가동 및 취수 150% 증대하시고 사료는 전면 절식 유지하세요!</em>
                                </div>
                            </div>

                            <div style="margin-top:12px; background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:12px; font-size:14px;">
                                <strong>Step 6-1: 결과물 보완에 따른 실시간 튜닝:</strong><br>
                                답변 포맷이 불충분하다면 좌측 <strong class="red-target">[요청 사항(Instructions)]</strong> 입력창에서 즉시 텍스트를 수정 후 화살표 버튼을 누르면 실시간 업데이트됩니다.
                            </div>
                        </div>
                    </div>

                    <div class="right-col">
                        <div class="ui-sim-card">
                            <div class="sim-header" style="background:#059669;">
                                <span class="sim-title"><i class="fa-solid fa-share-nodes"></i> Step 7: Gems 비서 저장 및 양식장/수협 동료들과 공유하기</span>
                            </div>
                            <div class="sim-body" style="padding:16px;">
                                <div class="setting-step-sim" style="gap:10px;">
                                    <div class="s-step">
                                        <span class="badge-circle">1</span>
                                        <span>우측 상단의 파란색 <strong class="red-target">[저장]</strong> 버튼을 눌러 비서 최종 등록</span>
                                    </div>
                                    <div class="s-step">
                                        <span class="badge-circle">2</span>
                                        <span>Gem이 생성되었다는 완료 모달창 하단의 <strong class="red-target">[공유]</strong> 버튼 클릭</span>
                                    </div>
                                    <div class="s-step">
                                        <span class="badge-circle">3</span>
                                        <span>일반 액세스 권한을 '제한됨' ➔ <strong class="red-target">[링크가 있는 모든 사용자]</strong>로 교체 후 링크 복사 배포</span>
                                    </div>
                                </div>

                                <div style="background:#f0fdf4; border:1.5px solid #86efac; border-radius:10px; padding:14px; margin-top:10px; color:#14532d; font-size:14px; line-height:1.5;">
                                    💡 <strong>공동 작업의 시너지 효과:</strong><br>
                                    양식장/어촌계 내 한 명이 대표로 고품질 Gems를 빌딩하여 링크 공유 권한을 열어 배포하면, 동료 어민들도 즉시 원클릭으로 휴대폰/PC에서 사용 가능합니다!
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="brand-footer-line">
                    [3차시] 나만의 AI 비서 만들기 - 만들고, 자랑하기 | 오진실 강사
                </div>
            </div>
"""

final_content = content[:pos_step3_block_end] + "\n" + new_blocks + "\n" + content[pos_old_order:]

with open(r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html', 'wb') as f:
    f.write(final_content.encode('utf-8'))

print("SUCCESSFULLY WRITTEN index.html IN UTF-8!")
