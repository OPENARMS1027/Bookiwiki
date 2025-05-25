<template>
  <div class="comment-container">
    <div class="comment-form">
      <input
        v-model="commentContent"
        type="text"
        placeholder="댓글을 입력하세요"
        class="comment-input"
      />
      <button @click="submitComment" class="submit-button">작성</button>
    </div>
    <div class="comment-list">
      <div v-for="comment in comments" :key="comment.id" class="comment-item">
        <div class="comment-content">
          <span class="comment-text">{{ comment.content }}</span>
        </div>
        <div
          class="comment-actions"
          v-if="userStore.thisUser.id === comment.user"
        >
          <button
            v-if="editingCommentId !== comment.id"
            @click="startEdit(comment)"
            class="edit-button"
          >
            수정
          </button>
          <button
            v-if="editingCommentId === comment.id"
            @click="updateComment(comment.id)"
            class="save-button"
          >
            수정 완료
          </button>
          <button @click="deleteComment(comment.id)" class="delete-button">
            삭제
          </button>
        </div>
        <input
          v-if="editingCommentId === comment.id"
          v-model="editContent"
          type="text"
          class="edit-input"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useBookStore } from '@/stores/book'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

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
.comment-form {
  display: flex;
}

.submit-button {
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.comment-list {
  display: flex;
  flex-direction: column;
}

.comment-item {
  border: 1px solid #ddd;
}

.comment-content {
  margin-bottom: 10px;
}

.comment-text {
  display: block;
}

.edit-button,
.save-button,
.delete-button {
  cursor: pointer;
}

.edit-input {
  width: 100%;
  border: 1px solid #ddd;
}
</style>
