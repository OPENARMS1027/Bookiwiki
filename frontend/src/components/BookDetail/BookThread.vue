<template>
    <!-- <div class="container" v-if="book && threads">
        <div class="thread-list">
            <div v-for="thread in bookThreads" :key="thread.id" class="thread-item">
                <div class="thread-content">
                    <h3 class="thread-title" @click="moveToThread(thread.id)">{{ thread.title }}</h3>
                    <p class="thread-text">{{ thread.content }}</p>
                    <div class="thread-info">
                        <span class="likes">
                            <i class="fas fa-heart"></i> {{ thread.likes.length }}
                        </span>
                        <span class="comments">
                            <i class="fas fa-comment"></i> {{ thread.comments.length }}
                        </span>
                        <span class="date">{{ formatDate(thread.created_at) }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div> -->
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useBookStore } from '@/stores/book'
import '@/styles/BookDetail/BookThread.css'

const props = defineProps({
    book: {
        type: Object,
        required: true
    }
})

const router = useRouter()
const store = useBookStore()
const threads = computed(() => store.threads)
const thread = ref(null)
const book = ref(null)
// 현재 책의 쓰레드만 필터링
// const bookThreads = computed(() => {
//     if (!props.book || !threads.value) return []
//     return threads.value.filter(thread => Number(thread.book) === Number(props.book.id))
// })

// const moveToThread = (threadId) => {
//     router.push({ name: 'threadDetail', params: { threadId } })
// }

// const formatDate = (dateString) => {
//     const date = new Date(dateString)
//     return date.toLocaleDateString('ko-KR')
// }

onMounted(async () => {
    // thread.value = await store.getThreads(threadId)
    // const bookData = await store.getBook(props.book.id)
    // book.value = bookData
})
</script>

<style scoped>

</style>
  