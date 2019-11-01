<template>
    <div>
        <div class="row">
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
                <b-field>
                    <b-input
                        icon="search"
                        :placeholder="$t('service.cityLabel')"
                        v-model="citySearch"
                        @input="search"/>
                </b-field>
            </div>
            <div class="col-4">
                
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
