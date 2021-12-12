<template>
  <div class="p-4">
    <div class="zonas" style="display:flex">
      <Map v-bind:zonas="zonas"/>
      <div class="card overflow-auto" style="height:75vh; width:30% ">
        <div v-if="zonas">
          <div class="card-header">
            <h3>Zonas
            <button @click="showAll()">Show All</button>
            </h3>
          </div>
          <div class="card-body">
            <div v-for="row in all" v-bind:key="row" style="margin-bottom:2%">
                <label>{{row.nombre}}</label>
                <button @click="show(row)">Show</button>
            </div>
             
          </div> 
        </div>
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