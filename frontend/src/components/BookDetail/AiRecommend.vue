<template>
  <div class="recommend-container" v-if="book">
    <div class="ai-badge">
      <i class="fas fa-robot"></i>
      AI 도서 추천
    </div>
    <!-- 작가의 다른 책 추천 -->
    <div class="recommend-section">
      <h3 class="section-title">
        <i class="fas fa-book"></i>
        {{ book.author }} 작가의 다른 책
      </h3>
      <div class="book-list-container" v-if="authorBooks.length">
        <button
          class="nav-button prev"
          @click="scrollAuthorBooks('prev')"
          :disabled="authorCurrentIndex === 0"
        >
          <i class="fas fa-chevron-left"></i>
        </button>
        <div class="book-list" ref="authorBookList">
          <div
            v-for="(recommendBook, index) in authorBooks"
            :key="recommendBook.id"
            class="book-card"
            v-show="
              index >= authorCurrentIndex &&
              index < authorCurrentIndex + itemsToShow
            "
            @click="moveToBook(recommendBook.id)"
          >
            <div class="book-image-container">
              <img
                :src="recommendBook.cover"
                :alt="recommendBook.title"
                class="book-cover"
              />
            </div>
            <div class="book-info">
              <p class="book-title">{{ recommendBook.title }}</p>
              <p class="book-detail">
                {{ recommendBook.publisher }} | {{ recommendBook.pub_date }}
              </p>
            </div>
          </div>
        </div>
        <button
          class="nav-button next"
          @click="scrollAuthorBooks('next')"
          :disabled="authorCurrentIndex >= authorBooks.length - itemsToShow"
        >
          <i class="fas fa-chevron-right"></i>
        </button>
      </div>
      <p v-else class="no-results">작가의 다른 책이 없습니다.</p>
    </div>

    <!-- 같은 카테고리 책 추천 -->
    <div class="recommend-section">
      <h3 class="section-title">
        <i class="fas fa-tags"></i>
        비슷한 카테고리의 책
      </h3>
      <div class="book-list-container" v-if="categoryBooks.length">
        <button
          class="nav-button prev"
          @click="scrollCategoryBooks('prev')"
          :disabled="categoryCurrentIndex === 0"
        >
          <i class="fas fa-chevron-left"></i>
        </button>
        <div class="book-list" ref="categoryBookList">
          <div
            v-for="(recommendBook, index) in categoryBooks"
            :key="recommendBook.id"
            class="book-card"
            v-show="
              index >= categoryCurrentIndex &&
              index < categoryCurrentIndex + itemsToShow
            "
            @click="moveToBook(recommendBook.id)"
          >
            <div class="book-image-container">
              <img
                :src="recommendBook.cover"
                :alt="recommendBook.title"
                class="book-cover"
              />
            </div>
            <div class="book-info">
              <p class="book-title">{{ recommendBook.title }}</p>
              <p class="book-detail">
                {{ recommendBook.author }} | {{ recommendBook.publisher }}
              </p>
            </div>
          </div>
        </div>
        <button
          class="nav-button next"
          @click="scrollCategoryBooks('next')"
          :disabled="categoryCurrentIndex >= categoryBooks.length - itemsToShow"
        >
          <i class="fas fa-chevron-right"></i>
        </button>
      </div>
      <p v-else class="no-results">추천할 만한 책이 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book'

const props = defineProps({
  book: Object,
})

const router = useRouter()
const store = useBookStore()
const books = computed(() => store.books)

// 한 번에 보여줄 아이템 수
const itemsToShow = 3

// 현재 인덱스 관리
const authorCurrentIndex = ref(0)
const categoryCurrentIndex = ref(0)

// 자동 스크롤 타이머
const authorScrollTimer = ref(null)
const categoryScrollTimer = ref(null)
const scrollInterval = 6000 // 6초마다 스크롤

// 애니메이션 상태
const isAnimating = ref(false)

// 작가의 다른 책 필터링
const authorBooks = computed(() => {
  if (!props.book || !books.value) return []
  return books.value
    .filter((b) => b.author === props.book.author && b.id !== props.book.id)
    .slice(0, 9) // 최대 9권까지 표시 (3의 배수)
})

// 같은 카테고리 책 필터링
const categoryBooks = computed(() => {
  if (!props.book || !books.value) return []
  return books.value
    .filter(
      (b) =>
        b.category === props.book.category &&
        b.id !== props.book.id &&
        b.author !== props.book.author
    )
    .sort(() => Math.random() - 0.5) // 랜덤 정렬
    .slice(0, 9) // 최대 9권까지 표시 (3의 배수)
})

// 자동 스크롤 시작
const startAutoScroll = () => {
  if (authorBooks.value.length > itemsToShow) {
    authorScrollTimer.value = setInterval(() => {
      scrollAuthorBooks('next', true)
    }, scrollInterval)
  }

  if (categoryBooks.value.length > itemsToShow) {
    categoryScrollTimer.value = setInterval(() => {
      scrollCategoryBooks('next', true)
    }, scrollInterval)
  }
}

// 자동 스크롤 정지
const stopAutoScroll = () => {
  if (authorScrollTimer.value) {
    clearInterval(authorScrollTimer.value)
    authorScrollTimer.value = null
  }
  if (categoryScrollTimer.value) {
    clearInterval(categoryScrollTimer.value)
    categoryScrollTimer.value = null
  }
}

