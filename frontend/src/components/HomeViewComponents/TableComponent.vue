<script>
import { requests } from "@/requests";
import { statuses, statusesList } from "@/statuses";
import { formatTime } from "@/utils";

export default {
  name: "TableComponent",
  computed: {
    statuses() {
      return statuses;
    },
    statusesList() {
      return statusesList;
    },
  },
  props: ["items", "loading"],
  emits: ["updateList", "selectItem", "update:loading"],

  data() {
    return {
      headers: [
        { title: "ID", key: "id", width: "10%" },
        { title: "Задача", key: "name", width: "20%" },
        { title: "Статус", key: "status", width: "15%" },
        { title: "Исполнитель", key: "performer", width: "20%" },
        { title: "Автор", key: "author", width: "15%" },
        { title: "Создана", key: "created_at", width: "10%" },
        { title: "Обновлена", key: "updated_at", width: "10%" },
      ],
    };
  },
  methods: {
    formatTime,
    async selectItem(item) {
      this.$emit("selectItem", item);
    },
    async changeStatus(value, item) {
      this.$emit("update:loading", true);
      try {
        await requests.patch(`api/tasks/${item.id}/`, {
          status: value,
        });
        this.$emit("updateList");
        // eslint-disable-next-line no-empty
      } catch (error) {
      } finally {
        this.$emit("update:loading", true);
      }
    },
  },
};
</script>

<template>
  <v-data-table
    :loading="loading"
    :headers="headers"
    :items="items"
    no-data-text="Нет задач"
    loading-text="Загрузка данных"
    :items-per-page="-1"
  >
    <template v-slot:[`item.id`]="{ item }">
      <div @click="selectItem(item)">
        {{ item.id }}
      </div>
    </template>
    <template v-slot:[`item.name`]="{ item }">
      <div @click="selectItem(item)">
        {{ item.name }}
      </div>
    </template>
    <template v-slot:[`item.status`]="{ item }">
      <v-select
        v-if="item.status !== statuses"
        @update:model-value="changeStatus($event, item)"
        variant="outlined"
        density="compact"
        :items="statusesList.filter((i) => i.id >= item.status)"
        v-model="item.status"
        item-value="id"
        item-title="name"
      ></v-select>
      <div v-else>
        {{ statuses.find((i) => i.id >= item.status).name }}
      </div>
    </template>
    <template v-slot:[`item.performer`]="{ item }">
      <div @click="selectItem(item)">
        {{ item.performer.full_name }}
      </div>
    </template>
    <template v-slot:[`item.author`]="{ item }">
      <div @click="selectItem(item)">
        {{ item.author.full_name }}
      </div>
    </template>
    <template v-slot:[`item.created_at`]="{ item }">
      <div @click="selectItem(item)">
        {{ formatTime(item.created_at, true) }}
      </div>
    </template>
    <template v-slot:[`item.updated_at`]="{ item }">
      <div @click="selectItem(item)">
        {{ formatTime(item.updated_at, true) }}
      </div>
    </template>
    <template v-slot:bottom></template>
  </v-data-table>
</template>

<style scoped lang="scss">
:deep(.v-data-table__tr:hover) {
  background-color: #f7f7f7;
  cursor: pointer;
}
</style>
