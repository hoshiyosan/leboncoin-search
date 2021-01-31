<template>
  <article v-if="anounce" @click="onClick()">
    <h2>{{ anounce.title }}</h2>
    <strong>Prix: {{ anounce.price }} €</strong>
    <p>{{ anounce.description | maxLength(300) }}</p>
  </article>
</template>

<script>
export default {
  filters: {
    maxLength: function (text, length) {
      if (!text) return "";
      return text.substring(0, length) + "...";
    },
  },
  props: {
    anounce: { type: Object },
  },
  methods: {
    onClick() {
      this.$emit("click");
    },
  },
};
</script>