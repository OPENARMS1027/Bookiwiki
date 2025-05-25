<template>
  <div class="container">
    <div class="book-card">
      <img :src="book.cover" alt="book_cover" class="book-cover-img" />
      <div class="book-description">
        <p class="book-title" @click="moveToDetail(book.id)">
          {{ book.title }}
        </p>
        <p class="book-info">
          {{ book.author }} | {{ book.publisher }} |
          {{ book.pub_date }}
        </p>
        <p class="book-subtitle">{{ book.subTitle }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import '@/style/BooksList/BookCard.css'

const props = defineProps({
  book: Object,
});

const router = useRouter();
const book = props.book
const moveToDetail = (bookId) => {
  router.push({ name: "bookDetail", params: { bookId: bookId } });
};
</script>

<style scoped>
</style>
