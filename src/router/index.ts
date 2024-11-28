import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import AboutView from '@/views/AboutView.vue';
import RegistrationView from '@/views/RegistrationView.vue';
import LoginView from '@/views/LoginView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/account',
      redirect: '/account/registration',
    },
    {
      path: '/account/registration',
      name: 'registration',
      component: RegistrationView,
    },
    {
      path: '/account/login',
      name: 'login',
      component: LoginView,
    },
  ],
});

export default router;