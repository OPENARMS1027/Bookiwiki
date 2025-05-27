<template>
  <div class="detail-container">
    <div class="detail-wrapper">
      <div class="main-content">
        <div class="thread-info">
          <ThreadInfo
            v-if="thread"
            :thread="thread"
            @update-thread="updateThread"
          />
        </div>
        <div class="comments-section">
          <Comment :threadId="threadId" />
        </div>
      </div>
      <div class="side-content">
        <div class="book-info" v-if="book">
          <BookInfo :book="book" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import { useBookStore } from "@/stores/book.js";
import BookInfo from "@/components/ThreadDetail/BookInfo.vue";
import ThreadInfo from "@/components/ThreadDetail/ThreadInfo.vue";
import Comment from "@/components/ThreadDetail/Comment.vue";

const route = useRoute();
const store = useBookStore();
const threadId = Number(route.params.threadId);

const thread = ref(null);
const book = ref(null);

async function fetchData(threadId) {
  try {
    const threadData = await store.getThread(threadId);
    thread.value = threadData;

    if (threadData?.book?.id) {
      const bookData = await store.getBook(threadData.book.id);
      book.value = bookData;
    }
  } catch (error) {
    console.error(error);
  }
}

const updateThread = (updatedThread) => {
  thread.value = {
    ...thread.value,
    ...updatedThread,
  };
};

onMounted(() => {
  fetchData(threadId);
});

watch(
  () => threadId,
  (newThreadId) => {
    if (newThreadId) {
      fetchData(Number(newThreadId));
    }
  }
);
</script>

<style scoped>
.detail-container {
  padding: 2rem;
  min-height: 100vh;
  background: rgba(76, 175, 80, 0.02);
}

.detail-wrapper {
  display: flex;
  gap: 3rem;
  max-width: 1600px;
  margin: 0 auto;
}

.main-content {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

.thread-info {
  width: 100%;
}

.comments-section {
  width: 100%;
  background: white;
  border: 1px solid rgba(76, 175, 80, 0.1);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
}

.side-content {
  width: 460px;
  flex-shrink: 0;
}

.book-info {
  position: sticky;
  top: 2rem;
  background: white;
  border: 1px solid rgba(76, 175, 80, 0.1);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  padding: 1.5rem;
}

@media (max-width: 1400px) {
  .side-content {
    width: 420px;
  }
}

@media (max-width: 1200px) {
  .detail-wrapper {
    gap: 2rem;
  }

  .side-content {
    width: 380px;
  }
}

@media (max-width: 1024px) {
  .detail-wrapper {
    flex-direction: column;
  }

  .side-content {
    width: 100%;
  }

  .book-info {
    position: static;
    margin-bottom: 2rem;
  }
}

@media (max-width: 768px) {
  .detail-container {
    padding: 1rem;
  }

  .detail-wrapper {
    gap: 1.5rem;
  }

  .main-content {
    gap: 1.5rem;
  }
}
</style>
