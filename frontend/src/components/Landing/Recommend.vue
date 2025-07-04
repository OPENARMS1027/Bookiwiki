<template>
  <div class="recommend-section">
    <div class="recommend-container">
      <div v-if="loading" class="loading">
        <font-awesome-icon :icon="['fas', 'spinner']" spin />
        <span> 추천 도서를 찾고 있습니다...</span>
      </div>
      <div v-else-if="!userStore.isLogin" class="login-prompt">
        <p>
          <router-link to="/login" class="login-text">로그인</router-link>하고
          맞춤 도서 추천을 받아보세요!
        </p>
        <button @click="goToLogin" class="login-btn">로그인하기</button>
      </div>
      <div v-else-if="recommendedBooks.length === 0" class="no-books">
        <p>아직 관심 카테고리나 내 서재에 책이 없습니다.</p>
        <p>관심 카테고리를 설정하거나 책을 서재에 추가해보세요!</p>
      </div>
      <div v-else class="book-slider">
        <h2 class="recommend-title">
          <span class="highlight">맞춤 도서 추천</span>
        </h2>
        <Transition name="slide" mode="out-in">
          <div :key="currentBookIndex" class="book-slide">
            <div class="book-content" @click="goToAladin(currentBook.link)">
              <div class="book-image">
                <img :src="currentBook.cover" :alt="currentBook.title" />
                <div class="image-overlay"></div>
              </div>
              <div class="book-info">
                <div class="book-info-inner">
                  <span class="label">오늘의 추천</span>
                  <h3 class="book-title">{{ currentBook.title }}</h3>
                  <p class="book-author">{{ currentBook.author }}</p>
                  <p class="book-description">{{ currentBook.description }}</p>
                  <button class="view-detail">자세히 보기</button>
                </div>
              </div>
            </div>
          </div>
        </Transition>
        <div class="slider-controls">
          <button
            class="control-btn prev"
            @click="prevBook"
            :disabled="currentBookIndex === 0"
          >
            <font-awesome-icon :icon="['fas', 'chevron-left']" />
          </button>
          <div class="slider-dots">
            <span
              v-for="(_, index) in recommendedBooks"
              :key="index"
              :class="['dot', { active: index === currentBookIndex }]"
              @click="goToBook(index)"
            ></span>
          </div>
          <button
            class="control-btn next"
            @click="nextBook"
            :disabled="currentBookIndex === recommendedBooks.length - 1"
          >
            <font-awesome-icon :icon="['fas', 'chevron-right']" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios'

const router = useRouter()
const userStore = useUserStore()
const loading = ref(true)
const recommendedBooks = ref([])
const currentBookIndex = ref(0)
const autoSlideInterval = ref(null)
const UPSTAGE_API_KEY = import.meta.env.VITE_UPSTAGE_API_KEY

const currentBook = computed(() => {
  const book = recommendedBooks.value[currentBookIndex.value] || {}
  if (book) {
    // HTML 엔티티 디코딩 및 특수 문자 처리
    return {
      ...book,
      title: book.title
        ?.replace(/&[^;]+;/g, (match) => {
          const entities = {
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
            '&quot;': '"',
            '&#39;': "'",
            '&nbsp;': ' ',
          }
          return entities[match] || match
        })
        .replace(/[\\]/g, ''),
      author: book.author
        ?.replace(/&[^;]+;/g, (match) => {
          const entities = {
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
            '&quot;': '"',
            '&#39;': "'",
            '&nbsp;': ' ',
          }
          return entities[match] || match
        })
        .replace(/[\\]/g, ''),
      description: book.description
        ?.replace(/&[^;]+;/g, (match) => {
          const entities = {
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
            '&quot;': '"',
            '&#39;': "'",
            '&nbsp;': ' ',
          }
          return entities[match] || match
        })
        .replace(/[\\]/g, ''),
    }
  }
  return {}
})

