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

<style scoped>
.wrapper {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 1rem;
  text-align: center;
}

.container {
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  width: 100%;
}

.description {
  margin-bottom: 2rem;
  color: white;
  text-align: center;
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  text-align: left; /* 내부 카드 텍스트 정렬 */
}

.thread-list-item {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  background-color: #fafafa;
  transition: box-shadow 0.3s;
}

.thread-list-item:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.thread-title {
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: black;
}

.thread-content {
  color: #444;
}
</style>