// 작가 책 목록 스크롤
const scrollAuthorBooks = (direction, isAuto = false) => {
  if (isAnimating.value && !isAuto) return
  if (!isAuto) stopAutoScroll()

  isAnimating.value = true
  setTimeout(() => {
    isAnimating.value = false
  }, 600) // transition duration과 동일하게 설정

  const bookList = document.querySelector('.book-list')
  if (direction === 'next') {
    if (authorCurrentIndex.value >= authorBooks.value.length - itemsToShow) {
      authorCurrentIndex.value = 0
    } else {
      authorCurrentIndex.value += 1
    }
  } else if (direction === 'prev') {
    if (authorCurrentIndex.value <= 0) {
      authorCurrentIndex.value = authorBooks.value.length - itemsToShow
    } else {
      authorCurrentIndex.value -= 1
    }
  }

  if (bookList) {
    bookList.style.setProperty('--slide-index', authorCurrentIndex.value)
  }

  if (!isAuto) {
    setTimeout(startAutoScroll, 600)
  }
}

// 카테고리 책 목록 스크롤
const scrollCategoryBooks = (direction, isAuto = false) => {
  if (isAnimating.value && !isAuto) return
  if (!isAuto) stopAutoScroll()

  isAnimating.value = true
  setTimeout(() => {
    isAnimating.value = false
  }, 600)

  const bookList = document.querySelector('.book-list')
  if (direction === 'next') {
    if (
      categoryCurrentIndex.value >=
      categoryBooks.value.length - itemsToShow
    ) {
      categoryCurrentIndex.value = 0
    } else {
      categoryCurrentIndex.value += 1
    }
  } else if (direction === 'prev') {
    if (categoryCurrentIndex.value <= 0) {
      categoryCurrentIndex.value = categoryBooks.value.length - itemsToShow
    } else {
      categoryCurrentIndex.value -= 1
    }
  }

  if (bookList) {
    bookList.style.setProperty('--slide-index', categoryCurrentIndex.value)
  }

  if (!isAuto) {
    setTimeout(startAutoScroll, 600)
  }
}

// 책 상세 페이지로 이동
const moveToBook = async (bookId) => {
  stopAutoScroll()
  try {
    await router.push({
      path: `/books/${bookId}`,
    })
  } catch (err) {
    console.error('라우터 에러:', err)
  }
}

// 컴포넌트 마운트/언마운트 처리
onMounted(() => {
  if (props.book && (!books.value || !books.value.length)) {
    store.getBooks().then(() => {
      startAutoScroll()
    })
  } else {
    startAutoScroll()
  }
})

onUnmounted(() => {
  stopAutoScroll()
})

// 책 데이터 변경 감지
watch(
  () => props.book,
  async () => {
    if (props.book && (!books.value || !books.value.length)) {
      await store.getBooks()
      startAutoScroll()
    }
  },
  { immediate: true }
)
</script>

<style scoped>
.recommend-container {
  width: 100%;
  max-width: 1400px;
  margin: 25px auto 15px;
  position: relative;
}

.recommend-section {
  margin-bottom: 20px;
  background-color: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
}

.ai-badge {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #4caf50, #45a049);
  color: white;
  padding: 8px 20px;
  border-radius: 20px;
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
  z-index: 10;
  white-space: nowrap;
}

.ai-badge i {
  font-size: 1.1em;
}

.section-title {
  font-size: 1.2rem;
  color: #2c3e50;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0 24px;
}

.section-title i {
  color: #4caf50;
  font-size: 1.1em;
}

.book-list-container {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  padding: 0 36px;
  overflow: hidden;
}

.book-list {
  display: flex;
  gap: 24px;
  position: relative;
  width: 100%;
  min-height: 260px;
  margin: 0 auto;
  transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1);
  will-change: transform;
}

.book-card {
  flex: 0 0 calc((100% - 48px) / 3);
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  background-color: #f8f9fa;
  overflow: hidden;
  max-width: 200px;
  position: relative;
  z-index: 1;
  border: 1px solid rgba(0, 0, 0, 0.06);
}

.book-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
  border-color: rgba(76, 175, 80, 0.2);
}

.book-image-container {
  width: 100%;
  padding-top: 140%;
  position: relative;
  overflow: hidden;
  background-color: #f1f3f5;
}

.book-cover {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.book-card:hover .book-cover {
  transform: scale(1.05);
}

.book-info {
  padding: 12px;
  background-color: white;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 60px;
}

.book-title {
  font-weight: 600;
  margin: 0;
  color: #2c3e50;
  font-size: 0.95rem;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: center;
}

.book-detail {
  display: none;
}

.nav-button {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-color: white;
  border: 1px solid rgba(76, 175, 80, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  color: #4caf50;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.nav-button:hover:not(:disabled) {
  background-color: #4caf50;
  border-color: #4caf50;
  color: white;
  transform: translateY(-50%) scale(1.1);
}

.nav-button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  border-color: #ddd;
  color: #999;
}

.nav-button.prev {
  left: 0;
}

.nav-button.next {
  right: 0;
}

.no-results {
  color: #666;
  text-align: center;
  padding: 24px;
  font-size: 1rem;
  background-color: #f8f9fa;
  border-radius: 8px;
  margin: 0 36px;
}

@media (max-width: 1024px) {
  .book-card {
    flex: 0 0 calc((100% - 40px) / 3);
    max-width: 180px;
  }

  .book-list {
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .recommend-section {
    padding: 16px;
  }

  .section-title {
    padding: 0 16px;
    font-size: 1.1rem;
    margin-bottom: 16px;
  }

  .book-list-container {
    padding: 0 24px;
  }

  .book-card {
    flex: 0 0 calc((100% - 32px) / 3);
    max-width: 160px;
  }

  .book-list {
    gap: 16px;
  }

  .book-info {
    padding: 10px;
  }

  .book-title {
    font-size: 0.9rem;
  }

  .nav-button {
    width: 32px;
    height: 32px;
  }
}
</style>
