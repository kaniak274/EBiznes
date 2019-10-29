<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Profession</th>
                    <th>City</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="service in services.results" :key="service.id">
                    <td>{{ service.name }}</td>
                    <td>{{ service.profession.name }}</td>
                    <td>{{ service.city }}</td>
                    <td><router-link :to="{ name: 'service-details', params: { id: `${service.pk}` }}">More info</router-link></td>
                </tr>
            </tbody>
        </table>

        <button v-if="services.previous" class="btn btn-light" @click="loadPrevious">Previous</button>
        <button v-if="services.next" class="btn btn-light" @click="loadNext">Next</button>
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
        ...mapActions(['loadServicePage']),
        loadPrevious: function() {
            this.loadServicePage(this.services.previous);
        },
        loadNext: function() {
            this.loadServicePage(this.services.next);
        },
    },
    mounted: function() {
        this.loadServicePage();
    },
}
</script>
