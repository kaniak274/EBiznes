<template>
    <div>
        <service-table
            :isAll="false"
            :url="getUrl()"/>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
    name: 'UserServices',

    computed: {
        ...mapState({
            user: state => state.user,
        }),
    },

    methods: {
        getUrl: function() {
            return `/api/services/services/?owner=${this.user.pk}`
        },
    },
}
</script>
