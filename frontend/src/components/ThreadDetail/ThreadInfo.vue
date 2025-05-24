<template>
  <div>
    <div v-if="!props.thread || !user" class="loading-view">
      <font-awesome-icon :icon="['fas', 'spinner']" spin />
      <span>로딩 중입니다...</span>
    </div>

    <div v-else class="thread-info">
      <div class="thread-actions">
        <button @click="">삭제</button>
        <button @click="">수정</button>
      </div>
      <div class="thread-user">
        <span class="author">
          {{ user.username }}
          <button class="follow-btn">팔로우</button>
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
          <span class="likes" @click="">♡</span>
          <span> {{ props.thread.likes.length }}</span>
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
  thread: Object,
})

import { ref, watch } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const user = ref(null)

watch(
  () => props.thread,
  async (newThread) => {
    if (newThread && newThread.user) {
      user.value = await userStore.getUser(newThread.user)
    } else {
      user.value = null
    }
  },
  { immediate: true }
)
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

.thread-content {
  text-align: start;
}
</style>
