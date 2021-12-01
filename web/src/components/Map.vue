<template>
<div style="float:right; height: 75vh; width: 80vw;">
    <l-map
    v-model="zoom"
    :zoom="13"
    :center="[-34.9186, -57.956]"
    >
    <l-tile-layer
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    ></l-tile-layer>
    <l-control-layers />
    </l-map>
</div>
</template>
<script>
import {
  LMap,
  LTileLayer,
  LControlLayers,
} 
from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
export default ({
    name: 'Map',
    components:{
        LMap,
        LTileLayer,
        LControlLayers,
    },
    data() {
        return {
        zoom: 2,
        iconWidth: 25,
        iconHeight: 40,
        };
    },
    computed: {
        iconUrl() {
        return `https://placekitten.com/${this.iconWidth}/${this.iconHeight}`;
        },
        iconSize() {
        return [this.iconWidth, this.iconHeight];
        },
    },
    methods: {
        log(a) {
        console.log(a);
        },
        changeIcon() {
        this.iconWidth += 2;
        if (this.iconWidth > this.iconHeight) {
            this.iconWidth = Math.floor(this.iconHeight / 2);
        }
        },
    },
});
</script>

