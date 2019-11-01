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
                password: 'password',
                forgetPassword: 'I forget password',
                noAccount: 'Don t have an account?',
                registerFromLogin: 'CREATE NEW ONE',
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
                registerFromLogin: 'STWORZ NOWE',
            },
        },
    },
});


export default i18n;
