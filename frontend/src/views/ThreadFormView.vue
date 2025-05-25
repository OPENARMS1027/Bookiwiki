<template>
    <div>
      <ThreadWrite :bookId="bookId" />
      <ThreadBook :bookId="bookId" />
    </div>
  </template>
  
<script setup>
import ThreadWrite from '@/components/ThreadForm/ThreadWrite.vue'
import ThreadBook from '@/components/ThreadForm/ThreadBook.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const bookId = Number(route.params.bookId)
console.log(bookId)


</script>

  
  <style scoped></style>
  