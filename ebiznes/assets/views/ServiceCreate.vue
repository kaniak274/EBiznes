<template>
    <div>
        Create service

        <input
            type="text"
            class="form-control"
            placeholder="Name"
            v-model="name">
        <errors property='name' />

        <textarea
            class="form-control"
            placeholder="Description..."
            v-model="description"></textarea>
        <errors property='description' />

        <input
            type="text"
            class="form-control"
            placeholder="City"
            v-model="city">
        <errors property='city' />

        <b-field label="Service type">
            <b-autocomplete
                v-model="professionSelect"
                :open-on-focus="true"
                :data="filteredProfessions"
                field="name"
                @select="option => profession_id = option.pk" />
        </b-field>
        <errors property='profession_id' />
        <errors property='non_field_errors' />

        <button @click="addService" class="btn btn-primary mt-2">Create</button>
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
