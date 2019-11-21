<template>
    <div id="YourAccount" class="container-fluid">
        <div class="header">
            <h1>{{ $t('message.editHeader') }}</h1>
        </div>

        <div class="account-form col-5 mx-auto">
            <form method="POST" onSubmit="return false">
                <b-field
                    :type="{ 'is-danger': hasFieldError('username') }">
                    <b-input
                        v-model="username"
                        :placeholder="$t('message.loginLabel')"/>
                </b-field>

                <errors property="username"/>

                <b-field
                    :type="{ 'is-danger': hasFieldError('email') }">
                    <b-input
                        v-model="email"
                        :placeholder="$t('message.emailLabel')"/>
                </b-field>

                <errors property="email"/>

                <b-field
                    :type="{ 'is-danger': hasFieldError('first_name') }">
                    <b-input
                        v-model="first_name"
                        :placeholder="$t('message.firstNameLabel')"/>
                </b-field>

                <errors property="first_name"/>

                <b-field
                    :type="{ 'is-danger': hasFieldError('last_name') }">
                    <b-input
                        v-model="last_name"
                        :placeholder="$t('message.lastNameLabel')"/>
                </b-field>

                <errors property="last_name"/>

                <b-field
                    :type="{ 'is-danger': hasFieldError('phone_number') }">
                    <b-input
                        v-model="phone_number"
                        :placeholder="$t('service.phoneLabel')"/>
                </b-field>

                <errors property="phone_number"/>

                <b-field :type="{ 'is-danger': hasFieldError('address') }">
                    <b-input
                        v-model="address"
                        :placeholder="$t('service.addressLabel')"/>
                </b-field>

                <errors property="address"/>
                <errors property="non_field_errors"/>

                <b-button
                    tag="input"
                    native-type="submit"
                    type="is-primary is-medium"
                    @click="edit"
                    :value="$t('message.edit')"/>
            </form>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapState } from 'vuex';

export default {
    name: 'YourAccount',

    data() {
        return {
            email: '',
            username: '',
            first_name: '',
            last_name: '',
            phone_number: '',
            address: '',
        }
    },

    computed: {
        ...mapState({
            user: state => state.user,
        }),

        ...mapGetters(['hasFieldError']),
    },

    methods: {
        ...mapActions(['editAccount']),

        edit: function() {
            const { email, username, first_name, last_name, phone_number, address } = this;

            const payload = {
                email,
                username,
                first_name,
                last_name,
                phone_number,
                address,
            }

            this.editAccount(payload)
            .then(result => {
                this.$buefy.snackbar.open({
                    duration: 3000,
                    message: this.$t('message.editSuccess'),
                    type: 'is-success',
                    position: 'is-top',
                });
            })
            .catch(error => {});
        },
    },

    created() {
        const { user: {
            email,
            first_name,
            last_name,
            username,
            phone_number,
            address,
        }} = this;

        this.email = email;
        this.first_name = first_name;
        this.last_name = last_name;
        this.username = username;
        this.phone_number = phone_number;
        this.address = address;
    },
}
</script>
