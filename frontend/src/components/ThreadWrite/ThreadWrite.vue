<template>
    <div>
      <h3>제목</h3>
      <input type="text" v-model="newThread.title" />
      <h3>내용</h3>
      <textarea v-model="newThread.content"></textarea>
      <h3>읽은 날짜</h3>
      <input type="date" v-model="newThread.readDate" />
      <div>
        <button @click="goBack">취소</button>
        <button @click="writeThread">쓰레드 작성</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useBookStore } from '@/stores/book.js'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
//   import '@/style/ThreadWrite/ThreadWrite.css'

  const router = useRouter()
  const store = useBookStore()
  const props = defineProps({
    book: Object,
  })
  
  const newThread = ref({
    title: '',
    content: '',
    readDate: '',
    book: props.book.id,
    cover: props.book.cover 
  })
  
  const writeThread = () => {
    const newThreadId = store.writeThread(newThread)
    router.push(`/threads/${newThreadId}`)
  }
  
  const goBack = () => {
    router.back()
  }
  </script>
  
  <style scoped>
  
  </style>
  
  