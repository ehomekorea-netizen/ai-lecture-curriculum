# 회사가 원하는 효율적인 AI 활용 - AI 구조화 프롬프트로 엑셀 정복하기
## (기아자동차 맞춤형 전용 실습 프롬프트 모음 v1.1)

---

## PAGE 1

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 1 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
회사가 원하는 효율적인 AI 활용 
－ AI 구조화 프롬프트로 엑셀 정복하기 
 
 
 
 
 
 
 
 
 
 
펴낸곳 : 마소캠퍼스 
홈페이지 : https://www.masocampus.com 
 
 
 
이 문서 내용의 일부 또는 전부를 재사용하려면 반드시 마소캠퍼스의 동의를 얻어야 합니다. 
이 문서는 저작권법에 의하여 보호를 받는 저작물이므로 무단전재와 배포, 무단복제 및 허가 받지 
않은 2차 저작을 금합니다.

---

## PAGE 2

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 2 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
■■■■ EXCEL 과 AI, 꼭 알아둬야할 점 ■■■■ 
 
데이터 업로드 않고 결과를 얻어야 한다 
 
EV6 배터리 충전 효율 추정 실습 
• 실습자료 “01 외부 온도와 배터리 잔량에 따른 EV6 충전 효율.xlsx”를 활용하여 실습을 진행합니다. 
• 생성형 AI 툴에 위의 실습자료를 첨부하고, 프롬프트를 입력합니다. 
• 프롬프트 예시 
외부 온도가 35도, 배터리 잔량(SOC)이 60%일 때 EV6 충전 효율(%)을 추정해 주십시오. 
 
 
 
 
 
 
 
 
 
 
 
엑셀 업무용 프롬프트 작성 필수 지식 
 
마크다운 
• 프롬프트 예시 
다음을 코드블럭 없이 표시해주십시오. 
#마크다운 기호를 쓰면 
--- 
**프롬프트가 잘 정리될 수 있습니다**

---

## PAGE 3

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 3 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
■■■■ 항상 통하는 마법의 명령법: 꼼꼼히 해보면서 터득하기 ■■■■ 
 
비법 #1 EXCEL 데이터를 안 올리면서 설명하는 방법 
 
엑셀 행별 최대값 구하는 함수 도출하기 
• 실습자료 “02 기아 주요 차종별 월별 글로벌 판매 실적(2024).xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
#Task: 
엑셀 함수식을 알려주십시오. 
 
#Context: 
- 데이터의 범위: D5:O18 
- 행: 기아 주요 차종별 글로벌 판매 실적 
- 열: Jan. Feb. Mar. Apr. May. Jun. Jul. Aug. Sep. Oct. Nov.
 Dec. 
- 머릿글: 5번 행은 머릿글 
- 데이터 타입: 모두 수치형 
 
#Instruction: 
- 엑셀 2016을 기준으로 제안해주십시오. 
- 각 행의 최대값을 구하는 수식 
 
 
 
 
구글 스프레드시트의 정보를 활용하여 이메일을 보내는 앱스 스크립트 코드 작성하기 
• 새로운 구글 스프레드시트를 만들어 영상의 실습을 따라하며 내용을 구성한 후 진행합니다.  
• 프롬프트 예시 
구글 스프레드시트의 정보를 가지고 이메일을 보내는 앱스 스크립트 코드를 작성해주세요. 
 
#스프레드시트의 정보 
- A1:D2에 데이터가 있음 
- {A열,C열,D열}={address,subject,body} 
- 1번행은 머릿글

---

## PAGE 4

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 4 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
비법 #2 단어 1 개, 문장 하나만 바꾸면 된다 
 
행별 최대값을 나타내는 열 이름을 구하는 함수 도출하기 
• 실습자료 “02 기아 주요 차종별 월별 글로벌 판매 실적(2024).xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
#Task: 
엑셀 함수식을 알려주십시오. 
 
#Context: 
- 데이터의 범위: D5:O18 
- 행: 기아 주요 차종별 글로벌 판매 실적 
- 열: Jan. Feb. Mar. Apr. May. Jun. Jul. Aug. Sep. Oct. Nov.
 Dec. 
- 머릿글: 5번 행은 머릿글 
- 데이터 타입: 모두 수치형 
 
#Instruction: 
- 엑셀 2016을 기준으로 제안해주십시오. 
- 각 행의 최대값을 나타내는 월(열 이름)을 구하는 수식 
 
 
행별 최대값을 나타내는 셀을 노란색으로 색칠하는 방법 도출하기 
• 실습자료 “02 기아 주요 차종별 월별 글로벌 판매 실적(2024).xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
#Task: 
엑셀 사용법을 알려주십시오. 
 
