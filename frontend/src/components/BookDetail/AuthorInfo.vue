<template>
  <div class="container">
    <header class="header">
      <p class="header-title">작가정보</p>
    </header>
    <div class="author-info">
      <div class="author-text">
        <p class="author-title">{{ book.author }}</p>
        <p></p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  book: Object,
})
</script>

<style scoped>
.header {
  display: flex;
  flex-direction: row;
  width: 70%;
  padding: 20px 0;
}

.header-title {
  font-weight: 600;
  font-size: large;
}

.author-title {
  font-weight: 600;
  font-size: medium;
}

.author-image {
  padding: 20px;
  width: 30%;
}

img {
  border-radius: 50%;
  width: 130px;
  height: auto;
}

.author-text {
  padding: 20px;
}
</style>
