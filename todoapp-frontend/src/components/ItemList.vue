<script setup lang="ts">
import { ref, computed } from "vue";
import axios from "axios";
import { Item } from "./types";
import SearchInput from "./SearchInput.vue";
import AddItemForm from "./AddItemForm.vue";
import TaskTable from "./TaskTable.vue";

// Constants
const searchQuery = ref("");
const items = ref<Item[]>([]);
const newItem = ref<Item>({ title: "", description: "", completed: false });
const url = "http://localhost:8000/items";

// Computeds
const filteredItems = computed(() => {
  return items.value.filter(
    (item) =>
      item.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      item.description.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

// Methods
const fetchItems = () => {
  axios
    .get(url)
    .then((response) => {
      items.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
};

const addItem = (item: Item) => {
  axios
    .post(url, item)
    .then(() => {
      fetchItems();
      newItem.value = { title: "", description: "", completed: false };
    })
    .catch((error) => {
      console.error(error);
    });
};

const deleteItem = (itemId: number) => {
  axios
    .delete(`${url}/${itemId}`)
    .then(() => {
      fetchItems();
    })
    .catch((error) => {
      console.error(error);
    });
};

const updateItem = (item: Item) => {
  axios
    .put(`${url}/${item.id}`, item)
    .then(() => {
      fetchItems();
    })
    .catch((error) => {
      console.error(error);
    });
};

fetchItems();

const updateSearchQuery = (newValue: string) => {
  searchQuery.value = newValue;
};
</script>

<template>
  <div class="container">
    <h1 class="title">ToDo list</h1>

    <SearchInput @updateSearchQuery="updateSearchQuery" v-model="searchQuery" />
    <TaskTable
      :filteredItems="filteredItems"
      @delete="deleteItem"
      @update="updateItem"
    />
    <AddItemForm @add="addItem" />
  </div>
</template>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  font-size: 2rem;
  font-weight: bold;
  margin: 2rem;
}
.border-b {
  border-bottom-width: 1px;
}

.delete-button {
  padding: 0.5rem;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-button:hover {
  background-color: #e53935;
}

.delete-button:active {
  background-color: #d32f2f;
}
</style>
