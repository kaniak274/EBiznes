import axios from 'axios';
import Toastr from 'vue-toastr';

import router from './../router';

export default {
    register({ commit }, payload) {
        const { username, password1, password2, email } = payload;

        axios.post('/rest-auth/registration/', {
            username,
            password1,
            password2,
            email,
        })
        .then(({ data }) => {
            commit('setUser', data)
            router.push({ name: 'home' });
        })
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })
    },
    login({ commit }, payload) {
        const { username, password } = payload;

        axios.post('/rest-auth/login/', {
            username,
            password,
        })
        .then(({ data }) => {
            commit('setUser', data)
            router.push({ name: 'home' });
        })
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })
    },
    logout({ commit }) {
        axios.post('/rest-auth/logout/')
        .then(response => commit('logout'))
        .catch(({ data }) => Toastr.e(data))
    },
    loadServicePage({ commit }, url = '/api/services/services/') {
        axios.get(url)
        .then(({ data }) => commit('setServices', data))
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })
    },
}
