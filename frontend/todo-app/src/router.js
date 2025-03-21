import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import CreateView from './views/CreateView.vue';
import LoginView from './views/LoginView.vue';
import SignupView from './views/SignupView.vue';
import LandingView from './views/LandingView.vue';


const routes = [
  { path: '/home/:user', component: HomeView,name:"home",props:true },
  { path: '/', component: LoginView },
  { path: '/signup', component: SignupView },
  { path: '/create', component: CreateView },
  { path: '/landing',component: LandingView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
