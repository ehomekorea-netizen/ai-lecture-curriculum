import { mergeConfigs, presetIcons } from 'unocss'
// @ts-expect-error Slidev exposes its UnoCSS base config without a standalone type declaration.
import config from '@slidev/client/uno.config'

const deckFontFamily = '"Nunito Variable", "Nunito", "Kiwi Maru", "Comfortaa Variable", "Comfortaa", "DM Sans Variant", "DM Sans", ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"'
const roundedFontFamily = '"Comfortaa Variable", "Comfortaa", "DM Sans Variant", "DM Sans", ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"'

export default mergeConfigs([
  config,
  {
    presets: [
      presetIcons({
        scale: 1.1,
      }),
    ],
    safelist: [
      'font-sans',
      'font-rounded',
      'font-mono',
      'i-carbon:arrow-right',
      'i-carbon:checkmark-filled',
      'i-carbon:flash',
      'i-carbon:task',
      'i-carbon:play',
      'i-carbon:target',
      'i-carbon:document-view',
      'i-mdi:github',
      'i-logos:slidev',
    ],
    theme: {
      fontFamily: {
        sans: deckFontFamily,
        rounded: roundedFontFamily,
      },
    },
  },
])
