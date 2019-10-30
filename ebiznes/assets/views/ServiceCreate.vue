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

        <!-- TODO: ADD SELECT OR AUTOCOMPLETE INPUT -->
        <input
            type="text"
            class="form-control"
            placeholder="Service type"
            v-model="profession_id">
        <errors property='profession_id' />
        <errors property='non_field_errors' />

        <button @click="addService" class="btn btn-primary mt-2">Create</button>
    </div>
</template>
<script>
import { mapActions } from 'vuex';

export default {
    name: 'ServiceCreate',
    data () {
         return {
             name: '',
             description: '',
             city: '',
             profession_id: '',
         }
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
        }
    },
}
</script>
