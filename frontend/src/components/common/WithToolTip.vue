<script>
export default {
  name: "WithTooltip",
  props: {
    text: {
      type: String,
      default: "",
    },
    customClass: {
      type: String,
      default: "d-inline-block",
    },
    customStyle: {
      type: String,
      default: "",
    },
    location: {
      type: String,
      default: "top",
      validator(value) {
        return ["top", "bottom", "start", "end"].includes(value);
      },
    },
  },
};
</script>

<template>
  <v-tooltip :location="location">
    <template v-slot:activator="{ props }">
      <div v-bind="props" :class="customClass" :style="customStyle">
        <slot></slot>
      </div>
    </template>
    <span>{{ text }}</span>
  </v-tooltip>
</template>

<style scoped lang="scss"></style>
