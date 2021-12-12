<template>
<div class="container col-md-8 col-sm-12" >
      <b-card-group deck>
        <b-card
          bg-variant="ligth"
          header="Crear Turno"
          class="text-center"
          header-tag="header"
          header-bg-variant="primary"
          header-text-variant="white"
          style="max-width: 50rem;"
          align="center"
        >
      <form form v-on:submit.prevent="onSubmit">
      <div style="padding-left:2%; padding-right:2%; height: 45vh; width: 100%; margin-top:1rem;border-radius:10px;">
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
      
      <p
  v-for="error of v$.$errors"
  :key="error.$uid"
>
<strong>{{ error.$property }}</strong>
<small>  </small>
<strong>{{ error.$message }}</strong>
</p>       
  <p>
    <label for="form.titulo">Titulo</label>
    <input
      v-model="form.titulo"
      type="text"
      name="titulo"
      maxlength="30"
    >
  </p>
  <p>
    <label for="form.apellido_denunciante">Apellido</label>
    <input
      v-model="form.apellido_denunciante"
      type="text"
      name="apellido_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="form.nombre_denunciante">Nombre</label>
    <input
      v-model="form.nombre_denunciante"
      type="text"
      name="nombre_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="form.email_denunciante">Email</label>
    <input
      v-model="form.email_denunciante"
      type="text"
      name="email_denunciante"
      maxlength="30"
    >
  </p>
 
  <p>
    <label for="form.telcel_denunciante">Telefono</label>
    <input
      v-model="form.telcel_denunciante"
      type="number"
      name="telcel_denunciante"
      min="100000">
  </p>
 <p>
    <label for="form.descripcion">Descripcion</label>
    <textarea
      v-model="form.descripcion"
      type="text"
      name="descripcion"
    ></textarea>
  </p>
  <p>
    <label for="form.categoria_id">Categoria</label>
    <select
      v-model="form.categoria_id"
      name="categoria_id"
      selected= "1"
    >
      <option value="1" >Cañeria Rota</option>
      <option value="2">Calle Inundable</option>
      <option value="3">Calle Rota</option>
      <option value="4">Otro</option>
    </select>
  </p>
  <input class="button" type="submit" value="Submit">
  </form>
  </b-card>
  </b-card-group>
    </div>



  
</template>
<script>
// import axios from 'axios'
import useValidate from '@vuelidate/core';
import {required, email} from '@vuelidate/validators';
import {
  LMap,
  LTileLayer,
  LMarker,
}from "@vue-leaflet/vue-leaflet";import "leaflet/dist/leaflet.css";

export default {
  name: 'DynamicForm',
  components: {
    LMap,
    LTileLayer,
    LMarker,
 
  },

  props: {
    schema: {
      type: Object,
      required: true,
    },
  },

  data() {
      return {
        form:{
          titulo:'',
          coordenadas:'',
          apellido_denunciante:'',
          nombre_denunciante:'',
          email_denunciante:'',
          telcel_denunciante:'',
          descripcion:'',
          categoria_id:'1',
        },
          v$: useValidate(),
          zoom: 13,
          lat: -34.9186, 
          lng: -57.956,
          markerLatLng: [],
          categoria_id:1,
      } 
  },

  validations(){
    return{
        markerLatLng: { required },
        categoria_id:{ required },
        nombre_denunciante:{ required },
        apellido_denunciante:{ required },
        telcel_denunciante:{ required },
        email_denunciante:{ required, email }
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
      },
      onSubmit(){
        const axios = require('axios');
        this.v$.$validate()

            axios.post('https://127.0.0.1:5000/api/denuncias',{
                "categoria_id": 1,
                "coordenadas": "41.40338,2.17403",
                "apellido_denunciante": "Fulanasdito",
                "nombre_denunciante": "Cosasdme",
                "telcel_denunciante": "221-8436754",
                "email_denunciante": "juan.perez@gmasdail.com",
              })
              .then((response) => {
                console.log(response);
              }, (error) => {
                console.log(error);
              });
      }  
    }
  }

  </script>
<style scoped>
div {
  text-align: center;
}
</style>