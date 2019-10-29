import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './App.vue';
import router from './router.js';
import store from './store/index'

import Logout from './components/Logout';
import Errors from './components/Errors';

/* Import Buefy and used components */
import 'buefy/dist/buefy.css'
import {
    Field,
    Input
} from 'buefy'

Vue.use(Toastr);
Vue.use(Field);
Vue.use(Input);

Vue.component('errors', Errors);
Vue.component('logout', Logout);

var app = new Vue({
    el: '#app',
    store,
    router,
    render: h => h(App)
});

