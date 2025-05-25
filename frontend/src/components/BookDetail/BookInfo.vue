<template>
    <div v-if="book">
      <header class="header">
        <p class="book-title">{{ book.title }}</p>
        <div class="button-group">
          <button class="add-button" @click="moveToAdd(book.id)">
            <i class="fas fa-bookmark"></i> 내 서재에 담기
          </button>
          <button class="thread-button" @click="moveToThread(book.id)">
            <i class="fas fa-pen"></i> 스레드 작성
          </button>
        </div>
        <!-- <div v-else class="login-message">
          <router-link to="/login" class="login-link">로그인</router-link>하고 더 많은 기능을 사용해보세요!
        </div> -->
      </header>
      <div class="book-info">
        <div class="book-image">
          <img :src="book.cover" alt="book_cover" />
        </div>
        <div class="book-text">
          <p>{{ book.description }}</p>
          <br />
          <span>
            <strong>저자:</strong> {{ book.author }}<br />
            <strong>출판사:</strong> {{ book.publisher }}<br />
            <strong>출판일:</strong> {{ book.pub_date }}<br />
            <strong>ISBN:</strong> {{ book.isbn }}<br />
          </span>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

defineProps({
  book: Object,
})

const router = useRouter()
const userStore = useUserStore()

// 스레드 생성 페이지 이동 
const moveToThread = (bookId) => {
  if (!userStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    // 현재 페이지의 경로를 쿼리 파라미터로 같이 보내주기
    router.push({ 
      name: 'login',
      query: { redirect: router.currentRoute.value.fullPath }
    })
    return
  }
  router.push({ name: 'threadForm', params: { bookId: bookId } })
}

// 서재에 담기 버튼 함수
const moveToAdd = async (bookId) => {
  if (!userStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    // 현재 페이지의 경로를 쿼리 파라미터로 같이 보내주기
    router.push({ 
      name: 'login',
      query: { redirect: router.currentRoute.value.fullPath }
    })
    return
  }
  
  try {
    await axios.post('http://127.0.0.1:8000/books/userbooks/', {
      book_id: bookId
    }, {
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
    alert('내 서재에 저장되었습니다')
  } catch (error) {
    if (error.response?.status === 400 && error.response?.data?.message === 'already_exists') {
      alert('이미 서재에 존재하는 책입니다')
    } else {
      console.error('서재 담기 실패:', error)
      alert('서재 담기에 실패했습니다')
    }
  }
}
</script>

<style scoped>
.header {
  margin-bottom: 2rem;
  text-align: center;
}

.book-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: #333;
}

.button-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 1rem;
}

.add-button, .thread-button {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.add-button {
  background-color: #4CAF50;
  color: white;
}

.add-button:hover {
  background-color: #45a049;
}

.thread-button {
  background-color: #2196F3;
  color: white;
}

.thread-button:hover {
  background-color: #1976D2;
}

.login-message {
  margin-top: 1rem;
  color: #666;
}

.login-link {
  color: #2196F3;
  text-decoration: none;
  font-weight: bold;
}

.login-link:hover {
  text-decoration: underline;
}

.book-info {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
  background-color: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.book-image img {
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.book-text {
  flex: 1;
  line-height: 1.6;
}

.book-text p {
  margin-bottom: 1.5rem;
  color: #444;
}

.book-text strong {
  color: #333;
  margin-right: 0.5rem;
}

@media (max-width: 768px) {
  .book-info {
    flex-direction: column;
    align-items: center;
  }

  .book-image img {
    max-width: 100%;
    margin-bottom: 1.5rem;
  }
}
</style>
  