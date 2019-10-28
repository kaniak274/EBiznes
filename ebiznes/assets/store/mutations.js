export default {
    setUser(state, { token, user }) {
        state.user = user;
        state.token = token;
    },
    logout(state) {
        state.user = undefined;
        state.token = null;
    },
    setError(state, data) {
        state.errors = data;
    },
    clearErrors(state) {
        state.errors = {};
    },
    setServices(state, results) {
        state.services = results;
    },
}
