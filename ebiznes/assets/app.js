import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './App.vue';
import router from './router.js';
import store from './store/index'

import Logout from './components/Logout';
import Errors from './components/Errors';
import ServiceTable from './components/ServiceTable';
import PasswordReset from './components/PasswordReset';
import ServiceForm from './components/ServiceForm';
import Rent from './components/Rent';
import ClientList from './components/ClientList';

/* Import of file with all translations */
import i18n from './translations';

import '@mdi/font/scss/materialdesignicons.scss';

/* Import Buefy and used components */
import 'buefy/dist/buefy.css'
import {
    Button,
    Field,
    Input,
    Autocomplete,
    Upload,
    Icon,
    Loading,
    Navbar,
    Select,
    Rate,
    Modal,
    Checkbox,
    Table,
} from 'buefy'

import './styles/main.scss';

Vue.use(Toastr);
Vue.use(Field);
Vue.use(Input);
Vue.use(Button);
Vue.use(Autocomplete);
Vue.use(Upload);
Vue.use(Icon);
Vue.use(Loading);
Vue.use(Navbar);
Vue.use(Select);
Vue.use(Rate);
Vue.use(Modal);
Vue.use(Checkbox);
Vue.use(Table);

Vue.component('errors', Errors);
Vue.component('logout', Logout);
Vue.component('service-table', ServiceTable);
Vue.component('password-reset', PasswordReset);
Vue.component('service-form', ServiceForm);
Vue.component('rent', Rent);
Vue.component('client-list', ClientList);

import Buefy from 'buefy';

Vue.use(Buefy);

var app = new Vue({
    el: '#app',
    i18n,
    store,
    router,
    render: h => h(App)
});

