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

import { ref, computed, onMounted } from "vue";
import { useBookStore } from "@/stores/book.js";
import BookCard from "@/components/BookList/BookCard.vue";
import '@/style/BooksList/BookList.css'

const store = useBookStore();
const selectedCategory = ref(0); // '전체' 카테고리일 경우 0
const categories = computed(() => store.categories);
const searchText = ref('')

// 카테고리 필터링된 책 목록
const filteredBooks = computed(() => {
  if (selectedCategory.value === 0) {
    return searchBooks.value;
  }

  return searchBooks.value.filter(
    (book) => book.category === Number(selectedCategory.value)
  );
});

// 검색어로 필터링된 책 목록
const searchBooks = computed(() => {
  if (!searchText.value) {
    return store.books;
  }
  return store.books.filter((book) =>
    book.title.toLowerCase().includes(searchText.value.toLowerCase()) ||
    book.author.toLowerCase().includes(searchText.value.toLowerCase())
  );
});

function onFilterCategory(categoryId) {
  selectedCategory.value = categoryId;
}

onMounted(() => {
  store.getBooks();
  store.getCategories();
});
</script>

<style scoped>
</style>
