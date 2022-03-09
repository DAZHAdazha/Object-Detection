// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Login from './Login'
import Search from './Search'
import Index from './Index'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
import echarts from "echarts";
import 'jquery'
import Viewer from 'v-viewer';
import 'viewerjs/dist/viewer.css';

Vue.use(Viewer);
Vue.prototype.$echarts = echarts;
Vue.use(Element)
Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$http = axios

const router = new VueRouter({
    routes: [
        {path: "/App", component: App, meta: {title: "Object Detection Yolov5"},},
        {
            path: '/login',
            component: Login
         },
         {
            path: '/search',
            component: Search
         },
         {
            path: '/',
            component: Index
         },
    ],
    mode: "history"
})
Vue.component("App", App);

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    render: h => h(App)
})


