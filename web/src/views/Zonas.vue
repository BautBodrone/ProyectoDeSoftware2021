<template>
  <div class="zonas" style="display:flex">
    <Map v-bind:zonas="zonas"/>
    <div style="width:40%;margin-top:1%">
    <div v-if="zonas">
        <b>Zonas:</b>
        <div v-for="row in all" v-bind:key="row" style="margin-bottom:2%">
            <label>{{row.nombre}}</label>
            <button @click="show(row)">Show</button>
        </div>
        <button @click="showAll()">Show All</button>  
    </div>
    </div>
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
export default {
  name: 'Zonas',
  components:{
    Map
  },
  data() {
    return {
      all : [],
      zonas : []
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/zonas-inundables/').then((response) => {
        return response.json();
    }).then((json) => {
        this.all = json.zonas;
        this.zonas = json.zonas;
    }).catch((e) => {
        console.log(e)
    })
  },
  methods:{
    show(row){
      this.zonas = [row];
    },
    showAll(){
      this.zonas = this.all;
    }
  }
};
</script>
<style scoped>
div{
    text-align: left;
    margin-bottom:2%
}
button{
    float:right
}
</style>