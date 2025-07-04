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
import { ref, onMounted, watch } from 'vue'
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
      `https://bookiwiki.onrender.com/userbooks/check/${props.book.id}/`,
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      }
    )
    isInLibrary.value = response.data.is_in_library
  } catch (error) {
    console.error('서재 확인 실패:', error)
    isInLibrary.value = false
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
      await axios.delete(
        `https://bookiwiki.onrender.com/userbooks/${bookId}/`,
        {
          headers: {
            Authorization: `Token ${userStore.token}`,
          },
        }
      )
      isInLibrary.value = false
      alert('서재에서 제거되었습니다')
    } else {
      await axios.post(
        'https://bookiwiki.onrender.com/userbooks/',
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

// book prop이 변경될 때마다 서재 상태 확인
watch(
  () => props.book,
  (newBook) => {
    if (newBook) {
      checkIfInLibrary()
    }
  },
  { immediate: true }
)

// 로그인 상태가 변경될 때마다 서재 상태 확인
watch(
  () => userStore.isLogin,
  (newLoginState) => {
    if (newLoginState && props.book) {
      checkIfInLibrary()
    } else {
      isInLibrary.value = false
    }
  }
)

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
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.book-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
  margin: 0;
  flex: 1;
}

.button-group {
  display: flex;
  gap: 1rem;
}

.library-button,
.thread-button {
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border: none;
}

.add-button {
  background-color: #4caf50;
  color: white;
}

.add-button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
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
  background-color: white;
  color: #4caf50;
  border: 2px solid #4caf50;
}

.thread-button:hover {
  background-color: #4caf50;
  color: white;
  transform: translateY(-2px);
}

.book-info {
  display: flex;
  gap: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.book-image {
  flex-shrink: 0;
}

.book-image img {
  width: 300px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease;
}

.book-image img:hover {
  transform: scale(1.02);
}

.book-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.book-text p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #2c3e50;
  margin: 0;
}

.book-text span {
  display: grid;
  gap: 1rem;
  font-size: 1.05rem;
  color: #666;
}

.book-text strong {
  color: #4caf50;
  display: inline-block;
  width: 80px;
}

@media (max-width: 1024px) {
  .book-info {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }

  .book-image img {
    width: 250px;
  }

  .book-text {
    text-align: center;
  }

  .book-text span {
    justify-items: center;
  }

  .book-text strong {
    width: auto;
    margin-right: 0.5rem;
  }
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }

  .book-title {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-group {
    width: 100%;
  }

  .add-button,
  .thread-button {
    flex: 1;
    justify-content: center;
    padding: 0.6rem 1rem;
    font-size: 0.9rem;
  }

  .book-info {
    padding: 1rem;
  }

  .book-image img {
    width: 200px;
  }

  .book-text p {
    font-size: 1rem;
  }

  .book-text span {
    font-size: 0.95rem;
  }
}
</style>
