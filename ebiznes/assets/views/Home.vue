<template>
    <div>
        <div v-if="!authorizationGranted">
            <router-link :to="{ name: 'register' }">Register</router-link>
            <router-link :to="{ name: 'login' }">Login</router-link>
            <router-link :to="{ name: 'service-list' }">Services</router-link>
        </div>
        <div v-else>
            <logout />
            <router-link :to="{ name: 'service-list' }">Services</router-link>
            <router-link :to="{ name: 'service-create' }">Create service</router-link>
            <router-link :to="{ name: 'service-user' }">Your services</router-link>
            <router-link :to="{ name: 'password-change' }">Change password</router-link>
        </div>
    </div>
</template>
<script>
import { mapGetters } from 'vuex';

export default {
    name: 'Home',

    computed: {
        ...mapGetters(['authorizationGranted']),
    },

    mounted() {
        this.$store.commit('stopLoading');
    },
}
</script>
