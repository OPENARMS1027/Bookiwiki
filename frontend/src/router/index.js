import { createRouter, createWebHistory } from "vue-router";
import BooksListView from "@/views/BooksListView.vue";
import ThreadsListView from "@/views/ThreadsListView.vue";
import ThreadWriteView from "@/views/ThreadWriteView.vue";
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
    {
      path: "/threads/write",
      component: ThreadWriteView,
    },
  ],
});

export default router;
