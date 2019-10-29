import Vue from 'vue';
import Router from 'vue-router';

import store from './store';

import Home from './views/Home';
import Register from './views/Register';
import Login from './views/Login';
import ServiceList from './views/ServiceList';
import ServiceDetails from './views/ServiceDetails';
import Services from './components/Services';

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        { path: '', name: 'home', component: Home },
        { path: '/register/', name: 'register', component: Register },
        { path: '/login/', name: 'login', component: Login },
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

