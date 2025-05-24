import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useBookStore = defineStore('book', () => {
  const books = ref([])
  const categories = ref([])
  const threads = ref([])

  const getBooks = () => {
    axios({
      method: 'GET',
      url: 'http://localhost:8000/books/',
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
      url: 'http://localhost:8000/categories/',
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
      url: 'http://localhost:8000/threads/',
    }).then((response) => {
      // console.log(response.data)
      threads.value = response.data
    })
  }

  const getBook = (bookId) => {
    return axios({
      method: 'get',
      url: `http://localhost:8000/books/${bookId}/`,
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
      url: `http://localhost:8000/threads/${threadId}/`,
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
      url: `http://localhost:8000/threads/${threadId}/`,
    })
      .then((response) => {
        console.log('삭제 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return {
    books,
    getBooks,
    categories,
    getCategories,
    threads,
    getThreads,
    getBook,
    getThread,
    deleteThread,
  }
})
