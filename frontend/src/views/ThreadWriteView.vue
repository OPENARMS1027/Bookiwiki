<template>
    <div v-if="book">
      <ThreadWrite :book="book" />
      <ThreadForm :book="book" />
    </div>
  </template>
  
  <script setup>
  import { useRoute } from 'vue-router'
  import { useBookStore } from '@/stores/book.js'
  import ThreadWrite from '@/components/ThreadWrite/ThreadWrite.vue'
  import ThreadForm from '@/components/ThreadWrite/ThreadForm.vue'
  import { onMounted, ref } from 'vue'
  
  const route = useRoute()
  const store = useBookStore()
  const bookPk = Number(route.params.bookId)

  const book = ref(null)

  onMounted(() => {
    store.getBooks()
  })

</script>

  
  <style scoped></style>
  