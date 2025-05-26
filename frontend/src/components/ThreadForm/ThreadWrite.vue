<template>
    <div class="thread-write">
      <h2 class="thread-write-title">
        <font-awesome-icon :icon="['fas', 'pen-to-square']" />
        {{ isEditMode ? '스레드 수정' : '스레드 작성' }}
      </h2>
      <div class="form-container">
        <div class="form-group">
          <label for="title">제목</label>
          <input 
            type="text" 
            id="title"
            v-model="title" 
            placeholder="스레드 제목을 입력하세요"
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label for="content">내용</label>
          <textarea 
            id="content"
            v-model="content" 
            placeholder="독서에 대한 생각을 자유롭게 작성해보세요"
            class="form-textarea"
          ></textarea>
        </div>
        <div class="form-group">
          <label for="reading_date">읽은 날짜</label>
          <input 
            type="date" 
            id="reading_date"
            v-model="reading_date" 
            class="form-input"
          />
        </div>
        <div class="button-group">
          <button @click="goBack" class="btn btn-cancel">
            <font-awesome-icon :icon="['fas', 'times']" />
            취소
          </button>
          <button @click="handleSubmit" class="btn btn-submit">
            <font-awesome-icon :icon="['fas', 'paper-plane']" />
            {{ isEditMode ? '수정완료' : '스레드 작성' }}
          </button>
        </div>
      </div>
    </div>
  </template>

  <script setup>
  const props = defineProps({
    bookId: Number,
  })

  import { useUserStore } from '@/stores/user.js'
  import { useBookStore } from '@/stores/book.js'
  import { ref, onMounted } from 'vue'
  import { useRouter, useRoute } from 'vue-router'

  const router = useRouter()
  const route = useRoute()

  const store = useUserStore()
  const bookStore = useBookStore()
  const thisUser = ref(null)

  const title = ref('')
  const content = ref('')
  const reading_date = ref('')
  const isEditMode = ref(false)
  const threadId = ref(null)

  onMounted(async () => {
    await store.getThisUser()
    thisUser.value = store.thisUser

    const type = route.query.type
    if (type === 'edit') { // 수정 모드일때
      isEditMode.value = true
      threadId.value = route.query.threadId
      try {
        const threadData = await bookStore.getThread(threadId.value)
        title.value = threadData.title
        content.value = threadData.content
        reading_date.value = threadData.reading_date
      } catch (error) {
        console.error(error)
        goBack()
      }
    }
  })

  const handleSubmit = async () => {
    if (!title.value || !content.value) {
      alert('제목과 내용을 입력해주세요.')
      return
    }

    try {
      if (isEditMode.value) {
        // 수정
        const updateData = {
          title: title.value,
          content: content.value,
          reading_date: reading_date.value,
          book: props.bookId,
          user: thisUser.value.id
        }
        await bookStore.updateThread(threadId.value, updateData)
        router.push(`/threads/${threadId.value}/`)
      } else {
        // 생성
        const threadData = {
          title: title.value,
          content: content.value,
          reading_date: reading_date.value,
          book: props.bookId,
          user: thisUser.value ? thisUser.value.id : null,
        }
        const newThreadId = await bookStore.writeThread(threadData)
        router.push(`/threads/${newThreadId}/`)
      }
    } catch (error) {
      console.error(isEditMode.value ? '스레드 수정 실패:' : '스레드 생성 실패:', error)
      alert(isEditMode.value ? '스레드 수정에 실패했습니다.' : '스레드 생성에 실패했습니다.')
    }
  }

  const goBack = () => {
    if (isEditMode.value) {
      router.push(`/threads/${threadId.value}/`)
    } else {
      router.back()
    }
  }
  </script>
  
  <style scoped>
  .thread-write {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    font-family: 'Noto Sans KR', sans-serif;
  }

  .thread-write-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0 0 2rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(76, 175, 80, 0.1);
  }

  .thread-write-title svg {
    color: #4caf50;
  }

  .form-container {
    padding-right: 2rem;
  }

  .form-group {
    margin-bottom: 1.5rem;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #2c3e50;
    font-size: 1.1rem;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .form-input,
  .form-textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid rgba(76, 175, 80, 0.2);
    border-radius: 8px;
    font-size: 1rem;
    color: #2c3e50;
    transition: all 0.3s ease;
    background: transparent;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .form-input:focus,
  .form-textarea:focus {
    outline: none;
    border-color: #4caf50;
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
  }

  .form-textarea {
    min-height: 200px;
    resize: vertical;
    line-height: 1.6;
  }

  .button-group {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
    justify-content: flex-end;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
  }

  .btn-cancel {
    background-color: #f8f9fa;
    color: #666;
  }

  .btn-cancel:hover {
    background-color: #e9ecef;
    color: #444;
  }

  .btn-submit {
    background-color: #4caf50;
    color: white;
  }

  .btn-submit:hover {
    background-color: #45a049;
    transform: translateY(-2px);
  }

  @media (max-width: 768px) {
    .thread-write {
      padding: 1.5rem;
    }

    .thread-write-title {
      font-size: 1.3rem;
      margin-bottom: 1.5rem;
    }

    .form-container {
      padding-right: 0;
    }

    .form-group {
      margin-bottom: 1rem;
    }

    label {
      font-size: 1rem;
    }

    .form-textarea {
      min-height: 150px;
    }

    .button-group {
      margin-top: 1.5rem;
    }

    .btn {
      padding: 0.6rem 1.2rem;
      font-size: 0.95rem;
    }
  }
  </style>
  
  