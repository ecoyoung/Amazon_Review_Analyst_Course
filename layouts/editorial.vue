<script setup lang="ts">
const props = defineProps<{
  module?: string
  page?: string
}>()
</script>

<template>
  <div class="editorial">
    <div class="editorial__masthead">
      <span class="left"><BrandLogo /><span>{{ module ?? 'Consumer Insights' }}</span></span>
      <span class="right">{{ page }}</span>
    </div>
    <slot />
    <SessionTimer />
  </div>
</template>
