<template>
    <div>
        Login

        <input
            type="text"
            class="form-control"
            placeholder="Login"
            v-model="username">

        <errors property='username' />

        <input
            type="password"
            class="form-control"
            placeholder="Password"
            v-model="password">

        <errors property='password' />
        <errors property='non_field_errors' />
        
        <button @click="login" class="btn btn-primary mt-2">Login</button>
    </div>
</template>
<script>
import { mapActions } from 'vuex';

export default {
    name: 'Login',
    data () {
        return {
            username: '',
            password: '',
        }
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
