import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import store from "@/store";

const routes = [
  {
    path: "/",
    name: "HomeView",
    component: HomeView,
    meta: {
      title: "Главная страница",
    },
  },
  {
    path: "/auth",
    name: "AuthView",
    component: () => import("@/views/AuthView.vue"),
    meta: {
      title: "Авторизация",
    },
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const user = await store.getters.userInfo;

  if (user === null && store.getters.isAuthenticated) {
    await store.dispatch("getProfile");
  }
  if (
    store.getters.isAuthenticated &&
    (!store.getters.users.length || !store.getters.tags.length)
  ) {
    await store.dispatch("getInfo");
  }

  if (!store.getters.isAuthenticated) {
    if (to.name === "AuthView") await next();
    else return next({ name: "AuthView" });
  } else {
    if (to.name === "AuthView") return next({ name: "HomeView" });
    if (to.path.includes("/admin/") && user?.is_admin !== true) {
      return next({ name: "HomeView" });
    }
    return next();
  }
});
export default router;
