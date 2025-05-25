<template>
    <div class="container">
      <BookInfo :book="book" />
      <BookThread :book="book"/>
      <!-- <AuthorInfo :book="book" /> -->
    </div>
  </template>
  
  <script setup>
    import { ref, onMounted } from 'vue'
    import { useRoute } from 'vue-router'
    import { useBookStore } from '@/stores/book'
    import BookInfo from '@/components/BookDetail/BookInfo.vue'
    import AuthorInfo from '@/components/BookDetail/AuthorInfo.vue'
    import BookThread from '@/components/BookDetail/BookThread.vue'
    const route = useRoute()
    const bookPk = Number(route.params.bookId)
    const store = useBookStore()
    const book = ref(null)

    async function fetchData() {
        const bookData = await store.getBook(bookPk)
        book.value = bookData
    }

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
  