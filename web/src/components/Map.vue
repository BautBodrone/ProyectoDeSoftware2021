<template>
<div style="float:right; height: 75vh; width: 80vw;margin-top:1rem;border-radius:10px;">
    <l-map class="map"
    v-model="zoom"
    :zoom="zoom"
    :center="[-34.9186, -57.956]"
    >
    <div v-for="recorrido in recorridos" :key="recorrido">
        <l-polyline :lat-lngs="[recorrido.coordenadas]" :name="recorrido.nombre" :color="recorrido.color">
            <l-popup>{{recorrdio.nombre}}</l-popup>
        </l-polyline>
    </div>
    <div v-for="zona in zonas" v-bind:key="zona">
        <l-polygon :lat-lngs="[zona.coordenadas]" :name="zona.nombre" :color="zona.color" :fill="true" :fill-color="zona.color" :fillOpacity="0.2">
            <l-popup>{{zona.nombre}}</l-popup>
        </l-polygon>
    </div>
    <div v-for="punto in puntos" :key="punto">
        <l-marker :lat-lng="[punto.lat,punto.lng]" :name="punto.nombre">
            <l-popup>{{punto.nombre}}</l-popup>
        </l-marker>
    </div>
    <l-tile-layer
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    ></l-tile-layer>
    </l-map>
</div>
</template>
<script>
import {
  LMap,
  LTileLayer,
  LPolygon,
  LPolyline,
  LMarker,
  LPopup
}
from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
export default ({
    name: 'Map',
    components:{
        LMap,
        LTileLayer,
        LPolygon,
        LPolyline,
        LMarker,
        LPopup
    },
    data() {
        return {
            zoom: 13,
        };
    },
    props: {
        zonas: [],
        puntos: [],
        recorridos: []
    },
});
</script>
<style scoped>
.map {
    border-radius: 10px;
}
</style>

