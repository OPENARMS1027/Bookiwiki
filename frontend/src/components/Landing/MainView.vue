<template>
  <div class="hero-section">
    <div class="hero-content">
      <h1 class="hero-title">
        <span class="hello-text">Hello</span>
        <span class="bookiwiki-text">Bookiwiki</span>
      </h1>
      <p class="hero-subtitle">당신의 독서 여정을 함께합니다</p>
      <div class="hero-features">
        <div class="feature-item">
          <i class="fas fa-book-reader"></i>
          <span>독서 기록</span>
        </div>
        <div class="feature-item">
          <i class="fas fa-users"></i>
          <span>독서 커뮤니티</span>
        </div>
        <div class="feature-item">
          <i class="fas fa-map-marker-alt"></i>
          <span>주변 도서관</span>
        </div>
      </div>
    </div>
    <div class="hero-decoration">
      <div class="floating-books">
        <i class="fas fa-book book-1"></i>
        <i class="fas fa-book-open book-2"></i>
        <i class="fas fa-bookmark book-3"></i>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.hero-section {
  min-height: 80vh;
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(76, 175, 80, 0.05) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding: 2rem;
}

.hero-content {
  text-align: center;
  max-width: 800px;
  z-index: 1;
}

.hero-title {
  font-size: 5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  animation: fadeInUp 1s ease-out;
}

.hello-text {
  color: #2c3e50;
  display: block;
  font-size: 0.8em;
}

.bookiwiki-text {
  color: #4caf50;
  display: block;
  font-size: 1.2em;
  letter-spacing: -2px;
}

.hero-subtitle {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 3rem;
  animation: fadeInUp 1s ease-out 0.3s both;
}

.hero-features {
  display: flex;
  justify-content: center;
  gap: 3rem;
  animation: fadeInUp 1s ease-out 0.6s both;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: #2c3e50;
}

.feature-item i {
  font-size: 2rem;
  color: #4caf50;
  margin-bottom: 0.5rem;
  transition: transform 0.3s ease;
}

.feature-item:hover i {
  transform: translateY(-5px);
}

.hero-decoration {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  pointer-events: none;
}

.floating-books {
  position: absolute;
  width: 100%;
  height: 100%;
}

.floating-books i {
  position: absolute;
  color: rgba(76, 175, 80, 0.2);
  font-size: 3rem;
}

.book-1 {
  top: 20%;
  left: 15%;
  animation: float 6s ease-in-out infinite;
}

.book-2 {
  top: 60%;
  right: 15%;
  animation: float 8s ease-in-out infinite;
}

.book-3 {
  top: 40%;
  right: 25%;
  animation: float 7s ease-in-out infinite;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0);
  }
  50% {
    transform: translateY(-20px) rotate(5deg);
  }
}

@media (max-width: 768px) {
  .hero-section {
    min-height: 70vh;
    padding: 1rem;
  }

  .hero-title {
    font-size: 3.5rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }

  .hero-features {
    gap: 1.5rem;
    flex-wrap: wrap;
  }

  .feature-item {
    font-size: 0.9rem;
  }

  .feature-item i {
    font-size: 1.5rem;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .hero-features {
    gap: 1rem;
  }
}
</style>