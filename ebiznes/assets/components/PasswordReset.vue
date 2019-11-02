<template>
    <div>
        <b-loading :active.sync="isLoading"/>

        <form method="POST" onSubmit="return false">
            <b-field
                :type="{ 'is-danger': hasError }">
                <b-input
                    v-model="email"
                    :placeholder="$t('message.emailLabel')"/>
            </b-field>

            <errors property="email"/>

            <b-button
                type="is-primary is-medium"
                @click="reset">
                {{ $t('message.resetBtn') }}
            </b-button>
        </form>

        <label v-if="success">{{ msg }}</label>
    </div>
</template>
<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'PasswordReset',

    data () {
        return {
            email: '',
            success: false,
            isLoading: false,
            msg: '',
        }
    },

    computed: {
       ...mapGetters(['hasError']),
    },

    methods: {
        reset: async function() {
            this.isLoading = true;

            await axios.post('/rest-auth/password/reset/', { email: this.email })
                .then(({ data }) => {
                this.msg = data.detail;
                this.success = true;
            })
            .catch(error => {
                const { response: { data }} = error;

                this.$store.commit('setError', data);
            })

            this.isLoading = false;
        }
    },
}
</script>
