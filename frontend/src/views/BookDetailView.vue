<template>
    <div class="container">
      <BookInfo :book="book" />
      <VoiceOfAi :book="book" />
      <BookThread :book="book"/>
      <!-- <AuthorInfo :book="book" /> -->
      <AiRecommend :book="book"/>
      
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted, watch } from 'vue'
    import { useRoute } from 'vue-router'
    import { useBookStore } from '@/stores/book'
    import BookInfo from '@/components/BookDetail/BookInfo.vue'
    import AuthorInfo from '@/components/BookDetail/AuthorInfo.vue'
    import BookThread from '@/components/BookDetail/BookThread.vue'
    import VoiceOfAi from '@/components/BookDetail/VoiceOfAi.vue'
    import AiRecommend from '@/components/BookDetail/AiRecommend.vue'

    const route = useRoute()
    const store = useBookStore()
    const book = ref(null)

    async function fetchData() {
        const bookPk = Number(route.params.bookId)
        const bookData = await store.getBook(bookPk)
        book.value = bookData
    }

    // 라우트 파라미터가 변경될 때마다 데이터를 다시 불러옴
    watch(
        () => route.params.bookId,
        async (newId) => {
            if (newId) {
                await fetchData()
            }
        }
    )

    onMounted(() => {
        fetchData()
    })
  </script>
  
  <style scoped>
  .container {
    background-color: rgb(247, 247, 247);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0 40px;
  }
  </style>
  