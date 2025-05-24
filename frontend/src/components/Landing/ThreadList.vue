<template>
  <div>
    <h2 class="title">쓰레드 목록</h2>
    <div class="container">
      <div>
        <p class="description">
          관심 장르를 바탕으로 최근 스레드 6개를 추천해드려요.
        </p>
      </div>
      <div class="thread-grid">
        <div
          class="thread-list-item"
          v-for="thread in threadList"
          :key="thread.id"
        >
          <RouterLink
            :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
          >
            <p class="thread-title">{{ thread.title }}</p>
            <hr />
            <p class="thread-content">{{ thread.content }}</p>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import '@/styles/Landing/ThreadList.css'

const store = useBookStore()
const interestedCategory = [1, 2] // user 정보를 토대로 관심 장르 가져오기
const threadList = ref([])

onMounted(() => {
  store.getThreads()
  threadList.value = store.threads
    .filter((thread) => interestedCategory.includes(thread.book.category))
    .sort(
      (a, b) =>
        new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime()
    )
    .slice(0, 6)
})
</script>

<style scoped></style>
