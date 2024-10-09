<template>
  <v-menu v-model="isOpened" :close-on-content-click="false" location="top">
    <template v-slot:activator="{ props }">
      <div v-bind="props"></div>
    </template>
    <v-card
      min-width="300"
      class="menuCard"
      max-width="400px"
      :style="customStyle"
    >
      <v-card-text>
        <div class="text-center mt-2 fs-5 fw-bold">{{ title }}</div>

        <v-divider></v-divider>

        <div v-if="requireComment">
          <v-textarea
            v-if="multiLineComment"
            variant="outlined"
            density="compact"
            :placeholder="textPlaceholder"
            v-model="comment"
          ></v-textarea>
          <v-text-field
            v-else
            variant="outlined"
            density="compact"
            :placeholder="textPlaceholder"
            v-model="comment"
          ></v-text-field>
        </div>

        <div class="d-flex">
          <v-btn
            color="black"
            variant="tonal"
            :text="cancelButtonText"
            @click="confirm(false)"
          />
          <v-spacer />
          <v-btn
            color="primary"
            variant="flat"
            :text="confirmButtonText"
            @click="confirm(true)"
          />
        </div>
      </v-card-text>
    </v-card>
  </v-menu>
</template>

<script>
export default {
  name: "ConfirmMenuModal",
  props: {
    open: {
      type: Boolean,
      required: true,
    },
    title: {
      type: String,
      default: "Вы подтверждаете действие?",
    },
    confirmButtonText: {
      type: String,
      default: "Подтвердить",
    },
    cancelButtonText: {
      type: String,
      default: "Отмена",
    },
    requireComment: {
      type: Boolean,
      default: false,
    },
    textPlaceholder: {
      type: String,
      default: "Введите комментарий",
    },
    multiLineComment: {
      type: Boolean,
      default: false,
    },
    commentLength: {
      type: Number,
      default: 5,
    },
    customStyle: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      comment: "",
    };
  },
  computed: {
    isOpened: {
      get() {
        return this.open;
      },
      set(value) {
        this.$emit("update:open", value);
      },
    },
  },
  methods: {
    async confirm(value) {
      if (!value) {
        this.requireComment
          ? this.$emit("confirm", false, "")
          : this.$emit("confirm", false);
        this.isOpened = false;
        return;
      }
      if (this.requireComment && this.comment.length < this.commentLength) {
        alert(
          `Длина комментария должна быть не менее ${this.commentLength} символов`
        );
        return;
      }
      this.requireComment
        ? this.$emit("confirm", true, this.comment)
        : this.$emit("confirm", true);
      this.isOpened = false;
    },
  },
};
</script>

<style scoped lang="scss">
.menuCard {
  border: none;
  border-radius: 0.8rem !important;
}
</style>
