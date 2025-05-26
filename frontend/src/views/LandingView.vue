<template>
  <div class="landing-container">
    <MainView />
    <div class="content-section">
      <section class="section">
        <BestSeller />
      </section>
      <section class="section">
        <CategoryBooks />
      </section>
      <section class="section">
        <ThreadList />
      </section>
      <section class="section">
        <Location />
      </section>
    </div>
  </div>
</template>

<script setup>
import MainView from "@/components/Landing/MainView.vue";
import BestSeller from "@/components/Landing/BestSeller.vue";
import CategoryBooks from "@/components/Landing/CategoryBooks.vue";
import ThreadList from "@/components/Landing/ThreadList.vue";
import Location from "@/components/Landing/Location.vue";
</script>

<style scoped>
.landing-container {
  min-height: 100vh;
  background: rgba(76, 175, 80, 0.02);
}

.content-section {
  max-width: 1600px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 3rem;
}

.section {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

@media (max-width: 1600px) {
  .content-section {
    max-width: 1200px;
  }
}

@media (max-width: 768px) {
  .content-section {
    padding: 1rem;
    gap: 1.5rem;
  }

  .section {
    padding: 1.5rem;
  }
}
</style>
