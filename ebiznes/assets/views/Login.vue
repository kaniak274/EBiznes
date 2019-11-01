<template>
    <div id="Login">
        <div class="container-fluid login-background">
            <div class="row">
                <div class="col-12 nav-section">
                    <dir class="row">
                        <div class="col-6">
                            <div class="logo-col">
                                <img src="../../assets/images/logo.png" alt="">
                                <h1>Perfect Work</h1>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="register-col">
                                <p> {{ $t('message.noAccount') }} </p>
                                <router-link
                                    class="link-register" to="/register">
                                    {{ $t('message.registerFromLogin') }}
                                </router-link>
                            </div>
                        </div>
                    </dir>
                </div>
            </div>
            <div class="row">
                <div class="col-3 login-form mx-auto">
                    <h1> {{ $t("message.loginPage") }} </h1>
                    <p class="login-text"> {{ $t("message.loginText") }} </p>
                    <form method="POST" onSubmit="return false">
                        <b-field
                            :type="{ 'is-danger': hasError }">
                            <b-input 
                                :placeholder="$t('message.loginLabel')"
                                v-model="username"></b-input>
                        </b-field>

                        <errors property='username' />

                        <b-field 
                            :type="{ 'is-danger': hasError }">
                            <b-input
                                type="password"
                                :placeholder="$t('message.password')"
                                v-model="password"></b-input>
                        </b-field>

                        <errors property='password' />
                        <errors property='non_field_errors' />

                        <b-button type="is-primary is-medium"
                            @click="login">
                            {{ $t('message.loginBtn') }}
                        </b-button>

                        <div class="row">
                            <div class="col-12 mt-3">
                                <router-link
                                    to="/">
                                    {{ $t('message.forgetPassword') }}
                                </router-link>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: '',
        }
    },

    computed: {
        ...mapGetters(['hasError']),
    },

    methods: {
        ...mapActions({
            'loginUser': 'login',
        }),
        login: function() {
            const { username, password } = this;
            this.loginUser({ username, password });
        }
    }
}
</script>
