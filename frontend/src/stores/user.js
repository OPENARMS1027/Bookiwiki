import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore(
  'user',
  () => {
    const token = ref('')
    const router = useRouter()
    const isLogin = computed(() => {
      return token.value ? true : false
    })

    const signup = (formData) => {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
        .then((res) => {
          console.log('회원가입 성공')
          router.push({ name: 'login' })
        })
        .catch((err) => {
          console.log(err)
        })
    }

    const login = ({ username, password }) => {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: { username, password },
      })
        .then((res) => {
          console.log(res)
          console.log('로그인 성공')
          token.value = res.data.key
          // router.push({ name: 'home' })
        })
        .catch((err) => console.log(err))
    }

    const getUser = (userId) => {
      return axios({
        method: 'get',
        url: `http://127.0.0.1:8000/user/${userId}/`,
      })
        .then((response) => {
          // console.log(response.data)
          return response.data
        })
        .catch((err) => {
          console.log(err)
        })
    }

    return { signup, token, login, isLogin, getUser }
  },
  { persist: true }
)
