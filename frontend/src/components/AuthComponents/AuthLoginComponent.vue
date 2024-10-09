<script>
import { requests } from "@/requests";
import router from "@/router";
import store from "@/store";

export default {
  name: "AuthLoginComponent",
  props: ["isValid", "rules"],
  emits: ["update:isValid"],
  data() {
    return {
      loading: false,
      form: false,
      username: "",
      password: "",
      showPassword: false,
    };
  },
  methods: {
    async onSubmit() {
      if (!this.form) {
        this.$notify({
          text: "Заполните все необходимые поля",
          type: "error",
        });
        return;
      }
      this.loading = true;
      try {
        const response = await requests.post("/api/auth/", {
          username: this.username,
          password: this.password,
          full_name: null,
        });
        localStorage.setItem("token", response.data.token);
        store.commit("setUserInfo", response.data);
        await router.push({ name: "HomeView" });
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
  <v-card-text class="auth-card__credentials">
    <v-form v-model="form" @submit.prevent="onSubmit" @keydown.enter="onSubmit">
      <v-text-field
        prepend-icon="mdi-account"
        density="comfortable"
        variant="outlined"
        v-model="username"
        label="Имя пользователя"
        type="text"
        required
        :rules="rules.usernameRules"
      />
      <v-text-field
        prepend-icon="mdi-lock"
        :append-inner-icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye'"
        @click:append-inner="showPassword = !showPassword"
        density="comfortable"
        variant="outlined"
        v-model="password"
        label="Пароль"
        :type="showPassword ? 'text' : 'password'"
        required
        :rules="rules.passwordRules"
      />
    </v-form>
  </v-card-text>

  <v-card-actions>
    <v-spacer />
    <v-btn
      color="primary"
      :loading="loading"
      :disabled="!form"
      @click="onSubmit"
      >Войти</v-btn
    >
  </v-card-actions>
</template>

<style scoped lang="scss"></style>
