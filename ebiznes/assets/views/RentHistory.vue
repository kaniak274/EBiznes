<template>
    <div class="container-fluid">
        <b-loading :active.sync="isLoading"/>

        <div class="mt-5">
            <b-table
                :data="rents"
                :striped="true"
                v-if="rents.length !== 0">
                <template slot-scope="props">
                    <b-table-column field="service_name" :label="$t('rent.serviceLabel')">
                        {{ props.row.service_name }}
                    </b-table-column>

                    <b-table-column field="status_display" label="Status">
                        {{ props.row.status_display }}
                    </b-table-column>

                    <b-table-column field="address" :label="$t('rent.addressLabel')">
                        {{ props.row.address }}
                    </b-table-column>

                    <b-table-column field="modified" :label="$t('rent.dateLabel')">
                        {{ props.row.modified.split('T')[0] }}
                    </b-table-column>

                    <b-table-column>
                        <b-button
                            v-if="!props.row.is_paid"
                            type="is-primary"
                            tag="router-link"
                            :to="{
                                name: 'payment',
                                params: { id: `${props.row.pk}` }
                            }"
                        >Zapłać</b-button>
                        <span v-else>Zapłacono</span>
                    </b-table-column>
                </template>
            </b-table>
            <div class="text-center" v-else>
                <p>Brak dostępnych danych</p>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { mapGetters, mapState } from 'vuex';

export default {
    name: 'RentHistory',

    data () {
        return {
            rents: [],
            next: null,
            prev: null,
            isLoading: false,
        }
    },

    computed: {
        ...mapGetters(['axiosConfig']),

        ...mapState({
            pk: state => state.user.pk,
        }),
    },

    async created() {
        this.isLoading = true;

        await axios.get(`/api/services/rents/?user=${this.pk}`, this.axiosConfig)
        .then(({ data: { results, previous, next }}) => {
            this.rents = results;
            this.next = next;
            this.prev = previous;
        }).catch((error) => {
            this.$toastr.e(error.response.data);
        })

        this.isLoading = false;
    },
}
</script>
