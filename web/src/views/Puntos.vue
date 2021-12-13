<template>
  <div class="p-4">
    <div class="puntos" style="display:flex">
      <Map v-bind:puntos="puntos_mapa" v-bind:recorridos="recorridos_mapa"/>
      <div style="display:block; width:30%; height:70vh">
        <button @click="showAll()" class="btn btn-secondary" style="width:100%">Mostrar todo</button>
      <div class="card overflow-auto" style="height:36vh; ">
        <div v-if="puntos_all">
          <div class="card-header">
            <h5>Puntos</h5>
          </div>
          <div class="card-body">
            <div v-for="row in puntos_list" v-bind:key="row" style="margin-bottom:2%">
              <vue-collapsible-panel :expanded="false" @click="showPunto(row)">
                <template #title>
                    {{row.nombre}}
                </template>
                <template #content>
                    {{row.direccion}}<br>
                    {{row.telefono}}
                </template>
              </vue-collapsible-panel>
            </div>
            <Pagination v-model="page_puntos" :records="cant_puntos" :per-page="rows_per_page" @paginate="newItemsPuntos" :options="options"/>
          </div>
        </div>
      </div>
      <div class="card overflow-auto" style="height:35vh;">
      <div v-if="recorridos_all">
        <div class="card-header">
          <h5>Recorridos</h5>
        </div>
        <div class="card-body">
          <div v-for="row in recorridos_list" v-bind:key="row" style="margin-bottom:2%">
            <vue-collapsible-panel :expanded="false" @click="showRecorrido(row)">
                <template #title>
                    {{row.nombre}}
                </template>
                <template #content>
                    <label>{{row.descripcion}}</label>
                </template>
            </vue-collapsible-panel>
          </div>
          <Pagination v-model="page_recorridos" :records="cant_recorridos" :per-page="rows_per_page" @paginate="newItemsRecorridos" :options="options"/>
        </div>
      </div>
      </div>
      </div>
    </div>
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
import Pagination from 'v-pagination-3';
import {
  VueCollapsiblePanel,
} from '@dafcoe/vue-collapsible-panel'
import '@dafcoe/vue-collapsible-panel/dist/vue-collapsible-panel.css'
export default {
  name: 'Puntos',
  components:{
    Map,
    VueCollapsiblePanel,
    Pagination
  },
  data() {
    return {
      puntos_all : [],
      puntos_list : [],
      puntos_mapa : [],
      recorridos_all : [],
      recorridos_mapa : [],
      recorridos_list : [],
      cant_puntos : '',
      cant_recorridos : '',
      rows_per_page: '',
      page_puntos : 1,
      page_recorridos : 1,
      options : {
        chunk:5,
        edgeNavigation:true,
        chunksNavigation:"scroll",
        hideCount:true,
        texts:{
          first:"<<",
          last:">>"
        }
      }
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/').then((response) => {
        return response.json();
    }).then((json) => {
        this.puntos_mapa = json.puntos_encuentro;
        this.puntos_all = this.puntos_mapa;
        this.cant_puntos = this.puntos_all.length;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/recorridos-evacuacion').then((response) => {
        return response.json();
    }).then((json) => {
        this.recorridos_mapa = json.recorridos;
        this.recorridos_all = this.recorridos_mapa;
        this.cant_recorridos = this.recorridos_all.length;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/configuration-publica/').then((response) => {
        return response.json();
    }).then((json) => {
        this.rows_per_page = json.rows_per_page;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/?pagina='+this.page_puntos).then((response) => {
        return response.json();
      }).then((json) => {
          this.puntos_list = json.puntos_encuentro;
      }).catch((e) => {
          console.log(e)
      }),
      fetch(process.env.VUE_APP_ROOT_API+'/recorridos-evacuacion/?pagina='+this.page_recorridos).then((response) => {
        return response.json();
      }).then((json) => {
          this.recorridos_list = json.recorridos;
      }).catch((e) => {
          console.log(e)
      })
  },
  methods:{
    showPunto(row){
      this.recorridos_mapa = [];
      this.puntos_mapa = [row];
    },
    showRecorrido(row){
      this.recorridos_mapa = [row];
      this.puntos_mapa = [];
    },
    showAll(){
      this.recorridos_mapa = this.recorridos_all;
      this.puntos_mapa = this.puntos_all;
    },
    newItemsPuntos(){
      fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/?pagina='+this.page_puntos).then((response) => {
        return response.json();
      }).then((json) => {
          this.puntos_list = json.puntos_encuentro;
      }).catch((e) => {
          console.log(e)
      })
    },
    newItemsRecorridos(){
      fetch(process.env.VUE_APP_ROOT_API+'/recorridos-evacuacion/?pagina='+this.page_recorridos).then((response) => {
        return response.json();
      }).then((json) => {
          this.recorridos_list = json.recorridos;
      }).catch((e) => {
          console.log(e)
      })
    }
  }
};
</script>
<style scoped>
.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
</style>