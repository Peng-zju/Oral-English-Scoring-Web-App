import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "@/components/Login";
import Main from '@/components/Main'
import QueManage from "@/components/QueManage";
import RegionManage from "@/components/RegionManage";

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login'},
  { path: '/login', component: Login },
  { path: '/main',
    component: Main,
    redirect: '/que_manage',
    children: [{ path: '/que_manage', component: QueManage},
              { path: '/region_manage', component: RegionManage}]},
];

const router = new VueRouter({
  routes
});

export default router
