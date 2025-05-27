<template>
  <div class="password-change-container">
    <h2>비밀번호 변경</h2>
    <form @submit.prevent="changePassword" class="password-form">
      <div class="form-group">
        <label for="old_password">현재 비밀번호</label>
        <input
          type="password"
          id="old_password"
          v-model="passwordData.old_password"
          class="form-input"
          required
        />
      </div>

      <div class="form-group">
        <label for="new_password1">새 비밀번호</label>
        <input
          type="password"
          id="new_password1"
          v-model="passwordData.new_password1"
          class="form-input"
          required
        />
      </div>

      <div class="form-group">
        <label for="new_password2">새 비밀번호 확인</label>
        <input
          type="password"
          id="new_password2"
          v-model="passwordData.new_password2"
          class="form-input"
          required
        />
      </div>

      <div class="button-group">
        <button type="button" class="cancel-button" @click="goBack">
          취소
        </button>
        <button type="submit" class="submit-button">비밀번호 변경</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useUserStore } from "@/stores/user";

const router = useRouter();
const userStore = useUserStore();

const passwordData = ref({
  old_password: "",
  new_password1: "",
  new_password2: "",
});

const changePassword = async () => {
  if (passwordData.value.new_password1 !== passwordData.value.new_password2) {
    alert("새 비밀번호가 일치하지 않습니다.");
    return;
  }

  try {
    await axios.post(
      "http://127.0.0.1:8000/accounts/password/change/",
      {
        old_password: passwordData.value.old_password,
        new_password1: passwordData.value.new_password1,
        new_password2: passwordData.value.new_password2,
      },
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      }
    );
    alert("비밀번호가 성공적으로 변경되었습니다.");
    router.push("/mypage");
  } catch (error) {
    if (error.response) {
      if (error.response.data.old_password) {
        alert("현재 비밀번호가 올바르지 않습니다.");
      } else if (error.response.data.new_password1) {
        alert(error.response.data.new_password1[0]);
      } else if (error.response.data.new_password2) {
        alert(error.response.data.new_password2[0]);
      } else {
        alert("비밀번호 변경에 실패했습니다. 입력한 정보를 확인해주세요.");
      }
    } else {
      alert("서버와의 통신에 실패했습니다. 잠시 후 다시 시도해주세요.");
    }
    console.error(error);
  }
};

const goBack = () => {
  router.push("/mypage");
};
</script>

<style scoped>
.password-change-container {
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
}

.password-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-size: 0.9rem;
  color: #4a5568;
}

.form-input {
  padding: 0.75rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.form-input:focus {
  border-color: #4a5568;
  outline: none;
  box-shadow: 0 0 0 2px rgba(74, 85, 104, 0.2);
}

.button-group {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.submit-button,
.cancel-button {
  flex: 1;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.submit-button {
  background-color: #4a5568;
  color: white;
}

.submit-button:hover {
  background-color: #2d3748;
  transform: translateY(-1px);
}

.cancel-button {
  background-color: #e2e8f0;
  color: #4a5568;
}

.cancel-button:hover {
  background-color: #cbd5e0;
  transform: translateY(-1px);
}
</style>
