<script>
import { requests } from "@/requests";

export default {
  name: "AuthSignUpComponent",
  props: ["tab", "rules"],
  emits: ["update:tab"],
  data() {
    return {
      loading: false,
      form: false,
      username: "",
      fullName: "",
      password: "",
      confirmPassword: "",
      showPassword: false,

      confirmPasswordRules: [
        (v) => !!v || "Обязательное поле",
        (v) => v.length >= 8 || "Минимальное количество символов - 8",
        (v) => v === this.password || "Пароли не совпадают",
      ],
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
        await requests.post("/api/auth/sign-up/", {
          username: this.username,
          password: this.password,
          full_name: this.fullName,
        });
        this.$notify({
          text: "Вы успешно зарегистрировались. Пожалуйста, авторизуйтесь",
        });
        this.$emit("update:tab", 0);
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
  <v-card-text>
    <v-form v-model="form" @submit.prevent="onSubmit" @keydown.enter="onSubmit">
      <div>
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
          prepend-icon="none"
          density="comfortable"
          variant="outlined"
          v-model="fullName"
          label="Фамилия Имя Отчество"
          type="text"
          required
          :rules="rules.fullNameRules"
        />
      </div>
      <div style="margin-top: 1rem">
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
        <v-text-field
          prepend-icon="mdi-lock"
          :append-inner-icon="showPassword ? 'mdi-eye-off-outline' : 'mdi-eye'"
          @click:append-inner="showPassword = !showPassword"
          density="comfortable"
          variant="outlined"
          v-model="confirmPassword"
          label="Повторите пароль"
          :type="showPassword ? 'text' : 'password'"
          required
          :rules="confirmPasswordRules"
        />
      </div>
    </v-form>
  </v-card-text>

  <v-card-actions>
    <v-spacer />
    <v-btn
      color="primary"
      :loading="loading"
      :disabled="!form"
      @click="onSubmit"
    >
      Зарегистрироваться
    </v-btn>
  </v-card-actions>
</template>

<style scoped lang="scss"></style>
