import { createRouter, createWebHistory } from 'vue-router'
import BooksListView from '@/views/BooksListView.vue'
import ThreadsListView from '@/views/ThreadsListView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/books',
      component: BooksListView,
    },
    {
      path: '/threads',
      component: ThreadsListView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView,
    },
  ],
})

export default router
