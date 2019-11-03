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
                emailLabel: 'E-mail',
                resetBtn: 'Reset password',
                back: 'Back',
                resetPage: 'Password reset',
                haveAccount: 'Have an account?',
                loginLink: 'SIGN IN',
                registerPage: 'Sign up',
                registerText: 'Sign up now!',
                password2Label: 'Confirm password',
                registerBtn: 'Sign up',
                firstNameLabel: 'First name',
                lastNameLabel: 'Last name',
            },
            service: {
                createHeader: 'Create your service',
                nameLabel: 'Name',
                descriptionLabel: 'Description',
                cityLabel: 'City',
                serviceLabel: 'Service type',
                createBtn: 'Create service',
                logoText: 'Drop image which shows your service',
                streetLabel: 'Address',
                phoneLabel: 'Phone number',
                editBtn: 'Edit service',
                editSuccess: 'Service has been updated.',
                editHeader: 'Edit service',
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
                emailLabel: 'Adres e-mail',
                resetBtn: 'Zresetuj hasło',
                back: 'Powrót',
                resetPage: 'Reset hasła',
                haveAccount: 'Masz już konto?',
                loginLink: 'ZALOGUJ SIĘ',
                registerPage: 'Rejestracja',
                registerText: 'Zarejestruj się już dziś!',
                password2Label: 'Potwierdź hasło',
                registerBtn: 'Zarejestruj',
                firstNameLabel: 'Imię',
                lastNameLabel: 'Nazwisko',
            },
            service: {
                createHeader: 'Dodaj usługę',
                nameLabel: 'Nazwa',
                descriptionLabel: 'Opis usługi',
                cityLabel: 'Miasto',
                serviceLabel: 'Rodzaj usługi',
                createBtn: 'Dodaj usługę',
                logoText: 'Prześlij obrazek przedstawiający Twoją usługę',
                streetLabel: 'Adres',
                phoneLabel: 'Numer telefonu',
                editBtn: 'Edytuj usługę',
                editSuccess: 'Usługa została zmieniona.',
                editHeader: 'Edycja usługi',
            },
        },
    },
});


export default i18n;
