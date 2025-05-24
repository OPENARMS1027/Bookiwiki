<template>
  <div>
    <MainView />
    <BestSeller />
    <CategoryBooks />
    <ThreadList />
    <Location />
  </div>
</template>

<script setup>
import MainView from '@/components/Landing/MainView.vue'
import BestSeller from '@/components/Landing/BestSeller.vue'
import CategoryBooks from '@/components/Landing/CategoryBooks.vue'
import ThreadList from '@/components/Landing/ThreadList.vue'
import Location from '@/components/Landing/Location.vue'
</script>

<style scoped></style>
