<template>
  <div class="zonas">
    <Map v-bind:zonas="zonas"/>
    <table>
      <tr> 
        <th>nombre </th>
        <th> color </th>
      </tr>
      <tr>
        <div v-for="zona in zonas" :key="zona">
          <th>:zona.nombre</th> 
          <th>:zona.color</th>
        </div>
      </tr>
    </table>
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
    zonas : []
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/zonas-inundables/').then((response) => {
        return response.json();
    }).then((json) => {
        this.zonas = json.zonas;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>
<style scoped>
table, tr, td, th {
  border: 1px solid rgb(32, 32, 32);
  text-align: center;
  padding: 8px;
}

table, tr{
  text-align: center;
  border-collapse: collapse;
  min-width: 50%;
  align-content: center;
  table-layout:fixed;
  width: 100%;
  border-collapse: separate;
  border-spacing:  1px;
  overflow: hidden;
}

th , td{
  height: 1%;
}
</style>