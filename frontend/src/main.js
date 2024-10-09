import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "vuetify/styles";
import { createVuetify } from "vuetify";

import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import * as labsComponents from "vuetify/labs/components";

import "@mdi/font/css/materialdesignicons.css";
import Notifications from "@kyvg/vue3-notification";
import moment from "moment";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

const vuetify = createVuetify({
  components: {
    ...components,
    ...labsComponents,
  },
  directives,
});

moment.locale("ru");

const app = createApp(App);

app
  .component("VueDatePicker", VueDatePicker)
  .use(vuetify)
  .use(store)
  .use(router)
  .use(Notifications)
  .mount("#app");