const nextBook = () => {
  if (currentBookIndex.value < recommendedBooks.value.length - 1) {
    currentBookIndex.value++
  } else {
    currentBookIndex.value = 0
  }
  resetAutoSlide()
}

const prevBook = () => {
  if (currentBookIndex.value > 0) {
    currentBookIndex.value--
  } else {
    currentBookIndex.value = recommendedBooks.value.length - 1
  }
  resetAutoSlide()
}

const goToBook = (index) => {
  currentBookIndex.value = index
  resetAutoSlide()
}

const startAutoSlide = () => {
  autoSlideInterval.value = setInterval(() => {
    nextBook()
  }, 4000)
}

const resetAutoSlide = () => {
  if (autoSlideInterval.value) {
    clearInterval(autoSlideInterval.value)
  }
  startAutoSlide()
}

const goToLogin = () => {
  router.push({ name: 'login' })
}

const goToBookDetail = (book) => {
  router.push({
    name: 'bookDetail',
    params: {
      id: book.itemId,
    },
  })
}

const goToAladin = (link) => {
  if (link) {
    window.open(link, '_blank')
  }
}

const getEmbeddings = async (texts) => {
  try {
    const response = await axios.post(
      'https://api.upstage.ai/v1/solar/embeddings',
      {
        model: 'embedding-passage',
        input: texts,
      },
      {
        headers: {
          Authorization: `Bearer ${UPSTAGE_API_KEY}`,
          'Content-Type': 'application/json',
        },
      }
    )
    return response.data.data.map((item) => item.embedding)
  } catch (error) {
    console.error('Error getting embeddings:', error)
    return []
  }
}

const getAladinBooks = async (query) => {
  try {
    const response = await axios.get(
      `https://bookiwiki.onrender.com/aladin/search/`,
      {
        params: {
          Query: query,
        },
      }
    )

    const data = response.data
    console.log('Aladin API response:', data)

    if (data.item && Array.isArray(data.item)) {
      return data.item.map((book) => {
        console.log('Book cover URLs:', {
          coverLargeUrl: book.coverLargeUrl,
          cover: book.cover,
          coverUrl: book.coverUrl,
        })

        // 이미지 URL 처리
        let coverImage = book.coverLargeUrl || book.cover || book.coverUrl

        // http를 https로 변경
        if (coverImage && coverImage.startsWith('http:')) {
          coverImage = coverImage.replace('http:', 'https:')
        }

        return {
          ...book,
          description: book.description || book.title,
          cover: coverImage,
        }
      })
    }
    return []
  } catch (error) {
    console.error('Error fetching books from Aladin:', error)
    return []
  }
}

const extractKeywords = (books) => {
  // 책 제목에서 주요 키워드 추출
  const bookKeywords = books.flatMap((book) =>
    book
      .split(/[\s,/\(\)]/)
      .filter(
        (word) =>
          word.length >= 2 &&
          !word.match(/[은는이가을를의]$/) &&
          !word.match(/^[0-9]+$/)
      )
  )

  // 중복 제거
  return [...new Set(bookKeywords)].filter((keyword) => keyword.length > 0)
}

