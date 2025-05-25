<template>
  <div class="wrapper">
    <div class="book-info">
      <BookInfo v-if="book" :book="book" />
      <Comment :threadId="threadId" />
    </div>
    <div class="thread-info">
      <ThreadInfo
        v-if="thread"
        :thread="thread"
        @update-thread="updateThread"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import BookInfo from '@/components/ThreadDetail/BookInfo.vue'
import ThreadInfo from '@/components/ThreadDetail/ThreadInfo.vue'
import Comment from '@/components/ThreadDetail/Comment.vue'

const route = useRoute()
const store = useBookStore()
const threadId = Number(route.params.threadId)

const thread = ref(null)
const book = ref(null)

async function fetchData(threadId) {
  try {
    const threadData = await store.getThread(threadId)
    thread.value = threadData

    if (threadData?.book?.id) {
      const bookData = await store.getBook(threadData.book.id)
      book.value = bookData
    }
  } catch (error) {
    console.error(error)
  }
}

const updateThread = (updatedThread) => {
  thread.value = {
    ...thread.value,
    ...updatedThread,
  }
}

onMounted(() => {
  fetchData(threadId)
})

watch(
  () => threadId,
  (newThreadId) => {
    if (newThreadId) {
      fetchData(Number(newThreadId))
    }
  }
)
</script>

<style scoped>
.book-info {
  width: 35%;
}

.thread-info {
  width: 65%;
}
</style>
