<template>
  <div class="puntos">
    <Map v-bind:puntos="puntos" v-bind:recorridos="recorridos"/>
    <b>Puntos:</b>
    <div v-for="row in puntos" v-bind:key="row">
      <label>{{row.nombre}}</label>
    </div> 
    <b>Recorridos:</b>
    <div v-for="row in recorridos" v-bind:key="row">
      <label>{{row.nombre}}</label>
    </div>  
    <!--<pagination v-model="page" :records=puntos.length :per-page="1" @paginate="myCallback"/>-->
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
//import Pagination from 'v-pagination-3';
export default {
  name: 'Puntos',
  components:{
    Map,
    //Pagination
  },
  data() {
    return {
    puntos : [],
    recorridos : [],
    page: 1
    };
  },
  props: {
    rows_per_page : Number
  },
  method: {
    myCallBack(e){
      alert(e);
    }
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/').then((response) => {
        return response.json();
    }).then((json) => {
        this.puntos = json.puntos_encuentro;
    }).catch((e) => {
        console.log(e)
    }),
    fetch(process.env.VUE_APP_ROOT_API+'/recorridos-evacuacion').then((response) => {
        return response.json();
    }).then((json) => {
        this.recorridos = json.recorridos;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>
<style scoped>
div{
  text-align: center;
}
</style>