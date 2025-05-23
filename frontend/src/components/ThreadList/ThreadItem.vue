<template>
    <!-- <RouterLink  class="card" :to = "{name: 'threadsDetail', params: {threadId: ddddd}}"> -->
    <div class="card">
      <img :src="thread.cover" />
      <p>{{ thread.title }}</p>
      <p>{{ thread.content }}</p>
    </div>
    <!-- </RouterLink> -->
  </template>
  
  <script setup>
  import '@/style/ThreadsList/ThreadItem.css'
  
  defineProps({
    thread: Object,
  })

  </script>
  
  <style scoped>
  </style>
  