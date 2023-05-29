import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login/Login.vue')
    },
    {
      path: '/sign-up',
      name: 'sign-up',
      component: () => import('../views/Sign-Up/Sign-Up.vue')
    },
    {
      path: '/air-rep',
      name: 'air-rep',
      component: () => import('../views/admin/Air-Rep.vue')
    }
  ]
})

export default router
