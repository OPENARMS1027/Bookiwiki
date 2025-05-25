<template>
  ddd
    <div class="book-info">
      <h3>도서 정보</h3>
      <div class="book-details">
        <img :src="book.cover" alt="도서 표지" />
        <div class="book-text">
          <p class="title-author">
            <strong>{{ book.title }}</strong> | {{ book.author }} | {{ book.pub_date }}
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useBookStore } from '@/stores/book'
  defineProps({
    bookId: String,
  })
  const book = ref(null)
  const store = useBookStore()
  const bookData = await store.getBook(bookId)
  book.value = bookData


  </script>
  
  <style scoped>
  
  </style>
  