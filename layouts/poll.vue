<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import QRCode from 'qrcode'

const props = defineProps<{
  // poll id, resolves to http://localhost:8000/p/vote.html?id=<id>
  poll: string
  variant?: 'paper' | 'ink'
  eyebrow?: string
  // Optional explicit URL override (e.g. for LAN IP during real training)
  url?: string
  index?: string
}>()

const dataUrl = ref('')
const targetUrl = computed(() => {
  if (props.url) return props.url
  return `http://localhost:8000/p/vote.html?id=${props.poll}`
})

onMounted(async () => {
  dataUrl.value = await QRCode.toDataURL(targetUrl.value, {
    margin: 1,
    width: 320,
    color: { dark: '#0B1B2B', light: '#FFFFFF' },
  })
})
</script>

<template>
  <div :class="['cinema', variant === 'ink' && 'cinema--ink']">
    <div v-if="eyebrow" class="cinema__eyebrow">{{ eyebrow }}</div>
    <div v-if="index" class="cinema__index">{{ index }}</div>
    <div class="cinema__body" style="width: 100%;">
      <div class="poll">
        <div class="poll__qr">
          <img v-if="dataUrl" :src="dataUrl" alt="扫码参与投票" />
        </div>
        <div>
          <div class="poll__prompt"><slot /></div>
          <div class="poll__hint">扫码参与 · 实时投票</div>
        </div>
      </div>
    </div>
  </div>
</template>
