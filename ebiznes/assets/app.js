import Vue from 'vue';
import Toastr from 'vue-toastr';

import App from './App.vue';
import router from './router.js';
import store from './store/index'

import Logout from './components/Logout';
import Errors from './components/Errors';

/* Import of file with all translations */
import i18n from './translations';

/* Fontawesome */
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUpload, faExclamationCircle } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

/* Import Buefy and used components */
import 'buefy/dist/buefy.css'
import {
    Button,
    Field,
    Input,
    Autocomplete,
    Upload,
    Icon,
} from 'buefy'

import './styles/main.scss';

Vue.use(Toastr);
Vue.use(Field);
Vue.use(Input);
Vue.use(Button);
Vue.use(Autocomplete);
Vue.use(Upload);
Vue.use(Icon);

Vue.component('errors', Errors);
Vue.component('logout', Logout);

library.add(faUpload, faExclamationCircle)

Vue.component('vue-fontawesome', FontAwesomeIcon)

import Buefy from 'buefy';
Vue.use(Buefy, {
    defaultIconComponent: 'vue-fontawesome',
    defaultIconPack: 'fas',
});

var app = new Vue({
    el: '#app',
    i18n,
    store,
    router,
    render: h => h(App)
});

