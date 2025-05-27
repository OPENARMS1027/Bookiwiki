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
        <div class="nickname-container">
          <h2 class="nickname">{{ userStore.thisUser?.username }}</h2>
          <router-link to="/mypage/password" class="password-button">
            <font-awesome-icon :icon="['fas', 'key']" /> 비밀번호 변경
          </router-link>
        </div>
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

    <div class="genres-section">
      <h3>관심 장르 설정</h3>
      <div class="genres-grid">
        <button
          v-for="genre in genres"
          :key="genre.id"
          :class="[
            'genre-button',
            { selected: selectedGenres.includes(genre.id) },
          ]"
          @click="toggleGenre(genre.id)"
        >
          {{ genre.name }}
        </button>
      </div>
      <div class="save-button-container">
        <button class="save-button" @click="saveGenres" :disabled="!hasChanges">
          장르 저장
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const userStore = useUserStore();
const genres = ref([]);
const selectedGenres = ref([]);
const initialGenres = ref([]);

onMounted(async () => {
  await userStore.getThisUser();
  await fetchGenres();
  await fetchUserGenres();
});

const fetchGenres = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/categories/");
    genres.value = response.data;
  } catch (error) {
    console.error("장르 목록을 불러오는데 실패했습니다:", error);
  }
};

const fetchUserGenres = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/user/me/", {
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    });
    selectedGenres.value = response.data.interested_category.map(
      (category) => category.id
    );
    initialGenres.value = [...selectedGenres.value];
  } catch (error) {
    console.error("사용자 장르 정보를 불러오는데 실패했습니다:", error);
  }
};

const toggleGenre = (genreId) => {
  const index = selectedGenres.value.indexOf(genreId);
  if (index === -1) {
    selectedGenres.value.push(genreId);
  } else {
    selectedGenres.value.splice(index, 1);
  }
};

const hasChanges = computed(() => {
  if (selectedGenres.value.length !== initialGenres.value.length) return true;
  return !selectedGenres.value.every((id) => initialGenres.value.includes(id));
});

const saveGenres = async () => {
  try {
    await axios.put(
      "http://127.0.0.1:8000/user/me/",
      { interested_category: selectedGenres.value },
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
          "Content-Type": "application/json",
        },
      }
    );
    initialGenres.value = [...selectedGenres.value];
    alert("관심 장르가 성공적으로 저장되었습니다.");
  } catch (error) {
    console.error("장르 저장에 실패했습니다:", error);
    alert("장르 저장에 실패했습니다. 다시 시도해주세요.");
  }
};

const getImageUrl = (profileImg) => {
  if (!profileImg) return null;
  if (profileImg.startsWith("http")) return profileImg;
  return `http://127.0.0.1:8000/media/${profileImg}`;
};

const handleImageError = () => {
  const defaultIcon = document.createElement("div");
  defaultIcon.className = "default-profile-icon";
  defaultIcon.innerHTML = "<font-awesome-icon :icon=\"['fas', 'user']\" />";
  event.target.parentNode.replaceChild(defaultIcon, event.target);
};
</script>

<style scoped>
.profile-container {
  width: 100%;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  margin-bottom: 2rem;
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

.nickname-container {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.nickname {
  font-size: 1.75rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
}

.password-button {
  padding: 0.5rem 1rem;
  background-color: #e9ecef;
  border-radius: 8px;
  color: #495057;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.password-button:hover {
  background-color: #dee2e6;
  transform: translateY(-1px);
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

.genres-section {
  margin-top: 2rem;
  padding: 2rem;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.genres-section h3 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
}

.genres-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.genre-button {
  padding: 0.75rem 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  background-color: white;
  color: #4a5568;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.genre-button:hover {
  border-color: #4a5568;
  transform: translateY(-1px);
}

.genre-button.selected {
  background-color: #4a5568;
  color: white;
  border-color: #4a5568;
}

.save-button-container {
  display: flex;
  justify-content: center;
  margin-top: 1.5rem;
}

.save-button {
  padding: 0.75rem 2rem;
  background-color: #4a5568;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.save-button:hover:not(:disabled) {
  background-color: #2d3748;
  transform: translateY(-1px);
}

.save-button:disabled {
  background-color: #e2e8f0;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 1.5rem;
  }

  .nickname-container {
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
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

  .genres-grid {
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  }
}
</style>
