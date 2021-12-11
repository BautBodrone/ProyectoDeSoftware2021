import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/zonas-inundables',
    name: 'Zonas',
    component: () => import('../views/Zonas.vue')
  },
  {
    path: '/puntos-de-encuentro',
    name: 'Puntos',
    component: () => import('../views/Puntos.vue')
  },
  {
    path: '/denunciar',
    name: 'Denunciar',
    component: () => import('../views/Denunciar.vue')
  },
  {
    path: '/denuncias',
    name: 'Denuncias',
    component: () => import('../views/Denuncias.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
