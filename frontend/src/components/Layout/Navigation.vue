<template>
  <nav class="nav-container">
    <div class="nav-main">
      <RouterLink :to="{ name: 'main' }" class="logo-link">
        <font-awesome-icon :icon="['fas', 'book-open']" />
        <span>Bookiwiki</span>
      </RouterLink>
    </div>
    <div class="nav-content">
      <RouterLink :to="{ name: 'threadList' }" class="nav-link">
        <font-awesome-icon :icon="['fas', 'comments']" />
        <span>스레드</span>
      </RouterLink>
      <RouterLink :to="{ name: 'bookList' }" class="nav-link">
        <font-awesome-icon :icon="['fas', 'search']" />
        <span>도서 검색</span>
      </RouterLink>
      <RouterLink :to="{ name: 'myPage' }" class="nav-link">
        <font-awesome-icon :icon="['fas', 'user']" />
        <span>마이페이지</span>
      </RouterLink>
      <div class="auth-links">
        <RouterLink :to="{ name: 'login' }" class="nav-link">로그인</RouterLink>
        <span class="divider">|</span>
        <RouterLink :to="{ name: '' }" class="nav-link">로그아웃</RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: transparent;
  border-bottom: 1px solid rgba(76, 175, 80, 0.2);
  position: sticky;
  top: 0;
  backdrop-filter: blur(10px);
  z-index: 1000;
}

.nav-main {
  flex-shrink: 0;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.4em;
  font-weight: 600;
  color: #4CAF50;
  text-decoration: none;
  transition: all 0.3s ease;
}

.logo-link:hover {
  color: #2E7D32;
  text-decoration: none;
}

.nav-content {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: inherit;
  text-decoration: none;
  font-size: 0.95em;
  font-weight: 500;
  padding: 0.5rem;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #4CAF50;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.nav-link:hover {
  color: #4CAF50;
  text-decoration: none;
}

.nav-link:hover::after {
  transform: scaleX(1);
}

.auth-links {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-left: 1rem;
  padding-left: 1rem;
  border-left: 1px solid rgba(76, 175, 80, 0.2);
}

.divider {
  color: rgba(76, 175, 80, 0.3);
}

@media (max-width: 768px) {
  .nav-container {
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
  }

  .nav-content {
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
  }

  .auth-links {
    margin-left: 0;
    padding-left: 0;
    border-left: none;
    width: 100%;
    justify-content: center;
    margin-top: 0.5rem;
  }
}
</style>