const getRecommendations = async () => {
  if (!userStore.thisUser) return

  loading.value = true
  try {
    const userBooks = userStore.thisUser.books.map((book) => book.title)
    console.log('User Books:', userBooks)

    // 내 서재가 비어있는 경우 베스트셀러 추천
    if (userBooks.length === 0) {
      const defaultQueries = ['베스트셀러', '스테디셀러']
      const books = []
      for (const query of defaultQueries) {
        const aladinBooks = await getAladinBooks(query)
        books.push(...aladinBooks)
      }
      recommendedBooks.value = books.slice(0, 6)
      loading.value = false
      return
    }

    // 내 서재의 책 제목에서 키워드 추출
    const keywords = extractKeywords(userBooks)
    console.log('Extracted keywords:', keywords)

    // 키워드별로 책 검색
    const books = []
    for (const keyword of keywords) {
      if (books.length >= 20) break // 충분한 책을 찾으면 중단
      const aladinBooks = await getAladinBooks(keyword)
      if (aladinBooks && aladinBooks.length > 0) {
        console.log(
          `Found ${aladinBooks.length} books for keyword "${keyword}"`
        )
        books.push(...aladinBooks)
      }
    }

    // 중복 제거 (itemId 기준)
    const uniqueBooks = Array.from(
      new Map(books.map((book) => [book.itemId, book])).values()
    )

    // 내 서재의 책은 제외
    const filteredBooks = uniqueBooks.filter(
      (book) => !userBooks.includes(book.title)
    )

    if (filteredBooks.length === 0) {
      const bestSellers = await getAladinBooks('베스트셀러')
      recommendedBooks.value = bestSellers
        .filter((book) => !userBooks.includes(book.title))
        .slice(0, 6)
      loading.value = false
      return
    }

    // 책 설명에 대한 임베딩 생성
    const bookDescriptions = filteredBooks.map(
      (book) => book.description || book.title
    )
    const bookEmbeddings = await getEmbeddings(bookDescriptions)

    // 내 서재 책들의 설명에 대한 임베딩 생성
    const userBookEmbeddings = await getEmbeddings(userBooks)

    // 평균 사용자 임베딩 계산
    const avgUserEmbedding = userBookEmbeddings[0].map(
      (_, i) =>
        userBookEmbeddings.reduce((sum, e) => sum + e[i], 0) /
        userBookEmbeddings.length
    )

    // 유사도 계산 및 정렬
    const scores = bookEmbeddings.map((bookEmb, i) => ({
      book: filteredBooks[i],
      score: cosineSimilarity(avgUserEmbedding, bookEmb),
    }))

    scores.sort((a, b) => b.score - a.score)
    recommendedBooks.value = scores.slice(0, 6).map((item) => item.book)
    console.log('Final recommendations:', recommendedBooks.value)
  } catch (error) {
    console.error('Error getting recommendations:', error)
    recommendedBooks.value = []
  } finally {
    loading.value = false
  }
}

const cosineSimilarity = (a, b) => {
  const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0)
  const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0))
  const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0))
  return dotProduct / (magnitudeA * magnitudeB)
}

onMounted(async () => {
  if (userStore.isLogin) {
    try {
      await userStore.getThisUser()
      await getRecommendations()
      startAutoSlide()
    } catch (error) {
      console.error('Error loading recommendations:', error)
      loading.value = false
    }
  } else {
    loading.value = false
  }
})

onBeforeUnmount(() => {
  if (autoSlideInterval.value) {
    clearInterval(autoSlideInterval.value)
  }
})

// 로그인 상태 변경 시에만 추천 갱신
watch(
  () => userStore.isLogin,
  async (newValue) => {
    if (newValue) {
      await userStore.getThisUser()
      await getRecommendations()
    } else {
      recommendedBooks.value = []
    }
  }
)
</script>

<style scoped>
.recommend-section {
  width: 100%;
  background: #ffffff;
  padding: 8rem 0;
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
  overflow: visible;
  font-family: 'Pretendard', sans-serif;
}

.recommend-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  width: 100%;
  position: relative;
}

.recommend-title {
  text-align: center;
  margin-bottom: 4rem;
  font-weight: 800;
  font-size: 2.5rem;
  color: #1a1a1a;
}

.highlight {
  /* background: linear-gradient(to right, #34d399, #3b82f6); */
  -webkit-background-clip: text;
  background-clip: text;
  color: #4caf50;
  padding: 0 0.5rem;
}

.book-slider {
  position: relative;
  width: 100%;
  height: 600px;
  margin-bottom: 2rem;
}

.book-slide {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem 0;
}

.book-content {
  display: flex;
  gap: 6rem;
  background: #ffffff;
  padding: 3rem;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.5s ease;
  width: 100%;
  position: relative;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  border: 1px solid #f0f0f0;
}

.book-content:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
}

