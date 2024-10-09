import axios from "axios";
import router from "@/router";
import { notify } from "@kyvg/vue3-notification";
import store from "@/store";

const httpOkStatuses = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226];

export const requests = axios.create();

requests.interceptors.request.use(async (request) => {
  request.headers["Authorization"] = "Bearer " + localStorage.getItem("token");
  request.headers["Content-Type"] = "application/json";
  request.headers["Accept"] = "application/json";
  return request;
});

requests.interceptors.response.use(
  async (response) => response,
  async (error) => {
    if (!httpOkStatuses.includes(error.request.status)) {
      if (error.request.status === 401) {
        localStorage.removeItem("token");
        store.commit("setUserInfo", null);
        await router.push({ name: "AuthView" });
      }
      if (error.response.data?.detail)
        notify({
          text: error.response.data.detail,
          type: "error",
        });
      else
        notify({
          text: "Произошла ошибка",
          type: "error",
        });
    }
    return Promise.reject(error);
  }
);
