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
import UserServices from './views/UserServices';
import ServiceEdit from './views/ServiceEdit';
import PasswordChange from './views/PasswordChange';
import YourAccount from './views/YourAccount';
import Privacy from './views/Privacy';
import RentHistory from './views/RentHistory';
import About from './views/About';

Vue.use(Router)

const checkLogged = async (to, from, next) => {
    await Vue.nextTick();
    const { getters: { authorizationGranted } } = store;

    if (authorizationGranted) {
        next({ name: 'service-list', replace: true });
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

const goToList = async (to, from, next) => {
    await Vue.nextTick();
    next({ name: 'service-list', replace: true });
}

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '',
            name: 'home',
            component: Home,
            beforeEnter: goToList,
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
            path: '/password-change/',
            name: 'password-change',
            component: PasswordChange,
            beforeEnter: checkNotLogged,
        },
        {
            path: '/your-account/',
            name: 'your-account',
            component: YourAccount,
            beforeEnter: checkNotLogged,
        },
        {
            path: '/privacy/',
            name: 'privacy',
            component: Privacy,
        },
        {
            path: '/rent-history/',
            name: 'rent-history',
            component: RentHistory,
            beforeEnter: checkNotLogged,
        },
        {
            path: '/about/',
            name: 'about',
            component: About,
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
                    path: 'detail/:id/',
                    name: 'service-details',
                    component: ServiceDetails,
                },
                {
                    path: 'create/',
                    name: 'service-create',
                    component: ServiceCreate,
                    beforeEnter: checkNotLogged,
                },
                {
                    path: 'your-services/',
                    name: 'service-user',
                    component: UserServices,
                    beforeEnter: checkNotLogged,
                },
                {
                    path: 'edit/:id/',
                    name: 'service-edit',
                    component: ServiceEdit,
                    beforeEnter: checkNotLogged,
                },
            ],
        },
    ],
});

router.beforeEach((to, from, next) => {
    const { state: { errors }} = store;

    if (errors.length != 0) {
        store.commit('clearErrors');
    }

    next();
});

export default router;

