<template>
  <div class="p-4">
    <div class="denuncias" style="display:flex">
      <Map v-bind:denuncias="denuncias_mapa"/>
      <div class="card overflow-auto" style="height:75vh; width:30% ">
        <router-link class="btn btn-info" to="/denunciar" aria-current="page">Crear denuncia</router-link>
        <div v-if="all">
          <div class="card-header">
            <h3>Denuncias
              <button @click="showAll()" class="btn btn-secondary" style="float:right">Mostrar todas</button>
            </h3>
          </div>
          <div class="card-body">
            <div v-for="row in denuncias_list" v-bind:key="row" style="margin-bottom:2%">
                <vue-collapsible-panel :expanded="false" @click="show(row)">
                  <template #title>
                      {{row.titulo}}
                  </template>
                  <template #content>
                      Descripcion: {{row.descripcion}}<br>
                      Iniciada el día: {{row.fecha_inicio}}
                  </template>
                </vue-collapsible-panel>
            </div>
            <Pagination v-model="page" :records="cant" :per-page="rows_per_page" @paginate="newItems" :options="options"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Pagination from 'v-pagination-3';
import Map from '@/components/Map.vue';
import {
  VueCollapsiblePanel,
} from '@dafcoe/vue-collapsible-panel'
import '@dafcoe/vue-collapsible-panel/dist/vue-collapsible-panel.css'
export default {
  name: 'Denuncias',
  components:{
    Map,
    VueCollapsiblePanel,
    Pagination
  },
  data() {
    return {
      all : [],
      denuncias_mapa : [],
      denuncias_list : [],
      page : 1,
      cant : '',
      rows_per_page: '',
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
    fetch(process.env.VUE_APP_ROOT_API+'/configuration-publica/').then((response) => {
        return response.json();
    }).then((json) => {
        this.rows_per_page = json.rows_per_page;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/denuncias/').then((response) => {
        return response.json();
    }).then((json) => {
        this.all = json.denuncias;
        this.denuncias_mapa = json.denuncias;
        this.cant = this.all.length
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/denuncias/?pagina='+this.page).then((response) => {
        return response.json();
    }).then((json) => {
        this.denuncias_list = json.denuncias;
    }).catch((e) => {
        console.log(e)
    })
  },
  methods:{
    show(row){
      this.denuncias_mapa = [row];
    },
    showAll(){
      this.denuncias_mapa = this.all;
    },
    newItems(){
      fetch(process.env.VUE_APP_ROOT_API+'/denuncias/?pagina='+this.page).then((response) => {
        return response.json();
      }).then((json) => {
          this.denuncias_list = json.denuncias;
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