<template>
    <div id="ServiceEdit">
        <service-form
            :isCreate="false"/>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'ServiceEdit',

    data() {
        return {
            service: {},
        }
    },

    mounted() {
        axios.get(`/api/services/services/${this.$route.params.id}`)
        .then(({ data }) => {
            this.service = data;
        })
        .catch(error => {
            const { response: { data }} = error;
            this.$store.commit('setError', data);
        })
    },
}
</script>
