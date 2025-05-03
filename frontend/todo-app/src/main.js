import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import ToastService from 'primevue/toastservice'
import 'v-calendar/style.css'
import VCalendar from 'v-calendar'
import api from './axios.js'

const app = createApp(App)

app.use(PrimeVue, {
  theme: {
    preset: Aura
  }
})
app.use(ToastService)
app.use(router)
app.use(VCalendar, {})
app.config.globalProperties.$api = api

app.mount('#app')