import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useUserStore } from '@/stores/user.js'

export const useBookStore = defineStore('book', () => {
  const userStore = useUserStore()
  const books = ref([])
  const categories = ref([])
  const threads = ref([])
  const newThread = ref({})
  const comments = ref([])

  const getBooks = () => {
    axios({
      method: 'GET',
      url: 'https://bookiwiki.onrender.com/books/',
    })
      .then((response) => {
        // console.log(response.data)
        books.value = response.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getCategories = () => {
    axios({
      url: 'https://bookiwiki.onrender.com/categories/',
      method: 'GET',
    })
      .then((response) => {
        // console.log(response.data)
        categories.value = response.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getThreads = () => {
    axios({
      method: 'GET',
      url: 'https://bookiwiki.onrender.com/threads/',
      // headers: {
      //   Authorization: `Token ${userStore.token}`,
      // },
    }).then((response) => {
      // console.log(response.data)
      threads.value = response.data
    })
  }

  const getBook = (bookId) => {
    return axios({
      method: 'get',
      url: `https://bookiwiki.onrender.com/books/${bookId}/`,
    })
      .then((response) => {
        return response.data
      })
      .catch((err) => {
        console.log(err)
        throw err
      })
  }

  const getThread = (threadId) => {
    return axios({
      method: 'get',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/`,
      // headers: {
      //   Authorization: `Token ${userStore.token}`,
      // },
    })
      .then((response) => {
        return response.data
      })
      .catch((err) => {
        console.log(err)
        throw err
      })
  }

  const deleteThread = (threadId) => {
    axios({
      method: 'delete',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        console.log(response)
        console.log('삭제 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const likesThread = (threadId) => {
    axios({
      method: 'post',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/likes/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        // console.log(response)
        return response.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const writeThread = async (threadData) => {
    try {
      const response = await axios({
        method: 'post',
        url: 'https://bookiwiki.onrender.com/threads/',
        data: threadData,
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${userStore.token}`,
        },
      })
      return response.data.id
    } catch (error) {
      // console.error('스레드 생성 오류:', error.response?.data || error)
      throw error
    }
  }

  const getComments = (threadId) => {
    return axios({
      method: 'get',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/comments/`,
    })
      .then((response) => {
        comments.value = response.data
        return response.data
      })
      .catch((err) => {
        console.log('댓글 가져오기 에러')
        console.log(err)
      })
  }

  const createComment = (threadId, content) => {
    return axios({
      method: 'post',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/comments/`,
      data: { content },
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        comments.value.unshift(response.data) // 댓글 위에서부터 추가
        return response.data
      })
      .catch((err) => {
        console.log('댓글 생성하기 에러')
        console.log(err)
      })
  }

  const updateComment = (commentId, content) => {
    return axios({
      method: 'put',
      url: `https://bookiwiki.onrender.com/comments/${commentId}/`,
      data: { content },
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        const index = comments.value.findIndex(
          (comment) => comment.id === commentId
        )
        if (index !== -1) {
          comments.value[index] = response.data
        }
        return response.data
      })
      .catch((err) => {
        console.log('댓글 수정하기 에러')
        console.log(err)
      })
  }

  const deleteComment = (commentId) => {
    return axios({
      method: 'delete',
      url: `https://bookiwiki.onrender.com/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        comments.value = comments.value.filter(
          (comment) => comment.id !== commentId
        )
        return response.data
      })
      .catch((err) => {
        console.log('댓글 삭제하기 에러')
        console.log(err)
      })
  }

  const updateThread = (threadId, threadData) => {
    return axios({
      method: 'put',
      url: `https://bookiwiki.onrender.com/threads/${threadId}/`,
      data: threadData,
      headers: {
        Authorization: `Token ${userStore.token}`,
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        // console.log('수정 성공:', response.data)
        return response.data
      })
      .catch((err) => {
        console.log('스레드 수정 실패', err)
        throw err
      })
  }

  return {
    books,
    getBooks,
    categories,
    getCategories,
    threads,
    comments,
    getThreads,
    getBook,
    getThread,
    deleteThread,
    likesThread,
    newThread,
    writeThread,
    getComments,
    createComment,
    updateComment,
    deleteComment,
    updateThread,
  }
})
