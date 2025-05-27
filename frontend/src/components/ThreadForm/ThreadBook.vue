<template>
    <div class="book-info">
      <h3 class="book-info-title">
        <font-awesome-icon :icon="['fas', 'book']" />
        도서 정보
      </h3>
      <div v-if="book" class="book-details">
        <div class="book-cover">
          <img :src="book.cover" alt="도서 표지" />
        </div>
        <div class="book-text">
          <h4 class="book-title">{{ book.title }}</h4>
          <div class="book-meta">
            <p class="meta-item">
              <span class="label">저자</span>
              {{ book.author }}
            </p>
            <p class="meta-item">
              <span class="label">출판사</span>
              {{ book.publisher }}
            </p>
            <p class="meta-item">
              <span class="label">출판일</span>
              {{ book.pub_date }}
            </p>
          </div>
        </div>
      </div>
      <div v-else class="loading-state">
        <font-awesome-icon :icon="['fas', 'spinner']" spin />
        도서 정보를 불러오는 중...
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useBookStore } from '@/stores/book'

  const props = defineProps({
    bookId: {
      type: [String, Number],
      required: true
    }
  })

  const book = ref(null)
  const store = useBookStore()

  onMounted(async () => {
    try {
      const bookData = await store.getBook(props.bookId)
      book.value = bookData
    } catch (error) {
      console.error('도서 정보 로딩 실패:', error)
    }
  })
  </script>
  
  <style scoped>
  .book-info {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    font-family: 'Noto Sans KR', sans-serif;
  }

  .book-info-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .book-info-title svg {
    color: #4caf50;
  }

  .book-details {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .book-cover {
    width: 100%;
    aspect-ratio: 2/3;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .book-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .book-text {
    flex: 1;
  }

  .book-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 1rem;
    line-height: 1.4;
  }

  .book-meta {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .meta-item {
    margin: 0;
    font-size: 0.95rem;
    color: #666;
    display: flex;
    gap: 0.5rem;
  }

  .label {
    color: #4caf50;
    font-weight: 500;
    min-width: 4rem;
  }

  .loading-state {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    height: 200px;
    color: #4caf50;
    font-size: 0.95rem;
  }

  @media (max-width: 1024px) {
    .book-details {
      flex-direction: row;
    }

    .book-cover {
      width: 150px;
    }
  }

  @media (max-width: 768px) {
    .book-info {
      padding: 1rem;
    }

    .book-info-title {
      font-size: 1.1rem;
      margin-bottom: 1rem;
    }

    .book-details {
      flex-direction: column;
      gap: 1rem;
    }

    .book-cover {
      width: 120px;
      margin: 0 auto;
    }

    .book-title {
      font-size: 1rem;
      text-align: center;
    }

    .book-meta {
      align-items: center;
    }
  }
  </style>
  