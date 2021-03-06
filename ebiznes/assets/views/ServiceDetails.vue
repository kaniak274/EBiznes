<template>
    <div id="ServiceDetails" class="container-fluid">
        <div class="details-container">
            <div class="row">
                <div class="col-3 left-content">
                    <img
                        v-if="service.service_logo"
                        class="img-fluid"
                        :src="service.service_logo"/>
                    <img
                        v-else
                        class="img-fluid"
                        src="../images/placeholder-image.jpg"/> 
                </div>

                <div class="col-9 right-content">
                    <div class="name-container">
                        <h1 class="name">{{ service.name }}</h1>
                        <rent/>
                    </div>

                    <div class="description-container">
                        {{ service.description }}
                    </div>
                </div>
            </div>
        </div>

        <div class="info-container">
            <div class="row">
                <div class="col-4">
                    <div class="rating">
                        <p>{{ $t('service.averageRate') }}</p>

                        <b-rate
                            v-model="service.rate"
                            :disabled="true"
                            :spaced="true"
                            size="is-large"/>
                    </div>
                </div>
                <div class="col-4">
                    <div class="service-type">
                        <h1>{{ $t('service.serviceLabel') }}</h1>
                        <p>{{ professionName }}</p>
                    </div>
                </div>
                <div class="col-4">
                    <div class="contact-info">
                        <h1>{{ $t('service.contact') }}</h1>
                        <p>{{ service.city }}, {{ service.street }}</p>
                        <p>{{ service.phone_number }}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="rating-container">
            <h1>{{ $t('service.comments') }}</h1>

            <div class="user-comments">
                <div v-for="user_rating in service.random_ratings" class="rating">
                    <b-rate
                        v-model="user_rating.rating_value"
                        :disabled="true"
                        :customText="getCustomText(user_rating)"
                        :rtl="true"
                        :spaced="true"
                        size="is-large"/>

                    <p>{{ user_rating.comment }}</p>
                </div>
            </div>

            <b-loading :active.sync="isLoading"/>

            <div class="rating-form" v-if="authorizationGranted">
                <h1 v-if="alreadyCommented">{{ $t('service.yourComment') }}</h1>

                <form method="POST" onSubmit="return false">
                    <b-rate
                        v-model="rating"
                        :rtl="true"
                        :spaced="true"
                        :customeText="$t('service.rating')"
                        size="is-large"/>

                    <errors property="rating"/>

                    <b-field
                        :type="{ 'is-danger': hasFieldError('comment') }">
                        <b-input
                            :placeholder="$t('service.comment')"
                            v-model="comment"
                            max-length="255"
                            type="textarea"/>
                    </b-field>

                    <errors property="comment"/>
                    <errors property="non_field_errors"/>

                    <b-button
                        v-if="!alreadyCommented"
                        type="is-primary is-medium"
                        @click="addRating"
                    >{{ $t('service.submit') }}</b-button>

                    <b-button
                        v-else
                        type="is-primary is-medium"
                        @click="edit"
                    >{{ $t('service.edit') }}</b-button>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import axios from 'axios';

export default {
    name: 'ServiceDetails',

    data () {
        return {
            comment: '',
            rating: 0,
            alreadyCommented: false,
            pk: 0,
        }
    },

    computed: {
        ...mapState({
            service: state => state.service,
            isLoading: state => state.isLoading,
            owner: state => {
                const { user = { 'pk': 0 }} = state;

                return user.pk
            },
        }),

        ...mapGetters([
            'hasFieldError',
            'authorizationGranted',
            'professionName',
        ]),
    },

    methods: {
        ...mapActions([
            'loadSingleService',
            'submitRating',
            'checkRating',
            'editRating',
        ]),

        addRating: function() {
            const { rating, comment, owner } = this;

            const payload = {
                rating,
                comment,
                owner,
                service: this.$route.params.id,
            };

            this.submitRating(payload)
            .then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.ratingSuccess'),
                    type: 'is-success',
                    position: 'is-top',
                })
            })
            .catch(error => {});
        },

        getCustomText: ({ owner_data: { first_name, last_name }, modified }) => {
            return `${first_name} ${last_name} ${modified.split('T')[0]}`;
        },

        edit: function() {
            const { rating, comment, owner, pk } = this;

            const payload = {
                data: {
                    rating,
                    comment,
                    owner,
                    service: this.$route.params.id,
                },
                id: pk,
            };

            this.editRating(payload)
            .then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.ratingSuccess'),
                    type: 'is-success',
                    position: 'is-top',
                })
            })
            .catch(error => {});
        },
    },

    created() {
        window.scrollTo(0, 0);
        this.loadSingleService(this.$route.params.id);

        if (this.authorizationGranted) {
            this.checkRating(this.$route.params.id)
            .then(({ data: { comment, rating_value, pk }}) => {
                this.comment = comment;
                this.rating = rating_value;
                this.alreadyCommented = true;
                this.pk = pk
            })
            .catch(error => {});
        }
    },
}
</script>
