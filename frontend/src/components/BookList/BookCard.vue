<template>
  <div class="container">
    <div class="book-card" @click="moveToDetail(book.id)">
      <img :src="book.cover" alt="book_cover" class="book-cover-img" />
      <div class="book-description">
        <p class="book-title">
          {{ book.title }}
        </p>
        <p class="book-info">
          {{ book.author }} | {{ book.publisher }} |
          {{ book.pub_date }}
        </p>
        <p class="book-subtitle">{{ book.subTitle }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const props = defineProps({
  book: Object,
});

const router = useRouter();
const book = props.book;
const moveToDetail = (bookId) => {
  router.push({ name: "bookDetail", params: { bookId: bookId } });
};
</script>

<style scoped>
.book-card {
  display: flex;
  align-items: center;
  background-color: rgb(46, 46, 46);
  margin: 10px;
  padding: 30px 15px;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.book-card:hover {
  transform: translateY(-5px);
}

.book-cover-img {
  width: 80px;
}

p {
  padding: 5px 0px;
  margin: 0;
}

.book-description {
  display: flex;
  flex-direction: column;
  align-items: start;
  margin-left: 10px;
}

.book-title {
  font-size: larger;
  font-weight: 500;
  color: white;
}

.book-info {
  color: rgb(100, 99, 96);
}

.book-subtitle {
  color: rgb(139, 137, 132);
}
</style>