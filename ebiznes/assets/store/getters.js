export default {
    authorizationGranted: ({ token }) => !!token,
    getErrors: state => property => {
        const { [property]: value = [] } = state.errors;
        return value;
    },

    hasError: ({ errors }) => Object.keys(errors).length,

    axiosConfig: state => {
        return {
            headers: {
                'Authorization': `JWT ${state.token}`
            },
        }
    },
}
