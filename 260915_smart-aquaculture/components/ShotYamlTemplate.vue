<script setup lang="ts">
import { ref } from 'vue'

const copied = ref(false)

const yamlCode = `# 스마트수산업 숏폼 S01 쇼트 규격서
shot_id: S01
duration_seconds: 4
purpose: "첫 3초의 낯선 질문을 시각적으로 제시"
subject: "스마트 양식장 수조와 수질 센서 하우징"
action: "카메라가 수조 가장자리에서 센서와 물고기를 향해 천천히 전진"
camera: "medium wide shot, slow push-in, stable movement"
environment: "clean indoor recirculating aquaculture facility"
lighting: "cool daylight mixed with soft reflections on water"
style: "documentary realism, premium educational short-form"
continuity: "same blue-and-silver palette, no new people"
caption_after_edit: "양식장인데, 물을 계속 바꾸지 않는다고요?"`

const copyCode = () => {
  navigator.clipboard.writeText(yamlCode)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<template>
  <div class="w-full my-1 grid grid-cols-[1.15fr_1fr] gap-4 items-start text-xs">
    <!-- Left: Sleek Code Box -->
    <div class="rounded-2xl bg-black/70 border border-white/20 p-3.5 shadow-xl flex flex-col justify-between">
      <div class="flex items-center justify-between border-b border-white/10 pb-1.5 mb-2">
        <div class="flex items-center gap-1.5 font-mono text-[11px] text-sky-400 font-bold">
          <span class="i-carbon-document-yaml text-base"></span>
          <span>s01_shot_spec.yaml</span>
        </div>
        <button
          @click="copyCode"
          class="px-2 py-0.5 rounded text-[10px] bg-white/10 hover:bg-white/20 text-white flex items-center gap-1 transition-all cursor-pointer border border-white/15"
        >
          <span :class="copied ? 'i-carbon-checkmark text-emerald-400' : 'i-carbon-copy'"></span>
          <span>{{ copied ? '복사됨!' : 'YAML 복사' }}</span>
        </button>
      </div>

      <div class="font-mono text-[10.5px] leading-relaxed text-white/90 space-y-0.5">
        <div class="text-white/40 italic"># 스마트수산업 숏폼 S01 쇼트 규격서</div>
        <div><span class="text-sky-300 font-bold">shot_id:</span> <span class="text-amber-300">S01</span></div>
        <div><span class="text-sky-300 font-bold">duration_seconds:</span> <span class="text-amber-300">4</span></div>
        <div><span class="text-sky-300 font-bold">purpose:</span> <span class="text-emerald-300">"첫 3초의 낯선 질문을 시각적으로 제시"</span></div>
        <div><span class="text-sky-300 font-bold">subject:</span> <span class="text-emerald-300">"스마트 양식장 수조와 수질 센서 하우징"</span></div>
        <div><span class="text-sky-300 font-bold">action:</span> <span class="text-emerald-300">"수조에서 센서를 향해 천천히 전진"</span></div>
        <div><span class="text-sky-300 font-bold">camera:</span> <span class="text-emerald-300">"medium wide shot, slow push-in"</span></div>
        <div><span class="text-sky-300 font-bold">environment:</span> <span class="text-emerald-300">"clean indoor recirculating facility"</span></div>
        <div><span class="text-sky-300 font-bold">lighting:</span> <span class="text-emerald-300">"cool daylight with water reflection"</span></div>
        <div><span class="text-sky-300 font-bold">continuity:</span> <span class="text-emerald-300">"same blue-and-silver palette"</span></div>
        <div><span class="text-sky-300 font-bold">caption_after_edit:</span> <span class="text-teal-300">"양식장인데 물을 안 바꾼다?"</span></div>
      </div>
    </div>

    <!-- Right: Explanatory Cards -->
    <div class="flex flex-col gap-2.5">
      <div class="p-3 bg-sky-950/40 rounded-xl border border-sky-500/30 shadow-lg">
        <div class="text-sky-300 font-bold text-xs mb-1 flex items-center gap-1.5">
          <span class="i-carbon-checkmark-filled text-sm"></span>
          <span>항목별 정리의 이점</span>
        </div>
        <p class="text-white/85 text-[11px] leading-relaxed m-0">
          줄글로 길게 설명하지 않고 항목별로 나누어 적으면, AI가 엉뚱한 요소를 멋대로 추가하거나 누락하는 일을 방지합니다.
        </p>
      </div>

      <div class="p-3 bg-amber-950/40 rounded-xl border border-amber-500/30 shadow-lg">
        <div class="text-amber-300 font-bold text-xs mb-1 flex items-center gap-1.5">
          <span class="i-carbon-rule text-sm"></span>
          <span>연속성(Continuity) 메모 필수</span>
        </div>
        <p class="text-white/85 text-[11px] leading-relaxed m-0">
          다음 컷으로 넘어갈 때 배관 색상이나 조명 색감이 갑자기 바뀌지 않도록 <strong class="text-amber-200">'동일한 파란색 배관'</strong>처럼 고정 문구를 적어둡니다.
        </p>
      </div>

      <div class="p-2.5 bg-black/40 rounded-xl border border-white/10 flex items-start gap-1.5 text-[10.5px]">
        <span class="i-carbon-idea text-teal-400 text-sm flex-shrink-0 mt-0.5"></span>
        <span class="text-teal-200 leading-snug">
          <strong>현장 팁:</strong> 프롬프트뿐 아니라 <strong>'나중에 넣을 자막(caption)'</strong>을 함께 적어두면 영상 생성과 편집이 한 번에 이어집니다.
        </span>
      </div>
    </div>
  </div>
</template>