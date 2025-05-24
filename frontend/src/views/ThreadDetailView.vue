<template>
  <div>
    <BookInfo :book="book" />
    <ThreadInfo :thread="thread" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import BookInfo from '@/components/ThreadDetail/BookInfo.vue'
import ThreadInfo from '@/components/ThreadDetail/ThreadInfo.vue'

const route = useRoute()
const store = useBookStore()
const threadId = Number(route.params.threadId)

const thread = ref(null)
const book = ref(null)

onMounted(async () => {
  thread.value = await store.getThread(threadId)
  if (thread.value) {
    book.value = await store.getBook(thread.value.book.id)
  }
})
</script>

<style scoped></style>
