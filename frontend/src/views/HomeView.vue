<template>
  <div class="home-view">
    <h2 class="home-view__title">Мои задачи</h2>
    <MainTableComponent />
  </div>
</template>

<script>
import MainTableComponent from "@/components/HomeViewComponents/MainViewComponent.vue";

export default {
  name: "HomeView",
  components: { MainTableComponent },
};
</script>

<style lang="scss">
.home-view {
  &__title {
    font-weight: bold;
  }

  &__table {
    margin-top: 2rem;

    span.v-btn__content {
      text-transform: capitalize;
    }
    .v-data-table-header__content {
      font-weight: bold;
    }
    .v-input__details {
      display: none;
    }

    .v-icon {
      color: black;

      &:hover {
        background-color: lightgrey;
        border-radius: 0.4rem;
        cursor: pointer;
      }
    }
  }
}
</style>
