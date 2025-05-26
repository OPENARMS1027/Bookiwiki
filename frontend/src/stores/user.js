import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore(
  'user',
  () => {
    const token = ref('')
    const router = useRouter()
    const thisUser = ref(null) // 현재 로그인한 유저
    const followStatus = ref({}) // 팔로우 상태를 저장할 객체

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
      return new Promise((resolve, reject) => {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/login/',
          data: { username, password },
        })
          .then((res) => {
            console.log('로그인 성공')
            token.value = res.data.key
            resolve(res)
          })
          .catch((err) => {
            console.log('로그인 실패:', err)
            token.value = ''
            reject(err)
          })
      })
    }

    const logout = () => {
      // 서버에 로그아웃 요청
      if (token.value) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/logout/',
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
          .then(() => {
            console.log('로그아웃 성공')
          })
          .catch((err) => {
            console.log('로그아웃 에러:', err)
          })
          .finally(() => {
            // 로컬 상태 초기화
            token.value = ''
            thisUser.value = null
            followStatus.value = {} // 팔로우 상태도 초기화
          })
      }
    }

    const getUser = (userId) => {
      return axios({
        method: 'get',
        url: `http://127.0.0.1:8000/user/${userId}/`,
        headers: token.value ? {
          Authorization: `Token ${token.value}`
        } : {}
      })
        .then((response) => {
          // 팔로우 상태를 저장
          followStatus.value[userId] = response.data.is_followed
          return response.data
        })
        .catch((err) => {
          console.log(err)
        })
    }

    const getThisUser = () => {
      if (token.value) {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/user/me/',
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
          .then((response) => {
            thisUser.value = response.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }

    const followUser = (userId) => {
      if (token.value) {
        return axios({
          method: 'post',
          url: `http://127.0.0.1:8000/user/follow/${userId}/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        })
          .then((response) => {
            console.log('팔로우 성공')
            // 팔로우 상태 업데이트
            followStatus.value[userId] = response.data.is_followed
            return response.data
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }

    // 특정 사용자의 팔로우 상태를 반환하는 함수
    const getFollowStatus = (userId) => {
      return followStatus.value[userId] || false
    }

    return {
      signup,
      token,
      login,
      logout,
      isLogin,
      getUser,
      getThisUser,
      thisUser,
      followUser,
      getFollowStatus,
      followStatus,
    }
  },
  { persist: true }
)
