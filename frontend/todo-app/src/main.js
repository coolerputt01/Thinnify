import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import { create, NConfigProvider, NProgress} from 'naive-ui';

const naive = create({
    components: [NConfigProvider, NProgress]
  });

createApp(App).use(naive).use(router).mount('#app')
