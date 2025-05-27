<template>
  <div class="thread-form-container">
    <div class="form-content">
      <ThreadWrite :bookId="bookId" />
      <ThreadBook :bookId="bookId" />
    </div>
  </div>
</template>

<script setup>
import ThreadWrite from '@/components/ThreadForm/ThreadWrite.vue'
import ThreadBook from '@/components/ThreadForm/ThreadBook.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const bookId = Number(route.params.bookId)
</script>

<style scoped>
.thread-form-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  min-height: 100vh;
}

.form-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  align-items: start;
}

@media (max-width: 1024px) {
  .form-content {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .thread-form-container {
    padding: 1rem;
  }
}
</style>
  