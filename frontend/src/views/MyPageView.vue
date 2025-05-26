<template>
  <div class="mypage-container">
    <div class="content-wrapper">
      <section class="profile-section">
        <Profile />
      </section>
      <div class="content-grid">
        <section class="threads-section">
          <MyThreads />
        </section>
        <section class="archive-section">
          <Archive />
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
import Profile from '@/components/MyPage/Profile.vue'
import MyThreads from '@/components/MyPage/MyThreads.vue'
import Archive from '@/components/MyPage/Archive.vue'
</script>

<style scoped>
.mypage-container {
  min-height: 100vh;
  background: rgba(76, 175, 80, 0.02);
  padding: 2rem;
}

.content-wrapper {
  max-width: 1600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 0 1rem;
}

.profile-section {
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  overflow: hidden;
  padding: 2rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.threads-section,
.archive-section {
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  padding: 2rem;
  height: 100%;
  min-height: 400px;
}

@media (max-width: 1200px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .mypage-container {
    padding: 1rem;
  }

  .content-wrapper {
    gap: 1.5rem;
  }

  .threads-section,
  .archive-section {
    padding: 1.5rem;
  }
}
</style>
