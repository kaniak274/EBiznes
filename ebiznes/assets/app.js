import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './App.vue';
import router from './router.js';
import store from './store/index'

import Logout from './components/Logout';
import Errors from './components/Errors';

/* Import of file with all translations */
import i18n from './translations';

/* Import Buefy and used components */
import 'buefy/dist/buefy.css'
import {
    Button,
    Field,
    Input,
} from 'buefy'

import './styles/main.scss';

Vue.use(Toastr);
Vue.use(Field);
Vue.use(Input);
Vue.use(Button);

Vue.component('errors', Errors);
Vue.component('logout', Logout);

var app = new Vue({
    el: '#app',
    i18n,
    store,
    router,
    render: h => h(App)
});

