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
  defineProps({
    thread: Object,
  })
  
  // const gotoDetail = (id) => {
  //   router.push(`/thread/${id}`)
  // }
  </script>
  
  <style scoped>
  .card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 16px;
    margin: 16px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 240px;
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    background-color: #fff;
  }
  
  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.15);
  }
  
  .card img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    margin-bottom: 12px;
    object-fit: cover;
  }
  
  .card h2 {
    font-size: 1.2rem;
    margin: 0;
    text-align: center;
  }
  
  .card p {
    font-size: 0.9rem;
    color: #555;
    text-align: center;
    margin-top: 8px;
  }
  </style>
  