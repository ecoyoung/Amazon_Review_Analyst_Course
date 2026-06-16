<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  name: string
  caption?: string
  height?: string
}>()

const animationData = ref<any>(null)
const loadError = ref<string | null>(null)
const containerHeight = props.height ?? '320px'

async function loadAnimation(name: string) {
  animationData.value = null
  loadError.value = null
  try {
    // Files in public/ are served at root in dev and build; fetch them as URLs.
    const res = await fetch(`/animations/${name}.json`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    animationData.value = await res.json()
  } catch (err: any) {
    loadError.value = err?.message ?? String(err)
  }
}

loadAnimation(props.name)
watch(() => props.name, (n) => loadAnimation(n))
</script>

<template>
  <div class="lottie-frame">
    <div class="lottie-canvas" :style="{ height: containerHeight }">
      <Vue3Lottie
        v-if="animationData"
        :animation-data="animationData"
        :loop="true"
        :auto-play="true"
        :height="containerHeight"
      />
      <div v-else-if="loadError" class="lottie-missing">
        ⚠️ Failed to load <code>{{ name }}.json</code>
        <br />
        <span class="text-sm opacity-70">{{ loadError }}</span>
      </div>
      <div v-else class="lottie-missing">
        <div class="spinner" />
        Loading animation…
      </div>
    </div>
    <div v-if="caption" class="lottie-caption">{{ caption }}</div>
  </div>
</template>

<style scoped>
.lottie-frame {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  margin: 12px 0;
}
.lottie-canvas {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, #f7fbff 0%, #ffffff 100%);
  border: 1px solid rgba(0, 174, 239, 0.18);
  border-radius: 16px;
  padding: 12px;
}
.lottie-missing {
  font-size: 14px;
  text-align: center;
  color: #5a6b7b;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.spinner {
  width: 24px;
  height: 24px;
  border: 2px solid rgba(0, 174, 239, 0.2);
  border-top-color: #00aeef;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.lottie-caption {
  font-size: 13px;
  color: #5a6b7b;
  font-style: italic;
}
</style>
