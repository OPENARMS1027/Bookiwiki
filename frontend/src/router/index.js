import { createRouter, createWebHistory } from "vue-router";
import BooksListView from "@/views/BooksListView.vue";
import ThreadsListView from "@/views/ThreadsListView.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/books",
      component: BooksListView,
    },
    {
      path: "/threads",
      component: ThreadsListView,
    },
  ],
});

export default router;
