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
      <div v-if="threads.length === 0" class="no-threads">
        작성한 스레드가 없습니다.
      </div>
      <div v-else>
        <div
          v-for="thread in threads"
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const threads = ref([])
const loading = ref(true)
const error = ref(null)

const fetchMyThreads = async () => {
  try {
    loading.value = true
    const response = await axios.get(
      'https://bookiwiki.onrender.com/my-threads/',
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      }
    )
    if (response.data) {
      threads.value = response.data
    }
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

onMounted(() => {
  fetchMyThreads()
})
</script>

<style scoped>
.my-threads {
  height: 100%;
}

h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

h2::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 1em;
  background-color: #4caf50;
  border-radius: 2px;
}

.loading,
.error {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.thread-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 0 0.5rem;
}

.no-threads {
  text-align: center;
  padding: 3rem 2rem;
  color: #666;
  background: #f8f9fa;
  border-radius: 8px;
  font-size: 0.95rem;
}

.thread-card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.thread-card:hover {
  transform: translateY(-2px);
  border-color: #4caf50;
  background: white;
}

.thread-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.thread-header h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.1rem;
  font-weight: 500;
  line-height: 1.4;
}

.thread-book {
  color: #666;
  font-size: 0.9rem;
  white-space: nowrap;
}

.thread-stats {
  display: flex;
  align-items: center;
  gap: 1rem;
  color: #666;
  font-size: 0.9rem;
}

.stat {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.stat i {
  color: #4caf50;
}

.thread-date {
  margin-left: auto;
  color: #888;
  font-size: 0.85rem;
}

@media (max-width: 768px) {
  h2 {
    font-size: 1.3rem;
    margin-bottom: 1.25rem;
  }

  .thread-card {
    padding: 1rem;
  }

  .thread-header {
    flex-direction: column;
    gap: 0.5rem;
  }

  .thread-header h3 {
    font-size: 1rem;
  }

  .thread-book {
    font-size: 0.85rem;
  }

  .thread-stats {
    flex-wrap: wrap;
    gap: 0.75rem;
  }
}
</style>
