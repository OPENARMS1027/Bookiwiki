<template>
  <div class="profile-container">
    <div class="profile-header">
      <div class="profile-image">
        <template v-if="userStore.thisUser?.profile_img">
          <img
            :src="getImageUrl(userStore.thisUser.profile_img)"
            alt="프로필 이미지"
            class="profile-img"
            @error="handleImageError"
          />
        </template>
        <template v-else>
          <div
            class="d2d76bbf7f79ab92e3fd085b97932089efd3a2498efault-profile-icon"
          >
            <font-awesome-icon :icon="['fas', 'user']" />
          </div>
        </template>
      </div>
      <div class="profile-info">
        <h2 class="nickname">{{ userStore.thisUser?.username }}</h2>
        <div class="stats">
          <div class="stat-item">
            <span class="stat-label">팔로워</span>
            <span class="stat-value">{{
              userStore.thisUser?.followers_count || 0
            }}</span>
          </div>
          <div class="stat-item">
            <span class="stat-label">팔로잉</span>
            <span class="stat-value">{{
              userStore.thisUser?.followings_count || 0
            }}</span>
          </div>
          <div class="stat-item">
            <span class="stat-label">작성 스레드</span>
            <span class="stat-value">{{
              userStore.thisUser?.thread_count || 0
            }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

onMounted(() => {
  userStore.getThisUser()
})

const getImageUrl = (profileImg) => {
  if (!profileImg) return null
  if (profileImg.startsWith('http')) return profileImg
  return `http://127.0.0.1:8000/media/${profileImg}`
}

const handleImageError = () => {
  const defaultIcon = document.createElement('div')
  defaultIcon.className = 'default-profile-icon'
  defaultIcon.innerHTML = "<font-awesome-icon :icon=\"['fas', 'user']\" />"
  event.target.parentNode.replaceChild(defaultIcon, event.target)
}
</script>

<style scoped>
.profile-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 2rem;
  background-color: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-image {
  flex-shrink: 0;
}

.profile-img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #f0f0f0;
}

.default-profile-icon {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  color: #666;
}

.profile-info {
  flex: 1;
}

.nickname {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #333;
}

.stats {
  display: flex;
  gap: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.stat-label {
  font-size: 0.875rem;
  color: #666;
  margin-bottom: 0.25rem;
}

.stat-value {
  font-size: 1.25rem;
  font-weight: 600;
  color: #333;
}

@media (max-width: 640px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
  }

  .stats {
    justify-content: center;
  }
}
</style>
