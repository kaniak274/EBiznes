<template>
    <div id="Login">
        <div class="container-fluid login-background">
            <b-loading :active.sync="isLoading"/>
            <div class="row">
                <div class="col-12 nav-section">
                    <dir class="row">
                        <div class="col-6">
                            <div class="logo-col">
                                <img src="../images/logo-bigger.png"/>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="register-col">
                                <p> {{ $t('message.noAccount') }} </p>
                                <router-link
                                    class="link-register" :to="{ name: 'register' }">
                                    {{ $t('message.registerFromLogin') }}
                                </router-link>

                                <router-link
                                    class="link-register ml-3" :to="{ name: 'home' }">
                                    {{ $t('message.homePage') }}
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

                        <b-button
                            type="is-primary is-medium"
                            @click="login"
                            tag="input"
                            native-type="submit"
                            :value="$t('message.loginBtn')" />

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
            <div class="row fixed-bottom text-white ml-2 image-text">
                <p>
                https://www.pexels.com/photo/man-in-green-polo-shirt-3084330/
                Photo by Ekrulila from Pexels
                </p>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';

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
        ...mapState({
            isLoading: state => state.isLoading,
        }),
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
