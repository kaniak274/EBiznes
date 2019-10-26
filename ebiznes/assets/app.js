import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './components/App.vue';
import router from './router.js';

Vue.use(Toastr)

var app = new Vue({
    el: '#app',
    router,
    render: h => h(App)
});

