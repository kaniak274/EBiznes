export default {
    authorizationGranted: ({ token }) => !!token,
    getErrors: state => property => {
        const { [property]: value = [] } = state.errors;
        return value;
    },

    hasError: ({ errors }) => Object.keys(errors).length,

    hasFieldError: ({ errors }) => property => {
        const { [property]: value = [] } = errors;

        return value.length !== 0;
    },

    axiosConfig: ({ token }) => {
        return {
            headers: {
                'Authorization': `JWT ${token}`
            },
        };
    },

    axiosConfigFileForm: ({ token }) => {
        return {
            headers: {
                'Authorization': `JWT ${token}`,
                'Content-Type': 'multipart/form-data',
            },
        };
    },

    services: ({ services }) => services,

    shouldDisplayNavbar: state => routeName => {
        return routeName !== 'login' && routeName !== 'register'
    },

    shouldShowCookieModal: ({ cookieAccepted }) => {
        return !cookieAccepted;
    },

    professionName: ({ service }) => {
        if (service.profession) {
            return service.profession.name;
        } else {
            return '';
        }
    },
}
