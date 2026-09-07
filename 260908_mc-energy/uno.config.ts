import { createExternalPackageIconLoader } from '@iconify/utils/lib/loader/external-pkg'
// @ts-expect-error - Ignoring missing types for uno config
import config from '@slidev/client/uno.config'
import { mergeConfigs, presetAttributify, presetIcons, presetWebFonts, presetWind3 } from 'unocss'

export default mergeConfigs([
  config,
  {
    rules: [
      ['font-math', { 'font-family': 'Latin Modern Roman, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif' }],
    ],
    theme: {
      fontSize: {
        xs: ['0.875rem', { lineHeight: '1.32rem' }],
        sm: ['1.02rem', { lineHeight: '1.45rem' }],
        base: ['1.15rem', { lineHeight: '1.6rem' }],
        lg: ['1.28rem', { lineHeight: '1.75rem' }],
        xl: ['1.42rem', { lineHeight: '1.9rem' }],
        '2xl': ['1.75rem', { lineHeight: '2.2rem' }],
        '3xl': ['2.15rem', { lineHeight: '2.5rem' }],
        '4xl': ['2.65rem', { lineHeight: '2.9rem' }],
      },
    },
    safelist: [
      ...Array.from({ length: 30 }, (_, i) => `delay-${(i + 1) * 100}`),
    ],
    presets: [
      presetWind3({
        dark: 'class',
      }),
      presetAttributify(),
      presetIcons({
        collections: {
          ...createExternalPackageIconLoader('@proj-airi/lobe-icons'),
        },
      }),
      presetWebFonts({
        fonts: {
          sans: 'Pretendard, DM Sans, Noto Sans KR, sans-serif',
          mono: 'JetBrains Mono, Fira Code, monospace',
        },
        timeouts: {
          failure: 30000,
          warning: 30000,
        },
      }),
    ],
  },
])
