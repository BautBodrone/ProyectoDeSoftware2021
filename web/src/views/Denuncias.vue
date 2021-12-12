<template>
  <div class="p-4">
    <div class="denuncias" style="display:flex">
      <Map v-bind:denuncias="denuncias"/>
      <div class="card overflow-auto" style="height:75vh; width:30% ">
        <div v-if="denuncias">
          <div class="card-header">
            <h3>Denuncias</h3>
          </div>
          <div class="card-body">
            <div v-for="row in all" v-bind:key="row" style="margin-bottom:2%">
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
  name: 'Denuncias',
  components:{
    Map,
    VueCollapsiblePanel
  },
  data() {
    return {
      all : [],
      denuncias : []
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/denuncias/').then((response) => {
        return response.json();
    }).then((json) => {
        this.all = json.denuncias;
        this.denuncias = json.denuncias;
    }).catch((e) => {
        console.log(e)
    })
  },
  methods:{
    show(row){
      this.denuncias = [row];
    },
    showAll(){
      this.denuncias = this.all;
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