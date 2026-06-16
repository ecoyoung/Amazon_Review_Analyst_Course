<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  variant?: 'paper' | 'ink' | 'cyan'
  eyebrow?: string
  index?: string
  name: string
  caption?: string
}>()

const animationData = ref<any>(null)
async function load(name: string) {
  animationData.value = null
  try {
    const r = await fetch(`/animations/${name}.json`)
    if (!r.ok) throw new Error(`HTTP ${r.status}`)
    animationData.value = await r.json()
  } catch (e) {
    console.error('lottie load failed', e)
  }
}
load(props.name)
watch(() => props.name, load)
</script>

<template>
  <div :class="['cinema', variant === 'ink' && 'cinema--ink', variant === 'cyan' && 'cinema--cyan']">
    <div v-if="eyebrow" class="cinema__eyebrow">{{ eyebrow }}</div>

    <div class="lottie-stage">
      <Vue3Lottie
        v-if="animationData"
        :animation-data="animationData"
        :loop="true"
        :auto-play="true"
        :height="360"
        :width="640"
      />
    </div>

    <div v-if="caption" class="lottie-stage__caption">{{ caption }}</div>
    <div v-if="index" class="cinema__index">{{ index }}</div>
  </div>
</template>
