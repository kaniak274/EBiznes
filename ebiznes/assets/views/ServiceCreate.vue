<template>
    <div id="ServiceCreate">
        <div class="container-fluid">
            <div class="row">
                <div class="col-3 mx-auto">
                    <h1>{{ $t("service.createHeader") }}</h1>

                    <form method="POST" onSubmit="return false">
                        <b-field>
                            <b-input
                                :placeholder="$t('service.nameLabel')"
                                v-model="name"/>
                        </b-field>

                        <errors property='name'/>

                        <b-field>
                            <b-input
                                :placeholder="$t('service.descriptionLabel')"
                                maxlength="200"
                                type="textarea"
                                v-model="description"/>
                        </b-field>

                        <errors property='description'/>

                        <b-field>
                            <b-input
                                :placeholder="$t('service.cityLabel')"
                                v-model="city"/>
                        </b-field>

                        <errors property='city'/>

                        <b-field>
                            <b-autocomplete
                                :placeholder="$t('service.serviceLabel')"
                                :open-on-focus="true"
                                :data="filteredProfessions"
                                field="name"
                                @select="option => profession_id = option.pk"
                                v-model="professionSelect"/>
                        </b-field>

                        <errors property='profession_id'/>
                        <errors property='non_field_errors'/>

                        <b-button
                            type="is-primary is-medium"
                            @click="addService">
                            {{ $t('service.createBtn') }}
                        </b-button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapActions } from 'vuex';
import axios from 'axios';

export default {
    name: 'ServiceCreate',

    data () {
         return {
             name: '',
             description: '',
             city: '',
             profession_id: '',
             professions: [],
             professionSelect: '',
         }
    },

    computed: {
        filteredProfessions() {
            return this.professions.filter(profession =>
                profession.name.toLowerCase().includes(this.professionSelect.toLowerCase())
            );
        },
    },

    methods: {
        ...mapActions(['createService']),
        addService: function() {
            const { name, description, city, profession_id } = this;

            this.createService({
                name,
                description,
                city,
                profession_id
            });
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
    },
}
</script>
