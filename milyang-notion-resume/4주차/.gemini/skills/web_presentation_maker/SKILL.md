---
name: web_presentation_maker
description: Generates standalone 16:9 HTML presentation decks with responsive auto-scaling, slide navigation, keyboard shortcuts, print/PDF layout support, helper modal, image search recommendations, and Google Drive upload delivery. Use when the user asks to create an HTML presentation, web slide deck, presentation web page, or HTML 교안.
---

# Web Presentation Maker Skill (Project-Scoped)

Generates professional, standalone 16:9 single-file HTML presentation decks with built-in slide navigation, responsive auto-scaling, print/PDF support, and shortcut help modal UI. Uploads/delivers the HTML presentation and provides a structured slide-by-slide Image Search & Rename Guide.

## When to Use

- Creating web-based slide decks, HTML 교안, or interactive presentations in a single HTML file.
- Converting text drafts, outlines, or lecture content into structured presentation slides.
- Designing responsive, interactive 16:9 slides with print/PDF export support.

---

## Key Features & Specifications

### 1. Default Layout Policy: Text & Card First (Clean & Readable)
- **Default Mode**: By default, generate clean, beautifully structured **Text & Card Component Layouts** without forcing empty image frames.
- **Optional Image Mode**: Only embed image frame components (`<img>` tags) when the user explicitly requests images or visual placeholders in slides.

### 2. Standardized `images/` Subfolder & Simple Number Mapping
To streamline local image management and clean workspace organization:
- **Standard Folder Structure**: Recommend storing slide photos in the `images/` subfolder (`images/1.jpg`, `images/2.jpg`, etc.).
- **Slide-by-Slide Search Guide**: For slides where images would be helpful, generate a structured **Image Search & Rename Guide (추천 검색어 - 한글 & 영문)** in the chat response.
- **Robust Path Fallback in HTML**: When image frames are included, HTML `<img>` tags MUST feature JS `onerror` fallbacks prioritising `images/` subfolder paths, extension variations, and Windows double-extensions:
  ```html
  <img src="images/1.jpg" onerror="if(!this.t1){this.t1=true;this.src='images/1.png';}else if(!this.t2){this.t2=true;this.src='images/1.jpg.jpg';}else if(!this.t3){this.t3=true;this.src='1.jpg';}else if(!this.t4){this.t4=true;this.src='1.png';}" alt="Slide 1 Image">
  ```

### 3. Subtitle & Educational Context Principle (No Direct Operational CTA in Subtitles)
- **Meaningful Educational Context Policy**: The `<p>` subtitle tag underneath `<h2>` slide titles MUST state the **core educational value, domain insight, or key takeaway** of the slide.
- **NEVER Use Direct UI/Operational Instructions as Subtitles**: Avoid writing operational CTA prompts like *"Click the box to see..."*, *"Press the button below..."*, or *"Select the option..."* in slide header subtitles `<p>`. Reserve interactive guides for card footnotes or status badges.

### 4. Dynamic Slide Numbering & Total Counter Engine
To prevent slide number mismatch, broken footers, or hardcoded index drift when adding or deleting slides:
- **Automatic Dynamic Re-numbering Engine**: In JavaScript, dynamically query `querySelectorAll('.slide')` and update all `.slide-number-badge`, footer `Slide X / Y` spans, and `#pageIndicator` counts on load (`syncDynamicSlideNumbers()`).
- **Dynamic JavaScript Formula**:
  ```javascript
  function syncDynamicSlideNumbers() {
    const allSlides = document.querySelectorAll('.slide');
    const realTotal = allSlides.length;
    allSlides.forEach((slide, idx) => {
      const badge = slide.querySelector('.slide-number-badge');
      if (badge) badge.innerText = (idx + 1);
      const footerSpans = slide.querySelectorAll('.slide-footer span');
      if (footerSpans && footerSpans.length > 1) {
        footerSpans[footerSpans.length - 1].innerText = `Slide ${idx + 1} / ${realTotal}`;
      }
    });
    const pInd = document.getElementById('pageIndicator');
    if (pInd) pInd.innerText = `1 / ${realTotal}`;
  }
  window.addEventListener('load', syncDynamicSlideNumbers);
  ```

### 4-1. ⚠️ 슬라이드 애니메이션 트리거: 하드코딩 인덱스 절대 금지
슬라이드가 추가·삭제되면 DOM 순서(인덱스)가 밀리므로, `goTo()` 함수 안에서 특정 슬라이드의 애니메이션을 실행할 때 **절대로 하드코딩 숫자 인덱스를 사용하지 말 것**.

