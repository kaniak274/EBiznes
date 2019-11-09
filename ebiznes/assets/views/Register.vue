<template>
    <div id="Register">
        <div class="container-fluid register-background">
            <div class="row">
                <div class="col-12 nav-section">
                    <div class="row">
                        <div class="col-6">
                            <div class="logo-col">
                                <h1>Service Rent</h1>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="register-col">
                                <p>{{ $t('message.haveAccount') }}</p>
                                <router-link
                                    class="link-register"
                                    :to="{ name: 'login' }">
                                    {{ $t('message.loginLink') }}
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-3 register-form mx-auto">
                    <h1>{{ $t('message.registerPage') }}</h1>
                    <p class="register-text">{{ $t('message.registerText') }}</p>
                    <form method="POST" onSubmit="return false">
                        <b-field
                            :type="{ 'is-danger': hasFieldError('username') }">
                            <b-input
                                :placeholder="$t('message.loginLabel')"
                                v-model="username"/>
                        </b-field>

                        <errors property='username'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('password1') }">
                            <b-input
                                type="password"
                                :placeholder="$t('message.password')"
                                v-model="password1"/>
                        </b-field>

                        <errors property='password1'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('password2') }">
                            <b-input
                                type="password"
                                :placeholder="$t('message.password2Label')"
                                v-model="password2"/>
                        </b-field>

                        <errors property='password2'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('email') }">
                            <b-input
                                :placeholder="$t('message.emailLabel')"
                                v-model="email"/>
                        </b-field>

                        <errors property='email'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('first_name') }">
                            <b-input
                                :placeholder="$t('message.firstNameLabel')"
                                v-model="first_name"/>
                        </b-field>

                        <errors property='first_name'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('last_name') }">
                            <b-input
                                :placeholder="$t('message.lastNameLabel')"
                                v-model="last_name"/>
                        </b-field>

                        <errors property='last_name'/>
                        <errors property='non_field_errors'/>

                        <p v-html="$t('message.privacyMessage')"></p>

                        <b-button
                            type="is-primary is-medium"
                            @click="register">
                            {{ $t('message.registerBtn') }}
                        </b-button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'Register',

    data () {
        return {
            username: '',
            email: '',
            password1: '',
            password2: '',
            first_name: '',
            last_name: '',
        }
    },

    computed: {
        ...mapGetters(['hasFieldError']),
    },

    methods: {
        ...mapActions({
            'registerUser': 'register',
        }),

        register: function() {
            const { username, email, password1, password2, first_name, last_name } = this;

            this.registerUser({ username, email, password1, password2, first_name, last_name });
        },
    },
}
</script>
