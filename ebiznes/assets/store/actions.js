import axios from 'axios';
import Toastr from 'vue-toastr';

import router from './../router';

export default {
    register({ commit }, payload) {
        axios.post('/rest-auth/registration/', payload)
        .then(({ data }) => {
            commit('setUser', data)
            router.push({ name: 'service-list' });
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
        .then((response) => {
            commit('setUser', response.data)
            router.push({ name: 'service-list' });
        })
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })
    },

    logout({ commit, getters }) {
        axios.post('/rest-auth/logout/', {}, getters.axiosConfig)
        .then(response => {
            commit('logout');
            router.push({ name: 'login' });
        })
        .catch(({ data }) => Toastr.e(data))
    },

    async loadServicePage({ commit, state }, url = '/api/services/services/') {
        state.isLoading = true;

        await axios.get(url)
        .then(({ data }) => {
            commit('setServices', data);
        })
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })

        state.isLoading = false;
    },

    loadSingleService({ commit }, pk) {
        axios.get(`/api/services/services/${pk}/`)
        .then(({ data }) => {
            commit('setService', data);
        })
        .catch(error => {
            const { response: {
                data
            }} = error;

            commit('setError', data);
        })
    },

    createService({ commit, getters }, payload) {
        axios.post('/api/services/services/', payload, getters.axiosConfigFileForm)
        .then((response) => {
            router.push({ name: 'service-user' });
        })
        .catch(error => {
            const { response: { data }} = error;
            commit('setError', data);
        })
    },

    async editService({ commit, getters }, payload) {
        this.loading = true;

        await axios.put(
            `/api/services/services/${payload.id}/`,
            payload.data,
            getters.axiosConfigFileForm,
        )
        .then(response => {
            this.loading = false;
            return response;
        })
        .catch(error => {
            const { response: { data }} = error;
            commit('setError', data);

            this.loading = false;
            return Promise.reject(error);
        })
    },

    async changePassword({ commit, getters }, payload) {
        this.loading = true;

        await axios.post(
            `/rest-auth/password/change/`,
            payload,
            getters.axiosConfig,
        )
        .then(response => {
            this.loading = false;
            return response;
        })
        .catch(error => {
            const { response: { data }} = error;
            commit('setError', data);

            this.loading = false;
            return Promise.reject(error);
        })
    },
}
