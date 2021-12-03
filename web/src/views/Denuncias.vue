<template>
  <div class="denuncias">
    <Map v-bind:denuncias="denuncias"/>
  </div>
  <div class="max-w-xl mx-auto px-4">
    <div class="rounded-lg shadow-lg p-4">
      <p> TEST </p>
    </div>
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
    fetch(process.env.VUE_APP_ROOT_API+'/denuncias/').then((response) => {
        return response.json();
    }).then((json) => {
        this.denuncias = json.denuncias;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>