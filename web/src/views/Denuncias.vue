<template>
  <div class="denuncias">
    <Map v-bind:denuncias="denuncias"/>
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
export default {
  name: 'Puntos',
  components:{
    Map
  },
  data() {
    return {
    denuncias : []
    };
  },
  created() {
    fetch('http://localhost:5000/api/denuncias/').then((response) => {
        return response.json();
    }).then((json) => {
        this.denuncias = json.denuncias;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>