<template>
  <div class="p-4">
    <div class="puntos" style="display:flex">
      <Map v-bind:puntos="puntos" v-bind:recorridos="recorridos"/>
      <div style="display:block; width:30%; height:70vh">
      <div class="card overflow-auto" style="height:40vh; ">
        <div v-if="puntos">
          <div class="card-header">
            <h3>Puntos</h3>
          </div>
          <div class="card-body">
            <div v-for="row in puntos_all" v-bind:key="row" style="margin-bottom:2%">
              <vue-collapsible-panel :expanded="false" @click="showPunto(row)" @leave="showAll()">
                <template #title>
                    {{row.nombre}}
                </template>
                <template #content>
                    {{row.direccion}}<br>
                    {{row.telefono}}
                </template>
              </vue-collapsible-panel>
            </div>
          </div>
        </div>
      </div>
      <div class="card overflow-auto" style="height:35vh;">
      <div v-if="recorridos">
        <div class="card-header">
          <h3>Recorridos</h3>
        </div>
        <div class="card-body">
          <div v-for="row in recorridos_all" v-bind:key="row" style="margin-bottom:2%">
            <vue-collapsible-panel :expanded="false" @click="showRecorrido(row)" @leave="showAll()">
                <template #title>
                    {{row.nombre}}
                </template>
                <template #content>
                    <label>{{row.nombre}}</label>
                    <label>{{row.descripcion}}</label>
                </template>
            </vue-collapsible-panel>
          </div>
        </div>
      </div>
      </div>
    </div>
    </div>
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
import {
  VueCollapsiblePanel,
} from '@dafcoe/vue-collapsible-panel'
import '@dafcoe/vue-collapsible-panel/dist/vue-collapsible-panel.css'
export default {
  name: 'Puntos',
  components:{
    Map,
    VueCollapsiblePanel,
  },
  data() {
    return {
      puntos_all : [],
      puntos : [],
      recorridos_all : [],
      recorridos : [],
    };
  },
  props: {
    rows_per_page : Number
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/').then((response) => {
        return response.json();
    }).then((json) => {
        this.puntos = json.puntos_encuentro;
        this.puntos_all = this.puntos;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/recorridos-evacuacion').then((response) => {
        return response.json();
    }).then((json) => {
        this.recorridos = json.recorridos;
        this.recorridos_all = this.recorridos;
    }).catch((e) => {
        console.log(e)
    })
  },
  methods:{
    showPunto(row){
      this.recorridos = [];
      this.puntos = [row];
    },
    showRecorrido(row){
      this.recorridos = [row];
      this.puntos = [];
    },
    showAll(){
      this.recorridos = this.recorridos_all;
      this.puntos = this.puntos_all;
    },
  }
};
</script>
<style scoped>
.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
</style>