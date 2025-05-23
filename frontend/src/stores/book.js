import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
export const useBookStore = defineStore("book", () => {
  const books = ref([]);
  const categories = ref([]);

  const getBooks = () => {
    axios({
      method: "GET",
      url: "http://localhost:8000/books/",
    }).then((response) => {
      books.value = response.data;
      console.log(response.data);
    });
  };

  const getCategories = () => {
    axios({
      method: "GET",
      url: "http://localhost:8000/categories/",
    }).then((response) => {
      categories.value = response.data;
      console.log(response.data);
    });
  };

  return { books, categories, getBooks, getCategories };
});
