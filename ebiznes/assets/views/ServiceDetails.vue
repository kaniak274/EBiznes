<template>
    <div id="ServiceDetails">
        {{ service.name }},
        {{ service.description }},
        {{ service.owner }}

        <b-loading :active.sync="isLoading"/>

        <div class="rating-form">
            <form method="POST" onSubmit="return false">
                <b-rate
                    v-model="rating"
                    :rtl="true"
                    :spaced="true"
                    :customeText="$t('service.rating')"/>

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
                    type="is-primary is-medium"
                    @click="addRating"
                >{{ $t('service.submit') }}</b-button>
            </form>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';

export default {
    name: 'ServiceDetails',

    data () {
        return {
            comment: '',
            rating: 0,
        }
    },

    computed: {
        ...mapState({
            service: state => state.service,
            isLoading: state => state.isLoading,
            owner: state => state.user.pk,
        }),

        ...mapGetters(['hasFieldError']),
    },

    methods: {
        ...mapActions([
            'loadSingleService',
            'submitRating',
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
    },

    created() {
        this.loadSingleService(this.$route.params.id);
    },
}
</script>
