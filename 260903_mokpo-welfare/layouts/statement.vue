<template>
  <div class="slidev-layout statement-layout flex items-center justify-center text-center h-full w-full select-none p-12 bg-[#FAF8F4]">
    <!-- Pure Center Statement (Zero Clutter) -->
    <div class="statement-content max-w-4xl px-4 flex flex-col items-center justify-center">
      <slot />
    </div>
  </div>
</template>

<style>
/* ── Pure Statement Layout Typography ── */
.statement-layout h1 {
  font-family: 'Source Serif 4', Georgia, serif !important;
  font-size: 3.6rem !important;
  line-height: 1.3 !important;
  letter-spacing: -0.03em !important;
  font-weight: 700 !important;
  color: #1e293b !important;
  margin: 0 auto !important;
  text-align: center !important;
}

.statement-layout br {
  display: block;
  content: "";
  margin-top: 0.5rem;
}
</style>
