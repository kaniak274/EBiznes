<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Profession</th>
                    <th>City</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="service in services" :key="service.id">
                    <td>{{ service.name }}</td>
                    <td>{{ service.profession.name }}</td>
                    <td>{{ service.city }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
    name: 'ServiceList',
    computed: {
        ...mapState({
            services: state => state.services,
        })
    },
    methods: {
        ...mapActions(['loadServicePage'])
    },
    mounted: function() {
        this.loadServicePage();
    },
}
</script>
