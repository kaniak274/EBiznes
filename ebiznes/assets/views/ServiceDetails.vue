<template>
    <div>
        {{ service.name }},
        {{ service.description }},
        {{ service.owner }},
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
    name: 'ServiceDetails',
    computed: {
        ...mapState({
            service: state => state.service,
        }),
    },
    methods: {
        ...mapActions(['loadSingleService']),
    },
    created() {
        this.loadSingleService(this.$route.params.id);
    },
}
</script>
