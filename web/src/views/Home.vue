<template>
  <div class="home">
    <Navbar/>
    <Map/>
  </div>
</template>
<script>
// @ is an alias to /src
import Navbar from '@/components/Navbar.vue';
import Map from '@/components/Map.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Map
  }
};

</script>
