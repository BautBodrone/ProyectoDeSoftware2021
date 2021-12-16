<template>
<div class="content">
  <div class="p-4" style="display:flex">
      <Map v-bind:zonas="zonas_mapa"/>
      <div class="card">
        <div v-if="zonas_list"> 
          <div class="card-header">
            <h3>Zonas
            <button @click="showAll()" class="btn btn-secondary">Mostrar todas</button>
            </h3>
          </div>
          <div class="card-body">
            <div v-for="row in zonas_list" v-bind:key="row" style="margin-bottom:5%">
                <label>{{row.nombre}}</label>
                <button @click="show(row)" class="btn btn-info">Mostrar</button>
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
export default {
  name: 'Zonas',
  components:{
    Map,
    Pagination
  },
  data() {
    return {
      all : [],
      zonas_mapa : [],
      zonas_list : [],
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
    fetch(process.env.VUE_APP_ROOT_API+'/zonas-inundables/').then((response) => {
        return response.json();
    }).then((json) => {
        this.all = json.zonas;
        this.zonas_mapa = this.all;
        this.cant = this.all.length;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/zonas-inundables/?pagina='+this.page).then((response) => {
        return response.json();
      }).then((json) => {
          this.zonas_list = json.zonas;
      }).catch((e) => {
          console.log(e)
      })
  },
  methods:{
    show(row){
      this.zonas_mapa = [row];
    },
    showAll(){
      this.zonas_mapa = this.all;
    },
    newItems(){
      fetch(process.env.VUE_APP_ROOT_API+'/zonas-inundables/?pagina='+this.page).then((response) => {
        return response.json();
      }).then((json) => {
          this.zonas_list = json.zonas;
      }).catch((e) => {
          console.log(e)
      })
    }
  }
};
</script>