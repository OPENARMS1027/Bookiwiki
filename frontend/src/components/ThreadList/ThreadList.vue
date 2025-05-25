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

  const store = useBookStore()
  const threads = computed(() => store.threads)

  onMounted(() => {
    store.getThreads()
  })
  </script>
  
  <style scoped>
  /* .card-container {
    padding-left: 50px;
    padding-right: 50px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    background-color: #121212; 
    min-height: 100vh; 
    color: #eee; 
  }
  
  .card-item {
    width: 280px;
  }
  
  
  .card-item a {
    text-decoration: none;
    color: #eee; 
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    transition: color 0.3s ease;
  }
  
  .card-item a:hover {
    color: #40a9ff; 
  } */
  </style>
  