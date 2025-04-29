import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import ToastService from 'primevue/toastservice';
import 'v-calendar/style.css';
import VCalendar from 'v-calendar';


createApp(App).use(PrimeVue,{
  theme: {
      preset: Aura
  }
}).use(ToastService).use(router).use(VCalendar,{}).mount('#app')
