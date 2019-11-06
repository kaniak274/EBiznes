<template>
    <div id="ServiceList" class="container-fluid">
        <div class="row">
            <div class="col-12 header-section">
                <h1>{{ $t('service.serviceListHeader') }}</h1>
            </div>
        </div>
        <div class="row filters">
            <div class="col-4">
                <b-field>
                    <b-input
                        icon="magnify"
                        :placeholder="$t('service.serviceLabel')"
                        v-model="professionSearch"
                        @input="search"/>
                </b-field>
            </div>
            <div class="col-4">
                <b-field>
                    <b-input
                        icon="magnify"
                        :placeholder="$t('service.cityLabel')"
                        v-model="citySearch"
                        @input="search"/>
                </b-field>
            </div>
            <div class="col-4">
                <b-field>
                    <b-select
                        :placeholder="$t('service.options.all')"
                        :expanded="true"
                        v-model="ratingSearch"
                        @input="search">
                        <option value="all">{{ $t('service.options.all') }}</option>
                        <option value="more_1">{{ $t('service.options.more1') }}</option>
                        <option value="more_2">{{ $t('service.options.more2') }}</option>
                        <option value="more_3">{{ $t('service.options.more3') }}</option>
                        <option value="more_4">{{ $t('service.options.more4') }}</option>
                        <option value="five">{{ $t('service.options.five') }}</option>
                    </b-select>
                </b-field>
            </div>
        </div>

        <service-table
            :url="null"
            :isAll="true"/>
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
            ratingSearch: 'all',
        }
    },

    methods: {
        ...mapActions(['loadServicePage']),
        search: async function() {
            const { citySearch, professionSearch, ratingSearch } = this;
            let params = new URLSearchParams();
            params.append('city', citySearch);
            params.append('profession', professionSearch);
            params.append('rating', ratingSearch);

            await this.loadServicePage(`/api/services/services/?${params.toString()}`);
        }
    },
}
</script>
