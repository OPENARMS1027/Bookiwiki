<template>
  <div>
    <Navigation />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navigation from '@/components/Layout/Navigation.vue'
</script>

<style scoped></style>
