<template>
    <div class="container">
        <div class="thread-list">
            <div v-if="bookThreads">
            <div v-for="thread in bookThreads" :key="thread.id" class="thread-item">
                <div class="thread-content">
                    <h3 class="thread-title" @click="moveToThread(thread.id)">{{ thread.title }}</h3>
                    <p class="thread-text">{{ thread.content }}</p>
                    <div class="thread-info">
                        <span class="likes">
                            <i class="fas fa-heart"></i> {{ thread.likes.length }} |
                        </span>
                        <!-- comments생성후 확인 필수 -->
                        <span class="comments">
                            <i class="fas fa-comment"></i> {{ thread.likes.length }}
                        </span>
                        <p class="date">{{ formatDate(thread.created_at) }}</p>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book'
// import '@/styles/BookDetail/BookThread.css'

const props = defineProps({
    book: Object,
    })

const router = useRouter()
const store = useBookStore()
const threads = computed(() => store.threads)

async function fetchData() {
    await store.getThreads()
}

onMounted(() => {
    fetchData()
})

const bookThreads = computed(() => {
    // console.log('현재 book:', props.book)
    // console.log('현재 threads:', threads.value)
    if (!props.book || !threads.value) return []
    return threads.value.filter(thread => {
        // console.log('비교:', thread.book, props.book.id)
        return Number(thread.book.id) === props.book.id
    })
})

const moveToThread = (threadId) => {
    router.push({ name: 'threadDetail', params: { threadId } })
}

const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('ko-KR')
}

</script>

<style scoped>

</style>
  