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
          <div class="default-profile-icon">
            <font-awesome-icon :icon="['fas', 'user']" size="4x" />
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
              userStore.thisUser?.threads_count || 0
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
  width: 100%;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.profile-image {
  flex-shrink: 0;
}

.profile-img,
.default-profile-icon {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.profile-img {
  object-fit: cover;
  border: 3px solid #f0f0f0;
}

.default-profile-icon {
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #666;
  border: 3px solid #f0f0f0;
}

.profile-info {
  flex: 1;
}

.nickname {
  font-size: 1.75rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: #2c3e50;
}

.stats {
  display: flex;
  gap: 2.5rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.75rem 1.5rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  transition: all 0.2s ease;
}

.stat-item:hover {
  background-color: #f0f0f0;
  transform: translateY(-2px);
}

.stat-label {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 1.5rem;
  }

  .nickname {
    font-size: 1.5rem;
    margin-bottom: 1.25rem;
  }

  .stats {
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .stat-item {
    padding: 0.6rem 1.25rem;
    min-width: 120px;
  }

  .stat-value {
    font-size: 1.25rem;
  }
}
</style>
