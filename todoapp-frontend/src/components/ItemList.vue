<script setup lang="ts">
import { ref, computed } from "vue";
import axios from "axios";
import { Item } from "./types";
import SearchInput from "./SearchInput.vue";
import AddItemForm from "./AddItemForm.vue";

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

    <table class="table__item min-w-max w-full table-auto">
      <thead>
        <tr class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
          <th class="py-3 px-6 text-left"></th>
          <th class="py-3 px-6 text-left">Title</th>
          <th class="py-3 px-6 text-left">Description</th>
          <th class="py-3 px-6 text-left">Status</th>
          <th class="py-3 px-6 text-left">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in filteredItems"
          :key="item.id"
          class="border-b border-gray-200 hover:bg-gray-100"
          :class="{ 'completed-item': item.completed }"
        >
          <td class="py-3 px-6 text-left whitespace-nowrap">
            <input
              type="checkbox"
              v-model="item.completed"
              @change="updateItem(item)"
            />
          </td>
          <td class="item__title">{{ item.title }}</td>
          <td class="item__description">{{ item.description }}</td>
          <td>
            <span
              class="py-1 px-3 rounded-full text-xs bg-yellow-200 text-yellow-600"
              :class="
                item.completed
                  ? 'bg-green-200 text-green-600'
                  : 'bg-yellow-200 text-yellow-600'
              "
            >
              {{ item.completed ? "Completed" : "Pending" }}</span
            >
          </td>
          <td>
            <template v-if="!item.completed">
              <button
                class="completed-button"
                @click="item.id !== undefined && deleteItem(item.id)"
              >
                Delete
              </button>
            </template>
          </td>
        </tr>
      </tbody>
    </table>
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

.table__item {
  width: 80%;
}
.completed-item .item__title,
.completed-item .item__description {
  text-decoration: line-through;
}
.table-auto {
  width: auto;
}
.bg-gray-200 {
  background-color: #edf2f7;
}
.text-gray-600 {
  color: #4a5568;
}
.uppercase {
  text-transform: uppercase;
}
.py-3 {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}
.px-6 {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}
.text-left {
  text-align: left;
}
.text-center {
  text-align: center;
}
.border-b {
  border-bottom-width: 1px;
}
.border-gray-200 {
  border-color: #edf2f7;
}
.hover\:bg-gray-100:hover {
  background-color: #f7fafc;
}
.whitespace-nowrap {
  white-space: nowrap;
}
.bg-green-200 {
  background-color: #c6f6d5;
}
.text-green-600 {
  color: #38a169;
}
.py-1 {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}
.px-3 {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}
.rounded-full {
  border-radius: 9999px;
}
.text-xs {
  font-size: 0.75rem;
}
.bg-red-200 {
  background-color: #feb2b2;
}
.text-red-600 {
  color: #c53030;
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

.completed-button {
  padding: 0.5rem;
  background-color: #039be5;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.completed-button:hover {
  background-color: #0288d1;
}

.completed-button:active {
  background-color: #0277bd;
}
</style>
