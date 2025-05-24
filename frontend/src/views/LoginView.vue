<template>
  <div>
    <h1>sign in</h1>
    <form @submit.prevent="onLogIn">
      <div>
        <label for="username">username</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div>
        <label for="password">password</label
        ><input type="password" v-model="password" />
      </div>
      <input type="submit" value="login" />
    </form>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user.js'

const store = useUserStore()
const router = useRouter()
const username = ref('')
const password = ref('')

const onLogIn = () => {
  const data = {
    username: username.value,
    password: password.value,
  }
  store.login(data)
  //   if (store.token) {
  //     router.push({ name: 'home' })
  //   }
}
</script>

<style scoped></style>
