import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import CreateView from './views/CreateView.vue';
import LoginView from './views/LoginView.vue';
import SignupView from './views/SignupView.vue';
import LandingView from './views/LandingView.vue';
import TransitionView from './views/TransitionView.vue';


const routes = [
  { path: '/home/:user', component: HomeView,name:"home",props:true },
  { path: '/', component: LoginView },
  { path: '/signup', component: SignupView },
  { path: '/create', component: CreateView ,name:"create",props:true},
  { path: '/landing',component: LandingView },
  { path:'/transtion:page',component: TransitionView ,name:"transition",props:true},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
