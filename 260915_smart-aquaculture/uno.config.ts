// @ts-expect-error - Ignoring missing types for slidev client config
import config from '@slidev/client/uno.config'
import { mergeConfigs, presetAttributify, presetIcons, presetUno, presetWebFonts } from 'unocss'

const koreanFontFamily = '"Pretendard", "Noto Sans KR", -apple-system, BlinkMacSystemFont, system-ui, Roboto, "Helvetica Neue", "Segoe UI", sans-serif'

export default mergeConfigs([
  config,
  {
    presets: [
      presetUno(),
      presetAttributify(),
      presetIcons({
        scale: 1.2,
        warn: true,
      }),
      presetWebFonts({
        fonts: {
          sans: 'Inter:400,600,800',
          mono: 'Fira Code',
        },
      }),
    ],
    rules: [
      ['font-kr', { 'font-family': koreanFontFamily }],
    ],
    shortcuts: {
      'glass-card': 'bg-white/5 border border-white/10 backdrop-blur-md rounded-xl p-5 transition-all duration-300 hover:border-white/20',
      'hero-badge': 'inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-white/10 text-white/90 border border-white/15',
      'stage-title': 'text-3xl font-extrabold tracking-tight text-white mb-1',
      'stage-subtitle': 'text-sm text-white/70 font-normal',
    },
    theme: {
      fontFamily: {
        sans: koreanFontFamily,
        kr: koreanFontFamily,
      },
    },
  },
])
