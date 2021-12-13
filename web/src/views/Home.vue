<template>
  <div class="container p-4" style="display:flex;">
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div class="col" style="display:flex">
        <div class="card">
          <img src="@/assets/puntos_recorridos_info.jpeg" class="card-img-top" alt="recorridos" style="width: 100%;">
          <div class="card-body">
            <h5 class="card-title">Denuncias</h5>
            <p class="card-text"> Se mostraran todas las denuncias con un punto en el mapa. Si se desea selecciona una puede hacerlos desde el listado que se encuentra a la izquierda.</p>
            <router-link class="nav-link active position-absolute bottom-0 start-0" to="/denuncias" aria-current="page">Ir</router-link>
          </div>
        </div>
      </div>
      <div class="col position-relative" style="display:flex">
        <div class="card">
          <img src="@/assets/zonas_info.jpeg" class="card-img-top" alt="zonas" style="width: 100%;">
          <div class="card-body">
            <h5 class="card-title">Zonas</h5>
            <p class="card-text">Se mostraran todas las zonas en el mapa. Si se desea selecciona una puede hacerlos desde el listado que se encuentra a la izquierda. Y si desea visualizarlas todos lo podra hacer presionando Mostrar todas.</p>
            <router-link class="nav-link active position-absolute bottom-0 start-0" to="/zonas-inundables" aria-current="page">Ir</router-link>
          </div>
        </div>
      </div>
      <div class="col position-relative" style="display:flex">
        <div class="card">
          <img src="@/assets/puntos_recorridos_info.jpeg" class="card-img-top" alt="puntos" style="width: 100%;">
          <div class="card-body">
            <h5 class="card-title">Puntos y Recorridos</h5>
            <p class="card-text">Se mostraran todos los puntos y recorridos con un punto en el mapa. Si se desea selecciona una puede hacerlos desde el listado que se encuentra a la izquierda.</p>
            <router-link class="nav-link active position-absolute bottom-0 start-0" to="/puntos-de-encuentro" aria-current="page">Ir</router-link>
          </div>
        </div>
      </div>
      <div class="col position-relative" style="display:flex">
        <div class="card">
          <img src="@/assets/denunciar_info.png" class="card-img-top" alt="denunciar" style="width: 100%;;">
          <div class="card-body">
            <h5 class="card-title">Denunciar</h5>
            <p class="card-text">En caso de que encuentre un problema puede informalo en la seccion "Denunciar" secleccionando en el mapa el punto y llenando la informacion que se muestra a la izquierda.</p>
            <router-link class="nav-link active position-absolute bottom-0 start-0" to="/denunciar" aria-current="page">Ir</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
// @ is an alias to /src

export default {
  name: 'Home'
};

</script>
<style scoped>
  .content {
    text-align: center;
    color: #2e2e2e;
    padding: 1%;
  }
</style>