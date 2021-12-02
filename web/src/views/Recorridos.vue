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
    fetch('http://localhost:5000/api/recorridos-evacuacion/').then((response) => {
        return response.json();
    }).then((json) => {
        this.recorridos = json.recorridos;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>

