<template>
  <div class="signup-container">
    <div class="signup-form">
      <h1>회원가입</h1>
      <form @submit.prevent="onSignUp" enctype="multipart/form-data">
        <div class="form-group">
          <label for="username">아이디</label>
          <input 
            type="text" 
            id="username" 
            v-model="username"
            placeholder="사용하실 아이디를 입력하세요"
            required
          />
        </div>

        <div class="form-group">
          <label for="password1">비밀번호</label>
          <input 
            type="password" 
            id="password1" 
            v-model="password1"
            placeholder="비밀번호를 입력하세요"
            required
          />
        </div>

        <div class="form-group">
          <label for="password2">비밀번호 확인</label>
          <input 
            type="password" 
            id="password2" 
            v-model="password2"
            placeholder="비밀번호를 다시 입력하세요"
            required
          />
        </div>

        <div class="form-row">
          <div class="form-group half">
            <label for="gender">성별</label>
            <select id="gender" v-model="gender" class="form-select">
              <option value="">선택 안 함</option>
              <option value="M">남성</option>
              <option value="F">여성</option>
            </select>
          </div>

          <div class="form-group half">
            <label for="age">나이</label>
            <input 
              type="number" 
              id="age" 
              v-model="age"
              placeholder="나이를 입력하세요"
            />
          </div>
        </div>

        <div class="form-group">
          <label>관심 카테고리</label>
          <div class="category-grid">
            <div v-for="category in categories" :key="category.id" class="category-item">
              <input
                type="checkbox"
                :id="'category-' + category.id"
                :value="category.id"
                v-model="interested_category"
                class="category-checkbox"
              />
              <label :for="'category-' + category.id" class="category-label">
                {{ category.name }}
              </label>
            </div>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group half">
            <label for="week_avg_time">주간 평균 독서 시간</label>
            <input 
              type="number" 
              id="week_avg_time" 
              v-model="week_avg_time"
              placeholder="시간 단위로 입력"
            />
          </div>

          <div class="form-group half">
            <label for="year_avg_time">연간 평균 독서 시간</label>
            <input 
              type="number" 
              id="year_avg_time" 
              v-model="year_avg_time"
              placeholder="시간 단위로 입력"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="profile_img">프로필 이미지</label>
          <div class="file-input-wrapper">
            <input 
              type="file" 
              id="profile_img" 
              @change="onFileChange"
              class="file-input"
            />
            <label for="profile_img" class="file-label">
              <font-awesome-icon :icon="['fas', 'upload']" />
              이미지 선택
            </label>
            <span v-if="profile_img" class="file-name">{{ profile_img.name }}</span>
          </div>
        </div>

        <button type="submit" class="signup-button">회원가입</button>
        <div class="login-link">
          이미 계정이 있으신가요? <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user.js'
import axios from 'axios'

const store = useUserStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const gender = ref('')
const age = ref(null)
const interested_category = ref([])
const week_avg_time = ref(null)
const year_avg_time = ref(null)
const profile_img = ref(null)

const categories = ref([])

const onFileChange = (e) => {
  profile_img.value = e.target.files[0]
}

const onSignUp = async () => {
  const formData = new FormData()
  formData.append('username', username.value)
  formData.append('password1', password1.value)
  formData.append('password2', password2.value)
  formData.append('gender', gender.value)
  formData.append('age', age.value)
  formData.append('week_avg_time', week_avg_time.value)
  formData.append('year_avg_time', year_avg_time.value)
  if (profile_img.value) {
    formData.append('profile_img', profile_img.value)
  }
  interested_category.value.forEach((id) => {
    formData.append('interested_category', id)
  })

  store.signup(formData)
}

// 카테고리 목록 불러오기
onMounted(async () => {
  try {
    const res = await axios.get('http://localhost:8000/categories/')
    categories.value = res.data
  } catch (error) {
    console.error('카테고리 로딩 실패:', error)
  }
})
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(76, 175, 80, 0.05) 100%);
}

.signup-form {
  background: white;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  width: 100%;
  max-width: 800px;
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2.5rem;
  font-size: 2.2rem;
  font-weight: 700;
}

.form-group {
  margin-bottom: 1.8rem;
}

.form-row {
  display: flex;
  gap: 2rem;
  margin-bottom: 1.8rem;
}

.half {
  flex: 1;
  margin-bottom: 0;
}

label {
  display: block;
  margin-bottom: 0.8rem;
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.1rem;
}

input:not([type="file"]),
select {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: rgba(76, 175, 80, 0.02);
}

input:not([type="file"]):focus,
select:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 0 4px rgba(76, 175, 80, 0.1);
}

input::placeholder {
  color: #aaa;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
}

.category-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.category-checkbox {
  display: none;
}

.category-label {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  background: rgba(76, 175, 80, 0.05);
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  margin: 0;
}

.category-checkbox:checked + .category-label {
  background: #4CAF50;
  color: white;
  border-color: #4CAF50;
}

.file-input-wrapper {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.file-input {
  display: none;
}

.file-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  background: #4CAF50;
  color: white;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1rem;
  margin: 0;
}

.file-label:hover {
  background: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}

.file-name {
  color: #666;
  font-size: 0.95rem;
}

.signup-button {
  width: 100%;
  padding: 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1rem;
}

.signup-button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}

.login-link {
  text-align: center;
  margin-top: 2rem;
  color: #666;
  font-size: 1.05rem;
}

.login-link a {
  color: #4CAF50;
  text-decoration: none;
  font-weight: 600;
  margin-left: 0.5rem;
  position: relative;
}

.login-link a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background: #4CAF50;
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.login-link a:hover::after {
  transform: scaleX(1);
}

@media (max-width: 768px) {
  .signup-container {
    padding: 1.5rem;
  }

  .signup-form {
    padding: 2rem;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 2rem;
  }

  .form-row {
    flex-direction: column;
    gap: 0;
  }

  .half {
    margin-bottom: 1.8rem;
  }

  .category-grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }

  .category-label {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }

  .file-input-wrapper {
    flex-direction: column;
    align-items: flex-start;
  }

  .file-name {
    margin-top: 0.5rem;
  }
}</style>