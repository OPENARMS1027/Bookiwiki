<template>
    <div v-if="book">
      <header class="header">
        <p class="book-title">{{ book.title }}</p>
        <button class="add-button" @click="moveToAdd(book.id)">내 서재에 담기</button>
        <button class="thread-button" @click="moveToThread(book.id)">
          스레드 작성
        </button>
      </header>
      <div class="book-info">
        <div class="book-image">
          <img :src="book.cover" alt="book_cover" />
        </div>
        <div class="book-text">
          <p>{{ book.description }}</p>
          <br />
          <span>
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

    // 함수
    const moveToThread = (bookId) => {
    router.push({ name: 'threadsWrite', params: { bookId: bookId } })
    }
    const moveToAdd = async (bookId) => {
        try {
        // 서재에 책 추가 API 호출
        await axios.post('http://127.0.0.1:8000/books/userbooks/', {
            book_id: bookId,
            user_id: userStore.user.id
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
  
  </style>
  