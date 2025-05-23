import { createRouter, createWebHistory } from "vue-router";
import BooksListView from "@/views/BooksListView.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/books",
      component: BooksListView,
    },
    
  ],
});

export default router;
