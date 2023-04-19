import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home-menu',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'Dashboard-menu',
    component: () => import('../views/Dashboard.vue')
  },
  {
    path: '/about',
    name: 'About-menu',
    component: () => import('../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
