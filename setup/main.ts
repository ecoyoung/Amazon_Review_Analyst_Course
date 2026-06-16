import type { UserModule } from '@slidev/types'
import Vue3Lottie from 'vue3-lottie'

export default <UserModule>(({ app }) => {
  app.component('Vue3Lottie', Vue3Lottie)
})
