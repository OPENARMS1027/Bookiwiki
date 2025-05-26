<template>
  <div class="archive">
    <h2>내 서재</h2>
    <div v-if="loading" class="loading">
      <font-awesome-icon :icon="['fas', 'spinner']" spin />
      <span>로딩 중...</span>
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else>
      <div v-if="books.length === 0" class="empty-archive">
        <p>아직 서재에 담은 책이 없습니다.</p>
      </div>
      <div v-else class="book-grid">
        <div
          v-for="book in books"
          :key="book.id"
          class="book-card"
          @click="goToBook(book.id)"
        >
          <div class="book-image">
            <img :src="book.cover" :alt="book.title" />
          </div>
          <div class="book-info">
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const books = ref([])
const loading = ref(true)
const error = ref(null)

const fetchMyBooks = async () => {
  try {
    loading.value = true
    const response = await axios.get('http://127.0.0.1:8000/user/me/', {
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
    if (response.data && response.data.books) {
      books.value = response.data.books
    }
  } catch (err) {
    error.value = '서재 정보를 불러오는데 실패했습니다.'
    console.error('Error fetching archive:', err)
  } finally {
    loading.value = false
  }
}

const goToBook = (bookId) => {
  router.push(`/books/${bookId}`)
}

onMounted(() => {
  fetchMyBooks()
})
</script>

<style scoped>
.archive {
  height: 100%;
}

h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

h2::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 1em;
  background-color: #4caf50;
  border-radius: 2px;
}

.loading,
.error {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.empty-archive {
  text-align: center;
  padding: 3rem 2rem;
  color: #666;
  background: #f8f9fa;
  border-radius: 8px;
  font-size: 0.95rem;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 1.5rem;
}

.book-card {
  background: #f8f9fa;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.book-card:hover {
  transform: translateY(-4px);
  border-color: #4caf50;
  background: white;
}

.book-image {
  position: relative;
  padding-top: 140%;
  background: #f1f1f1;
  overflow: hidden;
}

.book-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.book-card:hover .book-image img {
  transform: scale(1.05);
}

.book-info {
  padding: 1rem;
}

.book-title {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 500;
  color: #2c3e50;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  line-height: 1.4;
  height: 2.8em;
}

.book-author {
  margin: 0.5rem 0 0;
  font-size: 0.85rem;
  color: #666;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 1400px) {
  .book-grid {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 1.25rem;
  }
}

@media (max-width: 768px) {
  h2 {
    font-size: 1.3rem;
    margin-bottom: 1.25rem;
  }

  .book-grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 1rem;
  }

  .book-info {
    padding: 0.75rem;
  }

  .book-title {
    font-size: 0.9rem;
  }

  .book-author {
    font-size: 0.8rem;
  }
}
</style>
