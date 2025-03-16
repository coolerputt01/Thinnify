import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import CreateView from '@/views/CreateView.vue';
import LoginView from '@/views/LoginView.vue';
import SignupView from '@/views/SignupView.vue';


const routes = [
  { path: '/home', component: HomeView },
  { path: '/', component: LoginView },
  { path: '/signup', component: SignupView },
  { path: '/create', component: CreateView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
