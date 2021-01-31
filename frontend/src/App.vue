<template>
  <v-app id="app">
    <v-tabs class="tabs" centered grow height="60px">
      <v-tab v-for="tab in tabs" :key="tab.id" :to="tab.route" exact>
        {{ tab.name }}
      </v-tab>
    </v-tabs>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      tabs: [
        { id: 0, route: "/locations", name: "Locations" },
        { id: 1, route: "/anounces", name: "Annonces" },
        { id: 2, route: "/favorites", name: "Favoris" },
      ],
    };
  },
};
</script>