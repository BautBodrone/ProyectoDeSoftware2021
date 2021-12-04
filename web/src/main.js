import {createApp} from 'vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import App from './App.vue'
import router from './router'

// Optional, since every component import their Bootstrap funcionality
// the following line is not necessary
// import 'bootstrap'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import 'leaflet/dist/leaflet.css'

export default {
  components: {},
  methods: {
    // Validator function
    isRequired(value) {
      return value ? true : 'This field is required';
    },
  },
}

createApp(App).use(router,BootstrapVue3).mount('#app')