```javascript
// ❌ 절대 금지 — 슬라이드 추가 시 인덱스가 밀려서 애니메이션이 영원히 실행 안 됨
if (current === 37) runSlide38Animation();

// ✅ 반드시 이렇게 — ID 기반 체크로 DOM 위치와 무관하게 항상 정확히 매칭
if (slides[current] && slides[current].id === 'slide38Container') runSlide38Animation();
```

**적용 대상**: `goTo()` 내 모든 슬라이드별 애니메이션/시뮬레이터 트리거 조건문.
**위반 시 증상**: 해당 슬라이드로 이동해도 콘텐츠가 `opacity: 0` 상태로 남아 화면이 텅 비어 보임.
**근본 원리**: 슬라이드에 고유 `id` 속성(예: `id="slide38Container"`)을 부여하고, `slides[current].id === '...'`로 체크하면 슬라이드가 몇 개 추가·삭제되어도 항상 올바른 슬라이드에서 애니메이션이 실행됨.

### 5. YouTube & External Video Frame Embedding
- **Video Slide Support**: Support responsive 16:9 YouTube video player frames (`<iframe>`) inside slides when video links/IDs or video embed codes are provided.
- **Auto-Scaling Video Container**: Keep YouTube player containers sized properly within the 1280x720 canvas bounds with `width: 100%; height: 400px; border-radius: 14px; overflow: hidden;`.
- **Local File Policy Note**: Omit `referrerpolicy="strict-origin-when-cross-origin"` to avoid YouTube Error 153 when opening HTML directly via `file://` protocol.

### 6. 16:9 Responsive Auto-scaling
- Fixed `.deck` container canvas sized at `1280px` x `720px`.
- Centered on screen with flexible dynamic CSS scaling using `transform: scale(s)` where:
  $$\text{scale } s = \min\left(\frac{\text{window.innerWidth}}{1280}, \frac{\text{window.innerHeight}}{720}\right)$$
- Automatically recalculates on window `resize` events.

### 7. Navigation Engine
- Active slide switching managed via JavaScript `goTo(index)` function.
- CSS transitions for smooth sliding fade effects (`translateX` and `opacity`).
- Multi-input support:
  - **Keyboard**: `ArrowRight`, `ArrowLeft`, `Space`, `PageDown`, `PageUp`, `Home`, `End`.
  - **Mouse**: Invisible left/right click hover zones (`.nav-zone.left`, `.nav-zone.right`).
  - **Mobile Touch**: Touch swipe distance detection (`touchstart`, `touchend`).

### 8. Floating UI Controls & Helper Modal
- Bottom progress bar (`#progressBar`) showing completion percentage.
- Bottom-right page indicator (`#pageIndicator`, dynamically rendered).
- Bottom-right help button (`.help-btn` with `?` icon) opening a popup modal (`#helpModal`).
- Modal trigger shortcuts: `?` or `H` key to open/close, `Esc` to close.

### 9. Print & PDF Layout (`@media print`)
- Hides interactive floating UI overlays (`.progress-bar`, `.page-indicator`, `.nav-zone`, `.help-btn`, `.help-modal`).
- Disables `transform: scale()` and forces `page-break-after: always` per slide for standard 16:9 landscape printing.

---

## Slide Component Palette

- **Title Slide**: `.title-kicker`, `.title-main`, `.title-sub`, `.title-tags`.
- **Comparison Block**: `.fail-row` with `.fail-col.bad` and `.fail-col.good`.
- **KPI Metrics Row**: `.kpi-row` with `.kpi` cards.
- **Hero Grid**: `.grid-hero` with content columns and optional `.img-frame`.
- **Callout Notes**: `.info-block` and `.ai-note` with `gold`, `warn`, or default theme accents.
- **Summary Table**: `.summary-table` for key structured data.

---

## Execution Workflow & Output Deliverables

1. **Extract Narrative Beats**: Parse the user's content into structured slides.
2. **Apply Text-First Default Layout**: Build a clean 16:9 HTML presentation focused on readability and sleek card UI.
3. **Embed Dynamic Slide Numbering Engine**: Ensure all badges and total count indicators are automatically updated via JavaScript.
4. **Deliver Image Search & Rename Guide**:
   In the final response to the user, include a clear table detailing image recommendations.
