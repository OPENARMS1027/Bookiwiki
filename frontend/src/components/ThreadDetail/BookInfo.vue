<template>
  <div>
    <div class="book-info-container">
      <div class="book-header">
        <h2>도서 정보</h2>
      </div>
      <div class="book-content">
        <RouterLink
          :to="{ name: 'bookDetail', params: { bookId: book.id } }"
          class="book-cover"
        >
          <img :src="book.cover" alt="book_cover_img" />
        </RouterLink>
        <div class="book-details">
          <RouterLink
            :to="{ name: 'bookDetail', params: { bookId: book.id } }"
            class="book-title-link"
          >
            <h3 class="book-title">{{ book.title }}</h3>
          </RouterLink>
          <div class="book-meta">
            <p class="book-author">
              <span class="label">저자</span>
              {{ book.author }}
            </p>
            <p class="book-publisher">
              <span class="label">출판사</span>
              {{ book.publisher }}
            </p>
            <p class="book-date">
              <span class="label">출판일</span>
              {{ book.pub_date }}
            </p>
          </div>
          <div class="book-description" v-if="book.description">
            <p>{{ truncateDescription(book.description) }}</p>
          </div>
          <div class="book-actions">
            <RouterLink
              :to="{ name: 'bookDetail', params: { bookId: book.id } }"
              class="view-more"
            >
              자세히 보기
              <font-awesome-icon :icon="['fas', 'arrow-right']" />
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  book: Object,
})

const truncateDescription = (text) => {
  if (!text) return ''
  return text.length > 150 ? text.slice(0, 150) + '...' : text
}
</script>

<style scoped>
.book-info-container {
  color: #333;
}

.book-header {
  margin-bottom: 1.5rem;
}

.book-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #4caf50;
  margin: 0;
}

.book-content {
  display: flex;
  gap: 2rem;
}

.book-cover {
  flex-shrink: 0;
  display: block;
  transition: transform 0.3s ease;
}

.book-cover:hover {
  transform: translateY(-4px);
}

.book-cover img {
  width: 180px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.book-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.book-title-link {
  text-decoration: none;
  color: inherit;
}

.book-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin: 0;
  color: #2c3e50;
  transition: color 0.2s ease;
}

.book-title-link:hover .book-title {
  color: #4caf50;
}

.book-meta {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  color: #666;
}

.book-meta p {
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.label {
  font-weight: 600;
  color: #4caf50;
  min-width: 4rem;
}

.book-description {
  margin-top: 0.5rem;
  color: #666;
  line-height: 1.6;
}

.book-description p {
  margin: 0;
}

.book-actions {
  margin-top: auto;
  padding-top: 1rem;
}

.view-more {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #4caf50;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
}

.view-more:hover {
  gap: 0.75rem;
  color: #45a049;
}

@media (max-width: 768px) {
  .book-content {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .book-cover img {
    width: 140px;
  }

  .book-meta p {
    justify-content: center;
  }

  .book-actions {
    display: flex;
    justify-content: center;
  }
}
</style>
