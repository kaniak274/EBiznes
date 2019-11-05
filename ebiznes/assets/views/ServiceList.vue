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
                        :expanded="true">
                        <option>{{ $t('service.options.all') }}</option>
                        <option>{{ $t('service.options.more1') }}</option>
                        <option>{{ $t('service.options.more2') }}</option>
                        <option>{{ $t('service.options.more3') }}</option>
                        <option>{{ $t('service.options.more4') }}</option>
                        <option>{{ $t('service.options.five') }}</option>
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
        }
    },

    methods: {
        ...mapActions(['loadServicePage']),
        search: async function() {
            const { citySearch, professionSearch } = this;
            let params = new URLSearchParams();
            params.append('city', citySearch);
            params.append('profession', professionSearch);

            await this.loadServicePage(`/api/services/services/?${params.toString()}`);
        }
    },
}
</script>
