<template>
  <div class="thread-section">
    <div class="section-header">
      <h3 class="section-title">
        <i class="fas fa-comments"></i>
        스레드 목록
      </h3>
    </div>
    <div class="thread-list">
      <div v-if="bookThreads && bookThreads.length > 0">
        <div
          v-for="thread in bookThreads"
          :key="thread.id"
          class="thread-item"
          @click="moveToThread(thread.id)"
        >
          <div class="thread-info">
            <p class="thread-title">{{ thread.title }}</p>
            <div class="thread-meta">
              <span class="likes">
                <i class="fas fa-heart"></i> {{ thread.likes.length }}
              </span>
              <span class="comments">
                <i class="fas fa-comment"></i> {{ thread.comments_count }}
              </span>
              <span class="date">{{ formatDate(thread.created_at) }}</span>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="no-threads">작성된 스레드가 없습니다</div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useBookStore } from "@/stores/book";

const props = defineProps({
  book: Object,
});

const router = useRouter();
const store = useBookStore();
const threads = computed(() => store.threads);

async function fetchData() {
  await store.getThreads();
}

onMounted(() => {
  fetchData();
});

const bookThreads = computed(() => {
  if (!props.book || !threads.value) return [];
  return threads.value.filter((thread) => {
    return Number(thread.book.id) === props.book.id;
  });
});

const moveToThread = (threadId) => {
  router.push({ name: "threadDetail", params: { threadId } });
};

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("ko-KR");
};
</script>

<style scoped>
.thread-section {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.section-header {
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid rgba(76, 175, 80, 0.1);
}

.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.section-title i {
  color: #4caf50;
  font-size: 0.9em;
}

.thread-list {
  display: flex;
  flex-direction: column;
}

.thread-item {
  padding: 0.75rem;
  cursor: pointer;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.thread-item:last-child {
  border-bottom: none;
}

.thread-item:hover {
  background: rgba(76, 175, 80, 0.03);
}

.thread-title {
  margin: 0 0 0.4rem;
  color: #2c3e50;
  font-size: 1rem;
  font-weight: 500;
}

.thread-meta {
  display: flex;
  gap: 1rem;
  color: #666;
  font-size: 0.9rem;
}

.likes,
.comments {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.date {
  margin-left: auto;
  color: #888;
  font-size: 0.85rem;
}

.no-threads {
  text-align: center;
  padding: 1.5rem;
  color: #666;
  font-size: 0.95rem;
}

@media (max-width: 768px) {
  .thread-section {
    padding: 1rem;
  }

  .section-title {
    font-size: 1rem;
  }

  .thread-item {
    padding: 0.6rem;
  }

  .thread-title {
    font-size: 0.95rem;
  }

  .thread-meta {
    font-size: 0.85rem;
    gap: 0.75rem;
  }
}
</style>
