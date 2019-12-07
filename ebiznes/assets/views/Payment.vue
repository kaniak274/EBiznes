<template>
    <div id="Payment">
        <b-loading :active.sync="isLoading"/>
        <button type="button" @click="startPayment"></button>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'Payment',

    data () {
        return {
            rent: {},
            isLoading: false,
        }
    },

    methods: {
        startPayment: function() {
            this.isLoading = true;
            const { id } = this.$route.params;

            axios.post(`/api/services/payment/create/${id}/`)
                .then(({ data }) => {
                    this.isLoading = false;

                    window.open(data.redirectURI, '_self')
                })
                .catch(error => {
                    this.isLoading = false;
                    this.$toastr.e(error.response.data)
                })
        },
    },
};
</script>
