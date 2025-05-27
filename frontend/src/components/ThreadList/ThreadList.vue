<template>
  <div class="thread-container">
    <div class="search-section">
      <div class="search-box">
        <font-awesome-icon :icon="['fas', 'search']" class="search-icon" />
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="스레드 검색 (제목, 내용으로 검색)"
          class="search-input"
        >
      </div>
    </div>
    <div class="thread-grid">
      <div v-for="thread in filteredThreads" :key="thread.id" class="thread-item">
        <RouterLink
          :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
        >
          <ThreadItem :thread="thread" />
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, watch, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import ThreadItem from '@/components/ThreadList/ThreadItem.vue'

const route = useRoute()
const store = useBookStore()
const searchQuery = ref('')

const threads = computed(() => store.threads)

const filteredThreads = computed(() => {
  if (!searchQuery.value) return threads.value
  
  const query = searchQuery.value.toLowerCase()
  return threads.value.filter(thread => 
    thread.title.toLowerCase().includes(query) ||
    thread.content.toLowerCase().includes(query)
  )
})

onMounted(() => {
  store.getThreads()
})

watch(
  () => route.fullPath,
  () => {
    store.getThreads()
  }
)
</script>

<style scoped>
.thread-container {
  padding: 2rem;
  min-height: 100vh;
}

.search-section {
  max-width: 1400px;
  margin: 0 auto 2rem;
  padding: 0 1rem;
}

.search-box {
  position: relative;
  max-width: 600px;
  margin: 0 auto;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #4CAF50;
  opacity: 0.8;
}

.search-input {
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 12px;
  font-size: 1rem;
  background: transparent;
  color: inherit;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.2);
}

.search-input::placeholder {
  color: rgba(76, 175, 80, 0.5);
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.thread-item {
  transition: all 0.3s ease;
}

.thread-item a {
  text-decoration: none;
  color: inherit;
  display: block;
}

@media (max-width: 768px) {
  .thread-container {
    padding: 1rem;
  }
  
  .search-section {
    margin-bottom: 1.5rem;
  }
  
  .search-input {
    font-size: 0.95rem;
    padding: 0.75rem 0.75rem 0.75rem 2.5rem;
  }
  
  .search-icon {
    left: 0.75rem;
  }
  
  .thread-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }
}
</style>
