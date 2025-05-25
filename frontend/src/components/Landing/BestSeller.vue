<template>
  <div>
    <h2>베스트 셀러</h2>
    <div class="best-seller-container">
      <div class="best-seller-item" v-for="book in bestSellers" :key="book.id">
        <RouterLink :to="{ name: 'bookDetail', params: { bookId: book.id } }"
          ><img
            class="best-seller-img"
            :src="book.cover"
            alt="best_seller_book_cover"
        /></RouterLink>
        <RouterLink :to="{ name: 'bookDetail', params: { bookId: book.id } }"
          ><div class="best-seller-title">{{ book.title }}</div></RouterLink
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useBookStore } from '@/stores/book.js'
import { RouterLink } from 'vue-router'
import '@/styles/Landing/BestSeller.css'

const store = useBookStore()
const bestSellers = ref([])

onMounted(() => {
  store.getBooks()
  bestSellers.value = store.books
    .filter((book) => book.best_rank)
    .sort((a, b) => a.best_rank - b.best_rank)
    .slice(0, 5)
})
</script>

<style scoped></style>
