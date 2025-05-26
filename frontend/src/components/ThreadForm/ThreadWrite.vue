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
        <button @click="handleSubmit">{{ isEditMode ? '수정완료' : '쓰레드 작성' }}</button>
      </div>
    </div>
  </template>

  <script setup>
  const props = defineProps({
    bookId: Number,
  })

  import { useUserStore } from '@/stores/user.js'
  import { useBookStore } from '@/stores/book.js'
  import { ref, onMounted } from 'vue'
  import { useRouter, useRoute } from 'vue-router'

  const router = useRouter()
  const route = useRoute()

  const store = useUserStore()
  const bookStore = useBookStore()
  const thisUser = ref(null)

  const title = ref('')
  const content = ref('')
  const reading_date = ref('')
  const isEditMode = ref(false)
  const threadId = ref(null)

  onMounted(async () => {
    await store.getThisUser()
    thisUser.value = store.thisUser

    const type = route.query.type
    if (type === 'edit') { // 수정 모드일때
      isEditMode.value = true
      threadId.value = route.query.threadId
      try {
        const threadData = await bookStore.getThread(threadId.value)
        title.value = threadData.title
        content.value = threadData.content
        reading_date.value = threadData.reading_date
      } catch (error) {
        console.error(error)
        goBack()
      }
    }
  })

  const handleSubmit = async () => {
    if (!title.value || !content.value) {
      alert('제목과 내용을 입력해주세요.')
      return
    }

    try {
      if (isEditMode.value) {
        // 수정
        const updateData = {
          title: title.value,
          content: content.value,
          reading_date: reading_date.value,
          book: props.bookId,
          user: thisUser.value.id
        }
        await bookStore.updateThread(threadId.value, updateData)
        router.push(`/threads/${threadId.value}/`)
      } else {
        // 생성
        const threadData = {
          title: title.value,
          content: content.value,
          reading_date: reading_date.value,
          book: props.bookId,
          user: thisUser.value ? thisUser.value.id : null,
        }
        const newThreadId = await bookStore.writeThread(threadData)
        router.push(`/threads/${newThreadId}/`)
      }
    } catch (error) {
      console.error(isEditMode.value ? '스레드 수정 실패:' : '스레드 생성 실패:', error)
      alert(isEditMode.value ? '스레드 수정에 실패했습니다.' : '스레드 생성에 실패했습니다.')
    }
  }

  const goBack = () => {
    if (isEditMode.value) {
      router.push(`/threads/${threadId.value}/`)
    } else {
      router.back()
    }
  }
  </script>
  
  <style scoped>
  
  </style>
  
  