import sys
sys.stdout.reconfigure(encoding='utf-8')

html = r"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>노션 사이트 기반 인터랙티브 웹 포트폴리오 제작 - 5주차 교안</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b1a16; --card-bg: #142b24; --card-border: #057a5f;
      --text-main: #ffffff; --text-sub: #d1e7dd; --text-muted: #88ab9e;
      --purple: #00664f; --purple-light: #ffe066; --cyan: #34d399;
      --emerald: #10b981; --amber: #ffe066; --rose: #f43f5e;
      --gradient-purple: linear-gradient(135deg, #057a5f 0%, #00523f 100%);
      --gradient-cyan: linear-gradient(135deg, #059669 0%, #00664f 100%);
      --gradient-card: linear-gradient(180deg, rgba(5,122,95,0.25) 0%, rgba(20,43,36,0.95) 100%);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: var(--bg); color: var(--text-main); font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; overflow: hidden; width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; -webkit-font-smoothing: antialiased; }
    .deck-container { width: 1280px; height: 720px; position: relative; transform-origin: center center; flex-shrink: 0; }
    .slide { position: absolute; top: 0; left: 0; width: 1280px; height: 720px; background: var(--card-bg); border: none !important; border-radius: 20px; padding: 45px 65px; opacity: 0; visibility: hidden; transform: translateX(50px) scale(0.98); transition: opacity 0.4s cubic-bezier(0.16,1,0.3,1), transform 0.4s cubic-bezier(0.16,1,0.3,1), visibility 0.4s; display: flex; flex-direction: column; justify-content: space-between; overflow: hidden; box-shadow: 0 25px 60px rgba(0,0,0,0.6); }
    .slide.active { opacity: 1 !important; visibility: visible !important; transform: translateX(0) scale(1) !important; }
    .slide-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px; }
    .slide-meta { display: flex; align-items: center; gap: 12px; font-size: 14px; font-weight: 600; letter-spacing: 0.05em; color: var(--purple-light); text-transform: uppercase; }
    .slide-meta-tag { background: rgba(0,102,79,0.3); border: 1px solid var(--card-border); padding: 4px 10px; border-radius: 6px; }
    .slide-number-badge { font-size: 26px; font-weight: 800; color: rgba(255,255,255,0.30); }
    .slide-title-group h2 { font-size: 32px; font-weight: 800; line-height: 1.25; color: #fff; margin-top: 4px; letter-spacing: -0.02em; }
    .slide-title-group p { font-size: 17px; color: var(--text-sub); margin-top: 6px; font-weight: 400; }
    .slide-footer { display: flex; justify-content: flex-end; align-items: center; font-size: 13px; color: var(--text-muted); border-top: 1px solid rgba(255,255,255,0.06); padding-top: 14px; margin-top: auto; }
    .slide-footer span:first-child { display: none !important; }
    .content-body { flex: 1; display: flex; flex-direction: column; justify-content: center; margin: 10px 0; gap: 16px; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; }
    .grid-5 { display: grid; grid-template-columns: repeat(5,1fr); gap: 12px; }
    .card { background: var(--gradient-card); background-color: rgba(20,43,36,0.6); border: 1px solid var(--card-border); border-radius: 14px; padding: 20px 24px; display: flex; flex-direction: column; gap: 8px; transition: all 0.3s ease; }
    .card:hover { border-color: #34d399; transform: translateY(-2px); }
    .card-accent { border-left: 4px solid var(--purple); } .card-cyan { border-left: 4px solid var(--cyan); }
    .card-emerald { border-left: 4px solid var(--emerald); } .card-amber { border-left: 4px solid var(--amber); } .card-rose { border-left: 4px solid #f43f5e; }
    .card-num { font-size: 22px; font-weight: 800; color: var(--purple-light); }
    .card-title { font-size: 19px; font-weight: 700; color: #fff; }
    .card-desc { font-size: 14px; color: var(--text-sub); line-height: 1.5; }
    .callout { background: rgba(0,102,79,0.2); border: 1px solid var(--card-border); border-radius: 12px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; color: var(--text-main); font-size: 15px; font-weight: 500; }
    .callout-icon { font-size: 22px; }
    .ai-note { background: rgba(255,224,102,0.1); border: 1px solid rgba(255,224,102,0.3); border-radius: 12px; padding: 14px 18px; color: #ffe066; font-size: 14px; display: flex; gap: 10px; align-items: center; }
    .summary-table { width: 100%; border-collapse: collapse; background: rgba(0,0,0,0.2); border-radius: 12px; overflow: hidden; border: 1px solid var(--card-border); }
    .summary-table th { background: rgba(255,255,255,0.06); color: var(--purple-light); padding: 12px 16px; text-align: left; font-size: 14px; font-weight: 700; }
    .summary-table td { padding: 10px 16px; border-top: 1px solid rgba(255,255,255,0.05); color: var(--text-main); font-size: 13.5px; line-height: 1.45; }
    .summary-table tr:hover td { background: rgba(255,255,255,0.02); }
    .slide-title-hero { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; gap: 20px; padding: 0 40px; }
    .hero-kicker { background: var(--gradient-purple); color: white; padding: 6px 16px; border-radius: 20px; font-size: 14px; font-weight: 700; letter-spacing: 0.05em; }
    .hero-tags { display: flex; gap: 12px; margin-top: 10px; }
    .tag { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); padding: 8px 18px; border-radius: 8px; font-size: 14px; color: var(--cyan); font-weight: 600; }
    .slide-section-divider { height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; gap: 16px; }
    .progress-bar { position: fixed; bottom: 0; left: 0; height: 4px; background: var(--gradient-purple); transition: width 0.3s ease; z-index: 100; }
    .page-indicator { position: absolute; bottom: -42px; right: 0; background: rgba(18,21,34,0.85); border: 1px solid var(--card-border); backdrop-filter: blur(10px); padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; color: var(--text-sub); z-index: 100; }
    .nav-zone { position: fixed; top: 0; bottom: 0; width: 42px; z-index: 5; cursor: pointer; }
    .nav-zone.left { left: 0; } .nav-zone.right { right: 0; }
    .help-btn { position: absolute; bottom: -42px; right: 90px; width: 32px; height: 32px; border-radius: 50%; background: rgba(255,255,255,0.08); border: 1px solid var(--card-border); color: white; font-weight: 700; cursor: pointer; z-index: 100; display: flex; align-items: center; justify-content: center; transition: all 0.2s ease; }
    :fullscreen .page-indicator, :fullscreen .help-btn, :-webkit-full-screen .page-indicator, :-webkit-full-screen .help-btn { display: none !important; opacity: 0 !important; visibility: hidden !important; }
    body.is-fullscreen .page-indicator, body.is-fullscreen .help-btn { display: none !important; opacity: 0 !important; visibility: hidden !important; }
    .help-btn:hover { background: rgba(0,102,79,0.4); transform: scale(1.05); }
    .help-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(8px); z-index: 200; justify-content: center; align-items: center; }
    .help-modal.active { display: flex; }
    .help-content { background: var(--card-bg); padding: 36px 44px; border-radius: 16px; max-width: 480px; width: 90%; border: 1px solid var(--card-border); box-shadow: 0 20px 50px rgba(0,0,0,0.8); }
    .help-content h3 { font-size: 22px; margin-bottom: 20px; color: #fff; border-bottom: 1px solid var(--card-border); padding-bottom: 10px; }
    .help-list { list-style: none; display: flex; flex-direction: column; gap: 12px; font-size: 15px; color: var(--text-sub); }
    .help-list b { color: var(--purple-light); display: inline-block; width: 140px; }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .split-layout { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 24px; align-items: stretch; margin-top: 8px; }
    .view-left-canvas { background: #11131f; border: 1px solid var(--purple-light); border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
    .canvas-toolbar { background: rgba(255,255,255,0.05); border-bottom: 1px solid rgba(255,255,255,0.08); padding: 10px 16px; display: flex; justify-content: space-between; align-items: center; }
    .canvas-toolbar-title { font-size: 13px; font-weight: 700; color: var(--purple-light); }
    .canvas-screen-area { padding: 18px 22px; flex: 1; position: relative; min-height: 240px; }
    .guide-right-steps { display: flex; flex-direction: column; gap: 10px; justify-content: center; }
    .step-card { background: rgba(255,255,255,0.02); border: 1px solid var(--card-border); border-radius: 12px; padding: 14px 18px; transition: all 0.3s ease; opacity: 0.5; }
    .step-card.active { opacity: 1; background: rgba(0,102,79,0.15); border-color: var(--purple-light); box-shadow: 0 0 20px rgba(0,102,79,0.25); transform: translateX(4px); }
    .step-card-num { font-size: 12px; font-weight: 800; color: var(--text-muted); letter-spacing: 0.05em; }
    .step-card.active .step-card-num { color: var(--purple-light); }
    .step-card-title { font-size: 16px; font-weight: 600; color: var(--text-main); margin-top: 2px; }
    .step-card.active .step-card-title { color: #fff; font-weight: 800; font-size: 17px; }
    .step-card-desc { font-size: 13px; color: var(--text-sub); margin-top: 4px; line-height: 1.4; }
    .step-btn-group { display: flex; gap: 8px; }
    .btn-step { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.2s ease; }
    .btn-step:hover { background: rgba(0,102,79,0.3); border-color: var(--purple-light); }
    .btn-step-next { background: var(--gradient-purple); border: none; }
    .parr-block { background: rgba(255,255,255,0.03); border: 1px solid var(--card-border); border-radius: 10px; padding: 14px 16px; display: flex; gap: 14px; align-items: flex-start; transition: all 0.3s ease; }
    .parr-block.active { background: rgba(0,102,79,0.18); border-color: var(--cyan); box-shadow: 0 0 18px rgba(52,211,153,0.2); }
    .parr-letter { font-size: 28px; font-weight: 900; color: var(--purple-light); min-width: 36px; line-height: 1; }
    .parr-block.active .parr-letter { color: var(--cyan); }
    .parr-content-title { font-size: 15px; font-weight: 700; color: #fff; }
    .parr-content-desc { font-size: 13px; color: var(--text-sub); margin-top: 3px; line-height: 1.45; }
    .qa-row { display: flex; align-items: center; gap: 14px; padding: 10px 16px; border-radius: 10px; border: 1px solid var(--card-border); background: rgba(0,0,0,0.15); transition: all 0.3s ease; cursor: pointer; }
    .qa-row:hover { background: rgba(0,102,79,0.12); }
    .qa-row.checked { background: rgba(52,211,153,0.08); border-color: var(--cyan); }
    .qa-check { width: 22px; height: 22px; border-radius: 6px; border: 2px solid var(--card-border); display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 900; flex-shrink: 0; transition: all 0.2s ease; }
    .qa-row.checked .qa-check { background: var(--cyan); border-color: var(--cyan); color: #0b1a16; }
    .qa-num { font-size: 12px; font-weight: 800; color: var(--text-muted); min-width: 28px; }
    .qa-row.checked .qa-num { color: var(--cyan); }
    .qa-text { font-size: 14px; color: var(--text-main); font-weight: 500; flex: 1; }
    .qa-badge { font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 12px; background: rgba(255,255,255,0.08); color: var(--text-muted); }
    .qa-row.checked .qa-badge { background: rgba(52,211,153,0.15); color: var(--cyan); }
    .embed-box { background: #11131f; border: 1px dashed rgba(255,255,255,0.2); border-radius: 10px; padding: 14px 18px; display: flex; align-items: center; gap: 14px; font-size: 14px; color: var(--text-sub); transition: all 0.4s ease; min-height: 64px; }
    .embed-box.active { background: rgba(0,102,79,0.15); border-color: var(--cyan); border-style: solid; color: #fff; }
    .embed-icon { font-size: 26px; flex-shrink: 0; }
    .embed-label { font-size: 13px; font-weight: 700; color: var(--purple-light); margin-bottom: 3px; }
    .embed-box.active .embed-label { color: var(--cyan); }
    .settings-table { width: 100%; border-collapse: collapse; font-size: 13px; }
    .settings-table th { background: rgba(0,102,79,0.25); color: var(--purple-light); padding: 10px 14px; text-align: left; font-weight: 700; font-size: 13px; border-bottom: 1px solid var(--card-border); }
    .settings-table td { padding: 9px 14px; border-top: 1px solid rgba(255,255,255,0.05); color: var(--text-main); vertical-align: top; line-height: 1.45; }
    .settings-table td:first-child { color: var(--cyan); font-weight: 700; }
    .settings-table tr:hover td { background: rgba(255,255,255,0.025); }
    @media print {
      body { overflow: visible; background: #fff !important; color: #000 !important; }
      .deck-container { transform: none !important; width: 100% !important; height: auto !important; }
      .slide { position: relative !important; opacity: 1 !important; visibility: visible !important; transform: none !important; page-break-after: always; margin-bottom: 30px; box-shadow: none !important; border: 1px solid #ddd !important; background: #fff !important; color: #000 !important; }
      .slide * { color: #111 !important; border-color: #ddd !important; background: transparent !important; }
      .progress-bar, .page-indicator, .nav-zone, .help-btn, .help-modal { display: none !important; }
    }
  </style>
</head>
<body>
  <div class="deck-container" id="deckContainer">

    <!-- SLIDE 01: HERO TITLE -->
    <div class="slide active" id="slide01HeroContainer">
      <div class="slide-title-hero" style="padding: 0 20px;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
          <span class="hero-kicker" style="font-size:14px;padding:6px 18px;background:#00664f;color:#ffe066;border:1.5px solid #34d399;font-weight:800;border-radius:20px;">C&middot;Campus 밀양소통협력센터 &middot; DIGITAL SKILL</span>
          <span style="background:rgba(255,224,102,0.12);border:1px solid rgba(255,224,102,0.3);padding:5px 14px;border-radius:16px;font-size:13px;font-weight:700;color:#ffe066;">5주차</span>
        </div>
        <h1 style="font-size:50px;font-weight:900;line-height:1.25;color:#ffffff;letter-spacing:-0.02em;margin-top:6px;">
          노션 사이트(Notion Sites) 기반<br>
          <span style="color:#ffe066;text-shadow:0 0 15px rgba(255,224,102,0.4);">인터랙티브 웹 포트폴리오 제작</span>
        </h1>
        <p style="font-size:20px;color:var(--text-sub);margin-top:12px;font-weight:400;max-width:820px;line-height:1.6;">
          코딩 없이 노션만으로 <b>채용 담당자를 사로잡는 전문 웹 포트폴리오</b>를 완성합니다.<br>
          PAR-R 프레임워크 기반 기획 &rarr; 템플릿 커스터마이징 &rarr; 사이트 배포 &rarr; 최종 QA 검수
        </p>
        <div class="hero-tags">
          <span class="tag">📐 포트폴리오 기획</span>
          <span class="tag">🎨 템플릿 커스터마이징</span>
          <span class="tag">🌐 노션 사이트 배포</span>
          <span class="tag">📱 반응형 최적화</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 5주차 (수/목) · 디지털 실무 교안</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 02: PURPOSE -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">START</span></div>
          <h2>웹 포트폴리오, 왜 지금 만들어야 할까요?</h2>
          <p>채용 현장에서 평가자는 수많은 포트폴리오를 빠르게 스캐닝합니다 &mdash; 구조와 전달력이 먼저입니다.</p>
        </div>
        <div class="slide-number-badge">1</div>
      </div>
      <div class="content-body">
        <div class="grid-2">
          <div class="card card-accent" style="padding:24px;">
            <div class="card-num">01. 첫인상의 승부처</div>
            <div class="card-title" style="font-size:20px;">단 3초 안에 결정됩니다</div>
            <div class="card-desc" style="font-size:15px;margin-top:8px;">채용 담당자가 포트폴리오를 검토하는 평균 시간은 3초. <b>정보의 전달력과 구조적 명확성</b>이 합격을 결정합니다.</div>
          </div>
          <div class="card card-cyan" style="padding:24px;">
            <div class="card-num">02. 노션의 강점</div>
            <div class="card-title" style="font-size:20px;">코딩 없이 전문 웹사이트</div>
            <div class="card-desc" style="font-size:15px;margin-top:8px;">노션 사이트(Notion Sites)는 클릭 몇 번으로 작성 중인 페이지를 <b>고유한 URL의 전문 웹사이트</b>로 즉시 전환합니다.</div>
          </div>
        </div>
        <div class="grid-3" style="margin-top:4px;">
          <div class="card" style="padding:18px;border-left:4px solid var(--cyan);">
            <div style="font-size:28px;font-weight:900;color:var(--purple-light);">5</div>
            <div style="font-size:15px;font-weight:700;color:#fff;margin-top:2px;">5대 핵심 섹션</div>
            <div style="font-size:13px;color:var(--text-sub);">Profile · Experience · Projects · Skills · Contact</div>
          </div>
          <div class="card" style="padding:18px;border-left:4px solid var(--emerald);">
            <div style="font-size:28px;font-weight:900;color:var(--purple-light);">4</div>
            <div style="font-size:15px;font-weight:700;color:#fff;margin-top:2px;">PAR-R 프레임워크</div>
            <div style="font-size:13px;color:var(--text-sub);">문제→행동→결과→회고로 역량 입증</div>
          </div>
          <div class="card" style="padding:18px;border-left:4px solid var(--amber);">
            <div style="font-size:28px;font-weight:900;color:var(--purple-light);">1</div>
            <div style="font-size:15px;font-weight:700;color:#fff;margin-top:2px;">최종 산출물</div>
            <div style="font-size:13px;color:var(--text-sub);">배포 가능한 나만의 웹 포트폴리오 URL</div>
          </div>
        </div>
        <div class="callout" style="padding:13px 20px;">
          <span class="callout-icon">💡</span>
          <span><b>교육 목표:</b> 단순 도구 사용법을 넘어, <b>채용 담당자의 관점에서 설계된 전략적 포트폴리오</b>를 2일 안에 완성합니다.</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 5주차 웹 포트폴리오 개요</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 03: 5대 핵심 섹션 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">STRUCTURE</span></div>
          <h2>포트폴리오 5대 핵심 섹션 구성</h2>
          <p>채용 담당자가 빠르게 스캐닝하는 5가지 정보 영역을 체계적으로 설계합니다.</p>
        </div>
        <div class="slide-number-badge">2</div>
      </div>
      <div class="content-body">
        <div class="grid-5" style="gap:14px;">
          <div class="card" style="padding:18px 16px;border-top:4px solid #00664f;border-left:none;"><div style="font-size:24px;margin-bottom:6px;">👤</div><div class="card-num" style="font-size:16px;">Profile</div><div class="card-title" style="font-size:15px;">프로필</div><div class="card-desc" style="font-size:12.5px;margin-top:6px;">한 줄 슬로건 · 직무 타이틀 · 이미지 · 주요 연락처</div></div>
          <div class="card" style="padding:18px 16px;border-top:4px solid var(--cyan);border-left:none;"><div style="font-size:24px;margin-bottom:6px;">📋</div><div class="card-num" style="font-size:16px;">Experience</div><div class="card-title" style="font-size:15px;">경력 사항</div><div class="card-desc" style="font-size:12.5px;margin-top:6px;">최신순 · 소속 조직 · 담당 직무 · 정량적 성과</div></div>
          <div class="card" style="padding:18px 16px;border-top:4px solid var(--emerald);border-left:none;"><div style="font-size:24px;margin-bottom:6px;">🗂️</div><div class="card-num" style="font-size:16px;">Projects</div><div class="card-title" style="font-size:15px;">프로젝트</div><div class="card-desc" style="font-size:12.5px;margin-top:6px;">3~5개 대표 사례 · 갤러리 DB · 성과 지표</div></div>
          <div class="card" style="padding:18px 16px;border-top:4px solid var(--amber);border-left:none;"><div style="font-size:24px;margin-bottom:6px;">⚙️</div><div class="card-num" style="font-size:16px;">Skills</div><div class="card-title" style="font-size:15px;">스킬</div><div class="card-desc" style="font-size:12.5px;margin-top:6px;">활용 가능 범위 · 작업 수준 정성·정량 서술</div></div>
          <div class="card" style="padding:18px 16px;border-top:4px solid var(--rose);border-left:none;"><div style="font-size:24px;margin-bottom:6px;">📧</div><div class="card-num" style="font-size:16px;">Contact</div><div class="card-title" style="font-size:15px;">연락처</div><div class="card-desc" style="font-size:12.5px;margin-top:6px;">이메일 · GitHub · LinkedIn · SNS 하이퍼링크</div></div>
        </div>
        <div style="background:rgba(0,102,79,0.15);border:1px solid var(--card-border);border-radius:12px;padding:16px 20px;margin-top:6px;">
          <div style="font-size:13px;font-weight:800;color:var(--purple-light);margin-bottom:10px;">📐 레이아웃 체계 (위 → 아래)</div>
          <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
            <span style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 14px;border-radius:8px;font-size:13px;color:var(--cyan);font-weight:600;">내비게이션 바</span>
            <span style="color:var(--text-muted);">→</span>
            <span style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 14px;border-radius:8px;font-size:13px;color:var(--cyan);font-weight:600;">히어로 섹션 (Profile)</span>
            <span style="color:var(--text-muted);">→</span>
            <span style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 14px;border-radius:8px;font-size:13px;color:var(--cyan);font-weight:600;">프로젝트 갤러리 DB</span>
            <span style="color:var(--text-muted);">→</span>
            <span style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 14px;border-radius:8px;font-size:13px;color:var(--cyan);font-weight:600;">경력 &amp; 스킬</span>
            <span style="color:var(--text-muted);">→</span>
            <span style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);padding:6px 14px;border-radius:8px;font-size:13px;color:var(--cyan);font-weight:600;">푸터 (Contact)</span>
          </div>
        </div>
        <div class="ai-note" style="margin-top:6px;padding:12px 18px;">
          <span>✍️ <b>작성 원칙:</b> 문장 어미를 <b>명사형('분석 완료', '기획 수립')</b>으로 통일하고, 메인은 요약 카드로, 상세 내용은 하위 페이지로 분리합니다.</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 5주차 포트폴리오 구성 설계</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 04: 커리큘럼 로드맵 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">CURRICULUM</span></div>
          <h2>[디지털 실무] 웹 포트폴리오 제작 커리큘럼 로드맵</h2>
          <p>수요일(기획/템플릿)과 목요일(동적 페이지/최종 완성)로 이어지는 2단계 세션</p>
        </div>
        <div class="slide-number-badge">3</div>
      </div>
      <div class="content-body">
        <div style="background:rgba(0,102,79,0.12);border:1.5px solid var(--purple-light);border-radius:12px;padding:10px 18px;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;">
          <div style="font-size:14px;font-weight:800;color:#fff;">📌 5주차 종합 목표: <span style="color:#ffe066;">코딩 없이 노션 사이트 기반 인터랙티브 웹 포트폴리오를 완성하고 URL 배포</span></div>
          <span style="background:var(--purple);color:#fff;font-size:12px;font-weight:900;padding:3px 12px;border-radius:6px;">[디지털 실무] Notion Sites</span>
        </div>
        <div class="grid-2" style="gap:18px;">
          <div class="card card-accent" style="padding:20px;background:rgba(26,26,36,0.95);border:2px solid #00664f;border-radius:16px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;border-bottom:1px solid #1a2a22;padding-bottom:8px;">
              <span style="font-size:13px;font-weight:900;background:var(--gradient-purple);color:#fff;padding:3px 10px;border-radius:6px;">1일차 · 수요일</span>
              <span style="font-size:12.5px;color:var(--cyan);font-weight:800;">기획 &amp; 템플릿 커스터마이징</span>
            </div>
            <div style="font-size:16px;font-weight:900;color:#fff;margin-bottom:8px;">포트폴리오 기획 및 메인 페이지 완성</div>
            <ul style="margin-left:16px;color:var(--text-sub);font-size:13px;line-height:1.7;">
              <li>Module 1: 포트폴리오 기획 &amp; PAR-R 프레임워크</li>
              <li>Module 2: 노션 템플릿 분석 &amp; 구조 세팅</li>
              <li>Module 3: 메인 페이지 커스터마이징 실습</li>
              <li><b>Module 4: 노션 사이트 배포 &amp; 1차 URL 생성</b></li>
            </ul>
            <div style="margin-top:10px;background:rgba(0,102,79,0.15);border-radius:8px;padding:8px 12px;font-size:12.5px;color:#86efac;font-weight:700;">🎯 산출물: 메인 랜딩페이지 + 1차 배포 URL</div>
          </div>
          <div class="card card-cyan" style="padding:20px;background:rgba(18,30,42,0.95);border:2px solid #06b6d4;border-radius:16px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;border-bottom:1px solid #1e3a47;padding-bottom:8px;">
              <span style="font-size:13px;font-weight:900;background:linear-gradient(135deg,#06b6d4,#10b981);color:#fff;padding:3px 10px;border-radius:6px;">2일차 · 목요일</span>
              <span style="font-size:12.5px;color:#22d3ee;font-weight:800;">동적 페이지 &amp; 최종 완성</span>
            </div>
            <div style="font-size:16px;font-weight:900;color:#fff;margin-bottom:8px;">동적 콘텐츠 구성 및 최종 포트폴리오 완성</div>
            <ul style="margin-left:16px;color:var(--text-sub);font-size:13px;line-height:1.7;">
              <li>Module 5: 프로젝트 상세 페이지 구조화</li>
              <li>Module 6: 멀티미디어 임베드 &amp; 동기화 블록</li>
              <li>Module 7: 고급 설정 &amp; 반응형 최적화</li>
              <li><b>Module 8: 시크릿 모드 검수 &amp; 최종 완성 공유</b></li>
            </ul>
            <div style="margin-top:10px;background:rgba(6,182,212,0.15);border-radius:8px;padding:8px 12px;font-size:12.5px;color:#67e8f9;font-weight:700;">🏆 최종 결과물: 배포 완료된 <b>나만의 웹 포트폴리오 URL</b></div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · [디지털 실무] 웹 포트폴리오 2단계 커리큘럼</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 05: 1일차 배너 -->
    <div class="slide">
      <div class="slide-section-divider" style="background:linear-gradient(135deg,rgba(0,102,79,0.18) 0%,rgba(6,182,212,0.12) 100%);border:2px solid #00664f;border-radius:24px;padding:50px;">
        <div class="hero-kicker" style="font-size:15px;padding:6px 18px;background:var(--gradient-purple);color:#fff;font-weight:900;">1일차 · 수요일</div>
        <h1 style="font-size:44px;font-weight:900;color:#fff;margin-top:18px;line-height:1.35;">포트폴리오 기획 및<br><span style="color:#ffe066;text-shadow:0 0 20px rgba(255,224,102,0.4);">템플릿 커스터마이징</span></h1>
        <p style="font-size:18px;color:#e2e8f0;margin-top:14px;max-width:800px;margin-left:auto;margin-right:auto;line-height:1.6;">채용 담당자 관점의 기획 전략을 세우고,<br>노션 공식 템플릿을 나만의 포트폴리오로 탈바꿈합니다.</p>
        <div style="margin-top:24px;display:inline-flex;gap:12px;align-items:center;background:rgba(0,0,0,0.4);padding:8px 20px;border-radius:30px;border:1px solid rgba(0,102,79,0.4);">
          <span style="color:var(--purple-light);font-weight:800;font-size:14px;">🎯 핵심 목표:</span>
          <span style="color:#fff;font-size:14px;">PAR-R 기획 완성 · 메인 페이지 커스터마이징 · 1차 URL 배포</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 1일차 세션 시작</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 06: MODULE 1 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 1</span></div>
          <h2>Module 1: 포트폴리오 기획 및 자산 정리 (40분)</h2>
          <p>채용 담당자 관점의 평가 기준을 이해하고, 대표 프로젝트 3개를 빠르게 선정합니다.</p>
        </div>
        <div class="slide-number-badge">5</div>
      </div>
      <div class="content-body">
        <div class="grid-3" style="gap:16px;">
          <div class="card card-accent" style="padding:20px;"><div class="card-num">STEP 01</div><div class="card-title">평가 기준 이해</div><div class="card-desc" style="margin-top:6px;">채용 담당자가 3초 안에 보는 것: <b>직무 연관성, 성과 수치, 구조적 명확성</b></div></div>
          <div class="card card-cyan" style="padding:20px;"><div class="card-num">STEP 02</div><div class="card-title">대표 사례 3개 선정</div><div class="card-desc" style="margin-top:6px;">성과가 가장 명확한 경험 3개를 <b>직무 연관성 기준</b>으로 빠르게 선별합니다.</div></div>
          <div class="card card-emerald" style="padding:20px;"><div class="card-num">STEP 03</div><div class="card-title">슬로건 &amp; 역량 요약</div><div class="card-desc" style="margin-top:6px;">메인 슬로건과 핵심 역량 요약문을 <b>5줄 이내로 간결하게</b> 작성합니다.</div></div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border:1px solid var(--card-border);border-radius:14px;padding:18px 22px;margin-top:8px;">
          <div style="font-size:14px;font-weight:800;color:var(--purple-light);margin-bottom:12px;">📝 스크리닝 매트릭스 활용법 (텍스트 작성 병목 최소화)</div>
          <div class="grid-3" style="gap:14px;">
            <div style="background:rgba(0,102,79,0.15);border-radius:10px;padding:12px 14px;"><div style="font-size:13px;font-weight:700;color:var(--cyan);margin-bottom:4px;">① 경험 목록 나열</div><div style="font-size:12.5px;color:var(--text-sub);">사전에 준비한 경험 자산을 시트에 전부 나열합니다</div></div>
            <div style="background:rgba(0,102,79,0.15);border-radius:10px;padding:12px 14px;"><div style="font-size:13px;font-weight:700;color:var(--cyan);margin-bottom:4px;">② 직무 필터링</div><div style="font-size:12.5px;color:var(--text-sub);">지원 직무에 적합한 항목만 선별 표시합니다</div></div>
            <div style="background:rgba(0,102,79,0.15);border-radius:10px;padding:12px 14px;"><div style="font-size:13px;font-weight:700;color:var(--cyan);margin-bottom:4px;">③ 서식 통일</div><div style="font-size:12.5px;color:var(--text-sub);">명사형 어미 + 수치 강조로 비즈니스 전문성 확보</div></div>
          </div>
        </div>
        <div class="ai-note" style="padding:12px 18px;">
          <span>📌 <b>강사 가이드:</b> 수강생들이 텍스트 작성에 오래 머물지 않도록 직무별 <b>예시 문구를 제시</b>하고, 빠른 선별을 유도합니다.</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 1 포트폴리오 기획</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 07: PAR-R 인터랙티브 -->
    <div class="slide" id="slideParrContainer">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 1 · INTERACTIVE</span></div>
          <h2>PAR-R 프레임워크로 프로젝트 사례 작성하기</h2>
          <p>논리적 사고 과정과 문제 해결 역량을 입증하는 4단계 구조입니다.</p>
        </div>
        <div class="slide-number-badge">6</div>
      </div>
      <div class="content-body">
        <div class="split-layout">
          <div style="display:flex;flex-direction:column;gap:10px;justify-content:center;">
            <div class="parr-block active" id="parrBlock0"><div class="parr-letter">P</div><div><div class="parr-content-title">Problem · 문제 정의</div><div class="parr-content-desc">해결해야 할 과제를 정량적 데이터나 유저 인터뷰를 바탕으로 <b>3줄 이내로 명확히</b> 명시합니다.</div></div></div>
            <div class="parr-block" id="parrBlock1"><div class="parr-letter">A</div><div><div class="parr-content-title">Action · 수행 행동</div><div class="parr-content-desc">본인의 실제 기여도와 핵심 설계·기획·개발 로직을 구체적으로 서술합니다.</div></div></div>
            <div class="parr-block" id="parrBlock2"><div class="parr-letter">R</div><div><div class="parr-content-title">Result · 결과 성과</div><div class="parr-content-desc">전환율, 조회수, 공정 단축 비율 등 <b>정량 지표</b>를 기반으로 성과를 증명합니다.</div></div></div>
            <div class="parr-block" id="parrBlock3"><div class="parr-letter">R</div><div><div class="parr-content-title">Retrospective · 회고</div><div class="parr-content-desc">Lessons Learned와 추후 개선점을 서술하여 <b>성장 가능성</b>을 어필합니다.</div></div></div>
          </div>
          <div style="display:flex;flex-direction:column;gap:10px;justify-content:center;">
            <div style="background:#11131f;border:1px solid var(--card-border);border-radius:14px;overflow:hidden;">
              <div style="background:rgba(255,255,255,0.05);padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.08);display:flex;align-items:center;justify-content:space-between;">
                <span style="font-size:13px;font-weight:700;color:var(--purple-light);">📝 작성 예시 미리보기</span>
                <div class="step-btn-group">
                  <button class="btn-step" onclick="parrPrev()">◀</button>
                  <button class="btn-step btn-step-next" onclick="parrNext()">다음 ▶</button>
                  <button class="btn-step" onclick="parrReset()">↺</button>
                </div>
              </div>
              <div style="padding:16px 18px;min-height:200px;display:flex;flex-direction:column;justify-content:center;gap:10px;">
                <div id="parrExampleContent" style="font-size:14px;color:#fff;line-height:1.7;">
                  <div style="color:var(--purple-light);font-size:12px;font-weight:700;margin-bottom:6px;">[ P · 문제 정의 ]</div>
                  <div style="color:var(--text-sub);margin-bottom:4px;">💼 프로젝트: SNS 콘텐츠 기획 인턴</div>
                  <div>기존 인스타그램 계정의 팔로워 증가율이 <b style="color:#ffe066;">월 평균 1.2%</b>에 그쳐 브랜드 인지도 확산에 한계. 콘텐츠 주제 분산과 업로드 일관성 부재가 핵심 원인으로 분석됨.</div>
                </div>
                <div id="parrStatusBadge" style="background:rgba(0,102,79,0.2);border-radius:8px;padding:7px 12px;font-size:12px;color:var(--cyan);font-weight:700;text-align:center;">P 단계 — [다음 ▶] 버튼으로 Action → Result → Retrospective 순서로 확인하세요</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · PAR-R 프레임워크 인터랙티브</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 08: MODULE 2 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 2</span></div>
          <h2>Module 2: 노션 템플릿 분석 및 구조 세팅 (50분)</h2>
          <p>목적과 직무군에 따라 구조가 다른 공식 템플릿을 선택하고 브랜딩 체계를 설정합니다.</p>
        </div>
        <div class="slide-number-badge">7</div>
      </div>
      <div class="content-body">
        <div class="grid-3" style="gap:16px;margin-bottom:8px;">
          <div class="card" style="border-top:4px solid #00664f;border-left:none;"><div style="font-size:22px;margin-bottom:4px;">🧑‍💼</div><div class="card-title" style="font-size:16px;">개인 포트폴리오형</div><div class="card-desc">단일 랜딩페이지 레이아웃 · 초보자 최적 · 빠른 커스터마이징</div></div>
          <div class="card" style="border-top:4px solid var(--cyan);border-left:none;"><div style="font-size:22px;margin-bottom:4px;">🎨</div><div class="card-title" style="font-size:16px;">디자이너·개발자형</div><div class="card-desc">메인에 갤러리 DB 배치 · 시각적 작업물 커버 먼저 노출</div></div>
          <div class="card" style="border-top:4px solid var(--amber);border-left:none;"><div style="font-size:22px;margin-bottom:4px;">🏢</div><div class="card-title" style="font-size:16px;">에이전시형</div><div class="card-desc">히어로 섹션 + 클라이언트 로고 + 서비스 프로세스 강조</div></div>
        </div>
        <div style="background:rgba(0,0,0,0.2);border:1px solid var(--card-border);border-radius:14px;padding:18px 20px;">
          <div style="font-size:14px;font-weight:800;color:var(--purple-light);margin-bottom:12px;">🎨 브랜드 디자인 원칙 (Visual Clarity)</div>
          <div class="grid-3" style="gap:12px;">
            <div style="background:rgba(0,102,79,0.12);border-radius:10px;padding:12px 14px;"><div style="font-size:15px;font-weight:700;color:var(--cyan);">🎨 컬러 3톤 이내</div><div style="font-size:13px;color:var(--text-sub);margin-top:4px;">메인·서브·포인트 3가지 톤으로 제한하여 통일감 확보</div></div>
            <div style="background:rgba(0,102,79,0.12);border-radius:10px;padding:12px 14px;"><div style="font-size:15px;font-weight:700;color:var(--cyan);">📐 제목 계층 준수</div><div style="font-size:13px;color:var(--text-sub);margin-top:4px;">H1 → H2 → H3 계층을 엄격히 준수하여 가독성 극대화</div></div>
            <div style="background:rgba(0,102,79,0.12);border-radius:10px;padding:12px 14px;"><div style="font-size:15px;font-weight:700;color:var(--cyan);">💬 콜아웃 &amp; 여백</div><div style="font-size:13px;color:var(--text-sub);margin-top:4px;">콜아웃 블록과 충분한 여백으로 시각적 피로도 최소화</div></div>
          </div>
        </div>
        <div class="callout" style="padding:13px 20px;">
          <span class="callout-icon">⚠️</span>
          <span><b>주의:</b> 복잡한 다단 구조나 위젯 과다 사용은 <b>로딩 속도 저하</b>와 집중 방해를 유발합니다 — 미학적 절제미가 핵심입니다.</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 2 노션 템플릿 분석</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 09: 노션 사이트 배포 설정 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 4 · DEPLOY</span></div>
          <h2>노션 사이트 게시 커스텀 옵션 완전 정복</h2>
          <p>6가지 배포 설정을 제대로 활용하면 플랫폼 독립적인 전문 웹사이트를 구현할 수 있습니다.</p>
        </div>
        <div class="slide-number-badge">8</div>
      </div>
      <div class="content-body" style="justify-content:flex-start;margin-top:4px;">
        <table class="settings-table">
          <thead><tr><th style="width:150px;">게시 옵션</th><th>기능 설명</th><th>실무 적용 전략</th></tr></thead>
          <tbody>
            <tr><td>Site Slug</td><td>기본 URL 뒤의 고유 하위 주소 변경 (.notion.site/my-name)</td><td>지원자 이름이나 퍼스널 브랜딩명을 반영한 직관적 URL 생성</td></tr>
            <tr><td>Theme</td><td>Light / Dark / 시스템 설정 모드 제어</td><td>IT·개발 직무 → 다크 / 기획·디자인 직무 → 라이트 테마</td></tr>
            <tr><td>Favicon &amp; Thumbnail</td><td>브라우저 탭 아이콘 + 소셜 링크 공유 썸네일 업로드</td><td>메신저 공유 시 브랜드 로고와 대표 작업물이 노출되도록 세팅</td></tr>
            <tr><td>Header Options</td><td>이동 경로(Breadcrumbs) · 검색 · 템플릿 복제 토글 제어</td><td>내비게이션 편의성 향상 + 템플릿 무단 복제 방지</td></tr>
            <tr><td>Search Engine Indexing</td><td>구글 등 웹 검색 엔진 노출 여부 선택</td><td>범용 공개 시 Indexing ON / 제출용 비공개 시 Indexing OFF</td></tr>
            <tr><td>Google Analytics</td><td>GA 추적 ID 연결을 통한 방문자 데이터 분석</td><td>포트폴리오 유입 경로 및 섹션별 체류 시간 지표 추적</td></tr>
          </tbody>
        </table>
        <div class="ai-note" style="padding:11px 18px;margin-top:10px;">
          <span>🌐 <b>Module 4 핵심 실습:</b> 노션 사이트 '웹에 게시' 버튼 → Custom Slug 설정 → <b>수강생 전원 1차 URL 생성 &amp; 상호 피드백</b></span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 노션 사이트 배포 설정</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 10: 1일차 타임테이블 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">DAY 1 · 타임테이블</span></div>
          <h2>1일차 수요일 3시간 교안 타임테이블</h2>
          <p>포트폴리오 기획 → 템플릿 세팅 → 커스터마이징 → 1차 배포까지 단계별로 진행합니다.</p>
        </div>
        <div class="slide-number-badge">9</div>
      </div>
      <div class="content-body" style="justify-content:flex-start;margin-top:6px;">
        <table class="summary-table">
          <thead><tr><th style="width:150px;">시간</th><th style="width:200px;">모듈명</th><th>주요 교육 내용 및 실습</th><th style="width:180px;">산출물</th></tr></thead>
          <tbody>
            <tr><td style="color:var(--cyan);">00:00 – 00:40</td><td><b>Module 1</b> · 포트폴리오 기획</td><td>PAR-R 기반 대표 프로젝트 3개 선정 · 메인 슬로건 및 역량 요약문 작성</td><td>기획 시트 완성</td></tr>
            <tr><td style="color:var(--cyan);">00:40 – 01:30</td><td><b>Module 2</b> · 템플릿 분석 &amp; 세팅</td><td>노션 블록 조작 숙달 · 공식 템플릿 복제 · 브랜드 테마 컬러 &amp; 폰트 설정</td><td>템플릿 복제본</td></tr>
            <tr><td style="color:var(--text-muted);font-style:italic;">01:30 – 01:40</td><td style="color:var(--text-muted);">Break Time</td><td style="color:var(--text-muted);">휴식 및 개인별 진행 상황 점검</td><td style="color:var(--text-muted);">—</td></tr>
            <tr><td style="color:var(--cyan);">01:40 – 02:30</td><td><b>Module 3</b> · 메인 커스터마이징</td><td>프로필·경력·스킬 블록 구조 개편 · 다단 레이아웃 배치 · 갤러리 DB 프레임 구축</td><td>메인 랜딩페이지</td></tr>
            <tr><td style="color:var(--purple-light);font-weight:700;">02:30 – 03:00</td><td><b>Module 4</b> · 노션 사이트 배포</td><td>노션 사이트 웹 게시 실행 · Custom Slug 설정 · 상호 피드백 · 2일차 준비 과제 안내</td><td style="color:var(--purple-light);font-weight:700;">1차 배포 URL ✓</td></tr>
          </tbody>
        </table>
        <div class="callout" style="margin-top:10px;padding:12px 20px;">
          <span class="callout-icon">🎯</span>
          <span><b>1일차 종료 기준:</b> 수강생 전원의 1차 노션 사이트 URL 생성 확인 + 퍼블리싱 환경 확립 완료</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 1일차 수요일 타임테이블</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 11: 2일차 배너 -->
    <div class="slide">
      <div class="slide-section-divider" style="background:linear-gradient(135deg,rgba(6,182,212,0.15) 0%,rgba(16,185,129,0.12) 100%);border:2px solid #06b6d4;border-radius:24px;padding:50px;">
        <div class="hero-kicker" style="font-size:15px;padding:6px 18px;background:linear-gradient(135deg,#06b6d4,#10b981);color:#fff;font-weight:900;">2일차 · 목요일</div>
        <h1 style="font-size:44px;font-weight:900;color:#fff;margin-top:18px;line-height:1.35;">동적 페이지 구성 및<br><span style="color:#67e8f9;text-shadow:0 0 20px rgba(103,232,249,0.4);">최종 포트폴리오 완성</span></h1>
        <p style="font-size:18px;color:#e2e8f0;margin-top:14px;max-width:800px;margin-left:auto;margin-right:auto;line-height:1.6;">Figma, YouTube, PDF를 페이지 안에 임베드하고,<br>시크릿 모드 QA 검수를 거쳐 완성된 포트폴리오를 세상에 공개합니다.</p>
        <div style="margin-top:24px;display:inline-flex;gap:12px;align-items:center;background:rgba(0,0,0,0.4);padding:8px 20px;border-radius:30px;border:1px solid rgba(6,182,212,0.4);">
          <span style="color:#67e8f9;font-weight:800;font-size:14px;">🏆 핵심 목표:</span>
          <span style="color:#fff;font-size:14px;">멀티미디어 임베드 · 반응형 최적화 · QA 검수 · 최종 URL 완성</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 2일차 세션 시작</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 12: MODULE 5 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 5</span></div>
          <h2>Module 5: 프로젝트 상세 페이지 구조화 (30분)</h2>
          <p>PAR-R 구조 기반 세부 내역을 작성하고 토글 블록으로 긴 서술문을 압축합니다.</p>
        </div>
        <div class="slide-number-badge">10</div>
      </div>
      <div class="content-body">
        <div class="grid-2" style="gap:20px;">
          <div style="display:flex;flex-direction:column;gap:12px;">
            <div style="background:rgba(0,102,79,0.12);border:1px solid var(--card-border);border-radius:12px;padding:16px 18px;">
              <div style="font-size:14px;font-weight:800;color:var(--purple-light);margin-bottom:10px;">📝 상세 페이지 구성 요소</div>
              <div style="display:flex;flex-direction:column;gap:8px;">
                <div style="display:flex;align-items:center;gap:10px;font-size:14px;"><span style="width:6px;height:6px;background:var(--cyan);border-radius:50%;flex-shrink:0;"></span><span><b style="color:var(--cyan);">PAR-R 구조</b> 기반 세부 내역 작성</span></div>
                <div style="display:flex;align-items:center;gap:10px;font-size:14px;"><span style="width:6px;height:6px;background:var(--cyan);border-radius:50%;flex-shrink:0;"></span><span><b style="color:var(--cyan);">토글(Toggle) 블록</b>으로 긴 서술문 압축 처리</span></div>
                <div style="display:flex;align-items:center;gap:10px;font-size:14px;"><span style="width:6px;height:6px;background:var(--cyan);border-radius:50%;flex-shrink:0;"></span><span><b style="color:var(--cyan);">콜아웃 블록</b>으로 핵심 성과 지표 강조</span></div>
                <div style="display:flex;align-items:center;gap:10px;font-size:14px;"><span style="width:6px;height:6px;background:var(--cyan);border-radius:50%;flex-shrink:0;"></span><span>사용 툴 태그 및 프로젝트 기간 속성 명시</span></div>
              </div>
            </div>
            <div class="ai-note" style="padding:12px 16px;">
              <span>⚠️ <b>강사 주의:</b> 상세 페이지에 텍스트만 과도하게 채우지 않도록 토글 블록을 적극 활용하여 비하인드 스토리를 숨김 처리하세요.</span>
            </div>
          </div>
          <div style="background:#f7f7f5;border-radius:14px;overflow:hidden;border:1px solid rgba(255,255,255,0.15);">
            <div style="background:#e8e8e6;padding:8px 14px;display:flex;align-items:center;gap:10px;">
              <div style="display:flex;gap:5px;"><div style="width:10px;height:10px;border-radius:50%;background:#ff5f57;"></div><div style="width:10px;height:10px;border-radius:50%;background:#ffbd2e;"></div><div style="width:10px;height:10px;border-radius:50%;background:#28ca41;"></div></div>
              <div style="flex:1;background:white;border-radius:16px;padding:4px 12px;font-size:11px;color:#555;font-family:monospace;">notion.site/my-portfolio/sns-project</div>
            </div>
            <div style="padding:16px 18px;">
              <div style="font-size:22px;font-weight:900;color:#1a1a1a;margin-bottom:12px;">📱 SNS 콘텐츠 기획 인턴십</div>
              <div style="background:rgba(0,102,79,0.08);border-left:3px solid #00664f;padding:10px 14px;border-radius:0 8px 8px 0;font-size:12.5px;color:#333;margin-bottom:10px;">
                💡 <b>핵심 성과:</b> 팔로워 증가율 월 1.2% → <span style="color:#00664f;font-weight:700;">월 8.7%</span>로 626% 개선
              </div>
              <div style="font-size:12px;color:#666;line-height:1.6;">▶ <b>Problem:</b> 기존 계정의 팔로워 증가율이 월 평균 1.2%에 그쳐...<br><span style="display:inline-block;background:#f0f0ee;padding:3px 8px;border-radius:4px;margin-top:6px;color:#888;font-size:11px;">🔽 클릭하여 Action 내용 펼치기</span></div>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 5 프로젝트 상세 페이지</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 13: MODULE 6 임베드 인터랙티브 -->
    <div class="slide" id="slideEmbedContainer">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 6 · INTERACTIVE</span></div>
          <h2>Module 6: 멀티미디어 임베드 &amp; 동기화 블록 (60분)</h2>
          <p>방문자가 포트폴리오 내부에서 직접 작업물을 검증할 수 있도록 동적 콘텐츠를 연동합니다.</p>
        </div>
        <div class="slide-number-badge">11</div>
      </div>
      <div class="content-body">
        <div class="split-layout">
          <div>
            <div class="view-left-canvas" style="height:100%;">
              <div class="canvas-toolbar">
                <span class="canvas-toolbar-title">🎬 /임베드 명령어 시뮬레이터</span>
                <div class="step-btn-group">
                  <button class="btn-step" onclick="embedPrev()">◀</button>
                  <button class="btn-step btn-step-next" onclick="embedNext()">임베드 추가 ▶</button>
                  <button class="btn-step" onclick="embedReset()">↺</button>
                </div>
              </div>
              <div class="canvas-screen-area" style="display:flex;flex-direction:column;gap:10px;">
                <div id="embedBox0" class="embed-box active"><div class="embed-icon">🖼️</div><div><div class="embed-label">Figma 프로토타입</div><div style="font-size:13px;color:var(--text-sub);">/임베드 → Figma 링크 → 페이지 내부에서 직접 조작 가능</div></div></div>
                <div id="embedBox1" class="embed-box"><div class="embed-icon">▶️</div><div><div class="embed-label">YouTube 영상</div><div style="font-size:13px;color:var(--text-sub);">/임베드 → YouTube 링크 → 인터뷰·발표 영상 즉시 재생</div></div></div>
                <div id="embedBox2" class="embed-box"><div class="embed-icon">📄</div><div><div class="embed-label">PDF 파일</div><div style="font-size:13px;color:var(--text-sub);">/임베드 → PDF 업로드 → 기획서·보고서 페이지 내 미리보기</div></div></div>
                <div id="embedBox3" class="embed-box"><div class="embed-icon">🖼️</div><div><div class="embed-label">이미지 갤러리</div><div style="font-size:13px;color:var(--text-sub);">갤러리 DB → 카드 커버 이미지로 시각적 작업물 그리드</div></div></div>
                <div id="embedStatusBadge" style="background:rgba(0,102,79,0.15);border-radius:8px;padding:8px 12px;font-size:12px;color:var(--cyan);font-weight:700;text-align:center;">Figma 임베드 완료 — [임베드 추가 ▶]로 다음 미디어 추가</div>
              </div>
            </div>
          </div>
          <div class="guide-right-steps">
            <div style="background:rgba(0,0,0,0.2);border:1px solid var(--card-border);border-radius:14px;padding:18px;">
              <div style="font-size:14px;font-weight:800;color:var(--purple-light);margin-bottom:12px;">🔄 동기화 블록(Synced Block)</div>
              <div style="font-size:13px;color:var(--text-sub);line-height:1.7;">내비게이션 바를 동기화 블록으로 설정하면,<br><b style="color:var(--cyan);">원본 1곳만 수정해도</b> 연결된<br><b style="color:var(--cyan);">모든 하위 페이지에 자동 반영</b>됩니다.</div>
              <div style="margin-top:12px;background:rgba(52,211,153,0.08);border:1px dashed var(--cyan);border-radius:8px;padding:10px 14px;font-size:12.5px;color:#fff;"><b>실습:</b> 만들어둔 내비게이션 바를 프로젝트 상세 페이지 상단에 붙여넣기</div>
            </div>
            <div style="background:rgba(0,0,0,0.2);border:1px solid var(--card-border);border-radius:14px;padding:18px;">
              <div style="font-size:14px;font-weight:800;color:var(--purple-light);margin-bottom:12px;">🔘 CTA 버튼 블록 삽입</div>
              <div style="display:flex;flex-direction:column;gap:8px;font-size:13px;color:var(--text-sub);">
                <div style="display:flex;align-items:center;gap:8px;"><span style="background:rgba(0,102,79,0.3);border:1px solid var(--card-border);padding:4px 12px;border-radius:20px;color:#fff;font-size:12px;font-weight:700;">📧 이메일 보내기</span><span>클릭 시 이메일 앱 즉시 실행</span></div>
                <div style="display:flex;align-items:center;gap:8px;"><span style="background:rgba(0,102,79,0.3);border:1px solid var(--card-border);padding:4px 12px;border-radius:20px;color:#fff;font-size:12px;font-weight:700;">📥 PDF 이력서 다운로드</span><span>이력서 즉시 다운로드</span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 6 멀티미디어 임베드</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 14: MODULE 7 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 7</span></div>
          <h2>Module 7: 사이트 고급 설정 및 반응형 최적화 (50분)</h2>
          <p>파비콘·소셜 썸네일 등록부터 모바일 반응형 레이아웃 점검까지 전문가 마무리 단계입니다.</p>
        </div>
        <div class="slide-number-badge">12</div>
      </div>
      <div class="content-body">
        <div class="grid-3" style="gap:16px;margin-bottom:10px;">
          <div class="card card-accent" style="padding:18px;"><div style="font-size:24px;margin-bottom:6px;">🔖</div><div class="card-title" style="font-size:15px;">Favicon &amp; OG 썸네일</div><div class="card-desc">카카오톡·링크드인 링크 공유 시 브랜드 이미지와 파비콘이 자동 노출되도록 등록</div></div>
          <div class="card card-cyan" style="padding:18px;"><div style="font-size:24px;margin-bottom:6px;">📱</div><div class="card-title" style="font-size:15px;">모바일 반응형 점검</div><div class="card-desc">PC의 좌우 다단 배치가 모바일에서 상하 정렬로 바뀌는 순서 꼬임 현상 수정</div></div>
          <div class="card card-amber" style="padding:18px;"><div style="font-size:24px;margin-bottom:6px;">🔒</div><div class="card-title" style="font-size:15px;">복제 방지 &amp; 검색 설정</div><div class="card-desc">템플릿 복제 토글 Off + 검색 엔진 노출 여부 상황에 맞게 최적화</div></div>
        </div>
        <div style="background:rgba(255,224,102,0.07);border:1px solid rgba(255,224,102,0.25);border-radius:14px;padding:18px 20px;">
          <div style="font-size:14px;font-weight:800;color:#ffe066;margin-bottom:12px;">📱 반응형 최적화 체크포인트</div>
          <div class="grid-2" style="gap:14px;">
            <div style="font-size:13.5px;color:var(--text-sub);line-height:1.7;"><b style="color:#fff;">PC → 모바일 확인 방법:</b><br>브라우저 개발자 도구(F12) → 모바일 디바이스 뷰 선택하여 반응형 상태 시뮬레이션</div>
            <div style="font-size:13.5px;color:var(--text-sub);line-height:1.7;"><b style="color:#fff;">자주 발생하는 문제:</b><br>PC 좌우 다단 → 모바일 상하 정렬 시 콘텐츠 순서 꼬임 / 텍스트 잘림 / 수평 스크롤</div>
          </div>
        </div>
        <div class="callout" style="padding:12px 20px;">
          <span class="callout-icon">🎯</span>
          <span><b>Module 7 완료 기준:</b> 파비콘 &amp; 소셜 썸네일 등록 완료 + 모바일 세로 뷰에서 텍스트 잘림 없이 정상 배치 확인</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 7 고급 설정 &amp; 반응형 최적화</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 15: MODULE 8 QA 체크리스트 -->
    <div class="slide" id="slideQaContainer">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">MODULE 8 · QA CHECKLIST</span></div>
          <h2>Module 8: 시크릿 모드 검수 &amp; 최종 완성 QA 체크리스트</h2>
          <p>배포 전 7가지 항목을 순서대로 클릭하여 품질 보증(QA) 절차를 완료합니다.</p>
        </div>
        <div class="slide-number-badge">13</div>
      </div>
      <div class="content-body" style="justify-content:flex-start;margin-top:4px;">
        <div style="display:flex;flex-direction:column;gap:8px;" id="qaChecklistContainer">
          <div class="qa-row" id="qa0" onclick="toggleQa(0)"><div class="qa-check" id="qaCheck0"></div><div class="qa-num">01</div><div class="qa-text">시크릿 창(Ctrl+Shift+N)에서 로그인 없이 페이지가 즉시 노출되는가?</div><div class="qa-badge" id="qaBadge0">외부 접근 권한</div></div>
          <div class="qa-row" id="qa1" onclick="toggleQa(1)"><div class="qa-check" id="qaCheck1"></div><div class="qa-num">02</div><div class="qa-text">메인 페이지 내 프로젝트 상세 하위 페이지가 정상적으로 열리는가?</div><div class="qa-badge" id="qaBadge1">하위 페이지 열람</div></div>
          <div class="qa-row" id="qa2" onclick="toggleQa(2)"><div class="qa-check" id="qaCheck2"></div><div class="qa-num">03</div><div class="qa-text">모바일 세로 뷰에서 텍스트 잘림 없이 정상 배치되는가?</div><div class="qa-badge" id="qaBadge2">반응형 레이아웃</div></div>
          <div class="qa-row" id="qa3" onclick="toggleQa(3)"><div class="qa-check" id="qaCheck3"></div><div class="qa-num">04</div><div class="qa-text">Figma, GitHub, PDF, 이메일 외부 링크가 클릭 시 정상 작동하는가?</div><div class="qa-badge" id="qaBadge3">외부 링크 작동</div></div>
          <div class="qa-row" id="qa4" onclick="toggleQa(4)"><div class="qa-check" id="qaCheck4"></div><div class="qa-num">05</div><div class="qa-text">노션 사이트 설정에서 '템플릿으로 복제 허용' 토글이 Off 상태인가?</div><div class="qa-badge" id="qaBadge4">무단 복제 방지</div></div>
          <div class="qa-row" id="qa5" onclick="toggleQa(5)"><div class="qa-check" id="qaCheck5"></div><div class="qa-num">06</div><div class="qa-text">카카오톡·링크드인 링크 공유 시 썸네일과 파비콘이 정상 노출되는가?</div><div class="qa-badge" id="qaBadge5">비주얼 브랜딩</div></div>
          <div class="qa-row" id="qa6" onclick="toggleQa(6)"><div class="qa-check" id="qaCheck6"></div><div class="qa-num">07</div><div class="qa-text">오타가 없으며 명사형 어미('분석 완료', '기획 수립')가 통일 적용되었는가?</div><div class="qa-badge" id="qaBadge6">텍스트 &amp; 가독성</div></div>
        </div>
        <div id="qaStatusBadge" style="background:rgba(0,102,79,0.15);border-radius:10px;padding:10px 16px;font-size:13px;color:var(--text-muted);font-weight:600;text-align:center;margin-top:4px;">📋 항목을 클릭하여 체크하세요 — 0 / 7 완료</div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · Module 8 최종 QA 체크리스트</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 16: 2일차 타임테이블 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-title-group">
          <div class="slide-meta"><span class="slide-meta-tag">DAY 2 · 타임테이블</span></div>
          <h2>2일차 목요일 3시간 교안 타임테이블</h2>
          <p>프로젝트 상세 → 멀티미디어 → 고급 설정 → QA 검수까지 최종 완성을 목표로 합니다.</p>
        </div>
        <div class="slide-number-badge">14</div>
      </div>
      <div class="content-body" style="justify-content:flex-start;margin-top:6px;">
        <table class="summary-table">
          <thead><tr><th style="width:150px;">시간</th><th style="width:200px;">모듈명</th><th>주요 교육 내용 및 실습</th><th style="width:200px;">산출물</th></tr></thead>
          <tbody>
            <tr><td style="color:var(--cyan);">00:00 – 00:30</td><td><b>Module 5</b> · 상세 페이지</td><td>PAR-R 구조 세부 작성 · 토글 블록 압축 · 핵심 성과 콜아웃 강조</td><td>프로젝트 상세 페이지 완성</td></tr>
            <tr><td style="color:var(--cyan);">00:30 – 01:30</td><td><b>Module 6</b> · 멀티미디어 임베드</td><td>Figma · YouTube · PDF 임베드 · 동기화 블록 내비게이션 · CTA 버튼 삽입</td><td>동적 상세 페이지 2개 이상</td></tr>
            <tr><td style="color:var(--text-muted);font-style:italic;">01:30 – 01:40</td><td style="color:var(--text-muted);">Break Time</td><td style="color:var(--text-muted);">휴식 및 개인별 디바이스 상태 점검</td><td style="color:var(--text-muted);">—</td></tr>
            <tr><td style="color:var(--cyan);">01:40 – 02:30</td><td><b>Module 7</b> · 고급 설정 &amp; 반응형</td><td>파비콘 &amp; OG 썸네일 등록 · 모바일 반응형 점검 · 복제 방지 &amp; 검색 설정 최적화</td><td>노션 사이트 최종 설정 완료</td></tr>
            <tr><td style="color:var(--purple-light);font-weight:700;">02:30 – 03:00</td><td><b>Module 8</b> · 최종 검수 &amp; 공유</td><td>시크릿 창 7단계 QA 검수 · 라이브 갤러리 피드백 · PDF 이력서 변환 &amp; 제출 링크 정리</td><td style="color:var(--purple-light);font-weight:700;">🏆 최종 포트폴리오 URL</td></tr>
          </tbody>
        </table>
        <div class="callout" style="margin-top:10px;padding:12px 20px;">
          <span class="callout-icon">🏆</span>
          <span><b>최종 산출물:</b> 단독 웹사이트 URL 형태로 채용 플랫폼에 제출하거나, <b>PDF 이력서 상단 대표 링크</b>로 결합 가능한 완성형 포트폴리오</span>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 2일차 목요일 타임테이블</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

    <!-- SLIDE 17: WRAP-UP -->
    <div class="slide">
      <div class="slide-title-hero" style="padding:0 20px;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
          <span class="hero-kicker" style="background:linear-gradient(135deg,#06b6d4,#10b981);color:#fff;">5주차 완성!</span>
        </div>
        <h1 style="font-size:46px;font-weight:900;line-height:1.25;color:#ffffff;letter-spacing:-0.02em;">
          나만의 노션 웹 포트폴리오,<br>
          <span style="color:#ffe066;text-shadow:0 0 15px rgba(255,224,102,0.4);">세상에 공개되었습니다! 🚀</span>
        </h1>
        <p style="font-size:18px;color:var(--text-sub);margin-top:14px;font-weight:400;max-width:820px;line-height:1.6;">
          채용 담당자의 관점으로 설계하고, PAR-R로 역량을 증명하며, 노션 사이트로 배포한<br>
          <b>당신만의 전문 웹 포트폴리오</b>는 이제 평생 활용할 수 있는 최강의 취업 무기입니다.
        </p>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:20px;width:100%;">
          <div style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:16px;text-align:center;"><div style="font-size:26px;margin-bottom:6px;">📐</div><div style="font-size:14px;font-weight:700;color:#fff;">PAR-R 기획</div><div style="font-size:12px;color:var(--text-muted);margin-top:3px;">논리적 역량 입증 완성</div></div>
          <div style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:16px;text-align:center;"><div style="font-size:26px;margin-bottom:6px;">🎨</div><div style="font-size:14px;font-weight:700;color:#fff;">템플릿 커스터마이징</div><div style="font-size:12px;color:var(--text-muted);margin-top:3px;">나만의 브랜드 완성</div></div>
          <div style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:12px;padding:16px;text-align:center;"><div style="font-size:26px;margin-bottom:6px;">🌐</div><div style="font-size:14px;font-weight:700;color:#fff;">노션 사이트 배포</div><div style="font-size:12px;color:var(--text-muted);margin-top:3px;">전문 URL 완성</div></div>
          <div style="background:rgba(255,224,102,0.1);border:1px solid rgba(255,224,102,0.3);border-radius:12px;padding:16px;text-align:center;"><div style="font-size:26px;margin-bottom:6px;">✅</div><div style="font-size:14px;font-weight:700;color:#ffe066;">QA 검수 완료</div><div style="font-size:12px;color:var(--text-muted);margin-top:3px;">제출 준비 완료!</div></div>
        </div>
      </div>
      <div class="slide-footer">
        <span>밀양청년 취업역량 강화교육 · 5주차 마무리 · 디지털 실무</span>
        <span class="slide-dynamic-badge"></span>
      </div>
    </div>

  </div>

  <!-- FLOATING UI -->
  <div class="progress-bar" id="progressBar"></div>
  <div class="nav-zone left" onclick="go(-1)"></div>
  <div class="nav-zone right" onclick="go(1)"></div>
  <div class="page-indicator" id="pageIndicator">1 / 17</div>
  <button class="help-btn" onclick="toggleHelp()" title="단축키 도움말 (?)">?</button>

  <!-- HELP MODAL -->
  <div class="help-modal" id="helpModal">
    <div class="help-content">
      <h3>⌨️ 키보드 단축키</h3>
      <ul class="help-list">
        <li><b>→ / Space / PgDown</b> 다음 슬라이드</li>
        <li><b>← / PgUp</b> 이전 슬라이드</li>
        <li><b>Home</b> 첫 번째 슬라이드</li>
        <li><b>End</b> 마지막 슬라이드</li>
        <li><b>? 또는 H</b> 이 도움말 열기/닫기</li>
        <li><b>Esc</b> 도움말 닫기</li>
        <li><b>F</b> 전체 화면 토글</li>
      </ul>
    </div>
  </div>

  <script>
    let current = 0;
    const slides = document.querySelectorAll('.slide');
    const total = slides.length;

    function goTo(idx) {
      if (idx < 0 || idx >= total) return;
      slides[current].classList.remove('active');
      current = idx;
      slides[current].classList.add('active');
      document.getElementById('progressBar').style.width = ((current+1)/total*100)+'%';
      document.getElementById('pageIndicator').innerText = (current+1)+' / '+total;
      if (slides[current].id === 'slideParrContainer') initParr();
      if (slides[current].id === 'slideEmbedContainer') initEmbed();
      if (slides[current].id === 'slideQaContainer') resetQa();
    }
    function go(dir) { goTo(current+dir); }

    function syncDynamicSlideNumbers() {
      const allSlides = document.querySelectorAll('.slide');
      const realTotal = allSlides.length;
      allSlides.forEach((slide, idx) => {
        const badge = slide.querySelector('.slide-number-badge');
        if (badge) badge.innerText = (idx+1);
        const footerSpans = slide.querySelectorAll('.slide-footer span');
        if (footerSpans && footerSpans.length > 1) footerSpans[footerSpans.length-1].innerText = 'Slide '+(idx+1)+' / '+realTotal;
      });
      const pInd = document.getElementById('pageIndicator');
      if (pInd) pInd.innerText = '1 / '+realTotal;
    }
    window.addEventListener('load', syncDynamicSlideNumbers);

    document.addEventListener('keydown', e => {
      if (e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){e.preventDefault();go(1);}
      else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(-1);}
      else if(e.key==='Home'){e.preventDefault();goTo(0);}
      else if(e.key==='End'){e.preventDefault();goTo(total-1);}
      else if(e.key==='?'||e.key==='h'||e.key==='H') toggleHelp();
      else if(e.key==='Escape') document.getElementById('helpModal').classList.remove('active');
      else if(e.key==='f'||e.key==='F') toggleFullscreen();
    });

    let touchStartX=0;
    document.addEventListener('touchstart', e=>{touchStartX=e.touches[0].clientX;},{passive:true});
    document.addEventListener('touchend', e=>{const diff=touchStartX-e.changedTouches[0].clientX;if(Math.abs(diff)>50) go(diff>0?1:-1);},{passive:true});

    function scaleSlide(){const s=Math.min(window.innerWidth/1280,window.innerHeight/720);document.getElementById('deckContainer').style.transform='scale('+s+')';}
    window.addEventListener('resize',scaleSlide);scaleSlide();

    function toggleHelp(){document.getElementById('helpModal').classList.toggle('active');}
    document.getElementById('helpModal').addEventListener('click',function(e){if(e.target===this)this.classList.remove('active');});

    function toggleFullscreen(){
      if(!document.fullscreenElement){document.documentElement.requestFullscreen().then(()=>document.body.classList.add('is-fullscreen')).catch(()=>{});}
      else{document.exitFullscreen().then(()=>document.body.classList.remove('is-fullscreen')).catch(()=>{});}
    }
    document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement)document.body.classList.remove('is-fullscreen');});

    document.getElementById('progressBar').style.width=(1/total*100)+'%';

    // PAR-R
    let parrStep=0;
    const parrData=[
      {badge:'P 단계 — [다음 ▶] 버튼으로 Action → Result → Retrospective 순서로 확인하세요',content:'<div style="color:var(--purple-light);font-size:12px;font-weight:700;margin-bottom:6px;">[ P · 문제 정의 ]</div><div style="color:var(--text-sub);margin-bottom:4px;">💼 프로젝트: SNS 콘텐츠 기획 인턴</div><div>기존 인스타그램 팔로워 증가율이 <b style="color:#ffe066;">월 평균 1.2%</b>에 그쳐 브랜드 인지도 확산에 한계. 콘텐츠 주제 분산과 업로드 일관성 부재가 핵심 원인으로 분석됨.</div>'},
      {badge:'A 단계 — 본인의 기여도와 설계 로직을 구체적으로 서술',content:'<div style="color:var(--purple-light);font-size:12px;font-weight:700;margin-bottom:6px;">[ A · 수행 행동 ]</div><div>주 3회 콘텐츠 캘린더 설계 및 직접 집행. <b style="color:#ffe066;">Figma로 고정 템플릿 3종</b> 제작 후 팀 공유. 경쟁 계정 10개 벤치마킹 후 핵심 해시태그 전략 수립 및 A/B 테스트 실행.</div>'},
      {badge:'R 단계 — 정량 지표로 성과를 명확히 증명',content:'<div style="color:var(--purple-light);font-size:12px;font-weight:700;margin-bottom:6px;">[ R · 결과 성과 ]</div><div>3개월 운영 후 팔로워 월 증가율 <b style="color:var(--cyan);">1.2% → 8.7%</b>로 626% 개선. 게시물 평균 저장 수 <b style="color:var(--cyan);">23건 → 187건</b>으로 상승. 팔로워 순증 +1,240명 달성.</div>'},
      {badge:'✅ PAR-R 완성! 4단계 모두 작성하면 역량이 명확하게 전달됩니다.',content:'<div style="color:var(--purple-light);font-size:12px;font-weight:700;margin-bottom:6px;">[ R · 회고 ]</div><div>초기 A/B 테스트 샘플 수가 적어 데이터 신뢰도가 낮았음. 다음 프로젝트에서는 <b style="color:#ffe066;">최소 4주 이상의 테스트 기간</b>을 확보하고 Google Analytics 연동으로 유입 경로까지 분석할 계획.</div>'}
    ];
    function initParr(){parrStep=0;renderParr();}
    function parrNext(){if(parrStep<3){parrStep++;renderParr();}}
    function parrPrev(){if(parrStep>0){parrStep--;renderParr();}}
    function parrReset(){parrStep=0;renderParr();}
    function renderParr(){
      for(let i=0;i<4;i++){const b=document.getElementById('parrBlock'+i);if(b){if(i===parrStep)b.classList.add('active');else b.classList.remove('active');}}
      const c=document.getElementById('parrExampleContent');const s=document.getElementById('parrStatusBadge');
      if(c)c.innerHTML=parrData[parrStep].content;if(s)s.innerText=parrData[parrStep].badge;
    }

    // EMBED
    let embedStep=0;
    const embedLabels=['Figma 임베드 완료 — [임베드 추가 ▶]로 다음 미디어 추가','YouTube 임베드 완료 — [임베드 추가 ▶]로 PDF 추가','PDF 임베드 완료 — [임베드 추가 ▶]로 이미지 갤러리 추가','🎉 모든 미디어 임베드 완료! 이제 방문자가 포트폴리오 내에서 작업물을 직접 확인할 수 있습니다.'];
    function initEmbed(){embedStep=0;renderEmbed();}
    function embedNext(){if(embedStep<3){embedStep++;renderEmbed();}}
    function embedPrev(){if(embedStep>0){embedStep--;renderEmbed();}}
    function embedReset(){embedStep=0;renderEmbed();}
    function renderEmbed(){
      for(let i=0;i<=3;i++){const b=document.getElementById('embedBox'+i);if(b){if(i<=embedStep)b.classList.add('active');else b.classList.remove('active');}}
      const s=document.getElementById('embedStatusBadge');if(s)s.innerText=embedLabels[embedStep];
    }

    // QA
    const qaChecked=[false,false,false,false,false,false,false];
    function resetQa(){for(let i=0;i<7;i++){qaChecked[i]=false;const r=document.getElementById('qa'+i);const c=document.getElementById('qaCheck'+i);if(r)r.classList.remove('checked');if(c)c.innerText='';} updateQaStatus();}
    function toggleQa(idx){
      qaChecked[idx]=!qaChecked[idx];
      const r=document.getElementById('qa'+idx);const c=document.getElementById('qaCheck'+idx);
      if(r){if(qaChecked[idx]){r.classList.add('checked');c.innerText='✓';}else{r.classList.remove('checked');c.innerText='';}}
      updateQaStatus();
    }
    function updateQaStatus(){
      const done=qaChecked.filter(Boolean).length;const b=document.getElementById('qaStatusBadge');
      if(b){if(done===7){b.style.background='rgba(52,211,153,0.15)';b.style.color='#34d399';b.innerText='🎉 QA 검수 완료! 이제 포트폴리오를 자신 있게 제출하세요!';}
      else{b.style.background='rgba(0,102,79,0.15)';b.style.color='var(--text-muted)';b.innerText='📋 항목을 클릭하여 체크하세요 — '+done+' / 7 완료';}}
    }
  </script>
</body>
</html>"""

with open('presentation.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done! presentation.html written successfully.')
