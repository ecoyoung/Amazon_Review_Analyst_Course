<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  variant?: 'paper' | 'ink' | 'cyan'
  eyebrow?: string
  index?: string
}>()

const cls = computed(() => [
  'cinema',
  props.variant === 'ink' && 'cinema--ink',
  props.variant === 'cyan' && 'cinema--cyan',
])
</script>

<template>
  <div :class="cls">
    <div v-if="eyebrow" class="cinema__eyebrow">{{ eyebrow }}</div>
    <div class="cinema__body cinema-enter">
      <slot />
    </div>
    <SessionTimer />
    <div v-if="index" class="cinema__index">{{ index }}</div>
  </div>
</template>
