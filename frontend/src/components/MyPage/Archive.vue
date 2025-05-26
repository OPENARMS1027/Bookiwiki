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
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.loading,
.error {
  text-align: center;
  padding: 20px;
  color: #666;
}

.empty-archive {
  text-align: center;
  padding: 40px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  color: #666;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px;
}

.book-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
  cursor: pointer;
}

.book-card:hover {
  transform: translateY(-5px);
}

.book-image {
  width: 100%;
  height: 250px;
  overflow: hidden;
}

.book-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.book-info {
  padding: 15px;
}

.book-title {
  margin: 0;
  font-size: 1.1em;
  color: #333;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.book-author {
  margin: 5px 0 0;
  font-size: 0.9em;
  color: #666;
}

@media (max-width: 768px) {
  .book-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 15px;
    padding: 10px;
  }

  .book-image {
    height: 200px;
  }

  .book-info {
    padding: 10px;
  }
}
</style>
