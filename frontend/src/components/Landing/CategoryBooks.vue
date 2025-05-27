<template>
  <div class="category-section">
    <h2 class="section-title">
      <i class="fas fa-tags"></i>
      장르별 도서
    </h2>
    <div class="category-container">
      <button
        v-for="category in categories"
        :key="category.id"
        class="category-button"
        @click="moveToBookList(category.id)"
      >
        <i class="fas fa-book"></i>
        {{ category.name }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useBookStore } from "@/stores/book.js";

const router = useRouter();
const store = useBookStore();
const categories = computed(() => store.categories);

onMounted(() => {
  store.getCategories();
});

const moveToBookList = (categoryId) => {
  router.push({ name: "bookList", query: { category: categoryId } });
};
</script>

<style scoped>
.category-section {
  width: 100%;
}

.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-title i {
  color: #4caf50;
  font-size: 1.2em;
}

.category-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  padding: 0.5rem;
}

.category-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background-color: white;
  color: #4caf50;
  border: 2px solid #4caf50;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.category-button i {
  font-size: 0.9em;
  transition: transform 0.3s ease;
}

.category-button:hover {
  background-color: #4caf50;
  color: white;
  transform: translateY(-2px);
}

.category-button:hover i {
  transform: rotate(-15deg);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.3rem;
    margin-bottom: 1.5rem;
  }

  .category-button {
    padding: 0.6rem 1rem;
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .category-container {
    gap: 0.75rem;
  }

  .category-button {
    padding: 0.5rem 0.875rem;
    font-size: 0.9rem;
  }
}
</style>
