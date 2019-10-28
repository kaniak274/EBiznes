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
    loadServicePage({ commit }, page = 1) {
        axios.get(`/api/services/services?page=${page}`)
        .then(({ data }) => {
            const { results } = data;
            commit('setServices', results);
        })
        .catch(error => {
            const { response: { data } } = error;

            commit('setError', data);
        })
    }
}
