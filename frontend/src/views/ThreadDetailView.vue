<template>
  <div class="wrapper">
    <div class="book-info">
      <BookInfo v-if="book" :book="book" />
    </div>
    <div class="thread-info">
      <ThreadInfo v-if="thread" :thread="thread" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import BookInfo from '@/components/ThreadDetail/BookInfo.vue'
import ThreadInfo from '@/components/ThreadDetail/ThreadInfo.vue'

const route = useRoute()
const store = useBookStore()
const threadId = Number(route.params.threadId)

const thread = ref(null)
const book = ref(null)

async function fetchData(threadId) {
  const threadData = await store.getThread(threadId)
  thread.value = threadData

  const bookData = await store.getBook(threadData.book.id)
  book.value = bookData
}

onMounted(() => {
  fetchData(Number(route.params.threadId))
})

watch(
  () => route.params.threadId,
  (newThreadId) => {
    fetchData(Number(newThreadId))
  }
)
</script>

<style scoped>
.book-info {
  width: 30%;
}

.thread-info {
  width: 70%;
}
</style>
