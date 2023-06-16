<script setup lang="ts">
import { ref, computed } from "vue";
import axios from "axios";
import { Item } from "./types";

const items = ref<Item[]>([]);
const newItem = ref<Item>({ title: "", description: "", completed: false });
const searchQuery = ref("");

const filteredItems = computed(() => {
  return items.value.filter(
    (item) =>
      item.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      item.description.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const fetchItems = () => {
  axios
    .get("http://localhost:8000/items")
    .then((response) => {
      items.value = response.data;
    })
    .catch((error) => {
      console.error(error);
    });
};

const addItem = () => {
  axios
    .post("http://localhost:8000/items", newItem.value)
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
    .delete(`http://localhost:8000/items/${itemId}`)
    .then(() => {
      fetchItems();
    })
    .catch((error) => {
      console.error(error);
    });
};

const updateItem = (item: Item) => {
  axios
    .put(`http://localhost:8000/items/${item.id}`, item)
    .then(() => {
      fetchItems();
    })
    .catch((error) => {
      console.error(error);
    });
};

fetchItems();
</script>

<template>
  <div>
    <h2>Todo List</h2>
    <input v-model="searchQuery" placeholder="Search" />

    <table class="item-table">
      <thead>
        <tr>
          <th></th>
          <th>Title</th>
          <th>Description</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in filteredItems"
          :key="item.id"
          :class="{ 'completed-item': item.completed }"
        >
          <td>
            <input
              type="checkbox"
              v-model="item.completed"
              @change="updateItem(item)"
            />
          </td>
          <td>{{ item.title }}</td>
          <td>{{ item.description }}</td>
          <td>
            <span class="status" :class="{ completed: item.completed }">{{
              item.completed ? "Completed" : "Pending"
            }}</span>
          </td>
          <td>
            <template v-if="!item.completed">
              <button
                class="delete-btn"
                @click="item.id !== undefined && deleteItem(item.id)"
              >
                Delete
              </button>
            </template>
          </td>
        </tr>
      </tbody>
    </table>

    <form @submit.prevent="addItem">
      <input v-model="newItem.title" placeholder="Title" />
      <input v-model="newItem.description" placeholder="Description" />
      <button type="submit">Add Item</button>
    </form>
  </div>
</template>
<style scoped>
.completed-item {
  text-decoration: line-through;
}

.item-table {
  width: 100%;
  border-collapse: collapse;
}

.item-table th,
.item-table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.item-table th {
  background-color: #f2f2f2;
}

.completed-item {
  text-decoration: line-through;
}

.status {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  color: #fff;
}

.completed {
  background-color: green;
}

.delete-btn {
  padding: 4px 8px;
  border: none;
  background-color: #ff0000;
  color: #fff;
  cursor: pointer;
}
</style>
