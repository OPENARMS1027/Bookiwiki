<template>
  <div v-if="book">
    <header class="header">
      <p class="book-title">{{ book.title }}</p>
      <div class="button-group">
        <button class="add-button" @click="moveToAdd(book.id)">
          <i class="fas fa-bookmark"></i> 내 서재에 담기
        </button>
        <button class="thread-button" @click="moveToThread(book.id)">
          <i class="fas fa-pen"></i> 스레드 작성
        </button>
      </div>
      <!-- <div v-else class="login-message">
          <router-link to="/login" class="login-link">로그인</router-link>하고 더 많은 기능을 사용해보세요!
        </div> -->
    </header>
    <div class="book-info">
      <div class="book-image">
        <img :src="book.cover" alt="book_cover" />
      </div>
      <div class="book-text">
        <p>{{ book.description }}</p>
        <br />
        <span>
          <strong>저자:</strong> {{ book.author }}<br />
          <strong>출판사:</strong> {{ book.publisher }}<br />
          <strong>출판일:</strong> {{ book.pub_date }}<br />
          <strong>ISBN:</strong> {{ book.isbn }}<br />
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import axios from "axios";

defineProps({
  book: Object,
});
const router = useRouter();
const userStore = useUserStore();

// console.log(book)
// 스레드 생성 페이지 이동
const moveToThread = async (bookId) => {
  if (!userStore.isLogin || !userStore.token) {
    alert("로그인이 필요한 서비스입니다.");
    // 현재 페이지의 경로를 쿼리 파라미터로 같이 보내주기
    router.push({
      name: "login",
      query: { redirect: router.currentRoute.value.fullPath },
    });
    return;
  }

  try {
    // 토큰 유효성 확인
    await axios.get("http://127.0.0.1:8000/accounts/user/", {
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    });

    // 토큰이 유효하면 스레드 작성 페이지로 이동
    router.push({ name: "threadForm", params: { bookId: bookId } });
  } catch (error) {
    console.error("인증 확인 실패:", error);
    alert("로그인이 필요합니다. 다시 로그인해주세요.");
    router.push({ name: "login" });
  }
};

// 서재에 담기 버튼 함수
const moveToAdd = async (bookId) => {
  try {
    // 서재에 책 추가 API 호출
    await axios.post(
      "http://127.0.0.1:8000/books/userbooks/",
      {
        book_id: bookId,
      },
      {
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      }
    );

    // 성공 알림
    alert("내 서재에 저장되었습니다");
  } catch (error) {
    if (
      error.response?.status === 400 &&
      error.response?.data?.message === "already_exists"
    ) {
      alert("이미 서재에 존재하는 책입니다");
    } else {
      console.error("서재 담기 실패:", error);
      alert("서재 담기에 실패했습니다");
    }
  }
};

// 서재에 담기 버튼 함수
// const moveToAdd = async (bookId) => {
//   if (!userStore.isLogin) {
//     alert('로그인이 필요한 서비스입니다.')
//     // 현재 페이지의 경로를 쿼리 파라미터로 같이 보내주기
//     router.push({
//       name: 'login',
//       query: { redirect: router.currentRoute.value.fullPath },
//     })
//     return
//   }

//   try {
//     await axios.post(
//       'http://127.0.0.1:8000/books/userbooks/',
//       {
//         book_id: bookId,
//       },
//       {
//         headers: {
//           Authorization: `Token ${userStore.token}`,
//         },
//       }
//     )
//     alert('내 서재에 저장되었습니다')
//   } catch (error) {
//     if (
//       error.response?.status === 400 &&
//       error.response?.data?.message === 'already_exists'
//     ) {
//       alert('이미 서재에 존재하는 책입니다')
//     } else {
//       console.error('서재 담기 실패:', error)
//       alert('서재 담기에 실패했습니다')
//     }
//   }
// }
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.book-title {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
  margin: 0;
  flex: 1;
}

.button-group {
  display: flex;
  gap: 1rem;
}

.add-button,
.thread-button {
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  border: none;
}

.add-button {
  background-color: #4caf50;
  color: white;
}

.add-button:hover {
  background-color: #45a049;
  transform: translateY(-2px);
}

.thread-button {
  background-color: white;
  color: #4caf50;
  border: 2px solid #4caf50;
}

.thread-button:hover {
  background-color: #4caf50;
  color: white;
  transform: translateY(-2px);
}

.book-info {
  display: flex;
  gap: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.book-image {
  flex-shrink: 0;
}

.book-image img {
  width: 300px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease;
}

.book-image img:hover {
  transform: scale(1.02);
}

.book-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.book-text p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #2c3e50;
  margin: 0;
}

.book-text span {
  display: grid;
  gap: 1rem;
  font-size: 1.05rem;
  color: #666;
}

.book-text strong {
  color: #4caf50;
  display: inline-block;
  width: 80px;
}

@media (max-width: 1024px) {
  .book-info {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }

  .book-image img {
    width: 250px;
  }

  .book-text {
    text-align: center;
  }

  .book-text span {
    justify-items: center;
  }

  .book-text strong {
    width: auto;
    margin-right: 0.5rem;
  }
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }

  .book-title {
    font-size: 1.5rem;
    text-align: center;
  }

  .button-group {
    width: 100%;
  }

  .add-button,
  .thread-button {
    flex: 1;
    justify-content: center;
    padding: 0.6rem 1rem;
    font-size: 0.9rem;
  }

  .book-info {
    padding: 1rem;
  }

  .book-image img {
    width: 200px;
  }

  .book-text p {
    font-size: 1rem;
  }

  .book-text span {
    font-size: 0.95rem;
  }
}
</style>
