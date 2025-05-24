<template>
  <div>
    <h2>장르별 도서</h2>
    <div class="button-container">
      <div v-for="category in categories" :key="category.id">
        <button class="genre-button" @click="moveToBookList(category.id)">
          {{ category.name }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import '@/styles/Landing/CategoryBooks.css'

const router = useRouter()
const store = useBookStore()
const categories = computed(() => store.categories)

onMounted(() => {
  store.getCategories()
})

const moveToBookList = (categoryId) => {
  router.push({ name: 'bookList', query: { category: categoryId } })
}
</script>

<style scoped></style>
