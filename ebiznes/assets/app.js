import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './App.vue';
import router from './router.js';
import store from './store/index'

import Logout from './components/Logout';
import Errors from './components/Errors';

Vue.use(Toastr);

Vue.component('errors', Errors);
Vue.component('logout', Logout);

var app = new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
});

