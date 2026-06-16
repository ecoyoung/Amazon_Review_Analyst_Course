<script setup lang="ts">
const props = defineProps<{
  variant?: 'paper' | 'ink' | 'cyan'
  eyebrow?: string
  index?: string
}>()
</script>

<template>
  <div :class="['cinema', props.variant === 'ink' && 'cinema--ink', props.variant === 'cyan' && 'cinema--cyan']">
    <div v-if="props.eyebrow" class="cinema__eyebrow">{{ props.eyebrow }}</div>
    <div class="cinema__body cinema-enter" style="max-width: 1280px;">
      <blockquote class="cinema-quote">
        <slot />
      </blockquote>
    </div>
    <div v-if="props.index" class="cinema__index">{{ props.index }}</div>
  </div>
</template>
