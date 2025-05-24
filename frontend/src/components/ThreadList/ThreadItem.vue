<template>
  <div class="card">
    <img :src="thread.cover" />
    <p>{{ thread.title }}</p>
    <p>{{ thread.content }}</p>
  </div>
</template>

<script setup>
import '@/style/ThreadsList/ThreadItem.css'

defineProps({
  thread: Object,
})
</script>

<style scoped></style>
