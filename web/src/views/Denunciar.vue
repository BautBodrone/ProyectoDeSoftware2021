<template>
    <Form>
      <div style="padding-left:2%; padding-right:2%; height: 75vh; width: 100%; margin-top:1rem;border-radius:10px;">
        <l-map class="map"
        v-model="zoom"
        :zoom="zoom"
        :center="[lat,lng]"
        @click="onClick"
        >
        <div v-if="this.markerLatLng.lat!=undefined">
            <l-marker :lat-lng="[markerLatLng.lat,markerLatLng.lng]"/>
        </div>
        <l-tile-layer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        </l-map>
      </div>
      <div class="denuncias">
    </div>
      <!--
    <div
      v-for="{ as, name, label, children, ...attrs } in schema.fields"
      :key="name"
    >
      <label :for="name">{{ label }}</label>
      <Field :as="as" :id="name" :name="name" v-bind="attrs">
        <template v-if="children && children.length">
          <component v-for="({ tag, text, ...childAttrs }, idx) in children"
            :key="idx"
            :is="tag"
            v-bind="childAttrs"
          >
            {{ text }}
          </component>
        </template>
      </Field>
      <ErrorMessage :name="name" />
    </div>
    <button>Submit</button>
    -->
  </Form>
</template>
<script>
import {
  LMap,
  LTileLayer,
  LMarker,
}
from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import { Form,// Field, ErrorMessage 
} from 'vee-validate';
export default {
  name: 'DynamicForm',
  components: {
    LMap,
    LTileLayer,
    LMarker,
    Form,
    //Field,
    //ErrorMessage
  },
  props: {
    schema: {
      type: Object,
      required: true,
    },
  },
  data() {
      return {
          zoom: 13,
          lat: -34.9186, 
          lng: -57.956,
          markerLatLng: [],
      };
  },
  created() {
      if("geolocation" in navigator) {
          navigator.geolocation.getCurrentPosition(pos => {
              this.lat = pos.coords.latitude;
              this.lng = pos.coords.longitude;
          },
      )
      return;
      }
      this.$getLocation()
      .then(coordinates => {
          console.log(coordinates);
      });
  },
  methods: {
      onClick(e) { 
          if(e.latlng) {
              this.markerLatLng = e.latlng;
          }
      }  
  }
};
</script>
