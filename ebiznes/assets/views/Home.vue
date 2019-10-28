<template>
    <div>
        <router-link :to="{ name: 'register' }">Register</router-link>
        <router-link :to="{ name: 'login' }">Login</router-link>
        <router-link :to="{ name: 'service-list' }">Services</router-link>
    </div>
</template>
<script>
export default {
    name: 'Home',
}
</script>
