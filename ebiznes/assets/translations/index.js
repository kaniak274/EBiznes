import Vue from 'vue';
import VueI18n from 'vue-i18n';

import { message_en } from './en/message';
import { service_en } from './en/service';
import { navbar_en } from './en/navbar';
import { rent_en } from './en/rent';

import { message_pl } from './pl/message';
import { service_pl } from './pl/service';
import { navbar_pl } from './pl/navbar';
import { rent_pl } from './pl/rent';



Vue.use(VueI18n);

const i18n = new VueI18n({
    locale: 'pl',
    messages: {
        en: {
            message: message_en,
            service: service_en,
            navbar: navbar_en, 
            rent: rent_en,
        },
        pl: {
            message: message_pl,
            service: service_pl,
            navbar: navbar_pl,
            rent: rent_pl, 
        },
    },
});


export default i18n;
