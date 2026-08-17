<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  device?: 'macbook' | 'iphone' | 'browser'
  title?: string
  url?: string
  image?: string
  width?: string
  height?: string
  dark?: boolean
}>(), {
  device: 'macbook',
  title: 'Portfolio Preview',
  url: 'https://my-vibe-portfolio.netlify.app',
  dark: false
})
</script>

<template>
  <div class="devframe-container" :class="[device, { dark }]">
    <!-- MacBook Frame -->
    <div v-if="device === 'macbook'" class="macbook-frame">
      <div class="macbook-topbar">
        <div class="traffic-lights">
          <span class="light red"></span>
          <span class="light yellow"></span>
          <span class="light green"></span>
        </div>
        <div class="macbook-url-bar">
          <span class="lock-icon">🔒</span>
          <span class="url-text">{{ url }}</span>
        </div>
        <div class="topbar-actions">
          <span class="action-btn">⋯</span>
        </div>
      </div>
      <div class="macbook-screen">
        <img v-if="image" :src="image" :alt="title" class="screen-img" />
        <slot v-else />
      </div>
      <div class="macbook-notch"></div>
      <div class="macbook-bottom-lip"></div>
    </div>

    <!-- iPhone Frame -->
    <div v-else-if="device === 'iphone'" class="iphone-frame">
      <div class="iphone-island">
        <div class="island-camera"></div>
      </div>
      <div class="iphone-screen">
        <img v-if="image" :src="image" :alt="title" class="screen-img" />
        <slot v-else />
      </div>
      <div class="iphone-bar"></div>
    </div>

    <!-- Clean Browser Frame -->
    <div v-else class="browser-frame">
      <div class="browser-header">
        <div class="traffic-lights">
          <span class="light red"></span>
          <span class="light yellow"></span>
          <span class="light green"></span>
        </div>
        <div class="browser-tab">{{ title }}</div>
        <div class="browser-url-input">{{ url }}</div>
      </div>
      <div class="browser-viewport">
        <img v-if="image" :src="image" :alt="title" class="screen-img" />
        <slot v-else />
      </div>
    </div>
  </div>
</template>

<style scoped>
.devframe-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0.5rem auto;
  max-width: 100%;
}

/* ── MacBook ── */
.macbook-frame {
  width: 100%;
  max-width: 580px;
  background: #1e1e24;
  border-radius: 12px 12px 0 0;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.22), 0 2px 6px rgba(0,0,0,0.1);
  border: 2.5px solid #2f2f38;
  overflow: hidden;
  position: relative;
}

.macbook-topbar {
  background: #2a2a35;
  height: 28px;
  display: flex;
  align-items: center;
  padding: 0 10px;
  gap: 10px;
  border-bottom: 1px solid #383846;
}

.traffic-lights {
  display: flex;
  gap: 6px;
}
.light {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}
.light.red { background: #FF5F56; }
.light.yellow { background: #FFBD2E; }
.light.green { background: #27C93F; }

.macbook-url-bar {
  flex: 1;
  background: #1b1b22;
  border-radius: 6px;
  height: 19px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 0 8px;
  font-size: 0.68rem;
  color: #9da5b4;
  font-family: 'Geist Mono', monospace;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.lock-icon { font-size: 0.6rem; opacity: 0.7; }
.topbar-actions { font-size: 0.8rem; color: #78788c; }

.macbook-screen {
  background: #0f1015;
  min-height: 240px;
  max-height: 300px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.screen-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.macbook-bottom-lip {
  height: 10px;
  background: linear-gradient(180deg, #d2d2d8 0%, #b5b5bc 100%);
  border-radius: 0 0 14px 14px;
  margin: 0 -12px -2px -12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}

/* ── iPhone ── */
.iphone-frame {
  width: 240px;
  height: 360px;
  background: #0f1015;
  border-radius: 36px;
  border: 4px solid #3a3b45;
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.28);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.iphone-island {
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  width: 72px;
  height: 18px;
  background: #000;
  border-radius: 12px;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
}
.island-camera {
  width: 7px;
  height: 7px;
  background: #111a36;
  border-radius: 50%;
}

.iphone-screen {
  flex: 1;
  background: #181920;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 14px;
}

.iphone-bar {
  position: absolute;
  bottom: 6px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: #ffffff;
  opacity: 0.6;
  border-radius: 4px;
  z-index: 10;
}

/* ── Browser Frame ── */
.browser-frame {
  width: 100%;
  background: #fff;
  border: 1.5px solid #E7E0D4;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.06);
  overflow: hidden;
}

.browser-header {
  background: #FAF8F4;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  border-bottom: 1px solid #E7E0D4;
}

.browser-tab {
  font-size: 0.72rem;
  font-weight: 700;
  background: #fff;
  padding: 3px 10px;
  border-radius: 6px;
  border: 1px solid #E7E0D4;
  color: #2B2620;
}

.browser-url-input {
  flex: 1;
  background: #fff;
  border: 1px solid #E7E0D4;
  border-radius: 6px;
  padding: 3px 10px;
  font-size: 0.72rem;
  font-family: 'Geist Mono', monospace;
  color: #476BFF;
}

.browser-viewport {
  min-height: 220px;
  background: #FAF8F4;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
