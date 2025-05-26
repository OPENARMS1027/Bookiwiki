<template>
  <div v-if="book">
    <header class="header">
      <p class="book-title">{{ book.title }}</p>
      <div class="button-group">
        <button
          :class="[
            'library-button',
            isInLibrary ? 'remove-button' : 'add-button',
          ]"
          @click="handleLibraryAction(book.id)"
        >
          <i :class="isInLibrary ? 'far fa-bookmark' : 'fas fa-bookmark'"></i>
          {{ isInLibrary ? '내 서재에 담김' : '내 서재에 담기' }}
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

const props = defineProps({
  book: Object,
})

const router = useRouter()
const userStore = useUserStore()
const isInLibrary = ref(false)

// 서재에 있는지 확인
const checkIfInLibrary = async () => {
  if (!userStore.isLogin || !props.book) return

  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/userbooks/check/${props.book.id}/`,
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      }
    )
    isInLibrary.value = response.data.is_in_library
  } catch (error) {
    console.error('서재 확인 실패:', error)
  }
}

// 서재 담기, 빼기
const handleLibraryAction = async (bookId) => {
  if (!userStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({
      name: 'login',
      query: { redirect: router.currentRoute.value.fullPath },
    })
    return
  }

  try {
    if (isInLibrary.value) {
      await axios.delete(`http://127.0.0.1:8000/userbooks/${bookId}/`, {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
      isInLibrary.value = false
      alert('서재에서 제거되었습니다')
    } else {
      await axios.post(
        'http://127.0.0.1:8000/userbooks/',
        {
          book_id: bookId,
        },
        {
          headers: {
            Authorization: `Token ${userStore.token}`,
          },
        }
      )
      isInLibrary.value = true
      alert('내 서재에 저장되었습니다')
    }
  } catch (error) {
    if (
      error.response?.status === 400 &&
      error.response?.data?.message === 'already_exists'
    ) {
      alert('이미 서재에 존재하는 책입니다')
      isInLibrary.value = true
    } else {
      console.error('서재 작업 실패:', error)
      alert('작업에 실패했습니다')
    }
  }
}

// 스레드 생성 페이지 이동
const moveToThread = (bookId) => {
  if (!userStore.isLogin) {
    alert('로그인이 필요한 서비스입니다.')
    router.push({
      name: 'login',
      query: { redirect: router.currentRoute.value.fullPath },
    })
    return
  }
  router.push({ name: 'threadForm', params: { bookId: bookId } })
}

onMounted(() => {
  checkIfInLibrary()
})
</script>

<style scoped>
.button-group {
  display: flex;
  gap: 8px; /* 버튼 간 여백 조정 */
}

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

.library-button,
.thread-button {
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
  background-color: #4caf50;
  color: white;
}

.add-button:hover {
  background-color: #45a049;
}

.remove-button {
  background-color: white;
  color: #4caf50;
  border: 2px solid #4caf50;
}

.remove-button:hover {
  background-color: #f8f8f8;
  border-color: #45a049;
  color: #45a049;
}

.thread-button {
  background-color: #2196f3;
  color: white;
}

.thread-button:hover {
  background-color: #1976d2;
}

.login-message {
  margin-top: 1rem;
  color: #666;
}

.login-link {
  color: #2196f3;
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
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.book-image img {
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
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
