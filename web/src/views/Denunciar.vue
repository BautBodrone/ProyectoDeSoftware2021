<template>
  <div class="max-w-xl mx-auto px-4">
    <div class="rounded-lg shadow-lg p-4">

      <form>
        
  <p>
    <label for="titulo">Titulo</label>
    <input
      id="titulo"
      v-model="titulo"
      type="text"
      name="titulo"
      maxlength="30"
    >
  </p>
  <p>
    <label for="apellido_denunciante">Apellido</label>
    <input
      id="apellido_denunciante"
      v-model="apellido_denunciante"
      type="text"
      name="apellido_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="nombre_denunciante">Nombre</label>
    <input
      id="nombre_denunciante"
      v-model="nombre_denunciante"
      type="text"
      name="nombre_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="email_denunciante">Email</label>
    <input
      id="email_denunciante"
      v-model="email_denunciante"
      type="text"
      name="email_denunciante"
      maxlength="30"
    >
  </p>
 
  <p>
    <label for="telcel_denunciante">Telefono</label>
    <input
      id="telcel_denunciante"
      v-model="telcel_denunciante"
      type="number"
      name="telcel_denunciante"
      min="100000">
  </p>
 <p>
    <label for="descripcion">Descripcion</label>
    <textarea
      id="descripcion"
      v-model="descripcion"
      type="text"
      name="descripcion"
    ></textarea>
  </p>
  <p>
    <label for="categoria_id">Categoria</label>
    <select
      id="categoria_id"
      v-model="categoria_id"
      name="categoria_id"
      selected= "1"
    >
      <option value="1" >Cañeria Rota</option>
      <option value="2">Calle Inundable</option>
      <option value="3">Calle Rota</option>
      <option value="4">Otro</option>
    </select>
  </p>
  <button @click="submitForm">Enviar</button>

</form>
    </div>
  </div>


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
  
</template>
<script>
import useValidate from '@vuelidate/core';
import {required} from '@vuelidate/validators';
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
        descripcion:{ required },
        telcel_denunciante:{ required },
        email_denunciante:{ required }
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
      submitForm(){
        this.v$.$validate()
        if (!this.v$.$error){
          const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(`nombre_denunciante: ${this.nombre_denunciante},apellido_denunciante: ${this.apellido_denunciante},descripcion; ${this.descripcion},telcel_denunciante: ${this.telcel_denunciante}
          , email_denunciante: ${this.email_denunciante} ,categoria_id: ${this.categoria_id}, coordenadas:${this.markerLatLng.lat}, ${this.markerLatLng.lng}`)
          };
          fetch("https://admin-grupo33.proyecto2021.linti.unlp.edu.ar/api/denuncias", requestOptions)
            .then(response => response.json())
            .then(data => (this.postId = data.id));
          }
        else{
          alert("Complete todos los campos")
        }
      }  
  }
}

</script>
