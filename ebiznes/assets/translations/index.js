import Vue from 'vue';
import VueI18n from 'vue-i18n';


Vue.use(VueI18n);

const i18n = new VueI18n({
    locale: 'pl',
    messages: {
        en: {
            message: {
                loginPage: 'Login page',
                loginLabel: 'User login',
                loginBtn: 'Login in',
                loginText: 'Welcome back. Let s find what do you need.',
                password: 'Password',
                forgetPassword: 'I forget password',
                noAccount: 'Don\'t have an account?',
                registerFromLogin: 'CREATE NEW ONE',
            },
            service: {
                createHeader: 'Create your service',
                nameLabel: 'Name',
                descriptionLabel: 'Description',
                cityLabel: 'City',
                serviceLabel: 'Service type',
                createBtn: 'Create service',
            },
        },
        pl: {
            message: {
                loginPage: 'Logowanie',
                loginLabel: 'Login',
                loginBtn: 'Zaloguj',
                loginText: 'Witaj ponownie. Czas się znaleźć.',
                password: 'Hasło',
                forgetPassword: 'Zapomniałem hasła',
                noAccount: 'Nie masz jeszcze konta?',
                registerFromLogin: 'STWÓRZ NOWE',
            },
            service: {
                createHeader: 'Dodaj usługę',
                nameLabel: 'Nazwa',
                descriptionLabel: 'Opis usługi',
                cityLabel: 'Miasto',
                serviceLabel: 'Rodzaj usługi',
                createBtn: 'Dodaj usługę',
            },
        },
    },
});


export default i18n;
