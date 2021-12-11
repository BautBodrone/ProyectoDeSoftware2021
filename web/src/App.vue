<template>
  <header class="top-bar spread">
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;" >
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <img alt="Vue logo" src="@/assets/logo.png" width="100" height="100"> 
          <ul class="navbar-nav my-2 my-lg-0 me-sm-0 my-sm-0">
            <li class="nav-item">
              <router-link class="nav-link active" to="/" aria-current="page">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/denuncias" aria-current="page">Ver denuncias</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/zonas-inundables" aria-current="page">Zonas Inundables</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/puntos-de-encuentro" aria-current="page">Puntos de encuentro</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/denunciar" aria-current="page">Generar denuncia</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <router-view/>
  <label style="text-align:center;width:100%">Proyecto de software - Grupo 33 ©</label>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      rows_per_page: Number,
      bg_color: String,
      accent_color: String,
      color: String  
    };
  },
  created() {
    fetch(process.env.VUE_APP_ROOT_API+'/configuration-publica/').then((response) => {
        return response.json();
    }).then((json) => {
        this.rows_per_page = json.rows_per_page;
        this.order = json.order;
        this.bg_color = json.public_bg_color;
        this.accent_color = json.public_accent_color;
        this.color = json.public_letters_color;
    }).catch((e) => {
        console.log(e)
    })
  }
};
</script>
