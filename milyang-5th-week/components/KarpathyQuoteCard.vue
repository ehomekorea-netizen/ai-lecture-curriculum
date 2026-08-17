<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    src?: string
  }>(),
  {
    src: '/img/karpathy-vibe-quote.png'
  }
)
</script>

<template>
  <div class="karpathy-quote-wrapper w-full h-[315px] flex items-center justify-center">
    <div class="card-frame relative h-[315px] rounded-2xl overflow-hidden shadow-xl border border-slate-200/90 bg-white transition-transform hover:scale-[1.02] duration-300 flex items-center justify-center">
      <img
        :src="props.src"
        alt="가장 핫한 개발 언어는 영어다 - Andrej Karpathy"
        class="h-full w-auto object-contain select-none"
      />
    </div>
  </div>
</template>

<style scoped>
.card-frame {
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
}
</style>
