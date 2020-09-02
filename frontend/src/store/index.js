import Vue from "vue";
import Vuex from "vuex";
import auth from './modules/auth';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        drawer: null
    },
    mutations: {
        SET_DRAWER(state, payload) {
            state.drawer = payload
        },
    },
    actions: {},
    modules: {
        auth
    },
    strict: process.env.NODE_ENV !== 'production'
});