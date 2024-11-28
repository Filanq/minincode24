import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import NewsView from '@/views/NewsView.vue';
import EventsView from '@/views/EventsView.vue';
import RegistrationView from '@/views/RegistrationView.vue';
import LoginView from '@/views/LoginView.vue';
import OrganizationsView from '@/views/OrganizationsView.vue';
import UserAccountFullnameSettingsView from '@/views/UserAccountFullnameSettingsView.vue';
import UserAccountEventsListView from '@/views/UserAccountEventsListView.vue';
import AdminOrganizationsRequestsView from '@/views/AdminOrganizationsRequestsView.vue';
import OrgAccountDataSettingsView from '@/views/OrgAccountDataSettingsView.vue';
import OrgAccountEventssView from '@/views/OrgAccountEventssView.vue';
import OrgAccountNewsView from '@/views/OrgAccountNewsView.vue';
import OrgAccountGuestsView from '@/views/OrgAccountGuestsView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
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

    {
      path: '/user_account',
      redirect: '/user_account/name_settings'
    },
    {
      path: '/user_account/name_settings',
      name: 'name_settings',
      component: UserAccountFullnameSettingsView,
    },
    {
      path: '/user_account/events_list',
      name: 'events_list',
      component: UserAccountEventsListView,
    },

    {
      path: '/admin',
      redirect: '/admin/organizations_requests',
    },
    {
      path: '/admin/organizations_requests',
      name: 'organizations_requests',
      component: AdminOrganizationsRequestsView,
    },

    {
      path: '/org_account',
      redirect: '/org_account/data_settings'
    },
    {
      path: '/org_account/data_settings',
      name: 'org_account_data_settings',
      component: OrgAccountDataSettingsView,
    },
    {
      path: '/org_account/events',
      name: 'org_account_events',
      component: OrgAccountEventssView,
    },
    {
      path: '/org_account/news',
      name: 'org_account_news',
      component: OrgAccountNewsView,
    },
    {
      path: '/org_account/guests',
      name: 'org_account_guests',
      component: OrgAccountGuestsView,
    },
    {
      path: '/news',
      name: 'news',
      component: NewsView,
    },
    {
      path: '/events',
      name: 'events',
      component: EventsView,
    }
  ],
});

export default router;