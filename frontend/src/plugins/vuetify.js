import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import CUSTOM_ICONS from "./materialDesignIcons"

Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont: 'mdiSvg',
        values: CUSTOM_ICONS
    },
    theme: {
        options: {
            customProperties: true
        },
        themes: {
            light: {
                primary: '#0d324d',
                secondary: '#7f5a83',
            },
        },
    },
});