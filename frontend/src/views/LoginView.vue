<template>
  <div class="login-container">
    <div class="login-form">
      <h1>로그인</h1>
      <form @submit.prevent="onLogIn">
        <div class="form-group">
          <label for="username">아이디</label>
          <input 
            type="text" 
            id="username" 
            v-model="username"
            placeholder="아이디를 입력하세요"
            required 
          />
        </div>
        <div class="form-group">
          <label for="password">비밀번호</label>
          <input 
            type="password" 
            id="password"
            v-model="password"
            placeholder="비밀번호를 입력하세요"
            required 
          />
        </div>
        <button type="submit" class="login-button">로그인</button>
      </form>
      <div class="signup-link">
        계정이 없으신가요? 
        <router-link to="/signup">회원가입</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user.js'

const store = useUserStore()
const router = useRouter()
const route = useRoute()
const username = ref('')
const password = ref('')
const onLogIn = async () => {
  try {
    const data = {
      username: username.value,
      password: password.value,
    }
    const response = await store.login(data)
    if (response.data.key) {
      const redirectPath = route.query.redirect || '/'
      router.push(redirectPath)
    }
  } catch (error) {
    console.error('로그인 실패:', error)
    alert('로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
    password.value = '' // 비밀번호만 초기화
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 2rem;
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(76, 175, 80, 0.05) 100%);
}

.login-form {
  background: white;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  width: 100%;
  max-width: 450px;
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

label {
  display: block;
  margin-bottom: 0.8rem;
  color: #2c3e50;
  font-weight: 500;
  font-size: 1.1rem;
}

input {
  width: 100%;
  padding: 1rem;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: rgba(76, 175, 80, 0.02);
}

input:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 0 4px rgba(76, 175, 80, 0.1);
}

input::placeholder {
  color: #aaa;
}

.login-button {
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

.login-button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}

.signup-link {
  text-align: center;
  margin-top: 2rem;
  color: #666;
  font-size: 1.05rem;
}

.signup-link a {
  color: #4CAF50;
  text-decoration: none;
  font-weight: 600;
  margin-left: 0.5rem;
  position: relative;
}

.signup-link a::after {
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

.signup-link a:hover::after {
  transform: scaleX(1);
}

@media (max-width: 768px) {
  .login-form {
    padding: 2rem;
    margin: 1rem;
  }

  h1 {
    font-size: 2rem;
  }
}
</style>