#Context: 
- 데이터의 범위: D5:O18 
- 행: 기아 주요 차종별 글로벌 판매 실적 
- 열: Jan. Feb. Mar. Apr. May. Jun. Jul. Aug. Sep. Oct. Nov.
 Dec. 
- 머릿글: 5번 행은 머릿글 
- 데이터 타입: 모두 수치형 
 
#Instruction: 
- 엑셀 2016을 기준으로 제안해주십시오. 
- 각 행의 최대값을 나타내는 셀을 노란색으로 색칠하는 방법

---

## PAGE 5

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 5 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
행별 최대값을 나타내는 셀(단, 행의 값이 모두 0 인 행 제외)을 파란색으로 색칠하는 방법 도출하기 
• 실습자료 “02 기아 주요 차종별 월별 글로벌 판매 실적(2024).xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
#Task: 
엑셀 사용법을 알려주십시오. 
 
#Context: 
- 데이터의 범위: D5:O18 
- 행: 기아 주요 차종별 글로벌 판매 실적 
- 열: Jan. Feb. Mar. Apr. May. Jun. Jul. Aug. Sep. Oct. Nov.
 Dec. 
- 머릿글: 5번 행은 머릿글 
- 데이터 타입: 모두 수치형 
 
#Instruction: 
- 엑셀 2016을 기준으로 제안해주십시오. 
- 각 행의 최대값을 나타내는 셀을 파란색으로 색칠하는 방법 
- 특정 행의 값이 모두 0이라면, 해당 행은 색칠하지 말아주세요

---

## PAGE 6

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 6 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
비법 #3 어설픈 설명보다 정확한 명령 
 
한영 번역(절차로 설명하기) 
• 프롬프트 예시 
한영 번역해주십시오. 
다음 지침을 이해했다면, “OK”로 입력 요청하십시오. 
 
사용자가 입력하는 한글을 문장마다 끊어서 출력하고, 
다음 줄에 영어로 번역해주십시오. 
한글은 앞에 -을 추가하고, 영어는 소괄호 안에 넣어 출력하십시오. 
 
오늘 날씨가 좋네요. 소풍 갈까요? 
 
 
한영 번역(예시로 설명하기) 
• 프롬프트 예시 
한영 번역해주십시오. 
다음 지침을 이해했다면, “OK”로 입력 요청하십시오. 
 
예를 들어, “AI는 당신을 대체하지 않습니다. AI를 잘 활용하는 사람이 당신을 대체합니다.”라는 문장이 
입력되면 다음과 같이 처리합니다. 
- AI는 당신을 대체하지 않습니다. 
(AI does not replace you.) 
- AI를 잘 활용하는 사람이 당신을 대체합니다. 
(It is the person who uses AI well that replaces you.) 
 
오늘 날씨가 좋네요. 소풍 갈까요? 
 
 
엑셀 수식 계산 방법 
• 실습 파일 “03 기아 차종별 옵션 품목 재고액.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
A2:A11을 더해서 C2로 나누는 엑셀 수식을 알려줘.

---

## PAGE 7

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 7 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
품목에 특정 키워드가 포함되어 있으면, 포함된 키워드 출력하기(절차로 설명하기) 
• 실습 파일 “03 기아 차종별 옵션 품목 재고액.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
엑셀 수식을 만들어 주십시오. 
# 데이터 
- 품목 : A2:A21 (문자열) 
- 분류 : F2:F6 (문자열) 
# 작업 
- ‘품목’에 ‘분류’의 키워드 중 하나라도 포함되어 있으면, 그 포함된 키워드 출력 
- 만약 여러 키워드가 포함되어 있으면, 그 중 마지막으로 탐색된 키워드 출력 
# 기타 
- 키워드가 없는 행은 “기타”를 출력한다. 
- 엑셀 2016 기준 
 
 
품목에 특정 키워드가 포함되어 있으면, 포함된 키워드 출력하기(예시로 설명하기) 
• 실습 파일 “03 기아 차종별 옵션 품목 재고액.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
엑셀 수식을 만들어 주십시오. 
 
# 데이터 
- 품목 : A2:A21 (문자열) 
- 분류 : F2:F6 (문자열) 
# 결과 예시 
- A2: “쏘렌토 하이브리드 그래비티 패키지 7인승” → “하이브리드” 
- A3: “카니발 가솔린 프레스티지 기본형 9인승” → “가솔린” 
- A4: “EV6 전기 스탠다드 라이트 패키지” → “전기” 
 
# 기타 
- 키워드가 없는 행은 “기타”를 출력한다. 
- 엑셀 2016 기준

---

## PAGE 8

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 8 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
■■■■ 심화 응용: 까다로운 조건에 맞는 자료 추출 ■■■■ 
 
