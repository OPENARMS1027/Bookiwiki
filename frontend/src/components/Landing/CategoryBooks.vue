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
import { computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book.js'

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

<style scoped>
.button-container {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.genre-button {
  all: unset;
  padding: 0.5rem 1.2rem;
  background-color: #327729;
  color: white;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.2s ease, transform 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.genre-button:hover {
  background-color: #27601f;
  transform: translateY(-2px);
}
</style>
