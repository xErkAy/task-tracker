<script>
import TableComponent from "@/components/HomeViewComponents/TableComponent.vue";
import { requests } from "@/requests";
import { statuses } from "@/statuses";
import TaskViewComponent from "@/components/HomeViewComponents/TaskViewComponent.vue";

export default {
  name: "MainViewComponent",
  components: { TaskViewComponent, TableComponent },
  data() {
    return {
      taskModal: {
        show: false,
        item: null,
      },
      tab: 0,
      loading: false,
      items: {
        all: [],
        active: [],
        planned: [],
        closed: [],
      },
    };
  },
  async created() {
    await this.init();
  },
  methods: {
    async init() {
      this.loading = true;
      try {
        const response = await requests.get("api/tasks/");
        this.items.all = response.data;
        this.items.active = response.data.filter(
          (i) => i.status === statuses.in_progress
        );
        this.items.planned = response.data.filter((i) =>
          [statuses.not_started, statuses.in_analysis].includes(i.status)
        );
        this.items.closed = response.data.filter(
          (i) => i.status === statuses.closed
        );
        // eslint-disable-next-line no-empty
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },
    async showModal(value) {
      this.taskModal.item = value;
      this.taskModal.show = true;
    },
  },
};
</script>

<template>
  <v-card class="home-view__table">
    <v-card-title>
      <v-tabs v-model="tab" bg-color="white" slider-color="#694fff">
        <v-tab value="all">Все</v-tab>
        <v-tab value="active">Активные</v-tab>
        <v-tab value="planned">Планируемые</v-tab>
        <v-tab value="closed">Закрытые</v-tab>

        <v-spacer />
        <v-icon icon="mdi-plus" size="25" @click="showModal(null)" />
      </v-tabs>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="all">
          <table-component
            v-model:loading="loading"
            :items="items.all"
            @update-list="init"
            @select-item="showModal"
          />
        </v-tabs-window-item>
        <v-tabs-window-item value="active">
          <table-component
            v-model:loading="loading"
            :items="items.active"
            @update-list="init"
            @select-item="showModal"
          />
        </v-tabs-window-item>
        <v-tabs-window-item value="planned">
          <table-component
            v-model:loading="loading"
            :items="items.planned"
            @update-list="init"
            @select-item="showModal"
          />
        </v-tabs-window-item>
        <v-tabs-window-item value="closed">
          <table-component
            v-model:loading="loading"
            :items="items.closed"
            @update-list="init"
            @select-item="showModal"
          />
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-title>
  </v-card>
  <TaskViewComponent
    @update-list="init"
    v-if="taskModal.show"
    v-model:show="taskModal.show"
    :item="taskModal.item"
  />
</template>

<style scoped lang="scss"></style>
