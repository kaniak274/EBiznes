<template>
    <div>
        Register
  
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
            v-model="password1">

        <errors property='password1' />

        <input
            type="password"
            class="form-control"
            placeholder="Confirm password"
            v-model="password2">

        <errors property='password2' />

        <input
            type="email"
            class="form-control"
            placeholder="E-mail"
            v-model="email">

        <errors property='email' />
        <errors property='non_field_errors' />

        <button @click="register" class="btn btn-primary mt-2">Register</button>
    </div>
</template>
<script>
import { mapActions } from 'vuex';

export default {
    name: 'Register',
    data () {
        return {
            username: '',
            email: '',
            password1: '',
            password2: '',
        }
    },
    methods: {
        ...mapActions({
            'registerUser': 'register',
        }),
        register: function() {
            const { username, email, password1, password2 } = this;

            this.registerUser({ username, email, password1, password2 });
        },
    },
}
</script>
