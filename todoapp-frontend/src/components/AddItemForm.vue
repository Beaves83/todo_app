<script setup lang="ts">
import { ref, defineEmits } from "vue";

const newItem = ref({ title: "", description: "", completed: false });

const emit = defineEmits(["add"]);

const addItem = () => {
  emit("add", newItem.value);
  newItem.value = { title: "", description: "", completed: false };
};
</script>
<template>
  <div class="add-item">
    <div class="add-item__header">
      <h3 class="add-item__title">Add new item</h3>
    </div>
    <form @submit.prevent="addItem" class="add-item__form">
      <div class="add-item__form-group">
        <label for="title" class="add-item__label">Title</label>
        <input
          type="text"
          id="title"
          v-model="newItem.title"
          class="add-item__input"
        />
      </div>
      <div class="add-item__form-group">
        <label for="description" class="add-item__label">Description</label>
        <input
          type="text"
          id="description"
          v-model="newItem.description"
          class="add-item__input"
        />
      </div>
      <button type="submit" class="add-item__button">Add item</button>
    </form>
  </div>
</template>
<style scoped>
.add-item {
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.add-item__header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.add-item__title {
  font-weight: bold;
  margin-right: 1rem;
}

.add-item__form {
  display: flex;
  flex-direction: column;
}

.add-item__form-group {
  margin-bottom: 1rem;
}

.add-item__label {
  font-weight: bold;
  margin-right: 20px;
}

.add-item__input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

.add-item__button {
  padding: 0.5rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.add-item__button:hover {
  background-color: #45a049;
}

.add-item__button:active {
  background-color: #3e8e41;
}
</style>
