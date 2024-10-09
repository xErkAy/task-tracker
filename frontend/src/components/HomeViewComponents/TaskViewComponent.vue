<script>
import { mapGetters } from "vuex";
import VueDatePicker from "@vuepic/vue-datepicker";
import { requests } from "@/requests";

export default {
  name: "TaskViewComponent",
  components: { VueDatePicker },
  props: ["show", "item"],
  emits: ["updateList", "update:show", "update:item"],
  data() {
    return {
      rules: {
        required: {
          rules: [(v) => !!v || "Обязательное поле"],
        },
        minLength: {
          length: 5,
          rules: [
            (v) => !!v || "Обязательное поле",
            (v) => v.length >= 5 || "Минимальное количество символов - 5",
          ],
        },
      },
      taskItem: null,
      loading: false,
    };
  },
  async beforeMount() {
    this.taskItem = structuredClone(this.item);
    if (this.taskItem === null) {
      this.taskItem = {
        name: null,
        tags: [],
        description: null,
        author: null,
        performer: null,
        due_date: null,
        status: 1,
      };
    }
  },
  computed: {
    ...mapGetters(["users", "tags"]),
    isOpened: {
      get() {
        return this.show;
      },
      set(value) {
        this.$emit("update:show", value);
      },
    },
    formIsValid() {
      if (!this.taskItem) return false;
      let isValid = true;
      Object.keys(this.taskItem).forEach((key) => {
        if (key !== "due_date" && !this.taskItem[key]) isValid = false;
        else if (
          ["name", "description"].includes(key) &&
          this.taskItem[key].length < this.rules.minLength.length
        )
          isValid = false;
      });
      return isValid;
    },
  },
  methods: {
    async save() {
      if (!this.formIsValid)
        return this.$notify({
          text: "Заполните все поля",
          type: "error",
        });

      try {
        const response = this.taskItem?.id
          ? await requests.put(`api/tasks/${this.taskItem.id}/`, this.taskItem)
          : await requests.post("api/tasks/", this.taskItem);
        if (!this.taskItem?.id)
          this.$notify({
            text: "Задача успешно создана",
          });
        this.taskItem = response.data;
        this.$emit("updateList");
        // eslint-disable-next-line no-empty
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<template>
  <v-menu
    location="right"
    v-model="isOpened"
    :close-on-content-click="false"
    :transition="{ name: 'slide-x-reverse-transition', duration: 3000 }"
  >
    <template v-slot:activator="{ props }">
      <div v-bind="props"></div>
    </template>
    <v-card
      :loading="loading"
      style="background-color: #f7f7f7"
      elevation="5"
      class="menu-component"
    >
      <v-card-title style="font-weight: bold; display: flex">
        <div>
          {{ taskItem?.id ? `Задача №${taskItem.id}` : "Создание задачи" }}
        </div>
        <v-spacer />
        <div style="display: flex">
          <v-icon
            :disabled="!formIsValid"
            style="cursor: pointer"
            icon="mdi-check"
            @click="save"
          />
          <v-icon
            style="cursor: pointer; margin-left: 1rem"
            icon="mdi-close"
            @click="isOpened = false"
          />
        </div>
      </v-card-title>
      <v-card-text>
        <div class="menu-component__block">
          <span class="menu-component__block__title">Название</span>
          <v-text-field
            clearable
            required
            :rules="rules.minLength.rules"
            variant="underlined"
            density="compact"
            v-model="taskItem.name"
          />
        </div>
        <div style="display: flex; justify-content: space-between">
          <div style="width: 100%">
            <v-card
              elevation="4"
              class="menu-component__block block_overflow"
              max-height="17rem"
            >
              <v-card-text>
                <v-card-title class="menu-component__block__title">
                  Описание
                </v-card-title>
                <v-card-text>
                  <v-textarea
                    required
                    :rules="rules.minLength.rules"
                    density="compact"
                    variant="underlined"
                    v-model="taskItem.description"
                  ></v-textarea>
                </v-card-text>
              </v-card-text>
            </v-card>
          </div>
          <div style="width: 100%; margin-left: 1rem">
            <v-card elevation="4" class="menu-component__block">
              <v-card-text style="display: grid">
                <div>
                  <div class="menu-component__block__title">Исполнитель</div>
                  <v-select
                    required
                    :rules="rules.required.rules"
                    clearable
                    clear-icon="mdi-close"
                    item-title="full_name"
                    item-key="id"
                    return-object
                    :items="users"
                    density="compact"
                    variant="underlined"
                    v-model="taskItem.performer"
                  ></v-select>
                </div>
                <div style="margin-top: 1rem">
                  <div class="menu-component__block__title">Автор</div>
                  <v-select
                    required
                    :rules="rules.required.rules"
                    clearable
                    clear-icon="mdi-close"
                    item-title="full_name"
                    item-key="id"
                    return-object
                    :items="users"
                    density="compact"
                    variant="underlined"
                    v-model="taskItem.author"
                  ></v-select>
                </div>
                <div style="margin-top: 1rem; position: relative">
                  <div class="menu-component__block__title">
                    Срок исполнения
                  </div>
                  <vue-date-picker
                    required
                    locale="ru"
                    v-model="taskItem.due_date"
                    format="dd.MM.yyyy"
                    model-type="yyyy-MM-dd"
                    mode="date"
                    select-text="Выбрать"
                    cancel-text="Отмена"
                    :enable-time-picker="false"
                  />
                </div>
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div style="margin-top: 1rem">
          <v-select
            clearable
            v-model="taskItem.tags"
            placeholder="Теги"
            density="comfortable"
            variant="underlined"
            chips
            multiple
            item-title="name"
            item-key="id"
            return-object
            :items="tags"
          ></v-select>
        </div>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<style scoped lang="scss">
:deep(.v-overlay__content) {
  top: 5rem !important;
  border-radius: 1.2rem !important;
}

.v-card {
  overflow: visible !important;
}

.menu-component {
  .v-input__details {
    display: none;
  }

  .block_overflow {
    overflow: hidden !important;
  }

  width: 800px;
  max-height: 800px;
  overflow: visible;

  &__block {
    margin-top: 1rem;
    border-radius: 2rem;

    &__title {
      font-weight: bold;
      font-size: 0.9rem;
    }
  }
}
</style>
