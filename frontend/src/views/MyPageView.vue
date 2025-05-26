<template>
  <div>
    <h1>마이페이지</h1>
    <Profile />
    <MyThreads />
    <Archive />
  </div>
</template>

<script setup>
import Profile from '@/components/MyPage/Profile.vue'
import MyThreads from '@/components/MyPage/MyThreads.vue'
import Archive from '@/components/MyPage/Archive.vue'
</script>

<style scoped></style>
