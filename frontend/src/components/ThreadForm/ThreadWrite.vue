<template>
    <div>
      <h3>제목</h3>
      <input type="text" v-model="title" />
      <h3>내용</h3>
      <textarea v-model="content"></textarea>
      <h3>읽은 날짜</h3>
      <input type="date" v-model="reading_date" />
      <div>
        <button @click="goBack">취소</button>
        <button @click="writeThread">쓰레드 작성</button>
      </div>
    </div>
  </template>

  <script setup>
  import { useUserStore } from '@/stores/user.js'
  import { useBookStore } from '@/stores/book.js'
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const props = defineProps({
    bookId: Number,
  })
  const store = useUserStore()
  const BookStore = useBookStore()
  const thisUser = ref(null)

  onMounted(async () => {
    await store.getThisUser()
    thisUser.value = store.thisUser
  })

  const title = ref('')
  const content = ref('')
  const reading_date = ref('')
  const writeThread = async () => {
  const threadData = {
    title: title.value,
    content: content.value,
    reading_date: reading_date.value,
    book: props.bookId,
    user: thisUser.value ? thisUser.value.id : null,
  }
    const newThreadId = await BookStore.writeThread(threadData)
    router.push(`/threads/${newThreadId}/`)
  }
  
  const goBack = () => {
    router.back()
  }
  </script>
  
  <style scoped>
  
  </style>
  
  