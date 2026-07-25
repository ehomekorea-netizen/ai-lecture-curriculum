// JavaScript logic for tab switching, font enlargement toggle, prompt copy, and KST clock widget

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Tab Navigation logic
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');

            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));

            btn.classList.add('active');
            const targetElement = document.getElementById(targetTab);
            if (targetElement) {
                targetElement.classList.add('active');
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });



    // 3. Prompt Copy to Clipboard functionality
    const copyBtns = document.querySelectorAll('.copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (btn.id === 'download-csv-btn') {
                triggerCSVDownload();
                return;
            }

            const copyText = btn.getAttribute('data-copy');
            if (copyText) {
                navigator.clipboard.writeText(copyText).then(() => {
                    showToast('프롬프트가 복사되었습니다! ChatGPT에 붙여넣으세요.');
                }).catch(err => {
                    console.error('Copy failed: ', err);
                });
            }
        });
    });

    // 4. 2차시 엑셀 CSV 다운로드 기능 (국립수산과학원 표준 파라미터 & UTF-8 BOM 적용)
    const downloadCsvBtns = document.querySelectorAll('.download-csv-btn, #download-csv-btn');
    downloadCsvBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            triggerCSVDownload();
        });
    });

    function triggerCSVDownload() {
        const csvContent = "\uFEFF" + 
`일시,수조번호,수온(℃),용존산소(DO mg/L),염분(psu),pH,사료투입량(kg),신규폐사수(마리),현장관제 및 조치사항
2026-07-26 06:00,A-03 수조,22.8,8.2,33.5,8.1,15.0,0,정상 취수(환수율 100%) 및 아침 1차 급이
2026-07-26 10:00,A-03 수조,24.3,7.1,33.4,8.0,15.0,1,연안 수온 상승 시작 (정상 모니터링)
2026-07-26 14:00,A-03 수조,26.5,5.4,33.2,7.9,7.5,2,수온 26℃ 초과에 따른 사료 공급량 50% 감량
2026-07-26 16:30,A-03 수조,28.2,4.1,33.0,7.8,0.0,12,★ 고수온 특보(28℃↑) & 극저산소(4.1mg/L) 감지: 사료 전면 절식 및 액성산소 100% 총력 가동
2026-07-26 20:00,A-03 수조,26.8,6.8,33.3,8.0,0.0,3,액성산소 가동 및 취수 밸브 150% 증대 조치 후 DO 회복세`;

        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.setAttribute('download', '완도_넙치양식장_수온_산소_실습데이터.csv');
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        showToast('📊 실습 데이터(.csv)가 다운로드되었습니다!');
    }

    // 4-1. NIFS 표준 수질관리 매뉴얼 PDF 다운로드 기능
    const downloadPdfBtns = document.querySelectorAll('.download-pdf-btn');
    downloadPdfBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const a = document.createElement('a');
            a.href = 'data/NIFS_넙치_스마트양식_수질관리_매뉴얼.pdf';
            a.setAttribute('download', 'NIFS_넙치_스마트양식_수질관리_매뉴얼.pdf');
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            showToast('📄 NIFS 국립수산과학원 표준 수질관리 매뉴얼(.pdf)이 다운로드되었습니다!');
        });
    });

    // 5. Utility AI Assistant Instructions Generator logic
    const generateBtn = document.getElementById('generate-prompt-btn');
    const outputBox = document.getElementById('generated-output-box');
    const codeBox = document.getElementById('generated-prompt-code');
    const copyGenBtn = document.getElementById('copy-gen-btn');

    if (generateBtn && outputBox && codeBox) {
        generateBtn.addEventListener('click', () => {
            const fishery = document.getElementById('fishery-type').value;
            const task = document.getElementById('task-type').value;

            let taskTitle = "";
            let taskDetail = "";

            if (task === 'daily-log') {
                taskTitle = "양식 관제일지 자동 작성";
                taskDetail = "어민이 거칠게 텍스트/음성으로 말한 수온, 용존산소, 사료투입량, 폐사수 기록을 읽고 한글 깔끔한 관제 표로 변환한다.";
            } else if (task === 'water-warning') {
                taskTitle = "수질이상 긴급 경보 및 대응 가이드";
                taskDetail = "수온 27도 이상, 용존산소 5.0 이하 등 위험 수치가 감지되면 즉시 [긴급 위험 경보]를 발령하고 현장 점검 체크리스트 3가지를 제시한다.";
            } else if (task === 'document-helper') {
                taskTitle = "수산 지원사업 및 수협 서류 작성 도우미";
                taskDetail = "지자체/해양수산부/수협 지원금 및 재해 보상 신청서 문장을 어민 현황에 맞게 행정 양식 문체로 작성한다.";
            }

            const promptCode = 
`[역할선언]
너는 전남 해양수산 현장 전담 '${fishery} 맞춤형 AI 비서'야.

[담당업무]
${taskTitle}: ${taskDetail}

[행동규칙]
1. 어민이 데이터를 입력하면 질문에 대답하기 전, 3초 만에 행동할 수 있는 표(Table) 형태로 요약한다.
2. 이상 수온이나 질병 의심 수치가 나타나면 주저하지 않고 붉은색 강조 및 긴급 체크리스트를 우선 출력한다.
3. 기계 고장이나 질병을 최종 단정짓지 말고 '어민 현장 점검 항목'으로 안내한다.
4. 답변 말투는 전남 어민 어르신께 친근하고 정중하게 존댓말로 작성한다.`;

            codeBox.textContent = promptCode;
            outputBox.classList.remove('hidden');
            outputBox.scrollIntoView({ behavior: 'smooth' });
            showToast('맞춤형 AI 비서 지침이 성공적으로 생성되었습니다!');
        });
    }

    if (copyGenBtn && codeBox) {
        copyGenBtn.addEventListener('click', () => {
            const codeText = codeBox.textContent;
            if (codeText) {
                navigator.clipboard.writeText(codeText).then(() => {
                    showToast('생성된 AI 비서 지침이 복사되었습니다! ChatGPT 맞춤 설정에 붙여넣으세요.');
                });
            }
        });
    }

    // 6. Toast Notification Helper
    function showToast(msg) {
        const toast = document.getElementById('toast');
        const toastMsg = document.getElementById('toast-msg');
        if (toast && toastMsg) {
            toastMsg.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
    }

    // 7. KST Clock Ticking Widget (09:50, 10:50, 11:50 붉은색 휴식 알림)
    function updateKSTClock() {
        const timeDisplay = document.getElementById('kst-time-display');
        const clockWidget = document.getElementById('kst-clock-widget');

        if (!timeDisplay) return;

        const now = new Date();
        const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
        const kstTime = new Date(utc + (3600000 * 9));

        const hours = String(kstTime.getHours()).padStart(2, '0');
        const minutes = String(kstTime.getMinutes()).padStart(2, '0');
        const seconds = String(kstTime.getSeconds()).padStart(2, '0');

        timeDisplay.textContent = `${hours}:${minutes}:${seconds}`;

        if (clockWidget) {
            const restMinutes = ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'];
            if ((hours === '09' || hours === '10' || hours === '11') && restMinutes.includes(minutes)) {
                clockWidget.classList.add('rest-time-alert');
            } else {
                clockWidget.classList.remove('rest-time-alert');
            }
        }
    }

    setInterval(updateKSTClock, 1000);
    updateKSTClock();
});
