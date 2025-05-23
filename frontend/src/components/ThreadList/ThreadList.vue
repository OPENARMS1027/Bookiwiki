<template>
    <div class="card-container">
      <div v-for="thread in threads" :key="thread.id" class="card-item">
        <!-- <RouterLink
          :to="{ name: 'threadsDetail', params: { threadId: thread.id } }"
        > -->
          <ThreadItem :thread="thread" />
        <!-- </RouterLink> -->
      </div>
    </div> 
  </template>
  
  <script setup>
  import { onMounted, computed } from 'vue'
  import { useBookStore } from '@/stores/book.js'
  import ThreadItem from '@/components/ThreadList/ThreadItem.vue'
  import '@/style/ThreadsList/ThreadList.css'

  const store = useBookStore()
  const threads = computed(() => store.threads)

  onMounted(() => {
    store.getThreads()
  })
  </script>
  
  <style scoped>
  </style>
  