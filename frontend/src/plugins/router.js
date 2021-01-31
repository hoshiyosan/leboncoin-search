import Vue from 'vue'
import VueRouter from 'vue-router'


import Anounces from '@/views/Anounces'
import Favorites from '@/views/Favorites'
import Locations from '@/views/Locations'

Vue.use(VueRouter)

const routes = [
  {
    path: '/anounces/:anounceUid?',
    name: 'Anounces',
    component: Anounces
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites
  },
  {
    path: '/locations',
    name: 'Locations',
    component: Locations
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
