<template>
    <div>
      <ThreadWrite :book="book" />
      <ThreadForm :book="book" />
    </div>
  </template>
  
<script setup>
import ThreadWrite from '@/components/ThreadWrite/ThreadWrite.vue'
import ThreadForm from '@/components/ThreadWrite/ThreadForm.vue'
const props = defineProps({
    book: Object,
})  


</script>

  
  <style scoped></style>
  