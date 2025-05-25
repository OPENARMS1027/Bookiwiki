<template>
  <div>
    <div class="book-info-container">
      <RouterLink :to="{ name: 'bookDetail', params: { bookId: book.id } }">
        <img :src="book.cover" alt="book_cover_img"
      /></RouterLink>
      <div class="book-text">
        <RouterLink :to="{ name: 'bookDetail', params: { bookId: book.id } }"
          ><p class="book-title">{{ book.title }}</p>
        </RouterLink>
        <span class="book-author">{{ book.author }} | {{ book.pub_date }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  book: Object,
})

import { RouterLink } from 'vue-router'
</script>

<style scoped>
.book-info-container {
  display: flex;
  padding: 15px;
}

.book-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 10px;
}

.book-title {
  color: black;
}

a {
  text-decoration: none;
}
</style>
