import { createExternalPackageIconLoader } from '@iconify/utils/lib/loader/external-pkg'
// @ts-expect-error - Ignoring missing types for slidev uno config
import config from '@slidev/client/uno.config'
import { mergeConfigs, presetIcons } from 'unocss'

const cuteFontFamily = '"Nunito Variable", "Nunito", "Pretendard", "ChillRoundM", "Kiwi Maru", "Comfortaa Variable", "Comfortaa", "DM Sans Variant", "DM Sans", ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"'
const roundedFontFamily = '"Comfortaa Variable", "Comfortaa", "Pretendard", "DM Sans Variant", "DM Sans", ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"'
const monoFontFamily = '"Fira Code", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace'

export default mergeConfigs([
  config,
  {
    rules: [
      ['font-math', { 'font-family': 'Latin Modern Roman, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif' }],
      ['font-cover', { 'font-family': `${roundedFontFamily} !important` }],
      ['font-mono', { 'font-family': `${monoFontFamily} !important` }],
      ['glass-border', { 'border': '1px solid rgb(255 255 255 / 12%)' }],
      ['glass-border-light', { 'border': '1px solid rgb(0 0 0 / 8%)' }],
    ],
    safelist: [
      'font-sans',
      'font-cover',
      'font-cute',
      'font-mono',
      'i-carbon:idea',
      'i-carbon:tools',
      'i-carbon:chip',
      'i-carbon:network-4',
      'i-carbon:rocket',
      'i-carbon:checkmark-filled',
      'i-carbon:warning-filled',
      'i-ri:github-fill',
      'i-ri:twitter-x-fill',
      ...Array.from({ length: 30 }, (_, i) => `delay-${(i + 1) * 100}`),
    ],
    presets: [
      presetIcons({
        collections: {
          ...createExternalPackageIconLoader('@proj-airi/lobe-icons'),
        },
      }),
    ],
    theme: {
      fontFamily: {
        sans: cuteFontFamily,
        cute: cuteFontFamily,
        rounded: roundedFontFamily,
        cover: roundedFontFamily,
        mono: monoFontFamily,
      },
    },
  },
])
