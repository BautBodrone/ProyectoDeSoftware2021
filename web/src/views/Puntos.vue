<template>
  <div class="puntos">
    <Map v-bind:puntos="puntos"/>
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
    puntos : []
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/puntos-encuentro/').then((response) => {
        return response.json();
    }).then((json) => {
        this.puntos = json.puntos_encuentro;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>