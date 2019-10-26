import Vue from 'vue';
import Router from 'vue-router';

import PostList from './components/PostList.vue';
import PostAdd from './components/PostAdd.vue';

Vue.use(Router)

const router = new Router({
    mode: 'hash',
    routes: [
        { path: '/', name: 'posts', component: PostList },
        { path: '/add', name: 'post-add', component: PostAdd },
    ],
});

export default router;

