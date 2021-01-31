<template>
  <article v-if="anounce">
    <header>
      <h2>{{ anounce.title }}</h2>
      <v-simple-table style="margin: 16px 8px">
        <tr>
          <td>Prix</td>
          <td>{{ anounce.price }} €</td>
        </tr>
        <tr v-for="(value, attribute) in anounce.apartment" :key="attribute">
          <td>{{ attribute }}</td>
          <td>{{ value }}</td>
        </tr>
      </v-simple-table>
      <p>{{ anounce.description }}</p>
    </header>

    <Caroussel :images="anounce.images" />

    <footer>
      <v-btn
        title="Ajouter aux favoris"
        class="mx-2"
        fab
        dark
        small
        color="pink"
        @click="setAsFavorite()"
      >
        <v-icon dark> mdi-heart </v-icon>
      </v-btn>
      <v-btn
        title="Pas intéressé"
        class="mx-2"
        fab
        dark
        small
        color="red"
        @click="setAsBlacklisted()"
      >
        <v-icon dark> mdi-delete</v-icon>
      </v-btn>
      <v-btn title="Voir l'annonce" class="mx-2" fab dark small color="indigo">
        <a
          :href="anounce.anounce_url"
          target="blank"
          style="text-decoration: none; color: inherit"
        >
          <v-icon dark> mdi-link-variant </v-icon>
        </a>
      </v-btn>
    </footer>
  </article>
</template>

<script>
import Caroussel from "@/components/Caroussel";

export default {
  components: { Caroussel },
  props: {
    anounce: { type: Object },
  },
  methods: {
    setAsFavorite() {
      this.$store
        .dispatch("anounce/favoriteAnounce", this.anounce.uid)
        .then(() => this.$emit("anounceFavorited"));
    },
    setAsBlacklisted() {
      this.$store
        .dispatch("anounce/blacklistAnounce", this.anounce.uid)
        .then(() => this.$emit("anounceBlacklisted"));
    },
  },
};
</script>

<style scoped>
footer {
  margin-top: 16px;
}
article {
  margin-bottom: 10vh;
}
</style>