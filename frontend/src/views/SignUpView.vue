<template>
  <div>
    <h1>sign up</h1>
    <form @submit.prevent="onSignUp" enctype="multipart/form-data">
      <div>
        <label for="username">username</label>
        <input type="text" id="username" v-model="username" />
      </div>

      <div>
        <label for="password1">password</label>
        <input type="password" id="password1" v-model="password1" />
      </div>

      <div>
        <label for="password2">password confirmation</label>
        <input type="password" id="password2" v-model="password2" />
      </div>

      <div>
        <label for="gender">gender</label>
        <select id="gender" v-model="gender">
          <option value="">선택 안 함</option>
          <option value="M">남성</option>
          <option value="F">여성</option>
        </select>
      </div>

      <div>
        <label for="age">age</label>
        <input type="number" id="age" v-model="age" />
      </div>

      <div>
        <label>관심 카테고리</label>
        <div>
          <div v-for="category in categories" :key="category.id">
            <input
              type="checkbox"
              :id="'category-' + category.id"
              :value="category.id"
              v-model="interested_category"
            />
            <label :for="'category-' + category.id" style="margin-left: 5px;">
              {{ category.name }}
            </label>
          </div>
        </div>
      </div>

      <div>
        <label for="week_avg_time">주간 평균 독서 시간</label>
        <input type="number" id="week_avg_time" v-model="week_avg_time" />
      </div>

      <div>
        <label for="year_avg_time">연간 평균 독서 시간</label>
        <input type="number" id="year_avg_time" v-model="year_avg_time" />
      </div>

      <div>
        <label for="profile_img">프로필 이미지</label>
        <input type="file" id="profile_img" @change="onFileChange" />
      </div>

      <input type="submit" value="회원가입" />
    </form>
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

<style scoped></style>
