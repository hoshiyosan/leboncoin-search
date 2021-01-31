<template>
  <v-container>
    <main>
      <aside>
        <AnounceSummary
          v-for="(anounce, index) in anouncesInbox"
          :key="anounce.uid"
          :anounce="anounce"
          class="clickable"
          :class="{ active: anounce === selectedAnounce }"
          @click="selectAnounce(index)"
        />
      </aside>
      <aside v-if="selectedAnounce">
        <Anounce
          :anounce="selectedAnounce"
          @anounceBlacklisted="nextAnounce()"
          @anounceFavorited="nextAnounce()"
        />
      </aside>
    </main>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import AnounceSummary from "@/components/AnounceSummary";
import Anounce from "@/components/Anounce";

export default {
  components: { AnounceSummary, Anounce },
  data() {
    return { selectedAnounceIndex: 0 };
  },
  mounted() {
    this.updateAnounces();
  },
  computed: {
    selectedAnounce() {
      return this.anouncesInbox[this.selectedAnounceIndex];
    },
    ...mapGetters("anounce", ["anouncesInbox"]),
  },
  methods: {
    selectAnounce(index) {
      this.selectedAnounceIndex = index;
    },
    ...mapActions("anounce", ["updateAnounces"]),
  },
};
</script>

<style scoped>
main {
  display: flex;
  height: 90vh;
}
aside {
  flex: 1;
  max-height: 100%;
  overflow-y: auto;
}

.active,
.clickable:hover {
  cursor: pointer;
  background: rgba(0, 0, 0, 0.08);
}
</style>