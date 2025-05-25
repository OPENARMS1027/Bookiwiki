<template>
  <div class="wrapper">
    <div class="book-aside">
      <div>
        <label for="search">검색</label>
        <br>
        <input type="text" id = 'search' v-model="searchText">
      </div>

      <div v-for="category in categories" :key="category.id">
        <button
          class="category-button"
          :class="{ selected: selectedCategory === category.id }"
          @click="onFilterCategory(category.id)"
        >
          {{ category.name }}
        </button>
      </div>
    </div>
    <div class="book-main">
      <div v-for="book in filteredBooks" :key="book.id">
        <BookCard :book="book" />
      </div>
    </div>
  </div>
</template>

<script setup>

import { ref, computed, onMounted } from "vue"
import { useRoute } from 'vue-router'
import { useBookStore } from "@/stores/book.js"
import BookCard from "@/components/BookList/BookCard.vue"

const route = useRoute()
const store = useBookStore()
const selectedCategory = ref(0) // '전체' 카테고리일 경우 0
const categories = computed(() => store.categories)
const searchText = ref('')

// 카테고리 필터링된 책 목록
const filteredBooks = computed(() => {
  if (selectedCategory.value === 0) {
    return searchBooks.value
  }

  return searchBooks.value.filter(
    (book) => book.category === Number(selectedCategory.value)
  )
})

// 검색어로 필터링된 책 목록
const searchBooks = computed(() => {
  if (!searchText.value) {
    return store.books
  }
  return store.books.filter((book) =>
    book.title.toLowerCase().includes(searchText.value.toLowerCase()) ||
    book.author.toLowerCase().includes(searchText.value.toLowerCase())
  )
})

function onFilterCategory(categoryId) {
  selectedCategory.value = categoryId
}

onMounted(() => {
  store.getBooks()
  store.getCategories()

  const categoryFromQuery = route.query.category
  if (categoryFromQuery) {
    selectedCategory.value = Number(categoryFromQuery)
  }
})
</script>

<style scoped>
.wrapper {
    display: flex;
    background-color: rgb(30, 30, 30);
    min-height: 100vh;
  }
  
  .book-aside {
    width: 20%;
  }
  
  .category-button {
    background-color: transparent;
    color: white;
    border: none;
    margin-top: 5px;
    margin-bottom: 10px;
    padding-left: 10px;
    cursor: pointer;
  }
  
  .category-button:hover {
    color: #ff3c3c;
  }
  
  .category-button.selected {
    color: #ff3c3c;
    font-weight: bold;
    border-left: 3px solid #ff3c3c;
    padding-left: 7px;
  }
  
  .book-main {
    width: 80%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: min-content;
    gap: 0;
    align-items: start;
  }
  
  .book-main > div {
    width: 100%;
  }
</style>
