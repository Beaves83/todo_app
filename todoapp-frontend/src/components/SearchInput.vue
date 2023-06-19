<script setup lang="ts">
import { ref, watch, defineEmits } from "vue";

const searchQuery = ref("");

const emit = defineEmits(["updateSearchQuery"]);

watch(searchQuery, (newValue) => {
  emit("updateSearchQuery", newValue);
});
</script>

<template>
  <div class="search">
    <h2 class="search__title">Search items</h2>
    <input
      type="text"
      v-model="searchQuery"
      class="search__input w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
      placeholder="Search"
    />
  </div>
</template>

<style scoped>
.search {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
}

.search__input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 300px;
  margin-left: 10px;
}
</style>
