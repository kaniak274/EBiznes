export default {
    authorizationGranted: ({ token }) => !!token,
    getErrors: state => property => {
        const { [property]: value = [] } = state.errors;
        return value;
    },

    hasError: ({ errors }) => Object.keys(errors).length,

    csrfToken: state => {
        var cookieValue = null;

        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');

            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, 'csrftoken'.length + 1) === ('csrftoken=')) {
                    cookieValue = decodeURIComponent(cookie.substring('csrftoken'.length + 1));
                    break;
                }
            }
        }

        return {
            headers: {
                'X-CSRFToken': cookieValue,
            },
        }
    },
}
