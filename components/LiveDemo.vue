<script setup lang="ts">
import { ref, onMounted } from 'vue'

const props = withDefaults(defineProps<{
  src: string
  title?: string
  height?: string
}>(), {
  height: '520px',
})

const loading = ref(true)

onMounted(() => {
  // Give the iframe a moment to start loading; the load event fires on completion.
  setTimeout(() => {
    // If the iframe never fires `load` (e.g., server is down), drop the spinner
    // after 8s so the user sees the broken-state message rather than an infinite loader.
    loading.value = false
  }, 8000)
})

function onLoad() {
  loading.value = false
}
</script>

<template>
  <div class="live-demo">
    <div class="live-demo-header">
      <span class="live-demo-dot" />
      <span class="live-demo-title">{{ title ?? src }}</span>
    </div>
    <div class="live-demo-frame" :style="{ height }">
      <div v-if="loading" class="live-demo-loading">
        <div class="spinner" />
        <div>正在加载实时演示…</div>
        <div class="text-sm opacity-70 mt-2">
          如果超过 8 秒还没出现，请确认 <code>{{ src }}</code> 服务已在运行。
        </div>
      </div>
      <iframe
        :src="src"
        :title="title ?? 'Live demo'"
        @load="onLoad"
        allow="clipboard-read; clipboard-write"
      />
    </div>
  </div>
</template>

<style scoped>
.live-demo {
  display: flex;
  flex-direction: column;
  gap: 0;
  margin: 8px 0;
  border: 1px solid rgba(0, 174, 239, 0.32);
  border-radius: 14px;
  overflow: hidden;
}
.live-demo-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  background: #00aeef;
  color: white;
  font-weight: 600;
  font-size: 13px;
}
.live-demo-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ff5252;
  box-shadow: 0 0 0 0 rgba(255, 82, 82, 0.6);
  animation: pulse 1.5s infinite;
}
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(255, 82, 82, 0.6); }
  70% { box-shadow: 0 0 0 10px rgba(255, 82, 82, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 82, 82, 0); }
}
.live-demo-frame {
  position: relative;
  background: #f7fbff;
}
.live-demo-frame iframe {
  width: 100%;
  height: 100%;
  border: 0;
  background: white;
}
.live-demo-loading {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.92);
  color: #5a6b7b;
  z-index: 2;
}
.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(0, 174, 239, 0.2);
  border-top-color: #00aeef;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 12px;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
