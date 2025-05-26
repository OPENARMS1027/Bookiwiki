<template>
  <div class="bestseller-section">
    <h2 class="section-title">
      <i class="fas fa-crown"></i>
      베스트셀러
    </h2>
    <div class="bestseller-container">
      <div
        v-for="(book, index) in bestSellers"
        :key="book.id"
        class="bestseller-item"
      >
        <div class="rank-badge">{{ index + 1 }}</div>
        <RouterLink
          :to="{ name: 'bookDetail', params: { bookId: book.id } }"
          class="book-link"
        >
          <div class="book-image">
            <img :src="book.cover" :alt="book.title" class="book-cover" />
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useBookStore } from '@/stores/book.js'
import { RouterLink } from 'vue-router'

const store = useBookStore();
const bestSellers = ref([]);

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
.bestseller-section {
  width: 100%;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-title i {
  color: #4caf50;
  font-size: 1.2em;
}

.bestseller-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2rem;
  padding: 0.5rem;
}

.bestseller-item {
  position: relative;
  transition: all 0.3s ease;
}

.bestseller-item:hover {
  transform: translateY(-4px);
}

.rank-badge {
  position: absolute;
  top: -12px;
  left: -12px;
  width: 32px;
  height: 32px;
  background: #4caf50;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.1rem;
  box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
  z-index: 1;
}

.book-link {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.book-image {
  position: relative;
  padding-top: 140%;
  background: #f8f9fa;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.book-cover {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.bestseller-item:hover .book-cover {
  transform: scale(1.05);
}

.book-info {
  text-align: center;
  padding: 0.5rem;
}

.book-title {
  font-size: 1rem;
  font-weight: 500;
  color: #2c3e50;
  margin: 0 0 0.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.4;
}

.book-author {
  font-size: 0.9rem;
  color: #666;
  margin: 0;
}

@media (max-width: 1200px) {
  .bestseller-container {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 992px) {
  .bestseller-container {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.3rem;
    margin-bottom: 1.5rem;
  }

  .bestseller-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }

  .book-title {
    font-size: 0.95rem;
  }

  .book-author {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .bestseller-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .rank-badge {
    width: 28px;
    height: 28px;
    font-size: 1rem;
  }
}
</style>
