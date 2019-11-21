<template>
    <div id="ServiceEdit">
        <service-form
            :isCreate="false"/>

        <div class="container-fluid">
            <div class="price-list">
                <header>
                    <h1>{{ $t('service.priceListHeader') }}</h1>
                </header>

                <div
                    class="price-list-added"
                    v-for="price in service.price_list"
                    :key="price.pk">
                    <div class="row">
                        <div class="col-3 offset-2">
                            <b-field>
                                <b-input
                                    v-model="price.name"
                                    :placeholder="$t('service.priceListName')"/>
                            </b-field>
                        </div>
                        <div class="col-3">
                            <b-field>
                                <b-input
                                    v-model="price.price"
                                    :placeholder="$t('service.priceListPrice')"/>
                            </b-field>
                        </div>
                        <div class="col-1">
                            <b-button
                                type="is-primary"
                                expanded
                                @click="change(price.pk)">
                                {{ $t('service.priceListChange') }}
                            </b-button>
                        </div>
                        <div class="col-1">
                            <b-button
                                type="is-primary"
                                expanded
                                @click="remove(price.pk)">
                                {{ $t('service.priceListRemove') }}
                            </b-button>
                        </div>
                    </div>
                </div>

                <div class="add-new">
                    <div class="row">
                        <div class="col-3 offset-2">
                            <b-field>
                                <b-input
                                    v-model="newName"
                                    :placeholder="$t('service.priceListName')"/>
                            </b-field>
                        </div>
                        <div class="col-3">
                            <b-field>
                                <b-input
                                    v-model="newPrice"
                                    :placeholder="$t('service.priceListPrice')"/>
                            </b-field>
                        </div>
                        <div class="col-1">
                            <b-button
                                type="is-primary"
                                expanded
                                @click="add">
                                {{ $t('service.priceListAdd') }}
                            </b-button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'ServiceEdit',

    data() {
        return {
            service: {},
            newPrice: '',
            newName: '',
        }
    },

    computed: {
        ...mapGetters(['axiosConfig',]),
    },

    methods: {
        change: async function(pk) {
            const { service: { price_list = [] }, axiosConfig } = this;
            const { price, name } = price_list.find(price => price.pk === pk);

            await axios.put(
                `/api/services/price-list/update/${pk}/`,
                { price, name, service: this.$route.params.id },
                axiosConfig
            ).then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.priceChanged'),
                    type: 'is-success',
                    position: 'is-top',
                });
            }).catch(error => {
                const { response: { data: { price = [], service = [], name = []} }} = error;

                price.push.apply(price, service);
                price.push.apply(price, name);

                this.$toastr.e(price.join(' '));
            });
        },

        remove: async function(pk) {
            const { axiosConfig } = this;

            await axios.delete(
                `/api/services/price-list/remove/${pk}/`,
                axiosConfig
            ).then(result => {
                this.service.price_list = this.service.price_list
                    .filter(price => price.pk !== pk);

                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.priceRemoved'),
                    type: 'is-success',
                    position: 'is-top',
                });
            }).catch(error => {
                const { response: { data }} = error;
                this.$toastr.e(data);
            });
        },

        add: async function() {
            const { axiosConfig, newPrice, newName } = this;

            await axios.post(
                `/api/services/price-list/`,
                {
                    price: newPrice,
                    name: newName,
                    service: this.$route.params.id
                },
                axiosConfig
            ).then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.priceAdded'),
                    type: 'is-success',
                    position: 'is-top',
                });

                this.service.price_list.push(result.data);
                this.newPrice = '';
                this.newName = '';
            }).catch(error => {
                const { response: { data: { price = [], service = [], name = []} }} = error;

                price.push.apply(price, service);
                price.push.apply(price, name);

                this.$toastr.e(price.join(' '));
            });
        },
    },

    mounted() {
        axios.get(`/api/services/services/${this.$route.params.id}`)
        .then(({ data }) => {
            this.service = data;
        })
        .catch(error => {
            const { response: { data }} = error;
            this.$store.commit('setError', data);
        })
    },
}
</script>
