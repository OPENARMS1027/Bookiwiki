<template>
  <div class="card-container">
    <div v-for="thread in threads" :key="thread.id" class="card-item">
      <RouterLink
        :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
      >
        <ThreadItem :thread="thread" />
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useBookStore } from '@/stores/book.js'
import ThreadItem from '@/components/ThreadList/ThreadItem.vue'
import '@/style/ThreadsList/ThreadList.css'

const route = useRoute()
const store = useBookStore()
const threads = computed(() => store.threads)

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

<style scoped></style>
