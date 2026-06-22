<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { showEditor } from '@slidev/client/state/index.ts'

const STORAGE_KEY = 'amazon-review-insight-course-started-at'
const TARGET_MINUTES = 60
const SLIDEV_FLOATING_SELECTORS = [
  '#slidev-goto-dialog',
  '#slidev-goto-input',
  '.autocomplete-list',
  'nav:has(button[title="Show slide overview"])',
  'div:has(> button[title="Draw with stylus"])',
  '.slidev-toc',
  '.slidev-outline',
  '.slidev-sidebar',
  '.slidev-drawer',
  '.slidev-menu',
]

const now = ref(Date.now())
const startedAt = ref<number | null>(null)
let timer: number | undefined
let observer: MutationObserver | undefined

function readStart() {
  const raw = window.localStorage.getItem(STORAGE_KEY)
  const parsed = raw ? Number(raw) : NaN
  if (Number.isFinite(parsed) && parsed > 0) {
    startedAt.value = parsed
    return
  }
  reset()
}

function reset() {
  const next = Date.now()
  window.localStorage.setItem(STORAGE_KEY, String(next))
  startedAt.value = next
  now.value = next
}

const elapsedSeconds = computed(() => {
  if (!startedAt.value) return 0
  return Math.max(0, Math.floor((now.value - startedAt.value) / 1000))
})

const elapsedLabel = computed(() => {
  const minutes = Math.floor(elapsedSeconds.value / 60)
  const seconds = elapsedSeconds.value % 60
  return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`
})

const progressPct = computed(() => {
  return Math.min(100, (elapsedSeconds.value / (TARGET_MINUTES * 60)) * 100)
})

onMounted(() => {
  readStart()
  suppressSlidevFloatingUi()
  timer = window.setInterval(() => {
    now.value = Date.now()
  }, 1000)
  observer = new MutationObserver(suppressSlidevFloatingUi)
  observer.observe(document.body, { childList: true, subtree: true })
  window.addEventListener('keydown', onKeydown, true)
})

onBeforeUnmount(() => {
  if (timer) window.clearInterval(timer)
  observer?.disconnect()
  window.removeEventListener('keydown', onKeydown, true)
})

function onKeydown(event: KeyboardEvent) {
  const target = event.target as HTMLElement | null
  const tagName = target?.tagName?.toLowerCase()
  if (tagName === 'input' || tagName === 'textarea' || target?.isContentEditable) return

  const key = event.key.toLowerCase()
  if (key === 'e') {
    event.preventDefault()
    event.stopImmediatePropagation()
    showEditor.value = !showEditor.value
    return
  }

  if (key === 't') {
    event.preventDefault()
    event.stopImmediatePropagation()
    reset()
    return
  }

  if (key === 'g') {
    event.preventDefault()
    event.stopImmediatePropagation()
    suppressSlidevFloatingUi()
  }
}

function suppressSlidevFloatingUi() {
  SLIDEV_FLOATING_SELECTORS.forEach((selector) => {
    document.querySelectorAll<HTMLElement>(selector).forEach((element) => {
      element.setAttribute('aria-hidden', 'true')
      element.style.display = 'none'
      element.style.visibility = 'hidden'
      element.style.pointerEvents = 'none'
    })
  })
}
</script>

<template>
  <div class="session-timer" title="Elapsed time · press T to reset">
    <span class="session-timer__label">TIME</span>
    <span class="session-timer__value">{{ elapsedLabel }}</span>
    <span class="session-timer__target">/ 60</span>
    <button
      class="session-timer__reset"
      type="button"
      title="Reset timer"
      @pointerdown.stop
      @mousedown.stop
      @touchstart.stop
      @click.stop="reset"
    >
      Reset
    </button>
    <span class="session-timer__bar">
      <span :style="{ width: `${progressPct}%` }" />
    </span>
  </div>
</template>
