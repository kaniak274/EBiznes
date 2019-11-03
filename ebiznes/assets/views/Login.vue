<template>
    <div id="Login">
        <div class="container-fluid login-background">
            <div class="row">
                <div class="col-12 nav-section">
                    <dir class="row">
                        <div class="col-6">
                            <div class="logo-col">
                                <h1>Service Rent</h1>
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
                <div class="col-3 login-form mx-auto" v-if="showLogin">
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
                                <router-link to="#" @click.native="reset">
                                    {{ $t('message.forgetPassword') }}
                                </router-link>
                            </div>
                        </div>
                    </form>

                </div>
                <div class="col-3 login-form mx-auto" v-else>
                    <h1> {{ $t("message.resetPage") }} </h1>

                    <password-reset/>

                    <div class="row">
                        <div class="col-12 mt-3">
                            <router-link to="#" @click.native="reset">
                                {{ $t('message.back') }}
                            </router-link>
                        </div>                        
                    </div>
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
            showLogin: true,
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
        },
        reset: function() {
            this.showLogin = !this.showLogin;
            this.$store.commit('clearErrors');
        }
    }
}
</script>
