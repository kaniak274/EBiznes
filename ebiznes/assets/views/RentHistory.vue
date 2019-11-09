<template>
    <div class="container-fluid">
        <b-loading :active.sync="isLoading"/>

        <div class="mt-5">
            <b-table
                :data="rents"
                :columns="columns"
                :striped="true">
                <template slot-scope="props">
                    <b-table-column field="service_name" :label="$t('rent.serviceLabel')">
                        {{ props.row.service_name }}
                    </b-table-column>

                    <b-table-column field="status" label="Status">
                        {{ props.row.status }}
                    </b-table-column>

                    <b-table-column field="address" :label="$t('rent.addressLabel')">
                        {{ props.row.address }}
                    </b-table-column>

                    <b-table-column field="created" :label="$t('rent.dateLabel')">
                        {{ props.row.created.split('T')[0] }}
                    </b-table-column>
                </template>
            </b-table>
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
