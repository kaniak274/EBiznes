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
    setServices(state, { next, previous, results }) {
        state.services.results = results;
        state.services.next = next;
        state.services.previous = previous;
    },
    setService(state, data) {
        state.service = data;
    }
}
