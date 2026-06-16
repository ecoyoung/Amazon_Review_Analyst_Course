<script setup lang="ts">
const props = defineProps<{
  variant?: 'paper' | 'ink' | 'cyan'
  eyebrow?: string
  index?: string
  name: string
  caption?: string
}>()

import { ref, watch } from 'vue'
const animationData = ref<any>(null)
async function load(name: string) {
  animationData.value = null
  const r = await fetch(`/animations/${name}.json`)
  animationData.value = await r.json()
}
load(props.name)
watch(() => props.name, load)
</script>

<template>
  <div :class="['cinema', props.variant === 'ink' && 'cinema--ink', props.variant === 'cyan' && 'cinema--cyan']">
    <div v-if="eyebrow" class="cinema__eyebrow">{{ eyebrow }}</div>
    <div class="lottie-stage">
      <Vue3Lottie v-if="animationData" :animation-data="animationData" :loop="true" :auto-play="true" :height="'70%'" />
    </div>
    <div v-if="caption" class="cinema__sub" style="position: absolute; bottom: 88px; left: 0; right: 0;">
      {{ caption }}
    </div>
    <div v-if="index" class="cinema__index">{{ index }}</div>
  </div>
</template>
