<template>
    <div class="recommend-container" v-if="book">
        <!-- 작가의 다른 책 추천 -->
        <div class="recommend-section">
            <h3 class="section-title">
                <i class="fas fa-book"></i>
                {{ book.author }}의 다른 책
            </h3>
            <div class="book-list-container" v-if="authorBooks.length">
                <button class="nav-button prev" @click="scrollAuthorBooks('prev')" :disabled="authorCurrentIndex === 0">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <div class="book-list" ref="authorBookList">
                    <div v-for="(recommendBook, index) in authorBooks" 
                         :key="recommendBook.id" 
                         class="book-card"
                         v-show="index >= authorCurrentIndex && index < authorCurrentIndex + itemsToShow"
                         @click="moveToBook(recommendBook.id)">
                        <div class="book-image-container">
                            <img :src="recommendBook.cover" :alt="recommendBook.title" class="book-cover">
                        </div>
                        <div class="book-info">
                            <p class="book-title">{{ recommendBook.title }}</p>
                            <p class="book-detail">{{ recommendBook.publisher }} | {{ recommendBook.pub_date }}</p>
                        </div>
                    </div>
                </div>
                <button class="nav-button next" @click="scrollAuthorBooks('next')" :disabled="authorCurrentIndex >= authorBooks.length - itemsToShow">
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
                <button class="nav-button prev" @click="scrollCategoryBooks('prev')" :disabled="categoryCurrentIndex === 0">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <div class="book-list" ref="categoryBookList">
                    <div v-for="(recommendBook, index) in categoryBooks" 
                         :key="recommendBook.id" 
                         class="book-card"
                         v-show="index >= categoryCurrentIndex && index < categoryCurrentIndex + itemsToShow"
                         @click="moveToBook(recommendBook.id)">
                        <div class="book-image-container">
                            <img :src="recommendBook.cover" :alt="recommendBook.title" class="book-cover">
                        </div>
                        <div class="book-info">
                            <p class="book-title">{{ recommendBook.title }}</p>
                            <p class="book-detail">{{ recommendBook.author }} | {{ recommendBook.publisher }}</p>
                        </div>
                    </div>
                </div>
                <button class="nav-button next" @click="scrollCategoryBooks('next')" :disabled="categoryCurrentIndex >= categoryBooks.length - itemsToShow">
                    <i class="fas fa-chevron-right"></i>
                </button>
            </div>
            <p v-else class="no-results">추천할 만한 책이 없습니다.</p>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book'

const props = defineProps({
    book: Object
})

const router = useRouter()
const store = useBookStore()
const books = computed(() => store.books)

// 한 번에 보여줄 아이템 수
const itemsToShow = 4

// 현재 인덱스 관리
const authorCurrentIndex = ref(0)
const categoryCurrentIndex = ref(0)

// 작가의 다른 책 필터링
const authorBooks = computed(() => {
    if (!props.book || !books.value) return []
    return books.value
        .filter(b => 
            b.author === props.book.author && 
            b.id !== props.book.id
        )
        .slice(0, 8) // 최대 8권까지 표시
})

// 같은 카테고리 책 필터링
const categoryBooks = computed(() => {
    if (!props.book || !books.value) return []
    return books.value
        .filter(b => 
            b.category === props.book.category && 
            b.id !== props.book.id && 
            b.author !== props.book.author
        )
        .sort(() => Math.random() - 0.5) // 랜덤 정렬
        .slice(0, 8) // 최대 8권까지 표시
})

// 작가 책 목록 스크롤
const scrollAuthorBooks = (direction) => {
    if (direction === 'next' && authorCurrentIndex.value < authorBooks.value.length - itemsToShow) {
        authorCurrentIndex.value += 1
    } else if (direction === 'prev' && authorCurrentIndex.value > 0) {
        authorCurrentIndex.value -= 1
    }
}

// 카테고리 책 목록 스크롤
const scrollCategoryBooks = (direction) => {
    if (direction === 'next' && categoryCurrentIndex.value < categoryBooks.value.length - itemsToShow) {
        categoryCurrentIndex.value += 1
    } else if (direction === 'prev' && categoryCurrentIndex.value > 0) {
        categoryCurrentIndex.value -= 1
    }
}

// 책 상세 페이지로 이동
const moveToBook = async (bookId) => {
    console.log('moveToBook 함수 실행됨, bookId:', bookId)
    try {
        await router.push({
            path: `/books/${bookId}`
        })
    } catch (err) {
        console.error('라우터 에러:', err)
    }
}

// 컴포넌트 마운트 시 모든 책 데이터 가져오기
watch(() => props.book, async () => {
    if (props.book && (!books.value || !books.value.length)) {
        await store.getBooks()
    }
}, { immediate: true })
</script>

<style scoped>
.recommend-container {
    width: 100%;
    max-width: 1200px;
    margin: 20px auto;
    padding: 0 20px;
}

.recommend-section {
    margin-bottom: 30px;
    background-color: white;
    border-radius: 10px;
    padding: 20px 60px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    position: relative;
}

.section-title {
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-title i {
    color: #4CAF50;
}

.book-list-container {
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
}

.book-list {
    display: flex;
    gap: 30px;
    position: relative;
    width: 100%;
    min-height: 300px;
    margin: 0 auto;
}

.book-card {
    flex: 0 0 calc(25% - 22.5px);
    cursor: pointer;
    transition: transform 0.2s;
    display: flex;
    flex-direction: column;
    border-radius: 8px;
    background-color: #f8f9fa;
    overflow: hidden;
    max-width: 200px;
    position: relative;
    z-index: 1;
}

.book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.book-image-container {
    width: 100%;
    padding-top: 130%;
    position: relative;
    overflow: hidden;
}

.book-cover {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.book-info {
    padding: 15px;
    background-color: white;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.book-title {
    font-weight: 500;
    margin-bottom: 8px;
    color: #333;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-height: 1.3;
}

.book-detail {
    font-size: 0.9rem;
    color: #666;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.nav-button {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: white;
    border: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.nav-button:hover:not(:disabled) {
    background-color: #f8f9fa;
    border-color: #aaa;
}

.nav-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.nav-button.prev {
    left: -50px;
}

.nav-button.next {
    right: -50px;
}

.no-results {
    color: #666;
    text-align: center;
    padding: 20px;
}
</style>
