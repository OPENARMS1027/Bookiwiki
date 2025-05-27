<template>
  <div class="detail-container">
    <div class="detail-content">
      <div class="main-section">
        <BookInfo :book="book" />
        <VoiceOfAi :book="book" />
        <BookThread :book="book" />
      </div>
      <div class="side-section">
        <AiRecommend :book="book" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import { useBookStore } from "@/stores/book";
import BookInfo from "@/components/BookDetail/BookInfo.vue";
import AuthorInfo from "@/components/BookDetail/AuthorInfo.vue";
import BookThread from "@/components/BookDetail/BookThread.vue";
import VoiceOfAi from "@/components/BookDetail/VoiceOfAi.vue";
import AiRecommend from "@/components/BookDetail/AiRecommend.vue";

const route = useRoute();
const store = useBookStore();
const book = ref(null);

async function fetchData() {
  const bookPk = Number(route.params.bookId);
  const bookData = await store.getBook(bookPk);
  book.value = bookData;
}

// 라우트 파라미터가 변경될 때마다 데이터를 다시 불러옴
watch(
  () => route.params.bookId,
  async (newId) => {
    if (newId) {
      await fetchData();
    }
  }
);

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
.detail-container {
  padding: 2rem;
  min-height: 100vh;
  background: rgba(76, 175, 80, 0.02);
}

.detail-content {
  display: flex;
  gap: 2.5rem;
  max-width: 1600px;
  margin: 0 auto;
  position: relative;
}

.main-section {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 1000px;
}

.side-section {
  width: 520px;
  flex-shrink: 0;
  position: sticky;
  top: 2rem;
  height: calc(100vh - 4rem);
  overflow-y: auto;
  padding-right: 1rem;
  scrollbar-width: thin;
  scrollbar-color: rgba(76, 175, 80, 0.3) transparent;
}

.side-section::-webkit-scrollbar {
  width: 6px;
}

.side-section::-webkit-scrollbar-track {
  background: transparent;
}

.side-section::-webkit-scrollbar-thumb {
  background-color: rgba(76, 175, 80, 0.3);
  border-radius: 3px;
}

@media (max-width: 1600px) {
  .side-section {
    width: 480px;
  }
}

@media (max-width: 1400px) {
  .side-section {
    width: 440px;
  }
}

@media (max-width: 1200px) {
  .detail-content {
    flex-direction: column;
  }

  .main-section {
    max-width: 100%;
  }

  .side-section {
    width: 100%;
    position: relative;
    top: 0;
    height: auto;
    padding-right: 0;
  }
}

@media (max-width: 768px) {
  .detail-container {
    padding: 1rem;
  }

  .detail-content {
    gap: 2rem;
  }

  .main-section {
    gap: 1.5rem;
  }
}
</style>
