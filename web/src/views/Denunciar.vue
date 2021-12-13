<template>
  <div class="p-4">

    <form @submit.prevent="formSubmit" style="display:flex">
    <div style="padding-left:2%; padding-right:2%; height: 75vh; width: 70%;border-radius:10px;">
      
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
      <div style="width:30% ">
        <div class="card overflow-auto" style="height:75vh">
          <div class="card-header">
            <h3 class="text-center">Generar denuncia</h3>
          </div>
          <div class="card-body">  
            <div v-if="v$.markerLatLng.$error" style="color:red;">Seleccione un punto en el mapa</div>          
            <div class="text-center">
              <label for="titulo">Titulo</label>
              <br>
              <input
                id="titulo"
                v-model="titulo"
                type="text"
                name="titulo"
                maxlength="30"
                class="form-control text-center"
              >
              <div v-if="v$.titulo.$error" style="color:red;">Ingrese un titulo</div>
            </div>
            <div class="text-center">
              <label for="apellido_denunciante">Apellido</label>
              <br>
              <input
                id="apellido_denunciante"
                v-model="apellido_denunciante"
                type="text"
                name="apellido_denunciante"
                maxlength="30"
                class="form-control text-center"
              >
              <div v-if="v$.apellido_denunciante.$error" style="color:red;">Ingrese un apellido</div>
            </div>
            <div class="text-center">
              <label for="nombre_denunciante">Nombre</label>
              <br>
              <input
                id="nombre_denunciante"
                v-model="nombre_denunciante"
                type="text"
                name="nombre_denunciante"
                maxlength="30"
                class="form-control text-center"
              >
              <div v-if="v$.nombre_denunciante.$error" style="color:red;">Ingrese un nombre</div>
            </div>
            <div class="text-center">
              <label for="email_denunciante">Email</label>
              <br>
              <input
                id="email_denunciante"
                v-model="email_denunciante"
                type="email"
                name="email_denunciante"
                maxlength="30"
                class="form-control text-center"
                pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
              >
              <div v-if="v$.email_denunciante.$error" style="color:red;">Ingrese un email valido</div>
            </div>
            <div class="text-center">
              <label for="telcel_denunciante">Telefono</label>
              <br>
              <input
                id="telcel_denunciante"
                v-model="telcel_denunciante"
                type="number"
                name="telcel_denunciante"
                min="100000"
                class="form-control text-center"
              >
              <div v-if="v$.telcel_denunciante.$error" style="color:red;">Ingrese un telefono valido</div>
            </div>
            <p class="text-center">
              <label for="categoria_id">Categoria</label>
              <br>
              <select
                id="categoria_id"
                v-model="categoria_id"
                name="categoria_id"
                selected= "1"
                class="form-control text-center"
                required
              >
                <option value="1" >Cañeria Rota</option>
                <option value="2">Calle Inundable</option>
                <option value="3">Calle Rota</option>
                <option value="4">Otro</option>
              </select>
            </p>
            <p class="text-center">
              <label for="descripcion">Descripcion</label>
              <br>
              <textarea
                id="descripcion"
                v-model="descripcion"
                type="text"
                name="descripcion"
                class="form-control"
              ></textarea>
            </p>
            <div class="d-grid gap-2 d-md-flex justify-content-md-end">
              <button @click="submitForm" class="btn btn-success" style="width:100%">Enviar</button>
            </div>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script>
// import axios from 'axios'
import useValidate from '@vuelidate/core';
import {required, email, minLength} from '@vuelidate/validators';
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
  setup () {
    return{ v$: useValidate() }
  },
  data() {
      return {
          zoom: 13,
          lat: -34.9186, 
          lng: -57.956,
          markerLatLng: [],
          categoria_id:1,
          titulo:'',
          nombre_denunciante:'',
          apellido_denunciante:'',
          descripcion:'',
          telcel_denunciante:'',
          email_denunciante:'',
      } 
  },

  validations(){
    return{
        titulo: { required },
        markerLatLng: { required },
        categoria_id:{ required },
        nombre_denunciante:{ required },
        apellido_denunciante:{ required },
        telcel_denunciante:{ required, minLength: minLength(6) },
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
      async submitForm(){
        this.v$.$validate();
        if (!this.v$.$error){
          let coordenadas = this.markerLatLng.lat +','+ this.markerLatLng.lng;
          const datos = {categoria_id:this.categoria_id,
          coordenadas:coordenadas,
          apellido_denunciante:this.apellido_denunciante,
          nombre_denunciante:this.nombre_denunciante,
          telcel_denunciante:this.telcel_denunciante,
          email_denunciante:this.email_denunciante,
          titulo:this.titulo,
          descripcion:this.descripcion,
          };
          const requestOptions = {
            method: "POST",
            headers: {'Content-Type' : 'application/json'
            },
            body: JSON.stringify(datos)
          };
          await fetch(process.env.VUE_APP_ROOT_API+"/denuncias/", requestOptions)
            .then(response => response.json())
            .then(data => (this.postId = data.id))
            .catch(function (){
                alert("Ya existe denuncia con ese título");
            });
          }
      }  
    }
  }

  </script>
<style scoped>
div {
  text-align: left;
}
.map {
    border-radius: 10px;
}
</style>