.book-image {
  flex: 0 0 350px;
  position: relative;
  transform: perspective(1000px) rotateY(-5deg);
  transition: transform 0.5s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.book-content:hover .book-image {
  transform: perspective(1000px) rotateY(0deg);
}

.book-image img {
  width: 100%;
  height: auto;
  max-height: 500px;
  object-fit: contain;
  border-radius: 15px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  background: #fff;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.2) 100%
  );
  border-radius: 15px;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.book-content:hover .image-overlay {
  opacity: 1;
}

.book-info {
  flex: 1;
  color: #1a1a1a;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.book-info-inner {
  max-width: 600px;
}

.label {
  display: inline-block;
  background: #4caf50;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: white;
}

.book-title {
  font-size: 3rem;
  margin: 0 0 1rem;
  line-height: 1.2;
  font-weight: 700;
}

.book-author {
  font-size: 1.2rem;
  color: #4b5563;
  margin-bottom: 2rem;
  font-weight: 500;
}

.book-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #4b5563;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 2rem;
}

.view-detail {
  background: #4caf50;
  border: none;
  color: white;
  padding: 1rem 2rem;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
}

.view-detail:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
  background: #66bb6a;
}

.slider-controls {
  position: relative;
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2rem auto 0;
  gap: 2rem;
}

.control-btn {
  position: absolute;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  color: #4caf50;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  font-size: 1.2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  z-index: 10;
}

.control-btn.prev {
  left: 0;
}

.control-btn.next {
  right: 0;
}

.control-btn:hover:not(:disabled) {
  background: #4caf50;
  color: white;
  transform: scale(1.1);
  border-color: transparent;
}

.control-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.slider-dots {
  display: flex;
  gap: 0.8rem;
  background: #ffffff;
  padding: 1rem 2rem;
  border-radius: 30px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #e5e7eb;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: #4caf50;
  transform: scale(1.3);
}

.loading,
.login-prompt,
.no-books {
  text-align: center;
  color: #1a1a1a;
  font-size: 1.2rem;
  padding: 4rem;
  /* font-family: 'Pretendard', sans-serif; */
}

.login-btn {
  margin-top: 1.5rem;
  padding: 1rem 2.5rem;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 30px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
}

.login-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
  background: #66bb6a;
}

.login-text {
  color: #4caf50;
  text-decoration: none;
  font-weight: 600;
  font-family: 'Pretendard', sans-serif;
  transition: color 0.3s ease;
}

.login-text:hover {
  color: #66bb6a;
  text-decoration: underline;
}

/* Slide Transitions */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-enter-from {
  opacity: 0;
  transform: translateX(5%) scale(0.95);
}

.slide-leave-to {
  opacity: 0;
  transform: translateX(-5%) scale(0.95);
}

@media (max-width: 1200px) {
  .book-content {
    gap: 3rem;
    padding: 2rem;
  }

  .book-image {
    flex: 0 0 300px;
  }

  .book-image img {
    height: 450px;
  }

  .book-title {
    font-size: 2.5rem;
  }
}

@media (max-width: 768px) {
  .recommend-section {
    padding: 4rem 0;
  }

  .book-slider {
    height: auto;
    min-height: 800px;
    margin-bottom: 2rem;
  }

  .slider-controls {
    padding: 0 1rem;
    margin-top: 3rem;
    gap: 1rem;
  }

  .control-btn.prev {
    position: static;
  }

  .control-btn.next {
    position: static;
  }

  .slider-dots {
    position: relative;
    transform: none;
    left: auto;
    margin: 1rem 0;
  }

  .book-content {
    flex-direction: column;
    gap: 2rem;
  }

  .book-image {
    flex: none;
    width: 100%;
    max-width: 300px;
    margin: 0 auto;
  }

  .book-image img {
    height: 400px;
  }

  .book-info {
    text-align: center;
  }

  .book-title {
    font-size: 2rem;
  }

  .book-description {
    -webkit-line-clamp: 3;
  }
}
</style>
