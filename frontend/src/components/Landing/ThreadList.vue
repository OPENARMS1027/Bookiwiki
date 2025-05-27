<template>
  <div class="thread-section">
    <h2 class="section-title">
      <i class="fas fa-comments"></i>
      추천 스레드
    </h2>
    <p class="section-description">
      <div v-if="userStore.isLogin">
        <template v-if="user?.interested_category?.length">
          관심 장르를 바탕으로 최근 스레드를 추천해드려요
        </template>
        <template v-else>
          관심 장르를 추가하면 더 정확한 추천이 가능해요!
        </template>
      </div>
      <div v-else>
        <span class="login-text" @click="goToLogin">로그인</span>하면 관심 장르를 바탕으로 최근 스레드를 추천해드려요
      </div>
    </p>
    <div v-if="userStore.isLogin" class="thread-grid">
      <div v-if="isLoading" class="loading-message">
        스레드를 불러오는 중입니다...
      </div>
      <template v-else>
        <RouterLink
          v-for="thread in threadList"
          :key="thread.id"
          :to="{ name: 'threadDetail', params: { threadId: thread.id } }"
          class="thread-card"
        >
          <div class="thread-content">
            <h3 class="thread-title">{{ thread.title }}</h3>
            <p class="thread-text">{{ thread.content }}</p>
          </div>
          <div class="thread-meta">
            <span class="meta-item">
              <i class="fas fa-heart"></i>
              {{ thread.likes.length }}
            </span>
            <span class="meta-item">
              <i class="fas fa-comment"></i>
              {{ thread.comments_count }}
            </span>
          </div>
        </RouterLink>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue"
import { RouterLink } from "vue-router"
import { useBookStore } from "@/stores/book.js"
import { useUserStore } from "@/stores/user.js"
import { useRouter } from "vue-router"

const router = useRouter()
const userStore = useUserStore()
const bookStore = useBookStore()
const threadList = ref([])
const user = ref(null)
const interestedCategory = ref([])
const isLoading = ref(true)

const goToLogin = () => {
  router.push({ name: 'login' })
}

const updateThreadList = async () => {
  try {
    isLoading.value = true

    // 유저 정보가 없으면 가져오기
    if (!user.value && userStore.isLogin) {
      await userStore.getThisUser()
      if (userStore.thisUser) {
        user.value = userStore.thisUser
        interestedCategory.value = user.value.interested_category.map(item => item.id)
      }
    }

    // 스레드 데이터가 없으면 가져오기
    if (!bookStore.threads?.length) {
      await bookStore.getThreads()
    }

    // 유저가 로그인했고 관심 카테고리가 있는 경우
    if (userStore.isLogin && user.value?.interested_category?.length) {
      threadList.value = bookStore.threads
        .filter(thread => {
          return interestedCategory.value.includes(thread.book?.category)
        })
        .sort((a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime())
        .slice(0, 6)
    } else if (userStore.isLogin) {
      // 로그인은 했지만 관심 카테고리가 없는 경우
      threadList.value = [...bookStore.threads]
        .sort((a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime())
        .slice(0, 6)
    } else {
      // 로그인하지 않은 경우
      threadList.value = []
    }
  } catch (error) {
    console.error('스레드 업데이트 중 에러:', error)
  } finally {
    isLoading.value = false
  }
}

// 로그인 상태 변경 감지
watch(() => userStore.isLogin, async (newLoginState) => {
  if (newLoginState) {
    await updateThreadList()
  } else {
    user.value = null
    interestedCategory.value = []
    threadList.value = []
  }
}, { immediate: true })

// 유저 정보 변경 감지
watch(() => userStore.thisUser, async (newUser) => {
  if (newUser) {
    user.value = newUser
    interestedCategory.value = newUser.interested_category.map(item => item.id)
    await updateThreadList()
  }
}, { immediate: true })

// 스레드 데이터 변경 감지
watch(() => bookStore.threads, async (newThreads) => {
  if (newThreads?.length > 0 && userStore.isLogin) {
    await updateThreadList()
  }
}, { immediate: true })

onMounted(async () => {
  if (userStore.isLogin) {
    await updateThreadList()
  }
})
</script>

<style scoped>
.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-title i {
  color: #4caf50;
  font-size: 1.2em;
}

.section-description {
  color: #666;
  margin-bottom: 2rem;
  font-size: 1.1rem;
}

.login-text {
  color: #4caf50;
  font-weight: 500;
  cursor: pointer;
  transition: color 0.2s ease;
}

.login-text:hover {
  color: #45a049;
  text-decoration: underline;
}

.thread-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 2.5rem;
  margin: 0 auto;
  width: 100%;
  padding: 0.5rem;
}

.thread-card {
  background: #f8f9fa;
  border-radius: 16px;
  padding: 1.75rem;
  text-decoration: none;
  color: inherit;
  border: 1px solid rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  min-height: 280px;
  position: relative;
  overflow: hidden;
  margin: 0;
  box-sizing: border-box;
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

.thread-card:hover {
  transform: translateY(-4px);
  background: white;
  border-color: rgba(76, 175, 80, 0.2);
  box-shadow: 0 8px 24px rgba(76, 175, 80, 0.12);
}

.thread-card:hover::before {
  opacity: 1;
}

.thread-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  overflow: hidden;
}

.thread-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.4;
  position: relative;
  padding-bottom: 0.75rem;
  word-break: break-word;
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
  color: #666;
  font-size: 0.95rem;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.6;
  word-break: break-word;
}

.thread-meta {
  display: flex;
  gap: 1.5rem;
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(76, 175, 80, 0.1);
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #666;
  font-size: 0.9rem;
  transition: color 0.2s ease;
}

.meta-item i {
  color: #4caf50;
  font-size: 1rem;
}

.thread-card:hover .meta-item {
  color: #4caf50;
}

.loading-message {
  text-align: center;
  color: #666;
  grid-column: 1 / -1;
  padding: 2rem;
  font-size: 1.1rem;
}

@media (max-width: 1400px) {
  /* .thread-section {
    padding: 2rem 3rem;
  } */
}

@media (max-width: 1200px) {
  .thread-section {
    padding: 2rem;
  }

  .thread-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 2rem;
    padding: 0.5rem;
  }

  .thread-card {
    min-height: 250px;
  }
}

@media (max-width: 768px) {
  .thread-section {
    padding: 1.5rem;
  }

  .section-title {
    font-size: 1.3rem;
  }

  .section-description {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }

  .thread-grid {
    grid-template-columns: minmax(0, 1fr);
    gap: 1.5rem;
    padding: 0.5rem;
  }

  .thread-card {
    padding: 1.5rem;
    min-height: 220px;
  }

  .thread-title {
    font-size: 1.1rem;
  }

  .thread-text {
    font-size: 0.9rem;
  }

  .thread-meta {
    margin-top: 1.25rem;
    padding-top: 0.75rem;
  }
}
</style>
