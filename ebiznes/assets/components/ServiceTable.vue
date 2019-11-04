<template>
    <div>
        <b-loading :active.sync="isLoading"/>

        <div class="grid-start">
            <div class="service-grid" v-for="service in services.results" :key="service.id">
                <div class="logo">
                    <!-- TODO EMPTY IMAGE -->
                    <img
                        class="img-fluid rounded"
                        :src="service.service_logo"/>
                </div>
                <div class="name">
                    <router-link
                        v-if="isAll"
                        :to="{ name: 'service-details', params: { id: `${service.pk}` }}"
                        >{{ service.name }}</router-link>
                    <router-link
                        v-else
                        :to="{ name: 'service-edit', params: { id: `${service.pk}` }}"
                        >{{ service.name }}</router-link>
                </div>
                <div class="info">
                    <div class="profession">
                        {{ $t('service.serviceLabel') }}: {{ service.profession.name }}
                    </div>
                    <div class="city">
                        {{ $t('service.cityLabel') }}: {{ service.city }}
                    </div>
                </div>  
                <div class="rating">
                    Rating
                </div>
            </div>
        </div>

        <div class="float-right">
            <button v-if="services.previous" class="btn btn-light" @click="loadPrevious">Previous</button>
            <button v-if="services.next" class="btn btn-light" @click="loadNext">Next</button>
        </div>
    </div>
</template>
<script>
import { mapActions, mapState } from 'vuex';

export default {
    name: 'ServiceList',

    props: {
        isAll: Boolean,
        url: String,
    },

    computed: {
        ...mapState({
            services: state => state.services,
            isLoading: state => state.isLoading,
        }),
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
        (this.url !== null) ? this.loadServicePage(this.url) : this.loadServicePage();
    },

    destroyed: function() {
        this.$store.commit('clearServices');
    },
}
</script>

