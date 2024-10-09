<template>
  <v-app>
    <notifications style="margin-top: 1rem" :max="3" :pause-on-hover="true" />
    <v-icon
      icon="mdi-logout"
      size="24px"
      style="cursor: pointer; position: absolute; top: 1rem; right: 1rem"
      @click="logout"
    />
    <v-container fluid>
      <router-view />
    </v-container>
  </v-app>
</template>

<script>
import store from "@/store";
import router from "@/router";

export default {
  name: "App",
  methods: {
    async logout() {
      store.commit("logout");
      await router.push({ name: "AuthView" });
    },
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
