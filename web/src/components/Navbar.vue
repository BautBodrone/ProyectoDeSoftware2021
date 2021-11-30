<template>
  <div class="navbar">
      <a href="" class="navbar">Denuncias</a>
      <a href="" class="navbar">Zonas inundables</a>
      <a href="" class="navbar">Puntos de encuentros</a>
  </div>
</template>
<script>
export default {
  name: 'Navbar'
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar a {
  text-decoration: none;
  font-size: 1em;
  display: block;
  width: 100%;
  height: 3.5em;
}
.navbar {
  font-family: 'Montserrat', sans-serif;
  float: left;
  width: 15%;
  padding-left: 1%;
  padding-top: 1%;
  padding-right: 1%;
  margin-bottom: 2em;
  text-align: center;
  transition: 0.5s;
  overflow-x: hidden;
  white-space: nowrap;   
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
</style>
