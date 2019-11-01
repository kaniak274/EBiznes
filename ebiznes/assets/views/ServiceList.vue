<template>
    <div>
        <div class="row">
            <div class="col-4">
                <b-field>
                    <b-input
                        icon="search"
                        :placeholder="$t('service.cityLabel')"
                        v-model="citySearch"
                        @input="search"/>
                </b-field>
            </div>
            <div class="col-4">
                <b-field>
                    <b-input
                        icon="search"
                        :placeholder="$t('service.serviceLabel')"
                        v-model="professionSearch"
                        @input="search"/>
                </b-field>
            </div>
            <div class="col-4">
                
            </div>
        </div>
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

    data () {
        return {
            citySearch: '',
            professionSearch: '',
        }
    },

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
        search: function() {
            const { citySearch, professionSearch } = this;
            let params = new URLSearchParams();
            params.append('city', citySearch);
            params.append('profession', professionSearch);

            this.loadServicePage(`/api/services/services/?${params.toString()}`);
        }
    },

    mounted: function() {
        this.loadServicePage();
    },
}
</script>
