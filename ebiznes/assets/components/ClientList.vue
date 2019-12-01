<template>
    <div class="mt-5">
        <div class="header">
            <h1>Lista klientów</h1>
        </div>

        <b-table
            :data="rents"
            :striped="true"
            ref="table"
            hoverable
            v-if="rents.length !== 0"
            detailed
            detail-key="pk"
            :show-detail-icon="true"
            @details-open="detailsOpened">
            <template slot-scope="props">
                <b-table-column label="Użytkownik">
                    {{ props.row.user.first_name }} {{ props.row.user.last_name }}
                </b-table-column>

                <b-table-column field="status_display" label="Aktualny status">
                    {{ props.row.status_display }}
                </b-table-column>

                <b-table-column field="total_price" label="Koszt">
                    {{ props.row.total_price }} zł
                </b-table-column>

                <b-table-column field="modified" :label="$t('rent.dateLabel')">
                    {{ props.row.modified.split('T')[0] }}
                </b-table-column>
            </template>

            <template slot="detail" slot-scope="props">
                <article class="media">
                    <div class="media-content">
                        <div class="content">
                            <p>
                                <strong>{{ props.row.user.first_name }} {{ props.row.user.last_name }}</strong>
                                <small>@{{ props.row.phone_number }}</small>
                                <br/>
                                {{ props.row.address }}
                                <br/>
                                <br/>
                                <div class="row">
                                    <div class="col-4">
                                        <b-field label="Status">
                                            <b-select
                                                v-model="props.row.status"
                                                expanded>
                                                <option
                                                    v-for="option in options"
                                                    :value="option.value"
                                                    :key="option.value">
                                                    {{ option.display }}
                                                </option>
                                            </b-select>
                                        </b-field>
                                    </div>
                                    <div class="col-4">
                                        <b-field label="Koszt">
                                            <b-input v-model="props.row.total_price"/>
                                        </b-field>
                                    </div>
                                    <div class="col-4 align-bottom change-button">
                                        <b-button
                                            type="is-primary"
                                            expanded
                                            @click="change(props.row.pk)"
                                        >Zmień</b-button>
                                    </div>
                                </div>
                            </p>
                        </div>
                    </div>
                </article>
            </template>
        </b-table>
        <div class="text-center" v-else>
            <p>Brak dostępnych danych</p>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
    name: 'ClientList',

    data () {
        return {
            rents: [],
            next: null,
            pervious: null,
            current_status: '',
            current_price: '',
            options: [
                {
                    'value': 'WAITING_FOR_APPROVAL',
                    'display': 'Oczekuję na zatwierdzenie',
                },
                {
                    'value': 'NOT_APPROVED',
                    'display': 'Nie zatwierdzono'
                },
                {
                    'value': 'APPROVED',
                    'display': 'Zatwierdzone',
                },
                {
                    'value': 'DONE',
                    'display': 'Zakończone',
                }
            ]
        }
    },

    computed: {
        ...mapGetters(['axiosConfig']),
    },

    methods: {
        change: function(pk) {
            
        }
    },

    created() {
        axios.get(`/api/services/rents/?service=${this.$route.params.id}`, this.axiosConfig)
        .then(({ data: { results, previous, next }}) => {
            this.rents = results;
            this.next = next;
            this.prev = previous;
        }).catch((error) => {
            this.$toastr.e(error.response.data);
        })
    },
}
</script>
