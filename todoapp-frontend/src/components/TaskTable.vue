<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import { Item } from "./types";

const props = defineProps<{
  filteredItems: Item[];
}>();

const emit = defineEmits(["delete", "update"]);

const deleteItem = (itemId: number) => {
  emit("delete", itemId);
};

const updateItem = (item: Item) => {
  emit("update", item);
};
</script>
<template>
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
        v-for="item in props.filteredItems"
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
            {{ item.completed ? "Completed" : "Pending" }}
          </span>
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
</template>

<style scoped>
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

.text-sm {
  font-size: 0.875rem;
}

.leading-normal {
  line-height: 1.5;
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

.bg-yellow-200 {
  background-color: #fff88d;
}

.text-yellow-600 {
  color: #c7a500;
}

.bg-green-200 {
  background-color: #a3fba1;
}

.text-green-600 {
  color: #228b22;
}

.completed-button {
  background-color: transparent;
  border: none;
  color: #3182ce;
  cursor: pointer;
}

.completed-button:hover {
  text-decoration: underline;
}
.completed-button:active {
  background-color: #0277bd;
}
</style>
