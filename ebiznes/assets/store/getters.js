export default {
    authorizationGranted: ({ token }) => !!token,
    getErrors: state => property => {
        const { [property]: value = [] } = state.errors;
        return value;
    },
    getAllErrors: state => () => {
        console.log(state.errors)
    }
}
