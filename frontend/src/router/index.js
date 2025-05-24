import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '@/views/LandingView.vue'
import BooksListView from '@/views/BooksListView.vue'
import ThreadsListView from '@/views/ThreadsListView.vue'
import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ThreadDetailView from '@/views/ThreadDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'main', component: LandingView },
    { path: '/threads', name: 'threadList', component: ThreadsListView },
    {
      path: '/threads/:threadId',
      name: 'threadDetail',
      component: ThreadDetailView,
    },
    { path: '/books', name: 'bookList', component: BooksListView },
    { path: '/books/:bookId', name: 'bookDetail', component: '' },
    { path: '/mypage', name: 'myPage', component: '' },
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
