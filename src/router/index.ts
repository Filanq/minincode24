import { createRouter, createWebHistory } from 'vue-router';
import AdminView from '@/views/AdminView.vue';
import HomeView from '@/views/HomeView.vue';
import NewsView from '@/views/NewsView.vue';
import RegistrationView from '@/views/RegistrationView.vue';
import LoginView from '@/views/LoginView.vue';
import OrganizationsView from '@/views/OrganizationsView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin',
      name: 'AdminView',
      component: AdminView,
    },
    {
      path: '/news',
      name: 'news',
      component: NewsView,
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/organizations',
      name: 'organizations',
      component: OrganizationsView,
    },
  ],
});

export default router;