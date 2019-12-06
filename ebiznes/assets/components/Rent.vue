<template>
    <div class="rent-container">
        <b-button
            v-if="authorizationGranted"
            @click="showPriceList = true"
            type="is-primary is-medium">
            {{ $t('service.rentBtn') }}
        </b-button>

        <b-modal
            :active.sync="showPriceList"
            has-modal-card
            trap-focus
            aria-role="dialog"
            aria-modal
            custom-class="price-list-modal">
            <form method="POST" onSubmit="return false">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p
                            class="modal-card-title">
                            Czego potrzebujesz?
                        </p>
                    </header>
                    <section class="modal-card-body">
                        <div
                            v-for="price in service.price_list"
                            :key="price.pk"
                            class="mt-2">
                            <div class="row mb-3">
                                <div class="col-4 text-center">
                                    {{ price.name }}
                                </div>
                                <div class="col-4 text-center">
                                    {{ price.price }}
                                </div>
                                <div class="col-4 text-center">
                                    <b-button
                                        v-if="!isUsed(price.pk)"
                                        type="is-primary"
                                        @click="addPrice(price)"
                                        expanded
                                    >+</b-button>

                                    <b-button
                                        v-else
                                        type="is-primary"
                                        @click="minusPrice(price)"
                                        expanded
                                    >-</b-button>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-12 text-center">
                                Do zaplaty: {{ total_price.toFixed(2) }} zl
                            </div>
                        </div>
                    </section>
                    <footer class="modal-card-foot">
                        <div class="row" style="width: 100%;">
                            <div class="col-6">
                                <button
                                    class="button"
                                    type="button"
                                    @click="closePriceList"
                                >Zamknij</button>
                            </div>

                            <div class="col-6 text-right">
                                <b-button
                                    type="is-primary"
                                    tag="input"
                                    @click="nextStep"
                                    value="Przejdz dalej"/>
                            </div>
                        </div>
                    </footer>
                </div>
            </form>
        </b-modal>

        <b-modal
            :active.sync="showModal"
            has-modal-card
            trap-focus
            aria-role="dialog"
            aria-modal>
            <form method="POST" onSubmit="return false">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">{{ $t('service.rentHeader') }}</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field>
                            <b-input
                                v-model="phone_number"
                                :placeholder="$t('service.phoneLabel')"/>
                        </b-field>

                        <b-field>
                            <b-input
                                v-model="address"
                                :placeholder="$t('service.addressLabel')"/>
                        </b-field>
                    </section>
                    <footer class="modal-card-foot">
                        <button
                            class="button"
                            type="button"
                            @click="close"
                        >{{ $t('service.close') }}</button>
                        <button
                            class="button is-primary"
                            @click="send"
                        >{{ $t('service.rentBtn') }}</button>
                     </footer>
                </div>
            </form>
        </b-modal>
    </div>
</template>
<script>
import axios from 'axios';
import { mapGetters, mapState } from 'vuex';
import { $ as money, add, minus } from 'moneysafe';

export default {
    name: 'Rent',

    data () {
        return {
            phone_number: '',
            showModal: false,
            address: '',
            showPriceList: false,
            total_price: 0,
            prices_used: [],
        }
    },
    
    computed: {
        ...mapGetters(['authorizationGranted', 'axiosConfig']),

        ...mapState({
            user: state => state.user,
            service: state => state.service,
        }),
    }, 

    methods: {
        close: function() {
            this.showModal = false;
        },

        closePriceList: function() {
            this.showPriceList = false;
        },

        nextStep: function() {
            this.showPriceList = false;
            this.showModal = true;
        },

        addPrice: function({ pk, price }) {
            this.total_price = add(
                money(this.total_price),
                money(parseFloat(price))
            );
            this.prices_used.push(pk);
        },

        isUsed: function(pk) {
            return this.prices_used.includes(pk);
        },

        minusPrice: function({ pk, price }) {
            this.total_price = add(
                money(this.total_price),
                money(parseFloat(price) * -1)
            );
            this.prices_used = this.prices_used.filter(item => item !== pk);   
        },

        send: function() {
            const { $route: { params: { id }}, phone_number, address, prices_used } = this;

            const payload = {
                phone_number,
                address,
                price_list: prices_used,
            };

            axios.post(
                `/api/services/services/${id}/rent_service/`,
                payload,
                this.axiosConfig,
            ).then(response => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.rentSuccess'),
                    type: 'is-success',
                    position: 'is-top',
                })
            }).catch(error => {
                this.$toastr.e('Try again later.')
            })
        },
    },

    created() {
        const { user: { phone_number = '', address = '' }} = this;

        this.phone_number = phone_number;
        this.address = address;
    },
}
</script>
