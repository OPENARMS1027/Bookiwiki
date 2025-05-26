<template>
  <div class="thread-section">
    <h2 class="section-title">
      <i class="fas fa-comments"></i>
      추천 스레드
    </h2>
    <p class="section-description">
      관심 장르를 바탕으로 최근 스레드를 추천해드려요
    </p>
    <div class="thread-grid">
      <RouterLink
        v-for="thread in threadList"
        :key="thread.id"
        :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
        class="thread-card"
      >
        <div class="thread-content">
          <h3 class="thread-title">{{ thread.title }}</h3>
          <p class="thread-text">{{ thread.content }}</p>
        </div>
        <div class="thread-meta">
          <span class="meta-item">
            <i class="fas fa-user"></i>
            {{ thread.user }}
          </span>
          <span class="meta-item">
            <i class="fas fa-heart"></i>
            {{ thread.likes.length }}
          </span>
          <span class="meta-item">
            <i class="fas fa-comment"></i>
            {{ thread.comments_count }}
          </span>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import { useBookStore } from "@/stores/book.js";

const store = useBookStore();
const interestedCategory = [1, 2]; // user 정보를 토대로 관심 장르 가져오기
const threadList = ref([]);

onMounted(() => {
  store.getThreads();
  threadList.value = store.threads
    .filter((thread) => interestedCategory.includes(thread.book.category))
    .sort(
      (a, b) =>
        new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime()
    )
    .slice(0, 6);
});
</script>

<style scoped>
.thread-section {
  width: 100%;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-title i {
  color: #4caf50;
  font-size: 1.2em;
}

.section-description {
  color: #666;
  margin-bottom: 2rem;
  font-size: 1.1rem;
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.thread-card {
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  text-decoration: none;
  color: inherit;
  border: 1px solid rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.thread-card:hover {
  transform: translateY(-4px);
  background: white;
  border-color: rgba(76, 175, 80, 0.2);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.thread-content {
  flex-grow: 1;
}

.thread-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.4;
}

.thread-text {
  color: #666;
  font-size: 0.95rem;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.6;
}

.thread-meta {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(0, 0, 0, 0.06);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #666;
  font-size: 0.9rem;
}

.meta-item i {
  color: #4caf50;
  font-size: 0.9em;
}

@media (max-width: 1200px) {
  .thread-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.3rem;
  }

  .section-description {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }

  .thread-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .thread-card {
    padding: 1.25rem;
  }

  .thread-title {
    font-size: 1.05rem;
  }

  .thread-text {
    font-size: 0.9rem;
  }
}
</style>
