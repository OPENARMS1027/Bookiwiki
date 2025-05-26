<template>
  <div class="wrapper">
    <div class="book-aside">
      <div class="search-container">
        <label for="search">
          <font-awesome-icon :icon="['fas', 'search']" /> 검색
        </label>
        <input
          type="text"
          id="search"
          v-model="searchText"
          placeholder="제목 또는 저자 검색"
          class="search-input"
        />
      </div>
      <div>
        <button
          class="category-button"
          :class="{ selected: selectedCategory === 0 }"
          @click="onFilterCategory(0)"
        >
          <font-awesome-icon :icon="['fas', 'list']" /> | 전체
        </button>
      </div>
      <div v-for="category in categories" :key="category.id">
        <button
          class="category-button"
          :class="{ selected: selectedCategory === category.id }"
          @click="onFilterCategory(category.id)"
        >
          <font-awesome-icon :icon="['fas', 'book']" /> | {{ category.name }}
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
import { useRoute } from "vue-router";
import { useBookStore } from "@/stores/book.js";
import BookCard from "@/components/BookList/BookCard.vue";

const route = useRoute();
const store = useBookStore();
const selectedCategory = ref(0); // '전체' 카테고리일 경우 0
const categories = computed(() => store.categories);
const searchText = ref("");

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
  return store.books.filter(
    (book) =>
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

  const categoryFromQuery = route.query.category;
  if (categoryFromQuery) {
    selectedCategory.value = Number(categoryFromQuery);
  }
});
</script>

<style scoped>
.wrapper {
  display: flex;
  min-height: 100vh;
}

.book-aside {
  width: 20%;
  padding: 2rem 1rem;
  border-right: 1px solid rgba(76, 175, 80, 0.2);
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.search-container {
  padding: 0 10px 20px 10px;
  margin-bottom: 20px;
  border-bottom: 1px solid rgba(76, 175, 80, 0.2);
}

.search-container label {
  color: #4caf50;
  font-size: 1.1em;
  margin-bottom: 12px;
  display: block;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.search-input {
  width: calc(100% - 30px);
  padding: 10px 15px;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 8px;
  color: inherit;
  font-size: 0.95em;
  transition: all 0.3s ease;
  background: transparent;
}

.search-input:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.2);
}

.search-input::placeholder {
  color: #666;
}

.category-button {
  width: 100%;
  background-color: transparent;
  color: inherit;
  border: none;
  margin: 5px 0;
  padding: 12px 15px;
  cursor: pointer;
  text-align: left;
  border-radius: 6px;
  transition: all 0.3s ease;
  font-size: 0.95em;
  display: flex;
  align-items: center;
  gap: 10px;
}

.category-button:hover {
  background-color: rgba(76, 175, 80, 0.1);
  color: #4caf50;
}

.category-button.selected {
  color: #4caf50;
  font-weight: 600;
  background-color: rgba(76, 175, 80, 0.15);
  border-left: 3px solid #4caf50;
}

.category-button svg {
  width: 16px;
  opacity: 0.8;
}

.book-main {
  width: 80%;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}

.book-main > div {
  width: 100%;
  transition: all 0.3s ease;
  border: 1px solid rgba(76, 175, 80, 0.1);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  padding: 0.5rem;
  background: transparent;
}

.book-main > div:hover {
  transform: translateY(-5px);
  border-color: rgba(76, 175, 80, 0.3);
  box-shadow: 0 5px 15px rgba(76, 175, 80, 0.1);
}

.book-main > div::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(to right, #4caf50, #81c784);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.book-main > div:hover::before {
  opacity: 1;
}

/* 책 카드 내부 스타일 추가 */
:deep(.book-card) {
  background: transparent;
  height: 100%;
}

:deep(.book-card img) {
  border-radius: 8px;
  transition: all 0.3s ease;
}

:deep(.book-card:hover img) {
  transform: scale(1.02);
}

:deep(.book-card h3) {
  color: inherit;
  font-size: 1.2em;
  margin: 0.5rem 0 0.25rem;
  font-weight: 600;
}

:deep(.book-card p) {
  color: inherit;
  opacity: 0.8;
  font-size: 0.95em;
  margin: 0.25rem 0;
}

:deep(.book-card .book-info) {
  padding: 0.5rem 0;
}

@media (max-width: 768px) {
  .wrapper {
    flex-direction: column;
  }

  .book-aside {
    width: 100%;
    padding: 1rem;
    border-right: none;
    border-bottom: 1px solid rgba(76, 175, 80, 0.2);
  }

  .book-main {
    width: 100%;
    padding: 1rem;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }

  .search-input {
    width: calc(100% - 20px);
  }
}
</style>
