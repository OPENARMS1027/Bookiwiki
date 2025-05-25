<template>
    <div v-if="book">
      <header class="header">
  <p class="book-title">{{ book.title }}</p>
  <div class="button-group">
    <button class="add-button" @click="moveToAdd(book.id)">내 서재에 담기</button>
    <button class="thread-button" @click="moveToThread(book.id)">스레드 작성</button>
  </div>
</header>
      <div class="book-info">
        <div class="book-image">
          <img :src="book.cover" alt="book_cover" />
        </div>
        <div class="book-text">
          <p>{{ book.description }}</p>
          <br />
          <span>
            <strong> 저자:</strong> {{ book.author }}<br />
            <strong> 출판사:</strong> {{ book.publisher }}<br />
            <strong> 출판일:</strong> {{ book.pub_date }}<br />
            <strong> ISBN:</strong> {{ book.isbn }}<br />
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
    import '@/styles/BookDetail/BookInfo.css'
    
    defineProps({
    book: Object,
    })
    const router = useRouter()
    const userStore = useUserStore()

    // 스레드 생성 페이지 이동 
    const moveToThread = (bookId) => {
    router.push({ name: 'threadsWrite', params: { bookId: bookId } })
    }
    
    // 서재에 담기 버튼 함수
    const moveToAdd = async (bookId) => {
        try {
            // 서재에 책 추가 API 호출
            await axios.post('http://127.0.0.1:8000/books/userbooks/', {
                book_id: bookId
            }, {
                headers: {
                    Authorization: `Token ${userStore.token}`
                }
            })
            
            // 성공 알림
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
  .button-group {
  display: flex;
  gap: 8px; /* 버튼 간 여백 조정 */
}

.add-button,
.thread-button {
  padding: 6px 12px;
  font-size: 14px;
  cursor: pointer;
}
  </style>
  