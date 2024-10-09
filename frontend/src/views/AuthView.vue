<template>
  <div class="auth-card">
    <v-card width="450px">
      <v-tabs
        class="auth-card__tabs"
        v-model="tab"
        bg-color="white"
        color="primary"
      >
        <v-tab value="auth">Авторизация</v-tab>
        <v-tab value="sign-up">Регистрация</v-tab>
      </v-tabs>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="auth">
          <AuthLoginComponent :rules="rules" />
        </v-tabs-window-item>
        <v-tabs-window-item value="sign-up">
          <AuthSignUpComponent :rules="rules" :tab="tab" />
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card>
  </div>
</template>

<script>
import AuthLoginComponent from "@/components/AuthComponents/AuthLoginComponent.vue";
import AuthSignUpComponent from "@/components/AuthComponents/AuthSignUpComponent.vue";

export default {
  name: "AuthView",
  components: { AuthSignUpComponent, AuthLoginComponent },
  data() {
    return {
      tab: 0,
      isValid: {
        login: false,
        signUp: false,
      },
      rules: {
        usernameRules: [
          (v) => !!v || "Обязательное поле",
          (v) => v.length >= 5 || "Минимальное количество символов - 5",
        ],
        passwordRules: [
          (v) => !!v || "Обязательное поле",
          (v) => v.length >= 8 || "Минимальное количество символов - 8",
        ],
        fullNameRules: [
          (v) => !!v || "Обязательное поле",
          (v) => v.length >= 10 || "Минимальное количество символов - 10",
        ],
      },
    };
  },
};
</script>

<style lang="scss">
.auth-card {
  position: absolute;
  top: 25%;
  left: 35%;

  &__tabs {
    .v-tab {
      font-weight: bold;
    }
  }

  &__credentials {
    padding-top: 2rem;
  }

  .v-btn {
    font-weight: bold;
  }
}
</style>
