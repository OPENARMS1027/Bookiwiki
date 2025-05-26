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
import { ref, computed, watch } from 'vue'
import { useBookStore } from '@/stores/book.js'
import { RouterLink } from 'vue-router'

const store = useBookStore()
const bestSellers = ref([])

const updateBestSellers = () => {
  bestSellers.value = store.books
    .filter((book) => book.best_rank)
    .sort((a, b) => a.best_rank - b.best_rank)
    .slice(0, 5)
}

watch(() => store.books, updateBestSellers, { immediate: true })

store.getBooks()
</script>

<style scoped>
.best-seller-container {
  display: flex;
}

.best-seller-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 10px;
  width: 150px;
}

.best-seller-img {
  width: 100px;
  height: 150px;
  cursor: pointer;
  margin-bottom: 5px;
}

.best-seller-title {
  width: 120px;
  min-width: 0;
  line-height: 25px;
  text-align: center;
  display: block;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.best-seller-item a {
  text-decoration: none;
  color: #222;
  font-weight: 450;
  cursor: pointer;
}
</style>
