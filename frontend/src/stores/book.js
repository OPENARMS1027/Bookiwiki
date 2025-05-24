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

  return { books, getBooks, categories, getCategories, threads, getThreads }
})
