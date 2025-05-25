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
    await store.login(data)
    const redirectPath = route.query.redirect || '/'
    router.push(redirectPath)
  } catch (error) {
    console.error('로그인 실패:', error)
    alert('로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.')
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 20px;
}

.login-form {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 500;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input:focus {
  outline: none;
  border-color: #2196F3;
  box-shadow: 0 0 0 2px rgba(33,150,243,0.1);
}

.login-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #2196F3;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.login-button:hover {
  background-color: #1976D2;
}

.signup-link {
  text-align: center;
  margin-top: 1.5rem;
  color: #666;
}

.signup-link a {
  color: #2196F3;
  text-decoration: none;
  font-weight: 500;
}

.signup-link a:hover {
  text-decoration: underline;
}
</style>
