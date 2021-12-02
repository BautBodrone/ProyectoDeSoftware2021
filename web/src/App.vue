<template>
  <img alt="Vue logo" src="@/assets/logo.png" style="height:5rem;float:left;padding-top:30px;margin-left:1%">  
  <div id="nav">
    <h1 class=header> Inicio </h1>
  </div>
  <div class="navbar">
    <router-link to="/">Inicio</router-link>
    <router-link to="/denuncias">Ver denuncias</router-link>
    <router-link to="/denunciar">Denunciar</router-link>
    <router-link to="/zonas-inundables">Zonas inundables</router-link>
    <router-link to="/puntos-de-encuentro">Puntos de encuentros</router-link> 
    <router-link to="/recorridos">Recorridos</router-link>
  </div>
  <router-view/>
</template>

<style>
.navbar a {
  margin-bottom:1rem;
  text-decoration: none;
  font-size: 1em;
  display: block;
  width: 100%;
  height: 3.5em;
  background-color: beige;
}
.navbar {
  font-family: 'Montserrat', sans-serif;
  float: left;
  width: 15%;
  padding-left: 1%;
  padding-top: 1%;
  padding-right: 1%;
  margin-bottom: 1em;
  margin-top: 1em;
  text-align: left;
  transition: 0.5s;
  overflow-x: hidden;
  white-space: nowrap;
  background-color: rgba(0, 128, 128, 0.178);
}

.navbar a.router-link-exact-active {
  background-color: #428db9;
}

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.header {
  text-align: center;
  font-size: 30px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  background-color: rgba(0, 128, 128, 0.185);
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

</style>
