<template>
  <div class="app-container">
    <Navigation />
    <div class="main-content">
      <RouterView />
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import Navigation from "@/components/Layout/Navigation.vue";
import Footer from "@/components/Layout/Footer.vue";
</script>

<style>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
}
</style>
