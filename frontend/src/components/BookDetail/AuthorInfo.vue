<template>
    <div class="container">
      <header class="header">
        <p class="header-title">작가정보</p>
      </header>
      <div class="author-info">
        <div class="author-text">
          <p class="author-title">{{ book.author }}</p>
          <p></p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import '@/styles/BookDetail/AuthorInfo.css'
  const props = defineProps({
    book: Object,
  })

  </script>
  
  <style scoped>
  
  </style>
  