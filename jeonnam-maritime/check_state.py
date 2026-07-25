with open(r'C:\Users\IN\.gemini\antigravity\scratch\jeonnam_maritime_curriculum\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Total lines:", content.count('\n'))
print("")

checks = [
    ("1차시 탭", "session1-tab"),
    ("2차시 탭", "session2-tab"),
    ("3차시 탭", "session3-tab"),
    ("Step1 Gems메뉴진입", "Step 1 : 구글 Gemini Gems 메뉴 진입하기"),
    ("Step1 이미지1(setting)", "step1_gems_setting.png"),
    ("Step1 이미지2(menu)", "step1_gems_menu.png"),
    ("Step2 새Gem생성", "Step 2 : 새로운 전용 비서(Gem) 생성하기"),
    ("Step2 이미지", "step2_new_gem.png"),
    ("Step3 이름설정", "Step 3 : 새 Gem의 이름 및 기본 설명 설정하기"),
    ("Step3 이미지", "step3_name_desc.png"),
    ("Step4 지침입력", "Step 4 : ★ 시스템 지침"),
    ("Step4 이미지", "step4_instructions.png"),
    ("Step5 지식탑재", "Step 5 : ★ Gems에 현장 양식 매뉴얼 지식"),
    ("Step5 이미지", "step5_knowledge.png"),
    ("Step5 PDF다운로드버튼", "download-pdf-btn"),
    ("Step6+7 테스트&공유", "Step 6"),
    ("3차시핵심정리 블록", "3차시 핵심 한 줄 정리"),
    ("생성기탭", "generator-tab"),
]

for name, keyword in checks:
    found = keyword in content
    status = "OK  " if found else "MISS"
    print(f"  [{status}] {name}")
