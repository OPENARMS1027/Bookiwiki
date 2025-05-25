<template>
  <div>
    <div v-if="!props.thread || !user" class="loading-view">
      <font-awesome-icon :icon="['fas', 'spinner']" spin />
      <span>로딩 중</span>
    </div>

    <div v-else class="thread-info">
      <div class="thread-actions">
        <button @click="onThreadDelete(props.thread.id)">삭제</button>
        <button @click="onThreadUpdate(props.thread.id)">수정</button>
      </div>
      <div class="thread-user">
        <span class="author">
          {{ user.username }}
          <button 
            v-if="showFollowButton" 
            class="follow-btn"
            :class="{ 'following': isFollowing }"
            @click="handleFollow"
          >
            {{ isFollowing ? '팔로잉' : '팔로우' }}
          </button>
        </span>
        <div v-if="user.profile_img">
          <img :src="user.profile_img" alt="user_profile_img" />
        </div>
        <div v-else>
          <font-awesome-icon :icon="['fas', 'user']" size="4x" />
        </div>
      </div>
      <div class="thread-header">
        <strong>{{ props.thread.title }}</strong>
        <p>
          <div class="likes" v-if="isLiked" @click="handleThreadLikes"
            ><font-awesome-icon :icon="['fas', 'heart']" />
          </div>
          <div class="likes" v-else @click="handleThreadLikes"
          ><font-awesome-icon :icon="['far', 'heart']" /></div>
          <span> {{ likesCount }}</span>
        </p>
      </div>
      <div class="thread-main">
        <div class="thread-content">
          {{ props.thread.content }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  thread: {
    type: Object,
    required: true
  }
})

import { ref, watch, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useBookStore } from '@/stores/book'

const router = useRouter()
const userStore = useUserStore()
const bookStore = useBookStore()
const user = ref(null)
const emit = defineEmits(['update-thread'])
const isFollowing = ref(false)

const showFollowButton = computed(() => {
  return userStore.thisUser && user.value && userStore.thisUser.id !== user.value.id
})

const isLiked = computed(() => {
  return userStore.thisUser && props.thread.likes.includes(userStore.thisUser.id)
})

const likesCount = computed(() => {
  return props.thread.likes.length
})

watch(
  () => props.thread?.user,
  async (newUser) => {
    if (newUser) {
      const userData = await userStore.getUser(newUser)
      user.value = userData
      isFollowing.value = userData.is_followed
    } else {
      user.value = null
    }
  },
  { immediate: true }
)

const onThreadDelete = async (threadId) => {
  await bookStore.deleteThread(threadId)
  router.push({ name: 'threadList' })
}

const onThreadUpdate = (threadId) => {
  router.push({ name: 'threadWrite', query: { id: threadId, type: 'edit' } })
}

const handleThreadLikes = async () => {
  if (!userStore.thisUser) return
  
  try {
    const userId = userStore.thisUser.id
    const currentLikes = [...props.thread.likes]
    const index = currentLikes.indexOf(userId)
    
    if (index === -1) {
      currentLikes.push(userId)
    } else {
      currentLikes.splice(index, 1)
    }

    emit('update-thread', {
      ...props.thread,
      likes: currentLikes
    })

    const updatedThread = await bookStore.likesThread(props.thread.id)
    
    emit('update-thread', updatedThread)
  } catch (error) {
    console.error('좋아요 업데이트 실패:', error)
    emit('update-thread', props.thread)
  }
}

const handleFollow = async () => {
  try {
    const response = await userStore.followUser(user.value.id)
    if (response) {
      isFollowing.value = response.is_followed
      const updatedUser = await userStore.getUser(user.value.id)
      user.value = updatedUser
    }
  } catch (err) {
    console.error(err)
  }
}

onMounted(() => {
  userStore.getThisUser()
})
</script>

<style scoped>
.loading-view {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 200px;
  font-size: 1.2em;
  color: #888;
}

.thread-info {
  display: flex;
  flex-direction: column;
}

.thread-actions {
  display: flex;
  flex-direction: row-reverse;
}

.thread-user {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.author {
  padding: 10px;
}

.thread-header {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

.likes{
  cursor: pointer;
}

.thread-content {
  text-align: start;
}
</style>
