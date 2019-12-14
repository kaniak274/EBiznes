<template>
    <p>{{ getErrors(this.property).join(' ') }}</p>
</template>
<script>
import { mapGetters } from 'vuex';

export default {
    name: 'Errors',
    props: {
        'property': String,
    },
    computed: {
        ...mapGetters([
            'getErrors',
        ]),
    },
}
</script>
