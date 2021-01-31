<template>
  <v-carousel v-model="model">
    <v-carousel-item v-for="(image, index) in images" :key="index">
      <img :src="image" alt="" />
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      model: 0,
    };
  },
  props: {
    images: { type: Array, default: null },
  },
};
</script>