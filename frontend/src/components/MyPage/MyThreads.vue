<template>
  <div class="my-threads">
    <h2>내가 작성한 스레드</h2>
    <div v-if="loading" class="loading">
      <font-awesome-icon :icon="['fas', 'spinner']" spin />
      <span>로딩 중...</span>
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <div v-else class="thread-list">
      <div v-if="myThreads.length === 0" class="no-threads">
        작성한 스레드가 없습니다.
      </div>
      <div v-else>
        <div
          v-for="thread in myThreads"
          :key="thread.id"
          class="thread-card"
          @click="goToThread(thread.id)"
        >
          <div class="thread-header">
            <h3>{{ thread.title }}</h3>
            <div class="thread-book">
              {{ thread.book.title }}
            </div>
          </div>
          <div class="thread-stats">
            <div class="stat">
              <font-awesome-icon :icon="['fas', 'heart']" />
              <span>{{ thread.likes_count }}</span>
            </div>
            <div class="stat">
              <font-awesome-icon :icon="['fas', 'comment']" />
              <span>{{ thread.comments_count }}</span>
            </div>
            <div class="thread-date">
              {{ formatDate(thread.created_at) }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const threads = ref([])
const loading = ref(true)
const error = ref(null)

const myThreads = computed(() => {
  if (userStore.thisUser) {
    return threads.value.filter(
      (thread) => thread.user === userStore.thisUser.id
    )
  }
})

const fetchThreads = async () => {
  try {
    loading.value = true
    const response = await axios.get('http://127.0.0.1:8000/threads/')
    threads.value = response.data
  } catch (err) {
    error.value = '스레드를 불러오는데 실패했습니다.'
    console.error('Error fetching threads:', err)
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

const goToThread = (threadId) => {
  router.push(`/threads/${threadId}`)
}

onMounted(async () => {
  await userStore.getThisUser()
  await fetchThreads()
})
</script>

<style scoped>
.my-threads {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.loading,
.error {
  text-align: center;
  padding: 20px;
  color: #666;
}

.thread-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.thread-card {
  background: white;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.2s ease;
}

.thread-card:hover {
  transform: translateY(-2px);
}

.thread-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.thread-header h3 {
  margin: 0;
  color: #333;
  font-size: 1.1em;
}

.thread-book {
  color: #666;
  font-size: 0.9em;
}

.thread-stats {
  display: flex;
  align-items: center;
  gap: 20px;
  color: #666;
  font-size: 0.9em;
}

.stat {
  display: flex;
  align-items: center;
  gap: 5px;
}

.thread-date {
  margin-left: auto;
  color: #888;
}

.no-threads {
  text-align: center;
  padding: 30px;
  color: #666;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
