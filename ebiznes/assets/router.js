import Vue from 'vue';
import Router from 'vue-router';

import store from './store';

import Home from './views/Home';
import Register from './views/Register';
import Login from './views/Login';
import ServiceList from './views/ServiceList';
import ServiceDetails from './views/ServiceDetails';
import Services from './components/Services';
import ServiceCreate from './views/ServiceCreate';

Vue.use(Router)

const checkLogged = async (to, from, next) => {
    await Vue.nextTick();
    const { getters: { authorizationGranted } } = store;

    if (authorizationGranted) {
        next({ name: 'home', replace: true });
    } else {
        next();
    }
}

const checkNotLogged = async (to, from, next) => {
    await Vue.nextTick();
    const { getters: { authorizationGranted } } = store;

    if (authorizationGranted) {
        next();
    } else {
        next({ name: 'login', replace: true });
    }
}

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '',
            name: 'home',
            component: Home
        },
        {
            path: '/register/',
            name: 'register',
            component: Register,
            beforeEnter: checkLogged,
        },
        {
            path: '/login/',
            name: 'login',
            component: Login,
            beforeEnter: checkLogged,
        },
        {
            path: '/services/',
            component: Services,
            children: [
                {
                    path: '',
                    name: 'service-list',
                    component: ServiceList,
                },
                {
                    path: ':id/',
                    name: 'service-details',
                    component: ServiceDetails,
                },
                {
                    path: 'create/',
                    name: 'service-create',
                    component: ServiceCreate,
                    beforeEnter: checkNotLogged,
                },
            ],
        },
    ],
});

router.beforeEach((to, from, next) => {
    const { state: { errors } } = store;

    if (errors.length != 0) {
        store.commit('clearErrors');
    }

    next();
});

export default router;

