<template>
    <div>
        Login
        <b-field label="Login"
            :type="{ 'is-danger': hasError }">
            <b-input value="Login" v-model="username"></b-input>
        </b-field>

        <errors property='username' />

        <b-field label="Password"
            :type="{ 'is-danger': hasError }">
            <b-input value="Password" type="password" v-model="password"></b-input>
        </b-field>

        <errors property='password' />
        <errors property='non_field_errors' />

        <button @click="login" class="btn btn-primary mt-2">Login</button>
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
