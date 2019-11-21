import axios from 'axios';
import Toastr from 'vue-toastr';

import router from './../router';

export default {
    async register({ commit, state }, payload) {
        state.isLoading = true;

        await axios.post('/rest-auth/registration/', payload)
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

        state.isLoading = false;
    },

    async login({ commit, state }, payload) {
        state.isLoading = true;
        const { username, password } = payload;

        await axios.post('/rest-auth/login/', {
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

        state.isLoading = false;
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
            commit('logout');
            router.push({ name: 'login' });
        })
        .catch(error => {
            const { response: { data }} = error;
            commit('setError', data);

            this.loading = false;
        })
    },

    async submitRating({ commit, getters }, payload) {
        this.loading = true;

        await axios.post(
            '/api/services/ratings/',
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

    async checkRating({ getters }, id) {
        return await axios.get(`/api/services/check-rating/${id}/`, getters.axiosConfig);
    },

    async editRating({ commit, getters }, payload) {
        this.loading = true;

        await axios.put(
            `/api/services/ratings/${payload.id}/`,
            payload.data,
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

    async editAccount({ commit, getters }, payload) {
        this.loading = true;

        await axios.put(
            `/rest-auth/user/`,
            payload,
            getters.axiosConfig
        )
        .then(({ data }) => {
            commit('changeUser', data);

            this.loading = false;
            return data;
        })
        .catch(error => {
            const { response: { data }} = error;
            commit('setError', data);

            this.loading = false;
            return Promise.reject(error);
        })
    }
}
