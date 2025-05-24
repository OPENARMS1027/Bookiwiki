<template>
    <div>
      <h3>제목</h3>
      <input type="text" v-model="newThread.title" />
      <h3>내용</h3>
      <textarea v-model="newThread.content"></textarea>
      <h3>읽은 날짜</h3>
      <input type="date" v-model="newThread.reading_date" />
      <div>
        <button @click="goBack">취소</button>
        <button @click="writeThread">쓰레드 작성</button>
      </div>
    </div>
  </template>

  <script setup>
  import { useUserStore } from '@/stores/user.js'
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import '@/style/ThreadWrite/ThreadWrite.css'

  const router = useRouter()
  const props = defineProps({
    book: Object,
  })
  const store = useUserStore()
  const user = store.user
  const newThread = ref({
    title: '',
    content: '',
    reading_date: '',
    book: props.book.id,
    user: user.id,
  })
  console.log(user)

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
  
  