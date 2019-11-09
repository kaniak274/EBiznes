<template>
    <div class="rent-container">
        <b-button
            v-if="authorizationGranted"
            @click="showModal = true"
            type="is-primary is-medium">
            {{ $t('service.rentBtn') }}
        </b-button>

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

export default {
    name: 'Rent',

    data () {
        return {
            phone_number: '',
            showModal: false,
            address: '',
        }
    },
    
    computed: {
        ...mapGetters(['authorizationGranted', 'axiosConfig']),

        ...mapState({
            user: state => state.user,
        }),
    }, 

    methods: {
        close: function() {
            this.showModal = false;
        },

        send: function() {
            const { $route: { params: { id }}, phone_number, address } = this;

            const payload = { phone_number, address };

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
