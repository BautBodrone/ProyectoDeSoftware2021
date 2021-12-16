<template>
  <header class="top-bar spread">
    <nav class="navbar navbar-expand-sm navbar-light" id="navbar" :style="{ 'background-color': accent_color }">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <img alt="Vue logo" src="@/assets/logo.png" width="100" height="100"> 
          <ul class="navbar-nav my-2 my-lg-0 me-sm-0 my-sm-0">
            <li class="nav-item">
              <router-link class="nav-link active" to="/" aria-current="page">Inicio</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/denuncias" aria-current="page">Denuncias</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/zonas-inundables" aria-current="page">Zonas</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/puntos-de-encuentro" aria-current="page">Puntos y Recorridos</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" to="/denunciar" aria-current="page">Denunciar</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <body :style="{ 'background-color': bg_color, 'color': color }"> 
    <router-view > </router-view>
  </body>
  <footer style="position:static;display:inline-block;text-align:center;width:100%"> Proyecto de software - Grupo 33 ©</footer>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      rows_per_page: Number,
      bg_color: String,
      accent_color: String,
      color: String,
      order:'' 
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
    })
    .catch((e) => {
        console.log(e)
    })
  }
};
</script>
<style scoped>
.navbar-expand-sm .navbar-collapse{
  display: block;
  text-align: center;
}
</style>
<style>
div{
  text-align: left;
}
button{
  float:right
}
.card{
  height:75vh; 
  width:30%;
  overflow: auto;
}
.mapa{
  padding-left:1%; 
  padding-right:1%; 
  display:flex;
  width:70%;
  border-radius:10px;
}
.map{
  border-radius: 10px;
}
.content{
  flex-direction: column;
  width: 100%;
}
@media screen and ( max-width:768px)  {
  .mapa{
    display:block;
    width:100%;
    height: 60vh;
  }
  .p-4{
    flex-direction: column;
    width: 100%;
  }
  .card{
    height: 100%;
    width: 100%;
    overflow: visible;
  }
}
</style>