import { createStore } from "vuex";
import { requests } from "@/requests";

export default createStore({
  state: {
    userInfo: null,
    users: [],
    tags: [],
  },
  getters: {
    userInfo(state) {
      return state.userInfo;
    },
    users(state) {
      return state.users;
    },
    tags(state) {
      return state.tags;
    },
    isAuthenticated(state) {
      return (
        (state.userInfo && state.userInfo?.token) ||
        localStorage.getItem("token") !== null
      );
    },
  },
  mutations: {
    setUserInfo(state, value) {
      state.userInfo = value;
    },
    setStatuses(state, value) {
      state.statuses = value;
    },
    setUsers(state, users) {
      state.users = users;
    },
    setTags(state, value) {
      state.tags = value;
    },
    logout(state) {
      localStorage.removeItem("token");
      state.userInfo = null;
    },
  },
  actions: {
    async getInfo({ commit }) {
      try {
        const response = await requests.get("api/tasks/info/");
        commit("setUsers", response.data.users);
        commit("setTags", response.data.tags);
        // eslint-disable-next-line no-empty
      } catch (error) {}
    },
    async getProfile({ commit }) {
      try {
        const response = await requests.get("api/profile/");
        commit("setUserInfo", response.data);
        // eslint-disable-next-line no-empty
      } catch (error) {}
    },
  },
  modules: {},
});
