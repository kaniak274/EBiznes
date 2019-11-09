<template>
    <div id="YourAccount" class="container-fluid">
        <b-loading :active.sync="isLoading"/>

        <div class="header">
            <h1>{{ $t('message.passwordChangeHeader') }}</h1>
        </div>

        <div class="row">
            <div class="account-form col-5 mx-auto">
                <form method="POST" onSubmit="return false">
                    <b-field
                        :type="{ 'is-danger': hasFieldError('new_password1') }">
                        <b-input
                            type="password"
                            :placeholder="$t('message.newPassword1')"
                            v-model="new_password1"/>
                    </b-field>

                    <errors property="new_password1"/>

                    <b-field
                        :type="{ 'is-danger': hasFieldError('new_password2') }">
                        <b-input
                            type="password"
                            :placeholder="$t('message.newPassword2')"
                            v-model="new_password2"/>
                    </b-field>

                    <errors property="new_password2"/>

                    <b-field
                        :type="{ 'is-danger': hasFieldError('old_password') }">
                        <b-input
                            type="password"
                            :placeholder="$t('message.oldPassword')"
                            v-model="old_password"/>
                    </b-field>

                    <errors property="old_password"/>
                    <errors property="non_field_errors"/>

                    <b-button
                        type="is-primary is-medium"
                        @click="change">
                        {{ $t('message.changePasswordBtn') }}
                    </b-button>
                    <p>{{ $t('message.passwordChangeMessage') }}</p>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';

export default {
    name: 'PasswordChange',

    data() {
        return {
            new_password1: '',
            new_password2: '',
            old_password: '',
        }
    },

    computed: {
        ...mapGetters(['hasFieldError']),

        ...mapState({
            isLoading: state => state.isLoading,
        }),
    },

    methods: {
        ...mapActions(['changePassword']),

        change: function() {
            this.$store.commit('clearErrors');

            const { new_password1, new_password2, old_password } = this;

            this.changePassword({ new_password1, new_password2, old_password})
        }
    },
}
</script>
