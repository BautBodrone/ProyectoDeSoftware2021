<template>
<div style="float:right; height: 75vh; width: 80vw;margin-top:1rem;border-radius:10px;">
    <l-map class="map"
    v-model="zoom"
    :zoom="zoom"
    :center="[-34.9186, -57.956]"
    >
    <div v-for="recorrido in recorridos" :key="recorrido">
        <l-polyline :lat-lngs="[recorrido.coordenadas]" :name="recorrido.nombre" :color="recorrido.color"/>
    </div>
    <div v-for="zona in zonas" :key="zona">
        <l-polygon :lat-lngs="[zona.coordenadas]" :name="zona.nombre" :color="zona.color" :fill="true" :fill-color="zona.color" :fillOpacity="0.5"/>
    </div>
    <div v-for="punto in puntos" :key="punto">
        <l-marker :lat-lng="[punto.lat,punto.lng]" :name="punto.nombre"/>
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
  LMarker
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
        LMarker
    },
    data() {
        return {
            zoom: 13,
            zonas: [],
            puntos: [],
            recorridos: []
        };
    },
    created() {
        fetch('http://localhost:5000/api/zonas-inundables/').then((response) => {
            return response.json();
        }).then((json) => {
            this.zonas = json.zonas;
        }).catch((e) => {
            console.log(e)
        }),
        fetch('http://localhost:5000/api/puntos-encuentro/').then((response) => {
            return response.json();
        }).then((json) => {
            this.puntos = json.puntos_encuentro;
        }).catch((e) => {
            console.log(e)
        }),
        fetch('http://localhost:5000/api/recorridos-evacuacion/').then((response) => {
            return response.json();
        }).then((json) => {
            this.recorridos = json.recorridos;
        }).catch((e) => {
            console.log(e)
        })
    }
});
</script>
<style scoped>
.map {
    border-radius: 10px;
}
</style>

