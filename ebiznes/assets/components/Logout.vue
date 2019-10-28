<template>
    <div>
        <button class="btn btn-danger" @click="logout">Logout</button>
    </div>
</template>
<script>
import { mapActions } from 'vuex';

export default {
    name: 'Logout',
    methods: {
        ...mapActions({
            'logoutUser': 'logout',
        }),
        logout: function() {
            this.logoutUser();
        },
    },
}
</script>
