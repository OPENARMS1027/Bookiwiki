<template>
  <div class="thread-card">
    <div class="thread-icon">
      <font-awesome-icon :icon="['fas', 'book-open']" />
    </div>
    <div class="thread-content">
      <h3 class="thread-title">{{ thread.title }}</h3>
      <p class="thread-text">{{ thread.content }}</p>
    </div>
    <div class="thread-footer">
      <font-awesome-icon :icon="['fas', 'comments']" />
      <span>댓글 보기</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  thread: Object,
})
</script>

<style scoped>
.thread-card {
  border: 1px solid rgba(76, 175, 80, 0.1);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  background: transparent;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.thread-card:hover {
  border-color: rgba(76, 175, 80, 0.3);
  box-shadow: 0 5px 15px rgba(76, 175, 80, 0.1);
  transform: translateY(-5px);
}

.thread-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(to right, #4CAF50, #81C784);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.thread-card:hover::before {
  opacity: 1;
}

.thread-icon {
  padding: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(76, 175, 80, 0.05);
  border-bottom: 1px solid rgba(76, 175, 80, 0.1);
}

.thread-icon svg {
  font-size: 2rem;
  color: #4CAF50;
  opacity: 0.8;
  transition: all 0.3s ease;
}

.thread-card:hover .thread-icon svg {
  transform: scale(1.1);
  opacity: 1;
}

.thread-content {
  padding: 1.5rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.thread-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: inherit;
  margin: 0;
  line-height: 1.4;
  position: relative;
  padding-bottom: 0.75rem;
}

.thread-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 2rem;
  height: 2px;
  background: rgba(76, 175, 80, 0.3);
}

.thread-text {
  font-size: 0.95rem;
  color: inherit;
  opacity: 0.8;
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.thread-footer {
  padding: 1rem 1.5rem;
  border-top: 1px solid rgba(76, 175, 80, 0.1);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4CAF50;
  font-size: 0.9rem;
}

.thread-footer svg {
  font-size: 1rem;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .thread-icon {
    padding: 1.5rem;
  }

  .thread-icon svg {
    font-size: 1.75rem;
  }
  
  .thread-content {
    padding: 1rem;
  }
  
  .thread-footer {
    padding: 0.75rem 1rem;
  }
}
</style>
