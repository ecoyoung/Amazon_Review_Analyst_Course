<script setup lang="ts">
import { ref, onMounted } from 'vue'
import QRCode from 'qrcode'

const props = defineProps<{
  url: string
  variant?: 'paper' | 'ink'
  eyebrow?: string
}>()

const dataUrl = ref('')
onMounted(async () => {
  dataUrl.value = await QRCode.toDataURL(props.url, {
    margin: 1,
    width: 320,
    color: { dark: '#0B1B2B', light: '#FFFFFF' },
  })
})
</script>

<template>
  <div :class="['cinema', variant === 'ink' && 'cinema--ink']">
    <div v-if="eyebrow" class="cinema__eyebrow">{{ eyebrow }}</div>
    <div class="cinema__body" style="width: 100%;">
      <div class="poll">
        <div class="poll__qr">
          <img v-if="dataUrl" :src="dataUrl" alt="Scan to vote" />
        </div>
        <div>
          <div class="poll__prompt"><slot /></div>
          <div class="poll__hint">扫码参与 · 实时投票</div>
        </div>
      </div>
    </div>
  </div>
</template>
