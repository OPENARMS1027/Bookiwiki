<template>
  <div class="comment-container">
    <div class="comment-header">
      <h3>
        <font-awesome-icon :icon="['fas', 'comments']" />
        댓글
      </h3>
    </div>
    <template v-if="userStore.isLogin">
      <div class="comment-form">
        <input
          v-model="commentContent"
          type="text"
          placeholder="댓글을 입력하세요"
          class="comment-input"
          @keyup.enter="submitComment"
        />
        <button @click="submitComment" class="submit-button">
          <font-awesome-icon :icon="['fas', 'paper-plane']" />
        </button>
      </div>
    </template>
    <template v-else>
      <div class="login-message">
        <RouterLink :to="{ name: 'login' }" class="login-link">로그인</RouterLink>하고 댓글을 작성해보세요!
      </div>
    </template>
    <div class="comment-list">
      <div v-for="comment in comments" :key="comment.id" class="comment-item">
        <div class="comment-content">
          <div v-if="editingCommentId !== comment.id" class="comment-text">
            {{ comment.content }}
          </div>
          <input
            v-else
            v-model="editContent"
            type="text"
            class="edit-input"
            @keyup.enter="updateComment(comment.id)"
          />
        </div>
        <div
          class="comment-actions"
          v-if="userStore.thisUser && userStore.thisUser.id === comment.user"
        >
          <button
            v-if="editingCommentId !== comment.id"
            @click="startEdit(comment)"
            class="action-btn"
          >
            <font-awesome-icon :icon="['fas', 'edit']" />
          </button>
          <button
            v-if="editingCommentId === comment.id"
            @click="updateComment(comment.id)"
            class="action-btn"
          >
            <font-awesome-icon :icon="['fas', 'check']" />
          </button>
          <button @click="deleteComment(comment.id)" class="action-btn delete">
            <font-awesome-icon :icon="['fas', 'trash']" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useBookStore } from '@/stores/book'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'
import { RouterLink } from 'vue-router'

const props = defineProps({
  threadId: {
    type: Number,
    required: true,
  },
})

const bookStore = useBookStore()
const userStore = useUserStore()
const { comments } = storeToRefs(bookStore)

const commentContent = ref('')
const editingCommentId = ref(null)
const editContent = ref('')

onMounted(() => {
  bookStore.getComments(props.threadId)
})

const submitComment = () => {
  if (!commentContent.value.trim()) return

  bookStore
    .createComment(props.threadId, commentContent.value)
    .then(() => {
      commentContent.value = ''
    })
    .catch((err) => {
      console.log(err)
      alert('댓글 작성에 실패했습니다.')
    })
}

const startEdit = (comment) => {
  editingCommentId.value = comment.id
  editContent.value = comment.content
}

const updateComment = (commentId) => {
  if (!editContent.value.trim()) return

  bookStore
    .updateComment(commentId, editContent.value)
    .then(() => {
      editingCommentId.value = null
    })
    .catch((err) => {
      console.log(err)
      alert('댓글 수정에 실패했습니다.')
    })
}

const deleteComment = (commentId) => {
  if (!confirm('정말 삭제하시겠습니까?')) return

  bookStore.deleteComment(commentId).catch((err) => {
    console.log(err)
    alert('댓글 삭제에 실패했습니다.')
  })
}
</script>

<style scoped>
.comment-container {
  padding: 1.5rem;
}

.comment-header {
  margin-bottom: 1.5rem;
}

.comment-header h3 {
  font-size: 1.2em;
  font-weight: 600;
  color: #4CAF50;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0;
}

.login-message {
  text-align: center;
  padding: 1rem;
  background: rgba(76, 175, 80, 0.05);
  border-radius: 8px;
  margin-bottom: 2rem;
  color: #666;
}

.login-link {
  color: #4CAF50;
  text-decoration: none;
  font-weight: 500;
  margin: 0 0.3rem;
}

.login-link:hover {
  text-decoration: underline;
}

.comment-form {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.comment-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 8px;
  background: transparent;
  color: inherit;
  font-size: 0.95em;
  transition: all 0.3s ease;
}

.comment-input:focus {
  outline: none;
  border-color: #4CAF50;
  box-shadow: 0 0 8px rgba(76, 175, 80, 0.2);
}

.submit-button {
  background: #4CAF50;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.submit-button:hover {
  background: #43A047;
}

.comment-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.comment-item {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 1rem;
  border: 1px solid rgba(76, 175, 80, 0.1);
  border-radius: 8px;
  transition: all 0.3s ease;
}

.comment-item:hover {
  background: rgba(76, 175, 80, 0.02);
  border-color: rgba(76, 175, 80, 0.2);
}

.comment-content {
  flex: 1;
  margin-right: 1rem;
}

.comment-text {
  line-height: 1.5;
  word-break: break-all;
}

.comment-actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  background: transparent;
  border: none;
  color: inherit;
  padding: 0.4rem;
  cursor: pointer;
  opacity: 0.6;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.action-btn:hover {
  opacity: 1;
  background: rgba(76, 175, 80, 0.1);
  color: #4CAF50;
}

.action-btn.delete:hover {
  background: rgba(244, 67, 54, 0.1);
  color: #F44336;
}

.edit-input {
  width: 100%;
  padding: 0.5rem;
  border: 2px solid rgba(76, 175, 80, 0.2);
  border-radius: 4px;
  background: transparent;
  color: inherit;
  font-size: 0.95em;
}

.edit-input:focus {
  outline: none;
  border-color: #4CAF50;
}

@media (max-width: 768px) {
  .comment-container {
    padding: 1rem;
  }

  .comment-form {
    margin-bottom: 1.5rem;
  }

  .comment-item {
    padding: 0.75rem;
  }
}
</style>
