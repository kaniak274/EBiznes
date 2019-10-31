<template>
    <div>
        Register

        <form method="POST" onSubmit="return false">
            <input
                type="text"
                class="form-control"
                placeholder="Login"
                autocomplete="on"
                v-model="username">

            <errors property='username' />

            <input
                type="password"
                class="form-control"
                placeholder="Password"
                autocomplete="on"
                v-model="password1">

            <errors property='password1' />

            <input
                type="password"
                class="form-control"
                placeholder="Confirm password"
                autocomplete="on"
                v-model="password2">

            <errors property='password2' />

            <input
                type="email"
                class="form-control"
                placeholder="E-mail"
                autocomplete="on"
                v-model="email">

            <errors property='email' />
            <errors property='non_field_errors' />

            <button @click="register" class="btn btn-primary mt-2">Register</button>
        </form>
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
