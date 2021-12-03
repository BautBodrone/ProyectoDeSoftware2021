<template>
  <div class="puntos">
    <Map v-bind:recorridos="recorridos"/>
  </div>
</template>
<script>
import Map from '@/components/Map.vue';
export default {
  name: 'Recorridos',
  components:{
    Map
  },
  data() {
    return {
    recorridos : []
    };
  },
  created() {
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

