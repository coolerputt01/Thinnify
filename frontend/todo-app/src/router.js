import { createRouter, createWebHistory } from 'vue-router';
import HomeView from './views/HomeView.vue';
import CreateView from './views/CreateView.vue';
import LoginView from './views/LoginView.vue';
import SignupView from './views/SignupView.vue';
import LandingView from './views/LandingView.vue';
import TransitionView from './views/TransitionView.vue';
import CalenderView from './views/CalenderView.vue';
import SearchView from './views/SearchView.vue';
import AboutView from './views/AboutView.vue';


const routes = [
  { path: '/home/:user', component: HomeView,name:"home",props:true },
  { path: '/login', component: LoginView ,name:"login" },
  { path: '/signup', component: SignupView },
  { path: '/create', component: CreateView ,name:"create",props:true},
  { path: '/',component: LandingView },
  { path: '/transition/:page/:user',component: TransitionView ,name:"transition",props:true},
  { path: '/calender/:user',component: CalenderView ,name:"calender",props:true},
  { path: '/search/:user', component: SearchView,name:"search",props:true},
  { path: '/about/:user',component: AboutView,name:"about",props:true},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
