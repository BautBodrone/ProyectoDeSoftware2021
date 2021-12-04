<template>
  <div class="zonas">
    <Map v-bind:zonas="zonas"/>
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