<template>
  <div class="zonas">
    <Map/>
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
    zoom: 10,
    iconWidth: 25,
    iconHeight: 40,
    };
  },
};
</script>