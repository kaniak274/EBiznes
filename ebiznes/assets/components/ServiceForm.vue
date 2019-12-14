<template>
    <div id="ServiceForm">
        <div class="container-fluid">
            <b-loading :active.sync="isLoading"/>

            <form method="POST" onSubmit="return false">
                <div class="row mb-5 header">
                    <div class="col-12 text-center">
                        <h1 v-if="isCreate">{{ $t("service.createHeader") }}</h1>
                        <h1 v-else>{{ $t("service.editHeader") }}</h1>
                    </div>
                </div>
                <div class="row">
                    <div class="col-4 mx-auto">
                        <b-field
                            :type="{ 'is-danger': hasFieldError('name') }"
                            class="mb-4">
                            <b-input
                                :placeholder="$t('service.nameLabel')"
                                v-model="name"/>
                        </b-field>

                        <errors property='name'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('description') }"
                            class="mb-4">
                            <b-input
                                :placeholder="$t('service.descriptionLabel')"
                                type="textarea"
                                v-model="description"/>
                        </b-field>

                        <errors property='description'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('city') }"
                            style="margin-bottom: 2.3em;">
                            <b-input
                                :placeholder="$t('service.cityLabel')"
                                v-model="city"/>
                        </b-field>

                        <errors property='city'/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('profession_id') }">
                            <b-autocomplete
                                :placeholder="$t('service.serviceLabel')"
                                :open-on-focus="true"
                                :data="filteredProfessions"
                                field="name"
                                @select="option => professionId = (option || {'pk': ''}).pk"
                                v-model="professionSelect"/>
                        </b-field>

                        <errors property='profession_id'/>
                        <errors property='non_field_errors'/>

                        <b-button
                            v-if="isCreate"
                            type="is-primary is-medium"
                            @click="addService">
                            {{ $t('service.createBtn') }}
                        </b-button>
 
                        <b-button
                            v-else
                            type="is-primary is-medium"
                            @click="edit">
                            {{ $t('service.editBtn') }}
                        </b-button>
                    </div>
                    <div class="col-4 mx-auto">
                        <b-field
                            :type="{ 'is-danger': hasFieldError('service_logo') }">
                            <b-upload
                                @input="swapImage"
                                v-model="logo" drag-drop>
                                <img v-if="imageURL" :src="imageURL"/>

                                <section class="section" v-else>
                                    <div class="content has-text-centered">
                                        <p>
                                            <b-icon
                                                icon="upload"
                                                size="is-large"/>
                                        </p>
                                        <p>{{ $t("service.logoText") }}</p>
                                    </div>
                                </section>
                            </b-upload>
                        </b-field>
                        
                        <errors property="service_logo"/>

                        <b-field
                            :type="{ 'is-danger': hasFieldError('street') }">
                            <b-input
                                :placeholder="$t('service.streetLabel')"
                                v-model="street"/>
                        </b-field>

                        <errors property="street"/>

                        <b-field
                           :type="{ 'is-danger': hasFieldError('phone_number') }">
                            <b-input
                                :placeholder="$t('service.phoneLabel')"
                                v-model="phoneNumber"/>
                        </b-field>

                        <errors property="phone_number"/>

                        <b-field
                           :type="{ 'is-danger': hasFieldError('account_number') }">
                            <b-input
                                placeholder="Numer konta"
                                v-model="accountNumber"/>
                        </b-field>

                        <errors property="account_number"/>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';
import axios from 'axios';

export default {
    name: 'ServiceForm',

    data () {
         return {
             name: '',
             description: '',
             city: '',
             professionId: '',
             professions: [],
             professionSelect: '',
             logo: null,
             phoneNumber: '',
             street: '',
             imageURL: null,
             accountNumber: '',
         }
    },

    computed: {
        filteredProfessions() {
            return this.professions.filter(profession =>
                profession.name.toLowerCase().includes(this.professionSelect.toLowerCase())
            );
        },

        ...mapGetters(['hasFieldError']),

        ...mapState({
            isLoading: state => state.isLoading,
        }),
    },

    props: {
        isCreate: {
            type: Boolean,
            default: true,
        },
    },

    methods: {
        ...mapActions(['createService', 'editService']),

        loadFormData: function() {
            const {
                name,
                description,
                city,
                professionId,
                logo,
                phoneNumber,
                street,
                accountNumber
            } = this;

            let formData = new FormData();

            if (logo !== null) {
                formData.append('service_logo', logo)
            }

            formData.append('name', name);
            formData.append('description', description);
            formData.append('profession_id', professionId);
            formData.append('phone_number', phoneNumber);
            formData.append('city', city);
            formData.append('street', street);
            formData.append('account_number', accountNumber);

            return formData;
        },

        addService: function() {
            this.createService(this.loadFormData());
        },

        edit: function() {
            this.$store.commit('clearErrors');
            const data = this.loadFormData();
            const id = this.$route.params.id;

            // Show snackbar after success, do nothing here on failure.
            this.editService({ id, data })
            .then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('service.editSuccess'),
                    type: 'is-success',
                    position: 'is-top',
                });
            })
            .catch(error => {});
        },

        swapImage: function(file) {
            this.imageURL = URL.createObjectURL(file);
        },
    },

    mounted() {
        axios.get('/api/services/professions/')
        .then(({ data }) => {
            this.professions = data;
        })
        .catch(error => {
            const { response: { data }} = error;
            this.$toastr.e(data);
        })

        if (!this.isCreate) {
            axios.get(`/api/services/services/${this.$route.params.id}`)
            .then(({ data }) => {
                const { city, name, description, profession, street, phone_number, service_logo } = data;

                this.city = city;
                this.name = name;
                this.description = description;
                this.professionId = profession.pk;
                this.professionSelect = profession.name;
                this.street = street;
                this.phoneNumber = phone_number;
                this.imageURL = service_logo;
                this.accountNumber = data.account_number;
                console.log(data)
                var logo = this.logo

                var request = new XMLHttpRequest();
                request.open('GET', service_logo, true);
                request.responseType = 'blob';

                request.onload = function() {
                    var reader = new FileReader();
                    reader.readAsDataURL(request.response);

                    reader.onload = ({ target: { result }}) => logo = result;
                };
                request.send();
            })
            .catch(error => {
                const { response: { data }} = error;
                this.$toastr.e(data);
            })
        }
    },
}
</script>
