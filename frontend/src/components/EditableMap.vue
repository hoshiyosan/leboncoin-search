<template>
  <main>
    <header>
      <v-text-field label="Nom de la zone"></v-text-field>

      <nav style="display: flex; padding-bottom: 3em">
        <input
          type="search"
          id="address-input"
          placeholder="Centrer la zone sur..."
          style="flex: 1"
        />

        <v-btn title="Recentrer">
          <v-icon>mdi-bullseye</v-icon>
        </v-btn>

        <v-btn title="Définir la zone">
          <v-icon>mdi-shape-polygon-plus</v-icon>
        </v-btn>
      </nav>
    </header>
    <div id="map"></div>
  </main>
</template>

<script>
import L from "leaflet";

export default {
  data() {
    return { map: null, drawingPolygonCoordinates: null, drawingPolygon: null };
  },
  mounted() {
    const places = require("places.js");
    const placesAutocomplete = places({
      appId: "plA5TDLIYZL5",
      apiKey: "b1a9be5716a64df9b56eae5021517f3e",
      container: document.querySelector("#address-input"),
    });

    placesAutocomplete.on("change", (event) => this.onPlaceSearch(event));

    this.map = L.map("map").setView([48.1182023, -1.6633924], 12);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    this.map.on("click", (event) => this.onClick(event));
    this.map.on("mousemove", (event) => this.onMouseMove(event));
  },
  methods: {
    onClick(event) {
      const clickedCoordinates = [event.latlng.lat, event.latlng.lng];
      if (!this.drawingPolygonCoordinates) {
        this.drawingPolygonCoordinates = [clickedCoordinates];
      } else {
        this.drawingPolygonCoordinates.push(clickedCoordinates);
      }
      if (this.drawingPolygonCoordinates.includes(clickedCoordinates));
      console.log("coordinates", this.drawingPolygonCoordinates);
    },
    onMouseMove(event) {
      const currentCoordinates = [event.latlng.lat, event.latlng.lng];
      if (this.drawingPolygon) {
        this.map.removeLayer(this.drawingPolygon);
      }
      if (this.drawingPolygonCoordinates) {
        const drawingPolygonTemporaryCoordinates = [
          ...this.drawingPolygonCoordinates,
          currentCoordinates,
        ];
        this.drawingPolygon = new L.Polygon(drawingPolygonTemporaryCoordinates);
        this.map.addLayer(this.drawingPolygon);
      }
      console.log("mouse move", event.latlng, currentCoordinates);
    },
    onPlaceSearch(event) {
      const centerCoordinates = [
        event.suggestion.latlng.lat,
        event.suggestion.latlng.lng,
      ];
      console.log("search place", event.suggestion);
      this.map.setView(centerCoordinates, 12);
    },
  },
};
</script>

<style scoped>
main {
  width: 800px;
  height: 500px;
}

#map {
  width: 100%;
  height: 400px;
}
</style>