온라인 거래 자료에서 까다로운 조건에 맞는 자료 추출 
 
대리점 ID 의 고유값을 추출하는 엑셀 수식 작성하기 
• 실습 파일 “04 기아 글로벌 해외 법인 대리점별 차량 발주 내역.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
고유값을 추출하는 엑셀 수식을 작성해주십시오. 
 
##원본 데이터 
- 표 
{발주번호,부품코드,부품/차종명,발주수량,발주지시일,단가,대리점ID,대리점명,국가} 
- 각 행은 개별 부품 거래 기록이다. 
- 데이터는 “01” 시트의 A1:I831에 있으며, 첫 행은 머리글이다. 
 
##결과물 
- “02” 시트의 A열에(첫 행은 머리글) “01” 시트 G열 [대리점ID]의 고유값을 추출한다. 
 
##제약조건 
- Excel 2016 버전에서 작동해야 하므로 버전 충돌 없도록 주의하십시오. 
 
 
대리점 ID 에 대응되는 대리점명 을 추출하는 엑셀 수식 작성하기 
• 실습 파일 “04 기아 글로벌 해외 법인 대리점별 차량 발주 내역.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
엑셀 수식을 작성해주십시오. 
 
##원본 데이터 
- 표 
{발주번호,부품코드,부품/차종명,발주수량,발주지시일,단가,대리점ID,대리점명,국가} 
- 각 행은 개별 부품 거래 기록이다. 
- 데이터는 “01” 시트의 A1:I831에 있으며, 첫 행은 머리글이다. 
 
##결과물 
- “02” 시트의 B열에(첫 행은 머리글) A열의 [대리점ID]에 대응되는 [대리점명]을 입력한다. 
 
##제약조건 
- Excel 2016 버전에서 작동해야 하므로 버전 충돌 없도록 주의하십시오.

---

## PAGE 9

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 9 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
대리점 ID 별로 최근 2 번째 발주지시일 을 추출하는 엑셀 수식 작성하기 
• 실습 파일 “04 기아 글로벌 해외 법인 대리점별 차량 발주 내역.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
각 대리점별 발주일자를 추출하는 엑셀 수식을 작성해주십시오. 
 
##원본 데이터 
- 표 
{발주번호,부품코드,부품/차종명,발주수량,발주지시일,단가,대리점ID,대리점명,국가} 
- 각 행은 개별 부품 거래 기록이다. 
- 데이터는 “01” 시트의 A1:I831에 있으며, 첫 행은 머리글이다. 
 
##결과물 
- “02” 시트의 C열에(첫 행은 머리글) A열(대리점ID)별 “01” 시트 E열(발주지시일)의 내림차순 
2번째로 큰값을 추출한다. 
 
##제약조건 
- Excel 2016 버전에서 작동해야 하므로 버전 충돌 없도록 주의하십시오.

---

## PAGE 10

Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
페이지 10 / 11 
Only legitimate buyers are authoirzed to read this. Copyright MasoCampus. All rights reserved. 
■■■■ 엑셀 수식으로 안되는 모든 작업에는 VBA 매크로 ■■■■ 
 
AI 로 VBA 만들고 실행하기 
 
특정 문자열을 입력하는 엑셀 VBA 코드 작성하기 
• 프롬프트 예시 
A1셀에 “안녕하세요”라고 입력하는 엑셀 VBA 코드를 만들어주세요. 
 
 
동그라미를 그리는 엑셀 VBA 코드 작성하기 
• 프롬프트 예시 
엑셀 VBA 코드를 만들어 주세요. 
 
- B2셀부터 10px 간격으로, 같은 행에 4개씩 총 16개의 동그라미를 그린다 
- 동그라미는 색상은 옅은 노랑색, 지름 30px, 투명도 20%이다. 
- 매크로를 실행한 후에 1초 간격으로 동그라미가 한 개씩 추가된다. 
 
 
함수 전부 외울 필요 없이 만들어 쓰자 
 
사용자 정의 함수를 만드는 엑셀 VBA 코드 작성하기 
• 실습 파일 “03 기아 차종별 옵션 품목 재고액.xlsx”를 활용하여 실습을 진행합니다. 
• 프롬프트 예시 
엑셀 사용자 정의 함수를 만드는 VBA 코드를 작성해주십시오. 
 
#함수 
- 형태: =my_engine(품목,분류) 
- 기능: ‘옵션명’에 있는 텍스트에 ‘분류’에 있는 항목이 포함되어 있다면, 해당 항목들을 추출한다. 
- 출력: 쉼표로 구분 
 
#지침 
- 엑셀 2016에서 잘 동작해야 합니다.

---
