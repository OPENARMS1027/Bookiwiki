<template>
  <div class="container">
    <div class="nav-main">
      <RouterLink :to="{ name: 'main' }">메인</RouterLink>
    </div>
    <div class="nav-content">
      <RouterLink :to="{ name: 'threadList' }">스레드</RouterLink
      >&nbsp;&nbsp;&nbsp;
      <RouterLink :to="{ name: 'bookList' }">도서 검색</RouterLink
      >&nbsp;&nbsp;&nbsp;
      <RouterLink :to="{ name: 'myPage' }">마이페이지</RouterLink
      >&nbsp;&nbsp;&nbsp;
      <RouterLink :to="{ name: '' }">로그인</RouterLink>&nbsp;&nbsp;&nbsp;
      <RouterLink :to="{ name: '' }">로그아웃</RouterLink>&nbsp;&nbsp;&nbsp;
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  text-decoration: none;
  background-color: #327729;
  padding: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}

.container a {
  text-decoration: none;
  color: white;
}

.container a:hover {
  text-decoration: underline;
}
</style>
